# 📚 Survey Agent

A modern framework for automatically generating research surveys by searching arXiv papers, downloading them, and using LLMs to summarize their content. Perfect for researchers, students, and anyone who wants to stay up-to-date with the latest research! ✨

## ✅ Features

- 🔍 Search arXiv papers by keywords or specific titles
- 📥 Download PDFs and extract text content
- 🤖 Generate summaries of papers using LLMs (supports various models including GLM-4)
- 📝 Create well-formatted markdown surveys with paper lists and summaries
- 🚀 Simple and intuitive API

## 🛠️ Installation

```bash
git clone https://github.com/yourusername/survey_agent.git
cd survey_agent
pip install -e .
```

## 🚀 Quick Start

Here's a complete example of how to use Survey Agent to generate a research survey:

```python
import os
os.environ.update({"https_proxy": "http://127.0.0.1:7890", "http_proxy": "http://127.0.0.1:7890"})
os.environ.update({"API_KEY": "your_api_key_here", "BASE_URL": "your_api_url"})

from survey_agent.survey import generate_survey

generate_survey(
    terms=["VLM", "Games"],
    max_results=10,
    output_file="output/vlm_games_survey.md",
    model_name="glm-4-air"
)
```

## 📊 Output

Running the example script will:

1. Search arXiv for papers matching the keywords "VLM" and "Games"
2. Download the top 10 papers as PDFs to the `pdfs/` directory
3. Generate a comprehensive survey in `output/vlm_games_survey.md`

The generated survey includes:

- A list of all papers with links to the original papers
- TLDR/Notes section with detailed summaries of each paper
- Paper abstracts and key insights

🏃🏻‍♀️🏃🏻‍♀️ 

 If you `python examples/generate_survey.md`, you will get `output/vlm_games_survey.md`
--> check [output/vlm_games_survey.md](output/vlm_games_survey.md "output/vlm_games_survey.md") . The log is at [output/vlm_games_survey.log](output/vlm_games_survey.md "output/vlm_games_survey.md").

<table>
  <tr>
    <td><img src="output/vlm_game.png" alt="Column Toggle"></td>
    <td><img src="output/vlm_game2.png" alt="Expanded View"></td>
  </tr>
  <tr>
    <td align="center">Page1</td>
    <td align="center">Page2 of survey</td>
  </tr>
</table>

## 🏗️ Project Structure

```
survey_agent/
├── examples/       # Example usage scripts
├── output/         # Generated survey markdown files
├── pdfs/           # Downloaded paper PDFs
└── src/
    └── survey_agent/
        ├── arxiv/  # ArXiv search and download functionality
        │   ├── search.py   # Search papers on arXiv
        │   └── download.py # Download PDFs from arXiv
        ├── llm/    # LLM integration for summarization
        ├── utils/  # Utility functions
        └── survey/ # Survey generation tools
            └── generator.py # Generate markdown surveys
```

## ⚙️ Configuration

You can configure the LLM used for summarization by setting environment variables:

```python
# Set the LLM API key and base URL
import os
os.environ["API_KEY"] = 'your_api_key_here'
os.environ["BASE_URL"] = 'https://open.bigmodel.cn/api/paas/v4/'
```

## 🙋‍♂️ Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request if you have any improvements or bug fixes.

## 📜 License

MIT
