# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Core Architecture

Survey Agent is a Python framework for automatically generating research literature surveys by:
1. Searching arXiv papers by keywords or parsing BibTeX files
2. Downloading PDFs and extracting text content  
3. Using LLMs to generate paper summaries with intelligent caching
4. Crawling paper images and captions from arXiv HTML pages
5. Creating well-formatted markdown and HTML surveys

**Key Components:**
- `src/survey_agent/arxiv_tools/` - ArXiv search, PDF download, and image crawling
- `src/survey_agent/llm/summarize.py` - LLM integration with caching and custom prompts
- `src/survey_agent/survey/generator.py` - Survey generation pipeline
- `src/survey_agent/utils/` - BibTeX parsing, caching, and utilities
- `src/survey_agent/frontend.py` - Query-based search interface
- `src/survey_agent/frontend_by_bib.py` - BibTeX file interface

## Entry Points (Only Two)

### 1. Query-Based Search Entry Point
```bash
./launch.sh
# Or: streamlit run src/survey_agent/frontend.py
```
**Features:**
- 1.1 Input query keywords to search arXiv
- 1.2 LLM paper interpretation and summarization
- 1.3 Image and caption crawling from arXiv HTML

### 2. BibTeX File Entry Point
```bash
./launch_bib.sh
# Or: streamlit run src/survey_agent/frontend_by_bib.py
```
**Features:**
- 2.1 Upload BibTeX file for paper parsing
- 2.2 LLM paper interpretation and summarization
- 2.3 Image and caption crawling from arXiv HTML

## Installation & Setup
```bash
pip install -e .
# Or: pip install -r requirements.txt
```

## Environment Variables

Required for LLM functionality:
```bash
export API_KEY="your_api_key_here"
export BASE_URL="your_api_base_url"
```

Optional proxy settings:
```bash
export https_proxy="http://127.0.0.1:7890"
export http_proxy="http://127.0.0.1:7890"
```

## Important Implementation Details

### Caching System
- Papers are cached in `cache/paper_summaries.json` based on arXiv ID
- 30-day auto-expiry with content hash validation
- Provides 200-1000x speedup for repeated queries
- Cache management in `src/survey_agent/utils/cache.py`

### Custom Prompts
- Support for templated prompts with placeholders: `{title}`, `{authors}`, `{abstract}`, `{pdf_text}`, etc.
- Default Chinese academic prompt in `src/survey_agent/llm/summarize.py:34`
- Custom prompts can be passed to all generation functions

### Parallel Processing
- Both frontends support parallel processing for arXiv search, PDF download, LLM summarization, and image crawling
- Configurable thread count (1-8 workers) via UI slider
- Significantly improves processing speed for multiple papers

### File Structure
- `pdfs/` - Downloaded paper PDFs
- `output/` - Generated survey markdown files
- `cache/` - Intelligent caching system
- `examples/` - Usage examples for both search and BibTeX workflows
- `paper_captions_*/` - Crawled images and captions (generated at runtime)

### Error Handling
- Graceful handling of malformed BibTeX entries
- Retry mechanisms for PDF downloads
- Progress tracking for long-running operations
- Continues processing even if individual papers fail

## Testing
No formal test framework configured. Test manually using the two entry points:
- `./launch.sh` - Test query-based search
- `./launch_bib.sh` - Test BibTeX file processing

## Dependencies
Core: streamlit, arxiv, PyMuPDF, openai, pandas, tqdm, fuzzywuzzy, python-Levenshtein, beautifulsoup4, requests
See `requirements.txt` and `setup.py` for complete list.