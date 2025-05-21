import streamlit as st
import os
import time
from survey_agent.survey.generator import generate_survey, generate_markdown
from survey_agent.arxiv_tools.search import search_papers
from survey_agent.arxiv_tools.download import process_paper
from survey_agent.llm.summarize import get_summarizer
os.environ["API_KEY"] = '979525e325524e629a9fe3a0d406b924.f5e8BbGc4DpMPAbm'
os.environ["BASE_URL"] = 'https://open.bigmodel.cn/api/paas/v4/'
# export https_proxy=http://127.0.0.1:7890 http_proxy=http://127.0.0.1:7890 all_proxy=socks5://127.0.0.1:7890
os.environ["https_proxy"] = "http://127.0.0.1:7890"
os.environ["http_proxy"] = "http://127.0.0.1:7890"
os.environ["all_proxy"] = "socks5://127.0.0.1:7890"
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




with st.form("query_form"):
    query = st.text_input("请输入你的论文查询关键词（支持多个关键词，用逗号分隔）", "Vision Language Model, Game")
    max_results = st.slider("最多检索论文数", 5, 50, 10)
    # llm_provider = st.selectbox("LLM 提供商", ["openai"])
    llm_provider = "openai"
    # model_name = st.text_input("LLM 模型名", "glm-4-air")
    model_name = st.selectbox("LLM 模型名", ["glm-4-air", "glm-4-plus"])
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
    summarizer = get_summarizer(llm_provider, model_name)
    processed_papers = summarize_papers_parallel(processed_papers, summarizer, progress_placeholder, paper_list_placeholder)   
        
    progress_placeholder.success("全部论文处理完成，正在生成 markdown...")
    uuid = str(uuid.uuid4())
    output_md = f"survey_result_{uuid}.md"
    markdown_content = generate_markdown(processed_papers, output_md, terms)
    # 分割条
    
    summary_placeholder.markdown("### 综述 Markdown 预览")
    # summary_placeholder.code(markdown_content, language="markdown")
    summary_placeholder.markdown(markdown_content)
    
    # 生成 HTML
    import markdown
    html_content = markdown.markdown(markdown_content, extensions=['tables', 'fenced_code'])
    download_placeholder.markdown("### 下载结果")
    st.download_button("下载 Markdown 文件", markdown_content, file_name="survey_result.md")
    st.download_button("下载 HTML 文件", html_content, file_name="survey_result.html")
    progress_placeholder.success("🎉 综述已生成！") 