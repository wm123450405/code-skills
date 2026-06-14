# 澄清记录 — REQ-00026

## 2026-06-08 11:50
- **问题 1**:本需求"项目专属内容"的波及范围是?
- **选项**:A. 仅 10 个 SKILL.md + 附属文本(推荐) / B. 扩大到旧需求 RESULT.md / C. 扩大到所有项目元信息
- **用户回答**:A(仅 10 个 SKILL.md + 附属文本)
- **影响**:FR-1 锁定为"10 个 SKILL.md 描述性文字 + 必要的附属文本(templates/guidelines/checklists)";**不**波及:
  - 旧需求 `assistants/V0.0.3/require/REQ-*/RESULT.md`(历史档案,字面必须保留以确保可追溯)
  - 仓库根 `README.md` / `README.en.md` / `CLAUDE.md`(项目级介绍文档,不在本需求范围)
  - `.claude-plugin/marketplace.json` / `plugins/code-skills/.claude-plugin/plugin.json`(项目元信息硬约束)

## 2026-06-08 11:50
- **问题 2**:如何区分"需改的描述性内容"与"应保留的约束性内容"?
- **选项**:A. 区分描述性与约束性(推荐) / B. 全部改 / C. 仅改描述性段落
- **用户回答**:A(区分描述性与约束性)
- **影响**:
  - **改**(描述性):10 个 SKILL.md 中的功能描述、上下游衔接、适用场景、工作流步骤、注意事项等文字段落
  - **不改**(约束性):"本需求不修改 marketplace.json / plugin.json"、"git diff plugins/.../SKILL.md"等不变量字面与可执行命令

## 2026-06-08 11:50
- **问题 3**:在 SKILL.md 描述性文字中遇到 `plugins/code-skills/...` 这类路径时,推荐替换成?
- **选项**:A. 换成 `<本仓库>` / B. 直接说"本技能市场清单中" / C. 不替换
- **用户回答**:A(替换为 `<本仓库>`)
- **影响**:
  - SKILL.md 描述性段落中,`plugins/code-skills/skills/code-x/SKILL.md` → `<本仓库>/skills/code-x/SKILL.md` 或 `本仓库中 code-x/SKILL.md`
  - SKILL.md 描述性段落中,`<本仓库>` 整体表达"该仓库的根"
  - 描述性段落中,`plugins/code-skills/.claude-plugin/plugin.json` → `<本仓库>/.claude-plugin/plugin.json`

## 2026-06-08 11:50
- **问题 4**:`./assistants 目录是本项目用来管理开发进度的重要目录,技能中是可以经常使用的` 这句话在本需求中的定位是?
- **选项**:A. 不需修改(推荐) / B. 表述为"项目级进度管理目录(默认 ./assistants/)" / C. 改述为"本项目的进度管理目录"
- **用户回答**:A(不需修改)
- **影响**:
  - `./assistants/` 在 SKILL.md 中**保持原样**,因为:
    1. `./assistants/` 是本项目级别的硬约定,跨版本共享(由 `code-version` 初始化,所有 `code-*` 技能都强依赖)
    2. 它是项目约定而非项目专属内容;本需求关注"强关联本项目"的内容(如仓库名、插件名、市场清单的 plugin 路径),而 `./assistants/` 是 SKILL.md 的**事实契约**
    3. 用户的原话"技能中是可以经常使用的"已明确表态
  - 唯一例外:若某 SKILL.md 描述性段落中以"本项目"指代仓库(而非"项目级目录"),该指代可保留(因为它已是泛用表述)
