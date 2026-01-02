# 快速开始指南 - Caption Crawler

## 🎯 一分钟快速体验

```bash
# 进入目录
cd /mnt/bn/med-mllm-lfv2/linjh/project/learn/idke/survey_agent

# 一键运行（前提：已有survey_result*.md文件）
./launch_with_caption.sh

# 打开生成的HTML文件
# paper_captions.html
```

就这么简单！🎉

## 📋 详细步骤

### 步骤1: 检查依赖

```bash
python3 -c "import requests, bs4; print('✓ 依赖已满足')"
```

如果报错，安装依赖：
```bash
pip3 install requests beautifulsoup4
```

### 步骤2: 生成调查报告（如果还没有）

```bash
./launch.sh
```

在交互界面中输入搜索关键词，等待生成 `survey_result_xxx.md`

### 步骤3: 爬取图片并生成HTML

```bash
./launch_with_caption.sh
```

脚本会自动：
1. 查找最新的 survey_result*.md 文件
2. 提取所有arXiv IDs
3. 批量爬取论文图片和Caption
4. 生成可视化HTML文件

### 步骤4: 查看结果

生成的文件：
- `paper_captions/` - 论文数据和图片
- `paper_captions.html` - 可视化HTML（双击打开）

## 🧪 测试功能

如果想先测试一下爬取功能：

```bash
./test_caption_crawler.sh
```

这会：
1. 爬取一篇测试论文
2. 检查数据完整性
3. 生成测试HTML

## 🔧 高级用法

### 只爬取特定论文

创建一个包含arXiv IDs的文件：
```bash
echo "2407.03007
2407.12823
2407.12871" > my_papers.txt
```

然后运行Python脚本：
```python
import sys
sys.path.insert(0, 'src')
from survey_agent.arxiv_tools import batch_crawl_arxiv_ids

with open('my_papers.txt') as f:
    ids = [line.strip() for line in f]

batch_crawl_arxiv_ids(ids, 'my_outputs')
```

### 自定义HTML生成

```python
import sys
sys.path.insert(0, 'src')
from survey_agent.arxiv_tools import (
    parse_markdown_summaries,
    find_all_papers,
    generate_html_with_summary
)

# 解析总结
summaries = parse_markdown_summaries('survey_result_xxx.md')

# 查找论文数据
papers = find_all_papers('paper_captions')

# 生成HTML
generate_html_with_summary(papers, summaries, 'my_custom.html')
```

## ❓ 常见问题

### Q: 爬取失败怎么办？
A: 检查网络连接。部分图片可能因网络超时失败，这是正常的。

### Q: 没有survey_result文件？
A: 先运行 `./launch.sh` 生成调查报告。

### Q: HTML文件太大？
A: 这是正常的（包含base64编码的图片）。可以用 `gzip` 压缩。

### Q: 能否只生成HTML不爬取？
A: 可以，如果已有 `paper_captions/` 数据，直接运行HTML生成脚本。

### Q: 导入报错？
A: 确保使用 `sys.path.insert(0, 'src')` 并且从 `survey_agent.arxiv_tools` 导入。

## 📚 更多信息

- 详细文档: `CAPTION_CRAWLER_README.md`
- 集成总结: `INTEGRATION_SUMMARY.md`
- 测试脚本: `test_caption_crawler.sh`

## 🎊 享受使用！

如有问题或建议，欢迎反馈！
