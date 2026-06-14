# 接口详细规格 — REQ-00025
版本:V0.0.3

## 接口:code-* 技能 SKILL.md 编号解析函数族(本需求涉及)

- **形式**:伪代码 / 正则字面量(在 SKILL.md 中以代码块形式呈现)
- **路径/签名**:`./plugins/code-skills/skills/<name>/SKILL.md §<章节> <code block>`
- **入参**:`<input>`(用户输入字符串)
- **出参**:布尔(`true` = 合法编号)+ 提取的 prefix + suffix
- **示例(旧 → 新)**:
  - `^REQ-\d{5}$` → `^REQ-[A-Za-z0-9.\-_]+$`
  - `^BUG-\d{5}$` → `^BUG-[A-Za-z0-9.\-_]+$`
  - `^TASK-REQ-\d{5}-\d{5}$` → `^TASK-REQ-[A-Za-z0-9.\-_]+-[A-Za-z0-9.\-_]+$`
  - `^TASK-BUG-\d{5}-\d{5}$` → `^TASK-BUG-[A-Za-z0-9.\-_]+-[A-Za-z0-9.\-_]+$`
- **错误码**:
  - 非法前缀:`⚠ 前缀 <X>- 未登记,请先调 code-rule 登记或使用 REQ-/BUG-/TASK- 之一`
  - 非法后缀字符:`⚠ 编号含非法字符: <char>`
  - 后缀空:`⚠ 编号后缀为空: <input>`
- **版本策略**:`code-skills` 主版本不破坏 5 位纯数字兼容性
- **兼容策略**:新正则 `[A-Za-z0-9.\-_]+` ⊇ 旧正则 `\d{5}`(超集)
- **依据规范**:`encoding-conventions.md §规则 1/2/4`(本需求修订后)

## 接口:encoding-conventions.md §规则 1.5(本需求新增)

- **形式**:Markdown 小节 + 表格
- **路径**:`./assistants/rules/encoding-conventions.md §规则 1.5(全新小节)`
- **入参**:用户登记的"前缀名" + "等价类别"(`REQ` / `BUG` / `TASK-REQ` / `TASK-BUG` 之一)
- **出参**:§规则 1.5 表格追加 1 行
- **示例**:
  ```
  JIRA- → 等价 REQ-(2026-06-07 登记)
  TAPD- → 等价 REQ-(2026-06-08 登记)
  ```
- **错误码**:
  - 前缀未登记:`⚠ 前缀 <X>- 未登记,请先调 code-rule 登记或使用 REQ-/BUG-/TASK- 之一`
- **版本策略**:N/A
- **兼容策略**:N/A
- **依据规范**:`encoding-conventions.md §规则 1.5`(本需求新增)
