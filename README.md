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
git clone https://github.com/linjh1118/survey_agent.git
cd survey_agent
pip install -e .
```

## 🚀 Quick Start

### 1. Using Web Interface (Recommended)

The easiest way to get started is using our interactive web interface:

```bash
streamlit run src/survey_agent/frontend.py
```

This will launch a user-friendly interface where you can:

- Input search keywords
- Track real-time progress
- View paper titles as they're found
- Download surveys in both markdown and HTML formats

📺 **User Case**

https://github.com/linjh1118/survey_agent/blob/main/.github/assets/demo.mp4

<video width="100%" controls>
  <source src="output/362_1747830210.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

### 2. Using Python API

Alternatively, you can use the Python API directly:

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

## 🏃🏻‍♀️🏃🏻‍♀️

 If you `python examples/generate_survey.py`, you will get `output/vlm_games_survey.md`
--> check [output/vlm_games_survey.md](output/vlm_games_survey.md) . The log is at [output/vlm_games_survey.log](output/vlm_games_survey.log).

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


## 📊 Some Details

Running the example script `（python examples/generate_survey.py`） will:

1. Search arXiv for papers matching the keywords "VLM" and "Games"
2. Download the top 10 papers as PDFs to the `pdfs/` directory
3. Generate a comprehensive survey in `output/vlm_games_survey.md`

The generated survey includes:

- A list of all papers with links to the original papers
- TLDR/Notes section with detailed summaries of each paper
- Paper abstracts and key insights


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

Contributors:

<a href="https://github.com/linjh1118/survey_agent/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=linjh1118/survey_agent" />
</a>

## 📜 License

MIT

## Streamlit 前端使用说明

### 依赖安装

```bash
pip install -r requirements.txt
```

### 启动前端

```bash
streamlit run src/survey_agent/frontend.py
```

### 功能说明

- 输入关键词，自动检索、下载、总结论文并生成综述。
- 实时展示进度和已查到的论文标题。
- 支持下载 markdown 和 html 格式的综述。
