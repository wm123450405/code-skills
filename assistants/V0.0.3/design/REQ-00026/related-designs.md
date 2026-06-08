# 关联概要设计 — REQ-00026

更新时间:2026-06-08 12:30
版本:V0.0.3

## 1. 强关联设计(模块交集)
**无。**

本需求为"纯文案扫除",不涉及任何模块的接口/数据结构/依赖变化。所有旧概要设计虽在 module-breakdown 中使用 `plugins/code-skills/skills/...` 路径作为模块定位,但都是"项目级硬约束路径字面",与本需求"通用化"主题**不冲突**(本需求仅改 SKILL.md 的描述性文字,不改 module-breakdown 等"不变量"段)。

## 2. 弱关联设计(同主题但范围不同)
| 旧设计 | 关联点 | 处理 |
| --- | --- | --- |
| REQ-00020 RESULT.md §模块拆分 | 同列 3 个 SKILL.md(`code-design` / `code-plan` / `code-it`),字面定位使用 `plugins/code-skills/skills/...` | **不改**(属"不变量段",本需求范围外) |
| REQ-00022 RESULT.md §模块拆分 | 同列 11 类引用方(`code-review` + 10 个其他 SKILL.md + marketplace.json + plugin.json + 4 README + 6 templates),字面定位 | **不改** |
| REQ-00024 RESULT.md §模块拆分 | 同列 1 个 SKILL.md(`code-auto`) | **不改** |
| REQ-00025 RESULT.md §模块拆分 | 同列 8 个 SKILL.md | **不改** |

## 3. 设计阶段观察
- 旧设计在 module-breakdown 中使用 `plugins/code-skills/...` 作模块定位,均属"定位性字面"而非"项目专属描述"
- 本需求在 SKILL.md 描述段中把这些字面替换为 `<本仓库>`,但**不改**旧设计 module-breakdown(它们是设计档案,改之破坏可追溯)
- 设计阶段**不**触发 `code-merge`(未在本需求 FR-1 10 个目标中)

## 4. 来源
- 扫描:`./assistants/V0.0.3/design/*/RESULT.md` + `module-breakdown.md` + `related-designs.md`
- 旧设计档案共 6 份,均**不**与本需求强关联
