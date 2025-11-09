import re
from typing import List, Dict, Any, Optional
from pathlib import Path
import arxiv

class BibParser:
    """Parser for BibTeX files to extract arXiv IDs and other information"""
    
    def __init__(self):
        self.entries = []
        
    def parse_file(self, file_path: str) -> Dict[str, List]:
        """Parse a BibTeX file and return arXiv IDs and entries without arXiv IDs"""
        file_path = Path(file_path)
        if not file_path.exists():
            raise FileNotFoundError(f"BibTeX file not found: {file_path}")
        
        content = file_path.read_text(encoding='utf-8')
        return self.parse_string(content)
    
    def clean_title(self, title: str) -> str:
        """Clean title by removing special BibTeX characters"""
        if not title:
            return ""
        
        # Remove curly braces and other special characters
        cleaned = re.sub(r'[{}]', '', title)
        # Remove colons (important for arXiv search compatibility)
        cleaned = cleaned.replace(':', '')
        # Remove extra whitespace
        cleaned = ' '.join(cleaned.split())
        # Remove special BibTeX commands like \textbackslash
        cleaned = re.sub(r'\\[a-zA-Z]+\s*', '', cleaned)
        # Remove other special characters that might interfere with search
        cleaned = re.sub(r'[^\w\s\-\(\),.!?]', ' ', cleaned)
        # Clean up extra spaces
        cleaned = ' '.join(cleaned.split())
        
        return cleaned.strip()
    
    def parse_string(self, content: str) -> Dict[str, List]:
        """Parse BibTeX content string and return arXiv IDs and entries without arXiv IDs"""
        arxiv_ids = set()  # 使用set去重
        entries_without_arxiv = []
        
        # 移除注释
        content = re.sub(r'%.*?\n', '\n', content)
        
        # 查找所有可能包含arxiv ID的URL
        # 匹配 arxiv.org/abs/XXXX.XXXXX 格式
        url_pattern = r'arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})'
        ids_from_urls = re.findall(url_pattern, content, re.IGNORECASE)
        arxiv_ids.update(ids_from_urls)
        
        # 匹配 arXiv:XXXX.XXXXX 格式
        arxiv_pattern = r'arxiv[:\.](\d{4}\.\d{4,5})'
        ids_from_arxiv = re.findall(arxiv_pattern, content, re.IGNORECASE)
        arxiv_ids.update(ids_from_arxiv)
        
        # 匹配 arXiv preprint arXiv:XXXX.XXXXX 格式
        preprint_pattern = r'arxiv preprint (?:arxiv:)?(\d{4}\.\d{4,5})'
        ids_from_preprint = re.findall(preprint_pattern, content, re.IGNORECASE)
        arxiv_ids.update(ids_from_preprint)
        
        # 匹配DOI中的arXiv格式: 10.48550/arXiv.XXXX.XXXXX
        doi_pattern = r'10\.48550/arxiv\.(\d{4}\.\d{4,5})'
        ids_from_doi = re.findall(doi_pattern, content, re.IGNORECASE)
        arxiv_ids.update(ids_from_doi)
        
        # 匹配 abs/XXXX.XXXXX 格式
        abs_pattern = r'abs/(\d{4}\.\d{4,5})'
        ids_from_abs = re.findall(abs_pattern, content, re.IGNORECASE)
        arxiv_ids.update(ids_from_abs)
        
        # 解析所有BibTeX条目，找出没有arXiv ID的
        # 改进的正则表达式，能够正确匹配嵌套的大括号
        entry_pattern = r'@\w+\s*\{([^,]+),\s*(.*?)\n\}'
        entries = re.findall(entry_pattern, content, re.DOTALL)
        
        for entry_key, entry_content in entries:
            # 检查这个条目是否包含arXiv ID
            has_arxiv = bool(re.search(url_pattern, entry_content, re.IGNORECASE) or
                           re.search(arxiv_pattern, entry_content, re.IGNORECASE) or
                           re.search(preprint_pattern, entry_content, re.IGNORECASE) or
                           re.search(doi_pattern, entry_content, re.IGNORECASE) or
                           re.search(abs_pattern, entry_content, re.IGNORECASE))
            
            if not has_arxiv:
                # 提取标题 - 改进的正则表达式处理嵌套大括号
                title_match = re.search(r'title\s*=\s*\{(.*?)\}(?=\s*,?\s*\w+\s*=|\s*$)', entry_content, re.IGNORECASE | re.DOTALL)
                if title_match:
                    title = title_match.group(1)
                    cleaned_title = self.clean_title(title)
                    
                    # 提取作者（可选） - 同样处理可能的嵌套大括号
                    author_match = re.search(r'author\s*=\s*\{(.*?)\}(?=\s*,?\s*\w+\s*=|\s*$)', entry_content, re.IGNORECASE | re.DOTALL)
                    authors = author_match.group(1) if author_match else ""
                    
                    # 提取年份（可选）
                    year_match = re.search(r'year\s*=\s*\{([^}]+)\}', entry_content, re.IGNORECASE)
                    year = year_match.group(1) if year_match else ""
                    
                    entries_without_arxiv.append({
                        'key': entry_key.strip(),
                        'original_title': title,
                        'cleaned_title': cleaned_title,
                        'authors': authors,
                        'year': year,
                        'full_content': entry_content
                    })
        
        return {
            'arxiv_ids': list(arxiv_ids),
            'entries_without_arxiv': entries_without_arxiv
        }
    
    def search_paper_by_title(self, title: str, verbose: bool = False) -> Optional[Any]:
        """Search for a paper on arXiv by title with strict similarity checking"""
        if not title:
            return None
            
        # Clean title for search
        cleaned_title = self.clean_title(title)
        
        if not cleaned_title:
            return None
        
        if verbose:
            print(f"🔍 标题搜索开始:")
            print(f"   原始标题: {title}")
            print(f"   清理后标题: {cleaned_title}")
            
        try:
            client = arxiv.Client()
            strategy_used = ""
            
            # Strategy 1: Exact title search with quotes
            if verbose:
                print(f"   策略1: 精确标题搜索...")
            search = arxiv.Search(
                query=f'ti:"{cleaned_title}"',
                max_results=15,
                sort_by=arxiv.SortCriterion.Relevance
            )
            
            results = list(client.results(search))
            if results:
                strategy_used = "精确标题匹配"
            
            # Strategy 2: Flexible title search without quotes
            if not results:
                if verbose:
                    print(f"   策略2: 灵活标题搜索...")
                search = arxiv.Search(
                    query=f'ti:{cleaned_title}',
                    max_results=15,
                    sort_by=arxiv.SortCriterion.Relevance
                )
                results = list(client.results(search))
                if results:
                    strategy_used = "灵活标题搜索"
            
            # Strategy 3: Search with key words from title
            if not results:
                if verbose:
                    print(f"   策略3: 关键词组合搜索...")
                # Extract key words (remove common words)
                stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'is', 'are', 'was', 'were', 'been', 'be', 'have', 'has', 'had', 'will', 'would', 'could', 'should'}
                words = cleaned_title.lower().split()
                key_words = [w for w in words if len(w) > 2 and w not in stop_words]
                
                if len(key_words) >= 3:
                    # Use top 5 key words
                    search_terms = ' AND '.join([f'ti:{word}' for word in key_words[:5]])
                    if verbose:
                        print(f"   关键词: {key_words[:5]}")
                    search = arxiv.Search(
                        query=search_terms,
                        max_results=20,
                        sort_by=arxiv.SortCriterion.Relevance
                    )
                    results = list(client.results(search))
                    if results:
                        strategy_used = "关键词组合搜索"
            
            if results:
                # Find the best match using improved scoring with strict similarity checking
                best_match = None
                best_score = 0
                
                for result in results:
                    result_title_cleaned = self.clean_title(result.title)
                    
                    # Calculate multiple similarity metrics
                    similarity_score = self._calculate_title_similarity(cleaned_title, result_title_cleaned)
                    
                    if similarity_score > best_score:
                        best_score = similarity_score
                        best_match = result
                
                # Use stricter threshold and additional checks
                if self._is_title_match_valid(cleaned_title, best_match.title, best_score, verbose):
                    if verbose:
                        print(f"   ✅ 搜索成功 ({strategy_used})")
                        print(f"   找到论文: {best_match.title}")
                        print(f"   匹配分数: {best_score:.3f}")
                        arxiv_id = best_match.entry_id.split('/')[-1].split('v')[0]
                        print(f"   arXiv ID: {arxiv_id}")
                        print()
                    return best_match
                else:
                    if verbose:
                        print(f"   ❌ 搜索失败: 标题相似性检查未通过")
                        print(f"   原始标题: {cleaned_title}")
                        print(f"   搜索到标题: {best_match.title}")
                        print(f"   匹配分数: {best_score:.3f}")
                        print()
            else:
                if verbose:
                    print(f"   ❌ 搜索失败: 未找到任何候选论文")
                    print()
                    
        except Exception as e:
            if verbose:
                print(f"   ❌ 搜索出错: {e}")
                print()
            else:
                print(f"Error searching for paper with title '{title}': {e}")
            
        return None
    
    def _calculate_title_similarity(self, title1: str, title2: str) -> float:
        """Calculate comprehensive similarity score between two titles"""
        if not title1 or not title2:
            return 0.0
        
        # Normalize titles for comparison
        t1 = title1.lower().strip()
        t2 = title2.lower().strip()
        
        # Method 1: Word overlap scoring (most important)
        words1 = set(t1.split())
        words2 = set(t2.split())
        
        if not words1 or not words2:
            return 0.0
        
        overlap = len(words1.intersection(words2))
        word_overlap_score = overlap / max(len(words1), len(words2))
        
        # Method 2: Jaccard similarity for words
        jaccard_score = overlap / len(words1.union(words2)) if words1.union(words2) else 0.0
        
        # Method 3: Character-level similarity (Levenshtein-based approximation)
        char_similarity = self._calculate_char_similarity(t1, t2)
        
        # Method 4: Length similarity (penalize very different lengths)
        length_ratio = min(len(t1), len(t2)) / max(len(t1), len(t2))
        
        # Method 5: Check for exact substring match (bonus)
        substring_bonus = 0.0
        if len(t1) > 10 and len(t2) > 10:  # Only for reasonably long titles
            if t1 in t2 or t2 in t1:
                substring_bonus = 0.2
        
        # Method 6: Check for significant word order preservation
        word_order_score = self._calculate_word_order_similarity(t1, t2)
        
        # Weighted combination
        final_score = (
            word_overlap_score * 0.4 +      # Most important: word overlap
            jaccard_score * 0.2 +           # Word set similarity
            char_similarity * 0.15 +        # Character-level similarity
            length_ratio * 0.1 +            # Length similarity
            substring_bonus +               # Exact substring bonus
            word_order_score * 0.15         # Word order preservation
        )
        
        return min(final_score, 1.0)  # Cap at 1.0
    
    def _calculate_char_similarity(self, s1: str, s2: str) -> float:
        """Calculate character-level similarity using a simple approach"""
        if not s1 or not s2:
            return 0.0
        
        # Simple character overlap
        chars1 = set(s1)
        chars2 = set(s2)
        
        if not chars1 or not chars2:
            return 0.0
        
        overlap = len(chars1.intersection(chars2))
        return overlap / max(len(chars1), len(chars2))
    
    def _calculate_word_order_similarity(self, title1: str, title2: str) -> float:
        """Calculate how well the word order is preserved"""
        words1 = title1.split()
        words2 = title2.split()
        
        if len(words1) < 2 or len(words2) < 2:
            return 0.0
        
        # Find common words and check their relative positions
        common_words = set(words1).intersection(set(words2))
        if len(common_words) < 2:
            return 0.0
        
        # Calculate position correlation for common words
        positions1 = {word: i for i, word in enumerate(words1) if word in common_words}
        positions2 = {word: i for i, word in enumerate(words2) if word in common_words}
        
        # Check if relative order is preserved
        order_preserved = 0
        total_pairs = 0
        
        for word1 in common_words:
            for word2 in common_words:
                if word1 != word2:
                    total_pairs += 1
                    pos1_1, pos1_2 = positions1[word1], positions1[word2]
                    pos2_1, pos2_2 = positions2[word1], positions2[word2]
                    
                    # Check if relative order is the same
                    if (pos1_1 < pos1_2) == (pos2_1 < pos2_2):
                        order_preserved += 1
        
        return order_preserved / total_pairs if total_pairs > 0 else 0.0
    
    def _is_title_match_valid(self, original_title: str, found_title: str, similarity_score: float, verbose: bool = False) -> bool:
        """Determine if a title match is valid based on multiple criteria"""
        
        # Criterion 1: Minimum similarity threshold
        min_similarity_threshold = 0.6  # Increased from 0.4 to 0.6 for stricter matching
        if similarity_score < min_similarity_threshold:
            if verbose:
                print(f"   ❌ 相似性分数 {similarity_score:.3f} 低于阈值 {min_similarity_threshold}")
            return False
        
        # Criterion 2: Check for significant word overlap
        original_words = set(original_title.lower().split())
        found_words = set(found_title.lower().split())
        
        if not original_words or not found_words:
            if verbose:
                print(f"   ❌ 标题为空或无法解析")
            return False
        
        # At least 60% of words should overlap for short titles, 50% for longer titles
        min_word_overlap_ratio = 0.6 if len(original_words) <= 5 else 0.5
        word_overlap_ratio = len(original_words.intersection(found_words)) / max(len(original_words), len(found_words))
        
        if word_overlap_ratio < min_word_overlap_ratio:
            if verbose:
                print(f"   ❌ 词汇重叠比例 {word_overlap_ratio:.3f} 低于阈值 {min_word_overlap_ratio}")
            return False
        
        # Criterion 3: Check for length similarity (avoid very different lengths)
        length_ratio = min(len(original_title), len(found_title)) / max(len(original_title), len(found_title))
        if length_ratio < 0.4:  # If one title is more than 2.5x longer than the other
            if verbose:
                print(f"   ❌ 标题长度差异过大，长度比例: {length_ratio:.3f}")
            return False
        
        # Criterion 4: Check for critical words (important technical terms)
        # Extract potential technical terms (words that are likely important)
        technical_indicators = ['learning', 'network', 'model', 'algorithm', 'method', 'approach', 'system', 'framework', 'deep', 'neural', 'transformer', 'attention', 'reinforcement', 'optimization', 'classification', 'regression', 'clustering', 'detection', 'recognition', 'generation', 'synthesis', 'analysis', 'prediction', 'inference', 'training', 'evaluation', 'benchmark']
        
        original_tech_words = [w for w in original_words if w in technical_indicators]
        found_tech_words = [w for w in found_words if w in technical_indicators]
        
        # If original title has technical terms, most should be present in found title
        if original_tech_words:
            tech_overlap = len(set(original_tech_words).intersection(set(found_tech_words)))
            tech_overlap_ratio = tech_overlap / len(original_tech_words)
            
            if tech_overlap_ratio < 0.8:  # At least 80% of technical terms should match
                if verbose:
                    print(f"   ❌ 技术词汇重叠不足，重叠比例: {tech_overlap_ratio:.3f}")
                    print(f"   原始技术词汇: {original_tech_words}")
                    print(f"   找到的技术词汇: {found_tech_words}")
                return False
        
        # Criterion 5: Check for exact word matches (at least some words should match exactly)
        exact_matches = len(original_words.intersection(found_words))
        min_exact_matches = 3 if len(original_words) <= 5 else 4  # More strict for longer titles
        if exact_matches < min_exact_matches:
            if verbose:
                print(f"   ❌ 精确匹配词汇数量不足: {exact_matches} (需要至少 {min_exact_matches})")
            return False
        
        # All criteria passed
        if verbose:
            print(f"   ✅ 标题匹配验证通过")
            print(f"   相似性分数: {similarity_score:.3f}")
            print(f"   词汇重叠比例: {word_overlap_ratio:.3f}")
            print(f"   长度比例: {length_ratio:.3f}")
            print(f"   精确匹配词汇数: {exact_matches}")
        
        return True
    
    def get_arxiv_papers(self) -> List[Dict[str, Any]]:
        """Get paper objects from arXiv using extracted IDs"""
        try:
            parse_result = self.parse_string(self.content)
            arxiv_ids = parse_result['arxiv_ids']
        except AttributeError:
            return []
        
        client = arxiv.Client()
        papers = []
        
        for arxiv_id in arxiv_ids:
            try:
                # 使用arxiv API获取论文信息
                search = arxiv.Search(id_list=[arxiv_id])
                results = list(client.results(search))
                if results:
                    papers.append(results[0])
            except Exception as e:
                print(f"Error fetching paper {arxiv_id}: {e}")
                continue
        
        return papers

def parse_bib_file(file_path: str) -> List[Dict[str, Any]]:
    """Convenience function to parse a BibTeX file and return paper objects"""
    parser = BibParser()
    content = Path(file_path).read_text(encoding='utf-8')
    parser.content = content
    return parser.get_arxiv_papers() 