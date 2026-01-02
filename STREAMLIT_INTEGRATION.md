# Streamlit 图片爬取集成说明

## ✅ 已完成的更新

已将**图片爬取功能直接集成到 Streamlit 前端流程**中！

---

## 🎯 新的完整流程

现在使用 `./launch.sh` 启动 Streamlit 后，流程如下：

```
1. 🔍 搜索论文
   ↓
2. 📥 下载 PDF 并提取文本
   ↓
3. ✨ LLM 生成四段式总结
   ↓
4. 🖼️ 爬取论文图片和 Caption  【新增步骤】
   ↓
5. 📄 生成 Markdown 报告
   ↓
6. 🌐 生成可视化 HTML（含图片）【新增步骤】
   ↓
7. 📦 提供下载
```

---

## 🚀 使用方法

### 启动 Streamlit

```bash
cd /mnt/bn/med-mllm-lfv2/linjh/project/learn/idke/survey_agent
./launch.sh
```

### 在界面中操作

1. **输入关键词**：如 "tool learning"
2. **设置参数**：
   - 最多检索论文数：5-50
   - LLM 模型：选择模型
   - ✅ **爬取论文图片和 Caption**（默认勾选）← 新增选项
3. **点击"开始生成综述"**

### 流程进度显示

界面会实时显示：
- 🔍 正在检索论文...
- 📥 正在下载与处理论文 X/Y
- ✨ LLM 总结中 X/Y
- 🖼️ **正在爬取论文图片 X/Y (成功: Z)** ← 新增
- 📄 正在生成 markdown...
- 🌐 **正在生成可视化 HTML...** ← 新增
- 🎉 综述已生成！

### 下载结果

完成后可以下载两个文件：
1. **📄 Markdown 文件**：纯文本调研报告
2. **🌐 HTML 文件（含图片）**：可视化 HTML，包含：
   - 四段式总结卡片（可折叠）
   - 论文图片和 Caption
   - 精美的界面设计

---

## ⚙️ 新增功能详解

### 1. 可选的图片爬取

在表单中新增了一个复选框：
```
☑️ 爬取论文图片和 Caption（生成可视化 HTML）
```

**默认**：勾选（启用）

**说明**：
- 勾选：执行完整流程，生成带图片的 HTML
- 不勾选：只生成标准 Markdown 和简单 HTML

### 2. 并行爬取

图片爬取采用**并行处理**（4 线程），提高效率：
- 同时爬取多篇论文
- 实时更新进度
- 显示成功/失败统计

### 3. 智能 HTML 生成

根据爬取结果智能生成：
- **有图片数据**：生成带图片的可视化 HTML
- **无图片数据**：生成标准 HTML（降级处理）

---

## 📊 性能说明

**典型场景（10 篇论文）：**
- 搜索论文：~10 秒
- 下载 PDF：~30 秒
- LLM 总结：~2 分钟
- **爬取图片：~30-60 秒** ← 新增
- 生成文件：~10 秒
- **总计：~3-4 分钟**

**注意**：
- 部分论文可能没有 HTML 版本（只有 PDF）
- 部分图片可能因网络问题下载失败
- 这些都是正常现象，不影响其他论文的处理

---

## 🎨 生成的 HTML 特性

生成的 HTML 文件包含：

### 1. 四段式总结卡片（可折叠）
- 📌 背景痛点/本文动机（默认展开）
- 🚀 核心方法（默认展开）
- 📈 实验结果（默认折叠）
- 💬 可借鉴之处（默认折叠）

### 2. 图片展示
- 网格布局
- 包含 Figure ID 和 Caption
- Base64 嵌入（单文件分发）

### 3. 视觉设计
- 紫色渐变背景
- 彩色边框卡片
- 响应式布局
- 平滑动画

---

## 🔧 技术实现

### 修改的文件

**`src/survey_agent/frontend.py`**

新增：
1. `crawl_paper_images_parallel()` - 并行爬取图片函数
2. `extract_arxiv_id()` - 提取 arXiv ID
3. 集成到主流程中

### 关键代码

```python
# 步骤 4: 爬取论文图片和 Caption（可选）
if crawl_images:
    crawl_results = crawl_paper_images_parallel(
        processed_papers,
        output_dir,
        progress_placeholder,
        paper_list_placeholder,
        max_workers=4
    )

    # 步骤 5: 生成带图片的 HTML
    summaries = parse_markdown_summaries(output_md)
    papers_data = find_all_papers(output_dir)
    generate_html_with_summary(papers_data, summaries, html_output_file)
```

---

## 📁 输出文件

运行 `./launch.sh` 完成后会生成：

```
survey_agent/
├── survey_result_xxx.md           # Markdown 调研报告
├── paper_captions/                 # 图片数据目录
│   ├── Paper_Title_1_2407.03007/
│   │   ├── crawled_data.json
│   │   └── images/
│   │       ├── figure_1.png
│   │       └── ...
│   └── ...
└── paper_captions_xxx.html         # 可视化 HTML（含图片）
```

---

## ❓ 常见问题

### Q1: 为什么有些论文没有图片？
**A:** 并非所有 arXiv 论文都有 HTML 版本。只有较新的论文才提供 HTML。

### Q2: 爬取失败怎么办？
**A:** 部分失败不影响整体流程。成功爬取的论文会显示图片，失败的只显示总结。

### Q3: 可以跳过图片爬取吗？
**A:** 可以！取消勾选"爬取论文图片和 Caption"即可。

### Q4: HTML 文件太大？
**A:** 这是正常的（图片 base64 编码）。可以用 gzip 压缩。

### Q5: 爬取太慢怎么办？
**A:**
- 减少论文数量
- 或取消勾选图片爬取选项
- 只下载 Markdown 文件即可

---

## 🆚 与之前的对比

### 之前（分两步）

```bash
# 步骤 1: 生成调研报告
./launch.sh
# 在浏览器中操作...

# 步骤 2: 手动爬取图片
./launch_with_caption.sh
```

### 现在（一步完成）

```bash
# 一步到位
./launch.sh
# 在浏览器中勾选"爬取图片"，自动完成所有步骤！
```

---

## 🎊 优势

1. ✅ **流程自然**：图片爬取作为生成流程的一部分
2. ✅ **实时反馈**：界面显示爬取进度
3. ✅ **一步完成**：无需手动执行第二步
4. ✅ **灵活可选**：可以选择是否爬取图片
5. ✅ **自动降级**：爬取失败时自动生成标准 HTML

---

## 🚀 现在就试试吧！

```bash
cd /mnt/bn/med-mllm-lfv2/linjh/project/learn/idke/survey_agent
./launch.sh
```

在界面中：
1. 输入关键词
2. ✅ 勾选"爬取论文图片和 Caption"
3. 点击"开始生成综述"
4. 等待完成（3-5 分钟）
5. 下载带图片的 HTML 文件

**Enjoy! 🎉**
