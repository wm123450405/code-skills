# 开发日志 — TASK-REQ-00006-00001

开始时间:2026-06-04 17:26
版本:V0.0.2
任务标题:[新增] 写 `code-publish/SKILL.md`(7 模块工作流 + frontmatter)
触发/来源:需求新增

## 项目现状(步骤 6 记录)

- **项目类型**:Claude Code Marketplace 插件(`code-skills`),纯文档型
- **语言**:Markdown(SKILL.md / templates / 规范)+ JSON(marketplace.json / plugin.json)
- **运行时**:Claude Code 通过读取 `SKILL.md` 的 YAML frontmatter 触发技能
- **构建命令**:**无**(本仓库无 build / lint / test 工具链,纯文档)
- **运行命令**:**无**(技能不"运行",由 Claude Code 在用户调用时按自然语言指令执行)
- **测试命令**:**无**(纯文档无传统单元测试)
- **既有 10 技能**:`code-init` / `code-version` / `code-rule` / `code-require` / `code-design` / `code-plan` / `code-it` / `code-unit` / `code-fix` / `code-review`
- **新增 11 技能(本次)**:`code-publish`
- **SKILL.md 实现风格**(核对既有 10 技能,详步骤 6 探查):
  - YAML frontmatter:`name` + `description`(强制)
  - `# <技能名> — <副标题>`(H1)
  - `## 目标` / `## 适用场景` / `## 不适用` 三段式
  - `## 工作目录约定(强制)`(版本工作空间路径树)
  - `## 输入` / `## 输出` / `## 工具使用约定`
  - `## 工作流程`(步骤 0..N,每步独立小节)
  - `## 衔接` / `## 不要做的事`
- **既有 SKILL.md 篇幅**:`code-version` ~200 行,`code-design` ~400 行,`code-review` ~600 行,`code-fix` ~600 行
- **`code-design/SKILL.md` 风格**是 T-001 的**最接近参考**(因为 `code-publish` 与 `code-design`/`code-plan` 同为 "按需求" 技能;且 `code-design` 的 frontmatter 描述本身较长,本技能的 `description` 也很长)

## 项目级规范要点(步骤 4 记录)

- `./assistants/rules/skill-conventions.md` §规则 1:**强制**
  - `name` = 目录名(`code-publish`)
  - `description` = 完整非空自然语言(本技能 description 较长,需覆盖目标/适用场景/关键触发/不参与项等)
- `./assistants/rules/module-conventions.md` §规则 1(DEPRECATED 但沿用):**适用**
  - `SKILL.md` 在技能根目录
  - 资源(templates/ checklists/ guidelines/)在子目录
- `./assistants/rules/dashboard-conventions.md` §规则 1:**0 触发**(本技能不扩展看板字段)
- `./assistants/rules/doc-conventions.md` §规则 1 + §规则 2:**不直接适用**(T-001 不改 README,T-008 处理)
- 占位规范 6 个 / 不相关规范 3 个:不影响

## 任务设计要点(步骤 5 记录)

### PLAN.md §3 任务详情(T-001 摘要)

- **类型**:新增
- **触发/来源**:需求新增
- **目标**:创建 `code-publish` 技能的入口 SKILL.md,实现 7 模块工作流 + 完整 frontmatter
- **涉及文件**:新建 `plugins/code-skills/skills/code-publish/SKILL.md`
- **关键变更**:frontmatter(强制 2 字段)+ 7 个工作流步骤(版本上下文 / 前置检查 / 基线识别 / 手册生成 / qanda 骨架 / qanda 聚合 / 报告)+ 异常路径(E-1~E-10)
- **依据规范**:`skill-conventions.md §规则 1`(frontmatter 强制)+ `module-conventions.md §规则 1`(SKILL.md 在根)
- **不依赖 review/**(本任务是 `需求新增` 而非 `审查改修`)

### 详细设计 §4 模块 1~7(本任务的主依据)

T-001 在 SKILL.md 中**同时实现 7 个逻辑模块**:
- 模块 1:SKILL.md 入口自身
- 模块 2:PreflightChecker(看板 3 区段解析)
- 模块 3:BaselineDetector(字典序最小)
- 模块 4:ManualBuilder(写 publish/ 3 份手册)
- 模块 5:QandaScaffolder(创建 qanda/ 骨架)
- 模块 6:QandaAggregator(聚合 qanda/*.md)
- 模块 7:ReportFormatter(报告 4 种场景)

### 详细设计 §5 算法 1~4(伪代码已在 design-notes.md §2)

### 详细设计 §8 异常处理(E-1~E-10 + DD-7 退出行为)

### 关键决策与权衡

#### 决策 IT-1:frontmatter description 的写法
- **选定**:沿用 `code-design/SKILL.md` 的长 description 风格(目标 + 适用场景 + 关键触发 + 关键约束 + 上下游)
- **理由**:本技能的 description 需覆盖"前置检查 + 3 份手册 + qanda 骨架 + 不自动 commit"等多要素;短 description 不够
- **依据**:`skill-conventions.md §规则 1`(description 需完整自然语言)

#### 决策 IT-2:章节顺序与既有 10 技能对齐
- **选定**:严格按 `code-version` / `code-design` / `code-fix` / `code-review` 的章节顺序(目标 / 适用场景 / 不适用 / 工作目录约定 / 输入 / 输出 / 工具使用约定 / 工作流程 / 衔接 / 不要做的事)
- **理由**:用户(含 AI 触发决策)已习惯此顺序;漂移会增加认知成本
- **依据**:无规范强制;但与所有 10 技能对齐 = 零现状偏离

#### 决策 IT-3:步骤 2.0 ~ 2.6 的子编号方案
- **选定**:步骤 0(版本上下文)→ 步骤 1(前置检查)→ 步骤 2.0(基线识别)→ 步骤 2(手册生成)→ 步骤 2.5(qanda 骨架)→ 步骤 2.6(qanda 聚合)→ 步骤 3(报告)
- **理由**:
  - 步骤 2.0 是步骤 2 的前置(必须先判定基线才能决定是否生成 UPDATE.md)
  - 步骤 2.5 / 2.6 是步骤 2 的"附加"(qanda 骨架可失败不阻塞,聚合是 Q&A.md 的内容渲染)
  - 这种"半步编号"与 `code-review` 等既有技能在 `## 工作流程` 中混用"步骤 X.Y"一致
- **依据**:无规范强制

#### 决策 IT-4:每个工具调用的明示
- **选定**:每步中显式写"`Bash: mkdir -p ...`" / "`Read: ...`" / "`Write: ...`" / "`Glob: ...`"(与既有 SKILL.md 风格一致)
- **理由**:让 Claude 知道"用什么工具";"不暗示"会让 Claude 自行决定
- **依据**:既有 10 技能的章节内均显式说明工具调用

#### 决策 IT-5:错误退出的"不阻塞 vs 立即退出"二元行为
- **选定**:
  - **不阻塞**:`qanda/` 骨架创建失败(FR-7.AC-7.4)
  - **立即退出**:前置检查不通过 / publish/ 写入失败(无 .current-version)
  - **模仿既有**:复制 `code-version` 步骤 0 的"无 .current-version → 提示 → 退出"模式
- **依据**:detail design `risk-analysis.md §1` + needs §9

#### 决策 IT-6:报告模板放哪
- **选定**:**不放**在 SKILL.md 内(过长),而是把 4 种报告模板放在 SKILL.md 的"## 步骤 3:报告"小节中(用 fenced code block 展示),让 Claude 在执行时直接渲染
- **理由**:SKILL.md 本身就是给 Claude 看的"指令集";模板放 SKILL.md 内 = Claude 必读
- **不放在 templates/**:因为 templates/ 是"静态文档"(publish/ 下生成的);报告是"运行时 stdout",生命周期不同
- **依据**:无规范

## 开发过程

### 2026-06-04 17:26
- **操作**:验证上游 + 解析任务输入
- **目的**:确认 V0.0.2 + PLAN.md 存在 + T-001 存在
- **结果**:成功(V0.0.2 / PLAN.md 已就绪 / T-001 触发/来源=需求新增)
- **状态推进**:PLAN.md 中 T-001 "待开始" → "进行中"

### 2026-06-04 17:27
- **操作**:与用户确认"前置任务 T-002~T-006 未完成"是否继续
- **用户回答**:T-001 是"当前应该第一个任务,不存在前置任务,按照顺序它应该就是第一个"
- **结果**:继续 T-001(用户显式重新组织任务顺序,SKILL.md 中模板路径以"路径字符串"形式引用即可,文件存在性由 T-002~T-006 后续保障)

### 2026-06-04 17:28
- **操作**:读 4 个有效规范文件 + `code-design/SKILL.md`(风格参考)
- **目的**:核对 frontmatter / 章节结构 / 工具调用模式
- **结果**:成功
- **关键发现**:
  - `code-design/SKILL.md` description 长度 ~600 字符;本技能 description 应在 800-1000 字符(覆盖 5+ 关键点)
  - 所有 10 技能都严格按相同章节顺序

### 2026-06-04 17:30
- **操作**:写 `plugins/code-skills/skills/code-publish/SKILL.md`
- **目的**:实现 7 模块工作流 + 4 报告模板 + 异常路径
- **结果**:成功
- **文件大小**:~510 行(预计;待写完后核实)
- **frontmatter 自检**:
  - `name: code-publish` ✓ (与目录名一致)
  - `description` 完整非空非占位 ✓
