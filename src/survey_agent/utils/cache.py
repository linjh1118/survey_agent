import json
import os
import hashlib
from typing import Dict, Any, Optional
from datetime import datetime, timedelta


class PaperCache:
    """论文摘要缓存管理器"""
    
    def __init__(self, cache_dir: str = "cache", cache_expire_days: int = 30):
        """
        初始化缓存管理器
        
        Args:
            cache_dir: 缓存目录路径
            cache_expire_days: 缓存过期天数，默认30天
        """
        self.cache_dir = cache_dir
        self.cache_expire_days = cache_expire_days
        self.cache_file = os.path.join(cache_dir, "paper_summaries.json")
        
        # 确保缓存目录存在
        os.makedirs(cache_dir, exist_ok=True)
        
        # 加载现有缓存
        self._cache = self._load_cache()
    
    def _load_cache(self) -> Dict[str, Any]:
        """加载缓存文件"""
        if os.path.exists(self.cache_file):
            try:
                with open(self.cache_file, 'r', encoding='utf-8') as f:
                    cache_data = json.load(f)
                
                # 清理过期缓存
                current_time = datetime.now()
                cleaned_cache = {}
                
                for arxiv_id, entry in cache_data.items():
                    cached_time = datetime.fromisoformat(entry.get('cached_at', '1970-01-01'))
                    if current_time - cached_time < timedelta(days=self.cache_expire_days):
                        cleaned_cache[arxiv_id] = entry
                
                # 如果清理了缓存，保存更新后的缓存
                if len(cleaned_cache) != len(cache_data):
                    self._save_cache(cleaned_cache)
                
                return cleaned_cache
                
            except (json.JSONDecodeError, KeyError, ValueError) as e:
                print(f"缓存文件损坏，重新创建: {e}")
                return {}
        
        return {}
    
    def _save_cache(self, cache_data: Dict[str, Any] = None):
        """保存缓存到文件"""
        data_to_save = cache_data if cache_data is not None else self._cache
        try:
            with open(self.cache_file, 'w', encoding='utf-8') as f:
                json.dump(data_to_save, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"保存缓存失败: {e}")
    
    def _extract_arxiv_id(self, paper: Dict[str, Any]) -> Optional[str]:
        """从论文信息中提取arxiv.id"""
        # 尝试从多个可能的字段获取arxiv.id
        arxiv_id = paper.get('arxiv_id')
        if arxiv_id:
            return arxiv_id
        
        # 从URL中提取
        url = paper.get('url', '')
        if 'arxiv.org' in url:
            # 匹配类似 "http://arxiv.org/pdf/2406.09172v2" 的URL
            import re
            match = re.search(r'arxiv\.org/(?:pdf|abs)/(\d+\.\d+)', url)
            if match:
                return match.group(1)
        
        # 从DOI中提取
        doi = paper.get('doi', '')
        if 'arxiv' in doi.lower():
            match = re.search(r'(\d+\.\d+)', doi)
            if match:
                return match.group(1)
        
        return None
    
    def _generate_content_hash(self, paper: Dict[str, Any]) -> str:
        """生成论文内容的哈希值，用于检测内容变化"""
        # 使用标题、摘要和PDF文本的前1000字符生成哈希
        content_parts = [
            paper.get('title', ''),
            paper.get('summary', ''),
            paper.get('pdf_text', '')[:1000]
        ]
        content = ''.join(content_parts)
        return hashlib.md5(content.encode('utf-8')).hexdigest()
    
    def get_cached_summary(self, paper: Dict[str, Any]) -> Optional[str]:
        """
        获取缓存的论文摘要
        
        Args:
            paper: 论文信息字典
            
        Returns:
            缓存的摘要字符串，如果没有缓存则返回None
        """
        arxiv_id = self._extract_arxiv_id(paper)
        if not arxiv_id:
            return None
        
        if arxiv_id in self._cache:
            cached_entry = self._cache[arxiv_id]
            
            # 检查内容是否有变化（可选）
            current_hash = self._generate_content_hash(paper)
            cached_hash = cached_entry.get('content_hash', '')
            
            if current_hash == cached_hash:
                print(f"📁 使用缓存摘要: {paper.get('title', 'Unknown')[:50]}...")
                return cached_entry.get('summary', '')
            else:
                print(f"🔄 论文内容已更新，重新生成摘要: {arxiv_id}")
                # 删除过期缓存
                del self._cache[arxiv_id]
        
        return None
    
    def cache_summary(self, paper: Dict[str, Any], summary: str):
        """
        缓存论文摘要
        
        Args:
            paper: 论文信息字典
            summary: 生成的摘要
        """
        arxiv_id = self._extract_arxiv_id(paper)
        if not arxiv_id or not summary:
            return
        
        cache_entry = {
            'arxiv_id': arxiv_id,
            'title': paper.get('title', ''),
            'summary': summary,
            'content_hash': self._generate_content_hash(paper),
            'cached_at': datetime.now().isoformat(),
            'model_info': {
                'provider': getattr(self, '_last_provider', 'unknown'),
                'model_name': getattr(self, '_last_model', 'unknown')
            }
        }
        
        self._cache[arxiv_id] = cache_entry
        self._save_cache()
        print(f"💾 已缓存摘要: {paper.get('title', 'Unknown')[:50]}... (arxiv:{arxiv_id})")
    
    def set_model_info(self, provider: str, model_name: str):
        """设置当前使用的模型信息，用于缓存记录"""
        self._last_provider = provider
        self._last_model = model_name
    
    def get_cache_stats(self) -> Dict[str, Any]:
        """获取缓存统计信息"""
        return {
            'total_entries': len(self._cache),
            'cache_file': self.cache_file,
            'cache_size_mb': round(os.path.getsize(self.cache_file) / 1024 / 1024, 2) if os.path.exists(self.cache_file) else 0,
            'oldest_entry': min([entry.get('cached_at', '') for entry in self._cache.values()]) if self._cache else None,
            'newest_entry': max([entry.get('cached_at', '') for entry in self._cache.values()]) if self._cache else None
        }
    
    def clear_cache(self):
        """清空所有缓存"""
        self._cache = {}
        self._save_cache()
        print("🗑️  已清空所有缓存")


# 全局缓存实例
_global_cache = None


def get_paper_cache() -> PaperCache:
    """获取全局缓存实例"""
    global _global_cache
    if _global_cache is None:
        _global_cache = PaperCache()
    return _global_cache 