# Learnings

Corrections, insights, and knowledge gaps captured during development.

**Categories**: correction | insight | knowledge_gap | best_practice

---

## 2026-04-10: Wiki 与 Agent 融合 (insight)

将 thq_wiki 的个人化 Agent 元素与 Karpathy LLM Wiki 架构融合：

**保留的 Wiki 核心:**
- raw/ → wiki/ 的编译流程
- index.md + log.md 的索引系统
- Ingest → Query → Lint 的工作流

**融入的 Agent 元素:**
- SOUL.md + USER.md + IDENTITY.md 的人格系统
- memory/ 的每日记忆机制
- .learnings/ 的错误和学习记录
- HEARTBEAT.md 的心跳任务

**关键洞察:**
Wiki 是知识的结构化沉淀，Agent 是持续的交互人格。两者结合既有知识积累，又有连续的人格体验。
