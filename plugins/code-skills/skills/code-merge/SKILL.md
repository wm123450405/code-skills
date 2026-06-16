---
name: code-merge
description: Worktree 模式自动合并。在 git worktree 里开发完,本技能一键帮你把改动合回主干:提交未提交文件、拉取主干、LLM 智能解冲突(代码/文档/配置智能合并,看板数据按时间合并,二进制留给你处理)、看板上 5 区段自检,最后用 `git merge --no-ff` 合回 main 并出报告。不自动 push,也不清理 worktree,出问题用 Ctrl+C 中止时已 commit 不回滚。
---

# code-merge — Worktree 模式自动合并

## 目标

在 git worktree 模式下,把"worktree 内开发 → 主分支合回"流程**完全自动化**:
1. 提交 worktree 内所有未提交文件
2. 拉取并合并主干分支(默认 `origin/main`)
3. LLM 智能解决冲突(看板数据 / 代码 / 文档 / 配置 / 二进制)
4. 看板 5 区段自检
5. 用 `git merge --no-ff` 合回 main

**核心约束**(源自 `require/REQ-00015/RESULT.md`):
- **不**在 worktree 模式外运行(强约束,无 `--no-worktree` 开关)
- **不**产生过程文件 / 结果文件(SKILL.md 在首次创建时已产,执行阶段不再写 SKILL.md)
- **不**自动 `git push` / **不**自动 `git worktree remove`
- **不**回滚已 commit(commit 是 git 原子的)
- **不**调任何其他子技能(`code-auto` / `code-publish` / 任何 `code-*`)

## 适用场景

- 用户在 git worktree 中完成某条 REQ 的开发,需把 worktree 合回 main
- 用户在 worktree 中遇到合并冲突,希望 LLM 智能合并(看板数据 + 代码 + 文档)
- 合并后希望自动扫描 5 个看板区段,确保统计数据无矛盾

## 不适用

- **不在 worktree 中**(主工作区直接 `git merge` 即可,无需本技能)
- **v1 follow-up 项**(以下**不**在 v1 范围,留作 v2):
 - `--ff-only` 开关
 - `--target <branch>` 显式主分支参数(仅环境变量 `CODE_MERGE_TARGET`)
 - 自动 `git push` 到 origin
 - 自动 `git worktree remove` 清理
 - 跨多个 worktree 同时合并
 - 看板自检"自动修复统计行"(v1 仅打印报告,不修复)
 - `code-auto` 在自动循环完成后**自动**调用本技能
- 紧急线上修复(走 hotfix 流程,不走 worktree)
- 修改 11 个既有 `code-*` SKILL.md(本技能**零修改**既有技能)

## 工作目录约定(强制)

**版本工作空间**:`./assistants/<版本号>/`(由 `./assistants/.current-version` 决定)。
本技能的目录粒度是**单次执行**(1 次合并 = 1 个完整流程);**不创建**任何独立目录,所有产物由 git 自身管理。

```
./assistants/
├── rules/ # 项目级规范(跨版本共享,本技能只读)
├── .current-version # 当前激活版本标记(本技能只读)
└── <版本号>/
 ├── RESULT.md # 版本看板(本技能只读消费 + FR-6 扫描)
 ├── require/<需求编码>/ # (本技能不读不写)
 ├── design/<需求编码>/ # (本技能不读不写)
 ├── plan/<需求编码>/ # (本技能不读不写)
 ├── code/<任务编码>/ # (本技能不读不写)
 ├── test/<任务编码>/ # (本技能不读不写)
 └── review/<需求编码>/ # (本技能不读不写)
```

- 路径以**当前工作目录(CWD)**为基准
- 本技能**不修改** `./assistants/rules/` 下任何文件
- 本技能**不修改** `<版本号>/RESULT.md`(FR-6 仅**读** + **打印**自检报告,**不修改**任何字段)
- 本技能**不修改** 11 个既有 `code-*` SKILL.md
- 本技能**不**写 `assistants/<版本号>/code/<任务编码>/RESULT.md`(本技能无任务编码概念)
- **执行阶段不**写任何 `.md` 过程文件 / 结果文件(SKILL.md 是首次创建时产,执行阶段**不**再写)

## 输入

| 参数 | 类型 | 必填 | 约束 | 缺省行为 |
| --- | --- | --- | --- | --- |
| `<branch>` | string | 可选 | 单个分支名,可省略 `origin/` 前缀(自动补全) | 默认 `origin/main` |
| `CODE_MERGE_SCOPE` | env | 可选 | commit message 的 `<scope>` 段(沿用 V0.0.2 既有 `chore(<scope>): ...` 格式) | 默认 `worktree-merge` |
| `CODE_MERGE_TARGET` | env | 可选 | 合并目标主分支名 | 默认 `main` |

**参数解析**(在步骤 0 之后):
- 0 个非空参 → target = `origin/main`
- 1 个非空参 → target = `<参>`(若不以 `origin/` 开头则补全)
- 2+ 个非空参 → 报错并打印用法(退出码非 0,E-M8)

**示例**:
```bash
/code-merge # 默认合并 origin/main
/code-merge develop # 合并 origin/develop
/code-merge origin/develop # 合并 origin/develop(显式前缀)
/code-merge # + CODE_MERGE_SCOPE=my-scope(自定义 commit scope)
/code-merge # + CODE_MERGE_TARGET=develop(合并到 develop 而非 main)
```

## 输出

### 屏幕(stdout)输出

**3 段式**:

1. **进度日志**(每步一行,沿用 V0.0.2 既有 `code-*` 风格):
 ```
 === code-merge 启动 ===
 worktree 路径: <worktree-path>
 源分支: <worktree-branch>
 默认目标分支: origin/main
 [FR-1] 前置检查 ... ✓ 在 worktree 中 / ✗ dirty N 文件
 [FR-2] 提交 worktree 内文件 ...
 git add -A → ✓
 git commit -m "chore(worktree-merge): ..." → ✓ hash: <hash>
 [FR-3] 拉取并合并主干 ...
 git fetch origin → ✓
 git merge origin/main --no-ff → ✓ / ✗ CONFLICT
 [FR-4] 冲突解决(LLM 智能合并)...
 · <file-1>: 看板数据 → ✓ 保留双方 + 统计一致
 · <file-2>: 代码 → ✓ 智能合并
 · <file-3>: 二进制 → ✗ 需用户手动
 [FR-5] 再次确认提交状态 ...
 git status --porcelain → ✓ 干净 / ⚠ N unmerged
 [FR-6] 看板自检(5 区段)...
 · 需求清单: ✓ 13 行 (一致)
 · 概要设计清单: ✗ 表格 3 行 vs 统计 4 行
 · 详细设计与任务计划汇总: ✓ 9 行
 · 任务清单: ✓ 18 行
 · 缺陷清单: ✓ 0 行
 → ✓ 看板自检通过 / ⚠ 1 个不一致(非阻塞)
 [FR-7] 合并 worktree 到 main ...
 git checkout main → ✓
 git merge <worktree-branch> --no-ff -m "..." → ✓ hash: <hash>
 [FR-8] 退出与清理 ...
 ```

2. **完成报告**(终态,详 §FR-8)

3. **磁盘输出**:**0 文件**(NFR-1 强约束)

### 退出码

| 退出码 | 含义 | 触发场景 |
| --- | --- | --- |
| 0 | 正常完成 | 全部 FR 走通(含非阻塞警告) |
| 非 0 | 致命错误 | E-M1 / E-M2 / E-M3 / E-M4 / E-M5 / E-M8 / E-M10 / E-M12 |
| 130 | 用户中止 | Ctrl+C(E-M11) |

---

## 工作流程

### 步骤 0 — 版本上下文检测(强制前置)

1. 读 `./assistants/.current-version` → 记为 `<版本号>`
2. 文件不存在 → 立即停下,提示"未找到 .current-version,请先调 /code-version"

> **注意**:本技能**不**做步骤 0a `git pull`(NFR-4 强约束:worktree 模式无 upstream 拉取语义)
> 若用户在主分支跑本技能,FR-1 会立即报错(E-M1),不会污染 worktree

### 步骤 0.5 — 解析主干参数

```
function parseTarget(args):
 if len(args) == 0: return "origin/main" // 默认
 if len(args) == 1:
 branch = args[0]
 if not branch.startswith("origin/"):
 branch = "origin/" + branch // 自动补全
 return branch
 if len(args) >= 2:
 print "✗ 参数过多(最多 1 个),用法: /code-merge [branch]"
 exit(非 0) // E-M8
```

### 步骤 FR-1 — worktree 模式识别 + 前置检查

**目标**:确认在 worktree 中 + 检查工作区状态

**算法**:
```
function FR1_preCheck():
 common_dir = exec("git rev-parse --git-common-dir")
 git_dir = exec("git rev-parse --git-dir")

 if common_dir == git_dir:
 print "✗ 不在 worktree 中"
 print " 请先执行: git worktree add <path> -b <branch>"
 exit(非 0) // E-M1

 status = exec("git status --porcelain")
 if status 非空:
 return DIRTY // 走 FR-2
 else:
 return CLEAN // 跳过 FR-2,走 FR-3
```

**worktree 识别原理**:
- 在主工作区:`git-common-dir == git-dir`
- 在 worktree:`git-common-dir != git-dir`

### 步骤 FR-2 — 提交 worktree 内未提交文件

**目标**:把所有 dirty 文件 commit,避免 `git merge` 时混入

**算法**:
```
function FR2_commit():
 scope = env.CODE_MERGE_SCOPE ?? "worktree-merge"
 exec("git add -A")

 staged = exec("git diff --cached --stat")
 if staged 为空:
 print "✓ 无变更,跳过 commit"
 return

 target = parseTarget(args) // 来自步骤 0.5
 message = f"chore({scope}): merge worktree into {target}"
 result = exec(f'git commit -m "{message}"')
 if result.exit_code != 0:
 print f"✗ commit 失败: {result.stderr}"
 print " 请手动处理(pre-commit hook 或其他)"
 exit(非 0) // E-M5

 hash = exec("git log -1 --format=%H")
 print f"✓ commit 完成, hash: {hash}"
```

**关键决策**:
- scope 默认 `worktree-merge`(可通过 `CODE_MERGE_SCOPE` 覆盖)
- 空提交跳过(避免无意义的 merge commit)
- pre-commit hook 失败**不**重试(用户手动决策)

### 步骤 FR-3 — 拉取并合并主干分支

**目标**:拉取 `origin/main`(或指定分支)最新代码,合并到当前 worktree 分支

**算法**:
```
function FR3_fetchMerge(target):
 // 1. fetch origin(拉取远端最新)
 fetch_result = exec("git fetch origin")
 if fetch_result.exit_code != 0:
 print f"⚠ git fetch 失败: {fetch_result.stderr}" // 不阻塞
 // 允许本地 fallback(直接合并本地分支)

 // 2. merge --no-ff(强制产生 merge commit,保留历史)
 merge_result = exec(f"git merge {target} --no-ff")
 if merge_result.exit_code == 0:
 return SUCCESS // 走 FR-5
 if "CONFLICT" in merge_result.stderr or "Merge conflict" in merge_result.stderr:
 return CONFLICT // 走 FR-4
 // 其他错误(致命)
 print f"✗ git merge 失败: {merge_result.stderr}"
 exit(非 0)
```

**关键决策**:
- `--no-ff` 强制产生 merge commit(NFR-7 + AC-5.1)
- git fetch 失败**不**阻塞(AC-8.4 允许本地 fallback)
- 冲突时退出码非 0 但**不**退出(走 FR-4 解决)

### 步骤 FR-4 — 冲突解决(LLM 智能合并)

**目标**:逐文件分析,LLM 现场拼装合并策略

#### 4.1 看板数据冲突(最高优先级)

**触发条件**:冲突文件路径匹配以下任一(用 `Glob` 预扫描):
- `assistants/V<版本>/RESULT.md`
- `assistants/V<版本>/require/REQ-*/RESULT.md`
- `assistants/V<版本>/plan/REQ-*/PLAN.md`
- `assistants/V<版本>/plan/REQ-*/RESULT.md`
- `assistants/V<版本>/design/REQ-*/RESULT.md`

**合并规则**(LLM 现场实施):
1. **保留双方数据** — 不删除任何一侧的记录
2. **保持顺序一致** — 按时间戳(创建时间列)升序;时间戳相同按需求/任务编号升序
3. **统计数据最终一致** — 合并后必须重新计算区段"统计"行
4. **完成后**:`git add <file>` 标记已解决

#### 4.2 其他类型文件(逐文件分析)

**触发条件**:非 4.1 列出的冲突文件

| 文件类型 | 处理方式 |
| --- | --- |
| 代码文件(.py / .ts / .go / .rs / .java 等) | LLM 读双侧 + 智能合并 + 优先保留双侧独有逻辑 |
| 配置文件(.json / .yaml / .toml) | 优先保留双侧字段并集(去重) |
| 文档文件(.md) | 同 4.1 看板数据规则(保留双方 + 顺序) |
| 二进制文件(.png / .pdf / .mp4 / .mp3 / .zip) | **不**自动合并,留 unmerged + 提示用户(E-M6) |

**算法**:
```
function resolveConflict(file):
 ext = file_extension(file)

 if ext in BINARY_EXTENSIONS: // .png .pdf .mp4 .mp3 .zip
 print f"⚠ {file} 是二进制文件,需用户手动处理"
 return UNRESOLVED // 留 unmerged,不阻塞

 ours = read(file, ref="HEAD")
 theirs = read(file, ref=target)

 if file in DASHBOARD_FILES:
 merged = llm_smart_merge(ours, theirs, kind="dashboard")
 elif ext in CODE_EXTENSIONS:
 merged = llm_smart_merge(ours, theirs, kind="code")
 elif ext in CONFIG_EXTENSIONS:
 merged = llm_smart_merge(ours, theirs, kind="config")
 elif ext in DOC_EXTENSIONS:
 merged = llm_smart_merge(ours, theirs, kind="doc")
 else:
 print f"⚠ {file} 未知扩展名,按 doc 规则处理"
 merged = llm_smart_merge(ours, theirs, kind="doc")

 if llm_cannot_resolve:
 print f"✗ {file} 冲突无法自动解决,需用户手动处理"
 return UNRESOLVED

 write(file, merged)
 exec(f"git add {file}")
 print f"✓ {file} 智能合并完成"
```

#### 4.3 失败兜底
- 严重无法解决 → 留 unmerged + 提示用户
- **不**自动 `git add`(避免半成品入库)
- **不阻塞**整体流程(继续处理其他文件)
- 最终 `git status` 报告所有 unmerged 文件清单

### 步骤 FR-5 — 再次确认所有文件已提交

**目标**:确保 merge 后所有变更都进 git,无 dirty state

**算法**:
```
function FR5_verifyCommit():
 status = exec("git status --porcelain")
 unmerged = exec("git diff --name-only --diff-filter=U")

 if status 非空 且 非 unmerged:
 // 有未提交文件(非冲突),自动 commit
 exec("git add -A")
 scope = env.CODE_MERGE_SCOPE ?? "worktree-merge"
 exec(f'git commit -m "chore({scope}): post-merge cleanup"')
 print "✓ post-merge cleanup 已 commit"

 if unmerged 非空:
 print f"⚠ 仍有 {len(unmerged)} 个 unmerged 文件: {unmerged}" // E-M9
 // 不阻塞,走 FR-6 + FR-7(由用户后续手动处理)

 if status 为空:
 print "✓ 所有文件已提交,准备合回主分支"
```

### 步骤 FR-6 — 看板自检(5 区段,全自动)

**目标**:合并完成后扫描 5 个看板区段,确保统计数据无矛盾

**算法**(复用 `code-dashboard` 算法 1 + 算法 5):
```
function FR6_dashboardCheck():
 version = read("./assistants/.current-version")
 result_md = read(f"assistants/{version}/RESULT.md")

 sections = [
 "需求清单",
 "概要设计清单",
 "详细设计与任务计划汇总",
 "任务清单",
 "缺陷清单"
 ]

 all_consistent = true
 for section in sections:
 // 算法 1:定位区段
 section_start = find_section(result_md, f"^## {section}$")
 table_rows = count_table_rows(result_md, section_start) // ^\| .* \|$

 // 算法 5:提取统计行
 stat_value = extract_stat(result_md, section) // **统计**:N / 总数:N

 if table_rows == stat_value:
 print f"✓ {section}: {table_rows} 行 (一致)"
 else:
 print f"✗ {section}: 表格 {table_rows} 行 vs 统计 {stat_value} 行" // E-M7
 all_consistent = false

 if all_consistent:
 print "✓ 看板自检通过"
 else:
 print "⚠ 看板自检发现问题(非阻塞)" // NFR-2
```

**关键决策**:
- 自检发现不一致**不**修复(NFR-2 + AC-4.4)— 留 `code-rule` 处理
- 自检结果**不**影响退出码(NFR-2)
- 复用既有 5 区段,**不**新增区段 → **不**触发 `dashboard-conventions §规则 1` 同步(REQ-00013 INV-5 协同)
- 自检过程**只读** `RESULT.md`,**不**修改任何字段(本技能严守职责边界)

### 步骤 FR-7 — 合并 worktree 到主分支

**目标**:把 worktree 分支合回 main(默认),产生 merge commit

**算法**:
```
function FR7_mergeToMain():
 target = env.CODE_MERGE_TARGET ?? "main"

 // 1. 切到主分支
 checkout = exec(f"git checkout {target}")
 if checkout.exit_code != 0:
 print f"✗ git checkout {target} 失败: {checkout.stderr}" // E-M2(main dirty)
 exit(非 0)

 // 2. 合并 worktree 分支(--no-ff,默认 merge 消息格式)
 worktree_branch = exec("git rev-parse --abbrev-ref HEAD", cwd=worktree_path)
 merge_msg = f"Merge branch '{worktree_branch}' into {target}" // git 默认格式
 merge = exec(f"git merge {worktree_branch} --no-ff -m \"{merge_msg}\"")
 if merge.exit_code != 0:
 print f"✗ git merge 失败: {merge.stderr}"
 exit(非 0) // 走 FR-4 理论不应再冲突

 hash = exec("git log -1 --format=%H")
 print f"✓ code-merge 完成, merge commit: {hash}"
```

**关键决策**:
- `--no-ff` 强制产生 merge commit(NFR-7 + AC-5.1)
- merge message 走 git 默认格式(用户在 clarifications 阶段锁定)
- main 分支 dirty → **不**自动 stash(用户决策)

### 步骤 FR-8 — 退出与清理

**最终报告**(stdout):
```
=== code-merge 完成 ===
 · worktree: <worktree-path>
 · 源分支: <worktree-branch>
 · 目标分支: <target>
 · merge commit: <hash>
 · 看板自检: ✓ 通过 / ⚠ N 个不一致(非阻塞)
 · 退出码: 0
```

**清理(0 操作)**:
- **不**自动 `git push` 到 origin
- **不**自动 `git worktree remove`
- **不**写任何过程/结果文件(SKILL.md 已在首次创建时产)

---

## 边界与异常

| ID | 场景 | 触发条件 | 行为 | 退出码 |
| --- | --- | --- | --- | --- |
| **E-M1** | 不在 worktree | `git-common-dir == git-dir` | 打印 `✗ code-merge 必须在 git worktree 中运行`,提示 `git worktree add` | 非 0 |
| **E-M2** | main 分支 dirty(FR-7) | `git status` 在 main 上非空 | 打印 `✗ main 分支 dirty, 请先 git stash 或 git commit`,**不**自动处理 | 非 0 |
| **E-M3** | worktree 路径不存在 | (保留,本 v1 不传路径参数,留作未来) | 打印 `✗ worktree 路径 <path> 不存在` | 非 0 |
| **E-M4** | 主干分支不存在 | `git rev-parse --verify origin/main` 失败 | 打印 `✗ 主干分支 <branch> 不存在, 请检查远端` | 非 0 |
| **E-M5** | pre-commit hook 失败 | FR-2 `git commit` 退出码非 0 | 打印 stderr,**不**重试,提示用户手动 | 非 0 |
| **E-M6** | 二进制文件冲突 | FR-4 识别为二进制 | 留 unmerged + 提示用户手动,**不阻塞** | 0(警告) |
| **E-M7** | 看板自检不一致 | FR-6 5 区段中任一不一致 | 打印详细 `✗` 行,**不修复**,不阻塞 | 0(警告) |
| **E-M8** | 参数错 | 用户传 2+ 个非空参 | 打印用法 + 退出 | 非 0 |
| **E-M9** | 主干分支冲突后无法合并 | FR-4 全 unmerged | 打印 `✗ 仍有 N 个 unmerged`,提示用户手动 | 0(警告) |
| **E-M10** | git 命令不可用 | `git --version` 失败 | 打印 `✗ 未检测到 git` | 非 0 |
| **E-M11** | Ctrl+C 中止 | 用户在执行中按 Ctrl+C | 立即停止,**不**回滚已 commit;打印 `⛔ code-merge 中止` | 130(SIGINT) |
| **E-M12** | worktree 已被 prune | `git worktree list` 中无当前 path | 打印 `✗ 当前 worktree 已被 prune` | 非 0 |

**统一错误信息风格**(NFR-8):
- 显式前缀 `✗`(失败)/ `✓`(成功)/ `⚠`(警告)
- 包含失败的具体 git 命令 + 退出码 + 关键 stderr 摘要
- 给出**可操作**的下一步建议

---

## 关联需求

- **REQ-00004**(`/code-dashboard`):FR-6 看板自检复用其"算法 1 + 算法 5"(5 区段表格行计数)
- **REQ-00005**(首步拉取 + 末步提交):FR-2 / FR-5 commit 格式 `chore(<scope>): ...` 同源
- **REQ-00006**(`/code-publish`):FR-6 自检**不**阻塞 publish 流程(同源"非阻塞警告"语义)
- **REQ-00007**(`/code-auto`):`code-auto` **不**自动调本技能(职责分离)
- **REQ-00009**:本技能不调任何单测相关技能(本仓库纯文档,无可测载体)
- **REQ-00010**(`/code-it`):本技能不调 `code-it`(本技能无任务编码概念,纯 CLI 操作)
- **REQ-00013**(6 技能"编号+标题"显示):FR-6 看板自检**不**触发 `dashboard-conventions §规则 1` 3 处同步(严守 INV-5)
- **REQ-00017**(拆任务约束):本 SKILL.md 是"功能级"文档,无任务编码概念,**不**触发 REQ-00017 拆任务约束

---

## 工具使用约定

- **Bash 工具**:执行 git 命令(FR-1~FR-7 全部 git 操作)
- **Read 工具**:读 `.current-version` / `RESULT.md` / 冲突文件双方内容(FR-6 + FR-4)
- **Grep 工具**:解析 RESULT.md 5 区段(FR-6 锚点定位)
- **Glob 工具**:扫描看板数据冲突文件(FR-4.1 预扫描)
- **Write 工具**:**0 使用**(执行阶段**不**写任何文件,NFR-1 严守)
- **Edit 工具**:**0 使用**(同上)
- **Skill 工具**:**0 使用**(本技能**不**调任何子技能,NFR-1 + INV-9 严守)

---

## 不要做的事

- 不要在没有 `.current-version` 的情况下继续(步骤 0 强制)
- 不要在主工作区(非 worktree)中运行本技能(E-M1 立即报错)
- 不要自动 `git push` 到 origin(NFR-10 + 职责分离)
- 不要自动 `git worktree remove`(NFR-10 + 职责分离)
- 不要回滚已 commit 的状态(commit 是 git 原子的)
- 不要写任何过程文件 / 结果文件(NFR-1 强约束)
- 不要调任何其他 `code-*` 子技能(INV-9 严守)
- 不要自动 `code-publish` / `code-auto` / 任何子技能
- 不要修改 11 个既有 `code-*` SKILL.md(INV-1 严守)
- 不要修改 `marketplace.json` 既有字段(INV-2 严守)
- 不要修改 `plugin.json`(INV-3 严守)
- 不要修改 `./assistants/rules/` 13 份规范(INV-4 严守)
- 不要用 `--squash` 合并(NFR-7 + INV-5 严守,必须用 `--no-ff`)
- 不要实现 v1 follow-up 项(7 项,INV-7 严守,留作 v2):
 - `--ff-only` 开关
 - `--target <branch>` 显式主分支参数
 - 自动 `git push`
 - 自动 `git worktree remove`
 - 跨多个 worktree 同时合并
 - 看板自检"自动修复统计行"
 - `code-auto` 自动调本技能
- 不要在 SKILL.md 中嵌入具体 git 命令模板(NFR-9 + INV-8 严守)
- 不要接受 `--no-worktree` 开关(INV-10 严守)
- 不要在异常 / 中止时尝试 flush 任何文件(NFR-1 + AC-6 严守)

---

## 变更记录

| 时间 | 版本 | 变更摘要 | 变更人 |
| --- | --- | --- | --- |
| 2026-06-06 09:20 | v1 | 初始创建:8 FR + 10 NFR + 12 边界 E-M1~M12 + 10 项 INV 严守。范围:新增第 12 个 `code-*` 技能 `code-merge`,在 git worktree 模式下自动执行 FR-1 → FR-2 → FR-3 → FR-4 → FR-5 → FR-6 → FR-7 → FR-8,含 LLM 智能合并冲突解决(看板数据保留双方 + 按时间戳排序 + 统计行重新计算;代码 / 配置 / 文档 LLM 智能合并;二进制留 unmerged) + 看板 5 区段自检(复用既有字段不修复) + `git merge --no-ff` 合回 main + **不**产生过程/结果文件(SKILL.md 必产) + **不**自动 push / **不**自动清理 worktree。`code-auto` 完成后**不**自动调本技能(职责分离) | wangmiao |
