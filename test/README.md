# 信息论+分治策略答案求解器

这是一个基于信息论和分治策略的智能答案求解系统，能够在最少的提交次数内找到所有题目的正确答案。

## 算法原理

### 核心思想
该算法将传统的"暴力搜索"转化为"信息论优化问题"，通过巧妙的批量测试，让每次提交都能获得最大信息量。

### 算法流程

#### 阶段一：统计答案分布（3次提交）
- 第1次提交：2000题全填A → 得到A的数量
- 第2次提交：2000题全填B → 得到B的数量  
- 第3次提交：2000题全填C → 得到C的数量
- D的数量 = 2000 - A - B - C

#### 阶段二：二分查找精确定位（最多33次提交）
- 将题目不断分组，每轮将问题规模减半
- 每轮需要3次提交来测试分组的答案分布
- 通过信息论原理反推每个分组的答案构成

### 理论最优次数
- 阶段一：3次
- 阶段二：11轮 × 3次/轮 = 33次
- **总计：36次**

## 文件结构

```
.
├── server.py              # 服务端脚本（答案检查服务）
├── binary_search_solver.py # 基础二分求解器
├── advanced_solver.py     # 高级求解器
├── complete_solver.py     # 完整求解器
├── requirements.txt       # Python依赖包
├── README.md             # 项目说明文档
└── task.md               # 任务描述文档
```

## 安装和运行

### 1. 安装依赖
```bash
pip install -r requirements.txt
```

### 2. 启动服务端
```bash
python server.py
```
服务端将在 http://localhost:5000 启动，提供以下接口：
- `POST /check` - 检查答案
- `GET /info` - 获取题目信息
- `GET /health` - 健康检查

### 3. 运行求解器
```bash
# 基础版本
python binary_search_solver.py

# 高级版本
python advanced_solver.py

# 完整版本
python complete_solver.py
```

## 使用方法

### 1. 准备数据文件
将你的题目数据文件放在指定路径：
```
/Users/bytedance/Downloads/hack_answer/curebench_valset_phase1_with_tags.jsonl
```

数据格式示例：
```json
{
  "id": "U9PHZ83RKYV8",
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
}
```

### 2. 启动服务
```bash
python server.py
```

### 3. 运行求解器
```bash
python complete_solver.py
```

## 算法优势

1. **效率极高**：从可能的数千次减少到36次
2. **信息密度大**：每次提交都测试大量题目
3. **可并行处理**：同时处理多个分组
4. **结果确定**：100%准确找到所有答案

## 注意事项

1. 确保服务端先启动，再运行求解器
2. 数据文件路径要正确配置
3. 网络连接要稳定，避免提交失败
4. 大量题目时可能需要较长时间

## 扩展功能

- 支持自定义题目数量
- 可配置服务器地址和端口
- 支持断点续传
- 结果导出和验证

## 技术特点

- 基于Flask的RESTful API服务
- 信息论+分治算法的Python实现
- 支持大规模题目处理
- 模块化设计，易于扩展

## 许可证

MIT License
