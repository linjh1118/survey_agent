import os
from survey_agent.survey import generate_survey_from_bib

# 设置环境变量
# 导入环境配置
from survey_agent import env

# 或者手动设置（如果需要的话）
# os.environ["https_proxy"] = "http://127.0.0.1:7890"
# os.environ["http_proxy"] = "http://127.0.0.1:7890"

def main():
    """
    Example script showing how to generate a research survey from a BIB file.
    This demonstrates:
    1. Loading papers from a BibTeX file
    2. Using a custom prompt for summarization
    3. Generating comprehensive survey reports
    """
    
    # 示例1: 使用默认论文总结prompt
    print("📚 Generating survey from BIB file with default prompt...")
    generate_survey_from_bib(
        bib_file=".github/assets/导出的条目.bib",
        output_file="output/survey_from_bib_default.md",
        llm_provider="openai",
        model_name="ep-20250529110941-khvtx",
        pdf_dir="pdfs/"
    )
    
    # 示例2: 使用自定义prompt
    print("🎯 Generating survey from BIB file with custom prompt...")
    
    # 自定义prompt示例 - 重点关注方法和实验
    custom_prompt = """### 任务
你是一个AI研究专家，请对以下论文进行专业的学术分析。

### 论文信息
#### 标题: {title}
#### 作者: {authors}
#### 年份: {year}
#### 摘要: {abstract}
#### 论文全文: {pdf_text}

### 分析要求
请从以下几个维度进行深度分析：

### 输出格式
```
## 📊 论文深度分析 | {title}

## 🎯 研究问题与动机
(简要描述论文要解决的核心问题和研究动机)

## 🔬 核心技术方法
(详细描述论文提出的主要技术方法和创新点)

## 📈 实验设计与结果
(分析实验设置、数据集、评估指标和主要结果)

## 💡 优势与局限性
### 优势:
- ...
### 局限性:
- ...

## 🔮 未来研究方向
(基于论文内容，提出可能的后续研究方向)

## 📝 关键要点总结
(用3-5个要点总结论文的核心贡献)
```
"""
    
    generate_survey_from_bib(
        bib_file=".github/assets/导出的条目.bib",
        output_file="output/survey_from_bib_custom.md",
        llm_provider="openai",
        model_name="ep-20250529110941-khvtx",
        custom_prompt=custom_prompt,
        pdf_dir="pdfs/"
    )
    
    # 示例3: 简化的英文prompt
    print("🌍 Generating survey from BIB file with English prompt...")
    
    english_prompt = """### Task
You are an AI research expert. Please analyze the following paper and provide a concise summary.

### Paper Information
Title: {title}
Authors: {authors}
Abstract: {abstract}
Full Text: {pdf_text}

### Output Format
```
## 📄 Paper Summary | {title}

## 🎯 Problem & Motivation
...

## 🛠️ Method
...

## 📊 Experiments
...

## 💭 Takeaways
...
```
"""
    
    generate_survey_from_bib(
        bib_file=".github/assets/导出的条目.bib",
        output_file="output/survey_from_bib_english.md",
        llm_provider="openai",
        model_name="ep-20250529110941-khvtx",
        custom_prompt=english_prompt,
        pdf_dir="pdfs/"
    )
    
    print("✅ All surveys generated successfully!")
    print("📂 Check the output/ directory for generated surveys")

if __name__ == "__main__":
    main()
