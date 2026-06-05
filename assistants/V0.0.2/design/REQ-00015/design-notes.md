# 设计笔记 — REQ-00015
更新时间:2026-06-06 09:00
版本:V0.0.2

## 关键设计问题清单

| # | 问题 | 决策 | 依据 |
| --- | --- | --- | --- |
| Q-1 | code-merge 是编排者还是执行者? | **执行者**(直接调 git 命令,不调其他 `code-*`) | NFR-1(不产生过程文件)+ FR-3(直接 git fetch/merge) |
| Q-2 | code-merge 是否调用其他子技能? | **不调**(0 派生) | NFR-1(无过程文件)+ FR-4(LLM 智能合并是本技能内部能力,非派生任务) |
| Q-3 | code-merge 的输入是什么? | **0 输入** + 1 可选参 `<branch>` | FR-3(默认 origin/main) + FR-8(退出码 0/非 0) |
| Q-4 | code-merge 的输出是什么? | **stdout 报告**(无 RESULT.md) | NFR-1(不产生结果文件) + AC-6.3 |
| Q-5 | LLM 智能合并的"智能"如何实现? | **Claude Code 模型层现场决策**(在 SKILL.md 描述算法,执行时由 LLM 现场分析双侧内容) | NFR-9(不嵌入 git 命令模板) + 既有 11 个 `code-*` 风格 |
| Q-6 | worktree 模式如何识别? | `git rev-parse --git-common-dir` ≠ `git rev-parse --git-dir` | FR-1(用户原话) + 既有 git worktree 工具约定 |
| Q-7 | 默认目标分支是哪个? | `main`(可通过环境变量 `CODE_MERGE_TARGET` 覆盖) | FR-7 + clarifications.md 第 1 轮问题 2 锁定 git merge |
| Q-8 | merge 时用 `--no-ff` 还是 `--ff-only`? | `--no-ff`(强制产生 merge commit,保留历史) | NFR-7 + AC-5.1 |
| Q-9 | 看板自检发现不一致是否修复? | **不修复**(只打印报告,留给 `code-rule`) | NFR-2 + AC-4.4 |
| Q-10 | 二进制文件冲突如何处理? | **留 unmerged + 提示用户**(不阻塞) | NFR-3 + AC-3.3 |

## 候选方案与决策

### 候选 A:`code-merge` 走"主分支提交"模式(已选定,本设计)
- **核心思路**:本技能直接调 git 命令,工作流由 SKILL.md 描述,执行时由 LLM 现场拼装具体命令
- **优势**:
  - 0 派生(符合 NFR-1)
  - 与既有 11 个 `code-*` 风格一致
  - 对 git 版本变化鲁棒(NFR-9)
- **劣势**:
  - LLM 现场拼命令可能与用户预期有偏差
- **决策依据**:用户 clarifications.md 第 1 轮问题 1 锁定 LLM 智能合并

### 候选 B:`code-merge` 走"调用其他子技能"模式(已否决)
- **核心思路**:code-merge 拆分多个子步骤,每步调 `code-it` 实施
- **优势**:与 REQ-00007 code-auto 风格一致
- **劣势**:
  - 会产生 8+ 任务文件,违反 NFR-1(不产生过程文件)
  - 任务粒度过细,失去"一键合并"的意义
- **否决理由**:直接违反 NFR-1 强约束

### 候选 C:`code-merge` 走"SKILL.md 嵌入具体 git 命令"模式(已否决)
- **核心思路**:SKILL.md 写死每一步的 git 命令字符串
- **优势**:确定性高
- **劣势**:
  - 与 git 自身版本变化冲突(NFR-9)
  - 与既有 11 个 `code-*` 风格不一致
- **否决理由**:违反 NFR-9 + 既有 SKILL.md 风格

## 不变量清单(本设计严守)

| # | 描述 | 来源 |
| --- | --- | --- |
| INV-1 | `code-merge` **不**修改其他 11 个 `code-*` SKILL.md | NFR-5 |
| INV-2 | `code-merge` **不**触碰 `marketplace.json` 中除 `plugins[].skills` 数组追加外的其他字段 | NFR-6 |
| INV-3 | `code-merge` **不**触碰 `plugin.json` 任何字段(本技能新增不涉及子插件清单) | NFR-6 + 既有 11 个 `code-*` 风格 |
| INV-4 | `code-merge` 执行阶段**不**产生任何 `.md` 过程文件 / 结果文件(SKILL.md 在首次创建时产) | NFR-1 + AC-6.1~6.5 |
| INV-5 | `code-merge` **不**回滚 worktree 内已有 commit(`git merge --no-ff` 产生新 merge commit,**不**用 `--squash`) | NFR-7 + AC-5.1~5.3 |
| INV-6 | `code-merge` **不**自动 `git push` 到 origin / **不**自动 `git worktree remove` | NFR-10 + AC-1.4 |
| INV-7 | `code-merge` **不**实现 v1 follow-up 项(`--ff-only` / `--target` / 自动 PUSH / 自动清理 worktree) | NFR-10 + 7 项 v1 follow-up |
| INV-8 | `code-merge` 的 SKILL.md 描述工作流 + 算法,**不**嵌入具体 git 命令模板 | NFR-9 + 既有 11 个 `code-*` 风格 |
| INV-9 | `code-merge` **不**自动调 `code-publish` / `code-auto` / 任何子技能 | 职责分离 + NFR-7(Q-P7 锁定) |
| INV-10 | `code-merge` 在非 worktree 环境调用 → 立即报错退出(退出码非 0),**不**接受 `--no-worktree` 开关 | NFR-4 + AC-7.3 |

## 与既有规范的交叉验证
- ✅ `skill-conventions.md §规则 1`:新 SKILL.md frontmatter 必含 name + description(本设计 INV-1 保证)
- ✅ `module-conventions.md §规则 1`:本技能无新增资源(无 templates/ checklists/ guidelines)
- ✅ `marketplace-protocol.md §规则 1`:`marketplace.json` 追加 `./skills/code-merge`,**不**触碰其他字段(INV-2)
- ✅ `encoding-conventions.md §规则 1+3`:本技能不产出新编码(只读 `.current-version` 取版本号)
- ✅ `dashboard-conventions.md §规则 1`:FR-6 看板自检**复用**既有字段,**不**新增区段(不触发 3 文件同步)
- ✅ `commit-conventions.md`:占位,本设计沿用 V0.0.2 既有 `chore(<scope>): <description>` 模式
