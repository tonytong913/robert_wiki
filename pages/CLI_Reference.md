# CLI 命令参考

## 概述

OpenClaw CLI 提供完整的命令行接口，用于管理 Gateway、Agent、通道、节点等所有功能。

## 全局标志

| 标志 | 说明 |
|------|------|
| `--dev` | 隔离状态到 `~/.openclaw-dev`，端口偏移 |
| `--profile <name>` | 隔离状态到 `~/.openclaw-<name>` |
| `--container <name>` | 目标容器执行 |
| `--no-color` | 禁用 ANSI 颜色 |
| `--update` | 简写为 `openclaw update` |
| `-V, --version` | 打印版本 |

## 命令分类

### 1. 设置和初始化

| 命令 | 功能 |
|------|------|
| `openclaw setup` | 初始化配置 + 工作空间 |
| `openclaw onboard` | 交互式引导 |
| `openclaw configure` | 交互式配置向导 |
| `openclaw config` | 非交互式配置 (get/set/unset) |
| `openclaw completion` | 生成 shell 补全脚本 |
| `openclaw doctor` | 健康检查 + 快速修复 |

### 2. Gateway 管理

| 命令 | 功能 |
|------|------|
| `openclaw gateway` | 运行 Gateway 前台进程 |
| `openclaw gateway run` | 前台运行别名 |
| `openclaw gateway status` | 服务状态 + RPC 探测 |
| `openclaw gateway health` | 健康检查 |
| `openclaw gateway probe` | 全面探测所有目标 |
| `openclaw gateway discover` | Bonjour 发现 Gateway |
| `openclaw gateway call <method>` | 底层 RPC 调用 |
| `openclaw gateway install/start/stop/restart/uninstall` | 服务管理 |

### 3. Agent 管理

| 命令 | 功能 |
|------|------|
| `openclaw agents list` | 列出配置的 Agents |
| `openclaw agents add <name>` | 添加新 Agent |
| `openclaw agents delete <id>` | 删除 Agent |
| `openclaw agents bindings` | 查看路由绑定 |
| `openclaw agents bind` | 添加路由绑定 |
| `openclaw agents unbind` | 移除路由绑定 |
| `openclaw agents set-identity` | 设置 Agent 身份 |

### 4. 通道管理

| 命令 | 功能 |
|------|------|
| `openclaw channels list` | 列出配置的通道 |
| `openclaw channels status` | 检查通道健康 |
| `openclaw channels add` | 添加通道账户 |
| `openclaw channels remove` | 移除通道账户 |
| `openclaw channels login` | 交互式登录 |
| `openclaw channels logout` | 登出 |

### 5. 节点管理

| 命令 | 功能 |
|------|------|
| `openclaw nodes list` | 列出配对节点 |
| `openclaw nodes status` | 节点状态 |
| `openclaw nodes approve/reject` | 批准/拒绝配对请求 |
| `openclaw nodes camera snap` | 拍照 |
| `openclaw nodes canvas snapshot` | Canvas 截图 |
| `openclaw nodes screen record` | 录屏 |
| `openclaw nodes location get` | 获取位置 |

### 6. 浏览器控制

| 命令 | 功能 |
|------|------|
| `openclaw browser start/stop` | 启动/停止浏览器 |
| `openclaw browser open <url>` | 打开页面 |
| `openclaw browser screenshot` | 截图 |
| `openclaw browser snapshot` | 页面快照 |
| `openclaw browser click/type/press` | 交互操作 |

### 7. 消息发送

| 命令 | 功能 |
|------|------|
| `openclaw message send` | 发送消息 |
| `openclaw message poll` | 创建投票 |
| `openclaw message react` | 添加反应 |
| `openclaw message thread` | 线程操作 |

### 8. 模型管理

| 命令 | 功能 |
|------|------|
| `openclaw models list` | 列出模型 |
| `openclaw models status` | 模型状态 |
| `openclaw models set <model>` | 设置默认模型 |
| `openclaw models scan` | 扫描可用模型 |
| `openclaw models auth login` | 登录提供商 |

### 9. 记忆和搜索

| 命令 | 功能 |
|------|------|
| `openclaw memory status` | 记忆索引状态 |
| `openclaw memory search` | 语义搜索 |
| `openclaw memory index` | 重新索引 |
| `openclaw memory promote` | 提升短期记忆 |

### 10. 定时任务

| 命令 | 功能 |
|------|------|
| `openclaw cron list` | 列出定时任务 |
| `openclaw cron add` | 添加任务 |
| `openclaw cron edit/rm` | 编辑/删除 |
| `openclaw cron enable/disable` | 启用/禁用 |

### 11. 插件管理

| 命令 | 功能 |
|------|------|
| `openclaw plugins list` | 列出插件 |
| `openclaw plugins install` | 安装插件 |
| `openclaw plugins enable/disable` | 启用/禁用 |
| `openclaw skills install` | 安装 Skill |

### 12. 会话和状态

| 命令 | 功能 |
|------|------|
| `openclaw status` | 会话健康状态 |
| `openclaw health` | Gateway 健康 |
| `openclaw sessions list` | 列会话 |
| `openclaw sessions cleanup` | 清理过期会话 |

### 13. 维护和备份

| 命令 | 功能 |
|------|------|
| `openclaw backup create` | 创建备份 |
| `openclaw backup verify` | 验证备份 |
| `openclaw security audit` | 安全审计 |
| `openclaw logs` | 查看日志 |
| `openclaw update` | 更新 CLI |
| `openclaw reset` | 重置配置 |
| `openclaw uninstall` | 卸载 |

## 颜色主题

OpenClaw 使用"龙虾调色板":

| 颜色 | 用途 |
|------|------|
| `#FF5A2D` (accent) | 标题、标签、主高亮 |
| `#FF7A3D` (accentBright) | 命令名、强调 |
| `#2FBF71` (success) | 成功状态 |
| `#FFB020` (warn) | 警告、注意 |
| `#E23D2D` (error) | 错误、失败 |

## 输出格式

- 默认: 人类可读（TTY 中彩色）
- `--json`: 机器可读 JSON
- `--plain`: 禁用样式
- `--no-color`: 禁用 ANSI

## 相关实体
- [[OpenClaw]]

## 相关概念
- [[Gateway_Architecture]]
- [[Multi_Agent_Routing]]
- [[Agent_Runtime]]
