# 需求分析阶段 — code-req

> 本文件为 code-req 技能的 REQUIRE 阶段提供详细流程。在进入 REQUIRE 阶段时加载。

## 目标

将用户输入的需求描述(自然语言/文档/设计稿等)转化为结构化的 `REQUIRE.md`,作为后续 DESIGN/PLAN/CODING/CHECK 阶段的共同基线。

## 输入

- 用户输入的需求描述(自然语言,必填)
- 用户放置在 `req/<REQ-NNNNN>/` 目录下的补充材料(可选)
- 项目级规范:`./assistants/rules/` 下所有文件

## 输出

主产出物:`req/<REQ-NNNNN>/REQUIRE.md`
辅助产物:`req/<REQ-NNNNN>/LOG.md`(可选,非必要不记录)

## 需求编号分配

### 新建需求

```
function allocateReqNum(versionPath):
  existing = Glob("req/REQ-*/")
  if existing.length == 0:
    return "REQ-00001"
  nums = existing.map(extractNumber).sort()
  return "REQ-" + pad(nums[nums.length - 1] + 1, 5)
```

### 续跑需求

- 用户传入 `REQ-NNNNN` → 直接使用该编号
- 验证 `req/<REQ-NNNNN>/` 目录存在

## 工作流程

### 步骤 1 — 创建目录与 PROCESS.md

1. 检查 `req/<REQ-NNNNN>/` 是否存在
   - 不存在 → `mkdir -p`,创建 `PROCESS.md` 初始行
   - 存在 → 从 PROCESS.md 恢复

2. PROCESS.md 初始行:
```
| YYYY-MM-DD HH:mm | INIT | 开始 | 创建需求 <REQ-NNNNN> |
```

### 步骤 2 — 收集需求材料

1. 若用户输入为自然语言描述 → 直接作为主需求材料
2. `Glob "req/<REQ-NNNNN>/**/*"` 列出补充材料
3. 对每个文件尝试读取:
   - 文本/图片直接读取
   - 不可读格式 → 在 LOG.md 中标注,提示用户提供文字摘要

### 步骤 3 — 提取需求要素

从材料中提取:

| 要素 | 说明 | REQUIRE.md 章节 |
| --- | --- | --- |
| 功能点(FR) | 系统必须做什么 | §3 功能需求 |
| 约束(NFR) | 性能/安全/兼容/合规/可观测性 | §4 非功能需求 |
| 验收标准(AC) | 可验证的完成条件 | §5 验收标准 |
| 用户角色 | 谁会使用 | §1 需求概述 |
| 交互流程 | 用户操作步骤 | §1 需求概述 |
| 边界条件 | 异常路径/边界值 | §1 需求概述 |

### 步骤 4 — 检索关联需求

1. `Glob "req/*/REQUIRE.md"` 列出同版本所有需求
2. `Grep` 关键词做粗筛
3. 对疑似关联的需求,读取其 REQUIRE.md 摘要
4. 在 `REQUIRE.md §6 关联需求` 中记录关联点

### 步骤 5 — 与用户澄清(非 --auto)

对模糊、歧义、缺失的功能或交互,向用户确认:

- 能给出 2-4 个具体选项 → 使用 `AskUserQuestion`
- 需要开放式描述 → 自然语言提问

> **不过滤技术选型类问题**:本阶段确定功能点,技术选型归 DESIGN 阶段。

### 步骤 6 — 撰写 REQUIRE.md

按 `templates/REQUIRE.md` 结构生成:

```
# 需求分析 — <REQ-NNNNN> · <标题>

## 1. 需求概述
## 2. 背景与目标
## 3. 功能需求(FR)
## 4. 非功能需求(NFR)
## 5. 验收标准(AC)
## 6. 关联需求
## 7. 变更记录
```

### 撰写原则

- **详尽**:每一条需求都展开为可独立验证的描述
- **不臆造**:无材料佐证的细节写进"待澄清"或明确标注"假设"
- **可追溯**:每条 FR/AC 标注来源材料
- **不涉及技术选型**:本阶段只确定功能点,技术选型/架构风格/框架选择归 DESIGN 阶段

### 步骤 7 — 同步版本看板

在 `RESULT.md` 需求清单追加:

```
| REQ-NNNNN | <标题> | [PROCESS.md](req/REQ-NNNNN/PROCESS.md) |
```

## 技术选型过滤

> 本阶段不涉及技术选型。以下关键词命中的内容**不写入** REQUIRE.md,留待 DESIGN 阶段处理:
> `{技术选型, 实现方式, 框架, 库, 工具, 数据库, ORM, 消息队列, 缓存, 架构风格, 部署形态}`

## 非 --auto 模式确认

阶段完成后弹出确认:
```
需求分析完成: <N> FR / <M> NFR / <K> AC
选项:
A. 继续 DESIGN 阶段(推荐)
B. 暂停
C. 取消
```