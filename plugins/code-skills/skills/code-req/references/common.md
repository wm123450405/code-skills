# 公共流程 — code-req

> 本文件为 code-req 技能提供阶段无关的公共流程。始终加载。

## §1 版本检测(强制前置)

1. 读取 `./assistants/.current-version`
2. **文件不存在** → 立即停下,告知用户先调 `code-ver`
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

```
async function executeStage(stage, context, autoMode):
  // 1. 追加 PROCESS.md 开始记录
  appendProcess(stage, "开始", stageDescriptions[stage].start)
  
  // 2. 执行阶段逻辑
  result = await stageHandlers[stage](context)
  
  // 3. 追加 PROCESS.md 完成记录
  appendProcess(stage, "完成", result.summary)
  
  // 4. 交互确认(非 --auto 模式)
  if not autoMode:
    response = askUserQuestion("阶段完成,是否继续?")
    if response == "取消":
      return { status: "CANCELLED" }
  
  return result
```

### --auto 模式

- 所有 `AskUserQuestion` 自动选第一项(推荐项)
- 屏幕输出 `[code-req --auto] <阶段> 完成,自动继续`
- 错误时仍中断(不静默吞错误)

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

### 缺陷路径(code-fix 复用)

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

## §7 交互确认(非 --auto)

### 确认时机

每个阶段完成后,弹出确认:

```
阶段 <阶段名> 完成: <摘要>
选项:
A. 继续下一阶段(推荐)
B. 暂停(保存进度,下次从此阶段继续)
C. 取消(放弃本次执行)
```

### 暂停处理

- 选 B(暂停):追加 PROCESS.md `| <时间> | <阶段> | 暂停 | 用户暂停 |`,退出
- 下次调用时从 PROCESS.md 恢复,从暂停的阶段继续

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
| 中止 | `⛔ code-req 中止: REQ-NNNNN · <需求标题>(<原因>)` |
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