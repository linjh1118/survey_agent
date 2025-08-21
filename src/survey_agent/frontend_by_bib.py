import streamlit as st
import os
import time
import tempfile
import uuid
import arxiv
import re
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from survey_agent.arxiv_tools.download import process_paper
from survey_agent.survey.generator import generate_survey_from_bib
from survey_agent.utils.bib_parser import BibParser
from survey_agent.llm.summarize import get_summarizer
from survey_agent.survey.generator import generate_markdown

# 设置环境变量
from survey_agent.env import *



st.set_page_config(page_title="AI 论文综述生成器 (BIB文件版)", layout="wide")
st.title("📚 AI 论文综述生成器 (BIB文件版) 🔬")

st.markdown("""
<style>
.big-font { font-size:22px !important; }
.prompt-preview { 
    background-color: #f0f2f6; 
    padding: 10px; 
    border-radius: 5px; 
    border-left: 5px solid #4CAF50; 
    margin: 10px 0;
}
</style>
""", unsafe_allow_html=True)

def fetch_arxiv_paper_parallel(arxiv_ids, progress_placeholder, paper_list_placeholder, max_workers=4):
    """并行从arXiv获取论文对象"""
    papers = [None] * len(arxiv_ids)  # Pre-allocate list to maintain order
    
    def fetch_single_paper(idx_id):
        idx, arxiv_id = idx_id
        try:
            client = arxiv.Client()
            search = arxiv.Search(id_list=[arxiv_id])
            results = list(client.results(search))
            if results:
                return idx, results[0]
            else:
                return idx, None
        except Exception as e:
            print(f"Error fetching paper {arxiv_id}: {e}")
            return idx, None
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Create list of (idx, arxiv_id) tuples for processing
        futures = [executor.submit(fetch_single_paper, (i, arxiv_id)) 
                  for i, arxiv_id in enumerate(arxiv_ids)]
        
        for future in as_completed(futures):
            idx, result = future.result()
            papers[idx] = result
            
            # Update progress display
            completed_count = sum(1 for p in papers if p is not None)
            progress_placeholder.info(f"🔍 正在从arXiv获取论文信息 {completed_count}/{len(arxiv_ids)}")
            
            # Update paper list display
            paper_list_placeholder.markdown(
                "\n".join([
                    f"- {'📄 ' if papers[i] is not None else '🔍 '}{arxiv_ids[i]}" 
                    for i in range(len(arxiv_ids))
                ])
            )
    
    # Filter out None results
    return [p for p in papers if p is not None]

def search_papers_by_title_parallel(entries_without_arxiv, progress_placeholder, paper_list_placeholder, max_workers=4):
    """并行通过标题搜索arXiv论文"""
    found_papers = [None] * len(entries_without_arxiv)  # Pre-allocate list to maintain order
    
    def search_single_paper(idx_entry):
        idx, entry = idx_entry
        try:
            parser = BibParser()
            # 启用详细输出模式，在终端显示搜索过程
            print(f"\n📋 [{idx+1}/{len(entries_without_arxiv)}] 开始搜索论文...")
            result = parser.search_paper_by_title(entry['cleaned_title'], verbose=True)
            return idx, result, entry
        except Exception as e:
            print(f"❌ Error searching paper with title '{entry['cleaned_title']}': {e}\n")
            return idx, None, entry
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Create list of (idx, entry) tuples for processing
        futures = [executor.submit(search_single_paper, (i, entry)) 
                  for i, entry in enumerate(entries_without_arxiv)]
        
        for future in as_completed(futures):
            idx, result, entry = future.result()
            found_papers[idx] = result
            
            # Update progress display
            completed_count = sum(1 for p in found_papers if p is not None)
            progress_placeholder.info(f"🔍 正在通过标题搜索论文 {completed_count}/{len(entries_without_arxiv)}")
            
            # Update paper list display
            paper_list_placeholder.markdown(
                "\n".join([
                    f"- {'📄 ' if found_papers[i] is not None else '❌ '}{entries_without_arxiv[i]['cleaned_title'][:60]}..." 
                    for i in range(len(entries_without_arxiv))
                ])
            )
    
    # Filter out None results
    return [p for p in found_papers if p is not None]

def process_papers_parallel(papers, progress_placeholder, paper_list_placeholder, pdf_dir=None, max_workers=4):
    """并行处理论文：下载PDF并提取文本"""
    processed_papers = [None] * len(papers)  # Pre-allocate list to maintain order
    
    def process_with_progress(idx_paper):
        idx, paper = idx_paper
        result = process_paper(paper, pdf_dir)
        return idx, result
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Create list of (idx, paper) tuples for processing
        futures = [executor.submit(process_with_progress, (i, paper)) 
                  for i, paper in enumerate(papers)]
        
        for future in as_completed(futures):
            idx, result = future.result()
            processed_papers[idx] = result
            
            # Update progress display
            progress_placeholder.info(f"📥 正在下载与处理论文 {sum(1 for p in processed_papers if p is not None)}/{len(papers)}")
            paper_list_placeholder.markdown(
                "\n".join([
                    f"- {'📥 ' if processed_papers[i] is not None else '🔍 '}{papers[i].title}" 
                    for i in range(len(papers))
                ])
            )
    
    return [p for p in processed_papers if p is not None]

def summarize_papers_parallel(processed_papers, summarizer, progress_placeholder, paper_list_placeholder, max_workers=4):
    """并行生成论文总结"""
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
            progress_placeholder.info(f"✨ LLM 总结中 {sum(1 for p in summarized_papers if p is not None)}/{len(processed_papers)}")
            paper_list_placeholder.markdown(
                "\n".join([
                    f"- {'✨ ' if summarized_papers[i] is not None else '📥 '}{processed_papers[i]['title']}" 
                    for i in range(len(processed_papers))
                ])
            )
    
    return [p for p in summarized_papers if p is not None]

def generate_survey_from_bib_parallel(bib_file: str,
                                    output_file: str = "survey_from_bib.md",
                                    llm_provider: str = "openai",
                                    model_name: str = None,
                                    custom_prompt: str = None,
                                    pdf_dir: str = None,
                                    progress_placeholder=None,
                                    paper_list_placeholder=None,
                                    max_workers: int = 4) -> str:
    """
    并行版本的从BIB文件生成综述函数，支持通过标题搜索没有arXiv ID的条目
    """
    # Step 1: Parse BIB file and extract arXiv IDs and entries without arXiv IDs
    if progress_placeholder:
        progress_placeholder.info(f"📚 正在解析 BIB 文件...")
    
    parser = BibParser()
    content = Path(bib_file).read_text(encoding='utf-8')
    parse_result = parser.parse_string(content)
    
    arxiv_ids = parse_result['arxiv_ids']
    entries_without_arxiv = parse_result['entries_without_arxiv']
    
    if not arxiv_ids and not entries_without_arxiv:
        if progress_placeholder:
            progress_placeholder.error("❌ 在BIB文件中没有找到任何可处理的论文")
        return None
    
    if progress_placeholder:
        progress_placeholder.info(f"✅ 找到 {len(arxiv_ids)} 个arXiv ID，{len(entries_without_arxiv)} 个需要通过标题搜索的条目")
    
    all_papers = []
    
    # Step 2: 并行从arXiv获取有ID的论文对象
    if arxiv_ids:
        if progress_placeholder:
            progress_placeholder.info("🔍 正在从arXiv获取有ID的论文详细信息...")
        
        papers_from_ids = fetch_arxiv_paper_parallel(
            arxiv_ids, progress_placeholder, paper_list_placeholder, max_workers
        )
        all_papers.extend(papers_from_ids)
        
        if progress_placeholder:
            progress_placeholder.info(f"✅ 成功获取 {len(papers_from_ids)} 篇有ID的论文信息")
    
    # Step 3: 并行通过标题搜索没有arXiv ID的论文
    if entries_without_arxiv:
        if progress_placeholder:
            progress_placeholder.info("🔍 正在通过标题搜索论文...")
        
        papers_from_titles = search_papers_by_title_parallel(
            entries_without_arxiv, progress_placeholder, paper_list_placeholder, max_workers
        )
        all_papers.extend(papers_from_titles)
        
        if progress_placeholder:
            progress_placeholder.info(f"✅ 通过标题搜索成功找到 {len(papers_from_titles)} 篇论文")
    
    if not all_papers:
        if progress_placeholder:
            progress_placeholder.error("❌ 没有成功获取到任何论文信息")
        return None
    
    if progress_placeholder:
        progress_placeholder.info(f"✅ 总共获取 {len(all_papers)} 篇论文信息")
    
    # Step 4: 并行处理论文 (下载PDFs和提取文本)
    if progress_placeholder:
        progress_placeholder.info("📥 正在下载PDFs和提取文本...")
    
    processed_papers = process_papers_parallel(
        all_papers, progress_placeholder, paper_list_placeholder, pdf_dir, max_workers
    )
    
    if not processed_papers:
        if progress_placeholder:
            progress_placeholder.error("❌ 没有论文被成功处理")
        return None
    
    # Step 5: 并行生成总结
    if progress_placeholder:
        progress_placeholder.info("🤖 正在使用LLM生成总结...")
    
    summarizer = get_summarizer(llm_provider, model_name, custom_prompt)
    summarized_papers = summarize_papers_parallel(
        processed_papers, summarizer, progress_placeholder, paper_list_placeholder, max_workers
    )
    
    
    markdown_content = generate_markdown(summarized_papers, output_file, bib_file=bib_file)
    
    if progress_placeholder:
        progress_placeholder.success("🎉 综述生成完成！")
    
    return output_file

# 初始化会话状态
if 'bib_content' not in st.session_state:
    st.session_state.bib_content = None
if 'arxiv_papers' not in st.session_state:
    st.session_state.arxiv_papers = []
if 'title_papers' not in st.session_state:
    st.session_state.title_papers = []
if 'all_papers' not in st.session_state:
    st.session_state.all_papers = []

# 侧边栏：配置选项
st.sidebar.header("⚙️ 配置选项")

# LLM设置
llm_provider = "openai"
model_name = st.sidebar.selectbox("🤖 LLM 模型", ["ep-20250529110941-khvtx", "doubao"])

# 并行处理设置
max_workers = st.sidebar.slider("🔧 并行处理线程数", min_value=1, max_value=8, value=4, 
                               help="增加线程数可以加快处理速度，但会消耗更多系统资源")

# 主界面
col1, col2 = st.columns([1, 1])

with col1:
    st.header("📁 BIB 文件上传")
    uploaded_bib = st.file_uploader(
        "上传您的 BibTeX 文件",
        type=['bib', 'txt'],
        help="支持 .bib 和 .txt 格式的 BibTeX 文件"
    )
    
    if uploaded_bib is not None:
        try:
            # 读取文件内容并处理编码
            file_content = uploaded_bib.read()
            if isinstance(file_content, bytes):
                # 尝试不同的编码
                encodings = ['utf-8', 'gbk', 'latin-1', 'cp1252']
                bib_content = None
                for encoding in encodings:
                    try:
                        bib_content = file_content.decode(encoding)
                        break
                    except UnicodeDecodeError:
                        continue
                
                if bib_content is None:
                    st.error("❌ 无法解码文件内容，请检查文件编码")
                    st.stop()
            else:
                bib_content = file_content
            
            # 保存到会话状态
            st.session_state.bib_content = bib_content
            
            # 预览BIB文件内容
            st.subheader("📋 BIB 文件预览")
            preview_content = bib_content[:1000] + "..." if len(bib_content) > 1000 else bib_content
            st.text_area("文件内容", preview_content, height=200, disabled=True)
            
            # 解析BIB文件，提取arxiv IDs和需要标题搜索的条目
            try:
                parser = BibParser()
                parse_result = parser.parse_string(bib_content)
                
                arxiv_ids = parse_result['arxiv_ids']
                entries_without_arxiv = parse_result['entries_without_arxiv']
                
                # 构造有arXiv ID的论文字典列表
                arxiv_papers = [
                    {
                        'arxiv_id': arxiv_id,
                        'url': f"https://arxiv.org/abs/{arxiv_id}",
                        'pdf_url': f"https://arxiv.org/pdf/{arxiv_id}.pdf"
                    }
                    for arxiv_id in arxiv_ids
                ]
                
                # 构造需要标题搜索的条目列表  
                title_papers = [
                    {
                        'title': entry['cleaned_title'],
                        'original_title': entry['original_title'],
                        'authors': entry['authors'],
                        'year': entry['year'],
                        'key': entry['key']
                    }
                    for entry in entries_without_arxiv
                ]
                
                # 保存到会话状态
                st.session_state.arxiv_papers = arxiv_papers
                st.session_state.title_papers = title_papers
                st.session_state.all_papers = arxiv_papers + title_papers
                
                if arxiv_ids or entries_without_arxiv:
                    st.success(f"✅ 成功解析BIB文件！")
                    st.info(f"📊 找到 {len(arxiv_ids)} 个arXiv ID，{len(entries_without_arxiv)} 个需要通过标题搜索的条目")
                    
                    # 显示有arXiv ID的论文列表
                    if arxiv_ids:
                        with st.expander("📄 查看有arXiv ID的论文"):
                            for i, arxiv_id in enumerate(arxiv_ids):
                                st.write(f"{i+1}. **{arxiv_id}**")
                                st.write(f"   - URL: https://arxiv.org/abs/{arxiv_id}")
                    
                    # 显示需要标题搜索的条目列表
                    if entries_without_arxiv:
                        with st.expander("🔍 查看需要通过标题搜索的条目"):
                            for i, entry in enumerate(entries_without_arxiv):
                                st.write(f"{i+1}. **{entry['cleaned_title']}**")
                                if entry['authors']:
                                    st.write(f"   - 作者: {entry['authors']}")
                                if entry['year']:
                                    st.write(f"   - 年份: {entry['year']}")
                else:
                    st.warning("⚠️ 没有找到任何可处理的论文")
                    st.session_state.arxiv_papers = []
                    st.session_state.title_papers = []
                    st.session_state.all_papers = []
            
            except Exception as e:
                st.error(f"❌ BIB文件解析失败: {e}")
                st.session_state.arxiv_papers = []
        
        except Exception as e:
            st.error(f"❌ 文件读取失败: {e}")
    
    elif st.session_state.bib_content:
        # 如果有之前上传的文件，显示信息
        st.info("📄 已上传 BIB 文件")
        st.info(f"📊 总共 {len(st.session_state.all_papers)} 篇论文，其中 {len(st.session_state.arxiv_papers)} 篇有 arXiv ID，{len(st.session_state.title_papers)} 篇需要标题搜索")

with col2:
    st.header("🎯 自定义 Prompt")
    
    # Prompt 模板选择
    prompt_type = st.selectbox(
        "选择 Prompt 模板",
        ["默认模板", "学术分析模板", "英文简洁模板", "自定义模板"]
    )
    
    # 预定义的prompt模板
    prompt_templates = {
        "默认模板": """### 任务
你是一个人工智能领域的专家，你能够快速阅读arxiv上的各种AI前沿论文，并给出非常好的论文总结。
现在请你阅读以下论文，并给出你对这篇论文的详细介绍，从而放到你的博客上，让更多人了解这篇论文。

### 论文信息
#### 1. 论文标题: {title}
#### 2. 论文总结: {abstract}
#### 3. 论文全文: {pdf_text}

### 输出格式（输出语言用中文）
```
## 🌟 论文解读 | <想一个，宣传该论文的文案标题>

## 📌 背景痛点/本文动机
...(介绍论文的背景或痛点，或者本文的动机)

## 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1
...

💡 创新点2
...

## 📈 实验结果
...

## 💬 可借鉴之处
...(介绍论文的可借鉴之处)
```""",
        
        "学术分析模板": """### 任务
你是一个AI研究专家，请对以下论文进行专业的学术分析。

### 论文信息
#### 标题: {title}
#### 作者: {authors}
#### 年份: {year}
#### 总结: {abstract}
#### 论文全文: {pdf_text}

### 输出格式
```
## 📊 论文深度分析 | {title}

## 🎯 研究问题与动机
(简要描述论文要解决的核心问题和研究动机)

## 🔬 核心技术方法
(详细描述论文提出的主要技术方法和创新点)

## 📈 实验设计与结果
(分析实验设置、数据集、评估指标和主要结果)

## 💡 优势与局限性
### 优势:
- ...
### 局限性:
- ...

## 🔮 未来研究方向
(基于论文内容，提出可能的后续研究方向)

## 📝 关键要点总结
(用3-5个要点总结论文的核心贡献)
```""",
        
        "英文简洁模板": """### Task
You are an AI research expert. Please analyze the following paper and provide a concise summary.

### Paper Information
Title: {title}
Authors: {authors}
Abstract: {abstract}
Full Text: {pdf_text}

### Output Format
```
## 📄 Paper Summary | {title}

## 🎯 Problem & Motivation
...

## 🛠️ Method
...

## 📊 Experiments
...

## 💭 Takeaways
...
```""",
        
        "自定义模板": ""
    }
    
    if prompt_type == "自定义模板":
        custom_prompt = st.text_area(
            "自定义 Prompt",
            value="",
            height=300,
            help="可用占位符: {title}, {abstract}, {authors}, {year}, {url}, {pdf_text}, {full_pdf_text}, {doi}, {arxiv_id}"
        )
    else:
        custom_prompt = prompt_templates[prompt_type]
        st.markdown('<div class="prompt-preview">', unsafe_allow_html=True)
        st.markdown("**当前 Prompt 预览:**")
        st.text_area("Prompt预览", custom_prompt, height=300, disabled=True, label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # 显示可用占位符
    with st.expander("📝 可用占位符说明"):
        placeholders = [
            "{title} - 论文标题",
            "{abstract} - 论文总结", 
            "{authors} - 作者信息",
            "{year} - 发表年份",
            "{url} - 论文链接",
            "{pdf_text} - 论文全文(截断版)",
            "{full_pdf_text} - 论文全文(完整版)",
            "{doi} - DOI 信息",
            "{arxiv_id} - arXiv ID"
        ]
        for placeholder in placeholders:
            st.write(f"• {placeholder}")

# 生成综述按钮
st.header("🚀 生成综述")

with st.form("bib_survey_form"):
    output_filename = st.text_input("输出文件名", value="survey_from_bib_result.md")
    submitted = st.form_submit_button("🎯 开始生成综述", use_container_width=True)

# 进度显示区域
progress_placeholder = st.empty()
paper_list_placeholder = st.empty()
summary_placeholder = st.empty()
download_placeholder = st.empty()

if submitted:
    if st.session_state.bib_content is None:
        st.warning("⚠️ 请先上传 BIB 文件")
    elif len(st.session_state.all_papers) == 0:
        st.warning("⚠️ 没有找到可处理的论文")
    else:
        try:
            # 创建临时文件保存BIB内容
            with tempfile.NamedTemporaryFile(mode='w', suffix='.bib', delete=False, encoding='utf-8') as tmp_file:
                tmp_file.write(st.session_state.bib_content)
                temp_bib_path = tmp_file.name
            
            progress_placeholder.info("📚 开始并行处理 BIB 文件...")
            
            # 确定使用的prompt
            final_prompt = custom_prompt if custom_prompt.strip() else None
            
            # 并行生成综述
            output_path = generate_survey_from_bib_parallel(
                bib_file=temp_bib_path,
                output_file=f"output/{output_filename}",
                llm_provider=llm_provider,
                model_name=model_name,
                custom_prompt=final_prompt,
                pdf_dir="pdfs/",
                progress_placeholder=progress_placeholder,
                paper_list_placeholder=paper_list_placeholder,
                max_workers=max_workers
            )
            
            if output_path and Path(output_path).exists():
                # 读取生成的markdown内容
                markdown_content = Path(output_path).read_text(encoding='utf-8')
                
                # 显示预览
                summary_placeholder.markdown("### 📋 综述预览")
                with summary_placeholder.expander("查看生成的综述", expanded=True):
                    # 预处理markdown内容，移除代码块标记让内容正常显示
                    def replace_code_blocks(match):
                        return match.group(1)
                    
                    display_markdown = re.sub(r'```[a-zA-Z]*\n(.*?)\n```', replace_code_blocks, markdown_content, flags=re.DOTALL)
                    st.markdown(display_markdown)
                
                # 生成HTML版本
                import markdown
                # 预处理markdown内容，移除代码块标记让内容正常渲染
                processed_markdown = markdown_content
                # 替换markdown代码块为普通段落 - 修复正则表达式
                def replace_code_blocks(match):
                    return match.group(1)
                
                processed_markdown = re.sub(r'```[a-zA-Z]*\n(.*?)\n```', replace_code_blocks, processed_markdown, flags=re.DOTALL)
                # 生成HTML
                html_content = markdown.markdown(processed_markdown, extensions=['tables', 'fenced_code', 'nl2br'])
                
                # 下载按钮
                download_placeholder.markdown("### 📥 下载结果")
                col_download1, col_download2 = download_placeholder.columns(2)
                
                with col_download1:
                    st.download_button(
                        "📄 下载 Markdown 文件",
                        markdown_content,
                        file_name=output_filename,
                        mime="text/markdown"
                    )
                
                with col_download2:
                    st.download_button(
                        "🌐 下载 HTML 文件", 
                        html_content,
                        file_name=output_filename.replace('.md', '.html'),
                        mime="text/html"
                    )
            else:
                progress_placeholder.error("❌ 综述生成失败")
            
            # 清理临时文件
            try:
                os.unlink(temp_bib_path)
            except:
                pass
                
        except Exception as e:
            progress_placeholder.error(f"❌ 处理过程中出现错误: {e}")
            st.exception(e)

# 使用说明
with st.expander("📖 使用说明"):
    st.markdown("""
    ### 🎯 功能特点
    
    1. **BIB 文件支持**: 上传您的 BibTeX 文件，自动解析论文信息
    2. **智能论文识别**: 
       - 🆔 **arXiv ID 识别**: 自动提取包含 arXiv ID 的论文
       - 🔍 **多层标题搜索**: 对没有 arXiv ID 的论文，采用三层搜索策略：
         * 精确标题匹配
         * 灵活标题搜索
         * 关键词组合搜索
       - 🧹 **标题清理**: 自动清理标题中的特殊字符（如 {}、\\ 等）
       - 🎯 **智能匹配**: 综合词汇重叠度、字符相似度和长度相似度进行匹配
    3. **全流程并行处理**: 
       - 🔍 **并行arXiv搜索**: 同时获取多篇论文的详细信息
       - 📥 **并行PDF处理**: 同时下载和处理多个PDF文件
       - ✨ **并行LLM总结**: 并行生成论文总结，大幅提升效率
    4. **实时进度显示**: 详细的进度条和状态更新
    5. **自定义 Prompt**: 支持多种预设模板和完全自定义的 Prompt
    6. **多格式输出**: 同时生成 Markdown 和 HTML 格式的综述
    
    ### 📝 使用步骤
    
    1. **上传文件**: 选择您的 BibTeX 文件上传
    2. **配置参数**: 选择 LLM 模型和并行处理线程数
    3. **配置 Prompt**: 选择预设模板或自定义 Prompt
    4. **生成综述**: 点击生成按钮，享受全流程并行处理的高效体验
    5. **下载结果**: 获取生成的综述文件
    
    ### ⚡ 并行处理优势
    
    - **arXiv搜索并行**: 同时查询多个论文ID，大幅减少网络等待时间
    - **论文下载并行**: 同时下载多个论文PDF，显著提升处理速度
    - **LLM总结并行**: 并行调用LLM生成总结，充分利用计算资源
    - **可调节线程数**: 根据系统性能和网络状况调整并行度
    
    ### 🔧 性能调优建议
    
    - **网络良好**: 可将线程数设置为6-8，加快arXiv搜索和下载
    - **网络一般**: 建议使用3-4个线程，平衡速度和稳定性
    - **系统资源有限**: 使用1-2个线程，确保系统稳定运行
    
    ### 💡 Prompt 占位符
    
    在自定义 Prompt 中，您可以使用以下占位符来插入论文信息：
    - `{title}` - 论文标题
    - `{abstract}` - 论文总结
    - `{authors}` - 作者信息
    - `{year}` - 发表年份
    - `{pdf_text}` - 论文全文(截断版，约10000字符)
    - `{full_pdf_text}` - 论文全文(完整版)
    
    ### ⚠️ 注意事项
    
    - 支持包含 arXiv ID 的论文和通过标题搜索的论文
    - **标题搜索优化**: 采用多层搜索策略，显著提高匹配成功率
    - **HTML 输出优化**: 自动处理代码块标记，确保论文内容正确渲染
    - 并行处理会提升速度，但也会增加网络和系统资源消耗
    - arXiv API有速率限制，过高的并行度可能导致请求失败
    - 建议在网络稳定的环境下使用，以获得最佳体验
    """)

# 页脚
st.markdown("---")
st.markdown("💡 **提示**: 现在支持智能论文识别和全流程并行处理！采用多层搜索策略提高论文匹配成功率，并优化HTML输出格式，让综述内容更完整、更美观。")
