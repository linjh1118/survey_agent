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
        """Search for a paper on arXiv by title"""
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
                # Find the best match using improved scoring
                best_match = None
                best_score = 0
                
                for result in results:
                    result_title_cleaned = self.clean_title(result.title)
                    
                    # Method 1: Word overlap scoring
                    title_words = set(cleaned_title.lower().split())
                    result_words = set(result_title_cleaned.lower().split())
                    
                    if title_words and result_words:
                        overlap = len(title_words.intersection(result_words))
                        overlap_score = overlap / max(len(title_words), len(result_words))
                        
                        # Method 2: Character-level similarity (simple)
                        char_score = len(set(cleaned_title.lower()) & set(result_title_cleaned.lower())) / max(len(set(cleaned_title.lower())), len(set(result_title_cleaned.lower())))
                        
                        # Method 3: Length similarity bonus
                        length_ratio = min(len(cleaned_title), len(result_title_cleaned)) / max(len(cleaned_title), len(result_title_cleaned))
                        
                        # Combined score
                        final_score = overlap_score * 0.7 + char_score * 0.2 + length_ratio * 0.1
                        
                        if final_score > best_score:
                            best_score = final_score
                            best_match = result
                
                # Lower threshold for better recall
                if best_score > 0.25:  # Reduced threshold from 0.3 to 0.25
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
                        print(f"   ❌ 搜索失败: 最高匹配分数 {best_score:.3f} 低于阈值 0.25")
                        if results:
                            print(f"   最佳候选: {results[0].title}")
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