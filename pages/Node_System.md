# 节点系统

## 概述

**节点**是配套设备（macOS/iOS/Android/headless），通过 WebSocket 连接到 Gateway，暴露命令表面（如 `canvas.*`、`camera.*`、`device.*`）。

## 特点

- 节点是**外围设备**，不是 gateway
- Telegram/WhatsApp 等消息到达 **gateway**，不是节点
- macOS 也可以以**节点模式**运行

## 配对和状态

**WS 节点使用设备配对**。节点在 `connect` 期间呈现设备身份；Gateway 为 `role: node` 创建设备配对请求。

```bash
openclaw devices list
openclaw devices approve <requestId>
openclaw devices reject <requestId>
openclaw nodes status
openclaw nodes describe --node <idOrNameOrIp>
```

## 远程节点主机

当 Gateway 在一台机器上运行，而你想在另一台机器上执行命令时使用。

**启动节点主机（前台）**：

```bash
openclaw node run --host <gateway-host> --port 18789
```

## 节点命令

### Canvas
- `nodes canvas snapshot` - 截图
- `nodes canvas present` - 显示内容
- `nodes canvas hide` - 隐藏
- `nodes canvas navigate` - 导航 URL
- `nodes canvas eval` - 执行 JS

### 相机
- `nodes camera list` - 列出相机
- `nodes camera snap` - 拍照
- `nodes camera clip` - 录制视频

### 屏幕
- `nodes screen record` - 录屏

### 位置
- `nodes location get` - 获取位置

### 通知
- `nodes notify` - 发送通知

## 相关实体
- [[OpenClaw]]

## 相关概念
- [[Gateway架构]]
