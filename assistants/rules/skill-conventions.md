# 技能编写规范(skill-conventions)

> 本规范文件由 `code-rule` 技能维护,所有 `code-*` 技能在执行时会读取本文件作为强制约束。
> 最后更新:2026-06-03 18:50
> 适用版本:跨所有版本共享(项目级)

## 适用场景
本规范适用于 `plugins/code-skills/skills/<技能名>/SKILL.md` 的编写与修改。涉及"技能的元信息声明、命名、描述、版本感知工作"时查阅本文件。其它插件(未来)若需独立约定,各自维护自己的 `skill-conventions.md`。

## 强制级别约定
本文件中各规则的强制级别逐条标注(参见各"规则 N"小节的"强制级别"字段),本文件头部不统一声明。

---

## 规则 1:SKILL.md 必含 name + description,且 name 与目录名一致

### 条款
`plugins/code-skills/skills/<技能名>/SKILL.md` 必须以 YAML frontmatter 开头,至少包含以下两个字段:
- `name`:取值为**技能目录名**(kebab-case),与所在目录严格一致(例如 `skills/code-init/SKILL.md` 的 `name` 必须为 `code-init`)
- `description`:一段完整的自然语言描述,说明该技能的目标、适用场景、典型触发条件;**不**接受空字符串、占位符、纯关键词堆砌

`name` 与目录名不一致、或 `description` 缺失/为空,视为本规则违反。

### 强制级别
- 必须

### 适用范围
- `plugins/code-skills/skills/*/SKILL.md`(所有技能入口)
- 新增技能 / 修改技能元信息 / 重命名技能目录时均适用

### 正面示例
`plugins/code-skills/skills/code-version/SKILL.md` 顶部:
```markdown
---
name: code-version
description: 版本管理(Version Management)。要求用户提供一个"版本号",切换或创建 `./assistants/<版本号>/` 工作空间。在所有其他 `code-*` 技能调用之前使用,也可随时重跑以切换版本。
---
```

要点:
- `name` 与目录名 `code-version` 完全一致
- `description` 一句话讲清"做什么、何时用",可被 Claude Code 触发决策使用

### 反面示例
```markdown
---
name: CodeVersion         # 错误:大小写不一致,且与目录名 kebab-case 不符
description:              # 错误:description 为空
---
```

```markdown
---                      # 错误:完全缺少 frontmatter
# 版本管理
...
```

### 例外
- 无
- 若因 Claude Code 协议未来调整新增 frontmatter 字段,本规则应同步扩展(参见 `dashboard-conventions.md §看板字段约定扩展`)

### 关联规范
- `./assistants/rules/module-conventions.md §规则 1`(技能目录结构约定)
- `./assistants/rules/dashboard-conventions.md §规则 1`(看板/模板扩展时的同步)

### 来源
- 由 `code-rule` 技能添加于 2026-06-03 18:50
- 用户原始描述:"所有 `SKILL.md` 的 YAML frontmatter 必须含 `name` + `description` 字段,`name` 与目录名一致"
