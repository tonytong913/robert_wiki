# 特性列表

## 核心特性

### 通道

- **内置通道**: Discord、Google Chat、iMessage (legacy)、IRC、Signal、Slack、Telegram、WebChat、WhatsApp
- **捆绑插件通道**: BlueBubbles (iMessage)、Feishu、LINE、Matrix、Mattermost、Microsoft Teams、Nextcloud Talk、Nostr、QQ Bot、Synology Chat、Tlon、Twitch、Zalo、Zalo Personal
- **可选单独安装**: Voice Call、WeChat 等第三方插件
- 群聊支持，基于提及的激活
- DM 安全，白名单和配对

### Agent

- 嵌入式 Agent 运行时，工具流式传输
- 多 Agent 路由，每个工作空间或发送者隔离会话
- 会话: 直接聊天折叠到共享 `main`；群组隔离
- 长回复的流式传输和分块

### 认证和提供商

- **35+ 模型提供商**: Anthropic、OpenAI、Google 等
- OAuth 订阅认证 (如 OpenAI Codex)
- 自定义和自托管提供商支持 (vLLM、SGLang、Ollama 等)

### 媒体

- 图片、音频、视频、文档收发
- 共享图像生成和视频生成功能
- 语音笔记转录
- 多提供商文本转语音 (TTS)

### 应用和界面

- WebChat 和浏览器控制界面
- macOS 菜单栏配套应用
- iOS 节点：配对、Canvas、相机、录屏、位置、语音
- Android 节点：配对、聊天、语音、Canvas、相机、设备命令

### 工具和自动化

- 浏览器自动化、exec、沙盒
- **网页搜索**: Brave、DuckDuckGo、Exa、Firecrawl、Gemini、Grok、Kimi、MiniMax Search、Ollama Web Search、Perplexity、SearXNG、Tavily
- 定时任务和心跳调度
- Skills、插件和工作流管道 (Lobster)

## 完整功能矩阵

| 类别 | 功能 |
|------|------|
| 通道 | Discord、Telegram、WhatsApp、Signal、Slack、iMessage、WebChat、Matrix、Nostr、Twitch、Zalo、Feishu、LINE、Mattermost、Teams、QQ Bot 等 |
| 路由 | 多 Agent、隔离会话、按发送者/群组/频道路由 |
| 媒体 | 图片、音频、视频、文档、图像生成、视频生成、TTS |
| 界面 | Web UI、macOS 应用、iOS/Android 节点 |
| 工具 | 浏览器、exec、搜索、定时任务、Skills、插件 |
| 模型 | 35+ 提供商、OAuth、自定义端点 |

## 相关实体
- [[OpenClaw]]
