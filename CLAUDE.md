# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Core Architecture

Survey Agent is a Python framework for automatically generating research literature surveys by:
1. Searching arXiv papers by keywords or parsing BibTeX files
2. Downloading PDFs and extracting text content  
3. Using LLMs to generate paper summaries with intelligent caching
4. Creating well-formatted markdown surveys

**Key Components:**
- `src/survey_agent/arxiv_tools/` - ArXiv search and PDF download functionality
- `src/survey_agent/llm/summarize.py` - LLM integration with caching and custom prompts
- `src/survey_agent/survey/generator.py` - Survey generation pipeline
- `src/survey_agent/utils/` - BibTeX parsing, caching, and utilities
- Frontend interfaces for web-based usage

## Development Commands

### Installation & Setup
```bash
pip install -e .
# Install from requirements.txt: pip install -r requirements.txt
```

### Running the Application

**Web Interfaces:**
```bash
# Standard keyword search interface
streamlit run src/survey_agent/frontend.py
# Alternative: ./launch.sh

# BibTeX file interface  
streamlit run src/survey_agent/frontend_by_bib.py
# Alternative: ./launch_bib.sh

# PDF viewer and batch Q&A interface
python3 pdf_api.py
# Alternative: ./launch_pdf_viewer.sh
# Access at: http://localhost:8002/pdf_viewer.html
```

**Python API Usage:**
```python
# Standard search
from survey_agent.survey import generate_survey
generate_survey(terms=["AI", "ML"], max_results=10, output_file="output/survey.md")

# From BibTeX file
from survey_agent.survey import generate_survey_from_bib
generate_survey_from_bib(bib_file="papers.bib", output_file="output/survey.md")
```

### Environment Variables

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

### File Structure
- `pdfs/` - Downloaded paper PDFs
- `output/` - Generated survey markdown files
- `cache/` - Intelligent caching system
- `examples/` - Usage examples for both search and BibTeX workflows

### Error Handling
- Graceful handling of malformed BibTeX entries
- Retry mechanisms for PDF downloads
- Progress tracking for long-running operations
- Continues processing even if individual papers fail

## Testing
No formal test framework configured. Test manually using:
- `python examples/basic_search.py`
- `python examples/generate_survey.py` 
- `python examples/generate_survey_by_bib.py`

## Dependencies
Core: streamlit, arxiv, PyMuPDF, openai, pandas, tqdm, fuzzywuzzy, python-Levenshtein
See `requirements.txt` and `setup.py` for complete list.