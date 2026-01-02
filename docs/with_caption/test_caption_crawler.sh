#!/bin/bash

###############################################################################
# Caption Crawler 测试脚本
# 测试爬取功能是否正常工作
###############################################################################

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}Caption Crawler 测试${NC}"
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# 测试 1: 爬取单篇论文
echo -e "${YELLOW}测试 1: 爬取单篇论文${NC}"
echo "arXiv ID: 2512.16149"
echo ""

python3 -c "
import sys
sys.path.insert(0, 'src')
from survey_agent.arxiv_tools import crawl_arxiv_html

result = crawl_arxiv_html('https://arxiv.org/html/2512.16149', 'test_outputs')
if result:
    print('\n✓ 测试 1 通过')
else:
    print('\n✗ 测试 1 失败')
    sys.exit(1)
"

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# 测试 2: 检查爬取的数据
echo -e "${YELLOW}测试 2: 检查爬取的数据${NC}"
echo ""

if [ -d "test_outputs" ]; then
    echo "✓ test_outputs 目录已创建"

    # 查找 JSON 文件
    json_files=$(find test_outputs -name "crawled_data.json" | wc -l)
    echo "✓ 找到 $json_files 个 JSON 文件"

    # 查找图片
    image_files=$(find test_outputs -name "*.png" -o -name "*.jpg" | wc -l)
    echo "✓ 找到 $image_files 张图片"
else
    echo "✗ 测试 2 失败: test_outputs 目录不存在"
    exit 1
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# 测试 3: 生成 HTML
echo -e "${YELLOW}测试 3: 生成 HTML（如果有 survey_result 文件）${NC}"
echo ""

# 查找 survey_result 文件
if ls survey_result*.md 1> /dev/null 2>&1; then
    latest_file=$(ls -t survey_result*.md | head -1)
    echo "使用文件: $latest_file"

    python3 -c "
import sys
sys.path.insert(0, 'src')
from survey_agent.arxiv_tools import (
    parse_markdown_summaries,
    find_all_papers,
    generate_html_with_summary
)

summaries = parse_markdown_summaries('$latest_file')
papers = find_all_papers('test_outputs')
generate_html_with_summary(papers, summaries, 'test_output.html')
print('\n✓ 测试 3 通过: HTML 已生成')
"
else
    echo "跳过测试 3: 未找到 survey_result 文件"
    echo "（这是正常的，如果还没运行过 survey agent）"
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# 清理测试文件
echo -e "${YELLOW}清理测试文件${NC}"
echo ""

read -p "是否删除测试文件？(y/N) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    rm -rf test_outputs
    rm -f test_output.html
    echo "✓ 测试文件已删除"
else
    echo "保留测试文件:"
    echo "  - test_outputs/"
    echo "  - test_output.html"
fi

echo ""
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}✓ 所有测试完成${NC}"
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
