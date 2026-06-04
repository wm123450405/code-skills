# 改修要求 — TASK-REQ-00006-00009

## 1. 任务信息

- **任务编码**:`TASK-REQ-00006-00009`
- **类型**:修改
- **触发/来源**:审查改修
- **触发时间**:2026-06-04 18:09
- **严重程度**:必须改
- **关联原任务**:`TASK-REQ-00006-00008`(双 README 同步)
- **来源评审**:`./assistants/V0.0.2/review/REQ-00006/REVIEW-REPORT.md` §F-002

## 2. 问题清单

### F-002:中英 README `<code-publish>` 行 "用途" 列措辞易误导(必须改)

- **位置**:
  - `plugins/code-skills/README.md` L38
  - `plugins/code-skills/README.en.md` L38
- **类别**:规范遵循 + 一致性
- **严重程度**:必须改(轻微措辞)
- **现状**:
  - zh L38 "用途"列含:「顺带在项目级创建 `assistants/qanda/` 目录」
  - en L38 "Purpose"列含:"also creates the project-level `assistants/qanda/` directory"
- **问题**:
  - 措辞隐含 `code-publish` "总会"创建 qanda/ 目录;但实际**仅在 qanda/ 不存在时**创建(FR-6.AC-6.1 + SKILL.md 步骤 2.5)
  - 若 qanda/ 已存在,本技能不重复创建 README.md(沿用既有)
  - 现有措辞"顺带" + "also creates" 误导用户认为:每次运行 code-publish 都会创建 qanda/,即使已经存在
- **应改为**:

#### zh 修改
- **当前**:`顺带在项目级创建 \`assistants/qanda/\` 目录`
- **改为**:`(首次调用时)在项目级创建 \`assistants/qanda/\` 目录(若已存在则跳过)`

#### en 修改
- **当前**:`also creates the project-level \`assistants/qanda/\` directory`
- **改为**:`(on first call) creates the project-level \`assistants/qanda/\` directory if it does not yet exist`

## 3. 应当改修的文件

### 文件 1:`plugins/code-skills/README.md`

- **现状**:L38 "用途"列:「顺带在项目级创建 `assistants/qanda/` 目录」
- **应改为**:「(首次调用时)在项目级创建 `assistants/qanda/` 目录(若已存在则跳过)」
- **理由**:与 SKILL.md 步骤 2.5 QandaScaffolder 行为一致(FR-6.AC-6.1 + FR-7.AC-7.4)
- **关联依据**:SKILL.md §"## 工作流程" 步骤 2.5 + 设计文档 data-changes.md §4 模块 5

### 文件 2:`plugins/code-skills/README.en.md`

- **现状**:L38 "Purpose"列:"also creates the project-level `assistants/qanda/` directory"
- **应改为**:"(on first call) creates the project-level `assistants/qanda/` directory if it does not yet exist"
- **理由**:与文件 1 同步(`doc-conventions §规则 1` 要求中英 H2 数量 + 顺序 + 语义完全对仗)
- **关联依据**:`doc-conventions.md §规则 1`

## 4. 验证手段

- `git diff` 验证 2 文件均只改 1 行(各 L38)
- 改后 grep 验证:
  - zh:"首次调用时" + "若已存在则跳过" 同时出现
  - en:"on first call" + "if it does not yet exist" 同时出现
- 与 SKILL.md §"## 工作流程" 步骤 2.5 措辞对仗验证

## 5. 关联依据(规范 / 设计 / 需求)

- **规范**:`doc-conventions.md §规则 1`(README 中英对仗 + 同步)
- **设计**:`plan/REQ-00006/RESULT.md §4 模块 5` QandaScaffolder(仅首次创建)+ `data-changes.md §4 模块 5`
- **需求**:FR-6 顺带创建 qanda/ + FR-7.AC-7.4(qanda/ 已存在不阻塞)

## 6. 不需要做的(避免 code-it 越界)

- **不**修改 SKILL.md (T-001 已是"已完成"任务,本任务仅修 README)
- **不**修改其他 10 个 `code-*` 技能的 SKILL.md
- **不**修改 `plugins/code-skills/CLAUDE.md`
- **不**修改 `assistants/rules/` 下任何规范
- **不**修改 `plugins/code-skills/templates/` 下任何文件
- **不**添加新章节(`doc-conventions §规则 1` 0 触发:H2 数量不变)
- **不**修改表格的其他列(技能 / 读取 / 写入 / 下游)
- **不**调整表格行顺序

## 7. 完成定义

- 2 个文件 L38 均已修改
- 改后通过 4 项验证(2 项 git diff + 2 项 grep)
- `git status` 显示 2 文件 M
- `code-review` 后,本任务 RESULT.md 由 code-it 更新"已完成"
- 由用户整体 commit

## 8. 提交规范

- 严格遵循 NFR-3(不自动 commit)
- 留 dirty tree 由用户整体 commit(连同 REQ-00006 的其他改动)
- 建议 commit message:
  ```
  docs(code-publish): refine README "code-publish" row wording
  
  F-002: Clarify that qanda/ is created on first call only,
  not on every code-publish invocation. Aligns with SKILL.md
  step 2.5 (QandaScaffolder) behavior.
  
  Co-synced zh + en (doc-conventions §规则 1).
  ```
