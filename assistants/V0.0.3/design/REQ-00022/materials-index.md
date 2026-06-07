# 材料登记 — REQ-00022
更新时间:2026-06-07
版本:V0.0.3

## 项目级规范(本次扫描)
- `skill-conventions.md` §规则 1:FR-1 触发
- `marketplace-protocol.md` §规则 1:FR-2 触发
- `doc-conventions.md` §规则 1:FR-4 触发
- `migration-mapping.md` §规则 5:FR-5 沿用
- `dashboard-conventions.md` §规则 1:INV-7 锁定 0 触发
- `encoding-conventions.md` §规则 1/3:INV-8 锁定 0 触发
- `naming-conventions.md`:基本名 `code-check` 用户原文锁定
- `dependency-conventions.md`:0 新增依赖
- `commit-conventions.md`:`chore(<scope>): <subject>` 沿用
- `module-conventions.md`(DEPRECATED) + `directory-conventions.md`:过程文档摆放

## 上游需求
- 来源:`./assistants/V0.0.3/require/REQ-00022/RESULT.md`
- 版本:v1(2026-06-07)
- 提取的 FR / NFR / AC 数量:7 FR / 6 NFR / ~33 AC / 9 INV

## 项目现状(本次扫描)
### 关键文件
- `plugins/code-skills/skills/code-review/SKILL.md`(待重命名为 `code-check/SKILL.md`)
- `.claude-plugin/marketplace.json`(待改 `skills[]` 路径 + `keywords[]` + `description`)
- `plugins/code-skills/.claude-plugin/plugin.json`(待改 `keywords[]` + `description`)
- 10 个其他 SKILL.md 的 `description` 字段(待改)
- 4 个 README(仓库根 / 仓库内,中英)+ 1 CLAUDE.md(待改)
- 13 份项目级规范(待改引用字面量)
- 6 个技能模板(待改引用字面量)
- V0.0.3 当前激活看板(待改 6 处规范引用)

### 不追溯范围
- V0.0.0 / V0.0.1 / V0.0.2 全部历史版本内容
- V0.0.3 历史 review 产物 `review/REQ-NNNN/*`
- `migration-mapping.md` L156"`EXISTING-010` → 代码评审(`code-review`)"行

## 关联需求
详 `related-designs.md`
