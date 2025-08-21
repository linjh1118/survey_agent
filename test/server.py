#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
服务端脚本：检测提交的答案并返回正确分数
基于 curebench_valset_phase1_with_tags.jsonl 数据
"""

import json
import os
from typing import List, Dict, Any
from flask import Flask, request, jsonify

app = Flask(__name__)

class AnswerChecker:
    def __init__(self, data_file: str):
        """初始化答案检查器"""
        self.questions = {}
        self.load_data(data_file)
    
    def load_data(self, data_file: str):
        """加载题目数据"""
        if not os.path.exists(data_file):
            print(f"警告：数据文件 {data_file} 不存在，使用示例数据")
            self.create_sample_data()
            return
        
        try:
            with open(data_file, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.strip():
                        data = json.loads(line)
                        self.questions[data['id']] = data
            print(f"成功加载 {len(self.questions)} 道题目")
        except Exception as e:
            print(f"加载数据文件失败：{e}")
            self.create_sample_data()
    
    def create_sample_data(self):
        """创建示例数据用于测试"""
        sample_questions = [
            {
                "id": "Q001",
                "question_type": "multi_choice",
                "question": "Which drug brand name is associated with the treatment of acne?",
                "correct_answer": "A",
                "options": {
                    "A": "Salicylic Acid",
                    "B": "Minoxidil", 
                    "C": "Ketoconazole",
                    "D": "Fluocinide"
                },
                "llm_category": "Drug Overview"
            },
            {
                "id": "Q002", 
                "question_type": "multi_choice",
                "question": "What is the capital of France?",
                "correct_answer": "B",
                "options": {
                    "A": "London",
                    "B": "Paris",
                    "C": "Berlin", 
                    "D": "Madrid"
                },
                "llm_category": "Geography"
            },
            {
                "id": "Q003",
                "question_type": "multi_choice", 
                "question": "Which planet is closest to the Sun?",
                "correct_answer": "A",
                "options": {
                    "A": "Mercury",
                    "B": "Venus",
                    "C": "Earth",
                    "D": "Mars"
                },
                "llm_category": "Astronomy"
            }
        ]
        
        for q in sample_questions:
            self.questions[q['id']] = q
        
        print(f"创建了 {len(self.questions)} 道示例题目")
    
    def check_answers(self, answers: Dict[str, str]) -> Dict[str, Any]:
        """检查答案并返回分数"""
        if not answers:
            return {"error": "答案不能为空"}
        
        total_questions = len(self.questions)
        correct_count = 0
        details = []
        
        for qid, answer in answers.items():
            if qid in self.questions:
                question = self.questions[qid]
                is_correct = answer == question['correct_answer']
                if is_correct:
                    correct_count += 1
                
                details.append({
                    "question_id": qid,
                    "submitted_answer": answer,
                    "correct_answer": question['correct_answer'],
                    "is_correct": is_correct
                })
            else:
                details.append({
                    "question_id": qid,
                    "submitted_answer": answer,
                    "correct_answer": "N/A",
                    "is_correct": False,
                    "error": "题目ID不存在"
                })
        
        score = correct_count
        accuracy = (correct_count / total_questions) * 100 if total_questions > 0 else 0
        
        return {
            "total_questions": total_questions,
            "correct_count": correct_count,
            "score": score,
            "accuracy": round(accuracy, 2),
            "details": details
        }
    
    def get_question_count(self) -> int:
        """获取题目总数"""
        return len(self.questions)
    
    def get_question_ids(self) -> List[str]:
        """获取所有题目ID"""
        return list(self.questions.keys())

# 全局答案检查器实例
checker = AnswerChecker("/Users/bytedance/Downloads/hack_answer/curebench_valset_phase1_with_tags.jsonl")

@app.route('/check', methods=['POST'])
def check_answers():
    """检查答案接口"""
    try:
        data = request.get_json()
        if not data or 'answers' not in data:
            return jsonify({"error": "请提供答案数据"}), 400
        
        answers = data['answers']
        result = checker.check_answers(answers)
        return jsonify(result)
    
    except Exception as e:
        return jsonify({"error": f"服务器错误：{str(e)}"}), 500

@app.route('/info', methods=['GET'])
def get_info():
    """获取题目信息接口"""
    return jsonify({
        "total_questions": checker.get_question_count(),
        "question_ids": checker.get_question_ids()
    })

@app.route('/health', methods=['GET'])
def health_check():
    """健康检查接口"""
    return jsonify({"status": "healthy", "questions_loaded": checker.get_question_count()})

if __name__ == '__main__':
    print("启动答案检查服务...")
    print(f"已加载 {checker.get_question_count()} 道题目")
    print("服务地址：http://localhost:5000")
    print("接口：")
    print("  POST /check - 检查答案")
    print("  GET  /info  - 获取题目信息")
    print("  GET  /health - 健康检查")
    
    app.run(host='0.0.0.0', port=5000, debug=True)
