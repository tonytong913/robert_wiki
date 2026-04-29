# 定时任务 (Cron)

## 概述

Cron 是 Gateway 的内置调度器。它持久化任务，在正确的时间唤醒 Agent，可以将输出交付回聊天通道或 webhook 端点。

## 快速开始

```bash
# 添加一次性提醒
openclaw cron add \
  --name "Reminder" \
  --at "2026-02-01T16:00:00Z" \
  --session main \
  --system-event "Reminder: check the cron docs draft" \
  --wake now \
  --delete-after-run

# 查看任务
openclaw cron list

# 查看运行历史
openclaw cron runs --id <job-id>
```

## 工作原理

- Cron 在 **Gateway 进程内**运行（不在模型内）
- 任务持久化在 `~/.openclaw/cron/jobs.json`
- 所有 cron 执行创建 [后台任务](/automation/tasks) 记录
- 一次性任务成功后默认自动删除

## 调度类型

| 类型 | CLI 标志 | 说明 |
|------|----------|------|
| `at` | `--at` | 一次性时间戳（ISO 8601 或相对如 `20m`） |
| `every` | `--every` | 固定间隔 |
| `cron` | `--cron` | 5 或 6 字段 cron 表达式 |

时区：无时区的时间戳视为 UTC。添加 `--tz Asia/Shanghai` 进行本地调度。

## 执行方式

| 方式 | `--session` 值 | 运行在 | 适合 |
|------|----------------|--------|------|
| 主会话 | `main` | 下次心跳 | 提醒、系统事件 |
| 隔离 | `isolated` | 专用 `cron:<jobId>` | 报告、后台任务 |
| 当前会话 | `current` | 创建时绑定 | 上下文感知重复工作 |
| 自定义会话 | `session:custom-id` | 持久命名会话 | 基于历史的工作流 |

## 常用命令

```bash
openclaw cron status          # 状态
openclaw cron list            # 列出任务
openclaw cron add ...         # 添加任务
openclaw cron edit <id>       # 编辑任务
openclaw cron rm <id>         # 删除任务
openclaw cron enable <id>     # 启用
openclaw cron disable <id>    # 禁用
openclaw cron runs --id <id>  # 运行历史
openclaw cron run <id>        # 立即运行
```

## 配置示例

```json5
{
  cron: {
    jobs: [
      {
        name: "Daily summary",
        schedule: "0 9 * * *",
        tz: "Asia/Shanghai",
        session: "main",
        systemEvent: "Generate daily summary",
        wake: "now"
      }
    ]
  }
}
```

## 相关实体
- [[OpenClaw]]

## 相关概念
- [[Gateway_Configuration]]
