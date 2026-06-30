# 软件设计 — REQ-00049 · 为 code-req、code-fix 增加 --confirm 模式

> 所属版本:V0.0.5
> 创建时间:2026-06-30

## 1. 设计概述

本需求为 `code-req` 和 `code-fix` 新增 `--confirm` 命令行参数，同时变更默认行为。涉及 3 个文件的修改，核心改动在 `common.md` 的阶段执行器(§4)和交互确认(§7)章节。

## 2. 模块拆分

| 模块 | 职责 | 涉及文件 | 依赖 |
| --- | --- | --- | --- |
| code-req 参数 | 新增 --confirm 输入/解析 | `skills/code-req/SKILL.md` | common.md |
| code-fix 参数 | 新增 --confirm 输入/解析 | `skills/code-fix/SKILL.md` | common.md |
| 公共阶段执行器 | 实现 --confirm 确认流程、默认行为变更 | `skills/code-req/references/common.md` | 无 |

## 3. 接口设计(修改点)

### 3.1 code-req SKILL.md 修改点

**输入章节**:
```
- **--confirm**(可选):增强确认模式,每个阶段完成后强制确认,提示产出物路径,允许用户修改后重读
- **--auto**(可选):静默模式,与 --confirm 互斥
```

**参数解析章节**:新增 `### --confirm 模式` 小节，描述确认流程

**阶段执行器章节**:更新确认逻辑，增加 --confirm 分支

### 3.2 code-fix SKILL.md 修改点

与 code-req 对称修改，将 `code-req` 替换为 `code-fix`。

### 3.3 common.md 修改点

**§4 阶段执行器**:Update `executeStage` pseudocode to handle --confirm mode

**§7 交互确认**:Rewrite to describe --confirm enhanced confirmation flow

## 4. 数据设计(关键流程)

### 4.1 --confirm 确认流程(新增)

```
async function executeStage(stage, context, flags):
  // 0. 阶段前置校验(不变)
  if not preStageCheck(stage, context.reqDir):
    appendProcess(stage, "失败", "前置产出物缺失,退回上一阶段")
    return { status: "ROLLBACK", targetStage: previousStage(stage) }
  
  // 1. 追加 PROCESS.md 开始记录(不变)
  appendProcess(stage, "开始", stageDescriptions[stage].start)
  
  // 2. 执行阶段逻辑(不变)
  result = await stageHandlers[stage](context)
  
  // 3. 追加 PROCESS.md 完成记录(不变)
  appendProcess(stage, "完成", result.summary)
  
  // 4. --confirm 模式:增强确认
  if flags.confirm:
    // 4a. 提示产出物文件路径
    outputFiles = getStageOutputFiles(stage, context.reqDir)
    print("阶段 <stage> 完成,产出物:")
    for file in outputFiles:
      print("  - " + file)
    print("你可以手动修改上述文件,完成后选择继续。")
    
    // 4b. 弹出确认
    response = askUserQuestion("继续下一阶段?", [
      "A. 继续(重新读取产出物,获取最新修改)",
      "B. 中止"
    ])
    
    if response == "B":
      appendProcess(stage, "中止", "用户在 --confirm 确认环节中止")
      return { status: "ABORTED" }
    
    // 4c. 重新读取产出物(获取用户最新修改)
    for file in outputFiles:
      reRead(file)  // 刷新内存中的内容
  
  // 5. --auto 模式:自动继续(不变)
  else if flags.auto:
    print("[code-req --auto] <stage> 完成,自动继续")
  
  // 6. 默认:自动继续(新增,替代原有 AskUserQuestion)
  // (无操作,直接进入下一阶段)
  
  return result
```

### 4.2 各阶段产出物路径映射

| 阶段 | 产出物路径(code-req) | 产出物路径(code-fix) |
| --- | --- | --- |
| INIT | — | `fix/<BUG>/BUG.md` |
| REQUIRE | `req/<REQ>/REQUIRE.md`, `req/<REQ>/clarifications.md`(如有) | — |
| DESIGN | `req/<REQ>/DESIGN.md` | `fix/<BUG>/DESIGN.md` |
| PLAN | `req/<REQ>/PLAN.md` | `fix/<BUG>/PLAN.md` |
| CODING | `req/<REQ>/TASK-*.md`(所有任务文件) | `fix/<BUG>/TASK-*.md`(所有任务文件) |
| CHECK | `req/<REQ>/CHECK.md` | `fix/<BUG>/CHECK.md` |

### 4.3 参数互斥检查

```
if flags.confirm and flags.auto:
  print("✗ --confirm 与 --auto 互斥,不能同时使用")
  exit(1)
```

## 5. 关键流程

### 5.1 阶段流转行为对比

| 场景 | 当前行为 | 新行为 |
| --- | --- | --- |
| 无 flag | AskUserQuestion(继续/暂停/取消) | 自动继续(无需确认) |
| --confirm | (不存在) | 增强确认:产出物路径 + 允许修改 + 重读 |
| --auto | 自动继续 + 前缀输出 | 不变 |
| --confirm --auto | (不存在) | 错误退出 |

### 5.2 --confirm 确认提示模板

```
=== code-req --confirm: <阶段名> 阶段完成 ===
<摘要统计>

产出物文件:
  - assistants/<版本号>/req/<REQ>/<文件名1>
  - assistants/<版本号>/req/<REQ>/<文件名2>

你可以现在手动修改上述文件。完成后选择:
A. 继续(重新读取产出物,进入下一阶段)
B. 中止(保存当前进度,退出)
```

## 6. 方案选型

### 决策 1:--confirm 与 --auto 关系
- **选择**:互斥,同时传入报错退出
- **备选**:--confirm 优先(忽略 --auto)
- **选择理由**:两个模式语义互斥(一个强制确认,一个强制自动),同时传入是用户错误,应明确提示
- **权衡**:用户不能"在 auto 模式下只确认阶段边界"

### 决策 2:默认行为变更
- **选择**:无 flag 时自动流转,去除默认 AskUserQuestion
- **备选**:保持默认 AskUserQuestion,仅 --confirm 增强
- **选择理由**:用户明确要求"未启用 --confirm 模式时自动进入下一个阶段"
- **权衡**:失去默认的安全确认机制,但 --confirm 提供了更强的确认能力

### 决策 3:重读时机
- **选择**:用户确认继续后,立即重读所有产出物文件
- **备选**:在下一阶段开始时重读
- **选择理由**:确认后立即重读确保下一阶段看到的是用户修改后的内容,避免时序问题
- **权衡**:增加一次文件读取,但 IO 开销可忽略

## 7. 规范合规

| 规范文件 | 检查项 | 结果 |
| --- | --- | --- |
| skill-conventions.md §规则 1 | SKILL.md name+description 完整 | ✅ 不修改 frontmatter |
| skill-conventions.md §规则 2 | 不含开发痕迹 | ✅ 修改后无开发痕迹 |
| encoding-conventions.md | 编码格式引用正确 | ✅ 不涉及 |

## 8. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-06-30 | v1 | 初始创建 | 软件设计完成 | wangmiao |