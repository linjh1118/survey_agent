import re
from typing import List, Dict, Any

def clean_title(title: str) -> str:
    """
    Clean a paper title for searching.
    
    Args:
        title: Paper title
        
    Returns:
        Cleaned title
    """
    # Remove special characters and extra spaces
    cleaned = title.replace(':', '').strip()
    cleaned = ' '.join(cleaned.split())  # Remove extra spaces
    return cleaned

def extract_project_url(summary: str) -> str:
    """
    Extract project URL from paper summary.
    
    Args:
        summary: Paper summary
        
    Returns:
        Project URL if found, empty string otherwise
    """
    urls = re.findall(r'https?://[^\s]+', summary)
    return urls[0] if urls else ""

def truncate_text(text: str, max_length: int = 10000) -> str:
    """
    Truncate text to a maximum length.
    
    Args:
        text: Text to truncate
        max_length: Maximum length
        
    Returns:
        Truncated text
    """
    if len(text) <= max_length:
        return text
    
    # Try to truncate at a paragraph boundary
    paragraphs = text[:max_length].split('\n\n')
    if len(paragraphs) > 1:
        return '\n\n'.join(paragraphs[:-1]) + '\n\n[Text truncated...]'
    
    # If no paragraph boundary, truncate at the maximum length
    return text[:max_length] + '\n[Text truncated...]' 