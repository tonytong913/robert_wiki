# ReAct 模式：AI Agent 的推理+行动架构

> 来源：用户提供（2026-05-04）
> 论文：ReAct: Synergizing Reasoning and Acting in Language Models（Google & Princeton, 2022）

---

## 概述

ReAct 模式（源自 Reason + Act，即"推理 + 行动"）是当前 AI Agent（智能体）领域最基石、最经典的架构范式。

该模式由 Google 与普林斯顿大学于 2022 年在论文《ReAct: Synergizing Reasoning and Acting in Language Models》中首次提出。它彻底打破了传统大模型"一问一答"的死板模式，让 AI 学会了像人类一样"边思考、边执行、边观察"。

---

## 🧠 1. 核心原理：四步死循环

ReAct 模式的本质，是让大语言模型（LLM）在一个持续的闭环中运行，直到找到最终答案。这个闭环由 4 个核心要素组成：

1. **Thought（思考）**：大模型根据当前问题，自主推理接下来"应该做什么"以及"为什么要这么做"。
2. **Action（行动）**：模型根据"思考"的结果，决定调用哪个外部工具（如搜索引擎、数据库或计算器），并输出指定格式的调用参数。
3. **Observation（观察）**：外部工具执行完毕后，将结果（如网页搜索结果、代码运行报错、数据库查询记录）作为新的上下文喂回给大模型。
4. **Final Answer（最终答案）**：当大模型通过不断的"观察"认为已经拿到了足够的信息，便停止循环，输出最终结果。

---

## 📝 2. 一个典型的 ReAct 运行示例

假设用户向大模型提问："OpenAI 现任 CEO 几岁了？"

传统模型如果知识没有更新，可能会直接胡说八道。而在 ReAct 模式下：

- **Thought**：用户想知道 OpenAI 现任 CEO 的年龄。我需要先确认现任 CEO 是谁，然后查他的出生日期。
- **Action**：google_search("OpenAI current CEO")
- **Observation**：搜索返回结果显示现任 CEO 是 Sam Altman。
- **Thought**：我知道 CEO 是 Sam Altman 了。现在我需要查找他的出生日期。
- **Action**：google_search("Sam Altman birth date")
- **Observation**：搜索返回结果显示他出生于 1985 年 4 月 22 日。
- **Thought**：今天是 2026 年 5 月，他出生于 1985 年 4 月。那么他的年龄是 2026 - 1985 = 41 岁。我已经得到了答案。
- **Final Answer**：OpenAI 现任 CEO 是 Sam Altman，他目前 41 岁。

---

## ⚖️ 3. 为什么要用 ReAct？（对比与优势）

在 ReAct 诞生前，业界主要有两派做法，但各有致命缺陷：

- **只思考，不行动**（如 Chain-of-Thought 思维链）：AI 逻辑很强，但无法获取外部新知识，容易一本正经地胡说八道（幻觉）。
- **只行动，不思考**（如传统的 API 调用）：AI 遇到复杂、需要多步拆解的问题时，无法动态调整计划，容错率极低。

🌟 **ReAct 的核心优势**：

- **极大地减少幻觉**：凡事讲证据，依赖外部工具（如搜索、数据库）检索真实世界的信息。
- **支持错误纠正**：如果某次 Action 调用的 API 报错了，AI 在下一个 Thought 里可以自己分析原因，更换参数重新尝试。
- **极高的可解释性**：人类可以清清楚楚地看到 AI 的每一步思维轨迹和工具调用过程，而不是面对一个黑盒输出。

---

## ⚠️ 4. ReAct 模式的局限性

尽管 ReAct 极为强大，但它在工程落地中也面临不小的挑战：

1. **Token 消耗巨大**：每进行一次"思考-行动-观察"的循环，都需要把之前所有的对话历史和工具返回结果重新塞给模型，导致成本飙升。
2. **耗时较长（高延迟）**：解决一个复杂任务往往需要与大模型进行 3-5 次的反复迭代，对于实时性要求高的场景不太适用。
3. **容易陷入死循环**：如果外部工具返回了不符合预期的信息，大模型可能会陷入反复尝试同一个错误 Action 的死胡同里。

---

## 🛠️ 5. 行业应用

现代几乎所有主流的 AI Agent 框架都将 ReAct 作为最基础的默认策略：

- **LangChain / LlamaIndex**：内置了成熟的 ReActAgent 类，开发者只需提供大模型和工具列表，框架会自动拼接 Prompt 并驱动循环。
- **Claude Code 或 GitHub Copilot Workspace**：其自主读写代码、报错后自动修复的 Agent 循环，正是 ReAct 思想在软件工程领域的具象化实现。

---

## 参考来源

1. Capabl: Agentic AI Design Patterns — https://capabl.in/blog/agentic-ai-design-patterns-react-rewoo-codeact-and-beyond
2. 论文：ReAct: Synergizing Reasoning and Acting in Language Models — https://arxiv.org/abs/2210.03629
3. 人人都是产品经理：ReAct 模式深度解析 — https://www.woshipm.com/it/6105809.html
4. 知乎：ReAct 模式详解 — https://zhuanlan.zhihu.com/p/1991816580384957616
5. 阿里云开发者：ReAct 框架定义 — https://developer.aliyun.com/article/1527894
6. Prompt Engineering Guide：ReAct 技术 — https://www.promptingguide.ai/zh/techniques/react
7. APXML：ReAct Framework — https://apxml.com/courses/agentic-llm-memory-architectures/chapter-2-advanced-agent-architectures-reasoning/react-framework-reasoning-acting
8. Portkey：ReAct Summary — https://portkey.ai/blog/react-synergizing-reasoning-and-acting-in-language-models-summary/
9. ThoughtWorks：ReAct Prompting — https://www.thoughtworks.com/radar/techniques/react-prompting
10. 极客时间：AI Agent 专栏 — https://time.geekbang.org/column/article/707191
