# 数据结构完整变更 — REQ-00015
更新时间:2026-06-06 09:10
版本:V0.0.2

## 新增实体:**0**
本需求**不新增任何持久化数据实体**。
- 0 数据库表
- 0 配置文件 schema
- 0 内存数据结构(纯 CLI 操作)

## 修改实体:**0**
本需求**不修改任何既有数据实体**。
- 0 既有文件被改 schema
- 0 既有 JSON 字段被改

## 新增文件清单

| 文件路径 | 类型 | 行数预估 | 说明 |
| --- | --- | --- | --- |
| `plugins/code-skills/skills/code-merge/SKILL.md` | Markdown | 600~800 | 新增第 12 个 `code-*` 技能入口(T-001) |

## 修改文件清单

| 文件路径 | 变更类型 | 变更行数 | 说明 |
| --- | --- | --- | --- |
| `.claude-plugin/marketplace.json` | 数组追加 1 项 | +1 | T-002 |
| `plugins/code-skills/README.md` | "主要能力" 段同步追加 1 行 | +1 | T-003 |
| `plugins/code-skills/README.en.md` | "Key Capabilities" 段同步追加 1 行 | +1 | T-003 |
| `assistants/V0.0.2/RESULT.md` | 4 处同步(需求清单 REQ-00015 状态推进 + 详细设计汇总 + 任务清单 4 行 + 里程碑 1 个 + 文档头 + 变更记录) | +~10 | T-004 |
| `assistants/V0.0.2/plan/REQ-00015/{RESULT,PLAN}.md` | 本步骤新增(非代码改动) | +~800 | code-plan 主产出 |
| `assistants/V0.0.2/plan/REQ-00015/{materials-index,design-notes,module-details,interface-specs,data-changes,risk-analysis,rule-compliance,clarifications}.md` | 本步骤新增(过程文档) | +~2000 | code-plan 过程文档 |

## 索引变更
**0** —— 既有"索引:本版本所有文件"区段**不**追加本需求文件,因为本需求的所有文件是过程文件 / 模板文件,**不**是用户可见的源文件。详 §"约束"。

## 迁移脚本
**0** —— 无数据迁移(纯文档仓库)

## 字段约束
- **任务编号**:严格 `^TASK-REQ-00015-\d{5}$`(沿用 `encoding-conventions §规则 1+3`)
- **SKILL.md frontmatter `name`**:严格 `code-merge`(kebab-case)
- **marketplace.json skills[] 项**:严格 `./skills/code-merge`(以 `./` 开头)

## 约束(本需求严守)
- 0 触发 `dashboard-conventions §规则 1` 3 文件同步
- 0 修改既有 11 个 `code-*` SKILL.md
- 0 修改 `./assistants/rules/` 13 份规范
- 0 修改 `plugins/code-skills/.claude-plugin/plugin.json`
- 0 修改 `marketplace.json` 既有字段(仅追加 1 项)
- 0 派生"更新看板"任务(REQ-00017 强约束)
