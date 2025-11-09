#!/usr/bin/env python3
"""
Survey Agent API服务器
为GitHub Pages提供后端API支持
"""

import os
import json
import uuid
from datetime import datetime
from typing import Dict, List, Optional
from flask import Flask, request, jsonify, cors
from flask_cors import CORS

# 导入Survey Agent模块
try:
    from src.survey_agent.survey.generator import generate_survey, generate_survey_from_bib
    from src.survey_agent.utils.cache import get_cache_stats
except ImportError:
    # 如果无法导入，提供模拟函数
    def generate_survey(*args, **kwargs):
        return "# 模拟调研报告\n\n这是一个模拟的调研报告。"
    
    def generate_survey_from_bib(*args, **kwargs):
        return "# 模拟BibTeX调研报告\n\n这是一个基于BibTeX的模拟调研报告。"
    
    def get_cache_stats():
        return {"total_papers": 0, "cache_hit_rate": 0}

app = Flask(__name__)
CORS(app)  # 允许跨域请求

# 配置
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

@app.route('/api/health', methods=['GET'])
def health_check():
    """健康检查端点"""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0"
    })

@app.route('/api/cache/stats', methods=['GET'])
def get_cache_statistics():
    """获取缓存统计信息"""
    try:
        stats = get_cache_stats()
        return jsonify({
            "success": True,
            "data": stats
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/api/papers', methods=['GET'])
def get_cached_papers():
    """获取缓存的论文列表"""
    try:
        cache_file = "cache/paper_summaries.json"
        if not os.path.exists(cache_file):
            return jsonify({
                "success": True,
                "data": [],
                "count": 0
            })
        
        with open(cache_file, 'r', encoding='utf-8') as f:
            papers_data = json.load(f)
        
        # 转换为列表格式
        papers_list = []
        for arxiv_id, paper_info in papers_data.items():
            paper = {
                "arxiv_id": arxiv_id,
                **paper_info
            }
            papers_list.append(paper)
        
        # 按缓存时间排序
        papers_list.sort(key=lambda x: x.get('cached_at', ''), reverse=True)
        
        return jsonify({
            "success": True,
            "data": papers_list,
            "count": len(papers_list)
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/api/reports', methods=['GET'])
def get_survey_reports():
    """获取调研报告列表"""
    try:
        output_dir = "output"
        if not os.path.exists(output_dir):
            return jsonify({
                "success": True,
                "data": [],
                "count": 0
            })
        
        reports = []
        for filename in os.listdir(output_dir):
            if filename.endswith('.md'):
                filepath = os.path.join(output_dir, filename)
                stat = os.stat(filepath)
                
                # 读取文件前几行获取标题
                title = filename.replace('.md', '')
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        first_line = f.readline().strip()
                        if first_line.startswith('#'):
                            title = first_line.lstrip('# ')
                except:
                    pass
                
                reports.append({
                    "filename": filename,
                    "title": title,
                    "created_at": datetime.fromtimestamp(stat.st_ctime).isoformat(),
                    "modified_at": datetime.fromtimestamp(stat.st_mtime).isoformat(),
                    "size": stat.st_size
                })
        
        # 按修改时间排序
        reports.sort(key=lambda x: x['modified_at'], reverse=True)
        
        return jsonify({
            "success": True,
            "data": reports,
            "count": len(reports)
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/api/report/<filename>', methods=['GET'])
def get_report_content(filename):
    """获取特定报告的内容"""
    try:
        filepath = os.path.join("output", filename)
        if not os.path.exists(filepath):
            return jsonify({
                "success": False,
                "error": "报告文件不存在"
            }), 404
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        return jsonify({
            "success": True,
            "data": {
                "filename": filename,
                "content": content
            }
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/api/survey/search', methods=['POST'])
def create_keyword_survey():
    """创建基于关键词的调研报告"""
    try:
        data = request.get_json()
        
        # 验证必需参数
        required_fields = ['keywords', 'api_key', 'base_url']
        for field in required_fields:
            if field not in data:
                return jsonify({
                    "success": False,
                    "error": f"缺少必需参数: {field}"
                }), 400
        
        keywords = data['keywords']
        if isinstance(keywords, str):
            keywords = [k.strip() for k in keywords.split(',')]
        
        max_results = data.get('max_results', 10)
        custom_prompt = data.get('custom_prompt')
        
        # 设置环境变量
        os.environ['API_KEY'] = data['api_key']
        os.environ['BASE_URL'] = data['base_url']
        
        # 生成输出文件名
        output_filename = f"survey_result_{uuid.uuid4().hex[:8]}.md"
        output_path = f"output/{output_filename}"
        
        # 生成调研报告
        result = generate_survey(
            terms=keywords,
            max_results=max_results,
            output_file=output_path,
            custom_prompt=custom_prompt
        )
        
        return jsonify({
            "success": True,
            "data": {
                "message": "调研报告生成成功",
                "output_file": output_filename,
                "content": result if isinstance(result, str) else "报告已保存到文件"
            }
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/api/survey/bibtex', methods=['POST'])
def create_bibtex_survey():
    """创建基于BibTeX的调研报告"""
    try:
        data = request.get_json()
        
        # 验证必需参数
        required_fields = ['file_content', 'api_key', 'base_url']
        for field in required_fields:
            if field not in data:
                return jsonify({
                    "success": False,
                    "error": f"缺少必需参数: {field}"
                }), 400
        
        file_content = data['file_content']
        custom_prompt = data.get('custom_prompt')
        
        # 设置环境变量
        os.environ['API_KEY'] = data['api_key']
        os.environ['BASE_URL'] = data['base_url']
        
        # 保存临时BibTeX文件
        temp_bib_file = f"temp_{uuid.uuid4().hex[:8]}.bib"
        with open(temp_bib_file, 'w', encoding='utf-8') as f:
            f.write(file_content)
        
        try:
            # 生成输出文件名
            output_filename = f"survey_from_bib_{uuid.uuid4().hex[:8]}.md"
            output_path = f"output/{output_filename}"
            
            # 生成调研报告
            result = generate_survey_from_bib(
                bib_file=temp_bib_file,
                output_file=output_path,
                custom_prompt=custom_prompt
            )
            
            return jsonify({
                "success": True,
                "data": {
                    "message": "BibTeX调研报告生成成功",
                    "output_file": output_filename,
                    "content": result if isinstance(result, str) else "报告已保存到文件"
                }
            })
            
        finally:
            # 清理临时文件
            if os.path.exists(temp_bib_file):
                os.remove(temp_bib_file)
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.errorhandler(413)
def too_large(e):
    """文件过大处理"""
    return jsonify({
        "success": False,
        "error": "上传文件过大，请确保文件小于16MB"
    }), 413

@app.errorhandler(404)
def not_found(e):
    """404错误处理"""
    return jsonify({
        "success": False,
        "error": "API端点不存在"
    }), 404

@app.errorhandler(500)
def internal_error(e):
    """500错误处理"""
    return jsonify({
        "success": False,
        "error": "服务器内部错误"
    }), 500

if __name__ == '__main__':
    # 确保必要目录存在
    os.makedirs('output', exist_ok=True)
    os.makedirs('cache', exist_ok=True)
    
    # 启动服务器
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)