import arxiv
from typing import List, Dict, Any, Optional
from fuzzywuzzy import fuzz

def search_papers_by_terms(terms: List[str], max_results: int = 100) -> List[Dict[Any, Any]]:
    """
    Search for papers on arXiv based on a list of terms.
    
    Args:
        terms: List of search terms
        max_results: Maximum number of results to return
        
    Returns:
        List of paper dictionaries
    """
    client = arxiv.Client()
    
    # Create query string for title search
    query_string_title = " AND ".join([f'ti:"{term}"' for term in terms])
    
    # Create query string for abstract search
    query_string_abs = " AND ".join([f'abs:"{term}"' for term in terms])
    
    # Combine both queries
    query_string = f"({query_string_title}) OR ({query_string_abs})"
    
    search = arxiv.Search(
        query=query_string,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )
    
    results = list(client.results(search))
    return results

def search_paper_by_title(paper_title: str) -> Optional[Dict[Any, Any]]:
    """
    Search for a specific paper by title.
    
    Args:
        paper_title: The title of the paper to search for
        
    Returns:
        Paper object if found, None otherwise
    """
    # Clean up title for search
    tidy_title = paper_title.replace(':', '').strip()
    tidy_title = ' '.join(tidy_title.split())  # Remove extra spaces
    
    client = arxiv.Client()
    search = arxiv.Search(query=f'ti:{tidy_title}', max_results=20)
    
    try:
        results = list(client.results(search))
        if not results:
            return None
        
        # Find the best match using fuzzy matching
        best_match = max(results, key=lambda result: fuzz.ratio(paper_title.lower(), result.title.lower()))
        return best_match
    except Exception as e:
        print(f"Error searching for paper: {e}")
        return None

def search_papers(terms=None, titles=None, max_results=100):
    """
    Search for papers on arXiv by terms or titles.
    
    Args:
        terms: List of search terms (e.g., ["VLM", "Games"])
        titles: List of paper titles to search for
        max_results: Maximum number of results per search
        
    Returns:
        List of paper objects
    """
    results = []
    
    if terms:
        if isinstance(terms[0], list):
            # Multiple term groups
            for term_group in terms:
                results.extend(search_papers_by_terms(term_group, max_results))
        else:
            # Single term group
            results.extend(search_papers_by_terms(terms, max_results))
    
    if titles:
        for title in titles:
            paper = search_paper_by_title(title)
            if paper:
                results.append(paper)
    
    return results 