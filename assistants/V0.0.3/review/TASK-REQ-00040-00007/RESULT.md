# 改修要求 — TASK-REQ-00040-00007

- 任务编码:`TASK-REQ-00040-00007`
- 任务标题:[修改] 移除 `design/REQ-00040/RESULT.md` line 175 越界字段类型字面 `string`
- 所属版本:V0.0.3
- 所属需求:REQ-00040
- 类型:修改
- 触发/来源:审查改修
- 严重程度:**必须改**(概设越界,违反 `code-plan` 步骤 8.11 准则)
- 触发时间:2026-06-25
- 严重程度:必须改
- 触发评审:`./assistants/V0.0.3/review/REQ-00040/REVIEW-REPORT.md`

## 1. 触发的原任务

- `TASK-REQ-00040-00001`(code-fix 步骤 0 末尾追加"项目可启动性探测" 子节) — 评审发现源(本任务的字面是 T-001 落地时在概设的"## 文档头新增字段" 段中错误地写了 `string` 类型)
- `TASK-REQ-00040-00002`(code-fix 步骤 6 末尾追加"复现产物登记" 子节) — T-001 的强依赖任务(也涉及产物路径,需在原 PLAN.md 任务详情中确认产物路径字面)
- 关联任务:`TASK-REQ-00040-00001, TASK-REQ-00040-00002`

## 2. 问题清单

### F-001:`design/REQ-00040/RESULT.md` line 175 字段类型越界

- **位置**:`./assistants/V0.0.3/design/REQ-00040/RESULT.md` line 175
- **类别**:详细设计符合度 / 概设越界
- **严重程度**:**必须改**
- **当前字面**:
 ```
 | 复现方式 | string | `程序复现` / `文本复现` / `未复现` |
 | 产物路径 | string | `reproduce/`(子目录相对路径;空表示无产物) |
 ```
- **问题**:`design/.../RESULT.md` §7 / §8 / §9 不应出现"完整字段类型"(string / number / integer / boolean / datetime / UUID)— 这是详细设计深度内容,违反 `code-plan` 步骤 8.11 概设越界检测准则
- **建议改修**:
 - 把 `string` 移除(改为**占位符描述**或"具体类型见 `plan/.../RESULT.md` §6.1")
 - 表格结构保留(`| 字段 | <类型字面删除,改为描述> | 值 |`)
- **示例(改修后字面)**:
 ```
 | 复现方式 | enum(三种值见下方"## 复现方式字面说明") | `程序复现` / `文本复现` / `未复现` |
 | 产物路径 | 字符串(子目录相对路径;空表示无产物) | `reproduce/` |
 ```
 或更轻量:
 ```
 | 复现方式 | 三选一字面 | `程序复现` / `文本复现` / `未复现` |
 | 产物路径 | 字符串 | `reproduce/` |
 ```

## 3. 应当改修的文件

### 3.1 `./assistants/V0.0.3/design/REQ-00040/RESULT.md`

- **现状**:line 175 表格中 2 行 `string` 类型字面
- **应改为**:把 `string` 移除(改为"enum" / "字符串" 等非严格类型字面,或"具体类型见 `plan/.../RESULT.md` §6.1"占位说明)
- **理由**:沿用 `code-plan` 步骤 8.11 概设越界检测准则,`design/.../RESULT.md` 不应出现"完整字段类型"

## 4. 验证手段

- **静态校验**:`grep -nE "\|\s*(string|number|integer|boolean|datetime|UUID)\s*\|" assistants/V0.0.3/design/REQ-00040/RESULT.md` → 期望 **0 命中**
- **设计符合度**:与 `plan/.../RESULT.md` §6.1 文档头 2 字段定义仍一致(详设保持"string" 类型字面,概设不冲突)
- **不破坏**:`bug.md` 模板的文档头 2 字段仍按 plan/§6.1 落地(本任务**不**改 bug.md)

## 5. 关联依据

- **规范条款**:`./assistants/rules/skill-conventions.md`(无新规则,沿用项目级职责分离 — 概设只关注"系统长什么样",**不**关注"字段类型")
- **`code-plan` SKILL.md** 步骤 8.11 概设越界检测(本评审沿用)
- **设计章节**:`./assistants/V0.0.3/design/REQ-00040/RESULT.md` §6.2 文档头扩展(line 175 命中位置,需重写)
- **详设章节**:`./assistants/V0.0.3/plan/REQ-00040/RESULT.md` §6.2 文档头新增 2 字段(line 230-231 详设描述,`string` 类型字面是详设的"职责",概设不写不冲突)

## 6. 不需要做的

- **不**修改 `plan/.../RESULT.md`(详设中的 `string` 类型字面是 §6.2 详设的"职责",**保留**)
- **不**修改 `bug.md` 模板(本任务**不**改模板)
- **不**修改 `code-fix/SKILL.md`(T-001/T-002 子节已正确使用变量形式 `reproduceDir = "./assistants/<version>/fix/" + bugNum + "/reproduce/"`,**无** `string` 字面)
- **不**修改 `assistants-layout.md`(已正确同步 reproduce/ 子目录行,**无**类型字面)
- **不**重写 `design/.../RESULT.md` 整段,只修改 line 175 表格 2 行的类型字面

## 7. 期望提交

- **commit**:`chore(code-it): TASK-REQ-00040-00007 移除 design line 175 越界字段类型字面`
- 落地后:`grep -nE "\|\s*(string|number|integer|boolean|datetime|UUID)\s*\|" assistants/V0.0.3/design/REQ-00040/RESULT.md` = 0