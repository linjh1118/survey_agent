import re
import json
import pandas as pd
from pathlib import Path
from typing import List, Dict, Any, Union

from tqdm import tqdm

from ..arxiv_tools.search import search_papers
from ..arxiv_tools.download import process_paper
from ..llm.summarize import get_summarizer



def summarize_papers(papers: List[Dict[str, Any]], 
                    llm_provider: str = "openai", 
                    model_name: str = None) -> List[Dict[str, Any]]:
    """
    Generate summaries for a list of papers.
    
    Args:
        papers: List of paper dictionaries
        llm_provider: LLM provider to use
        model_name: Name of the model to use
        
    Returns:
        List of paper dictionaries with summaries
    """
    summarizer = get_summarizer(llm_provider, model_name)
    
    for paper in tqdm(papers, desc="Summarizing papers"):
        if 'llm_summary_res' not in paper:
            paper['llm_summary_res'] = summarizer.summarize(paper)
    
    return papers

def generate_markdown(papers: List[Dict[str, Any]], 
                     output_file: str,
                     terms: List[str] = None) -> str:
    """
    Generate a markdown survey from a list of papers.
    
    Args:
        papers: List of paper dictionaries with summaries
        output_file: Path to save the markdown file
        terms: Search terms used to find the papers
        
    Returns:
        Generated markdown content
    """
    output_path = Path(output_file)
    
    # Generate header
    if terms:
        table_content = '# Paper List of Terms(' + '+'.join(terms) + ')\n'
    else:
        table_content = '# Paper List\n'
    
    tldr_content = '# TLDR/Notes\n'
    
    for paper in papers:
        # Prepare paper info
        title = paper['title']
        
        # Extract year/month from URL
        url = paper['url']
        pattern = r"abs/(\d{4})\."
        match = re.search(pattern, url)
        year_month_str = match.group(1)[:2] + '/' + match.group(1)[2:] if match else "YY/MM"
        
        # Extract project page if available
        page_url = re.findall(r'https?://[^\s]+', paper['summary'])
        code_or_page = page_url[0] if page_url else ""
        
        # Generate anchor for linking
        no_biaodian_title = re.sub(r'[,:.?"\']', ' ', title).replace(' ', '-').lower()
        
        # Add to table of contents
        markdown_table_content = f"""- [{year_month_str}] **{title}**  
[[Paper]({paper['pdf_url']})] [[Code/Page]({code_or_page})] [[TLDR/Notes](#{no_biaodian_title})]"""
        
        table_content += markdown_table_content + '\n\n'
        
        # Add paper summary
        cur_paper_tldr = f"## {no_biaodian_title}\n"
        cur_paper_tldr += f"### Abstract\n{paper['summary']}\n"
        cur_paper_tldr += paper['llm_summary_res'].replace('##', '###')
        tldr_content += cur_paper_tldr + '\n\n'
    
    # Combine content
    markdown_content = table_content + '\n\n' + tldr_content
    
    # Save to file
    output_path.write_text(markdown_content, encoding='utf-8')
    print(f"Saved markdown survey to {output_path}")
    
    return markdown_content

def generate_survey(papers=None, 
                   terms=None, 
                   titles=None, 
                   max_results=100,
                   output_file="survey_result.md",
                   llm_provider="openai",
                   model_name=None,
                   pdf_dir=None):
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
        pdf_dir: Directory to save PDFs
        
    Returns:
        Path to the generated markdown file
    """
    # Step 1: Search for papers if not provided
    if papers is None:
        if not terms and not titles:
            raise ValueError("Either papers, terms, or titles must be provided")
        
        papers = search_papers(terms=terms, titles=titles, max_results=max_results)
    
    # Step 2: Process papers (download PDFs and extract text)
    processed_papers = [process_paper(paper, pdf_dir) for paper in tqdm(papers, desc="Processing papers")]
    
    
    
    # Step 3: Generate summaries
    summarized_papers = summarize_papers(processed_papers, llm_provider, model_name)
    
    # Step 4: Generate markdown
    generate_markdown(summarized_papers, output_file, terms)
    
    return output_file 