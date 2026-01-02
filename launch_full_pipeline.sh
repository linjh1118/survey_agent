#!/bin/bash

###############################################################################
# Survey Agent Full Pipeline - 端到端完整流程
#
# 流程：
#   1. 启动 Survey Agent 前端（用户输入关键词，生成调研报告）
#   2. 监控 survey_result*.md 文件生成
#   3. 自动爬取论文图片和 Caption
#   4. 生成可视化 HTML 文件
###############################################################################

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m'

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

print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_error() {
    echo -e "${RED}✗ $1${NC}"
}

print_highlight() {
    echo -e "${PURPLE}★ $1${NC}"
}

# 检查依赖
check_dependencies() {
    print_step "检查依赖..."

    local missing_deps=()

    if ! command -v python3 &> /dev/null; then
        missing_deps+=("python3")
    fi

    # 检查 Python 包
    python3 -c "import streamlit" 2>/dev/null || missing_deps+=("streamlit")
    python3 -c "import requests" 2>/dev/null || missing_deps+=("requests")
    python3 -c "import bs4" 2>/dev/null || missing_deps+=("beautifulsoup4")

    if [ ${#missing_deps[@]} -ne 0 ]; then
        print_error "缺少依赖: ${missing_deps[*]}"
        print_info "请运行: pip3 install streamlit requests beautifulsoup4"
        exit 1
    fi

    print_success "依赖检查通过"
}

# 获取当前最新的 survey_result 文件的时间戳
get_latest_survey_timestamp() {
    local latest_file=$(ls -t survey_result*.md 2>/dev/null | head -1)
    if [ -f "$latest_file" ]; then
        stat -c %Y "$latest_file" 2>/dev/null || stat -f %m "$latest_file" 2>/dev/null
    else
        echo "0"
    fi
}

# 等待新的 survey_result 文件生成
wait_for_new_survey() {
    local initial_timestamp=$1

    print_step "等待新的 survey_result 文件生成..."
    print_info "（在浏览器中完成论文调研后，此脚本会自动继续）"
    echo ""

    local dots=0
    while true; do
        sleep 3

        # 检查是否有新文件
        local latest_file=$(ls -t survey_result*.md 2>/dev/null | head -1)
        if [ -f "$latest_file" ]; then
            local current_timestamp=$(stat -c %Y "$latest_file" 2>/dev/null || stat -f %m "$latest_file" 2>/dev/null)

            if [ "$current_timestamp" -gt "$initial_timestamp" ]; then
                echo ""
                print_success "检测到新的 survey_result 文件: $latest_file"
                echo "$latest_file"
                return 0
            fi
        fi

        # 打印等待动画
        dots=$((dots + 1))
        printf "\r${CYAN}等待中"
        for ((i=0; i<$((dots % 4)); i++)); do
            printf "."
        done
        printf "   ${NC}"
    done
}

# 启动 Survey Agent
launch_survey_agent() {
    print_step "启动 Survey Agent 前端..."
    echo ""
    print_highlight "Survey Agent 将在浏览器中打开"
    print_info "请在界面中："
    echo "  1. 输入搜索关键词"
    echo "  2. 点击搜索并等待生成报告"
    echo "  3. 完成后关闭浏览器标签页"
    echo ""
    print_info "提示: 当报告生成完成后，本脚本会自动继续执行"
    echo ""

    # 启动 streamlit（在后台）
    python3 -m streamlit run src/survey_agent/frontend.py &
    STREAMLIT_PID=$!

    sleep 3
    print_success "Survey Agent 已启动 (PID: $STREAMLIT_PID)"

    echo "$STREAMLIT_PID"
}

# 停止 Survey Agent
stop_survey_agent() {
    local pid=$1
    if [ -n "$pid" ]; then
        print_step "停止 Survey Agent..."
        kill $pid 2>/dev/null || true
        sleep 1
        print_success "Survey Agent 已停止"
    fi
}

# 运行 Caption Crawler
run_caption_crawler() {
    local survey_file=$1

    print_header "步骤 2: Caption Crawler - 爬取图片和生成 HTML"
    echo ""

    # 定义输出路径
    IDS_FILE="arxiv_ids.txt"
    OUTPUT_DIR="paper_captions"
    HTML_FILE="paper_captions.html"

    # 提取 arXiv IDs
    print_step "从 $survey_file 提取 arXiv IDs..."
    grep -oP 'arxiv\.org/pdf/\K[0-9]{4}\.[0-9]{5}' "$survey_file" | sort -u > "$IDS_FILE"
    local count=$(wc -l < "$IDS_FILE")
    print_success "提取到 $count 个唯一的 arXiv IDs"
    echo ""

    # 批量爬取
    print_step "开始批量爬取论文..."
    mkdir -p "$OUTPUT_DIR"

    python3 - "$IDS_FILE" "$OUTPUT_DIR" <<'EOF'
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
        # 继续执行，即使部分失败
    fi

    echo ""

    # 生成 HTML
    print_step "生成 HTML 文件..."

    python3 - "$survey_file" "$OUTPUT_DIR" "$HTML_FILE" <<'EOF'
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
        print_success "HTML 生成完成: $HTML_FILE"
    else
        print_error "HTML 生成失败"
        return 1
    fi

    # 清理临时文件
    rm -f "$IDS_FILE"
}

# 主流程
main() {
    print_header "Survey Agent - 端到端完整流程"
    echo ""
    print_highlight "这个脚本将完成以下步骤："
    echo "  ${CYAN}步骤 1${NC}: 启动 Survey Agent → 生成调研报告 (survey_result.md)"
    echo "  ${CYAN}步骤 2${NC}: 自动爬取论文图片和 Caption"
    echo "  ${CYAN}步骤 3${NC}: 生成可视化 HTML 文件"
    echo ""

    # 检查依赖
    check_dependencies
    echo ""

    # 询问用户是否继续
    print_info "准备启动 Survey Agent..."
    read -p "按 Enter 继续，或 Ctrl+C 取消..."
    echo ""

    # 记录初始状态
    INITIAL_TIMESTAMP=$(get_latest_survey_timestamp)

    # 启动 Survey Agent
    print_header "步骤 1: Survey Agent - 生成调研报告"
    echo ""
    STREAMLIT_PID=$(launch_survey_agent)

    # 等待新的 survey_result 文件
    SURVEY_FILE=$(wait_for_new_survey $INITIAL_TIMESTAMP)

    # 停止 Survey Agent
    echo ""
    stop_survey_agent $STREAMLIT_PID
    echo ""

    # 运行 Caption Crawler
    run_caption_crawler "$SURVEY_FILE"

    # 打印最终结果
    echo ""
    print_header "🎉 完整流程执行完毕！"
    echo ""
    print_success "生成的文件："
    echo -e "  ${GREEN}1. $SURVEY_FILE${NC}"
    echo -e "     📄 LLM 调研报告（Markdown）"
    echo ""
    echo -e "  ${GREEN}2. paper_captions/${NC}"
    echo -e "     📁 论文数据和图片"
    echo ""
    echo -e "  ${GREEN}3. paper_captions.html${NC}"
    echo -e "     🌐 可视化 HTML 文件（含总结和图片）"
    echo ""
    print_info "使用方法："
    echo "  - 直接双击打开: paper_captions.html"
    echo "  - 或在浏览器中打开: file://$(pwd)/paper_captions.html"
    echo ""
    print_highlight "Enjoy! 🚀"
    echo ""
}

# 捕获 Ctrl+C 信号，清理进程
cleanup() {
    echo ""
    print_info "清理进程..."
    if [ -n "$STREAMLIT_PID" ]; then
        kill $STREAMLIT_PID 2>/dev/null || true
    fi
    exit 1
}

trap cleanup INT TERM

# 执行主流程
main "$@"
