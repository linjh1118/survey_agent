import os
import json
from typing import Dict, Any, List, Optional, Union
from ..utils.cache import get_paper_cache

class LLMSummarizer:
    """
    Base class for LLM-based paper summarization.
    Subclass this to implement specific LLM integrations.
    """
    
    def __init__(self, model_name: str = None, custom_prompt: str = None):
        """
        Initialize the summarizer.
        
        Args:
            model_name: Name of the LLM model to use
            custom_prompt: Custom prompt template for summarization
        """
        self.model_name = model_name or os.environ.get("SURVEY_AGENT_LLM_MODEL", "gpt-4")
        self.custom_prompt = custom_prompt
    
    def get_default_summary_prompt(self, paper: Dict[str, Any]) -> str:
        """
        Generate the default prompt for paper summarization.
        
        Args:
            paper: Paper information dictionary
            
        Returns:
            Default prompt string for the LLM
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
{paper.get('pdf_text', '')[:10000]}  # Truncate if too long
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
    
    def get_summary_prompt(self, paper: Dict[str, Any]) -> str:
        """
        Generate the prompt for paper summarization.
        Uses custom prompt if provided, otherwise uses default.
        
        Args:
            paper: Paper information dictionary
            
        Returns:
            Prompt string for the LLM
        """
        if self.custom_prompt:
            # Replace placeholders in custom prompt with paper information
            return self._format_custom_prompt(self.custom_prompt, paper)
        else:
            return self.get_default_summary_prompt(paper)
    
    def _format_custom_prompt(self, prompt_template: str, paper: Dict[str, Any]) -> str:
        """
        Format custom prompt template with paper information.
        
        Args:
            prompt_template: Custom prompt template with placeholders
            paper: Paper information dictionary
            
        Returns:
            Formatted prompt string
        """
        # Available placeholders for custom prompts
        placeholders = {
            '{title}': paper.get('title', ''),
            '{abstract}': paper.get('summary', ''),
            '{authors}': paper.get('authors', ''),
            '{year}': paper.get('year', ''),
            '{url}': paper.get('url', ''),
            '{pdf_text}': paper.get('pdf_text', '')[:10000],  # Truncate if too long
            '{full_pdf_text}': paper.get('pdf_text', ''),
            '{doi}': paper.get('doi', ''),
            '{arxiv_id}': paper.get('arxiv_id', '')
        }
        
        # Replace all placeholders in the template
        formatted_prompt = prompt_template
        for placeholder, value in placeholders.items():
            formatted_prompt = formatted_prompt.replace(placeholder, str(value))
        
        return formatted_prompt
    
    def set_custom_prompt(self, custom_prompt: str):
        """
        Set a custom prompt template for summarization.
        
        Args:
            custom_prompt: Custom prompt template with placeholders like {title}, {abstract}, etc.
        """
        self.custom_prompt = custom_prompt
    
    def get_available_placeholders(self) -> List[str]:
        """
        Get list of available placeholders for custom prompts.
        
        Returns:
            List of placeholder strings
        """
        return [
            '{title}',
            '{abstract}', 
            '{authors}',
            '{year}',
            '{url}',
            '{pdf_text}',
            '{full_pdf_text}',
            '{doi}',
            '{arxiv_id}'
        ]
    
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
    
    def __init__(self, model_name: str = None, api_key: str = None, base_url: str = None, custom_prompt: str = None):
        """
        Initialize the OpenAI summarizer.
        
        Args:
            model_name: Name of the OpenAI model to use
            api_key: OpenAI API key
            base_url: OpenAI API base URL
            custom_prompt: Custom prompt template for summarization
        """
        super().__init__(model_name, custom_prompt)
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
        Generate a summary for a paper using OpenAI or Doubao API.
        
        Args:
            paper: Paper information dictionary
            
        Returns:
            Summary string
        """
        # 获取缓存实例
        cache = get_paper_cache()
        
        # 设置当前模型信息到缓存
        provider = "doubao" if (self.base_url and "ark-cn-beijing" in self.base_url) else "openai"
        cache.set_model_info(provider, self.model_name)
        
        # 检查缓存
        cached_summary = cache.get_cached_summary(paper)
        if cached_summary:
            return cached_summary
        
        # 没有缓存，生成新的摘要
        prompt = self.get_summary_prompt(paper)
        
        # 检查是否使用豆包API（通过base_url判断）
        if self.base_url and "ark-cn-beijing" in self.base_url:
            # 使用豆包API
            summary = self._summarize_with_doubao(prompt)
        else:
            # 使用标准OpenAI API
            summary = self._summarize_with_openai(prompt)
        
        # 缓存生成的摘要
        if summary:
            cache.cache_summary(paper, summary)
        
        return summary
    
    def _summarize_with_openai(self, prompt: str) -> str:
        """使用标准OpenAI API进行总结"""
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
    
    def _summarize_with_doubao(self, prompt: str) -> str:
        """使用豆包API进行总结"""
        try:
            import requests
            import time
            
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}"
            }
            
            payload = {
                "model": self.model_name,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.3,
                "max_tokens": 1500,
                "thinking": {"type": "disabled"}
            }
            print(f"base_url: {self.base_url}, model_name: {self.model_name}, api_key: {self.api_key}")
            # 重试逻辑 - 增加重试次数和更智能的错误处理
            max_retries = 5  # 增加重试次数
            for attempt in range(max_retries):
                try:
                    response = requests.post(
                        self.base_url,
                        headers=headers,
                        json=payload,
                        timeout=120
                    )
                    
                    # 检查响应状态
                    if response.status_code == 200:
                        result = response.json()
                        if "choices" in result and len(result["choices"]) > 0:
                            content = result["choices"][0].get("message", {}).get("content", "")
                            return content
                        else:
                            print(f"⚠️  API响应格式异常: {result}")
                            return ""
                    
                    elif response.status_code == 404:
                        # 404错误特殊处理 - 可能是临时性问题
                        wait_time = 2 * (2 ** attempt)  # 更长的等待时间
                        print(f"🔄 遇到404错误，{wait_time}秒后重试 (尝试 {attempt + 1}/{max_retries})")
                        if attempt < max_retries - 1:
                            time.sleep(wait_time)
                            continue
                        else:
                            print(f"❌ 豆包API服务暂时不可用 (404)，已达到最大重试次数")
                            return ""
                    
                    elif response.status_code == 429:
                        # 速率限制
                        wait_time = 5 * (2 ** attempt)
                        print(f"⏰ 速率限制，{wait_time}秒后重试 (尝试 {attempt + 1}/{max_retries})")
                        if attempt < max_retries - 1:
                            time.sleep(wait_time)
                            continue
                        else:
                            print(f"❌ 达到速率限制，已达到最大重试次数")
                            return ""
                    
                    else:
                        # 其他HTTP错误
                        response.raise_for_status()
                    
                except requests.exceptions.RequestException as e:
                    wait_time = 1 * (2 ** attempt)
                    if attempt < max_retries - 1:
                        print(f"🌐 网络请求失败，{wait_time}秒后重试 (尝试 {attempt + 1}/{max_retries}): {e}")
                        time.sleep(wait_time)
                    else:
                        print(f"❌ 网络请求最终失败: {e}")
                        return ""
                        
                except Exception as e:
                    wait_time = 1 * (2 ** attempt)
                    if attempt < max_retries - 1:
                        print(f"🔧 其他错误，{wait_time}秒后重试 (尝试 {attempt + 1}/{max_retries}): {e}")
                        time.sleep(wait_time)
                    else:
                        print(f"❌ 豆包API调用最终失败: {e}")
                        return ""
                        
        except Exception as e:
            print(f"❌ 豆包API初始化错误: {e}")
            return ""

# Factory function to get the appropriate summarizer
def get_summarizer(provider: str = "openai", model_name: str = None, custom_prompt: str = None) -> LLMSummarizer:
    """
    Get a summarizer instance based on the provider.
    
    Args:
        provider: LLM provider (e.g., "openai", "anthropic")
        model_name: Name of the model to use
        custom_prompt: Custom prompt template for summarization
        
    Returns:
        LLMSummarizer instance
    """
    if provider.lower() == "openai":
        return OpenAISummarizer(model_name, custom_prompt=custom_prompt)
    else:
        raise ValueError(f"Unsupported provider: {provider}") 