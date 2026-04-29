# Gateway 架构

## 概述

Gateway 是 OpenClaw 的核心组件，作为单一真相源管理所有消息通道、路由和会话。

## 核心组件

### 1. Gateway (守护进程)

- 维护所有通道提供商连接
- 暴露类型化的 WebSocket API
- 验证入站帧（JSON Schema）
- 发射事件: `agent`, `chat`, `presence`, `health`, `heartbeat`, `cron`

### 2. 客户端

- macOS 应用、CLI、Web 管理界面
- 每个客户端一个 WebSocket 连接
- 发送请求: `health`, `status`, `send`, `agent`, `system-presence`
- 订阅事件: `tick`, `agent`, `presence`, `shutdown`

### 3. 节点 (Nodes)

- macOS / iOS / Android / Headless
- 使用 `role: node` 连接同一 WS 服务器
- 提供命令: `canvas.*`, `camera.*`, `screen.record`, `location.get`

### 4. WebChat

- 静态 UI，使用 Gateway WS API
- 远程设置通过 SSH/Tailscale 隧道连接

## Canvas 主机

Gateway HTTP 服务器在默认端口 18789 下提供:
- `/__openclaw__/canvas/` - Agent 可编辑的 HTML/CSS/JS
- `/__openclaw__/a2ui/` - A2UI 主机

## 连接生命周期

```
Client -> Gateway: req:connect
Gateway -> Client: res (ok) [或 res error + close]
Gateway -> Client: event:presence
Gateway -> Client: event:tick
Client -> Gateway: req:agent
Gateway -> Client: res:agent ack {runId, status:"accepted"}
Gateway -> Client: event:agent (streaming)
Gateway -> Client: res:agent final {runId, status, summary}
```

## 协议摘要

- **传输**: WebSocket，文本帧，JSON 载荷
- **首帧**: 必须是 `connect`
- **请求**: `{type:"req", id, method, params}`
- **响应**: `{type:"res", id, ok, payload|error}`
- **事件**: `{type:"event", event, payload, seq?, stateVersion?}`

## 认证

- 共享密钥: `connect.params.auth.token` 或 `password`
- Tailscale Serve: 从请求头获取身份
- 本地回环: 可自动批准
- 所有连接必须签名 `connect.challenge` nonce

## 配对与本地信任

- 所有 WS 客户端包含设备身份
- 新设备 ID 需要配对批准
- Gateway 颁发设备令牌用于后续连接
- 非本地连接需要显式批准

## 远程访问

**推荐**: Tailscale 或 VPN

**替代**: SSH 隧道
```bash
ssh -N -L 18789:127.0.0.1:18789 user@host
```

## 操作命令

```bash
# 启动
openclaw gateway

# 健康检查
openclaw gateway status

# 重启
openclaw gateway restart
```

## 不变量

- 每台主机只有一个 Gateway 控制一个 Baileys 会话
- 握手是强制的；非 JSON 或非 connect 首帧会硬关闭
- 事件不重放；客户端必须在间隙时刷新

## 相关实体
- [[OpenClaw]]
- [[Multi_Agent_Routing]]

## 相关概念
- [[Agent_Runtime]]
- [[Multi_Agent_Routing]]
- [[Session_Management]]
