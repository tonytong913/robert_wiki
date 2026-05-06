# Agent 循环

## 概述

Agent 循环是将消息转化为行动和最终回复的完整运行过程，同时保持会话状态一致。

## 入口点

- Gateway RPC: `agent` 和 `agent.wait`
- CLI: `agent` 命令

## 工作流程

### 1. `agent` RPC

- 验证参数
- 解析会话 (sessionKey/sessionId)
- 持久化会话元数据
- 立即返回 `{ runId, acceptedAt }`

### 2. `agentCommand`

- 解析模型 + thinking/verbose 默认值
- 加载 skills 快照
- 调用 `runEmbeddedPiAgent`
- 如果嵌入式循环未发射生命周期事件，发射**生命周期 end/error**

### 3. `runEmbeddedPiAgent`

- 通过每会话 + 全局队列序列化运行
- 解析模型 + 认证配置
- 订阅 pi 事件并流式传输 assistant/tool 增量
- 强制执行超时 -> 超时则中止运行
- 返回载荷 + 使用元数据

### 4. `subscribeEmbeddedPiSession`

将 pi-agent-core 事件桥接到 OpenClaw `agent` 流：
- 工具事件 => `stream: "tool"`
- Assistant 增量 => `stream: "assistant"`
- 生命周期事件 => `stream: "lifecycle"` (`phase: "start" | "end" | "error"`)

### 5. `agent.wait`

- 等待 `runId` 的**生命周期 end/error**
- 返回 `{ status: ok|error|timeout, startedAt, endedAt, error? }`

## 队列 + 并发

- 按会话键（会话通道）序列化运行
- 可选通过全局通道
- 防止工具/会话竞争，保持会话历史一致
- 消息通道可选择队列模式（collect/steer/followup）

## 会话 + 工作空间准备

- 解析和创建工作空间
- 沙盒运行可能重定向到沙盒工作空间根目录
- 加载 Skills（或从快照重用）并注入到环境和提示
- 解析引导/上下文文件并注入到系统提示报告
- 获取会话写入锁

## 提示组装 + 系统提示

- 从 OpenClaw 基础提示、skills 提示、引导上下文和每运行覆盖构建系统提示
- 强制执行模型特定限制和压缩保留令牌

## 钩子点

### 内部钩子 (Gateway hooks)

- **`agent:bootstrap`**: 在系统提示最终确定前构建引导文件时运行
- **命令钩子**: `/new`, `/reset`, `/stop` 等

### 插件钩子

- `before_model_resolve`: 在模型解析前覆盖提供商/模型
- `before_prompt_build`: 注入 `prependContext`, `systemPrompt` 等
- `before_agent_start`: 在 LLM 调用前运行
- `before_agent_reply`: 在 LLM 调用后、回复前运行
- `agent_end`: 完成后检查最终消息列表
- `before_compaction` / `after_compaction`: 压缩周期
- `before_tool_call` / `after_tool_call`: 拦截工具参数/结果
- `message_received` / `message_sending` / `message_sent`: 消息钩子
- `session_start` / `session_end`: 会话生命周期
- `gateway_start` / `gateway_stop`: Gateway 生命周期

## 相关实体
- [[OpenClaw]]
- [[Multi_Agent_Routing]]
- [[ReAct_Pattern]]

## 相关概念
- [[Agent_Runtime]]
- [[Session_Management]]
