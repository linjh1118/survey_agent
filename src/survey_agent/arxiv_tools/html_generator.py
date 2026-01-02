#!/usr/bin/env python3
"""
arXiv Caption HTML Generator
生成包含 LLM 总结和可折叠图片的独立 HTML 文件
"""

import os
import re
import json
import base64
from pathlib import Path


def encode_image_to_base64(image_path):
    """
    将图片编码为 base64 字符串

    Args:
        image_path: 图片路径

    Returns:
        str: base64 编码的图片数据 URL
    """
    try:
        with open(image_path, 'rb') as f:
            image_data = f.read()

        ext = os.path.splitext(image_path)[1].lower()
        mime_type_map = {
            '.png': 'image/png',
            '.jpg': 'image/jpeg',
            '.jpeg': 'image/jpeg',
            '.gif': 'image/gif',
            '.webp': 'image/webp'
        }
        mime_type = mime_type_map.get(ext, 'image/png')

        base64_data = base64.b64encode(image_data).decode('utf-8')
        return f"data:{mime_type};base64,{base64_data}"

    except Exception as e:
        print(f"警告: 编码图片失败 {image_path}: {e}")
        return ""


def parse_summary_sections(summary):
    """
    解析总结内容为四个小节

    Args:
        summary: 论文总结文本

    Returns:
        dict: {'background': str, 'method': str, 'result': str, 'insight': str}
    """
    sections = {
        'background': '',
        'method': '',
        'result': '',
        'insight': ''
    }

    markers = {
        'background': r'###\s*📌\s*背景痛点[/／]本文动机',
        'method': r'###\s*🚀\s*核心方法',
        'result': r'###\s*📈\s*实验结果',
        'insight': r'###\s*💬\s*可借鉴之处'
    }

    for key, pattern in markers.items():
        match = re.search(pattern, summary)
        if match:
            start_pos = match.end()
            next_match = re.search(r'\n###\s*[📌🚀📈💬]', summary[start_pos:])
            if next_match:
                end_pos = start_pos + next_match.start()
            else:
                end_pos = len(summary)

            content = summary[start_pos:end_pos].strip()
            content = content.replace('\n', '<br>\n')
            sections[key] = content

    return sections


def parse_markdown_summaries(md_path):
    """
    解析 markdown 文件，提取每篇论文的 arXiv ID 和总结内容

    Args:
        md_path: markdown 文件路径

    Returns:
        dict: {arxiv_id: summary_content}
    """
    summaries = {}

    if not os.path.exists(md_path):
        print(f"警告: markdown 文件不存在: {md_path}")
        return summaries

    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 从目录部分建立 section_id -> arxiv_id 的映射
    section_to_arxiv = {}
    lines = content.split('\n')

    for line in lines:
        if '[[Paper](https://arxiv.org/pdf/' in line:
            arxiv_match = re.search(r'https://arxiv\.org/pdf/(\d{4}\.\d{5})', line)
            if arxiv_match:
                arxiv_id = arxiv_match.group(1)
                anchor_match = re.search(r'\[\[TLDR/Notes\]\(#([^\)]+)\)\]', line)
                if anchor_match:
                    section_id = anchor_match.group(1)
                    section_to_arxiv[section_id] = arxiv_id

    print(f"  从目录提取到 {len(section_to_arxiv)} 个映射")

    # 提取每个 section 的内容
    sections = re.split(r'\n## ', content)

    for section in sections:
        if not section.strip():
            continue

        lines = section.split('\n')
        if not lines:
            continue

        section_id = lines[0].strip()

        if len(lines) < 2 or not lines[1].strip().startswith('### Abstract'):
            continue

        arxiv_id = section_to_arxiv.get(section_id)
        if not arxiv_id:
            continue

        summary_content = '\n'.join(lines[1:]).strip()
        summaries[arxiv_id] = summary_content

    return summaries


def find_all_papers(outputs_dir):
    """
    查找 outputs 目录下的所有论文数据

    Args:
        outputs_dir: outputs 目录路径

    Returns:
        dict: {arxiv_id: paper_data}
    """
    papers = {}

    if not os.path.exists(outputs_dir):
        return papers

    for paper_dir in sorted(os.listdir(outputs_dir)):
        paper_path = os.path.join(outputs_dir, paper_dir)

        if not os.path.isdir(paper_path):
            continue

        json_path = os.path.join(paper_path, 'crawled_data.json')
        if not os.path.exists(json_path):
            continue

        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            arxiv_id = data.get('arxiv_id', '')
            if not arxiv_id:
                continue

            # 处理图片：转换为 base64
            for img_info in data.get('images_with_captions', []):
                local_path = img_info.get('local_path', '')
                if local_path and os.path.isfile(local_path):
                    base64_data = encode_image_to_base64(local_path)
                    img_info['base64_data'] = base64_data
                else:
                    img_info['base64_data'] = ''

            papers[arxiv_id] = {
                'dir_name': paper_dir,
                'data': data
            }

        except Exception as e:
            print(f"警告: 读取 {json_path} 失败: {e}")
            continue

    return papers


def generate_html_with_summary(papers, summaries, output_path):
    """
    生成包含论文总结和可折叠图片的 HTML 文件

    Args:
        papers: {arxiv_id: paper_data}
        summaries: {arxiv_id: summary_content}
        output_path: 输出 HTML 文件路径
    """

    html_content = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>arXiv 论文查看器 - 含总结和Caption</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Helvetica', 'Arial', sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }

        .container {
            max-width: 1400px;
            margin: 0 auto;
        }

        header {
            background: white;
            border-radius: 12px;
            padding: 30px;
            margin-bottom: 30px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
            text-align: center;
        }

        h1 {
            color: #667eea;
            font-size: 2.5em;
            margin-bottom: 10px;
            font-weight: 700;
        }

        .subtitle {
            color: #666;
            font-size: 1.1em;
        }

        .stats {
            display: flex;
            justify-content: center;
            gap: 30px;
            margin-top: 20px;
        }

        .stat-item {
            text-align: center;
        }

        .stat-number {
            font-size: 2em;
            font-weight: bold;
            color: #667eea;
        }

        .stat-label {
            color: #666;
            font-size: 0.9em;
        }

        .paper-card {
            background: white;
            border-radius: 12px;
            padding: 30px;
            margin-bottom: 30px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .paper-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 40px rgba(0, 0, 0, 0.2);
        }

        .paper-title {
            font-size: 1.8em;
            color: #2c3e50;
            margin-bottom: 15px;
            font-weight: 600;
            line-height: 1.3;
        }

        .paper-meta {
            display: flex;
            gap: 20px;
            margin-bottom: 20px;
            flex-wrap: wrap;
        }

        .meta-item {
            display: flex;
            align-items: center;
            gap: 5px;
            color: #666;
            font-size: 0.95em;
        }

        .meta-badge {
            background: #667eea;
            color: white;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.85em;
            font-weight: 500;
        }

        .section-title {
            font-size: 1.3em;
            color: #667eea;
            margin: 25px 0 15px 0;
            padding-bottom: 10px;
            border-bottom: 2px solid #667eea;
            font-weight: 600;
        }

        .abstract {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 8px;
            border-left: 4px solid #667eea;
            margin-bottom: 25px;
            line-height: 1.8;
            color: #444;
        }

        .summary-content {
            background: transparent;
            padding: 0;
            border-radius: 0;
            border-left: 0;
            margin-bottom: 25px;
            line-height: 1.8;
        }

        .summary-section-stack {
            display: flex;
            flex-direction: column;
            gap: 15px;
            margin-top: 15px;
        }

        .summary-card {
            background: white;
            border-radius: 8px;
            border-left: 4px solid;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
            overflow: hidden;
            transition: box-shadow 0.2s ease;
        }

        .summary-card:hover {
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.12);
        }

        .summary-card-header {
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 15px 20px;
            cursor: pointer;
            user-select: none;
            background: #fafafa;
            transition: background 0.2s ease;
        }

        .summary-card-header:hover {
            background: #f0f0f0;
        }

        .card-icon {
            font-size: 1.4em;
            flex-shrink: 0;
        }

        .card-title {
            flex: 1;
            font-weight: 600;
            font-size: 1.05em;
            color: #2c3e50;
        }

        .card-toggle {
            font-size: 1.2em;
            color: #999;
            transition: transform 0.3s ease;
            flex-shrink: 0;
        }

        .card-toggle.expanded {
            transform: rotate(90deg);
        }

        .summary-card-content {
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.3s ease;
            padding: 0 20px;
        }

        .summary-card-content.expanded {
            max-height: 2000px;
            padding: 15px 20px 20px 20px;
        }

        .summary-card-content-inner {
            line-height: 1.7;
            color: #555;
            font-size: 0.95em;
        }

        .background-card {
            border-left-color: #ff6b6b;
        }

        .method-card {
            border-left-color: #4ecdc4;
        }

        .result-card {
            border-left-color: #95e1d3;
        }

        .insight-card {
            border-left-color: #a8dadc;
        }

        .collapsible-header {
            cursor: pointer;
            user-select: none;
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 10px 0;
        }

        .collapsible-header:hover {
            opacity: 0.8;
        }

        .toggle-icon {
            transition: transform 0.3s ease;
            font-size: 1.2em;
        }

        .toggle-icon.expanded {
            transform: rotate(90deg);
        }

        .collapsible-content {
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.3s ease;
        }

        .collapsible-content.expanded {
            max-height: none;
        }

        .images-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(400px, 1fr));
            gap: 25px;
            margin-top: 20px;
        }

        .image-item {
            background: #f8f9fa;
            border-radius: 8px;
            overflow: hidden;
            transition: transform 0.3s ease;
            border: 1px solid #e0e0e0;
        }

        .image-item:hover {
            transform: scale(1.02);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }

        .image-wrapper {
            width: 100%;
            background: white;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 15px;
            min-height: 250px;
        }

        .image-wrapper img {
            max-width: 100%;
            height: auto;
            display: block;
            border-radius: 4px;
        }

        .image-caption {
            padding: 15px;
            color: #444;
            font-size: 0.9em;
            line-height: 1.6;
        }

        .figure-id {
            display: inline-block;
            background: #667eea;
            color: white;
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 0.85em;
            font-weight: 500;
            margin-bottom: 8px;
        }

        .arxiv-link {
            color: #667eea;
            text-decoration: none;
            font-weight: 500;
            transition: color 0.3s ease;
        }

        .arxiv-link:hover {
            color: #764ba2;
            text-decoration: underline;
        }

        footer {
            text-align: center;
            color: white;
            margin-top: 40px;
            padding: 20px;
            font-size: 0.9em;
        }

        @media (max-width: 768px) {
            .images-grid {
                grid-template-columns: 1fr;
            }

            h1 {
                font-size: 2em;
            }

            .paper-title {
                font-size: 1.5em;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>📚 arXiv 论文查看器</h1>
            <p class="subtitle">包含LLM总结和可折叠图片展示</p>
            <div class="stats">
                <div class="stat-item">
                    <div class="stat-number">""" + str(len(papers)) + """</div>
                    <div class="stat-label">篇论文</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number">""" + str(sum(len(p['data'].get('images_with_captions', [])) for p in papers.values())) + """</div>
                    <div class="stat-label">张图片</div>
                </div>
            </div>
        </header>
"""

    # 按 arXiv ID 排序（倒序，最新的在前）
    sorted_arxiv_ids = sorted(papers.keys(), reverse=True)

    for idx, arxiv_id in enumerate(sorted_arxiv_ids, 1):
        paper = papers[arxiv_id]
        data = paper['data']
        title = data.get('title', '未知标题')
        abstract = data.get('abstract', '暂无摘要')
        url = data.get('url', '')
        images = data.get('images_with_captions', [])

        summary = summaries.get(arxiv_id, '')

        html_content += f"""
        <div class="paper-card">
            <div class="paper-title">{idx}. {title}</div>

            <div class="paper-meta">
                <div class="meta-item">
                    <span>🔗</span>
                    <a href="{url}" class="arxiv-link" target="_blank">arXiv:{arxiv_id}</a>
                </div>
                <div class="meta-item">
                    <span class="meta-badge">{len(images)} 张图片</span>
                </div>
            </div>
"""

        # LLM 总结（如果有）
        if summary:
            sections = parse_summary_sections(summary)

            html_content += f"""
            <div class="section-title">🤖 LLM 总结</div>
            <div class="summary-content">
                <div class="summary-section-stack">
                    <div class="summary-card background-card">
                        <div class="summary-card-header" onclick="toggleSummaryCard('background-{idx}')">
                            <span class="card-icon">📌</span>
                            <span class="card-title">背景痛点/本文动机</span>
                            <span class="card-toggle expanded" id="toggle-background-{idx}">▶</span>
                        </div>
                        <div class="summary-card-content expanded" id="background-{idx}">
                            <div class="summary-card-content-inner">
                                {sections['background'] or '暂无内容'}
                            </div>
                        </div>
                    </div>

                    <div class="summary-card method-card">
                        <div class="summary-card-header" onclick="toggleSummaryCard('method-{idx}')">
                            <span class="card-icon">🚀</span>
                            <span class="card-title">核心方法</span>
                            <span class="card-toggle expanded" id="toggle-method-{idx}">▶</span>
                        </div>
                        <div class="summary-card-content expanded" id="method-{idx}">
                            <div class="summary-card-content-inner">
                                {sections['method'] or '暂无内容'}
                            </div>
                        </div>
                    </div>

                    <div class="summary-card result-card">
                        <div class="summary-card-header" onclick="toggleSummaryCard('result-{idx}')">
                            <span class="card-icon">📈</span>
                            <span class="card-title">实验结果</span>
                            <span class="card-toggle" id="toggle-result-{idx}">▶</span>
                        </div>
                        <div class="summary-card-content" id="result-{idx}">
                            <div class="summary-card-content-inner">
                                {sections['result'] or '暂无内容'}
                            </div>
                        </div>
                    </div>

                    <div class="summary-card insight-card">
                        <div class="summary-card-header" onclick="toggleSummaryCard('insight-{idx}')">
                            <span class="card-icon">💬</span>
                            <span class="card-title">可借鉴之处</span>
                            <span class="card-toggle" id="toggle-insight-{idx}">▶</span>
                        </div>
                        <div class="summary-card-content" id="insight-{idx}">
                            <div class="summary-card-content-inner">
                                {sections['insight'] or '暂无内容'}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
"""

        # Abstract
        html_content += f"""
            <div class="section-title">📄 摘要 (Abstract)</div>
            <div class="abstract">{abstract}</div>
"""

        # 图片部分（可折叠）
        if images:
            html_content += f"""
            <div class="section-title collapsible-header" onclick="toggleImages('images-{idx}')">
                <span class="toggle-icon" id="icon-{idx}">▶</span>
                <span>🖼️ 图片和 Caption ({len(images)} 张)</span>
            </div>
            <div class="collapsible-content" id="images-{idx}">
                <div class="images-grid">
"""

            for img_info in images:
                figure_id = img_info.get('figure_id', 'N/A')
                caption = img_info.get('caption', '暂无描述')
                base64_data = img_info.get('base64_data', '')

                if base64_data:
                    html_content += f"""                    <div class="image-item">
                        <div class="image-wrapper">
                            <img src="{base64_data}" alt="{figure_id}">
                        </div>
                        <div class="image-caption">
                            <div class="figure-id">{figure_id}</div>
                            <div>{caption}</div>
                        </div>
                    </div>
"""

            html_content += """                </div>
            </div>
"""

        html_content += """        </div>
"""

    html_content += """
        <footer>
            <p>由 survey_agent 自动生成 | 包含 LLM 总结、图片和 Caption</p>
        </footer>
    </div>

    <script>
        function toggleImages(id) {
            const content = document.getElementById(id);
            const icon = document.getElementById('icon-' + id.replace('images-', ''));

            if (content.classList.contains('expanded')) {
                content.classList.remove('expanded');
                icon.classList.remove('expanded');
            } else {
                content.classList.add('expanded');
                icon.classList.add('expanded');
            }
        }

        function toggleSummaryCard(id) {
            const content = document.getElementById(id);
            const toggle = document.getElementById('toggle-' + id);

            if (content.classList.contains('expanded')) {
                content.classList.remove('expanded');
                toggle.classList.remove('expanded');
            } else {
                content.classList.add('expanded');
                toggle.classList.add('expanded');
            }
        }
    </script>
</body>
</html>
"""

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"✓ HTML 文件已生成: {output_path}")
    file_size = os.path.getsize(output_path)
    print(f"  文件大小: {file_size / 1024 / 1024:.2f} MB")


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print("用法: python html_generator.py <survey_result.md> <outputs_dir> [output.html]")
        sys.exit(1)

    md_path = sys.argv[1]
    outputs_dir = sys.argv[2]
    output_html = sys.argv[3] if len(sys.argv) > 3 else 'paper_captions.html'

    print("正在解析 markdown 文件...")
    summaries = parse_markdown_summaries(md_path)
    print(f"找到 {len(summaries)} 篇论文总结")

    print("\n正在查找论文数据...")
    papers = find_all_papers(outputs_dir)
    print(f"找到 {len(papers)} 篇论文数据")

    if papers:
        print("\n正在生成 HTML（嵌入图片）...")
        generate_html_with_summary(papers, summaries, output_html)
        print("\n✓ 完成！")
    else:
        print("\n未找到论文数据")
