# 模型提供商

## 概述

OpenClaw 支持多种 LLM 提供商。选择提供商，认证，然后设置默认模型为 `provider/model`。

## 快速开始

1. 通过 `openclaw onboard` 认证提供商
2. 设置默认模型：

```json5
{
  agents: {
    defaults: {
      model: { primary: "anthropic/claude-opus-4-6" }
    }
  }
}
```

## 支持的提供商

| 提供商 | 特点 |
|--------|------|
| **Anthropic** | Claude API + Claude CLI |
| **OpenAI** | API + Codex |
| **Google** | Gemini |
| **Moonshot** | Kimi + Kimi Coding |
| **MiniMax** | 中文模型 |
| **Mistral** | 欧洲模型 |
| **xAI** | Grok |
| **OpenRouter** | 统一接口 |
| **Fireworks** | 推理优化 |
| **Chutes** | 无服务器 |
| **Qwen** | 阿里巴巴 |
| **GLM** | 智谱 |
| **Z.AI** | 零一万物 |
| **Venice** | 隐私优先 |
| **BytePlus** | 字节跳动 |
| **StepFun** | 阶跃星辰 |

## 模型引用格式

```
provider/model
```

示例：
- `anthropic/claude-opus-4-6`
- `openai/gpt-4o`
- `google/gemini-2.5-pro`

## 认证方式

- **API Key** - 直接设置
- **OAuth** - 订阅认证（如 OpenAI Codex）
- **GitHub Copilot** - `openclaw onboard --auth-choice copilot-proxy`

## 回退链

```json5
{
  agents: {
    defaults: {
      model: {
        primary: "anthropic/claude-opus-4-6",
        fallbacks: ["openai/gpt-4o", "google/gemini-2.5-pro"]
      }
    }
  }
}
```

## 相关实体
- [[OpenClaw]]

## 相关概念
- [[Agent_Runtime]]
