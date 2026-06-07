# 关联需求 — REQ-00022
更新时间:2026-06-06 18:00
版本:V0.0.3

## REQ-00007(V0.0.2):`code-auto` 自动开发技能
- **关联点**:`code-auto` SKILL.md 调 `code-review REQ-NNNNN`(步骤 5 / 步骤 6 派生循环)
- **影响**:本需求**同步改** `code-auto/SKILL.md` 中 `code-review` 字面量 → `code-check`;`code-auto` 的子技能调用表 / 屏显契约 / 状态机图全部需改
- **来源**:扫描 `plugins/code-skills/skills/code-auto/SKILL.md` L186/L189/L528 等

## REQ-00017(V0.0.2):`code-plan` 不再为"更新看板"拆派生任务
- **关联点**:V0.0.3/RESULT.md 看板的"评审发现汇总" / "派生任务记录" 区段由 `code-review` 写入
- **影响**:本需求**同步改** V0.0.3/RESULT.md L98/122/136/166/217/218 中"code-review"字面量 → `code-check`
- **来源**:扫描 `assistants/V0.0.3/RESULT.md`

## REQ-00019(V0.0.2):`code-plan` BUG 模式同构
- **关联点**:BUG 路径评审走 `code-review` 流程
- **影响**:本需求**同步改** V0.0.2 文档中"code-review"字面量(但 V0.0.2 历史**不**追溯替换,仅在 V0.0.3 当前规则下)
- **来源**:扫描 `assistants/V0.0.2/require/REQ-00019/RESULT.md`

## REQ-00021(V0.0.3):优化 3 技能 --result / --plan 模板参数
- **关联点**:本需求与 REQ-00021 同样为 SKILL.md 改造类需求
- **影响**:**0 触发** `code-require` / `code-design` / `code-plan` 3 技能 SKILL.md 的"## 命令行参数解析"或"## 模板填充步骤"小节;0 冲突
- **来源**:扫描 `assistants/V0.0.3/design/REQ-00021/`

## REQ-00020(V0.0.3):架构设计目标重新归位 + 3 新维度
- **关联点**:本需求不涉及步骤 0b 设计目标维度
- **影响**:**0 冲突**
- **来源**:扫描 `assistants/V0.0.3/design/REQ-00020/`

## 跨需求影响(本需求**不**触发)

- 本需求**不**触发任何 `code-plan` 派生任务(沿用 REQ-00017)
- 本需求**不**触发任何 `code-fix` 缺陷登记(本需求是改名,不是 bug)
- 本需求**不**触发 `dashboard-conventions §规则 1` 三同步(看板字段 0 新增 / 0 删除 / 0 改枚举,仅"code-review"字面量改名,字面量不在字段约定内)

## 关键引用方(本需求必须同步改)

| 引用方 | 路径 | 字面量出现位置 | 处理策略 |
| --- | --- | --- | --- |
| `code-review/SKILL.md` 自身 | plugins/code-skills/skills/code-review/SKILL.md | 全文(frontmatter + H1 + 全文引用) | **重命名目录** + 改 frontmatter + 改 H1 + 改全文 |
| `code-auto/SKILL.md` | plugins/code-skills/skills/code-auto/SKILL.md | L186 / L189 / L521 / L528 等(子技能调用表 + 屏显) | **同步改** "code-review" → "code-check" |
| `code-design/SKILL.md` | plugins/code-skills/skills/code-design/SKILL.md | (待补) | 同步改 |
| `code-require/SKILL.md` | plugins/code-skills/skills/code-require/SKILL.md | (待补) | 同步改 |
| `code-plan/SKILL.md` | plugins/code-skills/skills/code-plan/SKILL.md | (待补) | 同步改 |
| `code-it/SKILL.md` | plugins/code-skills/skills/code-it/SKILL.md | (待补) | 同步改 |
| `code-unit/SKILL.md` | plugins/code-skills/skills/code-unit/SKILL.md | (待补) | 同步改 |
| `code-fix/SKILL.md` | plugins/code-skills/skills/code-fix/SKILL.md | (待补) | 同步改 |
| `code-publish/SKILL.md` | plugins/code-skills/skills/code-publish/SKILL.md | (待补) | 同步改 |
| `code-dashboard/SKILL.md` | plugins/code-skills/skills/code-dashboard/SKILL.md | (待补) | 同步改 |
| `code-version/SKILL.md` | plugins/code-skills/skills/code-version/SKILL.md | (待补) | 同步改 |
| `code-rule/SKILL.md` | plugins/code-skills/skills/code-rule/SKILL.md | (待补) | 同步改 |
| `.claude-plugin/marketplace.json` | .claude-plugin/marketplace.json | L17 keyword + L25 keyword + L40 skills[] 路径 | **同步改** |
| `plugins/code-skills/.claude-plugin/plugin.json` | plugins/code-skills/.claude-plugin/plugin.json | L17 keyword | **同步改** |
| `plugins/code-skills/README.md` | plugins/code-skills/README.md | (全文) | 同步改 |
| `plugins/code-skills/README.en.md` | plugins/code-skills/README.en.md | (全文) | 同步改 |
| 仓库根 `README.md` | README.md | (全文) | 同步改 |
| 仓库根 `README.en.md` | README.en.md | (全文) | 同步改 |
| `CLAUDE.md` | CLAUDE.md | (全文) | 同步改 |
| `assistants/rules/migration-mapping.md` | assistants/rules/migration-mapping.md | L84 / L156 / L192 | 同步改(规范文档) |
| `assistants/rules/module-conventions.md` | assistants/rules/module-conventions.md | L41 / L53 | 同步改(规范文档) |
| `assistants/rules/encoding-conventions.md` | assistants/rules/encoding-conventions.md | (待补) | 同步改(规范文档) |
| `plugins/code-skills/skills/code-version/templates/version-RESULT.md` 等 6 个模板 | plugins/code-skills/skills/*/templates/*.md | (待补) | 同步改 |
| `assistants/V0.0.3/RESULT.md`(当前激活看板) | assistants/V0.0.3/RESULT.md | L98 / L122 / L136 / L166 / L217 / L218 | 同步改(规范引用) |
| `assistants/V0.0.2/RESULT.md` | assistants/V0.0.2/RESULT.md | (待补) | **不**追溯替换(沿用 `migration-mapping §规则 5`) |
| V0.0.2/V0.0.3 历史 review 产物 | assistants/<version>/review/... | (全文) | **不**追溯替换 |

## 本需求变更源(本会话 1 个)
| 变更源 | 检测方式 | 变化列表 |
| --- | --- | --- |
| 用户原文 1 句 | 口头/文本输入 | "修改 `/code-review` 技能名称为 `/code-check`" |
