import re
import json
import pandas as pd
from pathlib import Path
from typing import List, Dict, Any, Union

from tqdm import tqdm

from ..arxiv_tools.search import search_papers
from ..arxiv_tools.download import process_paper
from ..llm.summarize import get_summarizer
from ..utils.bib_parser import parse_bib_file, BibParser

def summarize_papers(papers: List[Dict[str, Any]], 
                    llm_provider: str = "openai", 
                    model_name: str = None,
                    custom_prompt: str = None) -> List[Dict[str, Any]]:
    """
    Generate summaries for a list of papers.
    
    Args:
        papers: List of paper dictionaries
        llm_provider: LLM provider to use
        model_name: Name of the model to use
        custom_prompt: Custom prompt template for summarization
        
    Returns:
        List of paper dictionaries with summaries
    """
    summarizer = get_summarizer(llm_provider, model_name, custom_prompt)
    
    for paper in tqdm(papers, desc="Summarizing papers"):
        if 'llm_summary_res' not in paper:
            paper['llm_summary_res'] = summarizer.summarize(paper)
    
    return papers

def generate_markdown(papers: List[Dict[str, Any]], 
                     output_file: str,
                     terms: List[str] = None,
                     bib_file: str = None) -> str:
    """
    Generate a markdown survey from a list of papers.
    
    Args:
        papers: List of paper dictionaries with summaries
        output_file: Path to save the markdown file
        terms: Search terms used to find the papers
        bib_file: BIB file path if papers were loaded from BIB
        
    Returns:
        Generated markdown content
    """
    output_path = Path(output_file)
    
    # Generate header
    if bib_file:
        table_content = f'# Paper List from BIB File: {Path(bib_file).name}\n'
    elif terms:
        table_content = '# Paper List of Terms(' + '+'.join(terms) + ')\n'
    else:
        table_content = '# Paper List\n'
    
    tldr_content = '# TLDR/Notes\n'
    
    for paper in papers:
        # Prepare paper info
        title = paper['title']
        
        # Extract year/month from URL or use provided year
        year_month_str = "YY/MM"
        if paper.get('year'):
            year_month_str = f"{paper['year'][:2]}/{paper['year'][2:]}" if len(paper['year']) >= 4 else paper['year']
        elif paper.get('url'):
            url = paper['url']
            pattern = r"abs/(\d{4})\."
            match = re.search(pattern, url)
            year_month_str = match.group(1)[:2] + '/' + match.group(1)[2:] if match else "YY/MM"
        
        # Extract project page if available
        summary_text = paper.get('summary', '')
        page_url = re.findall(r'https?://[^\s]+', summary_text)
        code_or_page = page_url[0] if page_url else ""
        
        # Generate anchor for linking
        no_biaodian_title = re.sub(r'[,:.?"\']', ' ', title).replace(' ', '-').lower()
        
        # Add to table of contents
        pdf_url = paper.get('pdf_url', paper.get('url', ''))
        markdown_table_content = f"""- [{year_month_str}] **{title}**  
[[Paper]({pdf_url})] [[Code/Page]({code_or_page})] [[TLDR/Notes](#{no_biaodian_title})]"""
        
        table_content += markdown_table_content + '\n\n'
        
        # Add paper summary
        cur_paper_tldr = f"## {no_biaodian_title}\n"
        cur_paper_tldr += f"### Abstract\n{summary_text}\n"
        if 'llm_summary_res' in paper and paper['llm_summary_res']:
            cur_paper_tldr += paper['llm_summary_res'].replace('##', '###')
        tldr_content += cur_paper_tldr + '\n\n'
    
    # Combine content
    markdown_content = table_content + '\n\n' + tldr_content
    
    # Save to file
    output_path.write_text(markdown_content, encoding='utf-8')
    print(f"Saved markdown survey to {output_path}")
    
    return markdown_content

def generate_survey_from_bib(bib_file: str,
                           output_file: str = "survey_from_bib.md",
                           llm_provider: str = "openai",
                           model_name: str = None,
                           custom_prompt: str = None,
                           pdf_dir: str = None) -> str:
    """
    Generate a complete survey from a BIB file.
    
    Args:
        bib_file: Path to the BIB file
        output_file: Path to save the markdown file
        llm_provider: LLM provider to use
        model_name: Name of the model to use
        custom_prompt: Custom prompt template for summarization
        pdf_dir: Directory to save PDFs
        
    Returns:
        Path to the generated markdown file
    """
    # Step 1: Parse BIB file and get arxiv papers
    print(f"📚 Parsing BIB file: {bib_file}")
    papers = parse_bib_file(bib_file)  # 现在返回的是真实的arxiv paper对象列表
    
    if not papers:
        print("❌ No arXiv papers found in BIB file")
        return None
    
    print(f"✅ Found {len(papers)} arXiv papers in BIB file")
    
    # Step 2: Process papers (download PDFs and extract text)
    print("📥 Processing papers...")
    processed_papers = []
    for paper in tqdm(papers, desc="Processing papers"):
        try:
            processed_paper = process_paper(paper, pdf_dir)
            if processed_paper:  # 只添加成功处理的论文
                processed_papers.append(processed_paper)
        except Exception as e:
            print(f"⚠️ Error processing paper '{paper.title}': {e}")
            continue
    
    if not processed_papers:
        print("❌ No papers were successfully processed")
        return None
    
    # Step 3: Generate summaries
    print("🤖 Generating summaries...")
    summarized_papers = summarize_papers(processed_papers, llm_provider, model_name, custom_prompt)
    
    # Step 4: Generate markdown
    print("📝 Generating markdown...")
    generate_markdown(summarized_papers, output_file, bib_file=bib_file)
    
    return output_file

def generate_survey(papers=None, 
                   terms=None, 
                   titles=None, 
                   max_results=100,
                   output_file="survey_result.md",
                   llm_provider="openai",
                   model_name=None,
                   custom_prompt=None,
                   pdf_dir=None,
                   bib_file=None):
    """
    Generate a complete survey from search to markdown generation.
    
    Args:
        papers: Pre-fetched paper objects (optional)
        terms: Search terms to use if papers not provided
        titles: Paper titles to search for if papers not provided
        max_results: Maximum number of results per search
        output_file: Path to save the markdown file
        llm_provider: LLM provider to use
        model_name: Name of the model to use
        custom_prompt: Custom prompt template for summarization
        pdf_dir: Directory to save PDFs
        bib_file: Path to BIB file to load papers from
        
    Returns:
        Path to the generated markdown file
    """
    # Step 1: Get papers from various sources
    if bib_file:
        # Generate survey from BIB file
        return generate_survey_from_bib(
            bib_file=bib_file,
            output_file=output_file,
            llm_provider=llm_provider,
            model_name=model_name,
            custom_prompt=custom_prompt,
            pdf_dir=pdf_dir
        )
    elif papers is None:
        # Search for papers if not provided
        if not terms and not titles:
            raise ValueError("Either papers, terms, titles, or bib_file must be provided")
        
        papers = search_papers(terms=terms, titles=titles, max_results=max_results)
    
    # Step 2: Process papers (download PDFs and extract text)
    processed_papers = [process_paper(paper, pdf_dir) for paper in tqdm(papers, desc="Processing papers")]
    
    # Step 3: Generate summaries
    summarized_papers = summarize_papers(processed_papers, llm_provider, model_name, custom_prompt)
    
    # Step 4: Generate markdown
    generate_markdown(summarized_papers, output_file, terms)
    
    return output_file 