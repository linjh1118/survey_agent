import re
from typing import List, Dict, Any
from pathlib import Path
import arxiv

class BibParser:
    """Parser for BibTeX files to extract arXiv IDs"""
    
    def __init__(self):
        self.entries = []
        
    def parse_file(self, file_path: str) -> List[str]:
        """Parse a BibTeX file and return list of arXiv IDs"""
        file_path = Path(file_path)
        if not file_path.exists():
            raise FileNotFoundError(f"BibTeX file not found: {file_path}")
        
        content = file_path.read_text(encoding='utf-8')
        return self.parse_string(content)
    
    def parse_string(self, content: str) -> List[str]:
        """Parse BibTeX content string and return list of arXiv IDs"""
        arxiv_ids = set()  # 使用set去重
        
        # 移除注释
        content = re.sub(r'%.*?\n', '\n', content)
        
        # 查找所有可能包含arxiv ID的URL
        # 匹配 arxiv.org/abs/XXXX.XXXXX 格式
        url_pattern = r'arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})'
        ids_from_urls = re.findall(url_pattern, content, re.IGNORECASE)
        arxiv_ids.update(ids_from_urls)
        
        # 匹配 arXiv:XXXX.XXXXX 格式
        arxiv_pattern = r'arxiv:(\d{4}\.\d{4,5})'
        ids_from_arxiv = re.findall(arxiv_pattern, content, re.IGNORECASE)
        arxiv_ids.update(ids_from_arxiv)
        
        # 匹配 arXiv preprint arXiv:XXXX.XXXXX 格式
        preprint_pattern = r'arxiv preprint (?:arxiv:)?(\d{4}\.\d{4,5})'
        ids_from_preprint = re.findall(preprint_pattern, content, re.IGNORECASE)
        arxiv_ids.update(ids_from_preprint)
        
        return list(arxiv_ids)
    
    def get_arxiv_papers(self) -> List[Dict[str, Any]]:
        """Get paper objects from arXiv using extracted IDs"""
        try:
            arxiv_ids = self.parse_string(self.content)
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