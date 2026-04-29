# HEARTBEAT.md - 心跳任务清单

当收到心跳轮询时，检查以下任务：

## 定期任务（每天 2-4 次）

- [ ] **Wiki 健康检查** — 检查是否有孤立页面、缺失链接
- [ ] **记忆整理** — 回顾近期 memory 文件，提取重要信息到 MEMORY.md
- [ ] **索引更新** — 确保 wiki/index.md 是最新的

## 周期性任务（每周）

- [ ] **矛盾检查** — 查找 Wiki 中矛盾或过时的声明
- [ ] **概念补全** — 识别被提及但未创建页面的重要概念

## 追踪状态

在 `memory/heartbeat-state.json` 中记录检查时间：

```json
{
  "lastChecks": {
    "wikiHealth": null,
    "memoryReview": null,
    "indexUpdate": null
  }
}
```

---

如果没有需要处理的任务，回复 `HEARTBEAT_OK`。
