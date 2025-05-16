import os
import json
from typing import Dict, Any, List, Optional, Union

class LLMSummarizer:
    """
    Base class for LLM-based paper summarization.
    Subclass this to implement specific LLM integrations.
    """
    
    def __init__(self, model_name: str = None):
        """
        Initialize the summarizer.
        
        Args:
            model_name: Name of the LLM model to use
        """
        self.model_name = model_name or os.environ.get("SURVEY_AGENT_LLM_MODEL", "gpt-4")
    
    def get_summary_prompt(self, paper: Dict[str, Any]) -> str:
        """
        Generate the prompt for paper summarization.
        
        Args:
            paper: Paper information dictionary
            
        Returns:
            Prompt string for the LLM
        """
        # Default prompt template
        prompt = f"""### 任务
你是一个人工智能领域的专家，你能够快速阅读arxiv上的各种AI前沿论文，并给出非常好的论文总结。
现在请你阅读以下论文，并给出你对这篇论文的详细介绍，从而放到你的博客上，让更多人了解这篇论文。

### 论文信息
###  1. 论文标题
```
{paper['title']}
```
#### 2. 论文摘要
```
{paper['summary']}
```

#### 3. 论文全文
```
{paper['pdf_text'][:10000]}  # Truncate if too long
```

请输出论文总结
### 输出格式（输出语言用中文）
```
## 🌟 论文解读 | <想一个，宣传该论文的文案标题>

## 📌 背景痛点/本文动机
...(介绍论文的背景或痛点，或者本文的动机)

## 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1
...

💡 创新点2
...

## 📈 实验结果
...

## 💬 可借鉴之处
...(介绍论文的可借鉴之处)
```
"""
        return prompt
    
    def summarize(self, paper: Dict[str, Any]) -> str:
        """
        Generate a summary for a paper using an LLM.
        This is a placeholder that should be implemented by subclasses.
        
        Args:
            paper: Paper information dictionary
            
        Returns:
            Summary string
        """
        raise NotImplementedError("Subclasses must implement this method")

class OpenAISummarizer(LLMSummarizer):
    """
    OpenAI-based paper summarizer.
    """
    
    def __init__(self, model_name: str = None, api_key: str = None, base_url: str = None):
        """
        Initialize the OpenAI summarizer.
        
        Args:
            model_name: Name of the OpenAI model to use
            api_key: OpenAI API key
        """
        super().__init__(model_name)
        self.api_key = api_key or os.environ.get("API_KEY")
        self.base_url = base_url or os.environ.get("BASE_URL")
        
        if not self.api_key:
            raise ValueError("OpenAI API key not provided")
        
        try:
            import openai
            self.client = openai.OpenAI(api_key=self.api_key, base_url=self.base_url)
        except Exception as e:
            # 根据内容，自己返回
            raise e
    
    def summarize(self, paper: Dict[str, Any]) -> str:
        """
        Generate a summary for a paper using OpenAI.
        
        Args:
            paper: Paper information dictionary
            
        Returns:
            Summary string
        """
        prompt = self.get_summary_prompt(paper)
        
        try:
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[
                    {"role": "system", "content": "You are a helpful AI assistant that summarizes research papers."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=1500
            )
            
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error generating summary: {e}")
            return ""

# Factory function to get the appropriate summarizer
def get_summarizer(provider: str = "openai", model_name: str = None) -> LLMSummarizer:
    """
    Get a summarizer instance based on the provider.
    
    Args:
        provider: LLM provider (e.g., "openai", "anthropic")
        model_name: Name of the model to use
        
    Returns:
        LLMSummarizer instance
    """
    if provider.lower() == "openai":
        return OpenAISummarizer(model_name)
    else:
        raise ValueError(f"Unsupported provider: {provider}") 