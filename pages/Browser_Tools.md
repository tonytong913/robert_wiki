# 浏览器工具

## 概述

OpenClaw 可以运行一个**专用的 Chrome/Brave/Edge/Chromium 配置文件**，由 Agent 控制。它与个人浏览器隔离，通过 Gateway 内的本地控制服务管理（仅回环）。

## 特点

- 单独的 **openclaw** 浏览器配置文件（默认橙色主题）
- 确定性标签控制（列出/打开/聚焦/关闭）
- Agent 操作（点击/输入/拖动/选择）、快照、截图、PDF
- 可选多配置文件支持（`openclaw`、`work`、`remote` 等）

## 快速开始

```bash
openclaw browser --browser-profile openclaw status
openclaw browser --browser-profile openclaw start
openclaw browser --browser-profile openclaw open https://example.com
openclaw browser --browser-profile openclaw snapshot
```

## 插件控制

默认 `browser` 工具是捆绑插件，默认启用：

```json5
{
  plugins: {
    entries: {
      browser: {
        enabled: false,  // 禁用浏览器
      },
    },
  },
}
```

## CLI 命令

### 管理
- `browser status` - 状态
- `browser start/stop` - 启动/停止
- `browser tabs` - 列出标签
- `browser profiles` - 列出配置文件

### 导航
- `browser open <url>` - 打开页面
- `browser navigate <url>` - 导航
- `browser focus <targetId>` - 聚焦标签
- `browser close [targetId]` - 关闭标签

### 检查
- `browser screenshot` - 截图
- `browser snapshot` - 页面快照
- `browser pdf` - 生成 PDF

### 交互
- `browser click <ref>` - 点击
- `browser type <ref> <text>` - 输入文本
- `browser press <key>` - 按键
- `browser hover <ref>` - 悬停
- `browser drag <startRef> <endRef>` - 拖动
- `browser select <ref> <values...>` - 选择
- `browser fill` - 填充表单
- `browser upload` - 上传文件

## 相关实体
- [[OpenClaw]]

## 相关概念
- [[Tool_System]]
