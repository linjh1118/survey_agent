import os
import json
import pandas as pd
from pathlib import Path
from typing import List, Dict, Any, Union

def ensure_directory(directory: str) -> str:
    """
    Ensure a directory exists.
    
    Args:
        directory: Directory path
        
    Returns:
        The directory path
    """
    os.makedirs(directory, exist_ok=True)
    return directory

def save_papers_to_jsonl(papers: List[Dict[str, Any]], output_file: str) -> str:
    """
    Save papers to a JSONL file.
    
    Args:
        papers: List of paper dictionaries
        output_file: Path to save the JSONL file
        
    Returns:
        Path to the saved file
    """
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    pd.DataFrame(papers).to_json(
        output_path, 
        orient='records', 
        lines=True, 
        force_ascii=False
    )
    
    print(f"Saved papers to {output_path}")
    return str(output_path)

def load_papers_from_jsonl(input_file: str) -> List[Dict[str, Any]]:
    """
    Load papers from a JSONL file.
    
    Args:
        input_file: Path to the JSONL file
        
    Returns:
        List of paper dictionaries
    """
    input_path = Path(input_file)
    if not input_path.exists():
        raise FileNotFoundError(f"File not found: {input_file}")
    
    papers = pd.read_json(input_path, lines=True).to_dict(orient='records')
    return papers 