# 记忆系统

## 概述

OpenClaw 通过将**纯 Markdown 文件**写入 Agent 工作空间来记忆事物。模型只"记住"保存到磁盘的内容——没有隐藏状态。

## 记忆存储位置

### 1. MEMORY.md - 长期记忆

- 持久的事实、偏好和决策
- 每个 DM 会话开始时加载
- 适用于安全/私密的个人上下文

### 2. memory/YYYY-MM-DD.md - 每日笔记

- 运行上下文和观察
- 自动加载今天和昨天的笔记
- 用于近期活动的原始记录

**位置**: Agent 工作空间 (默认 `~/.openclaw/workspace`)

## 记忆工具

Agent 有两个工具用于处理记忆：

| 工具 | 功能 |
|------|------|
| `memory_search` | 使用语义搜索查找相关笔记 |
| `memory_get` | 读取特定记忆文件或行范围 |

## 记忆搜索

配置嵌入提供商后，`memory_search` 使用**混合搜索**：
- **向量相似度** - 语义含义匹配
- **关键词匹配** - 精确术语（如 ID 和代码符号）

OpenClaw 从可用 API 密钥自动检测嵌入提供商：
- OpenAI
- Gemini
- Voyage
- Mistral

## 何时搜索记忆

在回答以下问题前**必须**运行 `memory_search`：
- 关于先前工作的问题
- 决策、日期、人员、偏好
- 待办事项

## 记忆文件格式

### MEMORY.md 示例

```markdown
# 记忆

## 偏好
- 喜欢 TypeScript 胜过 JavaScript
- 偏好简洁回复

## 项目
- 正在构建 Wiki 系统
- 使用 OpenClaw 作为基础

## 决策
- 2026-04-06: 采用 Markdown 格式存储所有内容
```

### 每日笔记示例

```markdown
# 2026-04-06

## 活动
- 搭建 LLM Wiki 系统
- 阅读 OpenClaw 文档

## 学习
- 了解了 Gateway 架构
- 学习了多 Agent 路由
```

## 安全注意事项

- **MEMORY.md** 只在主会话（直接聊天）加载
- **不在共享上下文加载**（Discord、群聊等）
- 这是为了安全——防止个人上下文泄露给陌生人

## 相关实体
- [[OpenClaw]]

## 相关概念
- [[Agent_Runtime]]
