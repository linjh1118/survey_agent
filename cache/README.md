# 📁 Survey Agent 缓存系统

Survey Agent 的智能缓存系统，用于优化论文摘要生成性能，避免重复的API调用。

## 🎯 功能概述

缓存系统基于论文的 `arxiv.id` 对生成的摘要进行持久化存储，大大提升了重复查询的效率：

- **自动缓存**：每次生成的论文摘要自动保存
- **智能复用**：相同 arxiv.id 的论文直接使用缓存结果
- **内容检测**：通过内容哈希检测论文变化，确保缓存有效性
- **过期管理**：30天自动过期机制，保持缓存新鲜度
- **透明使用**：对用户完全透明，无需额外配置

## 📊 性能提升

- **首次查询**：正常API调用时间（~20秒/论文）
- **缓存命中**：近乎瞬时响应（<0.1秒/论文）
- **效率提升**：重复查询速度提升 **200-1000倍**

## 🏗️ 核心实现

### 架构设计

```
缓存系统架构
├── PaperCache 类 (cache.py)
│   ├── 智能 arxiv.id 提取
│   ├── 内容哈希验证
│   ├── JSON 持久化存储
│   └── 自动过期清理
│
├── 集成点 (summarize.py)
│   ├── 摘要生成前检查缓存
│   ├── 生成后自动缓存
│   └── 模型信息记录
│
└── 存储文件
    └── paper_summaries.json
```

### 关键实现细节

#### 1. arxiv.id 智能提取
```python
def _extract_arxiv_id(self, paper: Dict[str, Any]) -> Optional[str]:
    # 支持多种格式：
    # - 直接从 arxiv_id 字段
    # - 从 URL 中提取 (arxiv.org/pdf/2406.09172v2)
    # - 从 DOI 中提取
```

#### 2. 内容变化检测
```python
def _generate_content_hash(self, paper: Dict[str, Any]) -> str:
    # 使用 MD5 哈希检测内容变化
    # 包含：标题 + 摘要 + PDF文本前1000字符
```

#### 3. 缓存条目结构
```json
{
  "2506.09172": {
    "arxiv_id": "2506.09172",
    "title": "论文标题",
    "summary": "生成的摘要内容...",
    "content_hash": "md5哈希值",
    "cached_at": "2025-06-22T23:38:30.231146",
    "model_info": {
      "provider": "doubao",
      "model_name": "ep-20250526175303-cv654"
    }
  }
}
```

## 🔧 技术特性

### 自动过期清理
- 默认30天过期时间
- 启动时自动清理过期条目
- 可配置过期时间

### 错误容错
- 损坏的缓存文件自动重建
- 缺失字段的优雅处理
- 网络错误时不影响缓存读取

### 统计信息
```python
stats = cache.get_cache_stats()
# 返回：总条目数、文件大小、最新/最旧条目时间等
```

## 📝 使用示例

缓存功能完全透明，无需特殊配置：

```python
from survey_agent.survey import generate_survey

# 第一次运行：正常API调用 + 自动缓存
generate_survey(terms=["AI", "ML"], max_results=5)

# 第二次运行：直接使用缓存，瞬时完成
generate_survey(terms=["AI", "ML"], max_results=5)
```

### 手动缓存管理
```python
from survey_agent.utils.cache import get_paper_cache

cache = get_paper_cache()

# 查看统计信息
print(cache.get_cache_stats())

# 清空缓存
cache.clear_cache()
```

## 🎨 用户体验

### 状态提示
- `📁 使用缓存摘要: 论文标题...` - 缓存命中
- `💾 已缓存摘要: 论文标题...` - 新生成并缓存
- `🔄 论文内容已更新，重新生成摘要` - 内容变化检测

### 性能监控
每次运行后可以看到：
- 缓存命中率
- 时间节省统计
- 缓存文件大小

## 🛠️ 实现文件

| 文件 | 功能 |
|------|------|
| `src/survey_agent/utils/cache.py` | 核心缓存实现 |
| `src/survey_agent/llm/summarize.py` | 缓存集成点 |
| `cache/paper_summaries.json` | 缓存数据文件 |

## 🔮 未来扩展

- [ ] 支持多级缓存（内存+磁盘）
- [ ] 缓存压缩和优化
- [ ] 分布式缓存支持
- [ ] 更精细的缓存策略
- [ ] 缓存统计和分析工具

---

**注意**：缓存文件包含生成的论文摘要，请根据需要备份或添加到 `.gitignore`。 