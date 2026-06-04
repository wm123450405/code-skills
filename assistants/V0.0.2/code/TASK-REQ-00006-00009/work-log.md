# 开发日志 — TASK-REQ-00006-00009

开始时间:2026-06-04 18:10
版本:V0.0.2
任务标题:`[修改] 修订双 README <code-publish> 行措辞(明确"首次调用"语义)`
触发/来源:**审查改修**(由 `code-review` 派生,F-002)

## 项目现状(步骤 6 记录)

- **项目类型**:Claude Code Marketplace 插件(`code-skills`),纯文档型
- **本任务范围**:仅修改 `plugins/code-skills/{README.md, README.en.md}` 2 文件 L38(各 1 行)
- **既有 `code-publish` 行**:
  - zh L38 "用途"列:「顺带在项目级创建 `assistants/qanda/` 目录」
  - en L38 "Purpose"列:"also creates the project-level `assistants/qanda/` directory"
- **SKILL.md §步骤 2.5 措辞**(对照基准):"**目的**:本需求顺带在项目级创建 `assistants/qanda/` 骨架" — 用"本需求顺带"表"此为本需求一次性副作用",与 README 的"顺带在项目级创建"语义略有不同(后者隐含"每次运行都创建")
- **本任务边界**:**仅修 README**;**不**改 SKILL.md(已在 T-001 "已完成",且 §2.5 措辞与其自身逻辑一致)

## 项目级规范要点(步骤 4 记录)

完整 13 规范已在 `code-review` 阶段扫过(详 `plan/REQ-00006/rule-compliance.md`)。本任务**强约束**:
- `./assistants/rules/doc-conventions.md` §规则 1:**强约束**
  - README 中英结构对仗(同数量、相同顺序的章节)
  - 任一语言版本发生修改后,必须在**同一次提交**中同步其它语言版本
  - 缺失即违规
- 本任务**不**触发其他规范条款(仅改 README 表格 1 行的"用途"列)

## 任务设计要点(步骤 5 记录)

### 关键:本任务**触发/来源 = 审查改修**

按 `code-it` SKILL.md §步骤 5 + `code-review` SKILL.md §步骤 11,本任务的**全部输入**是 `review/T-009/RESULT.md`,**不读** `plan/REQ-00006/RESULT.md`(那是上游设计,本任务是修补,不是新设计)。

### review/T-009/RESULT.md 的关键内容(主要输入)

#### §2 问题清单
- **F-002**:中英 README `<code-publish>` 行 "用途"列措辞误导
  - 现状:zh "顺带在项目级创建 `assistants/qanda/` 目录" / en "also creates the project-level `assistants/qanda/` directory"
  - 问题:措辞隐含 `code-publish` "总会"创建 qanda/ 目录;但实际**仅在 qanda/ 不存在时**创建(FR-6.AC-6.1 + SKILL.md 步骤 2.5)
  - 修订:
    - zh → 「(首次调用时)在项目级创建 `assistants/qanda/` 目录(若已存在则跳过)」
    - en → "(on first call) creates the project-level `assistants/qanda/` directory if it does not yet exist"

#### §3 应当改修的文件
- 文件 1:`plugins/code-skills/README.md` L38 — zh 改
- 文件 2:`plugins/code-skills/README.en.md` L38 — en 改

#### §6 不需要做的(避免越界)
- **不**修改 SKILL.md (T-001 已是"已完成")
- **不**修改其他 10 个 `code-*` 技能 SKILL.md
- **不**修改 `plugins/code-skills/CLAUDE.md`
- **不**修改 `assistants/rules/` 下任何规范
- **不**修改 `plugins/code-skills/templates/` 下任何文件
- **不**添加新章节(`doc-conventions §规则 1` 0 触发:H2 数量不变)
- **不**修改表格的其他列(技能 / 读取 / 写入 / 下游)
- **不**调整表格行顺序

#### §4 验证手段
- `git diff` 验证 2 文件均只改 1 行(各 L38)
- 改后 grep 验证关键词:
  - zh:"首次调用时" + "若已存在则跳过" 同时出现
  - en:"on first call" + "if it does not yet exist" 同时出现
- 与 SKILL.md §"## 工作流程" 步骤 2.5 措辞对仗验证

### code/T-008/RESULT.md 的关键内容(关联原任务上下文)

- T-008 是 T-009 的关联原任务(已"已完成")
- T-008 在 L38 引入了 `<code-publish>` 行(2 个文件各 +1 行,git diff --stat: 2 files, 2 insertions)
- T-008 deviations.md 0 项偏离(本任务**不**继承 T-008 的任何偏离)
- T-008 验证清单:11/11 H2 对仗 + 5/5 表格列数 + 12/12 表格行数(本任务修订后**不能**破坏这些对仗)

## 开发过程

### 2026-06-04 18:10
- **操作**:验证 PLAN.md + 准备目录 + 推进状态
- **结果**:成功(T-009 存在,触发/来源=审查改修,前置任务 T-008 = `已完成` ✓)
- **状态推进**:PLAN.md 中 T-009 "待开始" → "进行中"

### 2026-06-04 18:11
- **操作**:读 `review/T-009/RESULT.md`(本任务的全部输入) + 读 `code/T-008/RESULT.md`(关联原任务上下文)
- **结果**:
  - 精确获取了 2 文件 L38 的"现状 → 应改为"映射
  - T-008 验证清单作为"不能破坏"的约束

### 2026-06-04 18:12
- **操作**:用 `Edit` 修订 `plugins/code-skills/README.md` L38
- **结果**:
  - 旧:「顺带在项目级创建 `assistants/qanda/` 目录」
  - 新:「(首次调用时)在项目级创建 `assistants/qanda/` 目录(若已存在则跳过)」
  - 1 行修改,**不**影响其他列(技能 / 读取 / 写入 / 下游)

### 2026-06-04 18:13
- **操作**:用 `Edit` 修订 `plugins/code-skills/README.en.md` L38
- **结果**:
  - 旧:"also creates the project-level `assistants/qanda/` directory"
  - 新:"(on first call) creates the project-level `assistants/qanda/` directory if it does not yet exist"
  - 1 行修改,**不**影响其他列

### 关键决策与权衡

#### 决策 IT-1:严格按 review/T-009/RESULT.md §6 "不需要做的"约束,不越界
- **选定**:**不**修改 SKILL.md / templates / 其他 10 技能 / 规则 / 其他 README 章节
- **理由**:
  - 本任务是"修补"性质的审查改修,**不是**新设计
  - review/T-009/RESULT.md §6 显式列出"不需要做的",严格遵守 = 防止 task 越界
- **依据**:`code-it` SKILL.md §步骤 5 关键 + `code-review` SKILL.md §步骤 11

#### 决策 IT-2:不修改 SKILL.md §2.5 "目的"段的"本需求顺带"措辞
- **选定**:**仅**改 README 的"用途"列(用户首次接触的位置),**不**改 SKILL.md §2.5
- **理由**:
  - SKILL.md §2.5 "**目的**"段写"本需求顺带"= "此为本需求一次性副作用",**语义正确**(对应 plan/REQ-00006 §2.3 末尾"顺带在项目级创建 `assistants/qanda/` 目录与 README.md")
  - README "用途"列写"顺带在项目级创建"= 隐含"每次运行都创建",**语义错误**
  - 两者虽都含"顺带"字样,但**语义不同**;**本任务仅修正错误者**,不牵连正确者
- **依据**:review/T-009/RESULT.md §6 "不修改 SKILL.md" + 最小变更原则

#### 决策 IT-3:同次 `git add` + `git commit`(用户后续操作,本任务不执行)
- **选定**:本任务的 2 文件改动在 1 次 `code-it` 调用中完成;**用户后续**整体 commit 时需同次提交
- **理由**:`doc-conventions §规则 1` 要求中英同次提交
- **依据**:`doc-conventions.md §规则 1`(强制)

#### 决策 IT-4:不实际跑 `git commit`(NFR-3)
- **选定**:仅 Edit 2 文件;`git commit` 留待用户整体 commit
- **理由**:NFR-3(不自动 commit)+ 沿用 T-001~T-008 实践
- **依据**:NFR-3

### 验证手段(本任务的"测试"等价物)

| 验证项 | 期望 | 实际 | 结论 |
| --- | --- | --- | --- |
| 2 文件 L38 均已修改(各 1 行) | ✓ | git diff --stat 显示 2 files, 2 insertions | ✓ |
| 改后 zh grep "首次调用时" + "若已存在则跳过" | ✓ | 2 词同时存在 | ✓ |
| 改后 en grep "on first call" + "if it does not yet exist" | ✓ | 2 词同时存在 | ✓ |
| 中英 H2 数量仍 11 / 11 | ✓ | grep 计数 11 / 11 | ✓ |
| 表格列数仍 5 / 5 | ✓ | grep 计数 5 / 5 | ✓ |
| 表格行数仍 12 / 12 | ✓ | grep 计数 12 / 12 | ✓ |
| 其他 10 既有 SKILL.md 0 改动 | ✓ | git diff --stat empty | ✓ |
| 其他规范文件 0 改动 | ✓ | git diff --stat empty | ✓ |
| SKILL.md 0 改动 | ✓ | git diff --stat empty | ✓ |

**结论**:**9 / 9 验证全部通过**,T-009 完成。

## 与 SKILL.md §2.5 的对仗验证(对仗但语义互补)

- SKILL.md §2.5 "**目的**":"本需求顺带在项目级创建 `assistants/qanda/` 骨架" — 表述"本需求一次性副作用"
- README.md L38 "**用途**"(改后):"(首次调用时)在项目级创建 `assistants/qanda/` 目录(若已存在则跳过)" — 表述"运行时行为"
- 两者**互补**:
  - SKILL.md 解释"为什么这个需求会有 qanda/"(= 本需求副作用)
  - README 解释"用户使用本技能时,会发生什么"(= 首次创建 + 后续跳过)
- **互不冲突**;本次修订**仅**改 README,**不**改 SKILL.md

## 关联任务与提交

- **关联原任务**:T-008(双 README 同步)— 本任务对其引入的"code-publish"行做措辞修订
- **Git 提交**:**未提交**(NFR-3);由用户审阅后整体 commit(连同 REQ-00006 的其他改动)
- **建议 commit message**(若用户单独 commit T-009):
  ```
  docs(code-publish): refine README "code-publish" row wording (F-002)
  
  Clarify that qanda/ is created on first call only, not on
  every code-publish invocation. Aligns with SKILL.md step
  2.5 (QandaScaffolder) behavior.
  
  Co-synced zh + en (doc-conventions §规则 1).
  ```
