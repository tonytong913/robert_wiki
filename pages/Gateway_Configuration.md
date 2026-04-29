# Gateway 配置

## 概述

OpenClaw 从 `~/.openclaw/openclaw.json` 读取可选的 JSON5 配置。

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

## 编辑配置

### 交互式向导
```bash
openclaw onboard       # 完整引导流程
openclaw configure     # 配置向导
```

### CLI 命令
```bash
openclaw config get agents.defaults.workspace
openclaw config set agents.defaults.heartbeat.every "2h"
openclaw config unset plugins.entries.brave.config.webSearch.apiKey
```

### 控制界面
打开 http://127.0.0.1:18789，使用 **Config** 标签页。

### 直接编辑
编辑 `~/.openclaw/openclaw.json`，Gateway 监视文件并自动应用更改。

## 严格验证

OpenClaw 只接受完全匹配模式的配置。未知键、格式错误的类型或无效值会导致 Gateway **拒绝启动**。

验证失败时：
- Gateway 不启动
- 只有诊断命令可用
- 运行 `openclaw doctor` 查看问题
- 运行 `openclaw doctor --fix` 应用修复

## 常见任务

### 设置通道
```json5
{
  channels: {
    telegram: {
      enabled: true,
      botToken: "123:abc"
    }
  }
}
```

### 设置模型
```json5
{
  agents: {
    defaults: {
      model: { primary: "anthropic/claude-opus-4-6" }
    }
  }
}
```

### 设置定时任务
```json5
{
  cron: {
    jobs: [
      {
        name: "Daily summary",
        schedule: "0 9 * * *",
        session: "main",
        systemEvent: "Generate daily summary"
      }
    ]
  }
}
```

## 热重载

Gateway 监视配置文件并在更改时自动应用（无需重启）。

## 相关实体
- [[OpenClaw]]

## 相关概念
- [[Gateway架构]]
- [[CLI命令参考]]
