#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
系统测试脚本：验证服务端和求解器的功能
"""

import requests
import json
import time
import sys

def test_server_connection(server_url: str = "http://localhost:5000") -> bool:
    """测试服务器连接"""
    print("测试服务器连接...")
    try:
        response = requests.get(f"{server_url}/health", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"✓ 服务器连接成功，状态：{data['status']}")
            print(f"  已加载题目数：{data['questions_loaded']}")
            return True
        else:
            print(f"✗ 服务器连接失败，状态码：{response.status_code}")
            return False
    except Exception as e:
        print(f"✗ 服务器连接出错：{e}")
        return False

def test_server_info(server_url: str = "http://localhost:5000") -> bool:
    """测试服务器信息接口"""
    print("\n测试服务器信息接口...")
    try:
        response = requests.get(f"{server_url}/info", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"✓ 信息接口正常")
            print(f"  题目总数：{data['total_questions']}")
            print(f"  题目ID示例：{data['question_ids'][:3] if data['question_ids'] else '无'}")
            return True
        else:
            print(f"✗ 信息接口失败，状态码：{response.status_code}")
            return False
    except Exception as e:
        print(f"✗ 信息接口出错：{e}")
        return False

def test_answer_checking(server_url: str = "http://localhost:5000") -> bool:
    """测试答案检查功能"""
    print("\n测试答案检查功能...")
    try:
        # 测试提交部分答案
        test_answers = {}
        response = requests.get(f"{server_url}/info", timeout=5)
        if response.status_code == 200:
            data = response.json()
            if data['question_ids']:
                # 取前3道题进行测试
                for i, qid in enumerate(data['question_ids'][:3]):
                    test_answers[qid] = "A" if i % 2 == 0 else "B"
        
        if not test_answers:
            print("  跳过答案检查测试（无题目数据）")
            return True
        
        payload = {"answers": test_answers}
        response = requests.post(f"{server_url}/check", json=payload, timeout=10)
        
        if response.status_code == 200:
            result = response.json()
            print(f"✓ 答案检查功能正常")
            print(f"  测试题目数：{result['total_questions']}")
            print(f"  正确数量：{result['correct_count']}")
            print(f"  得分：{result['score']}")
            print(f"  准确率：{result['accuracy']}%")
            return True
        else:
            print(f"✗ 答案检查失败，状态码：{response.status_code}")
            return False
            
    except Exception as e:
        print(f"✗ 答案检查出错：{e}")
        return False

def test_solver_connection(server_url: str = "http://localhost:5000") -> bool:
    """测试求解器连接"""
    print("\n测试求解器连接...")
    try:
        response = requests.get(f"{server_url}/info", timeout=5)
        if response.status_code == 200:
            data = response.json()
            if data['total_questions'] > 0:
                print(f"✓ 求解器可以连接到服务器")
                print(f"  可用题目数：{data['total_questions']}")
                return True
            else:
                print("⚠ 服务器无题目数据")
                return False
        else:
            print(f"✗ 求解器连接失败")
            return False
    except Exception as e:
        print(f"✗ 求解器连接出错：{e}")
        return False

def run_full_test():
    """运行完整测试"""
    print("=" * 50)
    print("信息论+分治策略答案求解器 - 系统测试")
    print("=" * 50)
    
    server_url = "http://localhost:5000"
    
    # 测试服务器连接
    if not test_server_connection(server_url):
        print("\n❌ 服务器连接测试失败，请确保服务端已启动")
        return False
    
    # 测试服务器信息接口
    if not test_server_info(server_url):
        print("\n❌ 服务器信息接口测试失败")
        return False
    
    # 测试答案检查功能
    if not test_answer_checking(server_url):
        print("\n❌ 答案检查功能测试失败")
        return False
    
    # 测试求解器连接
    if not test_solver_connection(server_url):
        print("\n❌ 求解器连接测试失败")
        return False
    
    print("\n" + "=" * 50)
    print("✅ 所有测试通过！系统运行正常")
    print("=" * 50)
    
    print("\n下一步操作：")
    print("1. 运行求解器：python complete_solver.py")
    print("2. 或运行基础版本：python binary_search_solver.py")
    print("3. 或运行高级版本：python advanced_solver.py")
    
    return True

def main():
    """主函数"""
    try:
        success = run_full_test()
        if success:
            sys.exit(0)
        else:
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n\n测试被用户中断")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n测试过程中出现未预期的错误：{e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
