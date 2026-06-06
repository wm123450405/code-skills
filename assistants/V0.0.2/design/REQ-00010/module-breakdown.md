# 模块拆分 — REQ-00010

更新时间:2026-06-06 12:00
版本:V0.0.2
需求编码:REQ-00010

## 新增模块清单
**无**(本需求不新增技能、不新增模块)

## 复用既有模块清单
| 模块/路径 | 复用方式 | 依据 |
| --- | --- | --- |
| `plugins/code-skills/skills/code-it/SKILL.md` §"工具使用约定" 段后插入位置 | 作为"步骤 0a 守卫"小节的**插入锚点** | 沿用 REQ-00013 追加模式 |
| `plugins/code-skills/skills/code-it/SKILL.md` §"标题解析" 工具函数 `parsePlanTaskTitle()` | 复用解析 PLAN.md 任务标题 | REQ-00013 已沉淀 |
| `plugins/code-skills/skills/code-it/SKILL.md` §"标题解析" 工具函数 `truncateTitle()` / `formatTaskTitle()` | 复用中止报告中的标题格式化 | REQ-00013 已沉淀 |
| `code-dashboard` NFR-3 任务编码双格式正则 | 任务编码解析 | `encoding-conventions §规则 3` 沿用 |

## 修改既有模块清单
| 模块/路径 | 状态 | 修改内容 | 涉及行范围(粗略) | 关键决策 | 规范依据 |
| --- | --- | --- | --- | --- | --- |
| `plugins/code-skills/skills/code-it/SKILL.md` | **修改**(追加) | 在"标题解析(REQ-00013 新增)"段后追加"步骤 0a — 前置任务守卫(REQ-00010 新增)"小节(约 80-120 行) | 锚点 = "## 标题解析" 段后 + "## 工作流程" 段前 | **不**重写既有章节;**不**修改 frontmatter(L1-3);**不**改步骤 0 ~ 16 | `skill-conventions §规则 1` + NFR-7 + FR-3 |

## 不修改的模块清单(本设计强约束)
| 模块/路径 | 不修改理由 |
| --- | --- |
| `plugins/code-skills/.claude-plugin/plugin.json` | FR-5.AC-5.1 |
| `.claude-plugin/marketplace.json` | FR-5.AC-5.1 |
| `plugins/code-skills/skills/code-require/SKILL.md` | FR-4.AC-4.1 |
| `plugins/code-skills/skills/code-design/SKILL.md` | FR-4.AC-4.1 |
| `plugins/code-skills/skills/code-plan/SKILL.md` | FR-4.AC-4.1 |
| `plugins/code-skills/skills/code-version/SKILL.md` | FR-4.AC-4.1 |
| `plugins/code-skills/skills/code-unit/SKILL.md` | FR-4.AC-4.1 |
| `plugins/code-skills/skills/code-review/SKILL.md` | FR-4.AC-4.1 |
| `plugins/code-skills/skills/code-fix/SKILL.md` | FR-4.AC-4.1 |
| `plugins/code-skills/skills/code-dashboard/SKILL.md` | FR-4.AC-4.1 |
| `plugins/code-skills/skills/code-publish/SKILL.md` | FR-4.AC-4.1 |
| `plugins/code-skills/skills/code-auto/SKILL.md` | FR-4.AC-4.1 |
| `plugins/code-skills/skills/code-rule/SKILL.md` | FR-4.AC-4.1 |
| `plugins/code-skills/skills/code-init/SKILL.md` | FR-4.AC-4.1 |
| `plugins/code-skills/skills/code-version/templates/version-RESULT.md` | FR-5.AC-5.3(零字段变更) |
| `plugins/code-skills/CLAUDE.md` | 同上 |
| `./assistants/rules/dashboard-conventions.md` | FR-5.AC-5.4(Q-1 锁定 — 零字段变更) |
| `./assistants/rules/encoding-conventions.md` | (本需求不涉及编码格式变更) |
| `./assistants/rules/skill-conventions.md` | (本需求不涉及技能编写规范变更) |

## 模块拆分自检

对照 `module-conventions.md`(如存在)逐条检查:
- ✅ 命名一致性:`code-it` 技能目录名与 `name` 一致(既有)
- ✅ 目录位置:技能入口在 `plugins/code-skills/skills/code-it/SKILL.md`(既有)
- ✅ 依赖方向:本需求**仅**修改 `code-it` 自身,无新依赖
- ✅ 无禁止模式:不引入"前置任务"字段、不改模板、不改看板
