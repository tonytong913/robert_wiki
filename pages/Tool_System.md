# 工具系统

## 概述

Agent 除了生成文本外的所有操作都通过**工具**完成。工具是 Agent 读取文件、运行命令、浏览网页、发送消息和与设备交互的方式。

## 三层架构

### 1. Tools - Agent 调用的功能

类型化函数，如 `exec`, `browser`, `web_search`, `message`。

### 2. Skills - 教 Agent 何时和如何使用

`SKILL.md` 文件注入系统提示，提供上下文、约束和使用指南。

### 3. Plugins - 打包一切

包可以注册：通道、模型提供商、工具、skills、语音、实时转录、实时语音、媒体理解、图像生成、视频生成等。

## 内置工具

| 工具 | 功能 | 文档 |
|------|------|------|
| `exec` / `process` | 运行 shell 命令，管理后台进程 | [Exec](/tools/exec) |
| `code_execution` | 沙盒远程 Python 分析 | |
| `browser` | 控制 Chromium 浏览器 | [Browser](/tools/browser) |
| `web_search` / `web_fetch` | 搜索网页，获取页面内容 | [Web](/tools/web) |
| `read` / `write` / `edit` | 文件 I/O | |
| `apply_patch` | 多段文件补丁 | |
| `message` | 跨所有通道发送消息 | [Agent Send](/tools/agent-send) |
| `canvas` | 驱动节点 Canvas | |
| `nodes` | 发现和目标配对设备 | |
| `cron` / `gateway` | 管理定时任务；Gateway 操作 | |
| `image` / `image_generate` | 分析或生成图像 | [Image](/tools/image-generation) |
| `video_generate` | 生成视频 | [Video](/tools/video-generation) |
| `tts` | 一次性文本转语音 | [TTS](/tools/tts) |
| `sessions_*` / `subagents` | 会话管理和子代理编排 | [Sub-agents](/tools/subagents) |
| `session_status` | 轻量级状态读取 | |

## 工具配置

### Allow/Deny 列表

```json5
{
  tools: {
    allow: ["group:fs", "browser", "web_search"],
    deny: ["exec"],
  },
}
```

### 工具配置文件

| 配置 | 包含 |
|------|------|
| `full` | 无限制 |
| `coding` | 文件系统、运行时、网络、会话、记忆、定时任务、媒体 |
| `messaging` | 消息、会话列表/历史/发送/状态 |
| `minimal` | 仅 `session_status` |

### 工具组

| 组 | 工具 |
|----|------|
| `group:runtime` | exec, process, code_execution |
| `group:fs` | read, write, edit, apply_patch |
| `group:sessions` | sessions_list, sessions_history, sessions_send, sessions_spawn, sessions_yield, subagents, session_status |
| `group:memory` | memory_search, memory_get |
| `group:web` | web_search, x_search, web_fetch |
| `group:ui` | browser, canvas |
| `group:automation` | cron, gateway |
| `group:messaging` | message |
| `group:nodes` | nodes |
| `group:agents` | agents_list |
| `group:media` | image, image_generate, video_generate, tts |
| `group:openclaw` | 所有内置 OpenClaw 工具 |

### 按提供商限制

```json5
{
  tools: {
    profile: "coding",
    byProvider: {
      "google-antigravity": { profile: "minimal" },
    },
  },
}
```

## 相关实体
- [[OpenClaw]]

## 相关概念
- [[Agent 运行时]]
- [[多 Agent 路由]]
