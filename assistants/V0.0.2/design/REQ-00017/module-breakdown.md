# 模块拆分 — REQ-00017
更新时间:2026-06-05 16:30
版本:V0.0.2

## 新增模块

无。

## 复用既有模块

| 模块名 | 路径 | 状态 | 职责 | 对外接口 | 依赖 | 关键决策 | 规范条款 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `/code-plan` 步骤 4A | `plugins/code-skills/skills/code-plan/SKILL.md §步骤 4A 拆任务` | 修改 | 拆任务时遵守"实际产出候选集" | — | 既有 | D-1 | `skill-conventions.md §规则 1` |
| `/code-plan` 步骤 9A | `plugins/code-skills/skills/code-plan/SKILL.md §步骤 9A 看板同步` | 修改 | 只把真实任务以"待开发"写入看板 | — | 既有 | D-1 | `dashboard-conventions.md §规则 1` |
| `/code-it` 末尾兜底 | `plugins/code-skills/skills/code-it/SKILL.md §末尾兜底` | 修改 | commit + P-1 推进看板 | — | 既有 | D-2 + D-8 | 沿用 V0.0.2 既有模式 |
| `/code-it` P-1 推进看板 | `plugins/code-skills/skills/code-it/SKILL.md §步骤 P-1 推进看板` | 新增小步 | 解析看板 + 推进本任务"开发状态" | — | 既有看板解析 | D-2 + D-3 + D-4 | `dashboard-conventions.md §规则 1` |
| `/code-dashboard` | `plugins/code-skills/skills/code-dashboard/SKILL.md` | **不**修改 | 看板 3 区段解析 | — | 既有 | D-7 解析锚点复用 | `dashboard-conventions.md §规则 1` |

## 自检:对照 `module-conventions.md` / `directory-conventions.md`

- `module-conventions.md §规则 1`:资源放技能子目录 — 本次不涉及
- `directory-conventions.md`:技能目录结构 — 本次不涉及

## 总结

- 修改:2 个 SKILL.md(`/code-plan` + `/code-it`)
- **不**改:9 个 SKILL.md + 13 个 rules + 1 个 CLAUDE.md + 1 个 version-RESULT.md
- 新增:0
- 删除:0
