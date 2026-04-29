# Skills

## 概述

OpenClaw 使用 **[AgentSkills](https://agentskills.io)** 兼容的 skill 文件夹来教 Agent 如何使用工具。每个 skill 是包含 `SKILL.md` 的目录，带有 YAML frontmatter 和指令。

## 加载位置和优先级

OpenClaw 从这些来源加载 skills（优先级从高到低）：

1. **工作空间 skills**: `<workspace>/skills`
2. **项目 Agent skills**: `<workspace>/.agents/skills`
3. **个人 Agent skills**: `~/.agents/skills`
4. **托管/本地 skills**: `~/.openclaw/skills`
5. **捆绑 skills**: 随安装提供
6. **额外 skill 文件夹**: `skills.load.extraDirs`

## 冲突解决

如果 skill 名称冲突，优先级：

`<workspace>/skills` → `<workspace>/.agents/skills` → `~/.agents/skills` → `~/.openclaw/skills` → 捆绑 → `extraDirs`

## 每 Agent vs 共享 Skills

- **每 Agent skills**: `<workspace>/skills` - 仅该 Agent 可见
- **项目 skills**: `<workspace>/.agents/skills` - 该工作空间优先
- **个人 skills**: `~/.agents/skills` - 跨工作空间
- **共享 skills**: `~/.openclaw/skills` - 所有 Agent 可见

## Agent Skill 白名单

```json5
{
  agents: {
    defaults: {
      skills: ["github", "weather"],
    },
    list: [
      { id: "writer" }, // 继承 github, weather
      { id: "docs", skills: ["docs-search"] }, // 替换默认值
      { id: "locked-down", skills: [] }, // 无 skills
    ],
  },
}
```

规则：
- 省略 `agents.defaults.skills` - 默认无限制
- 省略 `agents.list[].skills` - 继承默认值
- 设置 `agents.list[].skills: []` - 无 skills
- 非空 `agents.list[].skills` - 该 Agent 的最终集合

## Skill 结构

```
skill-name/
├── SKILL.md          # 主要文档
├── references/       # 参考资料
└── scripts/          # 辅助脚本
```

## 相关实体
- [[OpenClaw]]

## 相关概念
- [[工具系统]]
