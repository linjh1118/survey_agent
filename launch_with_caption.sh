#!/bin/bash

###############################################################################
# Survey Agent with Caption Crawler
# 完整流程：调查论文 → 爬取图片和Caption → 生成可视化HTML
###############################################################################

set -e  # 遇到错误立即退出

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 打印函数
print_header() {
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${BLUE}$1${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
}

print_step() {
    echo -e "${GREEN}▶ $1${NC}"
}

print_info() {
    echo -e "${YELLOW}ℹ $1${NC}"
}

print_error() {
    echo -e "${RED}✗ $1${NC}"
}

print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

# 检查依赖
check_dependencies() {
    print_step "检查依赖..."

    local missing_deps=()

    if ! command -v python3 &> /dev/null; then
        missing_deps+=("python3")
    fi

    # 检查 Python 包
    python3 -c "import requests" 2>/dev/null || missing_deps+=("python3-requests")
    python3 -c "import bs4" 2>/dev/null || missing_deps+=("python3-beautifulsoup4")

    if [ ${#missing_deps[@]} -ne 0 ]; then
        print_error "缺少依赖: ${missing_deps[*]}"
        print_info "请运行: pip3 install requests beautifulsoup4"
        exit 1
    fi

    print_success "依赖检查通过"
}

# 查找最新的 survey_result 文件
find_latest_survey_result() {
    print_step "查找最新的 survey_result 文件..."

    local survey_files=(survey_result*.md)

    if [ ${#survey_files[@]} -eq 0 ] || [ ! -f "${survey_files[0]}" ]; then
        print_error "未找到 survey_result*.md 文件"
        print_info "请先运行 ./launch.sh 生成调查报告"
        exit 1
    fi

    # 如果有多个文件，选择最新的
    local latest_file=""
    local latest_time=0

    for file in survey_result*.md; do
        if [ -f "$file" ]; then
            local file_time=$(stat -c %Y "$file" 2>/dev/null || stat -f %m "$file" 2>/dev/null)
            if [ "$file_time" -gt "$latest_time" ]; then
                latest_time=$file_time
                latest_file=$file
            fi
        fi
    done

    echo "$latest_file"
}

# 提取 arXiv IDs
extract_arxiv_ids() {
    local md_file=$1
    local output_file=$2

    print_step "从 $md_file 提取 arXiv IDs..."

    grep -oP 'arxiv\.org/pdf/\K[0-9]{4}\.[0-9]{5}' "$md_file" | sort -u > "$output_file"

    local count=$(wc -l < "$output_file")
    print_success "提取到 $count 个唯一的 arXiv IDs"
}

# 批量爬取
batch_crawl() {
    local ids_file=$1
    local output_dir=$2

    print_step "开始批量爬取论文..."

    mkdir -p "$output_dir"

    python3 - "$ids_file" "$output_dir" <<'EOF'
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from survey_agent.arxiv_tools.caption_crawler import batch_crawl_arxiv_ids

if len(sys.argv) < 3:
    print("用法: python script.py <ids_file> <output_dir>")
    sys.exit(1)

ids_file = sys.argv[1]
output_dir = sys.argv[2]

# 读取 arXiv IDs
with open(ids_file, 'r') as f:
    arxiv_ids = [line.strip() for line in f if line.strip()]

# 批量爬取
result = batch_crawl_arxiv_ids(arxiv_ids, output_dir)

# 返回退出码
sys.exit(0 if result['failed'] == 0 else 1)
EOF

    if [ $? -eq 0 ]; then
        print_success "批量爬取完成"
    else
        print_error "批量爬取失败或部分失败"
        return 1
    fi
}

# 生成 HTML
generate_html() {
    local md_file=$1
    local output_dir=$2
    local html_file=$3

    print_step "生成 HTML 文件..."

    python3 - "$md_file" "$output_dir" "$html_file" <<'EOF'
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from survey_agent.arxiv_tools.html_generator import (
    parse_markdown_summaries,
    find_all_papers,
    generate_html_with_summary
)

if len(sys.argv) < 4:
    print("用法: python script.py <md_file> <output_dir> <html_file>")
    sys.exit(1)

md_file = sys.argv[1]
output_dir = sys.argv[2]
html_file = sys.argv[3]

print("正在解析 markdown 文件...")
summaries = parse_markdown_summaries(md_file)
print(f"找到 {len(summaries)} 篇论文总结")

print("\n正在查找论文数据...")
papers = find_all_papers(output_dir)
print(f"找到 {len(papers)} 篇论文数据")

matched = set(summaries.keys()) & set(papers.keys())
print(f"\n匹配成功: {len(matched)} 篇")

if papers:
    print("\n正在生成 HTML（嵌入图片）...")
    generate_html_with_summary(papers, summaries, html_file)
    print("\n✓ 完成！")
else:
    print("\n未找到论文数据")
    sys.exit(1)
EOF

    if [ $? -eq 0 ]; then
        print_success "HTML 生成完成: $html_file"
    else
        print_error "HTML 生成失败"
        return 1
    fi
}

# 主流程
main() {
    print_header "Survey Agent with Caption Crawler"

    # 检查依赖
    check_dependencies

    # 查找最新的 survey_result 文件
    SURVEY_FILE=$(find_latest_survey_result)
    print_success "使用文件: $SURVEY_FILE"

    # 定义输出路径
    IDS_FILE="arxiv_ids.txt"
    OUTPUT_DIR="paper_captions"
    HTML_FILE="paper_captions.html"

    # 提取 arXiv IDs
    extract_arxiv_ids "$SURVEY_FILE" "$IDS_FILE"

    # 批量爬取
    batch_crawl "$IDS_FILE" "$OUTPUT_DIR"

    # 生成 HTML
    generate_html "$SURVEY_FILE" "$OUTPUT_DIR" "$HTML_FILE"

    # 清理临时文件
    rm -f "$IDS_FILE"

    # 打印最终结果
    print_header "完成！"
    echo ""
    print_success "输出文件:"
    echo -e "  ${GREEN}1. $OUTPUT_DIR/${NC} - 爬取的论文数据和图片"
    echo -e "  ${GREEN}2. $HTML_FILE${NC} - 可视化 HTML 文件"
    echo ""
    print_info "使用方法:"
    echo "  直接双击打开: $HTML_FILE"
    echo "  或在浏览器中打开: file://$(pwd)/$HTML_FILE"
    echo ""
}

# 执行主流程
main "$@"
