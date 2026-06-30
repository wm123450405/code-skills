# 软件设计 — REQ-00049 · 为 code-req、code-fix 增加 --confirm 模式

> 所属版本:V0.0.5
> 创建时间:2026-06-30

## 1. 设计概述

为 `code-req` 和 `code-fix` 引入三态行为模型，通过 `--confirm`/`--auto` 两个互斥 flag 控制确认粒度。核心改动在 `common.md` 的阶段执行器(§4)和交互确认(§7)，以及两个 SKILL.md 的参数章节。

## 2. 模块拆分

| 模块 | 职责 | 涉及文件 | 依赖 |
| --- | --- | --- | --- |
| 参数模型 | 新增 --confirm 输入/解析，三态定义 | `skills/code-req/SKILL.md`, `skills/code-fix/SKILL.md` | common.md |
| 阶段执行器 | 实现三态确认流程 | `skills/code-req/references/common.md` | 无 |

## 3. 接口设计(修改点)

### 3.1 三态行为模型

> **核心原则**:`--confirm` 控制阶段边界确认(是否继续下一阶段)，不影响阶段内内容确认(需求澄清、设计选型、任务拆分等)。原有的 AskUserQuestion 与 --confirm 是正交关系，不冲突。

| 模式 | 触发条件 | 阶段边界确认 | 阶段内内容确认 |
| --- | --- | --- | --- |
| --confirm | `--confirm` flag | ✅ 增强确认(路径+重读+继续/中止) | 正常触发(AskUserQuestion) |
| --auto | `--auto` flag | ❌ 自动继续 | ❌ 自动选推荐项 |
| 默认 | 无 flag | ❌ 自动继续 | 正常触发(AskUserQuestion) |

**关键区别**:
- 阶段边界确认:控制"是否进入下一阶段"，原为(继续/暂停/取消)
- 阶段内内容确认:控制"需求细节/设计方案/任务拆分"等开发内容，原为 AskUserQuestion
- `--confirm` 仅增强阶段边界确认，不改变阶段内内容确认行为
- 原有 AskUserQuestion **保留**，不受 --confirm 影响

### 3.2 code-req SKILL.md 修改点

**输入章节**:
```
- **--confirm**(可选):增强确认模式,所有冲突/矛盾/二义性/模糊/规划/进程均需用户确认;与 --auto 互斥
- **--auto**(可选):静默模式,所有决策自动选推荐项;与 --confirm 互斥
```

**参数解析章节**:新增 `### --confirm 模式` 小节，描述三态行为

**阶段执行器章节**:更新确认逻辑为三态分支

### 3.3 code-fix SKILL.md 修改点

与 code-req 对称修改。

### 3.4 common.md 修改点

**§4 阶段执行器**:重写伪代码，支持三态分支

**§7 交互确认**:重写，描述 --confirm 增强确认流程

## 4. 数据设计(关键流程)

### 4.1 --confirm 确认流程(新增)

```
async function executeStage(stage, context, flags):
  // 0. 阶段前置校验(不变)
  ...
  
  // 1-2. 追加 PROCESS.md + 执行阶段逻辑(不变)
  ...
  
  // 3. 追加 PROCESS.md 完成记录(不变)
  ...
  
  // 4. 阶段边界确认(三态)
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
    
    // 4c. 重新读取产出物
    for file in outputFiles:
      reRead(file)
  
  else if flags.auto:
    print("[code-req --auto] <stage> 完成,自动继续")
  
  // else: 默认 — 自动继续,无输出
  
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

| 场景 | 阶段边界确认 | 阶段内内容确认 |
| --- | --- | --- |
| 无 flag | 自动继续 | 正常触发 |
| --confirm | 增强确认(路径+重读) | 正常触发 |
| --auto | 自动继续 | 自动选推荐项 |
| --confirm --auto | 错误退出 | — |

## 6. 方案选型

### 决策 1:--confirm 与 --auto 关系
- **选择**:互斥，同时传入报错退出
- **备选**:--confirm 优先(忽略 --auto)
- **选择理由**:用户确认(见 clarifications.md)
- **权衡**:两个模式语义互斥，不能同时使用

### 决策 2:默认行为变更
- **选择**:无 flag 时阶段边界自动流转，但阶段内内容确认(需求澄清、设计选型等)保留
- **备选**:保持默认阶段边界 AskUserQuestion
- **选择理由**:用户原始需求明确要求"未启用 --confirm 模式时自动进入下一个阶段"；且阶段内内容确认与阶段边界确认是正交关系，不受影响
- **权衡**:失去默认的"暂停"能力，但 --confirm 提供了更强的阶段边界控制
- **用户确认**:原有的 AskUserQuestion 与 --confirm 不冲突，保留阶段内内容确认

### 决策 3:重读时机
- **选择**:用户确认继续后，立即重读所有产出物文件
- **备选**:在下一阶段开始时重读
- **选择理由**:确认后立即重读确保下一阶段看到的是用户修改后的内容
- **权衡**:增加一次文件读取，IO 开销可忽略

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
| 2026-06-30 | v2 | 用户确认 | 9d 危险操作:保留原有 AskUserQuestion;9b 方案选型:三态模型合理;9c 改修方案:3 文件范围合理 | wangmiao |