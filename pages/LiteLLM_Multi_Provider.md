---
title: LiteLLM_Multi_Provider
type: source-summary
sources:
  - raw/articles/litellm-multi-provider-guide.md
related:
  - "[[Model_Providers]]"
  - "[[Gateway_Configuration]]"
tags: [LiteLLM, LLM代理, 多Provider, DashScope, DeepSeek, 配置]
created: 2026-05-02
updated: 2026-05-02
confidence: high
---

# LiteLLM_Multi_Provider（多 Provider LLM 统一代理）

**LiteLLM 是一个开源 LLM 代理服务器，将多个 LLM 提供商（通义千问、Kimi、智谱、DeepSeek）聚合为一个 OpenAI 兼容 API 端点。**

---

## 核心价值

| 特性 | 说明 |
|------|------|
| **统一接口** | 所有模型通过 `http://localhost:4000/v1` 访问 |
| **多 Provider 聚合** | 通义千问、Kimi、智谱 GLM、DeepSeek 一站式调用 |
| **Anthropic 兼容端点** | 使用 DashScope/DeepSeek 的 Anthropic 兼容 API |
| **参数自动适配** | `drop_params: true` 丢弃不支持的参数 |

## 架构

```
Claude Code → LiteLLM Proxy (localhost:4000) → DashScope (qwen3.6+, kimi-k2.5, glm-5)
                                              → DeepSeek (v4-pro, v4-flash)
```

## 后台运行

| 方式 | 命令 | 适用场景 |
|------|------|---------|
| **nohup** | `nohup bash start.sh > log 2>&1 &` | 简单临时运行 |
| **tmux** | `tmux new -d -s litellm 'bash start.sh'` | 日常使用，随时查看/重启 |

tmux 管理：`tmux attach -t litellm`（进入）、`Ctrl+B D`（退出）、`tmux kill-session -t litellm`（停止）

## 已配置模型

| 模型名 | 提供商 | 端点类型 |
|--------|--------|---------|
| `qwen3.6-plus` | DashScope | Anthropic 兼容 |
| `kimi-k2.5` | DashScope | Anthropic 兼容 |
| `glm-5` | DashScope | Anthropic 兼容 |
| `deepseek-v4-pro` | DeepSeek | Anthropic 兼容 |
| `deepseek-v4-flash` | DeepSeek | Anthropic 兼容 |

## 关键配置

- 环境变量通过 `.env` 文件管理（不提交 Git）
- API Key 使用 `os.environ/XXX` 从环境读取，不硬编码
- 每个模型使用 `anthropic/xxx` 前缀访问 Anthropic 兼容端点

---

## 相关页面

- [[Model_Providers|模型提供商]] — 支持的 LLM 提供商
- [[Gateway_Configuration|Gateway 配置]] — OpenClaw Gateway 配置参考

## 来源

- [LiteLLM 多 Provider 统一代理配置指南](../raw/articles/litellm-multi-provider-guide.md)

---

*标签: #LiteLLM #LLM代理 #多Provider #DashScope #DeepSeek #配置*
