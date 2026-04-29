# Exec 工具

## 概述

在工作空间中运行 shell 命令。支持前台 + 后台执行（通过 `process`）。

## 参数

| 参数 | 说明 |
|------|------|
| `command` (必需) | 要执行的命令 |
| `workdir` | 工作目录（默认 cwd） |
| `env` | 环境变量覆盖 |
| `yieldMs` | 自动后台延迟（默认 10000ms） |
| `background` | 立即后台运行 |
| `timeout` | 超时秒数（默认 1800） |
| `pty` | 在伪终端中运行（TTY 必需） |
| `host` | 执行位置: `auto`/`sandbox`/`gateway`/`node` |
| `security` | 执行模式: `deny`/`allowlist`/`full` |
| `ask` | 批准提示: `off`/`on-miss`/`always` |
| `node` | 节点 ID/名称（用于 `host=node`） |
| `elevated` | 请求提升模式（逃离沙盒） |

## Host 路由

- `host=auto` (默认): 沙盒运行时激活则使用沙盒，否则使用 gateway
- `host=gateway`: 在 Gateway 主机上执行
- `host=node`: 在配对节点上执行
- `host=sandbox`: 在沙盒中执行

## 配置

```json5
{
  tools: {
    exec: {
      host: "auto",
      security: "deny",
      ask: "off",
      notifyOnExit: true,
      pathPrepend: ["~/bin", "/opt/oss/bin"],
    },
  },
}
```

## PATH 处理

- `host=gateway`: 合并登录 shell 的 PATH
- `host=sandbox`: 在容器内运行 `sh -lc`
- `host=node`: 只发送非阻塞的环境覆盖

## 批准控制

Gateway/Node 执行批准由 `~/.openclaw/exec-approvals.json` 控制。

## 最佳实践

- 长时间运行的任务使用 `process` 管理
- 需要调度的任务使用 `cron`
- 避免用 sleep/delay 模式模拟调度

## 相关实体
- [[OpenClaw]]

## 相关概念
- [[Tool_System]]
