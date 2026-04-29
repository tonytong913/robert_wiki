# 子代理

## 概述

子代理是从现有 Agent 运行中派生的后台 Agent 运行。它们在自己的会话中运行，完成后**宣布**结果回请求者聊天通道。

## 斜杠命令

使用 `/subagents` 检查或控制**当前会话**的子代理运行：

| 命令 | 功能 |
|------|------|
| `/subagents list` | 列出子代理 |
| `/subagents kill <id>` | 终止子代理 |
| `/subagents log <id>` | 查看日志 |
| `/subagents info <id>` | 查看详情 |
| `/subagents send <id> <msg>` | 发送消息 |
| `/subagents steer <id> <msg>` | 引导子代理 |
| `/subagents spawn <agentId> <task>` | 派生子代理 |

## 派生行为

- 派生命令非阻塞，立即返回 run id
- 完成时，子代理向请求者聊天通道宣布摘要/结果
- 完成是**推送式**的，不要轮询等待
- 完成时会关闭子代理打开的浏览器标签/进程

## 工具使用

使用 `sessions_spawn`：

```javascript
await sessions_spawn({
  task: "研究任务",
  mode: "run",
  runtime: "subagent",
});
```

## ACP 代理

对于 ACP 工具会话（Codex、Claude Code、Gemini CLI）：

```javascript
await sessions_spawn({
  task: "编码任务",
  mode: "session",
  runtime: "acp",
  thread: true,
});
```

## 成本注意

每个子代理有自己的上下文和令牌使用。对于繁重或重复任务，为子代理设置更便宜的模型。

## 配置

```json5
{
  agents: {
    defaults: {
      subagents: {
        model: "anthropic/claude-sonnet-4-6",
      },
    },
  },
}
```

## 相关实体
- [[OpenClaw]]

## 相关概念
- [[Multi_Agent_Routing]]
- [[Agent_Loop]]
