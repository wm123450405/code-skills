# 澄清记录 — REQ-00005

更新时间:2026-06-04 13:33

## 2026-06-04 13:33(本轮)

### Q-1:版本不一致时的"上下文中"指代
- **问题**:拉取后远端 `.current-version` 与本地不一致时,应切到哪个版本?
- **选项**:
  - A. 询问用户从两个中选(推荐)— 默认推荐远端
  - B. 默认切换到远端 — 简单但可能丢失用户主动选择
  - C. 报错退出,不调 `code-version` — 需用户手动处理
- **用户回答**:A,询问用户从两个中选
- **影响**:RESULT.md §FR-2(`code-require` 专属子流程) §4 实现要点;§9 边界与异常 E-1

### Q-2:`git pull` 失败处理
- **问题**:`git pull` 冲突/网络失败时?
- **选项**:
  - A. 中断 + 报错退出(推荐)— 安全优先
  - B. 提示并继续(不中断)— 保留本地修改
  - C. 尝试快进/变基后重试
- **用户回答**:A,中断 + 报错退出
- **影响**:RESULT.md §FR-1 通用步骤;§9 边界与异常 E-2 / E-3 / E-4

### Q-3:commit message 生成
- **问题**:末尾提交步骤的 commit message 由谁生成?
- **选项**:
  - A. 技能自动生成,附预览让用户确认(推荐)
  - B. 技能自动生成不询问
  - C. `git add` 后留空让用户写
- **用户回答**:A,技能自动生成,附预览让用户确认
- **影响**:RESULT.md §FR-3(末尾提交);§7 交互逻辑;§8 数据(commit 模板字段)

### Q-4:`code-it` 与本需求末尾 commit 的边界
- **问题**:`code-it` 已显式 commit,与末尾自动 commit 冲突?
- **选项**:
  - A. 去掉 `code-it` 内部 commit,末尾统一(推荐)
  - B. 保留 `code-it` 内部 commit,本需求仅补充末尾提交
  - C. 二者共存,末尾 commit 跳过已 commit 的文件
- **用户回答**:B,保留 `code-it` 内部 commit,本需求**针对所有技能产生的过程文件、结果文件**统一在最后做一次完整提交,确保没有文件遗漏
- **影响**:RESULT.md §FR-3 末尾提交范围(只收"过程文件 + 结果文件"中**未**被 `code-it` 内部 commit 覆盖的部分);§5 关键定义"末尾兜底提交"边界
- **解读**:用户回答强调了"确保没有文件遗漏" — 即末尾提交是**兜底**性质,不是"取代"

### Q-5(本轮未结构化提问,默认采纳):`commit-conventions.md` 规则沉淀
- **问题**:本需求是否触发 `commit-conventions.md` 规则 1 的填充?
- **建议默认**:**不**直接在本需求中写规则(保持 `code-rule` 是规范唯一入口);在 `code-design` 阶段可派生"用 `code-rule` 沉淀 commit 规则"为后续 follow-up
- **状态**:采纳默认,不阻塞

## 用户原文笔误纠正(已在 materials-index.md §1 标注)
- `/code-desgin` → `/code-design`
- `/code-require` → `/code-require`
- 影响范围:**`code-require` / `code-design` / `code-plan` 三个技能**(对应"上游→中游→下游"管道的前 3 步)

## 待澄清 / 未决项(留作 follow-up)

### Q-6:`.gitignore` 与"不应提交的文件"
- **背景**:末尾兜底提交可能误把 `.DS_Store` / 编辑器临时文件 / `node_modules/` 等纳入
- **建议默认**:严格遵循项目根 `.gitignore`;若该文件不存在,采用 `.git status --porcelain` 全量纳入
- **状态**:采纳默认,不阻塞

### Q-7:本需求是否要在 `plugins/code-skills/CLAUDE.md` 的"AI 工作约定"小节追加
- **背景**:本需求会**改变 AI 协作者在调用 `code-require` / `code-design` / `code-plan` 时的行为**
- **建议默认**:**不**在 CLAUDE.md 追加(由用户在后续调 `code-rule` 沉淀);本需求**不**触发 `dashboard-conventions §规则 1`(因为 CLAUDE.md 不是看板字段)
- **状态**:采纳默认,不阻塞

### Q-8:末尾兜底提交时,`commit-conventions.md` 规则未填充(占位)如何处理
- **建议默认**:沿用 V0.0.1 实践(commit 信息格式 = `chore(<scope>): <subject>`,subject 含 `REQ-NNNNN` 引用);不阻塞 `commit-conventions` 规则填充
- **状态**:采纳默认,不阻塞
