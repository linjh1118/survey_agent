#!/usr/bin/env python3
"""
arXiv HTML Caption Crawler
从 arXiv HTML 页面爬取论文标题、摘要、图片和对应的 caption
"""

import os
import re
import json
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup


def clean_filename(text):
    """
    清理文件名，移除特殊字符

    Args:
        text: 原始文本

    Returns:
        str: 清理后的文件名
    """
    # 替换冒号为空格
    text = text.replace(':', ' ')
    # 移除其他特殊字符
    text = re.sub(r'[<>:"/\\|?*\n\r\t]', '', text)
    # 将连续空格替换为单个下划线
    text = re.sub(r'\s+', '_', text.strip())
    # 限制长度
    if len(text) > 100:
        text = text[:100].rstrip('_')
    return text


def get_paper_title(soup):
    """
    从 HTML 中提取论文标题

    Args:
        soup: BeautifulSoup 对象

    Returns:
        str: 论文标题，如果未找到则返回 None
    """
    # 方法1: 从 <title> 标签提取
    title_tag = soup.find('title')
    if title_tag:
        return title_tag.get_text(strip=True)

    # 方法2: 从 h1.ltx_title 提取
    h1_tag = soup.find('h1', class_='ltx_title')
    if h1_tag:
        return h1_tag.get_text(strip=True)

    return None


def crawl_arxiv_html(url, output_dir='outputs'):
    """
    爬取 arXiv HTML 论文页面

    Args:
        url: arXiv HTML 页面 URL
        output_dir: 输出目录

    Returns:
        dict: 包含论文信息的字典，如果失败则返回 None
    """
    print(f"\n正在爬取: {url}")

    # 提取 arXiv ID
    arxiv_id = url.split('/')[-1]
    print(f"arXiv ID: {arxiv_id}")

    # 先创建临时目录用于下载
    temp_dir = os.path.join(output_dir, f"temp_{arxiv_id}")
    os.makedirs(temp_dir, exist_ok=True)

    try:
        # 获取 HTML 内容
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        # 提取标题
        title = get_paper_title(soup)
        if not title:
            print("警告: 未找到论文标题")
            title = f"Unknown_{arxiv_id}"

        print(f"论文标题: {title}")

        # 提取摘要
        abstract = ""
        abstract_section = soup.find('section', class_='ltx_abstract')
        if not abstract_section:
            abstract_section = soup.find('div', class_='ltx_abstract')

        if abstract_section:
            abstract_p = abstract_section.find('p', class_='ltx_p')
            if abstract_p:
                abstract = abstract_p.get_text(strip=True)
            else:
                # 尝试获取所有文本
                abstract = abstract_section.get_text(strip=True)
                # 移除 "Abstract" 标题
                abstract = re.sub(r'^Abstract[\s:：]*', '', abstract, flags=re.IGNORECASE)
        else:
            # 备选方案：查找包含 "Abstract" 的段落
            for elem in soup.find_all(['p', 'div', 'section']):
                text = elem.get_text(strip=True)
                if text.startswith('Abstract'):
                    abstract = re.sub(r'^Abstract[\s:：]*', '', text)
                    break

        if abstract:
            print(f"摘要长度: {len(abstract)} 字符")
        else:
            print("警告: 未找到摘要")

        # 查找所有图片
        images_with_captions = []
        figures = soup.find_all('figure', class_='ltx_figure')

        print(f"找到 {len(figures)} 个图片")

        for idx, figure in enumerate(figures, 1):
            # 查找图片标签
            img_tag = figure.find('img')
            if not img_tag:
                continue

            # 获取图片 URL
            img_src = img_tag.get('src')
            if not img_src:
                continue

            # 构建完整的图片 URL
            # 确保 base_url 以 '/' 结尾
            base_url = url if url.endswith('/') else url + '/'
            full_img_url = urljoin(base_url, img_src)

            # 提取 figure ID
            figure_id = figure.get('id', f'figure_{idx}')

            # 提取 caption
            caption = ""
            figcaption = figure.find('figcaption', class_='ltx_caption')
            if figcaption:
                # 移除 "Figure X:" 前缀
                caption_text = figcaption.get_text(strip=True)
                caption = re.sub(r'^Figure\s+\d+[\.:：]\s*', '', caption_text, flags=re.IGNORECASE)
            else:
                # 尝试查找其他 caption 容器
                caption_elem = figure.find(class_='ltx_caption')
                if caption_elem:
                    caption = caption_elem.get_text(strip=True)

            # 下载图片
            try:
                img_response = requests.get(full_img_url, timeout=30)
                img_response.raise_for_status()

                # 获取文件扩展名
                img_ext = os.path.splitext(img_src)[1] or '.png'

                # 保存图片到临时目录
                img_filename = f"{figure_id}{img_ext}"
                img_path = os.path.join(temp_dir, 'images', img_filename)
                os.makedirs(os.path.dirname(img_path), exist_ok=True)

                with open(img_path, 'wb') as f:
                    f.write(img_response.content)

                print(f"  ✓ 下载图片: {img_filename}")

                images_with_captions.append({
                    'figure_id': figure_id,
                    'url': full_img_url,
                    'local_path': img_path,
                    'caption': caption
                })

            except Exception as e:
                print(f"  ✗ 下载图片失败 {full_img_url}: {e}")
                continue

        # 创建最终目录名（基于标题）
        cleaned_title = clean_filename(title)
        final_dir = os.path.join(output_dir, f"{cleaned_title}_{arxiv_id}")

        # 重命名临时目录为最终目录
        if os.path.exists(final_dir):
            import shutil
            shutil.rmtree(final_dir)
        os.rename(temp_dir, final_dir)

        # 更新图片路径
        for img_info in images_with_captions:
            old_path = img_info['local_path']
            new_path = old_path.replace(temp_dir, final_dir)
            img_info['local_path'] = new_path

        # 保存元数据
        metadata = {
            'url': url,
            'arxiv_id': arxiv_id,
            'title': title,
            'abstract': abstract,
            'images_with_captions': images_with_captions
        }

        metadata_path = os.path.join(final_dir, 'crawled_data.json')
        with open(metadata_path, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, ensure_ascii=False, indent=2)

        print(f"\n✓ 爬取完成: {len(images_with_captions)} 张图片")
        print(f"  输出目录: {final_dir}")

        return metadata

    except Exception as e:
        print(f"\n✗ 爬取失败: {e}")
        # 清理临时目录
        if os.path.exists(temp_dir):
            import shutil
            shutil.rmtree(temp_dir)
        return None


def batch_crawl_arxiv_ids(arxiv_ids, output_dir='outputs'):
    """
    批量爬取多个 arXiv 论文

    Args:
        arxiv_ids: arXiv ID 列表
        output_dir: 输出目录

    Returns:
        dict: 统计信息
    """
    total = len(arxiv_ids)
    success = 0
    failed = 0

    results = []

    print(f"\n开始批量爬取 {total} 篇论文...")
    print("=" * 60)

    for idx, arxiv_id in enumerate(arxiv_ids, 1):
        print(f"\n[{idx}/{total}] 处理: {arxiv_id}")

        url = f"https://arxiv.org/html/{arxiv_id}"
        result = crawl_arxiv_html(url, output_dir)

        if result:
            success += 1
            results.append(result)
        else:
            failed += 1

    print("\n" + "=" * 60)
    print("批量爬取完成")
    print("=" * 60)
    print(f"总计: {total} 篇")
    print(f"成功: {success} 篇")
    print(f"失败: {failed} 篇")
    print(f"成功率: {success / total * 100:.1f}%")
    print("=" * 60)

    return {
        'total': total,
        'success': success,
        'failed': failed,
        'results': results
    }


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("用法: python caption_crawler.py <arxiv_id_or_url>")
        print("示例: python caption_crawler.py 2512.16149")
        print("      python caption_crawler.py https://arxiv.org/html/2512.16149")
        sys.exit(1)

    arg = sys.argv[1]

    # 判断是 URL 还是 ID
    if arg.startswith('http'):
        url = arg
    else:
        url = f"https://arxiv.org/html/{arg}"

    crawl_arxiv_html(url)
