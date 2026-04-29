# 聊天通道

## 概述

OpenClaw 可以连接到你使用的任何聊天应用。每个通道通过 Gateway 连接。所有通道都支持文本；媒体和反应因通道而异。

## 支持的通道

### 内置通道
- **Discord** - Discord Bot API + Gateway；支持服务器、频道和 DM
- **Google Chat** - Google Chat API 应用 via HTTP webhook
- **iMessage (legacy)** - 传统 macOS 集成（已弃用，新设置用 BlueBubbles）
- **IRC** - 经典 IRC 服务器；频道 + DM
- **Signal** - signal-cli；隐私优先
- **Slack** - Bolt SDK；工作区应用
- **Telegram** - Bot API via grammY；支持群组
- **WebChat** - Gateway WebChat UI via WebSocket
- **WhatsApp** - 最受欢迎；使用 Baileys，需要 QR 配对

### 捆绑插件通道
- **BlueBubbles** - iMessage 推荐方案
- **Feishu** - 飞书/Lark bot via WebSocket
- **LINE** - LINE Messaging API bot
- **Matrix** - Matrix 协议
- **Mattermost** - Bot API + WebSocket
- **Microsoft Teams** - Bot Framework；企业支持
- **Nextcloud Talk** - 自托管聊天
- **Nostr** - 去中心化 DM via NIP-04
- **QQ Bot** - QQ Bot API；私聊、群聊、富媒体
- **Synology Chat** - Synology NAS Chat
- **Tlon** - Urbit-based messenger
- **Twitch** - Twitch 聊天 via IRC
- **Zalo** - 越南流行通讯工具
- **Zalo Personal** - Zalo 个人账户

### 可选单独安装
- **Voice Call** - Plivo 或 Twilio 电话
- **WeChat** - 腾讯 iLink Bot 插件

## 快速设置建议

| 通道 | 难度 | 特点 |
|------|------|------|
| Telegram | ⭐ 最简单 | 简单 bot token |
| Discord | ⭐⭐ 简单 | 需要创建应用和 bot |
| WhatsApp | ⭐⭐⭐ 中等 | 需要 QR 配对，更多状态存储 |
| QQ Bot | ⭐⭐ 简单 | 需要 QQ 开放平台注册 |

## 安全

- DM 配对和白名单强制执行
- 参见 [Security](/gateway/security)

## 故障排除

参见 [Channel troubleshooting](/channels/troubleshooting)

## 相关实体
- [[OpenClaw]]

## 相关概念
- [[多Agent路由]]
