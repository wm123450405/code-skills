# 材料登记 — REQ-00030

更新时间:2026-06-12 14:31
版本:V0.0.3

## 项目级规范

| 规范文件 | 类别 | 关键约束摘要 |
| --- | --- | --- |
| `skill-conventions.md §规则 1` | 技能元信息 | SKILL.md 必含 `name`(=目录名,kebab-case) + `description`;frontmatter L1-3 字节级保留 |
| `module-conventions.md §规则 1`(已弃用,沿用历史) | 资源摆放 | 资源文件必须放 `templates/` / `checklists/` / `guidelines/` 子目录 |
| `directory-conventions.md` | 目录结构 | (module-conventions 已迁移至此) |
| `doc-conventions.md §规则 1` | 文档 | README 多语言版本必须保持结构对仗 |
| `dashboard-conventions.md §规则 1` | 看板 | 看板字段三方同步(本需求**不**触发字段扩展) |
| `encoding-conventions.md §规则 1/3` | 编码 | 任务编号正则;接收端宽松 `[A-Za-z0-9.\-_]+` |
| `naming-conventions.md` | 命名 | kebab-case 技能目录名 |
| `coding-style.md` | 编码风格 | (本需求不涉及源代码) |
| `commit-conventions.md` | 提交 | `chore(<skill>):` 前缀;格式沿用既有 5 类 |
| `framework-conventions.md` | 框架 | (本仓库无框架) |
| `dependency-conventions.md` | 依赖 | (本需求 0 新增依赖) |

## 上游需求

- 来源:`./assistants/V0.0.3/require/REQ-00030/RESULT.md`
- 状态:已完成
- 提取:**8 FR / 6 NFR / 9 AC / 3 待澄清 / 7 关联需求**

## 上游概要设计

- 来源:`./assistants/V0.0.3/design/REQ-00030/RESULT.md`
- 设计目标:整体=--extensible / 功能性=高
- 提取:5 个被改文件 / 0 个被新增文件 / 11 个 0 改 SKILL.md
- 关键交叉点:

| 上游 FR | 概要设计对应章节 | 详设对应章节 |
| --- | --- | --- |
| FR-1 步骤 0b 扩展性判定 | §3.2 | §3.2 步骤 0b 自适应问路 |
| FR-2 步骤 0b 收紧 | §3.2 | §3.2 |
| FR-3 步骤 9A/10A/11A 输出深度 | §3.3 | §3.3 + §4 模块详细化 |
| FR-4 templates/design.md 重写 | §3.4 | §3.4 + §5 算法与逻辑 |
| FR-5 code-plan 补做强约束 | §3.5 | §3.5 + §6 数据结构 + §7 接口细节 |
| FR-6 架构骨架触发收紧 | §3.6 | §3.6 + §8 异常处理 + §9 安全要求 |
| FR-7 code-check 校验新增 | §3.7 | §3.7 + §10 状态机 / §11 性能与资源 |
| FR-8 扩展性三阶段下沉 | §3.8 | §3.8 + §12 测试要点 |

## 项目现状(实现细节)

### 命名风格

- 技能名:kebab-case(如 `code-design` / `code-plan` / `code-check`)
- 文件名:小写连字符(如 `design-notes.md` / `task-plan.md`)
- 函数名:本仓库不涉及源代码;**不适用**
- 变量名:本仓库不涉及源代码;**不适用**

### 错误模型

- 错误处理:沿用既有 `code-design` 步骤 E-1 ~ E-12(12 种边界异常)
- 错误码:本仓库**不**有错误码系统(无 API / 无后端)

### 并发原语

- 沿用既有:每个 `code-*` 技能是串行执行(无并发原语)
- 并发模型:**不适用**(本仓库不涉及多线程)

### 既有相似功能的实现风格

- `code-design` 步骤 0a / 0b.0 / 0 / 1-5:本设计**不**重写,字节级保留
- `code-plan` 步骤 0a / 0b.0 / 0b / 0-6 / 8A-9A / 11A-18A:本设计**不**重写
- `code-check` 既有评审清单:本设计**追加**(不重写)

### 既有测试用例的风格与覆盖度

- 本仓库**不**包含测试框架 / 测试用例(`CLAUDE.md` §"需与用户确认的约定"明确锁定)
- 测试要点:本设计的"## 测试要点"主要是**人工评审**(`code-check`)+ **git diff 验证**(`git status` / `git diff`)+ **历史兼容性核对**(既有 9 个 REQ 的 design / plan 0 改)

### 可复用的工具函数/中间件

- `truncateTitle(title, maxLen=30)`:沿用 `code-require` 既有工具函数
- `formatReqTitle(reqNum, title)`:沿用
- `formatTaskTitle(taskNum, title)`:沿用
- `parseResultTitle(filePath)`:沿用
- `writeDesignGoalsSection(designResultPath, goals, source)`:沿用 `code-design` 既有
- `readDesignGoalsFromDesign(designResultPath)`:沿用 `code-plan` 既有
- `adjustTaskGranularityByGoals(planResultPath)`:沿用 `code-plan` 既有

## 命令行参数

无 `--result` / `--plan` 参数,本轮**不**触发模板填充步骤(沿用 REQ-00007 Q-4)。

## 本次变更源(本节首次设计为空)

| 变更源 | 检测方式 | 变化列表 |
| --- | --- | --- |
| 需求侧 | 上游 RESULT.md 变更记录 | 无 |
| 概要设计侧 | 上游 RESULT.md 变更记录 | 无 |
| 规范侧 | ./assistants/rules/ 对比 | 无 |
| 代码侧 | 重跑项目探索 | 无 |
