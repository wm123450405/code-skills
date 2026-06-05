# 改修总结 — TASK-REQ-00015-00001

## 1. 任务信息
- **任务编码**:`TASK-REQ-00015-00001`
- **任务标题**:[新增] 写 `code-merge/SKILL.md`(frontmatter `name: code-merge` + `description: <完整>` + 12 章节正文 + 8 FR 伪代码 + E-M1~M12 边界异常 + 状态机 Mermaid)
- **任务类型**:**新增**
- **触发/来源**:**详细设计**(REQ-00017 强约束)
- **来源 PLAN.md**:`./assistants/V0.0.2/plan/REQ-00015/PLAN.md` §任务总览 + §2 任务详情
- **所属需求**:REQ-00015(新增 `/code-merge` 技能,worktree 模式下自动合并)
- **所属版本**:V0.0.2
- **执行时间**:2026-06-06 09:20
- **执行人**:wangmiao

## 2. 改修内容总览

### 新增文件(1 个)
- ✅ `plugins/code-skills/skills/code-merge/SKILL.md`(580 行,**新增第 12 个 `code-*` 技能**)

### 修改文件(0 个)
- **0**(本任务只新增,不修改任何既有文件)

### 删除文件(0 个)
- **0**

## 3. 详细改动

### 3.1 `plugins/code-skills/skills/code-merge/SKILL.md`(新增)

**frontmatter**(字符级对齐 `skill-conventions §规则 1`):
- `name: code-merge`(kebab-case,与目录名严格一致)
- `description: <完整>`(~600 字符,涵盖触发场景 + 8 FR 工作流 + 5 项强约束)

**12 章节正文**:
1. `## 目标` — 5 句话讲清"做什么、何时用"
2. `## 适用场景` — 3 类典型场景(worktree 模式 / 冲突解决 / 看板自检)
3. `## 不适用` — 7 项 v1 follow-up(严守 INV-7)
4. `## 工作目录约定`(强制)
5. `## 输入` — 1 个位置参 + 2 个环境变量(完整参数表)
6. `## 输出` — 3 段式 stdout 报告 + 退出码语义
7. `## 工作流程` — 步骤 0 + FR-1~FR-8(8 段伪代码 + 状态机 Mermaid)
8. `## 边界与异常` — E-M1~M12 表格(12 场景全覆盖)
9. `## 关联需求` — 7 项(REQ-00004/05/06/07/09/10/13)
10. `## 工具使用约定` — 6 工具(Bash/Read/Grep/Glob/Write=0/Edit=0/Skill=0)
11. `## 不要做的事` — 18 项(INV-1~10 子集 + 5 项子约束)
12. `## 变更记录` — v1 首版 1 条

**关键算法嵌入**(对齐概要设计 §3 + 详细设计 §4):
- FR-1:`git rev-parse --git-common-dir ≠ --git-dir` worktree 识别
- FR-2:`chore(<scope>): merge worktree into <target>` commit 格式
- FR-3:`git fetch origin` + `git merge <target> --no-ff`
- FR-4:LLM 智能合并(看板数据保留双方 + 顺序 + 统计一致 / 代码 / 配置 / 文档 / 二进制留 unmerged)
- FR-5:`post-merge cleanup` commit
- FR-6:5 区段看板自检(复用 `code-dashboard` 算法 1+5,**只读不修复**)
- FR-7:`git checkout main` + `git merge <worktree-branch> --no-ff`
- FR-8:完成报告(0 文件清理)

**状态机 Mermaid**(在 §7 工作流末尾):
- 步骤 0 → FR-1 → FR-2 → FR-3 → FR-4(条件)→ FR-5 → FR-6 → FR-7 → FR-8

**stdout 报告模板**(在 §6 输出 + §7 工作流):
```
=== code-merge 启动 ===
worktree 路径: <worktree-path>
源分支: <worktree-branch>
默认目标分支: origin/main
[FR-1] 前置检查 ... ✓ 在 worktree 中 / ✗ dirty N 文件
[FR-2] 提交 worktree 内文件 ...
  ...
[FR-8] 退出与清理 ...
  ✓ code-merge 完成
    · worktree: <path>
    · 源分支: <branch>
    · 目标分支: main
    · merge commit: <hash>
    · 看板自检: ✓ 通过 / ⚠ N 个不一致(非阻塞)
    · 退出码: 0
```

**E-M1~M12 边界异常表**(在 §8 边界与异常):
- Markdown 表格,12 行,4 列(ID / 场景 / 触发条件 / 行为 / 退出码)
- 涵盖致命(非 0)8 项 + 警告(0)3 项 + 中止(130)1 项

**"不要做的事"小节**(严守 INV-1~10 + NFR-1/7/9/10):
- 18 项禁止操作,显式列出,便于未来读 SKILL.md 的开发者快速了解约束
- 包含"不调任何子技能"(INV-9)、"不写任何文件"(NFR-1)、"不用 --squash"(NFR-7)、"不嵌入 git 命令模板"(NFR-9)

## 4. 关键决策与权衡

- **frontmatter description 长度**:~600 字符(详细但完整,涵盖触发场景 + 8 FR 流程 + 5 项强约束)。选择详细是因为 Claude Code 模型层需要从 description 决定是否触发本技能。
- **工作流章节顺序**:FR-1 → FR-2 → ... → FR-8(与概要设计 §3 + 详细设计 §4 顺序一致,便于交叉验证)
- **E-M 表**:用 Markdown 表格(与既有 11 个 `code-*` 风格一致,便于 Read)
- **"不要做的事"小节**:10 项 INV 全部显式列出(INV-1~10 子集)+ 5 项子约束,便于未来读 SKILL.md 的开发者快速了解约束
- **变更记录**:v1 首版 1 条,后续用户在增量更新时追加
- **行数 580**:略低于 600~800 预估上限(因 frontmatter description 详细程度刚好,无需填充),完全合理

## 5. 偏离设计/规范的地方

**0 偏离**(详 `deviations.md`):
- 0 偏离概要设计(8 FR + 10 NFR + 10 AC + 10 INV 100% 沿用)
- 0 偏离详细设计(PLAN.md 任务详情 100% 实施)
- 0 偏离项目级规范(13 份规范全部只读引用,0 违反)
- 0 用户授权的偏离(无)
- 0 任务范围扩展(严守 T-001 边界)

## 6. 验证结果

详 `compile-and-run.md` + `test-results.md`。

### 静态自检(替代编译/启动)
- ✅ SKILL.md frontmatter 字符级校验通过
- ✅ 12 章节锚点 Grep 自检通过
- ✅ 关键 token Grep 自检通过
- ✅ INV-5(不 --squash):0 命中
- ✅ INV-7(不实现 v1 follow-up):0 命中
- ✅ INV-8(SKILL.md 不嵌入 git 命令模板):0 命中
- ✅ INV-9(不调子技能):0 命中
- ✅ INV-10(worktree 强约束):0 命中

**8/8 通过 — 0 失败 / 0 警告 / 0 修复**

### 测试结果
- 测试状态:**不适用**(纯文档 + 仓库无可测载体)
- 真正可发布:**✅ 是**(开发=已完成 ∧ 测试=不适用)

## 7. 已知问题/未完成项

**0 已知问题 / 0 未完成项**:
- 本任务 100% 沿用概要设计 + 详细设计 + 项目级规范
- 0 偏离 / 0 冲突 / 0 授权

## 8. 关联任务与提交

- **关联原任务**:**无**(本任务是新增,**不**是审查改修)
- **依赖任务**:**无**(T-001 是本计划的**第 1 个**任务,无前置)
- **后续任务**:
  - T-002 依赖 T-001(本任务)→ 改 `marketplace.json` 追加 `./skills/code-merge`
  - T-003 依赖 T-001 → 改中英 README 同步追加 1 行
  - T-004 依赖 T-002 + T-003 → 同步看板 6 处
  - T-005 依赖 T-001 ~ T-004 → 10 项 INV 自检收尾
- **提交哈希**:`<TBD>`(由 `code-it` 末尾兜底提交时填入)
- **提交时间**:2026-06-06 09:25(预计)
- **代码改动行数**:+580 行(SKILL.md 全新),-0 行
