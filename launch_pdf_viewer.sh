#!/bin/bash

# PDF查看器启动脚本
# 启动PDF查看器API服务器，提供PDF和笔记管理功能

echo "==========================="
echo "Survey Agent - PDF查看器"  
echo "==========================="
echo ""

# 检查Python环境
if ! command -v python3 &> /dev/null; then
    echo "错误: 未找到python3，请先安装Python 3"
    exit 1
fi

# 检查必要的目录
echo "检查必要目录..."
mkdir -p pdfs cache output

# 检查是否有PDF文件
pdf_count=$(find pdfs -name "*.pdf" 2>/dev/null | wc -l)
if [ "$pdf_count" -eq 0 ]; then
    echo "警告: pdfs目录中没有PDF文件"
    echo "请先使用Survey Agent下载一些论文，或手动将PDF文件放入pdfs目录"
    echo ""
else
    echo "找到 $pdf_count 个PDF文件"
fi

# 检查缓存文件
if [ -f "cache/paper_summaries.json" ]; then
    cache_size=$(wc -c < "cache/paper_summaries.json")
    echo "缓存文件大小: $cache_size 字节"
else
    echo "提示: 暂无缓存文件，首次使用时将创建"
fi

echo ""
echo "启动PDF查看器API服务器..."
echo "端口: 8002"
echo "访问地址: http://localhost:8002/pdf_viewer.html"
echo ""
echo "功能特性:"
echo "- 查看本地PDF文件和对应笔记摘要"
echo "- 搜索和筛选论文"
echo "- 选择多篇论文进行批量问答"
echo "- 问答结果自动保存为Markdown文件"
echo ""
echo "按 Ctrl+C 停止服务器"
echo "=========================================="
echo ""

# 设置环境变量 (如果需要)
# export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"

# 启动服务器
python3 pdf_api.py