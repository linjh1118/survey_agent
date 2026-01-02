#!/bin/bash

###############################################################################
# Survey Agent Auto Pipeline - 全自动端到端流程
#
# 用法:
#   ./launch_auto.sh "search keywords"
#   ./launch_auto.sh "tool learning" "large language models"
#
# 流程:
#   1. 自动搜索论文并生成调研报告 (survey_result.md)
#   2. 自动爬取论文图片和 Caption
#   3. 自动生成可视化 HTML 文件
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

# 显示用法
show_usage() {
    cat <<EOF
${GREEN}用法:${NC}
  ./launch_auto.sh "关键词1" ["关键词2" ...]

${GREEN}示例:${NC}
  ./launch_auto.sh "tool learning"
  ./launch_auto.sh "large language models" "reasoning"
  ./launch_auto.sh "multimodal learning"

${GREEN}参数:${NC}
  关键词    - arXiv 搜索关键词（支持多个）

${GREEN}可选环境变量:${NC}
  MAX_RESULTS=50      - 每个关键词的最大结果数（默认：100）
  LLM_PROVIDER=openai - LLM 提供商（默认：openai）
  MODEL_NAME=...      - 模型名称（默认：使用提供商默认模型）

${GREEN}流程:${NC}
  ${CYAN}步骤 1${NC}: 搜索论文 → 生成调研报告 (survey_result_*.md)
  ${CYAN}步骤 2${NC}: 爬取论文图片和 Caption
  ${CYAN}步骤 3${NC}: 生成可视化 HTML (paper_captions.html)

EOF
    exit 1
}

# 检查参数
if [ $# -eq 0 ]; then
    print_error "错误: 未提供搜索关键词"
    echo ""
    show_usage
fi

# 检查依赖
check_dependencies() {
    print_step "检查依赖..."

    local missing_deps=()

    if ! command -v python3 &> /dev/null; then
        missing_deps+=("python3")
    fi

    # 检查 Python 包（忽略arxiv包的检查，让程序自己处理）
    python3 -c "import requests" 2>/dev/null || missing_deps+=("requests")
    python3 -c "import bs4" 2>/dev/null || missing_deps+=("beautifulsoup4")

    if [ ${#missing_deps[@]} -ne 0 ]; then
        print_error "缺少依赖: ${missing_deps[*]}"
        print_info "请运行: pip3 install requests beautifulsoup4 arxiv tqdm"
        exit 1
    fi

    print_success "依赖检查通过"
}

# 生成调研报告
generate_survey_report() {
    local search_terms=("$@")

    print_step "搜索关键词: ${search_terms[*]}"
    print_info "最大结果数: ${MAX_RESULTS:-100}"
    print_info "LLM 提供商: ${LLM_PROVIDER:-openai}"
    echo ""

    # 构建 Python 参数列表
    local terms_array="["
    for term in "${search_terms[@]}"; do
        terms_array+="\"$term\","
    done
    terms_array="${terms_array%,}]"

    # 调用 Python API
    python3 - "$terms_array" "${MAX_RESULTS:-100}" "${LLM_PROVIDER:-openai}" "${MODEL_NAME:-}" <<'PYEOF'
import sys
import os
import json
import uuid
from datetime import datetime

# 添加路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# 解析参数
terms = json.loads(sys.argv[1])
max_results = int(sys.argv[2])
llm_provider = sys.argv[3]
model_name = sys.argv[4] if len(sys.argv) > 4 and sys.argv[4] else None

print(f"搜索关键词: {terms}")
print(f"最大结果数: {max_results}")
print(f"LLM 提供商: {llm_provider}")
if model_name:
    print(f"模型: {model_name}")
print("")

# 导入 survey_agent（处理可能的导入错误）
try:
    from survey_agent.survey.generator import generate_survey
except ImportError as e:
    print(f"错误: 无法导入 survey_agent 模块")
    print(f"  {e}")
    print("")
    print("请确保已安装所有依赖:")
    print("  pip3 install arxiv tqdm openai anthropic")
    sys.exit(1)

# 生成唯一的输出文件名
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
unique_id = str(uuid.uuid4())[:8]
output_file = f"survey_result_{timestamp}_{unique_id}.md"

print(f"输出文件: {output_file}")
print("")

try:
    # 调用 generate_survey
    result = generate_survey(
        terms=terms,
        max_results=max_results,
        output_file=output_file,
        llm_provider=llm_provider,
        model_name=model_name
    )

    print(f"\n✓ 调研报告已生成: {result}")
    print(output_file)  # 最后一行输出文件名，供脚本读取

except Exception as e:
    print(f"\n✗ 生成失败: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
PYEOF

    # 获取生成的文件名（从Python脚本的最后一行输出）
    local survey_file=$(python3 - "$terms_array" "${MAX_RESULTS:-100}" "${LLM_PROVIDER:-openai}" "${MODEL_NAME:-}" 2>&1 | tail -1)

    if [ -f "$survey_file" ]; then
        print_success "调研报告已生成: $survey_file"
        echo "$survey_file"
    else
        print_error "调研报告生成失败"
        exit 1
    fi
}

# 运行 Caption Crawler
run_caption_crawler() {
    local survey_file=$1

    print_header "步骤 2: Caption Crawler - 爬取图片和生成 HTML"
    echo ""

    if [ ! -f "$survey_file" ]; then
        print_error "找不到 survey 文件: $survey_file"
        exit 1
    fi

    # 定义输出路径
    IDS_FILE="arxiv_ids_tmp.txt"
    OUTPUT_DIR="paper_captions"
    HTML_FILE="paper_captions.html"

    # 提取 arXiv IDs
    print_step "从 $survey_file 提取 arXiv IDs..."
    grep -oP 'arxiv\.org/pdf/\K[0-9]{4}\.[0-9]{5}' "$survey_file" | sort -u > "$IDS_FILE" 2>/dev/null || true

    local count=$(wc -l < "$IDS_FILE" 2>/dev/null || echo "0")

    if [ "$count" -eq 0 ]; then
        print_error "未找到任何 arXiv IDs"
        print_info "可能原因: 论文没有 arXiv ID，或格式不符合预期"
        print_info "跳过 Caption Crawler 步骤"
        rm -f "$IDS_FILE"
        return 0
    fi

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
        # 继续执行
    fi

    echo ""

    # 生成 HTML
    print_step "生成 HTML 文件..."

    python3 - "$survey_file" "$OUTPUT_DIR" "$HTML_FILE" 2>&1 <<'EOF'
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
    print("\n未找到论文数据，跳过 HTML 生成")
    sys.exit(1)
EOF

    local html_result=$?

    # 清理临时文件
    rm -f "$IDS_FILE"

    if [ $html_result -eq 0 ]; then
        print_success "HTML 生成完成: $HTML_FILE"
    else
        print_info "HTML 生成跳过（未找到图片数据）"
    fi
}

# 主流程
main() {
    print_header "Survey Agent - 全自动端到端流程"
    echo ""
    print_highlight "搜索关键词: $*"
    echo ""
    print_info "流程："
    echo "  ${CYAN}步骤 1${NC}: 搜索论文 → 生成调研报告"
    echo "  ${CYAN}步骤 2${NC}: 爬取论文图片和 Caption"
    echo "  ${CYAN}步骤 3${NC}: 生成可视化 HTML"
    echo ""

    # 检查依赖
    check_dependencies
    echo ""

    # 步骤 1: 生成调研报告
    print_header "步骤 1: Survey Agent - 生成调研报告"
    echo ""

    SURVEY_FILE=$(generate_survey_report "$@")

    if [ -z "$SURVEY_FILE" ] || [ ! -f "$SURVEY_FILE" ]; then
        print_error "调研报告生成失败"
        exit 1
    fi

    echo ""

    # 步骤 2 & 3: 运行 Caption Crawler
    run_caption_crawler "$SURVEY_FILE"

    # 打印最终结果
    echo ""
    print_header "🎉 全自动流程执行完毕！"
    echo ""
    print_success "生成的文件："
    echo -e "  ${GREEN}1. $SURVEY_FILE${NC}"
    echo -e "     📄 LLM 调研报告（Markdown）"
    echo ""

    if [ -d "paper_captions" ]; then
        echo -e "  ${GREEN}2. paper_captions/${NC}"
        echo -e "     📁 论文数据和图片"
        echo ""
    fi

    if [ -f "paper_captions.html" ]; then
        echo -e "  ${GREEN}3. paper_captions.html${NC}"
        echo -e "     🌐 可视化 HTML 文件（含总结和图片）"
        echo ""

        # 显示绝对路径
        HTML_ABS_PATH="$(pwd)/paper_captions.html"
        print_info "文件绝对路径："
        echo -e "  ${CYAN}$HTML_ABS_PATH${NC}"
        echo ""

        print_info "打开方式："
        echo "  1. 直接双击: paper_captions.html"
        echo "  2. 复制上方路径到浏览器"
        echo "  3. 终端运行: open \"$HTML_ABS_PATH\" (macOS)"
        echo "               xdg-open \"$HTML_ABS_PATH\" (Linux)"
        echo ""

        # 询问是否自动打开
        read -p "是否自动在浏览器中打开 HTML？(y/N) " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            print_step "正在打开浏览器..."
            if command -v open &> /dev/null; then
                # macOS
                open "$HTML_ABS_PATH"
                print_success "✓ 已在默认浏览器中打开！"
            elif command -v xdg-open &> /dev/null; then
                # Linux
                xdg-open "$HTML_ABS_PATH" &> /dev/null &
                print_success "✓ 已在默认浏览器中打开！"
            elif command -v start &> /dev/null; then
                # Windows (Git Bash)
                start "$HTML_ABS_PATH"
                print_success "✓ 已在默认浏览器中打开！"
            else
                print_error "无法自动打开浏览器"
                print_info "请手动打开: file://$HTML_ABS_PATH"
            fi
        fi
        echo ""
    fi

    print_highlight "Enjoy! 🚀"
    echo ""
}

# 执行主流程
main "$@"
