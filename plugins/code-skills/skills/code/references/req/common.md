# 公共流程 — `/code req`

> 本文件为 `/code req` 子命令提供阶段无关的公共流程。始终加载。

## §1 版本检测(强制前置)

1. 读取 `./assistants/.current-version`
2. **文件不存在** → 立即停下,告知用户先调 `/code ver`
3. 读取内容,记为 `<版本号>`,后续所有路径用 `assistants/<版本号>/...`

## §2 PROCESS.md 恢复(断点续跑)

### 读取与解析

```
function resumeFromProcess(processMdPath):
  if not exists(processMdPath):
    return { resumeStage: "INIT", isNew: true }
  
  lines = readAllLines(processMdPath)
  lastLine = lines[lines.length - 1]
  stage = parseStage(lastLine)
  status = parseStatus(lastLine)
  
  if stage == "DONE":
    return { resumeStage: "DONE", isNew: false }
  
  if status == "完成":
    return { resumeStage: nextStage(stage), isNew: false }
  else:
    return { resumeStage: stage, isNew: false }
```

### 阶段顺序

```
INIT → REQUIRE → DESIGN → PLAN → CODING → CHECK → DONE
```

### 下一阶段

```
function nextStage(current):
  order = ["INIT", "REQUIRE", "DESIGN", "PLAN", "CODING", "CHECK", "DONE"]
  idx = order.indexOf(current)
  return idx >= 0 && idx < order.length - 1 ? order[idx + 1] : "DONE"
```

## §3 PROCESS.md 追加(强制)

> 追加式写入,不预读文件内容。每次阶段开始/完成时追加一行。

### 追加格式

```
| YYYY-MM-DD HH:mm | <阶段> | <状态:开始|完成|失败> | <摘要> |
```

### 追加命令

```bash
echo "| $(date '+%Y-%m-%d %H:%M') | <阶段> | <状态> | <摘要> |" >> PROCESS.md
```

### 摘要约定

- 阶段开始:简要描述本阶段目标
- 阶段完成:关键产出统计(如 FR 数量、模块数量、任务数量)
- 阶段失败:错误原因简述

## §4 阶段执行器

### 执行流程

> 三态确认模型:阶段边界确认(是否继续下一阶段)与阶段内内容确认(需求澄清/设计选型等)是正交关系。`--confirm` 仅控制阶段边界确认。

```
async function executeStage(stage, context, flags):
  // 0. 阶段前置校验(强制)
  if not preStageCheck(stage, context.reqDir):
    appendProcess(stage, "失败", "前置产出物缺失,退回上一阶段")
    return { status: "ROLLBACK", targetStage: previousStage(stage) }
  
  // 1. 追加 PROCESS.md 开始记录
  appendProcess(stage, "开始", stageDescriptions[stage].start)
  
  // 2. 执行阶段逻辑(阶段内内容确认不受 flags 影响,由各阶段 references 自行控制)
  result = await stageHandlers[stage](context)
  
  // 3. 追加 PROCESS.md 完成记录
  appendProcess(stage, "完成", result.summary)
  
  // 4. 阶段边界确认(三态)
  if flags.confirm:
    // --confirm 模式:增强确认
    // 4a. 提示产出物文件路径
    outputFiles = getStageOutputFiles(stage, context.dir)
    print("=== " + skillName + " --confirm: " + stage + " 阶段完成 ===")
    print(result.summary)
    print("")
    print("产出物文件:")
    for file in outputFiles:
      print("  - " + file)
    print("")
    print("你可以手动修改上述文件,完成后选择继续。")
    
    // 4b. 弹出确认(继续/中止)
    response = askUserQuestion("继续下一阶段?", [
      "A. 继续(重新读取产出物,获取最新修改,进入下一阶段)",
      "B. 中止(保存当前进度,退出)"
    ])
    
    if response == "B":
      appendProcess(stage, "中止", "用户在 --confirm 确认环节中止")
      return { status: "ABORTED" }
    
    // 4c. 重新读取产出物(获取用户最新修改)
    for file in outputFiles:
      reRead(file)  // 刷新内存中的内容,确保下一阶段使用用户修改后的版本
  
  else if flags.auto:
    // --auto 模式:自动继续
    print("[" + skillName + " --auto] " + stage + " 完成,自动继续")
  
  // else: 默认模式 — 自动继续,无输出
  
  return result
```

### 阶段前置校验

> 每个阶段执行前,必须校验上一阶段的产出物已存在。校验失败则自动退回上一阶段。

| 当前阶段 | 校验项 | 校验命令 | 校验失败处理 |
| --- | --- | --- | --- |
| DESIGN | `REQUIRE.md` 存在 | `test -f <reqDir>/REQUIRE.md` | 追加失败记录,退回到 REQUIRE 阶段 |
| PLAN | `DESIGN.md` 存在 | `test -f <reqDir>/DESIGN.md` | 追加失败记录,退回到 DESIGN 阶段 |
| CODING | `PLAN.md` 存在 | `test -f <reqDir>/PLAN.md` | 追加失败记录,退回到 PLAN 阶段 |
| CHECK | 所有 `TASK-*.md` 存在 | `Glob "<reqDir>/TASK-*.md"` | 追加失败记录,退回到 CODING 阶段 |

```
function preStageCheck(stage, reqDir):
  checks = {
    "DESIGN":  ["REQUIRE.md"],
    "PLAN":    ["DESIGN.md"],
    "CODING":  ["PLAN.md"],
    "CHECK":   ["TASK-*.md"]  // Glob 匹配,至少一个
  }
  if stage not in checks: return true  // INIT/REQUIRE/DONE 无需校验
  for item in checks[stage]:
    if item contains "*":
      if Glob(reqDir + "/" + item).length == 0: return false
    else:
      if not exists(reqDir + "/" + item): return false
  return true
```

### 三态确认模型

> 阶段边界确认(是否继续下一阶段)与阶段内内容确认(需求澄清/设计选型/任务拆分等)是**正交**关系。

| 模式 | 触发条件 | 阶段边界确认 | 阶段内内容确认 |
| --- | --- | --- | --- |
| --confirm | `--confirm` flag | 增强确认(路径提示+重读+继续/中止) | 正常触发(AskUserQuestion) |
| --auto | `--auto` flag | 自动继续(前缀输出) | 自动选推荐项(跳过 AskUserQuestion) |
| 默认 | 无 flag | 自动继续(无输出) | 正常触发(AskUserQuestion) |

**关键规则**:
- `--confirm` 与 `--auto` 互斥,同时传入报错退出
- 阶段内内容确认由各阶段 references 自行控制,不受阶段边界确认模式影响
- `--auto` 模式下所有 AskUserQuestion 自动选第一项(推荐项)

## §5 目录结构

### 需求路径

```
assistants/<版本号>/req/<REQ-NNNNN>/
├── REQUIRE.md          # 需求分析产出
├── DESIGN.md           # 软件设计产出
├── PLAN.md             # 任务排期产出
├── TASK-001.md         # 任务完成产出(每个任务一个)
├── TASK-002.md
├── CHECK.md            # 代码审查产出
├── PROCESS.md          # 执行进程(追加式)
└── LOG.md              # 过程记录(可选,非必要不记录)
```

### 缺陷路径(`/code fix` 复用)

```
assistants/<版本号>/fix/<BUG-NNNNN>/
├── BUG.md              # 缺陷登记产出
├── DESIGN.md           # 修复设计产出
├── PLAN.md             # 任务排期产出
├── TASK-001.md
├── CHECK.md
├── PROCESS.md
└── LOG.md
```

## §6 版本看板同步

### RESULT.md 格式(简化版)

```markdown
# 版本开发进度看板 — <版本号>

## 需求清单
| 需求编码 | 标题 | 进度文档 |
| --- | --- | --- |
| REQ-00001 | 用户登录 | [PROCESS.md](req/REQ-00001/PROCESS.md) |

## 缺陷清单
| 缺陷编号 | 标题 | 进度文档 |
| --- | --- | --- |
| BUG-00001 | 空指针崩溃 | [PROCESS.md](fix/BUG-00001/PROCESS.md) |
```

### 写入规则

- **仅在首次创建需求/缺陷时追加一行**到对应清单
- 各阶段完成时**不再改写**看板
- 进度通过 `PROCESS.md` 链接查看

## §7 交互确认

> 三态确认模型:阶段边界确认与阶段内内容确认是正交关系。本节定义阶段边界确认的行为。

### --confirm 模式(增强确认)

每个阶段完成后,弹出增强确认:

```
=== code req --confirm: <阶段名> 阶段完成 ===
<摘要统计>

产出物文件:
  - assistants/<版本号>/req/<REQ>/<文件名1>
  - assistants/<版本号>/req/<REQ>/<文件名2>

你可以手动修改上述文件,完成后选择:
A. 继续(重新读取产出物,获取最新修改,进入下一阶段)
B. 中止(保存当前进度,退出)
```

**确认后行为**:
- 选 A(继续):重新读取所有产出物文件(获取用户最新修改),进入下一阶段
- 选 B(中止):追加 PROCESS.md `| <时间> | <阶段> | 中止 | 用户在 --confirm 确认环节中止 |`,退出

### --auto 模式

- 阶段边界自动继续,屏幕输出前缀
- 阶段内内容确认自动选推荐项

### 默认模式(无 flag)

- 阶段边界自动继续,无输出
- 阶段内内容确认正常触发(AskUserQuestion)

### 阶段内内容确认

> 阶段内内容确认(需求澄清、设计选型、任务拆分、审查发现等)由各阶段 references 自行控制,不受阶段边界确认模式影响。仅在 `--auto` 模式下,阶段内内容确认也被跳过。

## §8 标题解析

> 适用对象:所有用户可见的屏幕输出位置(启动/完成/中止/错误/报告)。
> 从产出文档中提取标题,用于屏幕输出。

### 工具函数

```ts
function truncateTitle(title: string, maxLen: number = 30): string {
  if ([...title].length <= maxLen) return title
  return [...title].slice(0, maxLen).join('') + '...'
}

function formatReqTitle(reqNum: string, title: string): string {
  return `${reqNum} · ${truncateTitle(title)}`
}
```

### 标题解析入口

```ts
function parseResultTitle(filePath: string): string {
  const content = readFile(filePath)
  // 匹配 REQUIRE.md / DESIGN.md / PLAN.md 的标题行
  const match = content.match(/^# (?:需求分析|软件设计|任务排期) — (.+)$/m)
  return match ? match[1] : ''  // 退化:返回空字符串
}
```

### 屏幕输出格式契约

| 场景 | 格式 |
| --- | --- |
| 启动 | `正在处理: REQ-NNNNN · <需求标题>` |
| 完成 | `完成: REQ-NNNNN · <需求标题>` |
| 中止 | `⛔ code req 中止: REQ-NNNNN · <需求标题>(<原因>)` |
| 错误 | `✗ 错误: REQ-NNNNN · <需求标题>(<错误信息>)` |

### 边界与异常

- E-1:标题 > 30 字符 → `truncateTitle` 自动截断到 30 字 + `...`
- E-2:标题字段缺失 → 退化:屏幕输出"编号+(无标题)"
- E-3:多次执行 → 标题覆盖(幂等)

### 约束

- **不**使用"本需求"等指代词 — 替换为"编号+标题"
- **不**修改 frontmatter
- **不**修改既有章节

## §9 通用边界

### 错误处理

- 任一阶段执行失败 → 追加 PROCESS.md 失败记录,退出
- 文件写入失败 → 屏显警告,不阻断主流程(除 REQUIRE.md/DESIGN.md 等核心产出)
- Git 操作失败 → 屏显警告,不阻断主流程

### 幂等性

- 重复执行同一阶段 → 覆盖既有产出文件(以最新为准)
- PROCESS.md 追加不幂等(每次执行追加新行)

### 编码规范

- 产出代码中不得出现 REQ-NNNNN / BUG-NNNNN / TASK-* 格式的编号
- 代码注释使用功能梗概替代编号
- 此约束不覆盖 commit message 和 `./assistants/` 工作产物

## §10 DONE 阶段兜底提交

> 本小节为 `/code req` 与 `/code fix` 流程的 DONE 阶段提供"兜底提交代码"的详细流程。
> 在进入 DONE 阶段时加载。

### 步骤 1 — 检测 git 仓库

```
Bash: git rev-parse --git-dir 2>/dev/null
```

- 退出码 ≠ 0 → 非 git 仓库,屏幕输出 `[兜底提交] 非 git 仓库,跳过提交`,结束
- 退出码 = 0 → 进入步骤 2

### 步骤 2 — 检查变更

```
Bash: git status --porcelain
```

- 输出为空 → 屏幕输出 `[兜底提交] 无文件变更,跳过提交`,结束
- 输出非空 → 进入步骤 3

### 步骤 3 — 暂存文件

```
Bash: git add -A
```

- 失败 → 透传 stderr,屏幕输出 `[兜底提交] git add 失败: <stderr>`,中断
- 成功 → 进入步骤 4

### 步骤 4 — 生成 commit message

按以下格式生成 commit message:

```
chore(<技能名>): <需求/缺陷编码> <标题>

<阶段统计摘要>

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>
```

示例:
```
chore(code req): REQ-00045 补充 REQ-00044 缺失的子命令能力

需求分析:6 FR / 6 NFR / 12 AC
软件设计:6 新增文件 / 7 修改文件 / 4 决策
任务排期:8 任务 / 4 里程碑
编码执行:8/8 任务完成
代码审查:0 发现 / 通过

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>
```

### 步骤 5 — 确认或执行提交

#### --auto 模式

直接执行提交,无需确认:

```
Bash: git commit -m "<message>"
```

- 成功 → 屏幕输出 `[兜底提交] commit 完成, hash: <hash>`
- 失败 → 屏幕输出 `[兜底提交] commit 失败: <stderr>`,提示用户手动处理

#### 非 --auto 模式

使用 `AskUserQuestion` 确认:

```
兜底提交:所有阶段已完成,是否提交代码?
commit message 预览:
---
<commit message>
---
选项:
A. 确认提交(推荐)
B. 跳过提交(文件保持暂存状态)
C. 取消
```

- 选 A → `Bash: git commit -m "<message>"`,输出结果
- 选 B → 屏幕输出 `[兜底提交] 已跳过提交,文件保持暂存状态,请手动 git commit`
- 选 C → 屏幕输出 `[兜底提交] 已取消`

## §11 --confirm 模式

> 本小节定义 `--confirm` 模式的完整行为规范。在解析到 `--confirm` flag 时加载。

### 触发条件

- 用户传入 `--confirm` flag
- 与 `--auto` 互斥,同时传入报错退出

### 阶段边界确认

每个阶段完成后,触发增强确认:

1. 提示产出物文件路径(所有本阶段新生成/修改的文件)
2. 弹出 AskUserQuestion(继续/中止)
3. 用户确认继续后,重新读取所有产出物文件(获取用户最新修改)
4. 不提供"暂停"选项(--confirm 模式下要么继续要么中止)

### 阶段内内容确认

`--confirm` 不影响阶段内内容确认行为。阶段内内容确认(需求澄清、设计选型、任务拆分等)由各阶段 references 自行控制,正常触发 AskUserQuestion。

### 各阶段产出物路径映射

| 阶段 | `/code req` 产出物 | `/code fix` 产出物 |
| --- | --- | --- |
| INIT | — | `fix/<BUG>/BUG.md` |
| REQUIRE | `req/<REQ>/REQUIRE.md`, `req/<REQ>/clarifications.md`(如有) | — |
| DESIGN | `req/<REQ>/DESIGN.md` | `fix/<BUG>/DESIGN.md` |
| PLAN | `req/<REQ>/PLAN.md` | `fix/<BUG>/PLAN.md` |
| CODING | `req/<REQ>/TASK-*.md`(所有任务文件) | `fix/<BUG>/TASK-*.md`(所有任务文件) |
| CHECK | `req/<REQ>/CHECK.md` | `fix/<BUG>/CHECK.md` |

### 确认提示模板

```
=== code req --confirm: <阶段名> 阶段完成 ===
<摘要统计>

产出物文件:
  - <路径1>
  - <路径2>

你可以手动修改上述文件,完成后选择:
A. 继续(重新读取产出物,获取最新修改,进入下一阶段)
B. 中止(保存当前进度,退出)
```

### 重读机制

用户选择继续后,对所有产出物文件执行 Read 操作,确保下一阶段使用用户修改后的最新内容。重读范围包括但不限于:REQUIRE.md/DESIGN.md/PLAN.md/TASK-*.md/CHECK.md。

### 中止处理

- 选 B(中止):追加 PROCESS.md `| <时间> | <阶段> | 中止 | 用户在 --confirm 确认环节中止 |`,退出
- 下次调用时从 PROCESS.md 恢复,从中止的阶段重新开始