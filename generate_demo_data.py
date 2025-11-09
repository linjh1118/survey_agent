#!/usr/bin/env python3
"""
从实际缓存数据生成GitHub Pages演示数据
"""

import json
import os
from datetime import datetime
from collections import OrderedDict

def load_actual_cache():
    """加载实际的缓存数据"""
    cache_file = "cache/paper_summaries.json"
    if os.path.exists(cache_file):
        with open(cache_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def truncate_summary(summary, max_length=500):
    """截断摘要到指定长度，保持格式"""
    if len(summary) <= max_length:
        return summary
    
    # 尝试在句号处截断
    truncated = summary[:max_length]
    last_period = truncated.rfind('。')
    last_newline = truncated.rfind('\n')
    
    # 优先在句号处截断，其次在换行处
    if last_period > max_length * 0.7:
        truncated = summary[:last_period + 1]
    elif last_newline > max_length * 0.7:
        truncated = summary[:last_newline]
    
    return truncated + "..."

def filter_papers_for_demo(papers_data, max_count=20):
    """筛选用于演示的论文"""
    # 转换为列表并按缓存时间排序
    papers_list = []
    for arxiv_id, paper_info in papers_data.items():
        paper_info['arxiv_id'] = arxiv_id
        papers_list.append(paper_info)
    
    # 按缓存时间排序（最新在前）
    papers_list.sort(key=lambda x: x.get('cached_at', ''), reverse=True)
    
    # 只取前max_count篇
    selected_papers = papers_list[:max_count]
    
    # 转回字典格式，并处理摘要
    demo_data = OrderedDict()
    for paper in selected_papers:
        arxiv_id = paper['arxiv_id']
        # 移除重复的arxiv_id字段
        paper_copy = paper.copy()
        if 'arxiv_id' in paper_copy:
            del paper_copy['arxiv_id']
        
        # 截断摘要以减少文件大小
        if 'summary' in paper_copy:
            paper_copy['summary'] = truncate_summary(paper_copy['summary'])
        
        demo_data[arxiv_id] = paper_copy
    
    return demo_data

def generate_demo_cache():
    """生成演示缓存文件"""
    print("正在加载实际缓存数据...")
    actual_cache = load_actual_cache()
    
    if not actual_cache:
        print("未找到实际缓存数据，将创建最小演示数据...")
        # 创建最小的演示数据
        demo_data = {
            "2506.19767": {
                "title": "SRFT: A Single-Stage Method with Supervised and Reinforcement Fine-Tuning for Reasoning",
                "summary": "## 🌟 论文解读 | SRFT：大语言模型推理微调的创新单阶段方法\n\n### 📌 背景痛点/本文动机\n大语言模型（LLMs）在推理任务中取得了显著进展，但监督微调（SFT）和强化学习（RL）的最佳整合仍是一个根本性挑战...\n\n### 🚀 核心方法\n💡 提出单阶段微调方法SRFT，将SFT整合到RL中，使用熵作为指标来控制两种范式之间的平衡。",
                "content_hash": "c22b21b0970fe44a31634b46a37e2608",
                "cached_at": datetime.now().isoformat(),
                "model_info": {
                    "provider": "doubao",
                    "model_name": "ep-20250529110941-khvtx"
                }
            }
        }
    else:
        print(f"找到 {len(actual_cache)} 篇缓存论文，正在生成演示数据...")
        demo_data = filter_papers_for_demo(actual_cache)
        print(f"选择了 {len(demo_data)} 篇论文用于演示")
    
    # 写入演示文件
    demo_file = "cache/demo_papers.json"
    with open(demo_file, 'w', encoding='utf-8') as f:
        json.dump(demo_data, f, ensure_ascii=False, indent=2)
    
    print(f"演示数据已保存到 {demo_file}")
    print(f"包含 {len(demo_data)} 篇论文")
    
    # 显示统计信息
    if demo_data:
        print("\n论文统计:")
        titles = [paper.get('title', 'Unknown') for paper in demo_data.values()]
        for i, title in enumerate(titles[:5], 1):
            print(f"  {i}. {title[:60]}{'...' if len(title) > 60 else ''}")
        if len(titles) > 5:
            print(f"  ... 还有 {len(titles) - 5} 篇论文")

def generate_summary_reports():
    """生成调研报告列表演示数据"""
    output_dir = "output"
    if not os.path.exists(output_dir):
        print(f"输出目录 {output_dir} 不存在")
        return
    
    reports = []
    for filename in os.listdir(output_dir):
        if filename.endswith('.md'):
            filepath = os.path.join(output_dir, filename)
            try:
                stat = os.stat(filepath)
                
                # 读取文件前几行获取标题
                title = filename.replace('.md', '')
                with open(filepath, 'r', encoding='utf-8') as f:
                    first_line = f.readline().strip()
                    if first_line.startswith('#'):
                        title = first_line.lstrip('# ')
                
                reports.append({
                    "filename": filename,
                    "title": title[:100],  # 限制标题长度
                    "created_at": datetime.fromtimestamp(stat.st_ctime).isoformat(),
                    "modified_at": datetime.fromtimestamp(stat.st_mtime).isoformat(),
                    "size": stat.st_size
                })
            except Exception as e:
                print(f"处理文件 {filename} 时出错: {e}")
                continue
    
    # 按修改时间排序
    reports.sort(key=lambda x: x['modified_at'], reverse=True)
    
    # 保存演示报告数据
    demo_reports_file = "cache/demo_reports.json"
    with open(demo_reports_file, 'w', encoding='utf-8') as f:
        json.dump(reports[:15], f, ensure_ascii=False, indent=2)  # 只保留前15个报告
    
    print(f"\n调研报告数据已保存到 {demo_reports_file}")
    print(f"包含 {len(reports[:15])} 个报告")

if __name__ == "__main__":
    print("=== Survey Agent 演示数据生成器 ===")
    
    # 确保目录存在
    os.makedirs("cache", exist_ok=True)
    
    # 生成论文缓存演示数据
    generate_demo_cache()
    
    # 生成调研报告演示数据
    generate_summary_reports()
    
    print("\n✅ 演示数据生成完成！")
    print("\n使用方法:")
    print("1. 推送代码到GitHub仓库")
    print("2. 启用GitHub Pages (Settings → Pages → GitHub Actions)")
    print("3. 访问 https://your-username.github.io/survey_agent")