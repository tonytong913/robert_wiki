# 多 Agent 路由

## 概述

目标: 在一个 Gateway 进程中运行多个**隔离**的 Agent（独立工作空间 + agentDir + 会话），外加多个通道账户。

## 什么是"一个 Agent"

一个 **Agent** 是一个完全独立的大脑，拥有自己的：

- **工作空间** - 文件、AGENTS.md/SOUL.md/USER.md、本地笔记
- **状态目录** (`agentDir`) - 认证配置、模型注册表、每 Agent 配置
- **会话存储** - 聊天历史 + 路由状态

**路径映射**:
```
配置: ~/.openclaw/openclaw.json
状态: ~/.openclaw/agents/<agentId>/agent
会话: ~/.openclaw/agents/<agentId>/sessions
工作空间: ~/.openclaw/workspace-<agentId>
```

## 单 Agent 模式（默认）

- `agentId` 默认为 `main`
- 会话键: `agent:main:<mainKey>`
- 工作空间: `~/.openclaw/workspace`

## 创建新 Agent

```bash
openclaw agents add work
openclaw agents add coding
openclaw agents add social
```

## 路由规则

Bindings 是**确定性**的，**最具体匹配优先**：

1. `peer` 匹配（精确 DM/群组/通道 ID）
2. `parentPeer` 匹配（线程继承）
3. `guildId + roles`（Discord 角色路由）
4. `guildId`（Discord）
5. `teamId`（Slack）
6. `accountId` 匹配
7. 通道级匹配 (`accountId: "*"`)
8. 回退到默认 Agent

## 配置示例

### WhatsApp 号码 per Agent

```json5
{
  agents: {
    list: [
      { id: "home", workspace: "~/.openclaw/workspace-home" },
      { id: "work", workspace: "~/.openclaw/workspace-work" },
    ],
  },
  bindings: [
    { agentId: "home", match: { channel: "whatsapp", accountId: "personal" } },
    { agentId: "work", match: { channel: "whatsapp", accountId: "biz" } },
  ],
  channels: {
    whatsapp: {
      accounts: {
        personal: {},
        biz: {},
      },
    },
  },
}
```

### 同一通道，特定 peer 路由到不同 Agent

```json5
{
  agents: {
    list: [
      { id: "chat", model: "anthropic/claude-sonnet-4-6" },
      { id: "opus", model: "anthropic/claude-opus-4-6" },
    ],
  },
  bindings: [
    {
      agentId: "opus",
      match: { channel: "whatsapp", peer: { kind: "direct", id: "+15551234567" } },
    },
    { agentId: "chat", match: { channel: "whatsapp" } },
  ],
}
```

### Discord bots per Agent

```json5
{
  agents: {
    list: [
      { id: "main", workspace: "~/.openclaw/workspace-main" },
      { id: "coding", workspace: "~/.openclaw/workspace-coding" },
    ],
  },
  bindings: [
    { agentId: "main", match: { channel: "discord", accountId: "default" } },
    { agentId: "coding", match: { channel: "discord", accountId: "coding" } },
  ],
  channels: {
    discord: {
      accounts: {
        default: { token: "TOKEN_MAIN" },
        coding: { token: "TOKEN_CODING" },
      },
    },
  },
}
```

## Agent 间通信

默认关闭，需显式启用：

```json5
{
  tools: {
    agentToAgent: {
      enabled: true,
      allow: ["home", "work"],
    },
  },
}
```

## 每 Agent 沙盒和工具配置

```json5
{
  agents: {
    list: [
      {
        id: "personal",
        sandbox: { mode: "off" },
        // 无工具限制
      },
      {
        id: "family",
        sandbox: { mode: "all", scope: "agent" },
        tools: {
          allow: ["read"],
          deny: ["exec", "write", "edit"],
        },
      },
    ],
  },
}
```

## 关键概念

- `agentId`: 一个"大脑"
- `accountId`: 一个通道账户实例
- `binding`: 按 `(channel, accountId, peer)` 路由消息到 `agentId`

## 相关实体
- [[OpenClaw]]

## 相关概念
- [[Agent 运行时]]
- [[Gateway 架构]]
