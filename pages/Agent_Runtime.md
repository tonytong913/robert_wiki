# Agent 运行时

## 概述

OpenClaw 运行单一的嵌入式 Agent 运行时，基于 Pi Agent 核心（模型、工具和提示管道）。

## 工作空间 (Workspace)

OpenClaw 使用单一 Agent 工作空间目录作为 Agent 的唯一工作目录 (`cwd`)。

**默认路径**: `~/.openclaw/workspace`

**沙盒模式**: 非主会话可覆盖为每会话工作空间

## 引导文件

首次会话时，OpenClaw 将这些文件注入 Agent 上下文：

| 文件 | 用途 |
|------|------|
| `AGENTS.md` | 操作指令 + "记忆" |
| `SOUL.md` | 角色、边界、语气 |
| `TOOLS.md` | 用户维护的工具笔记 |
| `BOOTSTRAP.md` | 首次运行仪式（完成后删除） |
| `IDENTITY.md` | Agent 名称/氛围/表情 |
| `USER.md` | 用户资料 + 称呼偏好 |

大文件会被截断并标记，保持提示精简。

## 内置工具

核心工具始终可用：
- `read` / `write` / `edit` - 文件 I/O
- `exec` / `process` - 执行命令
- `browser` - 浏览器控制
- `web_search` / `web_fetch` - 网络搜索/获取
- `message` - 跨通道发送消息
- `canvas` - 节点 Canvas 控制
- `cron` / `gateway` - 定时任务/Gateway 管理
- `sessions_*` / `subagents` - 会话和子代理管理

## Skills

Skills 从以下位置加载（优先级从高到低）：
1. 工作空间: `<workspace>/skills`
2. 项目 Agent skills: `<workspace>/.agents/skills`
3. 个人 Agent skills: `~/.agents/skills`
4. 托管/本地: `~/.openclaw/skills`
5. 捆绑（随安装提供）
6. 额外 skill 文件夹: `skills.load.extraDirs`

## 会话存储

会话记录存储为 JSONL：
```
~/.openclaw/agents/<agentId>/sessions/<SessionId>.jsonl
```

## 流式控制

- **队列模式**: `steer`（注入当前运行）/ `followup` / `collect`
- **块流式**: 默认关闭，可配置
- **软块分块**: 800-1200 字符，优先段落断点

## 模型引用

格式: `provider/model`

示例:
- `anthropic/claude-sonnet-4-6`
- `openrouter/moonshotai/kimi-k2`

省略 provider 时，OpenClaw 尝试别名，然后匹配配置，最后回退默认。

## 最小配置

```json5
{
  agents: {
    defaults: {
      workspace: "~/.openclaw/workspace"
    }
  },
  channels: {
    whatsapp: {
      allowFrom: ["+15555550123"]
    }
  }
}
```

## 相关实体
- [[OpenClaw]]
- [[Multi_Agent_Routing]]

## 相关概念
- [[Multi_Agent_Routing]]
- [[Session_Management]]
