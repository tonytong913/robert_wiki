# 流式传输与分块

## 概述

OpenClaw 有两个独立的流式层：

1. **块流式 (通道)**: 在 Assistant 写入时发射完成的**块**
2. **预览流式 (Telegram/Discord/Slack)**: 生成时更新临时**预览消息**

**注意**: 目前没有真正的令牌增量流式传输到通道消息。预览流式是基于消息的（发送 + 编辑/追加）。

## 块流式（通道消息）

块流式在输出可用时以粗粒度块发送 Assistant 输出。

```
模型输出
  └─ text_delta/events
       ├─ (blockStreamingBreak=text_end)
       │    └─ 分块器在缓冲区增长时发射块
       └─ (blockStreamingBreak=message_end)
            └─ 分块器在 message_end 时刷新
                   └─ 通道发送（块回复）
```

## 控制选项

| 配置 | 说明 |
|------|------|
| `agents.defaults.blockStreamingDefault` | `"on"`/`"off"` (默认 off) |
| `*.blockStreaming` | 每通道覆盖 |
| `agents.defaults.blockStreamingBreak` | `"text_end"` 或 `"message_end"` |
| `agents.defaults.blockStreamingChunk` | `{ minChars, maxChars, breakPreference? }` |
| `agents.defaults.blockStreamingCoalesce` | 合并流式块 |
| `*.textChunkLimit` | 通道硬上限 |
| `*.chunkMode` | `length` (默认) 或 `newline` |

## 边界语义

- `text_end`: 分块器发射时立即流式传输块；在每个 `text_end` 刷新
- `message_end`: 等待 Assistant 消息完成，然后刷新缓冲的输出

## 分块算法

**低边界**: 缓冲区 >= `minChars` 前不发射（除非强制）
**高边界**: 优先在 `maxChars` 前分割；如果强制，在 `maxChars` 分割
**断点偏好**: `paragraph` → `newline` → `sentence` → `whitespace` → 硬断点

**代码围栏**: 永不在围栏内分割；在 `maxChars` 强制时关闭 + 重新打开围栏以保持 Markdown 有效

## 合并（合并流式块）

- 合并等待**空闲间隙** (`idleMs`) 后刷新
- 缓冲区上限为 `maxChars`，超过则刷新
- `minChars` 防止微小片段发送，直到累积足够文本
- 连接符派生自 `blockStreamingChunk.breakPreference`

## 预览流式

Telegram、Discord、Slack 支持预览流式：

- 发送临时预览消息
- 生成时更新/追加
- 完成后替换为最终消息或删除预览

## 相关实体
- [[OpenClaw]]

## 相关概念
- [[Agent_Loop]]
- [[Session_Management]]
