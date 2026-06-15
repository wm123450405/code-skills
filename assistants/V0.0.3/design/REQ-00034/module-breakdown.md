# 模块拆分 — REQ-00034

更新时间:2026-06-15 13:30
版本:V0.0.3

## 模块清单(本设计 0 新增,3 状态汇总)

| 类别 | 数量 | 文件 |
| --- | --- | --- |
| 硬删除 | 1 技能 + 1 模板目录 | `code-unit/SKILL.md` (635) + `code-unit/templates/` 整体 |
| 改造既有(扩展) | 5 SKILL.md | `code-it`(净增 +150~+250)+ `code-plan`(-10~+20)+ `code-auto`(-50~+80)+ `code-check`(-10~+20)+ `code-it/templates/RESULT.md`(+20~+40) |
| 字面改写 | 2 JSON + 4 README + CLAUDE.md + 7 规范 + 11 描述段 | 详见 `materials-index.md` §3.1.3 ~ §3.1.6 |
| 保留(不追溯) | V0.0.2 / V0.0.3 既有历史档案 | `test/<TASK-...>/RESULT.md` + `code/<TASK-...>/test-results.md` + `auto-report.md` |
| **净变化** | **约 -600 ~ -800 行** | (技能合并;删除多于新增) |

## 自检(module-conventions.md 逐条)

- 命名是否符合规范:✅ 资源放 `templates/` 子目录(本需求**删除** `code-unit/templates/`,符合"按需增减")
- 目录位置是否符合规范:✅
- 依赖方向是否违反规范:✅ 本需求 0 新增依赖(NFR-5)
- 是否有被禁止的模式:✅ 0 触发
