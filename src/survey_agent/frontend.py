import streamlit as st
import os
import time
import re
from survey_agent.survey.generator import generate_survey, generate_markdown
from survey_agent.arxiv_tools.search import search_papers
from survey_agent.arxiv_tools.download import process_paper
from survey_agent.llm.summarize import get_summarizer
from survey_agent.arxiv_tools.caption_crawler import crawl_arxiv_html
from survey_agent.arxiv_tools.html_generator import (
    parse_markdown_summaries,
    find_all_papers,
    generate_html_with_summary
)

from survey_agent.env import *
import uuid

st.set_page_config(page_title="AI 论文综述生成器", layout="wide")
st.title("🌟 AI 论文综述生成器 💡")
st.markdown("""
<style>
.big-font { font-size:22px !important; }
</style>
""", unsafe_allow_html=True)

from concurrent.futures import ThreadPoolExecutor, as_completed

def process_papers_parallel(papers, process_paper, progress_placeholder, paper_list_placeholder, max_workers=4):
    processed_papers = [None] * len(papers)  # Pre-allocate list to maintain order
    
    def process_with_progress(idx_paper):
        idx, paper = idx_paper
        result = process_paper(paper)
        return idx, result
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Create list of (idx, paper) tuples for processing
        futures = [executor.submit(process_with_progress, (i, paper)) 
                  for i, paper in enumerate(papers)]
        
        for future in as_completed(futures):
            idx, result = future.result()
            processed_papers[idx] = result
            
            # Update progress display
            progress_placeholder.info(f"正在下载与处理论文 {sum(1 for p in processed_papers if p is not None)}/{len(papers)}")
            paper_list_placeholder.markdown(
                "\n".join([
                    f"- {'📥 ' if processed_papers[i] is not None else '🔍 '}{papers[i].title}" 
                    for i in range(len(papers))
                ])
            )
    
    return [p for p in processed_papers if p is not None]

def summarize_papers_parallel(processed_papers, summarizer, progress_placeholder, paper_list_placeholder, max_workers=4):
    summarized_papers = [None] * len(processed_papers)  # Pre-allocate list to maintain order

    def summarize_with_progress(idx_paper):
        idx, paper = idx_paper
        paper['llm_summary_res'] = summarizer.summarize(paper)
        return idx, paper

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(summarize_with_progress, (i, paper))
                  for i, paper in enumerate(processed_papers)]

        for future in as_completed(futures):
            idx, result = future.result()
            summarized_papers[idx] = result

            # Update progress display
            progress_placeholder.info(f"LLM 总结中 {sum(1 for p in summarized_papers if p is not None)}/{len(processed_papers)}")
            paper_list_placeholder.markdown(
                "\n".join([
                    f"- {'✨ ' if summarized_papers[i] is not None else '📥 '}{processed_papers[i]['title']}"
                    for i in range(len(processed_papers))
                ])
            )

    return [p for p in summarized_papers if p is not None]


def crawl_paper_images_parallel(processed_papers, output_dir, progress_placeholder, paper_list_placeholder, max_workers=4):
    """并行爬取论文图片和Caption"""
    crawl_results = [None] * len(processed_papers)

    def extract_arxiv_id(paper):
        """从论文数据中提取 arXiv ID"""
        # 尝试从 entry_id 提取
        if 'entry_id' in paper:
            match = re.search(r'(\d{4}\.\d{5})', paper['entry_id'])
            if match:
                return match.group(1)

        # 尝试从 pdf_url 提取
        if 'pdf_url' in paper:
            match = re.search(r'(\d{4}\.\d{5})', paper['pdf_url'])
            if match:
                return match.group(1)

        return None

    def crawl_with_progress(idx_paper):
        idx, paper = idx_paper
        arxiv_id = extract_arxiv_id(paper)

        if not arxiv_id:
            return idx, None

        # 爬取该论文的 HTML 页面
        url = f"https://arxiv.org/html/{arxiv_id}"
        try:
            result = crawl_arxiv_html(url, output_dir)
            return idx, result
        except Exception as e:
            print(f"爬取 {arxiv_id} 失败: {e}")
            return idx, None

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(crawl_with_progress, (i, paper))
                  for i, paper in enumerate(processed_papers)]

        for future in as_completed(futures):
            idx, result = future.result()
            crawl_results[idx] = result

            # Update progress display
            completed = sum(1 for r in crawl_results if r is not None)
            progress_placeholder.info(f"正在爬取论文图片 {sum(1 for r in crawl_results if r is not False)}/{len(processed_papers)} (成功: {completed})")
            paper_list_placeholder.markdown(
                "\n".join([
                    f"- {'🖼️ ' if crawl_results[i] is not None else '✨ '}{processed_papers[i]['title']}"
                    for i in range(len(processed_papers))
                ])
            )

    return crawl_results




with st.form("query_form"):
    query = st.text_input("请输入你的论文查询关键词（支持多个关键词，用逗号分隔）", "Vision Language Model, Game")
    max_results = st.slider("最多检索论文数", 5, 50, 10)
    # llm_provider = st.selectbox("LLM 提供商", ["openai"])
    llm_provider = "openai"
    # model_name = st.text_input("LLM 模型名", "glm-4-air")
    model_name = st.selectbox("LLM 模型名", ['None', "ep-20250529110941-khvtx"])

    # 新增：是否爬取图片选项
    crawl_images = st.checkbox("爬取论文图片和 Caption（生成可视化 HTML）", value=True)

    submitted = st.form_submit_button("开始生成综述")

progress_placeholder = st.empty()
paper_list_placeholder = st.empty()
summary_placeholder = st.empty()
download_placeholder = st.empty()

if submitted:
    terms = [t.strip() for t in query.split(",") if t.strip()]
    progress_placeholder.info("正在检索论文...")
    papers = search_papers(terms=terms, max_results=max_results)
    titles = [p.title for p in papers]
    paper_list_placeholder.markdown(
        "\n".join([f"- 🔍 {t}" for t in titles]) or "未检索到论文。"
    )
    
    # 修改原始代码部分
    processed_papers = process_papers_parallel(papers, process_paper, progress_placeholder, paper_list_placeholder)
    progress_placeholder.info("正在调用 LLM 生成总结...")
    # summarizer = get_summarizer(llm_provider, model_name)
    if model_name != "None":
        summarizer = get_summarizer(llm_provider, model_name)
    else:
        summarizer = get_summarizer(llm_provider)
    processed_papers = summarize_papers_parallel(processed_papers, summarizer, progress_placeholder, paper_list_placeholder)   
        
    progress_placeholder.success("全部论文处理完成，正在生成 markdown...")
    unique_id = str(uuid.uuid4())
    output_md = f"survey_result_{unique_id}.md"
    markdown_content = generate_markdown(processed_papers, output_md, terms)

    # 初始化 HTML 相关变量
    html_content_with_images = None
    html_output_file = None
    successful_crawls = 0

    # 步骤 4: 爬取论文图片和 Caption（可选）
    if crawl_images:
        progress_placeholder.info("正在爬取论文图片和 Caption...")
        output_dir = "paper_captions"
        os.makedirs(output_dir, exist_ok=True)

        crawl_results = crawl_paper_images_parallel(
            processed_papers,
            output_dir,
            progress_placeholder,
            paper_list_placeholder,
            max_workers=4
        )

        # 统计爬取结果
        successful_crawls = sum(1 for r in crawl_results if r is not None)
        progress_placeholder.success(f"图片爬取完成！成功: {successful_crawls}/{len(processed_papers)}")

        # 步骤 5: 生成带图片的 HTML
        progress_placeholder.info("正在生成可视化 HTML...")

        # 解析 Markdown 总结
        summaries = parse_markdown_summaries(output_md)

        # 查找爬取的论文数据
        papers_data = find_all_papers(output_dir)

        # 生成 HTML
        html_output_file = f"paper_captions_{unique_id}.html"

        if papers_data:
            generate_html_with_summary(papers_data, summaries, html_output_file)
            progress_placeholder.success(f"可视化 HTML 已生成: {html_output_file}")

            # 读取生成的 HTML 内容用于下载
            with open(html_output_file, 'r', encoding='utf-8') as f:
                html_content_with_images = f.read()
        else:
            progress_placeholder.warning("未找到图片数据，生成标准 HTML")
            import markdown
            html_content_with_images = markdown.markdown(markdown_content, extensions=['tables', 'fenced_code'])
    else:
        # 不爬取图片，生成标准 HTML
        import markdown
        html_content_with_images = markdown.markdown(markdown_content, extensions=['tables', 'fenced_code'])
        html_output_file = f"survey_result_{unique_id}.html"

    # 显示预览
    summary_placeholder.markdown("### 综述 Markdown 预览")
    summary_placeholder.markdown(markdown_content)

    # 提供下载
    download_placeholder.markdown("### 下载结果")

    col1, col2 = st.columns(2)
    with col1:
        st.download_button(
            "📄 下载 Markdown 文件",
            markdown_content,
            file_name=output_md,
            mime="text/markdown"
        )

    with col2:
        if html_content_with_images:
            button_label = "🌐 下载 HTML 文件（含图片）" if crawl_images and successful_crawls > 0 else "🌐 下载 HTML 文件"
            st.download_button(
                button_label,
                html_content_with_images,
                file_name=html_output_file,
                mime="text/html"
            )

    # 最终状态
    if crawl_images:
        progress_placeholder.success(f"🎉 综述已生成！共处理 {len(processed_papers)} 篇论文，爬取 {successful_crawls} 篇图片")
    else:
        progress_placeholder.success(f"🎉 综述已生成！共处理 {len(processed_papers)} 篇论文")

    # 显示文件路径信息
    st.markdown("---")
    st.markdown("### 📁 生成的文件")

    # Markdown 文件
    md_abs_path = os.path.abspath(output_md)
    st.markdown(f"**📄 Markdown 文件：**")
    st.code(md_abs_path, language="")

    # HTML 文件（如果有）
    if html_output_file and os.path.exists(html_output_file):
        html_abs_path = os.path.abspath(html_output_file)
        st.markdown(f"**🌐 HTML 文件：**")
        st.code(html_abs_path, language="")

        # 提供打开链接
        file_url = f"file://{html_abs_path}"
        st.markdown(f"👉 [点击在浏览器中打开 HTML]({file_url})")

        # 自动打开选项
        col_auto1, col_auto2 = st.columns([1, 3])
        with col_auto1:
            if st.button("🚀 自动打开 HTML"):
                import webbrowser
                webbrowser.open(file_url)
                st.success("✓ 已在浏览器中打开！")
        with col_auto2:
            st.caption("点击按钮在默认浏览器中自动打开 HTML 文件") 