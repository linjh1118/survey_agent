from survey_agent.survey import generate_survey
from survey_agent.utils import load_papers_from_jsonl
import os

os.environ["https_proxy"] = "http://127.0.0.1:7890"
os.environ["http_proxy"] = "http://127.0.0.1:7890"
# os.environ["all_proxy"] = "socks5://127.0.0.1:7890"
os.environ["API_KEY"] = 'YOUR_API_KEY_HERE'
os.environ["BASE_URL"] = 'YOUR_BASE_URL_HERE'


def main():
    """
    Example script showing how to generate a research survey using Survey Agent.
    This demonstrates two approaches:
    1. Directly from search terms
    2. From pre-processed papers stored in a JSONL file
    """
    # Option 1: Generate survey from search terms
    print("🔍 Generating survey from search terms...")
    generate_survey(
        terms=["VLM", "Games"],
        max_results=10,
        output_file="output/vlm_games_survey.md",
        llm_provider="openai",  # just a python class name, not mean openai api
        model_name="YOUR_MODEL_NAME_HERE",
    )
    
    '''# Option 2: Generate survey from pre-processed papers
    print("📄 Loading pre-processed papers...")
    papers = load_papers_from_jsonl("vlm_games_papers.jsonl")
    
    print(f"✨ Generating survey from {len(papers)} pre-processed papers...")
    generate_survey(
        papers=papers,
        output_file="vlm_games_survey_from_jsonl.md"
    )
    
    print("✅ Done! Surveys generated.")'''

if __name__ == "__main__":
    main() 
