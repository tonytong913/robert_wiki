# Agent 工作空间

## 概述

工作空间是 Agent 的家。它是文件工具和工作空间上下文的唯一工作目录。保持私密，视为记忆。

与 `~/.openclaw/` 分开，后者存储配置、凭证和会话。

**重要**: 工作空间是**默认 cwd**，不是硬沙盒。工具根据工作空间解析相对路径，但绝对路径仍可到达主机其他位置，除非启用沙盒。

## 默认位置

- 默认: `~/.openclaw/workspace`
- 如果设置了 `OPENCLAW_PROFILE` 且不是 `"default"`: `~/.openclaw/workspace-<profile>`
- 在 `~/.openclaw/openclaw.json` 中覆盖:

```json5
{
  agent: {
    workspace: "~/.openclaw/workspace",
  },
}
```

## 标准文件

### AGENTS.md
- Agent 的操作指令和如何使用记忆
- 每个会话开始时加载
- 适合规则、优先级和"如何行为"细节

### SOUL.md
- 角色、语气和边界
- 每个会话加载

### USER.md
- 用户是谁以及如何称呼他们
- 每个会话加载

### IDENTITY.md
- Agent 身份（名称、表情、头像）
- 每个会话加载

### TOOLS.md
- 用户维护的工具笔记
- 技能定义工具如何工作，此文件用于你的特定设置

### BOOTSTRAP.md
- 首次运行仪式（完成后删除）

### MEMORY.md
- 长期记忆
- 跨会话持久

### memory/
- 每日笔记: `memory/YYYY-MM-DD.md`
- 今天和昨天的笔记自动加载

### skills/
- 自定义 skills
- 从工作空间加载

## 禁用引导文件创建

```json5
{ agent: { skipBootstrap: true } }
```

## 备份策略

工作空间是**纯文本文件**。备份：

```bash
# 创建备份
cp -r ~/.openclaw/workspace ~/backups/workspace-$(date +%Y%m%d)

# 或使用 Git
cd ~/.openclaw/workspace
git init
git add .
git commit -m "Initial backup"
```

## 相关实体
- [[OpenClaw]]

## 相关概念
- [[Agent运行时]]
- [[记忆系统]]
