# 改修总结 — TASK-REQ-00015-00003

## 1. 任务信息
- **任务编码**:`TASK-REQ-00015-00003`
- **任务标题**:[修改] 中英 README "主要能力" 段同步追加 1 行(实际定位 = "## 技能概览" 表格)
- **任务类型**:**修改**
- **触发/来源**:**详细设计**(REQ-00017 强约束)
- **来源 PLAN.md**:`./assistants/V0.0.2/plan/REQ-00015/PLAN.md` §任务总览 + §2 任务详情
- **所属需求**:REQ-00015(新增 `/code-merge` 技能,worktree 模式下自动合并)
- **所属版本**:V0.0.2
- **执行时间**:2026-06-06 09:40
- **执行人**:wangmiao

## 2. 改修内容总览

### 新增文件(0 个)
- **0**

### 修改文件(2 个)
- ✅ `plugins/code-skills/README.md` §"## 技能概览" 表格(`code-auto` 行后追加 1 行)
- ✅ `plugins/code-skills/README.en.md` §"## Skills Overview" 表格(`code-auto` 行后追加 1 行)

### 删除文件(0 个)
- **0**

## 3. 详细改动

### 3.1 `plugins/code-skills/README.md`(修改 +1 行)

**变更**:
```diff
@@ -38,6 +38,7 @@
 | [`code-publish`](skills/code-publish/SKILL.md) | 发布部署 ... | ... | ... | ... |
 | [`code-dashboard`](skills/code-dashboard/SKILL.md) | 开发看板(只读)— ... | ... | 屏幕输出,无文件 | ... |
 | [`code-auto`](skills/code-auto/SKILL.md) | 自动开发编排— ... | (用户输入 1 个需求内容) | `<版本>/require/<REQ>/auto-report.md`(完成时) | (一键从需求到代码 + 单测 + 评审全自动跑通) |
+| [`code-merge`](skills/code-merge/SKILL.md) | Worktree 模式自动合并— 仅在 git worktree 中运行;`git rev-parse --git-common-dir ≠ --git-dir` 自动识别;串行执行 8 FR:worktree 识别 + dirty commit → `git fetch origin` + `git merge <target> --no-ff` → LLM 智能解决冲突(看板数据保留双方 + 按时间戳排序 + 统计行重新计算;代码/配置/文档智能合并;二进制留 unmerged)→ 看板 5 区段自检(只读不修复)→ `git merge <worktree-branch> --no-ff` 合回 main;**不**产生过程/结果文件;**不**自动 `git push` / `git worktree remove`;**不**调任何子技能;worktree 强约束(无 `--no-worktree` 开关) | (worktree 内 dirty 文件) | (屏幕输出,无文件) | (把 worktree 内开发合回 main,`code-auto` 完成后**不**自动调本技能) |
 
 ## 工作流管道
```

**修改要点**:
- 追加位置:`code-auto` 行后(沿用 V0.0.2 既有"新技能追加在 code-auto 后"模式)
- 5 列格式:技能 / 用途 / 读取 / 写入 / 下游(与既有 11 行严格一致)
- 缩进:与既有 11 行严格一致
- **0 改其他段**(`## 安装` / `## 工作流管道` / `## 仓库结构` / `## 核心概念` / `## 使用说明` / `## 完整工作流程` / `## 命令参考` / `## 典型场景` / `## 速查表` / `## 详细文档` 全部不变)

### 3.2 `plugins/code-skills/README.en.md`(修改 +1 行)

**变更**:
```diff
@@ -38,6 +38,7 @@
 | [`code-publish`](skills/code-publish/SKILL.md) | Release & Deployment ... | ... | ... | ... |
 | [`code-dashboard`](skills/code-dashboard/SKILL.md) | Dev Dashboard (read-only)— ... | ... | (screen output, no files) | ... |
 | [`code-auto`](skills/code-auto/SKILL.md) | Automated Dev Orchestration — ... | (user input: 1 requirement description) | `<version>/require/<REQ>/auto-report.md` (on completion) | (one-shot: requirement → code + tests + review passed) |
+| [`code-merge`](skills/code-merge/SKILL.md) | Worktree-mode auto-merge — runs only inside a git worktree (`git rev-parse --git-common-dir ≠ --git-dir`); serially executes 8 FR: worktree detection + dirty commit → `git fetch origin` + `git merge <target> --no-ff` → LLM-smart conflict resolution (dashboard data: keep both sides + sort by timestamp + recompute stats; code/config/docs: smart merge; binary: leave unmerged) → dashboard 5-section self-check (read-only, never fix) → `git merge <worktree-branch> --no-ff` back to main; **never** produces process/result files; **never** auto-`git push` / `git worktree remove`; **never** invokes any sub-skill; worktree is a strict constraint (no `--no-worktree` switch) | (dirty files inside worktree) | (stdout report, no files) | (merge worktree development back to main; `code-auto` does **not** auto-invoke this skill) |
 
 ## Pipeline
```

**修改要点**:同中文 README(中英对仗,`doc-conventions §规则 1`)

## 4. 关键决策与权衡

- **追加位置**:`code-auto` 行后(沿用 V0.0.2 既有"新技能追加在 code-auto 后"模式,与 REQ-00007 同款)
- **格式**:5 列(技能 / 用途 / 读取 / 写入 / 下游)与既有 11 行严格对齐
- **中英对仗**:中英 README 各 +1 行,行顺序与中文版一致(`doc-conventions §规则 1` 严守)
- **不动其他段**:`## 安装` / `## 工作流管道` / `## 仓库结构` / `## 核心概念` / `## 使用说明` / `## 完整工作流程` / `## 命令参考` / `## 典型场景` / `## 速查表` / `## 详细文档` 全部不变
- **实际定位**:"主要能力" 段实际为"## 技能概览" 表格(本仓库 README 结构是表格形式,不是段落形式)— 通过 Read 全文确认,严守 code-it 步骤 8 强制"修改文件前重读最新内容"
- **不动详细文档列表**:严守 T-003 边界(PLAN.md 说"中英 README 各 +1 行" → 仅 +1 行,不扩展到详细文档列表,因本任务没说要扩展)

## 5. 偏离设计/规范的地方

**0 偏离**(详 `deviations.md`):
- 0 偏离概要设计
- 0 偏离详细设计(PLAN.md §2 任务详情 100% 实施)
- 0 偏离项目级规范(`doc-conventions §规则 1` 中英对仗 100% 满足)
- 0 用户授权的偏离
- 0 任务范围扩展(严守 T-003 边界:仅 +1 行,不扩展到其他段)

## 6. 验证结果

详 `compile-and-run.md` + `test-results.md`。

### 静态自检(替代编译/启动)
- ✅ 中英 README 各 +1 行(`git diff --stat` 校验)
- ✅ 中英对仗校验(`doc-conventions §规则 1`)
- ✅ 5 列格式与既有 11 行严格对齐
- ✅ 0 改其他段(锚点定位)
- ✅ 0 触发 `dashboard-conventions §规则 1` 3 处同步

**5/5 通过 — 0 失败 / 0 警告 / 0 修复**

### 测试结果
- 测试状态:**不适用**(纯文档 + 仓库无可测载体)
- 真正可发布:**✅ 是**(开发=已完成 ∧ 测试=不适用)

## 7. 已知问题/未完成项

**0 已知问题 / 0 未完成项**:
- 本任务 100% 沿用概要设计 + 详细设计 + 项目级规范
- 0 偏离 / 0 冲突 / 0 授权

## 8. 关联任务与提交

- **关联原任务**:**无**(本任务是修改,不是审查改修)
- **依赖任务**:T-001(已完成)→ 本任务才有意义(SKILL.md 存在 → README 引用才能让用户找到入口)
- **后续任务**:
  - T-004 依赖 T-002 + T-003(看板同步需全部完成后)
  - T-005 依赖 T-001 ~ T-004(自检需全部完成后)
- **提交哈希**:`<TBD>`(由 `code-it` 末尾兜底提交时填入)
- **提交时间**:2026-06-06 09:45(预计)
- **代码改动行数**:+2 行(中文 README + 英文 README 各 +1 行),-0 行
