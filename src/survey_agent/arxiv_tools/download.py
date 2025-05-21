import os
import fitz  # PyMuPDF
from pathlib import Path
from typing import Dict, Any, Optional

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
            paper.download_pdf(filename=pdf_path)
            tqdm.write(f"Downloaded `{paper.title}` to `{pdf_path}`")
        except Exception as e:
            tqdm.write(f"Error downloading `{paper.title}`: {e}")
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
        'title': paper.title,
        'authors': ', '.join([str(author) for author in paper.authors]),
        'summary': paper.summary,
        'url': paper.entry_id,
        'pdf_url': paper.pdf_url,
        'published': paper.published,
        'comment': paper.comment if hasattr(paper, 'comment') else "",
        'pdf_path': pdf_path,
    }
    
    # Extract text from PDF if it exists
    if os.path.exists(pdf_path):
        paper_info['pdf_text'] = extract_text_from_pdf(pdf_path)
    else:
        paper_info['pdf_text'] = ""
    
    return paper_info 