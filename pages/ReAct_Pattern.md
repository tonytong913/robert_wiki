---
title: ReAct_Pattern
type: concept
sources:
  - raw/articles/2026-05-04-ReAct-pattern.md
  - https://arxiv.org/abs/2210.03629
  - https://zhuanlan.zhihu.com/p/1991816580384957616
  - https://developer.aliyun.com/article/1527894
  - https://www.promptingguide.ai/zh/techniques/react
  - https://capabl.in/blog/agentic-ai-design-patterns-react-rewoo-codeact-and-beyond
  - https://www.woshipm.com/it/6105809.html
  - https://portkey.ai/blog/react-synergizing-reasoning-and-acting-in-language-models-summary/
  - https://www.thoughtworks.com/radar/techniques/react-prompting
  - https://time.geekbang.org/column/article/707191
related:
  - "[[Agent_Loop]]"
  - "[[Agent_Runtime]]"
  - "[[Skills]]"
  - "[[Tool_System]]"
tags: [ReAct, Agent, 推理, 行动, 思维链, LangChain, 幻觉]
created: 2026-05-04
updated: 2026-05-04
confidence: high
---

# ReAct_Pattern（ReAct 模式：推理 + 行动）

ReAct（Reason + Act，推理 + 行动）是 AI Agent 领域最基石的架构范式。它让 LLM 在 **Thought → Action → Observation** 的闭环中边思考、边执行、边观察，直到获得最终答案。

---

## 一句话定义

**ReAct 模式** = LLM 在"感知→决策→执行→反馈"的智能闭环中自主决策，从"被动应答者"升级为"主动问题解决者"，让 AI 像人类一样边想边做。

---

## 核心原理：四步闭环

```
        ┌──────────────┐
        │   Thought    │ ← 大模型自主推理"该做什么、为什么"
        │   (思考)     │
        └──────┬───────┘
               ↓
        ┌──────────────┐
        │   Action     │ ← 调用外部工具（搜索/数据库/计算器）
        │   (行动)     │
        └──────┬───────┘
               ↓
        ┌──────────────┐
        │ Observation  │ ← 工具返回结果喂回模型
        │   (观察)     │
        └──────┬───────┘
               ↓
        信息足够？──否──→ 回到 Thought
               │
              是
               ↓
        ┌──────────────┐
        │ Final Answer │ ← 停止循环，输出结果
        └──────────────┘
```

---

## 运行示例

**问题**："OpenAI 现任 CEO 几岁了？"

| 步骤 | 类型 | 内容 |
|------|------|------|
| 1 | Thought | 需要先确认现任 CEO 是谁，再查出生日期 |
| 2 | Action | `google_search("OpenAI current CEO")` |
| 3 | Observation | 现任 CEO 是 Sam Altman |
| 4 | Thought | 知道了是 Sam Altman，现在查他的出生日期 |
| 5 | Action | `google_search("Sam Altman birth date")` |
| 6 | Observation | 出生于 1985 年 4 月 22 日 |
| 7 | Thought | 2026 - 1985 = 41 岁，已得到答案 |
| 8 | **Final** | OpenAI 现任 CEO 是 Sam Altman，他目前 41 岁 |

---

## 对比：ReAct vs 传统模式

| 维度 | 纯思维链（CoT） | 纯工具调用 | **ReAct** |
|------|---------------|-----------|----------|
| 推理能力 | ✅ 强 | ❌ 弱 | ✅ 强 |
| 获取外部知识 | ❌ 不能 | ✅ 能 | ✅ 能 |
| 幻觉程度 | 高 | 低 | **极低** |
| 错误纠正 | ❌ 不能 | ❌ 不能 | ✅ 能（下一轮 Thought 分析） |
| 可解释性 | 中 | 低 | **高**（每步思维可见） |
| 动态调整计划 | ❌ 不能 | ❌ 不能 | ✅ 能 |

---

## 核心优势

### 1. 极大地减少幻觉
凡事讲证据——依赖外部工具检索真实世界信息，不凭空编造。

### 2. 支持错误纠正
某次 Action 报错 → 下一个 Thought 分析原因 → 更换参数重新尝试。

### 3. 极高的可解释性
人类可清晰看到 AI 每一步的思维轨迹和工具调用过程，而非面对黑盒输出。

---

## 局限性

| 挑战 | 说明 |
|------|------|
| **Token 消耗巨大且不可控** | LLM 对任务的拆解和循环次数不可控，复杂任务可能 Token 过量消耗 |
| **LLM 输出不稳定** | 大模型通病——输出内容、复杂问题分析解决均存在波动 |
| **响应时间不可控** | 无法确定需要多少步骤、多少次 LLM 调用，秒级同步接口不合适，需异步方式 |
| **容易死循环** | 工具返回异常信息时，可能反复尝试同一错误 Action |

---

## 行业应用

**几乎所有主流 Agent 框架都以 ReAct 为默认策略：**

| 框架 | ReAct 实现 |
|------|-----------|
| **LangChain** | 内置 ReActAgent 类，提供模型+工具即可自动驱动 |
| **LlamaIndex** | 内置 ReAct Agent，自动拼接 Prompt 驱动循环 |
| **Claude Code** | 自主读写代码、报错自动修复 = ReAct 在软件工程的具象化 |
| **GitHub Copilot** | 同上，Agent 循环即 ReAct 思想 |
| **OpenClaw** | [[Agent_Loop|Agent 循环]] 本质即 ReAct 模式 |

---

## ReAct 与 OpenClaw Agent 循环的关系

[[Agent_Loop|OpenClaw 的 Agent 循环]] 正是 ReAct 模式的工程实现：

| ReAct 概念 | OpenClaw 对应 |
|-----------|--------------|
| Thought | LLM 推理（系统提示+工具选择） |
| Action | 工具调用（exec、browser、web_search 等） |
| Observation | 工具返回结果注入上下文 |
| Final Answer | Assistant 最终回复 |
| 循环控制 | 队列+超时+会话序列化 |

---

## 关键洞察

1. **ReAct = 基石** — 几乎所有现代 Agent 框架都建立在此范式上
2. **Thought 是关键** — 不是机械执行，而是自主推理"为什么这么做"
3. **工具是手脚** — ReAct 让 LLM 从"只会说"变成"会做"
4. **闭环是灵魂** — 观察→反馈→调整，持续的自主纠错
5. **代价是成本** — Token 消耗和高延迟是工程落地的主要挑战

---

## 相关页面

- [[Agent_Loop|Agent 循环]] — OpenClaw 中 ReAct 模式的工程实现
- [[Agent_Runtime|Agent 运行时]] — Agent 运行的完整环境
- [[Tool_System|工具系统]] — ReAct 中 Action 环节的工具支撑
- [[Skills|Skills 系统]] — 封装好的可复用工具能力
- [[Subagents|子 Agent]] — 多 Agent 协作中的 ReAct 嵌套

## 来源

- [ReAct 模式：AI Agent 的推理+行动架构](../raw/articles/2026-05-04-ReAct-pattern.md)
- 论文：ReAct: Synergizing Reasoning and Acting in Language Models (Google & Princeton, 2022) — https://arxiv.org/abs/2210.03629
- 知乎：ReAct 模式详解 — https://zhuanlan.zhihu.com/p/1991816580384957616
- 阿里云开发者：ReAct 框架定义 — https://developer.aliyun.com/article/1527894
- Prompt Engineering Guide：ReAct 技术 — https://www.promptingguide.ai/zh/techniques/react
- Capabl：Agentic AI Design Patterns — https://capabl.in/blog/agentic-ai-design-patterns-react-rewoo-codeact-and-beyond
- 人人都是产品经理：ReAct 模式深度解析 — https://www.woshipm.com/it/6105809.html
- APXML：ReAct Framework — https://apxml.com/courses/agentic-llm-memory-architectures/chapter-2-advanced-agent-architectures-reasoning/react-framework-reasoning-acting
- Portkey：ReAct Summary — https://portkey.ai/blog/react-synergizing-reasoning-and-acting-in-language-models-summary/
- ThoughtWorks：ReAct Prompting — https://www.thoughtworks.com/radar/techniques/react-prompting
- 极客时间：AI Agent 专栏 — https://time.geekbang.org/column/article/707191

---

*标签: #ReAct #Agent #推理 #行动 #思维链 #LangChain #幻觉 #工具调用*
