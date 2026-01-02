# arXiv Caption Crawler 使用指南

## 📋 功能概述

此功能扩展了 survey_agent，增加了以下能力：
1. **爬取 arXiv HTML 论文**：提取标题、摘要、图片和对应的 Caption
2. **批量处理**：自动处理 survey_result.md 中的所有论文
3. **生成可视化 HTML**：将 LLM 总结与图片 Caption 整合展示

## 🚀 快速开始

### 方式一：一键完整流程

```bash
# 1. 先运行 survey agent 生成调查报告
./launch.sh

# 2. 运行 caption crawler（自动爬取图片并生成HTML）
./launch_with_caption.sh
```

### 方式二：单独爬取特定论文

```python
python3 -c "
import sys
sys.path.insert(0, 'src')
from survey_agent.arxiv_tools import crawl_arxiv_html

# 爬取单篇论文
crawl_arxiv_html('https://arxiv.org/html/2512.16149', 'outputs')
"
```

### 方式三：手动批量爬取

```python
python3 -c "
import sys
sys.path.insert(0, 'src')
from survey_agent.arxiv_tools import batch_crawl_arxiv_ids

# 爬取多篇论文
arxiv_ids = ['2512.16149', '2512.03794', '2511.15370']
batch_crawl_arxiv_ids(arxiv_ids, 'outputs')
"
```

## 📁 输出结构

运行 `./launch_with_caption.sh` 后会生成：

```
survey_agent/
├── paper_captions/              # 爬取的论文数据
│   ├── {Title}_{ID}/
│   │   ├── crawled_data.json   # 元数据
│   │   └── images/              # 下载的图片
│   │       ├── figure_1.png
│   │       ├── figure_2.png
│   │       └── ...
│   └── ...
├── paper_captions.html          # 可视化 HTML 文件
└── survey_result_xxx.md         # LLM 生成的调查报告
```

## 🎨 HTML 功能特性

生成的 `paper_captions.html` 包含：

### 1. LLM 总结展示（可折叠卡片）
- 📌 **背景痛点/本文动机** - 默认展开
- 🚀 **核心方法** - 默认展开
- 📈 **实验结果** - 默认折叠
- 💬 **可借鉴之处** - 默认折叠

### 2. 图片和 Caption 展示
- 网格布局展示所有图片
- 每个图片包含 Figure ID 和对应的 Caption
- 默认折叠，点击展开查看

### 3. 视觉设计
- 紫色渐变背景
- 响应式布局（桌面/移动适配）
- 平滑动画效果
- 彩色边框卡片（橙、蓝、绿、紫）

## 🔧 技术细节

### 新增模块

#### 1. `caption_crawler.py`
爬取 arXiv HTML 论文的核心模块

**主要函数**：
- `crawl_arxiv_html(url, output_dir)` - 爬取单篇论文
- `batch_crawl_arxiv_ids(arxiv_ids, output_dir)` - 批量爬取
- `clean_filename(text)` - 清理文件名
- `get_paper_title(soup)` - 提取论文标题

**特性**：
- 自动下载图片到本地
- 提取图片对应的 Caption
- 智能目录命名（标题 + ID）
- 错误处理和重试机制

#### 2. `html_generator.py`
生成可视化 HTML 的模块

**主要函数**：
- `generate_html_with_summary(papers, summaries, output_path)` - 生成 HTML
- `parse_markdown_summaries(md_path)` - 解析 survey_result.md
- `find_all_papers(outputs_dir)` - 查找爬取的论文数据
- `parse_summary_sections(summary)` - 解析总结为四个小节
- `encode_image_to_base64(image_path)` - 图片转 base64

**特性**：
- 所有图片以 base64 嵌入，单文件分发
- 可折叠的卡片式布局
- 自动匹配 arXiv ID 和总结内容
- 离线可用，无需网络

### 依赖要求

```bash
# Python 包
pip install requests beautifulsoup4

# 或使用项目 requirements.txt
pip install -r requirements.txt
```

## 📊 使用示例

### 示例 1：完整流程

```bash
# 1. 运行 survey agent
./launch.sh
# （在界面中输入搜索关键词，等待生成 survey_result.md）

# 2. 爬取图片并生成 HTML
./launch_with_caption.sh

# 3. 查看结果
open paper_captions.html
```

### 示例 2：只爬取图片（不生成 HTML）

```bash
# 提取 arXiv IDs
grep -oP 'arxiv\.org/pdf/\K[0-9]{4}\.[0-9]{5}' survey_result_xxx.md | sort -u > ids.txt

# 批量爬取
python3 -c "
import sys
sys.path.insert(0, 'src')
from survey_agent.arxiv_tools import batch_crawl_arxiv_ids

with open('ids.txt') as f:
    ids = [line.strip() for line in f]

batch_crawl_arxiv_ids(ids, 'outputs')
"
```

### 示例 3：只生成 HTML（已有爬取数据）

```bash
python3 -c "
import sys
sys.path.insert(0, 'src')
from survey_agent.arxiv_tools import (
    parse_markdown_summaries,
    find_all_papers,
    generate_html_with_summary
)

summaries = parse_markdown_summaries('survey_result_xxx.md')
papers = find_all_papers('outputs')
generate_html_with_summary(papers, summaries, 'output.html')
"
```

## 🎯 常见问题

### Q1: 为什么有些论文没有图片？
A: 并非所有 arXiv 论文都提供 HTML 版本，或者 HTML 版本中没有图片。这是正常现象。

### Q2: 爬取失败怎么办？
A: 检查网络连接，或者单独重新爬取失败的论文：
```bash
python3 src/survey_agent/arxiv_tools/caption_crawler.py <arxiv_id>
```

### Q3: HTML 文件太大怎么办？
A: 生成的 HTML 包含 base64 编码的图片，文件较大（几百 MB）是正常的。可以压缩：
```bash
gzip -9 paper_captions.html
# 压缩后约 30-50 MB
```

### Q4: 如何自定义输出目录？
A: 修改 `launch_with_caption.sh` 中的变量：
```bash
OUTPUT_DIR="my_custom_dir"
HTML_FILE="my_output.html"
```

### Q5: 能否只爬取特定论文的图片？
A: 可以，创建一个包含 arXiv ID 的文件，然后使用 Python API：
```python
from survey_agent.arxiv_tools import batch_crawl_arxiv_ids

ids = ['2512.16149', '2511.15370']  # 您感兴趣的论文
batch_crawl_arxiv_ids(ids, 'outputs')
```

## 📝 更新日志

### v1.0.0 (2025-12-26)
- ✅ 初始版本
- ✅ 支持 arXiv HTML 论文爬取
- ✅ 批量处理功能
- ✅ 生成可折叠卡片式 HTML
- ✅ Base64 图片嵌入
- ✅ 响应式设计

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 License

遵循 survey_agent 主项目的 License

---

**祝你使用愉快！** 🎉
