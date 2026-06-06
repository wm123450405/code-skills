# 规范遵循记录 — REQ-00010

更新时间:2026-06-06 12:00
版本:V0.0.2
需求编码:REQ-00010

## 1. 本次参考的规范文件
- `./assistants/rules/skill-conventions.md` §规则 1(SKILL.md frontmatter 约束)
- `./assistants/rules/dashboard-conventions.md` §规则 1(看板字段三方同步)
- `./assistants/rules/encoding-conventions.md` §规则 1/2/3(编码格式)
- `./assistants/rules/module-conventions.md`(模块结构)
- `./assistants/rules/dependency-conventions.md`(依赖管理)
- `./assistants/rules/coding-style.md`(编码风格)
- `./assistants/rules/naming-conventions.md`(命名约定)

## 2. 规范 vs 现状偏离
**无**(`code-it` 既有实现均符合项目级规范,本需求**追加**而非偏离)

## 3. 规范 vs 需求冲突
**无**(需求 FR-5.AC-5.4 / NFR-3 显式声明**零规范变更**,与规范自身无冲突)

## 4. 用户授权的偏离
**无**

## 5. 关键约束条款遵循清单

| 条款 | 来源 | 遵循方式 |
| --- | --- | --- |
| SKILL.md frontmatter 不变 | `skill-conventions §规则 1` + NFR-7 | ✅ 增量追加在 frontmatter 之后的小节,**不**修改 L1-3 |
| 看板字段扩展需三方同步 | `dashboard-conventions §规则 1` | ✅ NFR-3 零字段变更,**不**触发本规则 |
| 任务编码双格式正则 | `encoding-conventions §规则 3` | ✅ 沿用 `^TASK-(REQ\|BUG)-\d{5}-\d{5}$` / `^(REQ\|BUG)-\d{5}-\d{5}$` |
| 资源摆放 | `module-conventions §规则 1` | ✅ 本设计所有过程文档位于 `design/REQ-00010/` 同级目录 |
| 零新增依赖 | `dependency-conventions` + NFR-1 | ✅ 仅用既有 `Read` / `Grep` 工具 |
| 编码风格 | `coding-style` | ✅ 追加小节贴合既有"§标题解析"格式(REQ-00013 模式) |
| 命名约定 | `naming-conventions` | ✅ 任务编码 / 需求编码格式严格遵循 `encoding-conventions` |

## 6. 关键 INV 清单(从 design-notes 引用,作为规范遵循的"硬约束"沉淀)

| INV | 内容 | 验证方式 |
| --- | --- | --- |
| INV-1 | `code-it/SKILL.md` frontmatter(L1-3)字节级不变 | `code-it` 任务完成后用 `git diff` 比对 frontmatter |
| INV-2 | `code-it/SKILL.md` §"工作流程"步骤 0 ~ 16 内容不变 | 同上 |
| INV-3 | `code-it/SKILL.md` §"缺陷分支"步骤 17 ~ 25 内容不变 | 同上 |
| INV-4 | `code-it/SKILL.md` §"标题解析(REQ-00013 新增)"小节不变 | 同上 |
| INV-5 | `PLAN.md` 模板 / 看板"任务清单"区段 / `dashboard-conventions.md` 不变 | `code-plan` 任务完成后用 `git diff` 比对 |
| INV-6 | `marketplace.json` / `plugin.json` 不变 | `code-it` 任务完成后用 `git diff` 比对 |
| INV-7 | 9 个其他 `code-*` 技能 SKILL.md 不变 | `code-it` 任务完成后用 `git diff --stat skills/` 比对 |
| INV-8 | `code-auto` FR-4.AC-4.3 "按任务总览行序"逻辑不变 | `code-auto` 任务无;**本设计**不强约束 `code-auto` 修改 |
| INV-9 | `code-unit` / `code-publish` / `code-dashboard` / `code-review` 现有逻辑不变 | `code-it` 任务完成后用 `git diff` 比对 |

## 7. 规范变更响应(本设计为首次设计,无历史规范变更需响应)

**无**

## 8. 派生建议(留作 follow-up,本设计不阻塞)

- **建议派生 1**:`code-rule` 沉淀 `task-dependency-conventions.md`(前置任务字段约定) — 沿用需求 Q-8 派生预警
- **建议派生 2**:`code-plan` 升级:拆分任务时支持"前置任务"字段 — 沿用需求 Q-8 派生预警
- **建议派生 3**:`code-auto` 升级:任务级"前置完成"预检 — 沿用需求 Q-8 派生预警
- **建议派生 4**:`code-rule` 沉淀"步骤 0a 守卫"统一模式 — 沿用需求 Q-8 派生预警
