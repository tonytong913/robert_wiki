# 会话管理

## 概述

OpenClaw 将对话组织成**会话**。每条消息根据来源路由到会话——DM、群聊、定时任务等。

## 消息路由

| 来源 | 行为 |
|------|------|
| 直接消息 (DM) | 默认共享会话 |
| 群聊 | 每个群组隔离 |
| 房间/频道 | 每个房间隔离 |
| 定时任务 | 每次运行新会话 |
| Webhooks | 每个 hook 隔离 |

## DM 隔离

默认所有 DM 共享一个会话以保持连续性。单用户设置没问题。

**警告**: 如果多个人可以发消息给你的 Agent，启用 DM 隔离。否则所有用户共享相同的对话上下文。

**解决方案**:

```json5
{
  session: {
    dmScope: "per-channel-peer", // 按通道 + 发送者隔离
  },
}
```

选项：
- `main` (默认) - 所有 DM 共享一个会话
- `per-peer` - 按发送者隔离（跨通道）
- `per-channel-peer` - 按通道 + 发送者隔离（推荐）
- `per-account-channel-peer` - 按账户 + 通道 + 发送者隔离

**身份链接**: 如果同一个人从多个通道联系你，使用 `session.identityLinks` 链接身份。

## 会话生命周期

会话在过期前被重用：

- **每日重置** (默认) - 网关主机本地时间凌晨 4:00 新会话
- **空闲重置** (可选) - 不活动后新会话。设置 `session.reset.idleMinutes`
- **手动重置** - 聊天中输入 `/new` 或 `/reset`。`/new <model>` 也切换模型

同时配置每日和空闲重置时，先过期的生效。

## 状态存储位置

所有会话状态由 **gateway** 拥有。UI 客户端查询 gateway 获取会话数据。

- **存储**: `~/.openclaw/agents/<agentId>/sessions/sessions.json`
- **记录**: `~/.openclaw/agents/<agentId>/sessions/<sessionId>.jsonl`

## 会话维护

OpenClaw 自动限制会话存储。默认 `warn` 模式（报告将要清理的内容）。

```json5
{
  session: {
    maintenance: {
      mode: "enforce",
      pruneAfter: "30d",
      maxEntries: 500,
    },
  },
}
```

预览: `openclaw sessions cleanup --dry-run`

## 检查会话

```bash
openclaw sessions list                    # 列出会话
openclaw sessions list --json             # JSON 输出
openclaw sessions list --active 30        # 过去 30 分钟活跃
openclaw sessions history <key>           # 获取会话历史
```

## 相关实体
- [[OpenClaw]]

## 相关概念
- [[Agent_Loop]]
- [[Multi_Agent_Routing]]
