# 澄清记录 — REQ-00001

> 标题同步:2026-06-03 20:20,目录已重命名为 `REQ-00001`(详见 v2 变更记录);第 1 轮问答内容**保留原字面值**作为审计线索。

## 2026-06-03 20:08(第 1 轮)

### Q1:本需求使用的需求编码是什么?
- **选项**:
  - A. `REQ-2026-0001`(本版本首个需求,使用 REQ-YYYY-NNNN 标准格式)
  - B. `REQ-MARKETPLACE-RENAME`(语义化编码)
  - C. `MARKETPLACE-RENAME-001`(主题前缀编码)
- **用户回答**:**A**(REQ-2026-0001)
- **影响**:工作目录定为 `./assistants/V0.0.1/require/REQ-2026-0001/`;后续 FR 编号正式使用 `REQ-2026-0001` 引用

### Q2:"修改 marketplace 名称" 指的是哪些字段?
- **选项**:
  - A. 仅 `.claude-plugin/marketplace.json` 根 `name`(最小化)
  - B. 根 `name` + `owner.name`
  - C. marketplace.json 内 4 个 name 全部(根/owner/plugins[].name/plugins[].author.name)
  - D. marketplace + plugin + 目录全部统一改名(含 `plugins/code-skills/` 目录重命名)
- **用户回答**:**A**(仅 marketplace.json 的根 name,最小化)
- **影响**:
  - **改**:`.claude-plugin/marketplace.json` 根 `name`:`"code-skills"` → `"code-skills-marketplace"`
  - **不改**:
    - `.claude-plugin/marketplace.json` 的 `owner.name`、`plugins[0].name`、`plugins[0].author.name`
    - `plugins/code-skills/.claude-plugin/plugin.json` 的所有字段
    - 仓库目录结构(`plugins/code-skills/` 保持)
    - git 远端仓库名(`wm123450405/code-skills.git` 保持)
  - **派生影响**(规则强制,无需另询):README.md / README.en.md 中所有 `@code-skills` 与"marketplace name 是 `code-skills`"的引用必须同步更新为 `@code-skills-marketplace`(`doc-conventions.md §规则 2` + `§规则 1`)
- **影响 RESULT.md 章节**:FR-1 ~ FR-7、AC-1 ~ AC-6、NFR(兼容性)

---

## 后续轮次预留
> 下列问题已识别,本轮未问;待 RESULT.md §12 "待澄清/未决项" 列出后,由用户决定何时回答
- Q-3:是否需要同步更新 marketplace.json 的 `description`?(本次回答 A 暗示"仅根 name",description 默认不改)
- Q-4:是否需要在 README.md / README.en.md 中追加"老用户迁移指引"小节,说明从 `@code-skills` 改为 `@code-skills-marketplace` 的步骤?
- Q-5:是否需要新增 CHANGELOG.md 或在 marketplace.json 升 minor 版本号(当前 `1.0.0` → `1.1.0`)以标识此 breaking change?
