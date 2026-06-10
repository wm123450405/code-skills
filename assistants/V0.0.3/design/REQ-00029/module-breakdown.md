# 模块拆分 — REQ-00029
更新时间:2026-06-10 11:30
版本:V0.0.3

## 1. 改造模块(单一目标)

| 模块/路径 | 状态 | 职责 | 规范遵循 |
| --- | --- | --- | --- |
| `plugins/code-skills/skills/code-dashboard/SKILL.md` | 修改既有 | code-dashboard 技能的完整规范 + 工作流描述;本次仅修改§输出段 + §工作流程 步骤 4 渲染层 + §输出契约样例 | `skill-conventions.md §规则 1`(frontmatter 字节级保留);`module-conventions.md §规则 1`(技能资源摆放 0 改) |

## 2. 不改模块(显式列出)

| 模块/路径 | 状态 | 不改理由 |
| --- | --- | --- |
| `plugins/code-skills/skills/code-dashboard/SKILL.md §工具使用约定`(L109-121) | 0 改 | NFR-7 工具集不变 |
| `plugins/code-skills/skills/code-dashboard/SKILL.md §附录 A`(L402-420) | 0 改 | INV-2 算法 4 字节级保留 |
| `plugins/code-skills/skills/code-dashboard/SKILL.md §附录 B`(L422-435) | 0 改 | INV-3 算法 5 字节级保留 |
| 其他 10 个 `code-*` 技能 SKILL.md | 0 改 | INV-5 |
| `./assistants/V<版本号>/RESULT.md` | 0 改 | INV-4 |
| `./assistants/rules/` 13 个文件 | 0 改 | INV-6 |
| `plugins/code-skills/CLAUDE.md` | 0 改 | INV-6 |
| `marketplace.json` / `plugin.json` | 0 改 | INV-6 |

## 3. 拆分依据

- **功能点维度**:1 个需求 = 1 个完整功能点 = "code-dashboard 屏显瘦身"(改造 SKILL.md 渲染层,1 个原子任务)
- **可独立验证**:改造后执行 `/code-dashboard`(无参 + REQ-NNNNN 各 1 次),屏显总行数 ≤ 8 / ≤ 15,grep 元描述关键词 0 匹配
- **0.5–2 天可完成**:单 SKILL.md 文档改造,典型 1 小时工作量
- **粒度判断**:不应拆为"§输出段改造" + "§步骤 4 改造"(同 1 个文件、互相依赖、改 1 处需重读全文)— 违反"按文件粒度合并"