# 快速参考卡片

## 🚀 我应该用哪个脚本？

### 场景 1: 日常调研（推荐 ⭐️）

```bash
./launch_auto.sh "tool learning"
```

**一行命令完成所有工作！**
- ✅ 搜索论文
- ✅ 生成调研报告
- ✅ 爬取图片
- ✅ 生成 HTML

---

### 场景 2: 需要浏览器界面交互

```bash
./launch_full_pipeline.sh
```

**自动监控模式**
- 🌐 浏览器界面输入关键词
- ⏳ 后台自动监控
- ✅ 检测到报告后自动继续

---

### 场景 3: 只想生成 HTML（已有报告）

```bash
./launch_with_caption.sh
```

**跳过搜索，直接生成 HTML**
- 📄 使用最新的 survey_result*.md
- 🖼️ 爬取图片
- 🌐 生成 HTML

---

### 场景 4: 分两步手动执行

```bash
# 步骤 1: 生成报告
./launch.sh

# 步骤 2: 生成 HTML
./launch_with_caption.sh
```

**适合调试或单独使用**

---

## 📊 快速对比

| 脚本 | 自动化 | 需要浏览器 | 输入方式 |
|------|--------|-----------|---------|
| `launch_auto.sh` | ⭐️⭐️⭐️⭐️⭐️ | ❌ | 命令行 |
| `launch_full_pipeline.sh` | ⭐️⭐️⭐️⭐️ | ✅ | 浏览器 |
| `launch_with_caption.sh` | ⭐️⭐️⭐️⭐️ | ❌ | 自动 |
| `launch.sh` | ⭐️⭐️ | ✅ | 浏览器 |

---

## 💡 常用命令

### 基础使用

```bash
# 搜索单个关键词
./launch_auto.sh "tool learning"

# 搜索多个关键词
./launch_auto.sh "large language models" "reasoning"

# 测试功能
./test_caption_crawler.sh
```

### 高级配置

```bash
# 限制搜索结果数
MAX_RESULTS=30 ./launch_auto.sh "tool learning"

# 使用 Claude
LLM_PROVIDER=anthropic ./launch_auto.sh "tool learning"

# 使用 GPT-4
MODEL_NAME=gpt-4 ./launch_auto.sh "tool learning"
```

---

## 📚 详细文档

- **完整指南**: `END_TO_END_GUIDE.md`
- **脚本说明**: `SCRIPTS_OVERVIEW.md`
- **快速上手**: `QUICKSTART.md`
- **技术总结**: `END_TO_END_SUMMARY.md`

---

## ⚡️ 30 秒快速开始

```bash
# 1. 进入目录
cd /mnt/bn/med-mllm-lfv2/linjh/project/learn/idke/survey_agent

# 2. 运行
./launch_auto.sh "your keywords"

# 3. 等待完成（5-15 分钟）

# 4. 打开 HTML
open paper_captions.html
```

**就这么简单！** 🎉
