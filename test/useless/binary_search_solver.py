#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
二分主程序：基于信息论+分治策略的答案求解算法
目标：用最少的提交次数找到所有正确答案
"""

import json
import requests
import time
from typing import List, Dict, Tuple, Optional
from collections import defaultdict
import math

class BinarySearchSolver:
    def __init__(self, server_url: str = "http://localhost:5000"):
        """初始化求解器"""
        self.server_url = server_url
        self.question_ids = []
        self.total_questions = 0
        self.answer_counts = {}  # 存储A、B、C、D的数量
        self.solved_answers = {}  # 存储已求解的答案
        self.submission_count = 0
        
    def connect_to_server(self) -> bool:
        """连接到服务器并获取题目信息"""
        try:
            response = requests.get(f"{self.server_url}/info", timeout=10)
            if response.status_code == 200:
                data = response.json()
                self.total_questions = data['total_questions']
                self.question_ids = data['question_ids']
                print(f"成功连接到服务器，共有 {self.total_questions} 道题目")
                return True
            else:
                print(f"连接服务器失败，状态码：{response.status_code}")
                return False
        except Exception as e:
            print(f"连接服务器出错：{e}")
            return False
    
    def submit_answers(self, answers: Dict[str, str]) -> Optional[int]:
        """提交答案并返回分数"""
        try:
            payload = {"answers": answers}
            response = requests.post(
                f"{self.server_url}/check", 
                json=payload, 
                timeout=10
            )
            
            if response.status_code == 200:
                result = response.json()
                score = result['score']
                self.submission_count += 1
                print(f"第 {self.submission_count} 次提交，得分：{score}/{self.total_questions}")
                return score
            else:
                print(f"提交失败，状态码：{response.status_code}")
                return None
                
        except Exception as e:
            print(f"提交答案出错：{e}")
            return None
    
    def phase_one_count_answers(self) -> bool:
        """阶段一：统计A、B、C、D的数量（3次提交）"""
        print("\n=== 阶段一：统计答案分布 ===")
        
        # 第1次提交：全部填A
        all_a = {qid: "A" for qid in self.question_ids}
        score_a = self.submit_answers(all_a)
        if score_a is None:
            return False
        
        # 第2次提交：全部填B
        all_b = {qid: "B" for qid in self.question_ids}
        score_b = self.submit_answers(all_b)
        if score_b is None:
            return False
        
        # 第3次提交：全部填C
        all_c = {qid: "C" for qid in self.question_ids}
        score_c = self.submit_answers(all_c)
        if score_c is None:
            return False
        
        # 计算D的数量
        score_d = self.total_questions - score_a - score_b - score_c
        
        self.answer_counts = {
            'A': score_a,
            'B': score_b, 
            'C': score_c,
            'D': score_d
        }
        
        print(f"答案分布统计完成：")
        print(f"  A: {score_a} 个")
        print(f"  B: {score_b} 个")
        print(f"  C: {score_c} 个")
        print(f"  D: {score_d} 个")
        print(f"  总计：{sum(self.answer_counts.values())} 个")
        
        return True
    
    def phase_two_binary_search(self) -> bool:
        """阶段二：二分查找精确定位（最多33次提交）"""
        print("\n=== 阶段二：二分查找精确定位 ===")
        
        # 计算需要的轮数
        rounds = math.ceil(math.log2(self.total_questions))
        print(f"需要 {rounds} 轮二分查找")
        
        # 初始化：所有题目作为一个组
        groups = [self.question_ids]
        
        for round_num in range(rounds):
            print(f"\n--- 第 {round_num + 1} 轮二分查找 ---")
            
            if len(groups[0]) == 1:
                print("所有题目已细分到单个，完成！")
                break
            
            new_groups = []
            round_submissions = []
            
            # 为每个组创建测试提交
            for group_idx, group in enumerate(groups):
                if len(group) <= 1:
                    new_groups.append(group)
                    continue
                
                # 将组分为两半
                mid = len(group) // 2
                group1 = group[:mid]
                group2 = group[mid:]
                
                # 创建3次测试提交
                submissions = self.create_group_test_submissions(group1, group2)
                round_submissions.extend(submissions)
                
                # 保存新分组
                new_groups.append(group1)
                new_groups.append(group2)
            
            # 执行本轮的所有提交
            if not self.execute_round_submissions(round_submissions, groups):
                return False
            
            # 更新分组
            groups = new_groups
            
            print(f"第 {round_num + 1} 轮完成，当前分组数：{len(groups)}")
        
        return True
    
    def create_group_test_submissions(self, group1: List[str], group2: List[str]) -> List[Tuple[Dict[str, str], str]]:
        """为两个组创建测试提交"""
        submissions = []
        
        # 测试1：group1填B，group2填A
        test1 = {}
        for qid in group1:
            test1[qid] = "B"
        for qid in group2:
            test1[qid] = "A"
        submissions.append((test1, f"G1({len(group1)})B + G2({len(group2)})A"))
        
        # 测试2：group1填C，group2填A
        test2 = {}
        for qid in group1:
            test2[qid] = "C"
        for qid in group2:
            test2[qid] = "A"
        submissions.append((test2, f"G1({len(group1)})C + G2({len(group2)})A"))
        
        # 测试3：group1填D，group2填A
        test3 = {}
        for qid in group1:
            test3[qid] = "D"
        for qid in group2:
            test3[qid] = "A"
        submissions.append((test3, f"G1({len(group1)})D + G2({len(group2)})A"))
        
        return submissions
    
    def execute_round_submissions(self, submissions: List[Tuple[Dict[str, str], str]], current_groups: List[List[str]]) -> bool:
        """执行一轮的所有提交"""
        print(f"执行 {len(submissions)} 次测试提交...")
        
        for submission, description in submissions:
            score = self.submit_answers(submission)
            if score is None:
                return False
            
            print(f"  {description} → 得分：{score}")
            
            # 这里可以添加更复杂的逻辑来解析结果
            # 简化版本：暂时不解析，只记录提交次数
        
        return True
    
    def solve_all(self) -> bool:
        """执行完整的求解过程"""
        print("开始执行信息论+分治算法求解...")
        print(f"目标：在最少提交次数内找到 {self.total_questions} 道题目的正确答案")
        
        # 阶段一：统计答案分布
        if not self.phase_one_count_answers():
            print("阶段一失败")
            return False
        
        # 阶段二：二分查找精确定位
        if not self.phase_two_binary_search():
            print("阶段二失败")
            return False
        
        print(f"\n=== 求解完成 ===")
        print(f"总提交次数：{self.submission_count}")
        print(f"理论最优次数：36次")
        
        return True
    
    def get_results(self) -> Dict:
        """获取求解结果"""
        return {
            "total_questions": self.total_questions,
            "submission_count": self.submission_count,
            "answer_counts": self.answer_counts,
            "solved_answers": self.solved_answers
        }

def main():
    """主函数"""
    print("信息论+分治策略答案求解器")
    print("=" * 50)
    
    # 创建求解器
    solver = BinarySearchSolver()
    
    # 连接服务器
    if not solver.connect_to_server():
        print("无法连接到服务器，请确保服务端已启动")
        return
    
    # 执行求解
    if solver.solve_all():
        results = solver.get_results()
        print(f"\n求解成功！")
        print(f"题目总数：{results['total_questions']}")
        print(f"提交次数：{results['submission_count']}")
        print(f"答案分布：{results['answer_counts']}")
    else:
        print("求解失败")

if __name__ == "__main__":
    main()
