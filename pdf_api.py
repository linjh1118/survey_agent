#!/usr/bin/env python3
"""
PDF查看器后端API
提供PDF列表、摘要缓存、批量问答等API接口
"""

import json
import re
from datetime import datetime
from typing import List, Dict, Any, Optional
from pathlib import Path
from http.server import HTTPServer, SimpleHTTPRequestHandler

# 导入项目模块
from src.survey_agent.utils.cache import get_paper_cache
from doubao_api import DoubaoAPI


class PDFAPIHandler(SimpleHTTPRequestHandler):
    """处理PDF查看器的API请求"""
    
    def __init__(self, *args, **kwargs):
        self.api = DoubaoAPI()
        super().__init__(*args, **kwargs)
    
    def do_GET(self):
        """处理GET请求"""
        if self.path == '/api/pdfs':
            self.handle_get_pdfs()
        elif self.path == '/api/summaries':
            self.handle_get_summaries()
        elif self.path.startswith('/api/'):
            self.send_error(404, "API endpoint not found")
        else:
            # 处理静态文件
            super().do_GET()
    
    def do_POST(self):
        """处理POST请求"""
        if self.path == '/api/batch-question':
            self.handle_batch_question()
        else:
            self.send_error(404, "API endpoint not found")
    
    def handle_get_pdfs(self):
        """获取PDF文件列表"""
        try:
            pdf_dir = Path("pdfs")
            if not pdf_dir.exists():
                self.send_json_response([])
                return
            
            # 加载缓存来尝试匹配标题
            cache = get_paper_cache()
            cached_papers = cache._cache
            
            papers = []
            for pdf_file in pdf_dir.glob("*.pdf"):
                # 从文件名提取arXiv ID（可能为空）
                arxiv_id = self.extract_arxiv_id_from_filename(pdf_file.name)
                
                # 清理文件名得到标题
                clean_title = self.clean_filename_to_title(pdf_file.stem)
                
                # 尝试通过标题匹配找到对应的缓存条目
                matched_arxiv_id = None
                matched_title = clean_title
                
                if not arxiv_id:
                    # 如果从文件名无法提取arXiv ID，尝试通过标题匹配
                    matched_arxiv_id = self.find_arxiv_id_by_title(clean_title, cached_papers)
                    if matched_arxiv_id and matched_arxiv_id in cached_papers:
                        matched_title = cached_papers[matched_arxiv_id].get('title', clean_title)
                else:
                    matched_arxiv_id = arxiv_id
                    if arxiv_id in cached_papers:
                        matched_title = cached_papers[arxiv_id].get('title', clean_title)
                
                # 获取文件信息
                stat = pdf_file.stat()
                paper_info = {
                    "arxiv_id": matched_arxiv_id or pdf_file.stem,
                    "filename": pdf_file.name,
                    "title": matched_title,
                    "date": datetime.fromtimestamp(stat.st_mtime).isoformat(),
                    "size": stat.st_size
                }
                papers.append(paper_info)
            
            # 按修改时间排序（最新优先）
            papers.sort(key=lambda x: x["date"], reverse=True)
            self.send_json_response(papers)
            
        except Exception as e:
            self.send_error(500, f"Failed to get PDFs: {str(e)}")
    
    def handle_get_summaries(self):
        """获取摘要缓存"""
        try:
            cache = get_paper_cache()
            summaries = cache._cache
            self.send_json_response(summaries)
        except Exception as e:
            self.send_error(500, f"Failed to get summaries: {str(e)}")
    
    def handle_batch_question(self):
        """处理批量问答请求"""
        try:
            # 读取请求数据
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            request_data = json.loads(post_data.decode('utf-8'))
            
            question = request_data.get('question', '').strip()
            arxiv_ids = request_data.get('arxiv_ids', [])
            
            if not question or not arxiv_ids:
                self.send_error(400, "Missing question or arxiv_ids")
                return
            
            # 执行批量问答
            results = self.process_batch_question(question, arxiv_ids)
            self.send_json_response(results)
            
        except json.JSONDecodeError:
            self.send_error(400, "Invalid JSON data")
        except Exception as e:
            self.send_error(500, f"Batch question failed: {str(e)}")
    
    def process_batch_question(self, question: str, arxiv_ids: List[str]) -> Dict[str, Any]:
        """处理批量问答"""
        cache = get_paper_cache()
        individual_answers = {}
        valid_papers = []
        
        # 为每篇论文生成答案
        for arxiv_id in arxiv_ids:
            try:
                # 从缓存获取论文摘要
                if arxiv_id in cache._cache:
                    cached_entry = cache._cache[arxiv_id]
                    summary = cached_entry.get('summary', '')
                    title = cached_entry.get('title', '')
                    
                    if summary:
                        # 构建针对单篇论文的提示
                        prompt = self.build_paper_question_prompt(question, title, summary)
                        
                        # 调用LLM获取答案
                        answer = self.api.generate_text(prompt)
                        individual_answers[arxiv_id] = answer
                        valid_papers.append({
                            'arxiv_id': arxiv_id,
                            'title': title,
                            'answer': answer
                        })
                    else:
                        individual_answers[arxiv_id] = "此论文暂无摘要，无法回答问题"
                else:
                    individual_answers[arxiv_id] = "未找到此论文的缓存信息"
                    
            except Exception as e:
                individual_answers[arxiv_id] = f"处理失败: {str(e)}"
        
        # 生成综合总结
        summary_answer = ""
        if valid_papers:
            try:
                summary_prompt = self.build_summary_prompt(question, valid_papers)
                summary_answer = self.api.generate_text(summary_prompt)
            except Exception as e:
                summary_answer = f"生成综合总结失败: {str(e)}"
        
        # 保存结果到markdown文件
        self.save_batch_results_to_markdown(question, individual_answers, summary_answer)
        
        return {
            "question": question, 
            "individual_answers": individual_answers,
            "summary": summary_answer,
            "timestamp": datetime.now().isoformat(),
            "total_papers": len(arxiv_ids),
            "answered_papers": len(valid_papers)
        }
    
    def build_paper_question_prompt(self, question: str, title: str, summary: str) -> str:
        """构建针对单篇论文的问题提示"""
        return f"""你是一个专业的学术研究助手。请基于以下论文的信息回答用户的问题。

论文标题：{title}

论文摘要：
{summary}

用户问题：{question}

请仔细分析论文内容，给出准确、专业的答案。如果论文内容与问题不相关，请明确说明。答案应该简洁明了，重点突出。
"""

    def build_summary_prompt(self, question: str, papers: List[Dict[str, Any]]) -> str:
        """构建综合总结提示"""
        papers_info = "\n\n".join([
            f"【论文{i+1}：{paper['title']}】\n{paper['answer']}" 
            for i, paper in enumerate(papers)
        ])
        
        return f"""你是一个专业的学术研究助手。用户对多篇论文提出了同一个问题，现在需要你基于各论文的回答生成一个综合性的总结。

用户问题：{question}

各论文的回答：
{papers_info}

请基于以上回答，生成一个综合性的总结，要求：
1. 综合分析各论文的观点和方法
2. 找出共同点和差异点
3. 提供整体性的见解
4. 保持客观和专业的语调
5. 如果论文之间存在矛盾或不同观点，请明确指出

请提供一个结构清晰、逻辑性强的综合总结。
"""

    def save_batch_results_to_markdown(self, question: str, individual_answers: Dict[str, str], summary: str):
        """将批量问答结果保存为Markdown文件"""
        try:
            # 创建输出目录
            output_dir = Path("output")
            output_dir.mkdir(exist_ok=True)
            
            # 生成文件名
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            safe_question = "".join(c for c in question[:50] if c.isalnum() or c in (' ', '-', '_')).strip()
            safe_question = safe_question.replace(' ', '_')
            filename = f"batch_qa_{safe_question}_{timestamp}.md"
            
            filepath = output_dir / filename
            
            # 构建Markdown内容
            content = f"""# 批量问答结果

## 问题
{question}

## 回答时间
{datetime.now().strftime("%Y年%m月%d日 %H:%M:%S")}

## 综合总结
{summary}

## 各论文详细回答

"""
            
            # 添加各论文的详细回答
            cache = get_paper_cache()
            for arxiv_id, answer in individual_answers.items():
                title = "未知标题"
                if arxiv_id in cache._cache:
                    title = cache._cache[arxiv_id].get('title', '未知标题')
                
                content += f"""### {title}
**arXiv ID:** {arxiv_id}

{answer}

---

"""
            
            # 写入文件
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content) 
            
            print(f"批量问答结果已保存到: {filepath}")
            
        except Exception as e:
            print(f"保存批量问答结果失败: {str(e)}")
    
    def extract_arxiv_id_from_filename(self, filename: str) -> Optional[str]:
        """从文件名提取arXiv ID"""
        # 匹配类似 2406.09172 的模式
        match = re.search(r'(\d{4}\.\d{4,5})', filename)
        return match.group(1) if match else None
    
    def find_arxiv_id_by_title(self, pdf_title: str, cached_papers: dict) -> Optional[str]:
        """通过标题匹配找到对应的arXiv ID"""
        if not pdf_title:
            return None
            
        # 清理标题用于匹配
        def normalize_title(title):
            # 移除特殊字符，转小写，移除多余空格
            normalized = re.sub(r'[^\w\s]', '', title.lower())
            normalized = re.sub(r'\s+', ' ', normalized).strip()
            return normalized
        
        normalized_pdf_title = normalize_title(pdf_title)
        
        # 尝试匹配缓存中的标题
        for arxiv_id, entry in cached_papers.items():
            cached_title = entry.get('title', '')
            if not cached_title:
                continue
                
            normalized_cached_title = normalize_title(cached_title)
            
            # 检查是否匹配（支持部分匹配）
            if (normalized_pdf_title in normalized_cached_title or 
                normalized_cached_title in normalized_pdf_title or
                self.calculate_title_similarity(normalized_pdf_title, normalized_cached_title) > 0.8):
                return arxiv_id
        
        return None
    
    def calculate_title_similarity(self, title1: str, title2: str) -> float:
        """计算两个标题的相似度（简单的词汇重叠度）"""
        if not title1 or not title2:
            return 0.0
            
        words1 = set(title1.split())
        words2 = set(title2.split())
        
        if not words1 or not words2:
            return 0.0
            
        intersection = words1.intersection(words2)
        union = words1.union(words2)
        
        return len(intersection) / len(union)
    
    def clean_filename_to_title(self, filename: str) -> str:
        """将文件名清理为可读的标题"""
        import re
        # 移除arXiv ID
        title = re.sub(r'\d{4}\.\d{4,5}', '', filename)
        # 替换下划线和连字符为空格
        title = title.replace('_', ' ').replace('-', ' ')
        # 移除多余空格
        title = ' '.join(title.split())
        # 首字母大写
        title = title.title()
        return title.strip()
    
    def send_json_response(self, data: Any):
        """发送JSON响应"""
        json_data = json.dumps(data, ensure_ascii=False, indent=2)
        
        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', len(json_data.encode('utf-8')))
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        
        self.wfile.write(json_data.encode('utf-8'))
    
    def do_OPTIONS(self):
        """处理CORS预检请求"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()


def start_pdf_api_server(port: int = 8002):
    """启动PDF API服务器"""
    print(f"启动PDF查看器API服务器，端口: {port}")
    print(f"访问地址: http://localhost:{port}/pdf_viewer.html")
    
    server = HTTPServer(('localhost', port), PDFAPIHandler)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n服务器已停止")
        server.shutdown()


if __name__ == "__main__":
    # 检查必要的目录和文件
    required_dirs = ["pdfs", "cache", "output"]
    for dir_name in required_dirs:
        Path(dir_name).mkdir(exist_ok=True)
    
    # 启动服务器
    start_pdf_api_server()