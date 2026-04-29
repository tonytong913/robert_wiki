# 网络搜索

## 概述

`web_search` 工具使用配置的提供商搜索网页并返回结果。查询缓存 15 分钟（可配置）。

还有 `x_search` 用于 X (Twitter) 帖子搜索，`web_fetch` 用于轻量级 URL 获取。

## 提供商选择

| 提供商 | 特点 |
|--------|------|
| **Brave Search** | 结构化结果，支持 `llm-context` 模式，国家/语言过滤，免费额度 |
| **DuckDuckGo** | 无需 API 密钥，非官方 HTML 集成 |
| **Exa** | 神经 + 关键词搜索，内容提取 |
| **Firecrawl** | 结构化结果，深度提取 |
| **Gemini** | AI 合成答案，Google Search 支持 |
| **Grok** | AI 合成答案，xAI 网络支持 |
| **Kimi** | Moonshot 搜索 |
| **Perplexity** | AI 驱动搜索 |
| **SearXNG** | 自托管搜索 |
| **Tavily** | AI 搜索 API |

## 配置

```bash
openclaw configure --section web
```

或设置环境变量：
- `BRAVE_API_KEY`
- `TAVILY_API_KEY`
- `PERPLEXITY_API_KEY`

## 使用

```javascript
await web_search({ query: "OpenClaw plugin SDK" });
await x_search({ query: "dinner recipes" });
await web_fetch({ url: "https://example.com" });
```

## 自动检测

OpenClaw 按以下顺序自动检测：
1. 配置中的显式提供商
2. 环境变量中的 API 密钥
3. 回退到 DuckDuckGo（无需密钥）

## 相关实体
- [[OpenClaw]]

## 相关概念
- [[工具系统]]
