# Telegram 通道

## 概述

通过 grammY 使用 Telegram Bot API。支持 bot DM 和群组。

## 快速设置

### 1. 在 BotFather 创建 bot token

打开 Telegram，与 **@BotFather** 聊天：
- 运行 `/newbot`
- 按照提示操作
- 保存 token

### 2. 配置 token 和 DM 策略

```json5
{
  channels: {
    telegram: {
      enabled: true,
      botToken: "123:abc",
      dmPolicy: "pairing",
      groups: { "*": { requireMention: true } },
    },
  },
}
```

环境变量回退: `TELEGRAM_BOT_TOKEN`

### 3. 启动 gateway 并批准第一个 DM

```bash
openclaw gateway
openclaw pairing list telegram
openclaw pairing approve telegram <CODE>
```

配对码 1 小时后过期。

### 4. 添加 bot 到群组

添加 bot 到群组，设置 `channels.telegram.groups` 和 `groupPolicy`。

## Telegram 设置

### 隐私模式和群组可见性

Telegram bots 默认为**隐私模式**，限制接收的群组消息。

如果 bot 需要看到所有群组消息：
- 通过 `/setprivacy` 禁用隐私模式，或
- 将 bot 设为群组管理员

切换隐私模式后，在每个群组移除并重新添加 bot。

### 群组权限

管理员状态在 Telegram 群组设置中控制。管理员 bots 接收所有群组消息。

### BotFather 切换

- `/setjoingroups` - 允许/拒绝群组添加
- `/setprivacy` - 群组可见性行为

## 特性

| 特性 | 支持 |
|------|------|
| 文本消息 | ✅ |
| 图片 | ✅ |
| 音频/语音 | ✅ |
| 视频 | ✅ |
| 文档 | ✅ |
| 反应 | ✅ |
| 线程 | ✅ |
| 提及激活 | ✅ |

## 相关实体
- [[OpenClaw]]

## 相关概念
- [[聊天通道]]
