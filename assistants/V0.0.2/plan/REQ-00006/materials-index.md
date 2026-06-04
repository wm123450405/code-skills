# 材料登记 — REQ-00006(详细设计阶段)

更新时间:2026-06-04 17:01
版本:V0.0.2

## 1. 项目级规范(与 design 阶段一致,4 个有效约束)

| 规范文件 | 类别 | 对本计划的关键约束 |
| --- | --- | --- |
| `skill-conventions.md §规则 1` | 技能编写 | `code-publish/SKILL.md` frontmatter 必含 `name: code-publish` + 完整 `description`(T-001 严格自检) |
| `module-conventions.md §规则 1` | 模块规划(DEPRECATED 但沿用) | 5 份模板必须在 `templates/` 子目录(T-002 ~ T-006 路径约束) |
| `dashboard-conventions.md §规则 1` | 看板与版本工作空间 | 本计划**不**扩展看板字段(0 触发) |
| `doc-conventions.md §规则 1` + `§规则 2` | 文档编写 | 若 T-008 拆为同步双 README,**必须**中英同次提交 |

占位规范 6 个 / 不相关规范 3 个,与 design 阶段判定一致。

## 2. 上游需求

- 来源:`./assistants/V0.0.2/require/REQ-00006/RESULT.md`(v1,已锁定)
- 摘录:9 FR / 9 NFR / ~33 AC / 10 个边界(E-1 ~ E-10)
- **关键交叉点**(每条 FR ↔ 详细设计章节 ↔ 任务):

| FR | 设计章节(本 RESULT.md) | PLAN.md 对应任务 |
| --- | --- | --- |
| FR-1 前置检查(全检查最严) | §5 算法 1 PreflightChecker | T-001 SKILL.md 中实现 |
| FR-2 生成 3 份手册 | §5 算法 2 ManualBuilder | T-001 SKILL.md 中实现 |
| FR-3 DEPLOY.md 模板 | §6.1 DEPLOY 模板字段 | T-002 写 DEPLOY 模板 |
| FR-4 UPDATE.md 模板 | §6.1 UPDATE 模板字段 | T-003 写 UPDATE 模板 |
| FR-5 Q&A.md 模板 | §6.1 Q&A 模板字段 | T-004 写 Q&A 模板 |
| FR-6 创建 qanda/ 骨架 | §5 算法 3 QandaScaffolder + §6.1 qanda-README 模板 | T-005 写 qanda-README 模板 + T-001 SKILL.md 步骤 2.5 实现 |
| FR-7 错误处理与边界 | §8 异常处理 + §7 接口异常 | T-001 SKILL.md |
| FR-8 不修改其他 8 技能 | (无新任务,纯约束) | 各任务的边界约束 + T-007 不变量自检 |
| FR-9 报告与建议 | §5 算法 4 ReportFormatter | T-001 SKILL.md 步骤 3 |

## 3. 上游概要设计

- 来源:`./assistants/V0.0.2/design/REQ-00006/RESULT.md`(v1,已完成首次)
- 关键摘录(模块拆分 / 接口 / 数据):
  - **7 个新增模块**(`code-publish` SKILL 入口 + 6 个逻辑模块:PreflightChecker / BaselineDetector / ManualBuilder / QandaScaffolder / QandaAggregator / ReportFormatter)
  - **5 份模板**:DEPLOY.md / UPDATE.md / Q&A.md / qanda-README.md / assistants-layout.md
  - **0 修改既有 + 0 新增依赖**
  - **8 项决策 D-1 ~ D-8** 全部演绎得出(0 阻塞)
- 设计阶段的"规范遵循结论":**完全合规,0 偏离 / 0 待澄清冲突 / 0 用户授权偏离**
- 设计阶段未发现规范 vs 设计的"待澄清冲突",故本计划**继承** 0 冲突状态

## 4. 项目现状(实现细节)

本项目是**纯文档型 marketplace 插件**,无源代码,因此"实现细节"集中在"如何写 SKILL.md 自然语言指令"和"模板的 Markdown 字段"上。

### 4.1 SKILL.md 的"实现风格"(参考既有 10 技能)

| 既有技能 SKILL.md | 篇幅 | 关键节奏 |
| --- | --- | --- |
| `code-version/SKILL.md` | 中等(~200 行) | YAML frontmatter + "## 目标" + "## 适用场景" + "## 不适用" + "## 工作目录约定" + "## 输入" + "## 输出" + "## 工具使用约定" + "## 工作流程"(步骤 0..N) + "## 衔接" + "## 不要做的事" |
| `code-review/SKILL.md` | 长(~600 行) | 同上结构 + checklists 引用 |
| `code-design/SKILL.md` | 长(~400 行) | 同上结构 + 首次/增量分支 |
| `code-fix/SKILL.md` | 长(~600 行) | 同上结构 + 缺陷状态机 |

**统一节奏**:`code-publish/SKILL.md` 必须沿用此结构(YAML frontmatter 必含 + "## 目标" + "## 工作流程" 步骤 0 ~ 3 + "## 衔接" + "## 不要做的事")

### 4.2 模板的"实现风格"(参考既有模板)

| 既有模板 | 关键风格 |
| --- | --- |
| `code-version/templates/version-RESULT.md` | 完整 Markdown + `<占位符>` 在尖括号内 |
| `code-design/templates/design.md` | 完整章节结构 + 每章节示例 |
| `code-review/templates/REVIEW-REPORT.md` | 完整章节结构 + 多语言友好(用图标 ✓/✗/⚠) |
| `code-fix/templates/bug.md` | 完整字段表格 + 占位 + 示例 |
| 各技能的 `templates/assistants-layout.md` | 共同范式:版本工作空间目录树 + 路径约定 |

**统一节奏**:`code-publish/templates/*` 全部用 `<占位符>` 风格 + 每个章节内置默认示例(对应需求 AC-3.2)。

### 4.3 看板表格的"实现风格"(参考 V0.0.1 实际看板)

- 数据行格式:`| col1 | col2 | ... |`(`|` 严格分隔,前后含空格)
- 分隔行:`|---|---|...|`(不参与数据)
- 统计行:`**统计**:...`(独立段落,不参与数据)
- 区段锚点:`^## 区段名`(顶格,无前缀)
- **PreflightChecker 实现**:按此风格的 Python/awk-like 行级解析(实际是 Claude 在自然语言指令下执行 Bash `sed`/`grep` 命令)

### 4.4 既有可复用的工具函数 / 中间件
- 无(纯文档项目无运行时函数)

## 5. 本次变更源(增量更新时填写)
- 不适用(首次创建)
