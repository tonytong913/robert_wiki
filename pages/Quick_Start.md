# 快速开始

## 概述

5 分钟内安装 OpenClaw，运行引导，并与 AI 助手聊天。

## 需要

- **Node.js** - Node 24 推荐（也支持 Node 22.14+）
- **API 密钥** - 来自模型提供商（Anthropic、OpenAI、Google 等）

检查 Node 版本：
```bash
node --version
```

## 快速设置

### 1. 安装 OpenClaw

**macOS / Linux：**
```bash
curl -fsSL https://openclaw.ai/install.sh | bash
```

**Windows (PowerShell)：**
```powershell
iwr -useb https://openclaw.ai/install.ps1 | iex
```

### 2. 运行引导

```bash
openclaw onboard --install-daemon
```

向导会引导你选择模型提供商、设置 API 密钥、配置 Gateway。约 2 分钟。

### 3. 验证 Gateway 运行

```bash
openclaw gateway status
```

应看到 Gateway 在端口 18789 监听。

### 4. 打开仪表板

```bash
openclaw dashboard
```

在浏览器中打开控制界面。如果能加载，一切正常。

### 5. 开始聊天

**选项 A：WebChat**
- 在仪表板中点击 **WebChat** 标签
- 发送消息

**选项 B：Telegram（最快）**
- 按照 [Telegram 设置](/channels/telegram) 创建 bot
- 发送消息给 bot

**选项 C：WhatsApp**
- 运行 `openclaw channels login --channel whatsapp`
- 扫描二维码
- 发送消息

## 下一步

- 配置更多通道：[Channels](/channels)
- 自定义 Agent：[Agent workspace](/concepts/agent-workspace)
- 设置定时任务：[Cron jobs](/automation/cron-jobs)

## 相关实体
- [[OpenClaw]]

## 相关概念
- [[Gateway_Configuration]]
- [[Chat_Channels]]
