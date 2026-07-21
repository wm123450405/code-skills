---
name: code-merge
description: git worktree 自动合回主干。仅首 token = `merge` 触发。仅在 git worktree 内运行,主工作区调用会立即报错(E-M1)。例:`/code merge`(合 origin/main)/ `/code merge develop`(合 origin/develop)。不自动 push / 不自动 remove worktree。
---

# `/code merge` — Worktree 模式自动合并

## 目标

在 git worktree 模式下,把"worktree 内开发 → 主分支合回"流程**完全自动化**:
1. 提交 worktree 内所有未提交文件
2. 拉取并合并主干分支(默认 `origin/main`)
3. LLM 智能解决冲突(看板数据 / 代码 / 文档 / 配置 / 二进制)
4. 看板 2 区段自检
5. 用 `git merge --no-ff` 合回 main

**核心约束**:
- **不**在 worktree 模式外运行(强约束,无 `--no-worktree` 开关)
- **不**产生过程文件 / 结果文件(SKILL.md 在首次创建时已产,执行阶段不再写 SKILL.md)
- **不**自动 `git push` / **不**自动 `git worktree remove`
- **不**回滚已 commit(commit 是 git 原子的)
- **不**调任何其他子技能(`/code ver` / `/code req` / 任何 `/code *`)

## 适用场景

- 用户在 git worktree 中完成某条 REQ 的开发,需把 worktree 合回 main
- 用户在 worktree 中遇到合并冲突,希望 LLM 智能合并
- 合并后希望自动扫描 2 个看板区段,确保统计数据无矛盾

## 不适用

- **不在 worktree 中**(主工作区直接 `git merge` 即可)
- **v1 follow-up 项**(留作 v2):`--ff-only` 开关、`--target <branch>`、自动 `git push`、自动 `git worktree remove`、跨多 worktree 同时合并、自检"自动修复"等
- 紧急线上修复(走 hotfix 流程)
- 修改既有 SKILL.md(本技能**零修改**)

## 工作目录约定(强制)

**版本工作空间**:`./assistants/<版本号>/`(由 `./assistants/.current-version` 决定)。
本技能的目录粒度是**单次执行**(1 次合并 = 1 个完整流程);**不创建**任何独立目录。

```
./assistants/
├── rules/                # 项目级规范(跨版本共享,本技能只读)
├── .current-version      # 当前激活版本标记(本技能只读)
└── <版本号>/
    ├── RESULT.md         # 版本看板(本技能只读消费 + FR-6 扫描)
    ├── req/<需求编码>/   # req 子命令产出(本技能只读)
    └── fix/<缺陷编码>/   # fix 子命令产出(本技能只读)
```

- 本技能**不修改** `./assistants/rules/` 下任何文件
- 本技能**不修改** `<版本号>/RESULT.md`(FR-6 仅**读** + **打印**自检报告)
- 本技能**不修改** 既有 SKILL.md
- 本技能**不**写 `assistants/<版本号>/req/` 或 `fix/` 下的任何文件
- **执行阶段不**写任何 `.md` 过程文件 / 结果文件

## 输入

| 参数 | 类型 | 必填 | 约束 | 缺省行为 |
| --- | --- | --- | --- | --- |
| `<branch>` | string | 可选 | 单个分支名,可省略 `origin/` 前缀(自动补全) | 默认 `origin/main` |
| `CODE_MERGE_SCOPE` | env | 可选 | commit message 的 `<scope>` 段 | 默认 `worktree-merge` |
| `CODE_MERGE_TARGET` | env | 可选 | 合并目标主分支名 | 默认 `main` |

**参数解析**(在步骤 0 之后):
- 0 个非空参 → target = `origin/main`
- 1 个非空参 → target = `<参>`(若不以 `origin/` 开头则补全)
- 2+ 个非空参 → 报错并打印用法(退出码非 0,E-M8)

**示例**:
```
/code merge                  # 默认合并 origin/main
/code merge develop          # 合并 origin/develop
/code merge origin/develop   # 显式前缀
+ CODE_MERGE_SCOPE=my-scope  # 自定义 commit scope
+ CODE_MERGE_TARGET=develop  # 合并到 develop 而非 main
```

## 输出

**3 段式**屏幕输出:

1. **进度日志**(每步一行)
```
=== code merge 启动 ===
worktree 路径: <worktree-path>
源分支: <worktree-branch>
默认目标分支: origin/main
[FR-1] 前置检查 ... ✓ 在 worktree 中 / ✗ dirty N 文件
[FR-2] 提交 worktree 内文件 ...
[FR-3] 拉取并合并主干 ...
[FR-4] 冲突解决(LLM 智能合并)...
[FR-5] 再次确认提交状态 ...
[FR-6] 看板自检(2 区段)...
[FR-7] 合并 worktree 到 main ...
[FR-8] 退出与清理 ...
```

2. **完成报告**(终态)

3. **磁盘输出**:**0 文件**(NFR-1 强约束)

## 退出码

| 退出码 | 含义 | 触发场景 |
| --- | --- | --- |
| 0 | 正常完成 | 全部 FR 走通(含非阻塞警告) |
| 非 0 | 致命错误 | E-M1/M2/M3/M4/M5/M8/M10/M12 |
| 130 | 用户中止 | Ctrl+C(E-M11) |

---

## 工作流程

### 步骤 0 — 版本上下文检测(强制前置)

1. 读 `./assistants/.current-version` → 记为 `<版本号>`
2. 文件不存在 → 立即停下,提示"未找到 .current-version,请先调 `/code ver`"

> **注意**:本技能**不**做步骤 0a `git pull`(NFR-4 强约束)

### 步骤 0.5 — 解析主干参数

```
function parseTarget(args):
 if len(args) == 0: return "origin/main"
 if len(args) == 1:
   branch = args[0]
   if not branch.startswith("origin/"):
     branch = "origin/" + branch
   return branch
 if len(args) >= 2:
   print "✗ 参数过多(最多 1 个),用法: /code merge [branch]"
   exit(非 0)  // E-M8
```

### 步骤 FR-1 — worktree 模式识别 + 前置检查

```
function FR1_preCheck():
 common_dir = exec("git rev-parse --git-common-dir")
 git_dir = exec("git rev-parse --git-dir")

 if common_dir == git_dir:
   print "✗ 不在 worktree 中"
   print " 请先执行: git worktree add <path> -b <branch>"
   exit(非 0)  // E-M1

 status = exec("git status --porcelain")
 if status 非空:
   return DIRTY  // 走 FR-2
 else:
   return CLEAN  // 跳过 FR-2,走 FR-3
```

### 步骤 FR-2 — 提交 worktree 内未提交文件

```
function FR2_commit():
 scope = env.CODE_MERGE_SCOPE ?? "worktree-merge"
 exec("git add -A")
 staged = exec("git diff --cached --stat")
 if staged 为空:
   print "✓ 无变更,跳过 commit"
   return
 target = parseTarget(args)
 message = f"chore({scope}): merge worktree into {target}"
 result = exec(f'git commit -m "{message}"')
 if result.exit_code != 0:
   print f"✗ commit 失败: {result.stderr}"
   exit(非 0)  // E-M5
 hash = exec("git log -1 --format=%H")
 print f"✓ commit 完成, hash: {hash}"
```

### 步骤 FR-3 — 拉取并合并主干分支

```
function FR3_fetchMerge(target):
 fetch_result = exec("git fetch origin")
 if fetch_result.exit_code != 0:
   print f"⚠ git fetch 失败: {fetch_result.stderr}"
 merge_result = exec(f"git merge {target} --no-ff")
 if merge_result.exit_code == 0:
   return SUCCESS
 if "CONFLICT" in merge_result.stderr:
   return CONFLICT
 print f"✗ git merge 失败: {merge_result.stderr}"
 exit(非 0)
```

### 步骤 FR-4 — 冲突解决(LLM 智能合并)

#### 4.1 看板数据冲突(最高优先级)

**触发条件**:冲突文件路径匹配 `assistants/V<版本>/RESULT.md` 或 `req/REQ-*/` / `fix/BUG-*/` 下关键文件。

**合并规则**(LLM 现场实施):
1. **保留双方数据** — 不删除任何一侧的记录
2. **保持顺序一致** — 按时间戳升序;时间戳相同按编号升序
3. **统计数据最终一致** — 合并后必须重新计算区段"统计"行
4. **完成后**:`git add <file>` 标记已解决

#### 4.2 其他类型文件(逐文件分析)

| 文件类型 | 处理方式 |
| --- | --- |
| 代码文件(.py / .ts / .go / .rs / .java 等) | LLM 读双侧 + 智能合并 + 优先保留双侧独有逻辑 |
| 配置文件(.json / .yaml / .toml) | 优先保留双侧字段并集(去重) |
| 文档文件(.md) | 同 4.1 看板数据规则 |
| 二进制文件(.png / .pdf / .mp4 / .mp3 / .zip) | **不**自动合并,留 unmerged + 提示用户(E-M6) |

#### 4.3 失败兜底

- 严重无法解决 → 留 unmerged + 提示用户
- **不**自动 `git add`(避免半成品入库)
- **不阻塞**整体流程

### 步骤 FR-5 — 再次确认所有文件已提交

```
function FR5_verifyCommit():
 status = exec("git status --porcelain")
 unmerged = exec("git diff --name-only --diff-filter=U")

 if status 非空 且 非 unmerged:
   exec("git add -A")
   scope = env.CODE_MERGE_SCOPE ?? "worktree-merge"
   exec(f'git commit -m "chore({scope}): post-merge cleanup"')
   print "✓ post-merge cleanup 已 commit"

 if unmerged 非空:
   print f"⚠ 仍有 {len(unmerged)} 个 unmerged 文件"

 if status 为空:
   print "✓ 所有文件已提交,准备合回主分支"
```

### 步骤 FR-6 — 看板自检(2 区段,全自动)

```
function FR6_dashboardCheck():
 version = read("./assistants/.current-version")
 result_md = read(f"assistants/{version}/RESULT.md")

 sections = ["需求清单", "缺陷清单"]

 all_consistent = true
 for section in sections:
   section_start = find_section(result_md, f"^## {section}$")
   table_rows = count_table_rows(result_md, section_start)
   stat_value = extract_stat(result_md, section)

   if table_rows == stat_value:
     print f"✓ {section}: {table_rows} 行 (一致)"
   else:
     print f"✗ {section}: 表格 {table_rows} 行 vs 统计 {stat_value} 行"
     all_consistent = false

 if all_consistent:
   print "✓ 看板自检通过"
 else:
   print "⚠ 看板自检发现问题(非阻塞)"
```

### 步骤 FR-7 — 合并 worktree 到主分支

```
function FR7_mergeToMain():
 target = env.CODE_MERGE_TARGET ?? "main"

 checkout = exec(f"git checkout {target}")
 if checkout.exit_code != 0:
   print f"✗ git checkout {target} 失败: {checkout.stderr}"
   exit(非 0)

 worktree_branch = exec("git rev-parse --abbrev-ref HEAD", cwd=worktree_path)
 merge_msg = f"Merge branch '{worktree_branch}' into {target}"
 merge = exec(f"git merge {worktree_branch} --no-ff -m \"{merge_msg}\"")
 if merge.exit_code != 0:
   print f"✗ git merge 失败: {merge.stderr}"
   exit(非 0)
```

### 步骤 FR-8 — 退出与清理

**最终报告**(stdout):
```
=== code merge 完成 ===
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
- **不**写任何过程/结果文件

---

## 边界与异常

| ID | 场景 | 触发条件 | 退出码 |
| --- | --- | --- | --- |
| E-M1 | 不在 worktree | `git-common-dir == git-dir` | 非 0 |
| E-M2 | main 分支 dirty | `git status` 在 main 上非空 | 非 0 |
| E-M3 | worktree 路径不存在 | (保留) | 非 0 |
| E-M4 | 主干分支不存在 | `git rev-parse --verify origin/main` 失败 | 非 0 |
| E-M5 | pre-commit hook 失败 | FR-2 `git commit` 退出码非 0 | 非 0 |
| E-M6 | 二进制文件冲突 | FR-4 识别为二进制 | 0(警告) |
| E-M7 | 看板自检不一致 | FR-6 2 区段中任一不一致 | 0(警告) |
| E-M8 | 参数错 | 用户传 2+ 个非空参 | 非 0 |
| E-M9 | 主干分支冲突后无法合并 | FR-4 全 unmerged | 0(警告) |
| E-M10 | git 命令不可用 | `git --version` 失败 | 非 0 |
| E-M11 | Ctrl+C 中止 | 用户在执行中按 Ctrl+C | 130 |
| E-M12 | worktree 已被 prune | `git worktree list` 中无当前 path | 非 0 |

---

## 工具使用约定

- **Bash 工具**:执行 git 命令
- **Read 工具**:读 `.current-version` / `RESULT.md` / 冲突文件双方内容
- **Grep 工具**:解析 RESULT.md 区段
- **Glob 工具**:扫描看板数据冲突文件;读取编码规范
- **Write 工具**:**0 使用**
- **Edit 工具**:**0 使用**
- **Skill 工具**:**0 使用**

---

## 衔接

- **下游**:无(本技能为终态)
- **上游**:`/code ver`(必须,提供激活版本);`/code req` 完成后**不**自动调本技能(职责分离)
- **横向**:`/code ver` 看板算法(FR-6 复用其"算法 1 + 算法 5")

## 不要做的事

- 不要在没有 `.current-version` 的情况下继续(步骤 0 强制)
- 不要在主工作区(非 worktree)中运行本技能(E-M1 立即报错)
- 不要自动 `git push` 到 origin
- 不要自动 `git worktree remove`
- 不要回滚已 commit 的状态
- 不要写任何过程文件 / 结果文件
- 不要调任何其他子技能(INV-9 严守)
- 不要自动 `/code ver --publish` / `/code req --auto` / 任何子技能
- 不要修改既有 SKILL.md
- 不要修改 `marketplace.json` 既有字段
- 不要修改 `plugin.json`
- 不要修改 `./assistants/rules/` 已有规范
- 不要用 `--squash` 合并(必须用 `--no-ff`)
- 不要实现 v1 follow-up 项(`--ff-only` / `--target` / 自动 push / 自动 remove / 跨多 worktree / 自检自动修复)
- 不要在 SKILL.md 中嵌入具体 git 命令模板
- 不要接受 `--no-worktree` 开关
- 不要在异常 / 中止时尝试 flush 任何文件
