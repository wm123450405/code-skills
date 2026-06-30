# 技能编写规范(skill-conventions)

> 本规范文件由 `code-rule` 技能维护,所有 `code-*` 技能在执行时会读取本文件作为强制约束。
> 最后更新:2026-06-30 18:00
> 适用版本:跨所有版本共享(项目级)

## 适用场景
本规范适用于 `plugins/code-skills/skills/<技能名>/SKILL.md` 的编写与修改。涉及"技能的元信息声明、命名、描述、版本感知工作"时查阅本文件。其它插件(未来)若需独立约定,各自维护自己的 `skill-conventions.md`。

## 强制级别约定
本文件中各规则的强制级别逐条标注(参见各"规则 N"小节的"强制级别"字段),本文件头部不统一声明。

---

## 规则 1:SKILL.md 必含 name + description,且 name 与目录名一致

### 条款
`plugins/code-skills/skills/<技能名>/SKILL.md` 必须以 YAML frontmatter 开头,至少包含以下两个字段:
- `name`:取值为**技能目录名**(kebab-case),与所在目录严格一致(例如 `skills/code-ver/SKILL.md` 的 `name` 必须为 `code-ver`)
- `description`:一段完整的自然语言描述,说明该技能的目标、适用场景、典型触发条件;**不**接受空字符串、占位符、纯关键词堆砌

`name` 与目录名不一致、或 `description` 缺失/为空,视为本规则违反。

### 强制级别
- 必须

### 适用范围
- `plugins/code-skills/skills/*/SKILL.md`(所有技能入口)
- 新增技能 / 修改技能元信息 / 重命名技能目录时均适用

### 正面示例
`plugins/code-skills/skills/code-ver/SKILL.md` 顶部:
```markdown
---
name: code-ver
description: 版本管理。合并 code-version + code-publish + code-init 能力。新项目自动初始化;已初始化项目切换版本;当前版本未发布时询问是否先发布再切换。
---
```

要点:
- `name` 与目录名 `code-ver` 完全一致
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
- `./assistants/rules/directory-conventions.md`(技能目录结构约定)
- `./assistants/rules/dashboard-conventions.md §规则 1`(看板/模板扩展时的同步)

### 来源
- 由 `code-rule` 技能添加于 2026-06-03 18:50
- 用户原始描述:"所有 `SKILL.md` 的 YAML frontmatter 必须含 `name` + `description` 字段,`name` 与目录名一致"

---

## 规则 2:SKILL.md 与同目录 templates/ 中不得包含开发痕迹

### 条款

`plugins/code-skills/skills/<技能名>/SKILL.md` 与同目录 `templates/` 下所有 `.md` 文件中,**不得**包含以下 6 类"开发痕迹"字面(段尾括号 / 句中 / 段首 / 标题括号 任何位置):

1. **段尾引用型**:形如 `(本需求 REQ-NNNNN FR-X 新增)` / `(本需求 BUG-NNNN 新增)` / `(本需求 REQ-NNNNN YYYY-MM-DD 起生效)` 等显式回溯某条需求/缺陷的尾注。
2. **回溯注释型**:形如 `原 code-unit 步骤 X` / `原 fix-plan.md 退场` / `沿用原 code-unit` / `原 code-design 步骤 0b 的 4 问题 → 1 问题 → 0 问题` 等对历史版本/已退场功能的回溯性叙述。
3. **决策记录型**:形如 `(Q-1 锁定 A)` / `(Q-3 锁定 A)` / `(Q-P7 锁定)` / `(Q-2 采纳默认)` / `(Q-4 隐含答复 C)` 等与用户/产品对齐过程的 Q&A 锚点编号。
4. **生效日标记型**:形如 `YYYY-MM-DD 起生效` / `2026-06-15 起生效` 等"该规则自某天起生效"的回溯日期标记。
5. **退场文件名引用型**:对 `fix-plan.md` / `fix-work-log.md` / `fix-compile-and-run.md` / `fix-test-results.md` 等已退场过程文档名的引用。
6. **杂项痕迹型**:`变更人:<具体自然人名>` 等指向具体人的字段;以及不属于上述 5 类但属于"开发过程产生的、不影响技能实际使用"的其他字面。

### 强制级别
- 必须

### 适用范围
- `plugins/code-skills/skills/*/SKILL.md`(全体 7 个 code-* 技能)
- `plugins/code-skills/skills/*/templates/*.md`(全体模板)
- **不**适用于:
  - `plugins/code-skills/skills/code-req/references/`(留作后续规范)
  - `plugins/code-skills/skills/code-req/templates/`(留作后续规范)
  - `assistants/` 下的任何历史工作产物(它们是有史料价值的工作记录)
  - `plugins/code-skills/.claude-plugin/`、`marketplace.json` / `plugin.json` / `README*.md` / `CLAUDE.md`
  - 已被代码层面删除的技能目录

### 例外(白名单)

以下 4 类字面**不属于**"开发痕迹",**允许**保留:

1. **合规性条款**:形如 `既有 N 个 PLAN 不追溯重拆` / `既有 N 需求 NFR-5 字节级保留` 等说明"历史边界不能动"的真实合规说明。
2. **跨版本规范继承引用**:形如 `(沿用 V0.0.0 NFR-X)` / `(沿用 V0.0.1 NFR-Y)` / `(沿用 encoding-conventions §规则 1)` 等指向**规范名**的版本化引用(它们是跨技能契约,不是开发痕迹)。
3. **跨需求引用**:`plugins/code-skills/CLAUDE.md` 等位置对其他需求文档的引用(如 `[RESULT.md](./require/REQ-XXXXX/RESULT.md)`)允许保留;但**不得**反过来在 SKILL.md / templates/ 中以"本需求"指代。
4. **模板占位符**:`templates/*.md` 中的 `REQ-00001` / `BUG-00001` / `TASK-REQ-00001-00001` 等示例性编号属于模板占位符,**保留**(它们是供用户填空用的,不是开发痕迹)。

### 正面示例
```markdown
## 标题解析

> 本节给出 `RESULT.md` 文档标题的解析约定。

### 工具函数

\`\`\`ts
function parseResultTitle(filePath: string): string { ... }
\`\`\`
```
要点:不出现"本需求 REQ-NNNNN 新增"等字面。

### 反面示例
```markdown
## 标题解析(REQ-00013 新增)

> 本节给出 `RESULT.md` 文档标题的解析约定,源自本需求 REQ-00013。

沿用原 code-unit 步骤 0a 的工具函数:
\`\`\`ts
function parseResultTitle(filePath: string): string { ... }  // (Q-1 锁定 A,2026-06-15 起生效)
\`\`\`
```
要点:段尾括号、句中「源自本需求」「沿用原 code-unit」「Q-1 锁定 A」「YYYY-MM-DD 起生效」全部违规。

### 例外
- **`code-fix` 技能 SKILL.md 中对自身 `fix/` 目录的引用**:`fix/` 目录是 `code-fix` 技能**当前职责范围**(`fix/RESULT.md` / `fix/<BUG-NNN>/RESULT.md` 仍是有效路径),**不**属于已退场功能,本规则**不**约束此类引用。
- **历史合规性条款**(本规则「例外」§1):即使形似"开发痕迹",只要是**真实的**合规性说明,保留。

### 关联规范
- `./assistants/rules/dashboard-conventions.md §规则 1`(本规则不触发看板字段扩展三方同步——本规则是"内容约束",不是"字段扩展")
- `./assistants/rules/directory-conventions.md`(资源放 `templates/` / `checklists/` / `guidelines/` 子目录——本规则约束范围只覆盖 `templates/`,不覆盖后两者)
- `./assistants/rules/doc-conventions.md §规则 1`(本规则与之**正交**:`doc-conventions` 约束 README 多语言对仗,本规则约束 SKILL.md / templates/ 内容纯净度)

### 来源
- 由 `code-rule` 技能添加于 2026-06-16 17:33
- 用户原始描述:"将需求 REQ-00036 中的清理规则按照不允许出现在技能代码中的方式记录到规范中"
- 上游追溯:`./assistants/V0.0.3/require/REQ-00036/RESULT.md §4 功能需求 FR-1 ~ FR-6` + `./assistants/V0.0.3/design/REQ-00036/RESULT.md §6 功能域 1`
