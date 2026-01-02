# Survey Agent 脚本总览

本文档列出所有可用的启动脚本及其用途。

## 🚀 启动脚本一览

### 端到端完整流程（推荐）

#### 1. `launch_auto.sh` ⭐️ 最推荐

**全自动端到端流程** - 命令行参数指定关键词，全程自动完成。

```bash
./launch_auto.sh "tool learning"
./launch_auto.sh "large language models" "reasoning"
```

**流程：**
搜索论文 → 生成调研报告 → 爬取图片 → 生成 HTML

**输出：**
- `survey_result_*.md` - 调研报告
- `paper_captions/` - 论文数据和图片
- `paper_captions.html` - 可视化 HTML

**优点：**
- ✅ 完全自动化
- ✅ 无需浏览器交互
- ✅ 适合批处理和脚本调用
- ✅ 支持环境变量配置

**适合场景：**
- 日常使用
- 批量处理多个主题
- CI/CD 集成
- 命令行爱好者

---

#### 2. `launch_full_pipeline.sh`

**交互式端到端流程** - 通过浏览器界面输入，后台自动监控。

```bash
./launch_full_pipeline.sh
```

**流程：**
1. 启动 Streamlit 前端（浏览器自动打开）
2. 在界面中输入关键词并生成报告
3. 脚本自动监控文件生成
4. 检测到新报告后，自动爬取图片并生成 HTML

**优点：**
- ✅ 可视化交互界面
- ✅ 实时查看搜索结果
- ✅ 可以手动筛选论文
- ✅ 后台自动监控和处理

**适合场景：**
- 需要查看搜索结果
- 需要精细控制
- 首次使用，不熟悉命令行

---

### 分步执行

#### 3. `launch.sh`

**步骤 1：生成调研报告** - 启动交互式 Streamlit 前端。

```bash
./launch.sh
```

**功能：**
- 搜索 arXiv 论文
- 使用 LLM 生成总结
- 输出 Markdown 调研报告

**输出：**
- `survey_result_*.md`

---

#### 4. `launch_with_caption.sh`

**步骤 2：爬取图片并生成 HTML** - 基于已有的调研报告。

```bash
./launch_with_caption.sh
```

**功能：**
- 自动查找最新的 `survey_result*.md`
- 提取 arXiv IDs
- 批量爬取论文图片和 Caption
- 生成可视化 HTML

**输出：**
- `paper_captions/` - 论文数据
- `paper_captions.html` - 可视化 HTML

**适合场景：**
- 已有调研报告，只需生成 HTML
- 想要重新生成 HTML（不重新搜索）
- 调试爬虫功能

---

### 其他脚本

#### 5. `test_caption_crawler.sh`

**测试脚本** - 测试爬虫功能是否正常。

```bash
./test_caption_crawler.sh
```

**功能：**
- 爬取单篇测试论文
- 检查数据完整性
- 生成测试 HTML

**适合场景：**
- 验证环境配置
- 调试爬虫功能
- 首次使用前测试

---

#### 6. `launch_bib.sh`

**从 BIB 文件生成调研报告**

```bash
./launch_bib.sh
```

适合已有文献列表的场景。

---

#### 7. `launch_pdf_viewer.sh`

**PDF 查看器**

```bash
./launch_pdf_viewer.sh
```

可视化查看下载的 PDF 文件。

---

## 📊 脚本对比表

| 脚本 | 自动化程度 | 需要浏览器 | 输入方式 | 输出 | 推荐指数 |
|------|-----------|-----------|---------|------|---------|
| `launch_auto.sh` | ⭐️⭐️⭐️⭐️⭐️ | ❌ | 命令行参数 | MD + HTML | ⭐️⭐️⭐️⭐️⭐️ |
| `launch_full_pipeline.sh` | ⭐️⭐️⭐️⭐️ | ✅ | 浏览器界面 | MD + HTML | ⭐️⭐️⭐️⭐️ |
| `launch.sh` + `launch_with_caption.sh` | ⭐️⭐️ | ✅ | 分两步执行 | MD + HTML | ⭐️⭐️⭐️ |
| `launch.sh` | ⭐️⭐️ | ✅ | 浏览器界面 | MD only | ⭐️⭐️ |
| `launch_with_caption.sh` | ⭐️⭐️⭐️⭐️ | ❌ | 自动查找 | HTML only | ⭐️⭐️⭐️ |
| `test_caption_crawler.sh` | ⭐️⭐️⭐️⭐️ | ❌ | 测试用 | Test HTML | ⭐️⭐️ |

---

## 🎯 使用建议

### 场景 1: 日常调研（推荐）

```bash
# 一行命令完成所有工作
./launch_auto.sh "tool learning"
```

### 场景 2: 需要交互式搜索

```bash
# 启动完整流程（带浏览器界面）
./launch_full_pipeline.sh
```

### 场景 3: 已有调研报告，只需生成 HTML

```bash
# 只运行第二步
./launch_with_caption.sh
```

### 场景 4: 首次使用，想测试功能

```bash
# 先运行测试脚本
./test_caption_crawler.sh

# 测试通过后，运行完整流程
./launch_auto.sh "your keywords"
```

### 场景 5: 批量处理多个主题

```bash
# 创建批处理脚本
cat > batch_survey.sh <<'EOF'
#!/bin/bash
./launch_auto.sh "tool learning"
./launch_auto.sh "multimodal learning"
./launch_auto.sh "reasoning in LLMs"
EOF

chmod +x batch_survey.sh
./batch_survey.sh
```

---

## 💡 环境变量配置

### `launch_auto.sh` 支持的环境变量

```bash
# 最大搜索结果数（默认：100）
MAX_RESULTS=50 ./launch_auto.sh "tool learning"

# LLM 提供商（默认：openai）
# 可选值：openai, anthropic
LLM_PROVIDER=anthropic ./launch_auto.sh "tool learning"

# 模型名称（默认：使用提供商默认模型）
MODEL_NAME=gpt-4 ./launch_auto.sh "tool learning"

# 组合使用
MAX_RESULTS=30 LLM_PROVIDER=anthropic ./launch_auto.sh "tool learning"
```

### API Key 配置

```bash
# OpenAI
export OPENAI_API_KEY="sk-..."

# Anthropic Claude
export ANTHROPIC_API_KEY="sk-ant-..."

# 推荐：写入 ~/.bashrc 或 ~/.zshrc
echo 'export OPENAI_API_KEY="sk-..."' >> ~/.bashrc
source ~/.bashrc
```

---

## 📁 输出文件说明

### 调研报告（Markdown）

```
survey_result_20241228_153045_a1b2c3d4.md
```

**包含：**
- 搜索关键词
- 论文列表（标题、作者、链接）
- 每篇论文的 LLM 四段式总结
  - 📌 背景痛点/本文动机
  - 🚀 核心方法
  - 📈 实验结果
  - 💬 可借鉴之处

### 论文数据目录

```
paper_captions/
├── Paper_Title_1_2407.03007/
│   ├── crawled_data.json      # 元数据（标题、摘要、图片信息）
│   └── images/                # 下载的图片
│       ├── figure_1.png
│       ├── figure_2.png
│       └── ...
├── Paper_Title_2_2407.12823/
└── ...
```

### 可视化 HTML

```
paper_captions.html
```

**特性：**
- 单文件（所有图片 base64 嵌入）
- 可折叠的四段式总结卡片
- 图片网格展示（含 Caption）
- 响应式设计（支持移动端）
- 紫色渐变背景 + 彩色边框

---

## 🔍 故障排查

### 问题 1: 命令找不到

```bash
# 检查是否有执行权限
ls -l launch*.sh

# 添加执行权限
chmod +x launch_auto.sh launch_full_pipeline.sh launch_with_caption.sh
```

### 问题 2: 依赖缺失

```bash
# 安装完整依赖
pip3 install requests beautifulsoup4 arxiv tqdm openai anthropic streamlit
```

### 问题 3: API Key 未设置

```bash
# 检查环境变量
echo $OPENAI_API_KEY
echo $ANTHROPIC_API_KEY

# 临时设置（当前 session）
export OPENAI_API_KEY="sk-..."

# 永久设置（写入配置文件）
echo 'export OPENAI_API_KEY="sk-..."' >> ~/.bashrc
source ~/.bashrc
```

### 问题 4: 没有生成 HTML

**可能原因：**
1. 论文没有 arXiv HTML 版本（只有 PDF）
2. 网络问题导致图片下载失败
3. 调研报告中没有 arXiv ID

**解决方法：**
```bash
# 检查是否有爬取到数据
ls -la paper_captions/

# 查看调研报告中的 arXiv ID
grep "arxiv.org/pdf/" survey_result_*.md
```

---

## 📚 相关文档

- **端到端使用指南**: `END_TO_END_GUIDE.md` ⭐️
- **快速上手**: `QUICKSTART.md`
- **详细文档**: `CAPTION_CRAWLER_README.md`
- **文件说明**: `CAPTION_CRAWLER_FILES.md`
- **集成总结**: `INTEGRATION_SUMMARY.md`

---

## 🎊 推荐工作流

### 最简单的方式（推荐）

```bash
# 1. 一行命令搞定
./launch_auto.sh "your keywords"

# 2. 打开生成的 HTML
open paper_captions.html  # macOS
xdg-open paper_captions.html  # Linux
```

### 需要交互控制

```bash
# 1. 启动完整流程
./launch_full_pipeline.sh

# 2. 在浏览器中完成搜索
# 3. 关闭浏览器后自动继续
# 4. 查看生成的文件
```

### 分步执行（调试用）

```bash
# 1. 生成调研报告
./launch.sh
# 在浏览器中完成

# 2. 爬取图片并生成 HTML
./launch_with_caption.sh
```

---

**Enjoy! 🚀**
