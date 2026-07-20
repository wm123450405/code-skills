# Marketplace 协议规范(marketplace-protocol)

> 本规范文件由 `code-rule` 技能维护,所有 `code-*` 技能在执行时会读取本文件作为强制约束。
> 最后更新:2026-06-03 19:15
> 适用版本:跨所有版本共享(项目级)

## 适用场景
本规范适用于本仓库(marketplace 仓库根)及所有子插件的"Claude Code 协议清单文件"。涉及"如何写 marketplace.json / plugin.json、字段如何同步、$schema 引用"时查阅本文件。

## 强制级别约定
本文件中各规则的强制级别逐条标注(参见各"规则 N"小节的"强制级别"字段),本文件头部不统一声明。

---

## 规则 1:marketplace 与 plugin 清单的字段约束

### 条款
本仓库的 marketplace 协议清单文件必须满足以下约束:

1. **`$schema` 必填**:每个协议清单文件(`marketplace.json`、`plugin.json`)必须在根节点含 `$schema` 字段,引用对应的官方 JSON Schema,当前值:
   - marketplace 根:`https://anthropic.com/claude-code/marketplace.schema.json`
   - 插件:`https://anthropic.com/claude-code/plugin.schema.json`
   - 字段未来若被官方协议调整,本规则应同步更新(参见 `dashboard-conventions.md §规则 1`)
2. **name / version 必填**:每个协议清单文件必须含 `name` 与 `version` 字段;`version` 推荐 semver(`MAJOR.MINOR.PATCH`)
3. **marketplace 与子插件的 version 同步**:`marketplace.json` 中 `plugins[].version` 必须与对应 `plugins/<name>/.claude-plugin/plugin.json` 的 `version` 字段保持**完全一致**;`marketplace.json` 自身的 `version` 是 marketplace 协议的版本,独立于子插件
4. **marketplace 根的 `plugins[].source`**:必须以 `./` 开头,指向相对路径(当前约定为 `./plugins/<name>`)
5. **marketplace 根的 `plugins[].skills`**:必须是**相对路径数组**,每个路径以 `./skills/<skill-name>` 开头;**不得**使用绝对路径、glob 模式或单字符串
6. **不允许未知字段**:marketplace.json 必须只含 Claude Code 协议文档定义过的字段(如 `name` / `version` / `description` / `owner` / `plugins`);`plugin.json` 同理。出现未声明字段(如自定义的 `metadata` / `tags`)会被 Claude Code 拒绝加载

### 强制级别
- 必须

### 适用范围
- **整个 marketplace 所有 JSON** 协议清单文件
- 当前具体路径:
  - `.claude-plugin/marketplace.json`(仓库根)
  - `plugins/code-skills/.claude-plugin/plugin.json`(子插件)
- 未来新增子插件时,每个新插件的 `.claude-plugin/plugin.json` 同样适用

### 正面示例
`.claude-plugin/marketplace.json`(片段):
```json
{
  "$schema": "https://anthropic.com/claude-code/marketplace.schema.json",
  "name": "code-skills",
  "version": "1.0.0",
  "owner": { "name": "code-skills" },
  "plugins": [
    {
      "name": "code-skills",
      "version": "1.0.0",
      "source": "./plugins/code-skills",
      "skills": [
        "./skills/code",
        "./skills/code"
      ]
    }
  ]
}
```

要点:
- `$schema` / `name` / `version` 全齐
- `plugins[].version = "1.0.0"` 与子插件 `plugin.json` 一致
- `source` 以 `./` 开头
- `skills` 是 `./` 开头的路径数组

### 反面示例
```json
{
  "$schema": "https://anthropic.com/claude-code/marketplace.schema.json",
  "name": "code-skills",
  "version": "1.0.0",
  "metadata": { "tier": "experimental" },   // ❌ 未知字段,Claude Code 会拒绝
  "plugins": [
    {
      "name": "code-skills",
      "source": "plugins/code-skills",      // ❌ 缺 ./ 前缀
      "skills": "./skills/*",               // ❌ 单字符串 + glob 模式
    }
  ]
}
```

```json
// plugin.json 反例
{
  "$schema": "https://anthropic.com/claude-code/plugin.schema.json",
  "name": "code-skills"
  // ❌ 缺 version 字段
}
```

### 例外
- **dev / 草稿态插件**:本地调试可临时去掉 `version` 同步约束,但**任何**对外发布(commit / push / publish)前必须恢复同步
- `$schema` 字段:若官方 URL 变更,允许临时使用 `https://example.com/placeholder.schema.json` 占位,但需在同一 commit 内附带 `TODO:` 注释,后续 PR 修复

### 关联规范
- `./assistants/rules/dashboard-conventions.md §规则 1`(看板/模板扩展需多文件同步 — `version` 字段扩展同理)
- `./assistants/rules/doc-conventions.md §规则 1`(README 多语言对仗)

### 来源
- 由 `code-rule` 技能添加于 2026-06-03 19:15
- 用户原始描述:"增加整个仓库 marketplace 级别的规范"(本规则覆盖了协议字段约束)
