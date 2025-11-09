#!/usr/bin/env python3
"""
生成用于展示的JSON数据文件
将缓存的论文数据转换为静态网页可以使用的格式
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Any

def load_cached_papers() -> Dict[str, Any]:
    """加载所有缓存的论文数据"""
    cache_files = [
        'cache/paper_summaries.json',
        'cache/demo_papers.json',
        'cache/demo_reports.json'
    ]
    
    all_papers = {}
    
    for cache_file in cache_files:
        if os.path.exists(cache_file):
            try:
                with open(cache_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    if isinstance(data, dict):
                        all_papers.update(data)
                        print(f"✅ 已加载 {cache_file}: {len(data)} 篇论文")
                    else:
                        print(f"⚠️  跳过 {cache_file}: 格式不正确")
            except Exception as e:
                print(f"❌ 加载 {cache_file} 失败: {e}")
        else:
            print(f"⚠️  文件不存在: {cache_file}")
    
    return all_papers

def process_papers_for_display(papers_data: Dict[str, Any]) -> List[Dict[str, Any]]:
    """处理论文数据为展示格式"""
    display_papers = []
    
    for arxiv_id, paper_info in papers_data.items():
        # 处理不同的数据结构
        if 'title' in paper_info and 'summary' in paper_info:
            # 标准格式
            processed_paper = {
                'arxiv_id': paper_info.get('arxiv_id', arxiv_id),
                'title': paper_info['title'],
                'summary': paper_info['summary'],
                'cached_at': format_date(paper_info.get('cached_at', '')),
                'content_hash': paper_info.get('content_hash', ''),
                'model_info': paper_info.get('model_info', {'provider': 'unknown', 'model_name': 'unknown'})
            }
            display_papers.append(processed_paper)
        else:
            print(f"⚠️  跳过格式不正确的论文: {arxiv_id}")
    
    # 按缓存时间排序（最新的在前面）
    display_papers.sort(key=lambda x: x['cached_at'], reverse=True)
    
    return display_papers

def format_date(date_str: str) -> str:
    """格式化日期字符串"""
    try:
        if date_str:
            # 尝试解析ISO格式的日期
            dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
            return dt.strftime('%Y-%m-%d %H:%M')
        else:
            return '未知时间'
    except:
        return date_str[:16] if len(date_str) >= 16 else date_str

def generate_display_json():
    """生成用于展示的JSON文件"""
    print("🚀 开始生成展示数据...")
    
    # 加载缓存的论文数据
    papers_data = load_cached_papers()
    print(f"📚 总共加载 {len(papers_data)} 篇论文")
    
    if not papers_data:
        print("❌ 没有找到任何论文数据")
        return
    
    # 处理数据
    display_papers = process_papers_for_display(papers_data)
    print(f"✅ 处理完成 {len(display_papers)} 篇有效论文")
    
    # 生成展示数据
    display_data = {
        'generated_at': datetime.now().isoformat(),
        'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M'),
        'total_papers': len(display_papers),
        'papers': display_papers
    }
    
    # 确保docs目录存在
    os.makedirs('docs', exist_ok=True)
    
    # 写入文件
    output_file = 'docs/papers_display.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(display_data, f, ensure_ascii=False, indent=2)
    
    print(f"🎉 展示数据已生成: {output_file}")
    print(f"📊 统计信息:")
    print(f"   - 论文总数: {display_data['total_papers']}")
    print(f"   - 生成时间: {display_data['last_updated']}")
    
    # 显示一些示例论文信息
    if display_papers:
        print(f"\n📄 示例论文:")
        for i, paper in enumerate(display_papers[:3]):
            print(f"   {i+1}. [{paper['arxiv_id']}] {paper['title'][:60]}...")

if __name__ == '__main__':
    generate_display_json()