# 模块拆分 — REQ-00035

更新时间:2026-06-15 19:05
版本:V0.0.3

## 改写模块清单(本设计 7 个改写点)

| 模块名 | 路径 | 状态 | 职责 | 依赖 |
| --- | --- | --- | --- | --- |
| M1-code-require | plugins/code-skills/skills/code-require/SKILL.md | 修改既有 | 需求分析 + 过程文档自适应 | 内部:§6.1 准则 |
| M1-code-design | plugins/code-skills/skills/code-design/SKILL.md | 修改既有 | 概要设计 + 过程文档自适应 | 内部:§6.2 准则 |
| M1-code-plan | plugins/code-skills/skills/code-plan/SKILL.md | 修改既有 | 详细设计 + 过程文档自适应 | 内部:§6.3 准则 |
| M1-code-it | plugins/code-skills/skills/code-it/SKILL.md | 修改既有 | 任务实施 + 任务级过程文档自适应 | 内部:§6.4 准则 |
| M1-code-check | plugins/code-skills/skills/code-check/SKILL.md | 修改既有 | 评审 + 评审级过程文档自适应 + 8.13 维度 | 内部:§6.5 准则 |
| M2-code-auto | plugins/code-skills/skills/code-auto/SKILL.md | 修改既有(微调) | 编排:子技能调用表"备注"列加 1 行 | 子技能 |
| M3-code-dashboard | plugins/code-skills/skills/code-dashboard/SKILL.md | 修改既有(微调) | 看板解析:加 1 条兼容说明 | 无 |
| M4-process-doc-decisions 模板 | plugins/code-skills/skills/<5 技能>/templates/process-doc-decisions.md | 新增 × 5 | 决策记录文件模板 | 5 技能 SKILL.md |

## 自检结果

- 命名:符合 `module-conventions.md`(模块名 = 路径末段)
- 目录位置:符合(SKILL.md 在 `skills/<name>/`,模板在 `skills/<name>/templates/`)
- 依赖方向:无违反(5 主流程技能 → 内部 §6 准则;code-auto → 子技能;code-dashboard → 无外部)
- 禁止模式:无违反

## 沿用模块(本设计不涉及)

- `code-fix` / `code-init` / `code-version` / `code-rule` / `code-publish` / `code-merge` / `code-answer` / `code-unit`(已退场) — 全部沿用,无改写
