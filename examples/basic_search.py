from tqdm import tqdm
from survey_agent.arxiv_tools import search_papers
from survey_agent.arxiv_tools import process_paper
from survey_agent.utils import save_papers_to_jsonl

def main():
    """
    Example script showing how to search for papers on arXiv and process them.
    This demonstrates:
    1. Searching for papers by keywords
    2. Processing papers (downloading PDFs and extracting text)
    3. Saving the processed papers to a JSONL file
    """
    # Step 1: Search for papers with specific keywords
    print("🔍 Searching for papers about VLM and Games...")
    papers = search_papers(terms=["VLM", "Games"], max_results=10)
    
    print(f"📚 Found {len(papers)} papers")
    
    # Step 2: Process papers (download PDFs and extract text)
    print("⏳ Processing papers (downloading PDFs and extracting text)...")
    processed_papers = [process_paper(paper, pdf_dir="./pdfs") for paper in tqdm(papers, desc="Processing papers", position=0)]
    
    # Step 3: Save to JSONL file
    print("💾 Saving papers to JSONL file...")
    save_papers_to_jsonl(processed_papers, "vlm_games_papers.jsonl")
    
    print("✅ Done! Papers saved to vlm_games_papers.jsonl")

if __name__ == "__main__":
    main() 