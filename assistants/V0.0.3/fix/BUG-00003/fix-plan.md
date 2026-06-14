# fix-plan — BUG-00003(SKILL.md 描述中"绝对路径"在 plugin 安装后断链)

- **缺陷编号**:BUG-00003
- **严重度**:P0
- **当前状态**:调查中 → 修复规划中
- **更新时间**:2026-06-08 14:50
- **版本**:V0.0.3

## 1. 缺陷摘要
- 链接:./RESULT.md
- 标题:SKILL.md 描述中"绝对路径"(`plugins/code-skills/...`)在 plugin 安装后断链
- 严重度:P0(阻断)
- 当前状态:修复规划中

## 2. 根因定位

本仓库作为 plugin 发布,SKILL.md 中的 `plugins/code-skills/...` 字面是"开发视角"的本仓库路径,**不是**"plugin 视角"的相对路径。plugin 安装到用户环境后,`plugins/code-skills/...` 路径不存在,所有引用断裂。

**关键发现**:
- BUG-00002(本会话早些时候)已修了 5 处(描述性段 + 5 处不变量字面补修),波及 `code-it` / `code-unit` / `code-init` / `code-require` / `code-design` / `code-plan` / `code-fix` 共 9 文件 9 处 Edit(commit `82d476c` + `678e602`)
- **本轮 BUG-00003 剩 5 处**:**命令示例段**(用户在阅读 SKILL.md 时可直接 Copy-Paste 执行)中的 `plugins/code-skills/...` 字面,这些是最直接影响用户使用的"实际可执行命令",必须改

## 3. 修复方案

### 3.1 选定方案
**方案 A(选定)**:把 5 处命令示例中的 `plugins/code-skills/...` 字面**统一改为** `<本仓库>` 占位符(与 BUG-00002 完全一致的方案)

### 3.2 候选方案
- **方案 B(否决)**:删除命令示例,只用语言描述——丢失"用户在自家项目中可 Copy-Paste 的具体命令"语义提示
- **方案 C(否决)**:用 `./` 或 `../` 相对路径——用户原话明确"应该和 其他技能一样修改"(指 BUG-00002 的 `<本仓库>` 方案)

### 3.3 选定理由
- 用户原话直接给出修复语义
- 与 BUG-00002 方案完全一致,字面统一
- 与本项目既有"占位符 `<本仓库>`"约定兼容(REQ-00026)

## 4. 涉及文件与变更

### 4.1 改 5 处(命令示例段)
| 文件 | 行 | 改前 | 改后 |
| --- | --- | --- | --- |
| `plugins/code-skills/skills/code-publish/SKILL.md` | L312 | `Read: plugins/code-skills/skills/code-publish/templates/DEPLOY.md` | `Read: <本仓库>/skills/code-publish/templates/DEPLOY.md` |
| `plugins/code-skills/skills/code-publish/SKILL.md` | L325 | `Read: plugins/code-skills/skills/code-publish/templates/UPDATE.md` | `Read: <本仓库>/skills/code-publish/templates/UPDATE.md` |
| `plugins/code-skills/skills/code-publish/SKILL.md` | L361 | `Read: plugins/code-skills/skills/code-publish/templates/qanda-README.md` | `Read: <本仓库>/skills/code-publish/templates/qanda-README.md` |
| `plugins/code-skills/skills/code-publish/SKILL.md` | L556 | `不要追加 \`plugins/code-skills/CLAUDE.md\` "AI 工作约定"小节` | `不要追加 \`<本仓库>/CLAUDE.md\` "AI 工作约定"小节` |
| `plugins/code-skills/skills/code-rule/SKILL.md` | L363 | `1. \`Read plugins/code-skills/CLAUDE.md\` 全文` | `1. \`Read <本仓库>/CLAUDE.md\` 全文` |

### 4.2 保留(0 处)
- 无 5 处不变量字面(BUG-00002 补修时已清零,本轮只剩命令示例段)

## 5. 测试方案

### 5.1 回归用例
- `git diff --stat plugins/code-skills/skills/{code-publish,code-rule}/SKILL.md` 列出 2 文件
- `git diff` 校验 5 处 Edit 全部生效
- 10 SKILL.md frontmatter byte 级保留
- `git diff marketplace.json plugin.json README*.md CLAUDE.md` 0 diff
- 旧需求档案 0 diff

### 5.2 不引入新 bug
- 仅在命令示例段做"占位符替换",不涉及不变量
- 占位符 `<本仓库>` 沿用 BUG-00002 + REQ-00026 既有约定

## 6. 风险与回退

### 6.1 风险
- **风险 1**:`code-publish` L556 改为"不要追加 `<本仓库>/CLAUDE.md`"后,语义与原意一致(指向本仓库根的 CLAUDE.md 文件)——**不**,`<本仓库>` 仍指本仓库(与 code-rule L336 一致)
- **风险 2**:`code-rule` L363 是"插入位置与算法"步骤的命令示例,占位符化后用户可按字面意思替换——**正确**

### 6.2 回退
- `git revert` 本次 commit
- 重跑 `code-it BUG-00003` 重新实施

## 7. 修复步骤

```
步骤 1:Edit code-publish/SKILL.md L312 / L325 / L361(3 处)
  涉及文件:plugins/code-skills/skills/code-publish/SKILL.md
  关键变更:"Read: plugins/code-skills/skills/code-publish/templates/..." → "Read: <本仓库>/skills/code-publish/templates/..."

步骤 2:Edit code-publish/SKILL.md L556(1 处)
  涉及文件:plugins/code-skills/skills/code-publish/SKILL.md
  关键变更:"不要追加 `plugins/code-skills/CLAUDE.md`" → "不要追加 `<本仓库>/CLAUDE.md`"

步骤 3:Edit code-rule/SKILL.md L363(1 处)
  涉及文件:plugins/code-skills/skills/code-rule/SKILL.md
  关键变更:"1. `Read plugins/code-skills/CLAUDE.md` 全文" → "1. `Read <本仓库>/CLAUDE.md` 全文"

步骤 4:静态校验(1 处)
  涉及文件:10 SKILL.md frontmatter / 旧需求档案
  关键变更:0 diff
```

## 8. 规范遵循

- `skill-conventions.md §规则 1`:SKILL.md frontmatter 必含 name+description,本修复不改 frontmatter ✓
- `marketplace-protocol.md §规则 1`:不改 marketplace.json / plugin.json ✓
- `doc-conventions.md §规则 1`:不改 README ✓
- `commit-conventions.md`:commit 沿用 `chore(code-it):` 前缀 ✓

## 9. 待澄清 / 未决项

无

## 10. 变更记录

| 时间 | 变更 | 关联 |
| --- | --- | --- |
| 2026-06-08 14:50 | 修复规划  code-plan 已产出 fix-plan.md(4 步骤,与 BUG-00002 方案统一) | BUG-00003 |
