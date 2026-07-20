# 修复设计 — BUG-00009

## 1. 设计目标

让 `/code ver` 在版本切换完成后自动 git 兜底提交,与 `/code req` `/code fix` 的 DONE 阶段保持一致。

## 2. 修复范围

| 项 | 是否修改 |
| --- | --- |
| `references/ver/common.md` §3.5 验证与汇报 | ✓ 增加 git 兜底提交逻辑 |
| `plugins/.../SKILL.md` 中"ver"步骤 6B 描述 | ✓ 增加 git 操作说明 |
| `plugins/.../SKILL.md` 中"ver"步骤 0 描述 | × 保持 |
| 其他章节 | × 保持 |

注:本仓库的 SKILL.md 是 merge 到 plugins 目录的源;实际生效的是 `C:/Users/wm/.claude/plugins/cache/code-skills-marketplace/code-skills/0.0.2/skills/code/SKILL.md`。两份需要同步修改。

## 3. 修复方案

### 3.1 references/ver/common.md §3.5 改造

将原"验证与汇报"函数 `verifyAndReport(version)` 改造为:

```
function verifyAndReport(version):
  // === 原有:验证与汇报 ===
  currentContent = Read("assistants/.current-version")
  assert currentContent.trim() == version

  lsOutput = Bash("ls assistants/{version}/")
  dashboard = Read("assistants/{version}/RESULT.md")

  // 汇报
  print("""
  ✅ 当前激活版本: {version}
  ...
  """)

  // === 新增:执行兜底提交(强制,不可跳过) ===
  executeFallbackCommit(scope="ver")
```

新增 `executeFallbackCommit(scope)`:

```
function executeFallbackCommit(scope):
  // 1. 检查是否为 git 仓库
  revResult = Bash("git rev-parse --git-dir 2>/dev/null")
  if revResult.exitCode != 0:
    print("非 git 仓库,跳过提交")
    return

  // 2. 检查是否有变更
  statusResult = Bash("git status --porcelain")
  if statusResult.stdout.trim() == "":
    print("无文件变更,跳过提交")
    return

  // 3. 暂存所有变更
  Bash("git add -A")

  // 4. 生成 commit message
  // 格式: chore(<scope>): <版本切换摘要>
  scope = scope ?? "ver"
  currentVersion = Read("assistants/.current-version").trim()
  message = f"chore({scope}): 版本切换至 {currentVersion}"

  // 5. 确认后提交
  AskUserQuestion:
    检测到 {countChanges(statusResult.stdout)} 个文件变更,是否提交?
    A. 提交(推荐)
    B. 跳过(用户自行处理)

  if A:
    result = Bash(f'git commit -m "{message}"')
    if result.exitCode == 0:
      hash = Bash("git log -1 --format=%H").stdout.trim()
      print(f"✓ 已提交:{hash}")
    else:
      print(f"✗ commit 失败:{result.stderr}")
```

### 3.2 SKILL.md 同步

在 `/code ver` SKILL.md "步骤 6B — 验证与汇报"小节后追加:

```
**执行兜底提交**(强制,不可跳过):
- 执行 `Bash: git rev-parse --git-dir 2>/dev/null` → 非 git 仓库则输出"非 git 仓库,跳过提交"
- 执行 `Bash: git status --porcelain` → 输出为空则输出"无文件变更,跳过提交"
- 执行 `Bash: git add -A`
- 生成 commit message(格式:`chore(ver): 版本切换至 <版本号>`)
- `AskUserQuestion` 确认后执行 commit
```

## 4. 兼容性考虑

- 既有用户行为:`/code ver` 不再"自动静默切换",而是会触发 commit 确认弹窗
- 这与 `/code req` `/code fix` 的兜底提交行为一致
- 非 git 仓库场景已做兼容(跳过 commit,只做汇报)
- 无变更场景已做兼容(跳过 commit)

## 5. 风险评估

| 风险 | 影响 | 缓解 |
| --- | --- | --- |
| 用户期望非交互的 ver 切换 | 中 | 显式 AskUserQuestion 提示;用户可选"跳过" |
| 误提交不期望文件 | 中 | `git add -A` 与 req/fix 一致,沿用其行为 |
| plugins cache 中 SKILL.md 未生效 | 高 | 必须同步更新两份 SKILL.md(源 + cache) |

## 6. 验收标准

- AC-1: 执行 `/code ver V0.0.7`(创建新版本)后,`git status --porcelain` 为空(已提交)
- AC-2: 非 git 仓库场景下,ver 不报错,仅输出"非 git 仓库,跳过提交"
- AC-3: 无变更场景(如切换到当前版本)不触发 commit
- AC-4: commit message 格式为 `chore(ver): 版本切换至 <版本号>`
- AC-5: 用户在 AskUserQuestion 选"跳过"则不提交,屏幕输出跳过原因

## 7. 任务拆分(待 PLAN 阶段细化)

候选任务:
- TASK-001: 修改 references/ver/common.md §3.5,加入 executeFallbackCommit
- TASK-002: 修改 plugins/.../SKILL.md ver 子命令的步骤 6B,加入兜底提交说明
- TASK-003: 修改 CWD 根的 plugins/.../SKILL.md(若存在)
- TASK-004: 在 V0.0.6/RESULT.md 缺陷清单中追加"修复状态"(可选,留给 CHECK 阶段)

实际拆分在 PLAN 阶段定。
