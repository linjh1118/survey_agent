# Try to import core search and download modules (require arxiv package)
try:
    from .search import search_papers, search_papers_by_terms, search_paper_by_title
    from .download import process_paper, download_paper_pdf, extract_text_from_pdf
except ImportError as e:
    # arxiv package might not be installed, skip these imports
    import warnings
    warnings.warn(f"Failed to import search/download modules: {e}. Some features may not be available.")

# Caption crawler and HTML generator (only require requests and beautifulsoup4)
from .caption_crawler import crawl_arxiv_html, batch_crawl_arxiv_ids
from .html_generator import generate_html_with_summary, parse_markdown_summaries, find_all_papers 