# LLM Wiki Agent

基于 Karpathy 的 LLM Wiki 模式构建的个人知识库，融合了个性化 AI Agent 能力。

## 系统特点

### Karpathy LLM Wiki 核心
- **原始资料 (raw/)** — 只读的源文档，你的输入
- **知识页面 (pages/)** — LLM 生成和维护的知识库（扁平结构）
- **三层架构** — 原始资料 → 页面 → Schema(AGENTS.md)

### OpenClaw Agent 标准
- **SOUL.md** — Agent 的核心身份和人格
- **USER.md** — 服务对象信息
- **IDENTITY.md** — 外在身份特征
- **MEMORY.md** — 长期记忆（主会话）
- **memory/** — 每日记忆 + 错误/学习记录
- **HEARTBEAT.md** — 心跳任务清单

## 快速开始

### 1. 添加资料

告诉你的 LLM Agent：
> "我要添加一篇新资料"

然后提供：
- 文件路径或链接
- 主题领域
- 你想关注的角度

### 2. 查询知识

> "Wiki 里关于 [主题] 有什么内容？"

LLM 会搜索相关页面并综合回答。

### 3. 定期整理

> "帮我检查一下 Wiki 的健康状况"

LLM 会检查矛盾、缺失链接、孤立页面等。

## 目录结构

```
wiki/
├── AGENTS.md          # Schema/系统配置
├── SOUL.md            # Agent 人格
├── USER.md            # 用户信息
├── IDENTITY.md        # Agent 身份
├── TOOLS.md           # 工具配置
├── HEARTBEAT.md       # 心跳任务
├── MEMORY.md          # 长期记忆（主会话）
├── README.md          # 本文件
│
├── memory/            # 日志和记忆
│   ├── YYYY-MM-DD.md  # 每日记忆
│   ├── errors.md      # 错误记录
│   ├── learnings.md   # 经验教训
│   └── feature_requests.md
│
├── raw/               # 原始资料（只读）
│   ├── articles/
│   ├── papers/
│   ├── books/
│   └── assets/
│
├── pages/             # 知识页面（LLM 维护，扁平）
│   ├── index.md       # 内容目录
│   ├── log.md         # 操作日志
│   ├── *.md           # 各种知识页面
│   └── sources/       # 源文档摘要
│
└── scripts/           # 辅助脚本
```

## 核心原则

> 维护知识库的繁琐工作不是阅读或思考，而是 **bookkeeping** ——更新交叉引用、保持摘要最新、标记矛盾。
> 
> 人类放弃 wiki 是因为维护负担增长快于价值。
> 
> LLM 不会厌倦、不会忘记更新交叉引用、可以一次修改 15 个文件。

---

*知识是积累的，不是重复的。*
