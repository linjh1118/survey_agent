import os
import fitz  # PyMuPDF
from pathlib import Path
from typing import Dict, Any, Optional
import time
import requests
from tqdm import tqdm

def ensure_pdf_dir(pdf_dir: str = None) -> str:
    """
    Ensure the PDF directory exists.
    
    Args:
        pdf_dir: Directory to save PDFs, defaults to './pdfs'
        
    Returns:
        Path to the PDF directory
    """
    if pdf_dir is None:
        pdf_dir = os.path.join(os.getcwd(), 'pdfs')
    
    os.makedirs(pdf_dir, exist_ok=True)
    return pdf_dir

def download_with_retry(url: str, output_path: str, max_retries: int = 5, initial_delay: int = 2) -> bool:
    """
    Download a file with retry mechanism
    
    Args:
        url: URL to download from
        output_path: Path to save the file
        max_retries: Maximum number of retry attempts
        initial_delay: Initial delay between retries (will be exponentially increased)
        
    Returns:
        bool: Whether the download was successful
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    for attempt in range(max_retries):
        try:
            response = requests.get(url, headers=headers, stream=True)
            response.raise_for_status()
            
            with open(output_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            return True
            
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                tqdm.write(f"文件不存在 (404): {url}")
                return False
            delay = initial_delay * (2 ** attempt)
            tqdm.write(f"🔄 下载失败，{delay}秒后重试 (尝试 {attempt + 1}/{max_retries})")
            time.sleep(delay)
            
        except Exception as e:
            delay = initial_delay * (2 ** attempt)
            tqdm.write(f"🔄 下载出错 ({str(e)})，{delay}秒后重试 (尝试 {attempt + 1}/{max_retries})")
            time.sleep(delay)
    
    tqdm.write(f"❌ 下载失败，已达到最大重试次数: {url}")
    return False

def download_paper_pdf(paper, pdf_dir: str = None) -> str:
    """
    Download a paper's PDF.
    
    Args:
        paper: ArXiv paper object
        pdf_dir: Directory to save the PDF
        
    Returns:
        Path to the downloaded PDF
    """
    pdf_dir = ensure_pdf_dir(pdf_dir)
    
    # Create a safe filename from the title
    safe_title = "".join([c if c.isalnum() else "_" for c in paper.title])
    pdf_path = os.path.join(pdf_dir, f"{safe_title}.pdf")
    
    # Download if not already exists
    if not os.path.exists(pdf_path):
        try:
            if hasattr(paper, 'download_pdf'):
                paper.download_pdf(filename=pdf_path)
                tqdm.write(f"Downloaded `{paper.title}` to `{pdf_path}`")
            else:
                # 如果paper对象没有download_pdf方法，尝试直接从URL下载
                pdf_url = paper.pdf_url if hasattr(paper, 'pdf_url') else f"https://arxiv.org/pdf/{paper.get('arxiv_id')}.pdf"
                if download_with_retry(pdf_url, pdf_path):
                    tqdm.write(f"Downloaded `{paper.title}` to `{pdf_path}`")
                else:
                    return None
        except Exception as e:
            tqdm.write(f"Error downloading `{paper.title}`: {e}")
            return None
    else:
        tqdm.write(f"Skipping `{paper.title}` because it already exists")
    
    return pdf_path

def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extract text from a PDF file.
    
    Args:
        pdf_path: Path to the PDF file
        
    Returns:
        Extracted text
    """
    if not pdf_path or not os.path.exists(pdf_path):
        return ""
        
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        return text
    except Exception as e:
        tqdm.write(f"Error extracting text from {pdf_path}: {e}")
        return ""

def process_paper(paper, pdf_dir: str = None) -> Dict[str, Any]:
    """
    Process a paper: download PDF and extract text.
    
    Args:
        paper: ArXiv paper object
        pdf_dir: Directory to save the PDF
        
    Returns:
        Dictionary with paper information
    """
    pdf_path = download_paper_pdf(paper, pdf_dir)
    
    # Extract information
    paper_info = {
        'title': paper.title if hasattr(paper, 'title') else paper.get('title', ''),
        'authors': ', '.join([str(author) for author in paper.authors]) if hasattr(paper, 'authors') else paper.get('authors', ''),
        'summary': paper.summary if hasattr(paper, 'summary') else paper.get('summary', ''),
        'url': paper.entry_id if hasattr(paper, 'entry_id') else paper.get('url', ''),
        'pdf_url': paper.pdf_url if hasattr(paper, 'pdf_url') else paper.get('pdf_url', ''),
        'published': paper.published if hasattr(paper, 'published') else paper.get('published', ''),
        'comment': paper.comment if hasattr(paper, 'comment') else paper.get('comment', ''),
        'pdf_path': pdf_path,
    }
    
    # Extract text from PDF if it exists
    if pdf_path and os.path.exists(pdf_path):
        paper_info['pdf_text'] = extract_text_from_pdf(pdf_path)
    else:
        paper_info['pdf_text'] = ""
    
    return paper_info 