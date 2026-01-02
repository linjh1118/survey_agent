# 端到端使用指南

本指南介绍如何使用 Survey Agent 的**端到端完整流程**，从搜索论文到生成带图片的可视化 HTML。

## 🎯 三种使用方式

### 方式 1: 全自动模式 ⭐️ 推荐

**最简单！** 直接通过命令行参数指定搜索关键词，全程自动完成。

```bash
./launch_auto.sh "tool learning"
```

**支持多个关键词：**
```bash
./launch_auto.sh "large language models" "reasoning"
```

**流程：**
1. ✅ 自动搜索论文
2. ✅ 自动生成调研报告（survey_result_*.md）
3. ✅ 自动爬取图片和 Caption
4. ✅ 自动生成可视化 HTML

**输出：**
- `survey_result_YYYYMMDD_HHMMSS_xxxxx.md` - LLM 调研报告
- `paper_captions/` - 论文数据和图片
- `paper_captions.html` - 可视化 HTML

**可选参数：**
```bash
# 限制每个关键词的最大结果数
MAX_RESULTS=50 ./launch_auto.sh "multimodal learning"

# 指定 LLM 提供商
LLM_PROVIDER=anthropic ./launch_auto.sh "tool learning"

# 指定模型
MODEL_NAME=gpt-4 ./launch_auto.sh "tool learning"
```

---

### 方式 2: 交互式模式

通过浏览器界面交互，适合需要精细控制的场景。

```bash
./launch_full_pipeline.sh
```

**流程：**
1. 🌐 自动启动 Streamlit 前端（浏览器界面）
2. 👤 在界面中输入搜索关键词并生成报告
3. ⏳ 脚本自动监控文件生成
4. ✅ 检测到新报告后，自动爬取图片
5. ✅ 自动生成 HTML

**适合场景：**
- 需要查看实时搜索结果
- 需要手动筛选论文
- 需要调整搜索参数

---

### 方式 3: 分步执行

分两步手动执行，适合调试或单独使用某个功能。

**步骤 1: 生成调研报告**
```bash
./launch.sh
# 在浏览器界面中完成搜索和报告生成
```

**步骤 2: 爬取图片并生成 HTML**
```bash
./launch_with_caption.sh
# 自动找到最新的 survey_result*.md，爬取图片，生成 HTML
```

**适合场景：**
- 已有 survey_result.md 文件，只需要生成 HTML
- 需要分别调试两个步骤
- 想要多次重新生成 HTML（不重新搜索）

---

## 📋 详细对比

| 特性 | 全自动模式 | 交互式模式 | 分步执行 |
|------|-----------|-----------|---------|
| **脚本** | `launch_auto.sh` | `launch_full_pipeline.sh` | `launch.sh` + `launch_with_caption.sh` |
| **用户输入** | 命令行参数 | 浏览器界面 | 浏览器界面 + 手动触发 |
| **自动化程度** | 🌟🌟🌟🌟🌟 | 🌟🌟🌟🌟 | 🌟🌟 |
| **适合场景** | 日常使用 | 需要交互 | 调试/单独使用 |
| **是否需要浏览器** | ❌ | ✅ | ✅ |

---

## 🚀 快速开始（全自动模式）

### 1. 安装依赖

```bash
pip3 install requests beautifulsoup4 arxiv tqdm openai anthropic
```

### 2. 配置 API Key

确保设置了 LLM API Key：

```bash
# OpenAI
export OPENAI_API_KEY="your-api-key"

# 或 Anthropic
export ANTHROPIC_API_KEY="your-api-key"
```

### 3. 运行脚本

```bash
cd /mnt/bn/med-mllm-lfv2/linjh/project/learn/idke/survey_agent

# 搜索"工具学习"相关论文
./launch_auto.sh "tool learning"
```

### 4. 查看结果

**生成的文件：**
```
survey_agent/
├── survey_result_20241228_153045_a1b2c3d4.md  # 调研报告
├── paper_captions/                            # 论文数据
│   ├── Paper_Title_1_2407.03007/
│   │   ├── crawled_data.json
│   │   └── images/
│   └── ...
└── paper_captions.html                         # 可视化 HTML ⭐️
```

**打开 HTML：**
- 直接双击 `paper_captions.html`
- 或在浏览器中打开：`file:///path/to/paper_captions.html`

---

## 💡 高级用法

### 限制搜索结果数量

```bash
# 每个关键词只返回前 20 篇论文
MAX_RESULTS=20 ./launch_auto.sh "multimodal learning"
```

### 使用不同的 LLM

```bash
# 使用 Anthropic Claude
LLM_PROVIDER=anthropic ./launch_auto.sh "tool learning"

# 使用 OpenAI GPT-4
LLM_PROVIDER=openai MODEL_NAME=gpt-4 ./launch_auto.sh "tool learning"
```

### 搜索多个关键词

```bash
# 搜索"大语言模型"和"推理"相关的论文
./launch_auto.sh "large language models" "reasoning"
```

### 只重新生成 HTML（不重新搜索）

如果已有 `survey_result*.md` 和 `paper_captions/` 数据：

```bash
./launch_with_caption.sh
```

这会跳过搜索和爬取步骤，直接生成新的 HTML 文件。

---

## 🎨 生成的 HTML 特性

生成的 `paper_captions.html` 包含：

### 1. LLM 总结（四段式可折叠卡片）
- 📌 **背景痛点/本文动机** - 默认展开
- 🚀 **核心方法** - 默认展开
- 📈 **实验结果** - 默认折叠
- 💬 **可借鉴之处** - 默认折叠

### 2. 图片展示
- 网格布局
- 包含 Figure ID 和 Caption
- 可折叠查看

### 3. 视觉设计
- 紫色渐变背景
- 彩色边框卡片（橙、蓝、绿、紫）
- 响应式布局（支持移动端）
- 平滑动画效果

### 4. 单文件分发
- 所有图片以 base64 嵌入
- 无需网络连接即可查看
- 方便分享和归档

---

## ❓ 常见问题

### Q1: 全自动模式失败怎么办？
**A:** 检查以下几点：
1. API Key 是否设置正确
2. 网络连接是否正常
3. 依赖包是否安装完整
4. 查看错误日志，定位问题

### Q2: 没有生成 HTML 文件？
**A:** 可能原因：
- 论文没有 arXiv HTML 版本（部分老论文只有 PDF）
- 网络问题导致图片下载失败
- 查看 `paper_captions/` 目录，如果为空说明没有成功爬取

### Q3: HTML 文件太大？
**A:** 这是正常的（base64 编码的图片）。压缩方法：
```bash
gzip -9 paper_captions.html
# 压缩后约减少 70-80% 大小
```

### Q4: 如何自定义搜索参数？
**A:** 查看 `src/survey_agent/survey/generator.py` 的 `generate_survey()` 函数参数。

### Q5: 能否搜索特定作者的论文？
**A:** 目前支持关键词搜索。如需按作者搜索，可以：
- 使用 `./launch.sh` 交互界面
- 或修改搜索逻辑添加作者过滤

---

## 📚 相关文档

- **快速上手**: `QUICKSTART.md`
- **详细文档**: `CAPTION_CRAWLER_README.md`
- **文件说明**: `CAPTION_CRAWLER_FILES.md`
- **集成总结**: `INTEGRATION_SUMMARY.md`

---

## 🎊 总结

**推荐使用全自动模式**（`launch_auto.sh`），一行命令完成所有流程：

```bash
./launch_auto.sh "your keywords"
```

生成的 `paper_captions.html` 包含：
- ✅ LLM 调研报告
- ✅ 论文图片和 Caption
- ✅ 可折叠的四段式总结
- ✅ 精美的可视化界面

**Enjoy! 🚀**
