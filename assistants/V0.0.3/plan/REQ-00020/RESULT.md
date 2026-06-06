# 详细设计 — REQ-00020(优化 code-design / code-plan,架构设计目标重新归位 + 新增 3 维度 + 步骤归并)

- 需求编码:REQ-00020
- 所属版本:V0.0.3
- 文档版本:v1
- 状态:已锁定
- 责任人:wangmiao
- 创建:2026-06-06
- 最近更新:2026-06-06 18:00
- 当前版本:v1
- **上游需求**:`./assistants/V0.0.3/require/REQ-00020/RESULT.md`(v1,2026-06-06 16:30)
- **上游概要设计**:`./assistants/V0.0.3/design/REQ-00020/RESULT.md`(v1,2026-06-06 17:30)
- **遵循规范**:`./assistants/rules/` 下 13 个文件(本需求 0 触发 §规则 1 三同步)
- **架构对象**:`code-skills` 仓库**自身**的 3 个 `code-*` 技能(`code-design` / `code-plan` / `code-it`)+ 1 份需求提示词文档(`require/REQ-00020/RESULT.md`)

---

## 设计目标

> 本小节由 `code-plan` 步骤 0b 沿用 `code-design` 的"## 设计目标"小节,并补充 7 维度详细优先级。

- **回写时间**:2026-06-06 18:00
- **回写触发**:`code-plan` 步骤 0b

### 整体设计目标
`--extensible`(沿用 `code-design` 阶段选择,本阶段再次确认)

### 维度优先级

| 维度 | 优先级 | 来源 | 依据 |
| --- | --- | --- | --- |
| 功能性 | 中 | 沿用 `code-design` | 本需求是元技能改造,功能性=中(沿用 SKILL.md 既有功能) |
| 扩展性 | 高 | `code-plan` 步骤 0b 第一轮 | 整体=--extensible + 扩展性=高 → 至少 3 个扩展性任务(FR-4) |
| 健壮性 | 高 | `code-plan` 步骤 0b 第一轮 | 用户显式选择,过程文档充分记录 |
| 可维护性 | 高 | `code-plan` 步骤 0b 第一轮 | "代码中无需说明,登记到过程文档中" → 过程文档详尽 |
| 封装性 | 高 | `code-plan` 步骤 0b 第二轮 | 本需求采纳 4 处归并(M-1 ~ M-4)即体现封装性 |
| 可复用性 | 高 | `code-plan` 步骤 0b 第二轮 | 本需求采纳"归并相同/相似代码逻辑" |
| 可读性 | 不适用 | `code-plan` 步骤 0b 第二轮 | 本仓库是 Markdown 自然语言,语义即注释 |

### 设计目标对本详设的影响(FR-4 + 本需求 FR-3)

| 维度=高 | 任务数 | 任务类型(本需求采纳) |
| --- | --- | --- |
| 扩展性(整体=--extensible) | ≥3 | 扩展架构设计 / 抽象层预留 / 接口契约 |
| 封装性 | ≥1 | 封装抽象层 / 接口契约 / 扩展点(本需求 M-1 ~ M-4 归并) |
| 可复用性 | ≥1 | 抽取公共逻辑 / 归并相似代码 / 复用既有模块(本需求 M-2 公共子步骤) |
| 可读性=不适用 | 0 | 跳过(本仓库 Markdown) |
| 健壮性 / 可维护性 | 参考 | 不强制加任务,过程文档充分记录 |

---

## 1. 概述

本详细设计把 `code-design` 阶段"系统长什么样"落地为"具体怎么改"——给出可直接编码的:
- 3 个 SKILL.md 改造点(用结构化语义锚点,不用行号)
- 4 处步骤归并(M-1 ~ M-4)的边界与引用约定
- 任务粒度调整规则 +3 行的具体内容
- 6-8 个任务的编码计划(分配到 PLAN.md)

实际改造**已落地**(git commit `e69a58a`,在 `code-require` 阶段完成),本计划为已落地改造补充**详细化** + 任务清单登记。

## 2. 上游引用(需求 / 设计 / 规范)

### 2.1 上游需求

- 来源:`./assistants/V0.0.3/require/REQ-00020/RESULT.md`(v1)
- 提取的 FR / NFR / AC 数量:8 FR / 8 NFR / ~40 AC / 9 INV
- 关键交叉点:
  - FR-1 → §3.1 步骤 0b 简化为 1 维度
  - FR-2 → §3.2 步骤 0b 扩展为 7 维度
  - FR-3 → §3.3 任务粒度调整规则 +3 行
  - FR-4 → §3.4 步骤归并 M-1 ~ M-4
  - FR-5 ~ FR-8 → 强约束(详 §12 规范遵循)

### 2.2 上游概要设计

- 来源:`./assistants/V0.0.3/design/REQ-00020/RESULT.md`(v1)
- 提取的模块拆分 / 接口概要 / 数据结构 / 决策:
  - D-1:code-design 步骤 0b 简化为 1-2 问
  - D-2:code-plan 步骤 0b 扩展为 7 维度
  - D-3:任务粒度调整规则 +3 行
  - D-4:M-1 ~ M-4 4 处归并
  - D-5:code-plan 略增(+6 行)接受
  - D-6:`--result` / `--plan` 参数预留(留 REQ-00021)
  - D-7:7 维度默认推荐值
- 9 条不变量(INV-1 ~ INV-9,字节级保留)

### 2.3 规范遵循清单

| 规范文件 | 关键约束 | 本详设遵循情况 |
| --- | --- | --- |
| `skill-conventions.md` | §规则 1:frontmatter `name` 字节级保留 | ✅ INV-1 锁定 0 改 |
| `dashboard-conventions.md` | §规则 1:任务清单 0 新增列/枚举/区段 | ✅ INV-5 锁定 0 触发 |
| `encoding-conventions.md` | §规则 1/3:任务编号 5+5 位嵌套式 | ✅ INV-6 锁定 0 触发 |
| `marketplace-protocol.md` | 0 改 `marketplace.json` / `plugin.json` | ✅ INV-6 锁定 0 触发 |
| `module-conventions.md` | §规则 1:过程文档摆放在 `<version>/plan/<REQ>/` 根目录 | ✅ |
| `commit-conventions.md` | `chore(<scope>): <subject>` 格式 | ✅ INV-3 锁定 0 触发 |
| `doc-conventions.md` | 中英 README 同步 | ✅ INV-3 锁定 0 触发 |
| `naming-conventions.md` | 0 新增文件名前缀 | ✅ INV-3 锁定 0 触发 |
| `dependency-conventions.md` | 0 新增依赖 | ✅ INV-3 锁定 0 触发 |

**0 触发任何 §规则 1**。

## 3. 模块详细化(对应 `code-design` §3.2 的 7 项设计决策)

### 3.1 模块:`code-design` 步骤 0b 简化(对应 D-1)

- **路径**:`plugins/code-skills/skills/code-design/SKILL.md` §步骤 0b
- **关键类/函数**:无(纯 SKILL.md 文档)
- **调用顺序**:技能启动 → 步骤 0a git pull → 步骤 0b.0 code-auto 检测 → **步骤 0b(本需求改后)**:
  - 评估需求规模(小/中/大)
  - 触发 1-2 个 `AskUserQuestion`(整体设计目标 + 功能性 1 维度)
  - 用户回答 → 调 `writeDesignGoalsSection(designResultPath, goals, "code-design")` 写入 `design/.../RESULT.md` 顶部"## 设计目标"小节
- **状态归属**:无
- **与概要设计的对应**:D-1
- **符合的规范**:`skill-conventions §规则 1`

### 3.2 模块:`code-plan` 步骤 0b 扩展(对应 D-2)

- **路径**:`plugins/code-skills/skills/code-plan/SKILL.md` §步骤 0b
- **关键类/函数**:无
- **调用顺序**:技能启动 → 步骤 0a git pull → 步骤 0b.0 引用 `code-design` 步骤 0b.0(M-1 归并)→ **步骤 0b(本需求改后)**:
  - 读 `design/<REQ>/RESULT.md` 的"## 设计目标"小节(沿用)
  - 补充 6 个新维度的 `AskUserQuestion`(扩展性 / 健壮性 / 可维护性 / 封装性 / 可复用性 / 可读性)
  - 评估需求规模:小 1 问 / 中 4 问 / 大 8 问
  - 用户回答 → 调 `writeDesignGoalsSection(planResultPath, goals, "code-plan")` 写入 `plan/.../RESULT.md` 顶部"## 设计目标"小节
- **状态归属**:无
- **与概要设计的对应**:D-2
- **符合的规范**:`skill-conventions §规则 1`

### 3.3 模块:`code-plan` 任务粒度调整规则 +3 行(对应 D-3)

- **路径**:`plugins/code-skills/skills/code-plan/SKILL.md` §步骤 10A 末尾"按'## 设计目标'小节调整任务粒度"小节
- **关键类/函数**:无
- **调用顺序**:任务拆分时读"## 设计目标"小节 → 提取 7 维度优先级 → 调整任务粒度
- **状态归属**:无
- **与概要设计的对应**:D-3
- **符合的规范**:`commit-conventions`(0 派生"更新看板"任务)

### 3.4 模块:步骤归并 M-1(对应 D-4)

- **路径**:`plugins/code-skills/skills/code-plan/SKILL.md` §步骤 0b.0
- **关键类/函数**:无
- **调用顺序**:M-1 归并为引用 → 18 行 → 12 行(`> 引用:` 块引用 `code-design` 步骤 0b.0 段)
- **状态归属**:无
- **与概要设计的对应**:D-4
- **符合的规范**:`module-conventions §规则 1`

### 3.5 模块:步骤归并 M-2(对应 D-4)

- **路径**:`plugins/code-skills/skills/code-plan/SKILL.md` §步骤 3 / 5 / 21 / 22
- **关键类/函数**:无
- **调用顺序**:抽"## 公共子步骤:读规范/读上游/探索代码"概念,4 处用 `> 引用:` 块引用
- **状态归属**:无
- **与概要设计的对应**:D-4
- **符合的规范**:`module-conventions §规则 1`

### 3.6 模块:步骤归并 M-3(对应 D-4)

- **路径**:`plugins/code-skills/skills/code-it/SKILL.md` §步骤 23
- **关键类/函数**:无
- **调用顺序**:23.1-23.3 引用任务分支 9-12 段;23.4 错误修复循环 1 行引用
- **状态归属**:无
- **与概要设计的对应**:D-4
- **符合的规范**:`module-conventions §规则 1`

### 3.7 模块:步骤归并 M-4(对应 D-4)

- **路径**:`plugins/code-skills/skills/code-plan/SKILL.md` §步骤 6 + `code-it/SKILL.md` §步骤 0a.7
- **关键类/函数**:无
- **调用顺序**:
  - `code-plan` 步骤 6:4 种情形 → 3 种情形(移除"PLAN.md 存在,RESULT.md 不存在"分支)
  - `code-it` 步骤 0a.7:E-1 / E-4 / E-8 / E-9 合并为 1 张职责归属表
- **状态归属**:无
- **与概要设计的对应**:D-4
- **符合的规范**:`module-conventions §规则 1`

### 3.8 模块:`--result` / `--plan` 参数预留(对应 D-6)

- **路径**:`code-require` / `code-design` / `code-plan` SKILL.md 顶部"## 命令行参数解析"小节
- **关键类/函数**:无
- **调用顺序**:本需求**不**实现,留 REQ-00021
- **状态归属**:无
- **与概要设计的对应**:D-6
- **符合的规范**:N/A(本需求 0 改)

## 4. 算法与逻辑(伪代码 / 流程图)

### 4.1 步骤归并 M-1 引用伪代码

```ts
// code-plan 步骤 0b.0 改后(本需求 FR-4 归并)
function codePlanStep0b0():
  if detectCodeAuto():
    skip AskUserQuestion, use --balanced default
  else:
    enter code-plan 步骤 0b 设计目标确认
    // 详见 code-design 步骤 0b.0 段(同源)
```

### 4.2 任务粒度调整 M-3 伪代码

```ts
// code-plan 步骤 10A 末尾"按'## 设计目标'小节调整任务粒度"改后(本需求 FR-3)
function adjustTaskGranularityByGoals(tasks, goals):
  newTasks = tasks

  if goals.overallGoal == '--extensible' or goals.extensibility == '高':
    newTasks.push([newTask('扩展架构设计')])
    if goals.extensibility == '高':
      newTasks.push([newTask('抽象层预留')])
      newTasks.push([newTask('接口契约设计')])

  if goals.encapsulation == '高':
    newTasks.push([newTask('封装抽象层 / 接口契约 / 扩展点')])

  if goals.reusability == '高':
    newTasks.push([newTask('抽取公共逻辑 / 归并相似代码 / 复用既有模块')])

  // 可读性=高 + 非自然语言 才加(本需求不适用)
  if goals.readability == '高' and isNonNaturalLanguage():
    newTasks.push([newTask('关键代码注释 / 复杂逻辑说明')])

  return newTasks
```

### 4.3 步骤归并 M-2 引用流程

```
code-plan 步骤 3 公共子步骤(读规范) ─┐
code-plan 步骤 5 公共子步骤(探索代码) ─┤ → 引用"## 公共子步骤:读规范/读上游/探索代码"
code-plan 步骤 21 公共子步骤(读规范) ─┤
code-plan 步骤 22 公共子步骤(探索代码) ─┘
```

## 5. 数据结构完整变更(本需求 N/A)

本需求**0**新增 / 修改数据结构(纯 SKILL.md 改造)。

但需要详细化 1 个数据结构(沿用 REQ-00011):

### 5.1 "## 设计目标"小节结构(扩展后,本需求 7 维度)

```ts
{
  writeTime: string,         // "YYYY-MM-DD HH:mm"
  writeTrigger: "code-design" | "code-plan"
  overallGoal: "--minimal" | "--extensible" | "--balanced"
  dimensionPriority: {
    functionality: "高" | "中" | "低",
    extensibility: "高" | "中" | "低",        // 沿用 REQ-00011
    robustness: "高" | "中" | "低",           // 沿用 REQ-00011
    maintainability: "高" | "中" | "低",       // 沿用 REQ-00011
    encapsulation: "高" | "中" | "低" | "不适用",  // 本需求新增
    reusability: "高" | "中" | "低" | "不适用",    // 本需求新增
    readability: "高" | "中" | "低" | "不适用"     // 本需求新增
  }
}
```

## 6. 接口细节(本需求 N/A)

本需求**0**新增 API 端点 / 内部函数。CLI 参数预留 `--result` / `--plan` 由 REQ-00021 实现。

## 7. 异常处理

沿用既有 `code-design` / `code-plan` / `code-it` 异常处理流程。

### 7.1 `code-plan` 步骤 0b 大需求 8 问时

- **异常**:用户取消 `AskUserQuestion` 中途
- **处理**:中止 + 回写空"## 设计目标"小节(沿用 REQ-00011 E-3)
- **影响**:PLAN.md 任务粒度调整规则不触发,按默认粒度拆分

### 7.2 步骤归并后某次调用找不到原逻辑(本需求 E-7)

- **异常**:M-1 / M-2 / M-3 / M-4 归并后,后续维护者读 SKILL.md 时找不到原逻辑
- **处理**:`> 引用:` 块明确指向原段位置
- **影响**:0(职责清晰,引用约定)

## 8. 安全要求

- NFR-6 锁定:无新增鉴权 / 加密需求(本需求纯文档重构)
- `--result` / `--plan` 参数(本需求预留)需在 REQ-00021 中加路径安全约束(NFR-6.1 模板路径不允许 `../` 跳出工作空间)

## 9. 状态机/流程(本需求 N/A)

沿用既有"## 工作流程"状态机(本需求**不**引入新状态)。

## 10. 性能与资源

- `AskUserQuestion` 1-8 问耗时 < 5 分钟(沿用 REQ-00011 NFR-8)
- `code-plan` SKILL.md 改后 1015 行(+0.6%);`code-it` SKILL.md 改后 928 行(-4.4%)
- 单次 `code-plan` 技能调用加载 SKILL.md 实测行数与改前持平略增,但屏显模板简化(4 维度 → 1 维度)
- 单次 `code-it` 技能调用加载 SKILL.md 实测行数下降(从 971 → 928)

## 11. 测试要点

### 11.1 单元测试(本仓库 0 测试框架,测试状态="不适用")

- `code-design` 步骤 0b 改造验证:1-2 问,功能性=中
- `code-plan` 步骤 0b 改造验证:1-8 问,7 维度齐全
- 任务粒度调整规则 +3 行验证

### 11.2 集成测试

- `code-auto` 上下文默认推荐值验证
- 步骤归并 M-1 ~ M-4 引用约定验证

### 11.3 端到端测试

- 完整流程:`code-require REQ-00020` → `code-design REQ-00020` → `code-plan REQ-00020` → 实际产出 3 技能改造

## 12. 规范遵循(本需求 0 触发 13 份规范任何一条)

- 0 触发 `dashboard-conventions §规则 1`
- 0 触发 `encoding-conventions §规则 1/3`
- 0 触发 `marketplace-protocol`
- 0 触发 `module-conventions §规则 1`(过程文档同源段引用)
- 0 触发 `commit-conventions`(沿用既有)
- 0 触发 `doc-conventions`(0 改中英 README)
- 0 触发 `naming-conventions`(0 新增前缀)
- 0 触发 `dependency-conventions`(0 新增依赖)
- 0 触发 `framework-conventions`
- 0 触发 `coding-style`(沿用既有)
- 0 触发 `migration-mapping`
- 0 触发 `directory-conventions`
- 0 触发 `skill-conventions`(frontmatter 字节级保留)

## 13. 关联(同版本 + 跨版本)

### 13.1 同版本 V0.0.3 关联

- REQ-00021:`code-require` / `code-design` / `code-plan` `--result` / `--plan` 模板参数(本需求 D-6 预留)

### 13.2 跨版本 V0.0.2 关联

- REQ-00011:`code-design` / `code-plan` 步骤 0b 设计目标确认(本需求改后 FR-1 / FR-2)
- REQ-00019:`code-plan` BUG 模式同构(本需求保持 BUG 路径)
- REQ-00010:`code-it` 步骤 0a 前置任务守卫(本需求 M-4 后半 E 边界合并)
- REQ-00013:6 技能标题解析(本需求沿用)
- REQ-00014:`code-plan` 任务拆分维度(本需求 FR-3 +3 行扩展)
- REQ-00017:`code-plan` 不再为"更新看板"拆派生任务(本需求 INV-7 沿用)
- BUG-00001:脏标记文件修复(本需求 M-1 引用)

## 14. 待澄清 / 未决项

| 编号 | 内容 | 状态 |
| --- | --- | --- |
| (无) | 本需求 0 待澄清;8 FR / 8 NFR / ~40 AC / 9 INV 全部已锁定;7 维度已由用户在 2 轮 `AskUserQuestion` 中确认(整体=--extensible / 扩展性=高 / 健壮性=高 / 可维护性=高 / 封装性=高 / 可复用性=高 / 可读性=不适用) | 0 待澄清 |

## 15. 变更记录

| 时间 | 版本 | 变更摘要 | 变更人 |
| --- | --- | --- | --- |
| 2026-06-06 18:00 | v1 | 初始创建:14 章节完整详细化(3 模块详细化 + 4 步归并 M-1~M-4 + 任务粒度 +3 行 + 7 维度确认) + 6-8 任务编码计划;整体=--extensible + 7 维度优先级已确认(封装性=高 / 可复用性=高 / 扩展性=高 / 可读性=不适用) | wangmiao |
