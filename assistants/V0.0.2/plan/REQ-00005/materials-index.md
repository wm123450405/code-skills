# 材料登记 — REQ-00005

更新时间:2026-06-04 16:30
版本:V0.0.2

## 项目级规范(13 个,与 design 阶段一致)

| 规范文件 | 类别 | 关键约束摘要 |
| --- | --- | --- |
| `./assistants/rules/skill-conventions.md` | 技能编写 | §规则 1 — frontmatter 不可变(本计划强约束) |
| `./assistants/rules/dashboard-conventions.md` | 看板与模板 | §规则 1 — 字段扩展需三同步(本计划不触发) |
| `./assistants/rules/doc-conventions.md` | 文档编写 | §规则 1 — README 中英同次提交(本计划不触发) |
| `./assistants/rules/marketplace-protocol.md` | Marketplace 协议 | §规则 1 — `$schema` / `name` / `version` 必填(本计划不触发) |
| `./assistants/rules/encoding-conventions.md` | 编码格式 | §规则 1 — REQ/BUG 5 位纯数字;§规则 3 — TASK 嵌套式 5+5 位;**本计划强约束**用于分配任务编号 |
| `./assistants/rules/migration-mapping.md` | 编码迁移 | §规则 1-4(不触发) |
| `./assistants/rules/module-conventions.md` | 模块规划 | ⚠️ DEPRECATED(不触发) |
| `./assistants/rules/directory-conventions.md` | 目录结构 | 占位(不触发) |
| `./assistants/rules/coding-style.md` | 代码风格 | 占位(不触发) |
| `./assistants/rules/commit-conventions.md` | 提交与合并 | 占位(NFR-6 显式不直接填充);本计划沿用 V0.0.1 实践 `chore(<scope>): <subject>` |
| `./assistants/rules/dependency-conventions.md` | 三方依赖 | 占位(不触发) |
| `./assistants/rules/framework-conventions.md` | 框架选型 | 占位(不触发) |
| `./assistants/rules/naming-conventions.md` | 命名风格 | 占位(不触发) |

## 上游需求

- **来源**:`./assistants/V0.0.2/require/REQ-00005/RESULT.md`
- **版本**:v1(2026-06-04 13:33,已锁定)
- **提取**:6 FR / 8 NFR / ~32 AC / 13 边界场景 / 8 澄清项(Q-1~Q-4 锁定,Q-5/Q-7 未采用,Q-6/Q-8 默认)
- **关键交叉点(每条 FR → 本计划章节)**:
  - FR-1(步骤 0a 拉取)→ `RESULT.md §4.1` / `interface-specs.md §步骤 0a`
  - FR-2(步骤 0b 版本对齐)→ `RESULT.md §4.2` / `interface-specs.md §步骤 0b`
  - FR-3(末尾兜底提交)→ `RESULT.md §4.3` / `interface-specs.md §步骤 N`
  - FR-4(不改 `code-it`)→ `PLAN.md §T-001 ~ §T-003 边界与异常`(严守 `code-it` 边界)
  - FR-5(不改 `code-version`)→ `RESULT.md §4.2.2 独立调用约束`
  - FR-6(不改 marketplace/plugin/CLAUDE.md)→ `module-details.md §1` 强约束不动表

## 上游概要设计

- **来源**:`./assistants/V0.0.2/design/REQ-00005/RESULT.md`
- **版本**:v1(2026-06-04 16:00,已完成)
- **提取**:
  - **模块拆分**:3 个 SKILL.md 修改(增量追加 0a/0b/N 步骤)+ 看板追加
  - **接口概要**:步骤 0a / 0b / N 工作流步骤的契约
  - **数据结构**:无新增/修改实体(本仓库无运行时数据模型)
  - **决策**:D-1 步骤 0a 位置 / D-2 0a/0b 协同 / D-3 末尾兜底范围 / D-5 与 `code-it` 并存
  - **13 条关键不变量**:全部保留(详见 `design/.../RESULT.md §3`)
- **关键交叉点(概要设计章节 → 本计划章节)**:
  - 概要设计 §7 模块划分 → `module-details.md` 详化每个插入点的位置/上下文
  - 概要设计 §8 接口概要 → `interface-specs.md` 给出伪代码/弹窗文本/错误码
  - 概要设计 §9 数据结构 → `data-changes.md` 字段级变更清单
  - 概要设计 §10.3 commit 模板 → `RESULT.md §7.1 / §8` 接口细节
  - 概要设计 §12 风险与缓解 → `risk-analysis.md` 13 个边界详化

## 项目现状(实现细节)

### 语言/框架
- **本仓库无应用代码**:无 Node.js / Python / Go / Rust 等运行时
- **唯一"代码"载体**:Markdown 文本(SKILL.md / RESULT.md / *.md)
- **唯一"运行时"**:Claude Code 解释执行 SKILL.md 中描述的工作流,工具集 = Read / Write / Edit / Glob / Grep / Bash / Skill / AskUserQuestion

### 命名风格(Markdown)
- **目录**:`kebab-case`(如 `code-require`、`code-design`)
- **SKILL.md frontmatter**:`name` = 目录名,`description` = 一段完整描述
- **章节标题**:`##` / `###` / `####` 层级
- **代码块**:` ` 行内代码 / ``` ``` 多行代码块
- **表格**:GitHub-flavored Markdown 表格

### 错误处理范式
- **`git pull` 失败**:中断 + stderr 透传 + 3 种分类提示(E-2/E-3/E-4)
- **`git commit` 失败**:不重试,stderr 透传
- **`AskUserQuestion` 必须答**:无超时(E-11)
- **末尾兜底无变更**:静默跳过(打印"无文件变更,跳过末尾提交")

### 并发原语
- **N/A**:本需求无并发场景(`code-require` / `code-design` / `code-plan` 是顺序工作流)

### 既有相似功能的实现风格
- **V0.0.1 REQ-00001 / REQ-00002 已实施过 SKILL.md 增量修改**:风格 = `Edit` 工具精确替换,不改 frontmatter,改前 `Read` 全文
- **V0.0.1 commit 实践**:`chore(<scope>): <subject>`,subject 含 `REQ-NNNNN` 引用
- **V0.0.1 看板"执行的开发命令记录"**:本需求末尾兜底 commit 的"失败处理"风格可参考

### 既有测试用例的风格与覆盖度
- **N/A**:本仓库无自动化测试(`CLAUDE.md` 显式说明)
- **本需求不写测试代码**:任务类型 = `文档` 类(测试状态 = `不适用`)
- **`code-unit` 阶段会按 `code-unit` 步骤 0a 项目可测性守卫(REQ-00009)判定**:本仓库无构建/测试文件 → 守卫判定"不可测" → 测试状态保持 `不适用`,不写 `test/.../RESULT.md`

### 可复用的工具函数
- **`git pull` / `git status --porcelain` / `git add` / `git commit`**:Bash 工具内置,无新增依赖
- **`AskUserQuestion`**:Claude Code 工具,直接调用
- **`Skill` 工具**:`code-require` 调 `code-version` 的唯一方式(FR-5.AC-5.2)

## 本次变更源(首次设计,无变更源)

> 本计划为首次编写,无"增量"历史。

| 变更源 | 检测方式 | 变化列表 |
| --- | --- | --- |
| 需求侧 | 上游 `require/.../RESULT.md` v1(已锁定) | 无变化(本计划首版) |
| 概要设计 | 上游 `design/.../RESULT.md` v1(已完成) | 无变化(本计划首版) |
| 规范侧 | `./assistants/rules/` 13 个文件(本计划首版) | 无变化(本计划首版) |
| 代码侧 | 3 个 SKILL.md + 看板(本计划首版) | 无变化(本计划首版) |
