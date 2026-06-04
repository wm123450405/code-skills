# 关联需求 — REQ-00005

更新时间:2026-06-04 13:32

## 扫描范围
- 同版本:`./assistants/V0.0.2/require/`
  - REQ-00004(本需求之前唯一)
- 跨版本:`./assistants/V0.0.1/require/`、`./assistants/V0.0.0/`

## 关联需求清单

### REQ-00004(版本:V0.0.2)— `/code-dashboard` 开发看板技能
- **关联点**:
  - **范围并列**:`code-require` / `code-design` / `code-plan` 属于"管道前 3 步",`code-dashboard` 属于"读取型"附属技能
  - **首次新增技能的样板**:REQ-00004 建立了"新增一个 `code-*` 技能的标准边界" — 继承 REQ-00003 的 FR-9 精神(不修改 marketplace.json / plugin.json / 其他 SKILL.md frontmatter)
- **对本需求的影响**:
  - **正交性**:`code-dashboard` 纯只读,本需求纯修改型,两者不冲突
  - **依赖**:本需求若 commit 末尾"自动提交"会**间接**修改 `.current-version` 等**非本需求**关心的文件;但 `code-dashboard` 的 NFR-7"幂等 / 纯只读"不受影响
  - **建议**:本需求的"NFR-6 不修改其他技能"应**显式列出** `code-dashboard` 边界不变
- **来源**:`./assistants/V0.0.2/require/REQ-00004/RESULT.md` §NFR-6 / §NFR-7

### REQ-00003(版本:V0.0.1)— 优化 `code-rule` 技能
- **关联点**:
  - **同源上下游**:REQ-00003 确立了"项目级规范由 `code-rule` 维护"的制度
  - **`commit-conventions.md` 占位**:REQ-00003 在 `REQ-00003-002` 中创建了 6 个占位文件,其中 `commit-conventions.md` 规则 1 是"待添加"
  - **本需求落地的"commit 行为"恰是 `commit-conventions.md` 应承载的内容** — 形成天然的下游沉淀
- **对本需求的影响**:
  - **规范消费**:本需求**不**直接写 `commit-conventions.md` 规则(由 `code-rule` 技能后续落地);但本需求**应**遵循"commit 信息格式 = `<type>(<scope>): <subject>`"这一传统(从 V0.0.1 历史 commit 推断)
  - **决策点(待澄清)**:本需求是否**触发** `code-rule` 落地 `commit-conventions.md` 规则?见 clarifications.md Q-5
  - **设计阶段任务**:可派生"用 `code-rule` 沉淀 commit 规则"为 `code-plan` 阶段的**审查派生任务**(类似 REQ-00001-005 / REQ-00002-009)
- **来源**:`./assistants/V0.0.1/require/REQ-00003/RESULT.md` FR-2 / FR-3 + `./assistants/rules/commit-conventions.md`(占位)

### REQ-00002(版本:V0.0.1)— 编码格式统一
- **关联点**:
  - **本需求的"末尾提交"产出的 commit 信息**会引用 `REQ-NNNNN` / `TASK-...` 编码,需遵循 `encoding-conventions.md` 权威源
  - **`.current-version` 切换后,版本号格式**遵循既有规范(本仓库用 `V0.0.0` / `V0.0.1` / `V0.0.2` 字面)
- **对本需求的影响**:
  - **commit 信息模板建议**:`chore(<scope>): REQ-NNNNN <subject>` 或 `feat(<scope>): <summary> (REQ-NNNNN)`,scope 选用 `code-require` / `code-design` / `code-plan`
  - **`<subject>` 长度**:与 `commit-conventions` 既有 1 行(50 字符内)习惯一致
- **来源**:`./assistants/V0.0.1/require/REQ-00002/RESULT.md` + `./assistants/rules/encoding-conventions.md`

### REQ-00001(版本:V0.0.1)— Marketplace 改名落地
- **关联点**(间接):
  - REQ-00001 是 V0.0.1 第一个 commit 落地的需求,建立了"每个任务显式 commit"的实践(单 commit,doc-conventions §规则 1 中英同次提交)
  - **现状**:`code-it` 显式 `git add` + `git commit`(见 V0.0.1 看板"执行的开发命令记录"段)
- **对本需求的影响**:
  - **关键设计冲突**:本需求要求"末尾自动 commit",但**`code-it` 已在内部**显式 commit;若两个 commit 流程共存,会产生"空 commit"或"双 commit"
  - **决策点(待澄清)**:本需求的"末尾提交"是否**取代** `code-it` 内部的显式 commit?见 clarifications.md Q-6(新增)
  - **设计阶段必决**:`code-it` 内部 commit 与本需求末尾 commit 的**边界**必须明确 — 推荐"只允许一处提交",选择"末尾统一"或"`code-it` 内部保留"
- **来源**:`./assistants/V0.0.1/require/REQ-00001/RESULT.md` + `./assistants/V0.0.1/RESULT.md` "执行的开发命令记录"段

### REQ-00001-005 / REQ-00002-009(版本:V0.0.1)— 审查派生任务
- **关联点**(设计模式):
  - 这 2 个任务展示了"review 派生的"无 commit 任务"模式 — review 发现 → 派生 → 实施 → 留 dirty tree 给用户
  - 本需求的"末尾自动 commit"若**强制** commit,会与该模式冲突
- **对本需求的影响**:
  - **设计例外**:若本需求在"末尾 commit"步骤中,检测到**无任何文件变更**,应**跳过** commit(不产生空 commit)
  - **可演进**:本需求 v1 不必彻底替代 review 派生任务的"留 dirty tree"模式,只对"正常新增文件 / 修改文件"做末尾 commit
- **来源**:`./assistants/V0.0.1/RESULT.md` "派生任务记录" + "执行的开发命令记录" 段

## 跨需求聚合(供 `code-design` 阶段权衡)

| 维度 | 涉及需求 | 共性 | 处理建议 |
| --- | --- | --- | --- |
| 边界继承 | REQ-00003 / REQ-00004 | 都不修改 marketplace.json / plugin.json / 其他 SKILL.md frontmatter | 本需求**只**改 3 个 SKILL.md 正文 + 必要时改 CLAUDE.md/README(由 `code-rule` Type B 沉淀) |
| 规范沉淀 | REQ-00003 | `commit-conventions.md` 是占位 | 本需求**间接**需要该规则,但**不**在本需求中直接写;留作 v2 或派生任务 |
| commit 实践 | REQ-00001 | "每个任务显式 commit" | 本需求是**反模式** — 需明确"末尾 commit"与"`code-it` 内部 commit"的边界 |
| dirty tree | REQ-00001-005 / REQ-00002-009 | review 派生任务可能"留 dirty tree" | 本需求在"无文件变更"时跳过 commit(不产生空 commit) |

## V0.0.0 EXISTING-* 任务
- 7 个 `code-*` 技能的 SKILL.md 整体结构在 V0.0.0 已固定
- 本需求不修改 frontmatter,只改正文(对齐 `skill-conventions.md §规则 1` 精神)
