# 澄清记录 — REQ-00022

更新时间:2026-06-07
版本:V0.0.3

## 2026-06-07 — 4 项澄清(用户采纳全部推荐项)

### Q-1 重命名策略
- **问题**:重命名策略选哪个?
- **选项**:A. 硬重命名(目录 + frontmatter + H1) / B. 软重命名(保留 `/code-review` 别名)
- **用户回答**:**A. 硬重命名**(推荐)
- **影响**:FR-1 锁定为"硬重命名"策略;目录 `code-review/` → `code-check/`;用户输入 `/code-review` 报未知技能;严格遵循 `skill-conventions §规则 1`

### Q-2 JSON 同步策略
- **问题**:marketplace.json + plugin.json 同步策略选哪个?
- **选项**:A. 全部同步改 / B. 只改路径,保留关键词
- **用户回答**:**A. 全部同步改**(推荐)
- **影响**:FR-2 锁定为"全部同步改"策略;`.claude-plugin/marketplace.json` + `plugins/code-skills/.claude-plugin/plugin.json` 中 `code-review` 字面量全部 → `code-check`;严格遵循 `marketplace-protocol §规则 1`

### Q-3 docs 同步策略
- **问题**:仓库根 README + 项目级规范 + 技能模板是否同步改?
- **选项**:A. 全部同步改 / B. 只改 SKILL.md + JSON,docs 留 follow-up
- **用户回答**:**A. 全部同步改**(推荐)
- **影响**:FR-3 锁定为"全部同步改"策略;仓库根 2 个 README + 仓库内 2 个 README + CLAUDE.md + 13 份项目级规范 + 6 个技能模板全部同步改;严格遵循 `doc-conventions §规则 1`(中英对仗)

### Q-4 历史产物处理
- **问题**:V0.0.2/V0.0.3 历史 review 产物(`assistants/<version>/review/...` 目录下)如何处理?
- **选项**:A. 历史产物不追溯 / B. 历史产物也同步改
- **用户回答**:**A. 历史产物不追溯**(推荐)
- **影响**:FR-4 锁定为"历史不追溯"策略;V0.0.2/V0.0.3 历史 `review/REQ-NNNN/*` 产物内容中 `code-review` 字面量**不**替换;`review/` 目录**不**重命名(目录名是"产出物类型",不是"技能名");沿用 `migration-mapping §规则 5` 历史快照不变更原则
