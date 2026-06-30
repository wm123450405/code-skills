# 概要设计 — REQ-00044 · 技能系统 v2 大改版

> 上游:`./assistants/V0.0.4/require/REQ-00044/RESULT.md`
> 遵循规范:`./assistants/rules/`(若存在)

## 文档头
- 需求编码:REQ-00044
- 所属版本:V0.0.4
- 设计标题:技能系统 v2 大改版
- 状态:已完成
- 创建:2026-06-30 00:00

## 1. 设计概述

将现有 14 个技能重构为 7 个技能,核心思路:
- **纵向合并**:将需求/缺陷开发流程的 5 段式(`require → design → plan → it → check`)合并为 2 个单入口技能(`code-req`/`code-fix`)
- **横向整合**:版本管理、发布、初始化合并为 `code-ver`
- **精简输出**:目录结构从 8 个子目录简化为 2 个(`req/`+`fix/`),文档从多份过程文档简化为核心文档 + `LOG.md`
- **断点续跑**:通过 `PROCESS.md` 追加式记录实现中断恢复

## 2. 模块拆分

### 2.1 新技能目录结构

```
plugins/code-skills/skills/
├── code-ver/          # 版本管理(合并 code-version + code-publish + code-init)
│   ├── SKILL.md
│   ├── references/
│   │   └── common.md
│   └── templates/
│       └── INIT-REPORT.md
├── code-req/          # 需求开发(合并 code-require + design + plan + it + check)
│   ├── SKILL.md
│   ├── references/
│   │   ├── common.md          # 公共流程(需求分析/设计/排期/编码/审查)
│   │   ├── require.md         # 需求分析阶段
│   │   ├── design.md          # 软件设计阶段
│   │   ├── plan.md            # 任务排期阶段
│   │   ├── coding.md          # 编码执行阶段
│   │   └── check.md           # 代码审查阶段
│   └── templates/
│       ├── REQUIRE.md         # 需求分析文档模板
│       ├── DESIGN.md          # 软件设计文档模板
│       ├── PLAN.md            # 任务排期文档模板
│       ├── TASK.md            # 任务完成文档模板
│       ├── CHECK.md           # 代码审查文档模板
│       ├── PROCESS.md         # 执行进程模板
│       └── LOG.md             # 过程记录模板
├── code-fix/          # 缺陷修复(合并 code-fix + plan + it + check)
│   ├── SKILL.md
│   ├── references/
│   │   ├── common.md          # 公共流程(与 code-req 共享大部分逻辑)
│   │   ├── fix-register.md    # 缺陷登记阶段
│   │   ├── design.md          # 修复设计阶段(复用 code-req/references/design.md)
│   │   ├── plan.md            # 任务排期阶段(复用 code-req/references/plan.md)
│   │   ├── coding.md          # 编码执行阶段(复用 code-req/references/coding.md)
│   │   └── check.md           # 代码审查阶段(复用 code-req/references/check.md)
│   └── templates/
│       ├── BUG.md             # 缺陷分析文档模板
│       └── ...(复用 code-req/templates/ 中的 DESIGN/PLAN/TASK/CHECK/PROCESS/LOG)
├── code-faq/          # 知识查询(合并 code-answer)
│   ├── SKILL.md
│   ├── references/
│   │   └── common.md
│   └── templates/
│       ├── REQUIRE-EXPORT.md
│       ├── DESIGN-EXPORT.md
│       └── SUMMARY-EXPORT.md
├── code-rule/         # 保留(适配新结构)
├── code-merge/        # 保留(适配新结构)
└── code-dashboard/    # 保留(适配新结构)
```

### 2.2 旧技能处理

| 旧技能 | 处理方式 |
| --- | --- |
| `code-require` | 在新技能开发的最后一个任务中删除整个目录 |
| `code-design` | 同上 |
| `code-plan` | 同上 |
| `code-it` | 同上 |
| `code-check` | 同上 |
| `code-auto` | 同上 |
| `code-version` | 同上 |
| `code-publish` | 同上 |
| `code-init` | 同上 |
| `code-answer` | 同上 |

> **决策 D-1(修订于 2026-06-30)**:旧技能在新技能开发完成后的最后一个任务中统一删除,不保留。修订理由:用户明确要求"不保留",避免旧技能与新技能并存造成混淆;新技能开发期间旧技能暂时保留以确保开发过程可参考旧逻辑。

## 3. 接口与数据结构

### 3.1 PROCESS.md 状态机

定义了 `code-req`/`code-fix` 的执行阶段枚举:

```
阶段枚举(按执行顺序):
INIT        → 初始化(创建目录+PROCESS.md)
REQUIRE     → 需求分析(code-req) / 缺陷登记(code-fix)
DESIGN      → 软件设计
PLAN        → 任务排期
CODING      → 编码执行(循环 TASK-N)
CHECK       → 代码审查
DONE        → 完成
```

**PROCESS.md 格式契约**:
```
| 时间 | 阶段 | 状态 | 摘要 |
| --- | --- | --- | --- |
| 2026-06-30 10:00 | INIT | 开始 | 创建需求 REQ-00001 |
| 2026-06-30 10:05 | REQUIRE | 完成 | 需求分析完成,5 FR / 3 NFR |
| 2026-06-30 10:20 | DESIGN | 完成 | 软件设计完成,3 模块 |
| 2026-06-30 10:30 | PLAN | 完成 | 任务排期完成,3 任务 |
| 2026-06-30 10:35 | CODING | 开始 | TASK-001 开始 |
| 2026-06-30 10:45 | CODING | 完成 | TASK-001 完成 |
```

**断点续跑算法**:
```
function resumeFromProcess(processMdPath):
  if not exists(processMdPath):
    return "INIT"  // 新需求/缺陷
  lastLine = tail(processMdPath, 1)
  stage = parseStage(lastLine)
  if stage == "DONE":
    return "DONE"  // 已完成
  if lastLine.status == "完成":
    return nextStage(stage)  // 进入下一阶段
  else:
    return stage  // 从当前阶段重新开始
```

### 3.2 新目录结构

```
assistants/
├── rules/                       # 跨版本规范(code-rule 维护)
├── .current-version             # 当前激活版本
└── <版本号>/
    ├── RESULT.md                # 简化版看板
    ├── req/                     # 需求管理
    │   └── <REQ-NNNNN>/
    │       ├── REQUIRE.md
    │       ├── DESIGN.md
    │       ├── PLAN.md
    │       ├── TASK-001.md
    │       ├── TASK-002.md
    │       ├── CHECK.md
    │       ├── LOG.md           # 可选
    │       └── PROCESS.md
    └── fix/                     # 缺陷管理
        └── <BUG-NNNNN>/
            ├── BUG.md
            ├── DESIGN.md
            ├── PLAN.md
            ├── TASK-001.md
            ├── CHECK.md
            ├── LOG.md           # 可选
            └── PROCESS.md
```

### 3.3 简化版 RESULT.md 格式

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

> **写入规则**:仅在 `code-req`/`code-fix` 首次创建需求/缺陷时追加一行。各阶段不再改写看板。

## 4. 关键流程

### 4.1 code-ver 流程

```
用户调 /code-ver [版本号]

1. 检测 assistants/ 目录是否存在
   ├─ 不存在 → 新项目初始化流程
   │   ├─ 扫描现有代码
   │   ├─ 登记基线需求(EXISTING-NNN)
   │   ├─ 生成 INIT-REPORT.md
   │   ├─ 创建基线版本(V0.0.0)
   │   └─ 创建 assistants/.current-version
   └─ 存在 → 版本切换流程
       ├─ 读取 assistants/.current-version
       ├─ 检查当前版本是否需要发布
       │   ├─ 是 → 询问:发布后切换 / 直接切换 / 取消
       │   └─ 否 → 直接切换
       ├─ 若选"发布后切换" → 执行 code-publish 逻辑
       └─ 更新 assistants/.current-version
```

### 4.2 code-req 流程

```
用户调 /code-req <需求描述或REQ-NNN> [--auto]

1. 版本检测 + 读取 PROCESS.md
2. 从 PROCESS.md 最后阶段恢复执行
3. 按阶段顺序执行:
   REQUIRE → DESIGN → PLAN → CODING(循环) → CHECK → DONE
4. 每阶段:
   ├─ 默认模式:完成后 AskUserQuestion 确认
   └─ --auto 模式:静默继续
5. 每阶段追加 PROCESS.md
6. 完成时追加 RESULT.md 需求清单
```

### 4.3 code-fix 流程

```
用户调 /code-fix <缺陷描述或BUG-NNN> [--auto]

1. 版本检测 + 读取 PROCESS.md
2. 从 PROCESS.md 最后阶段恢复执行
3. 按阶段顺序执行:
   INIT(登记) → DESIGN → PLAN → CODING(循环) → CHECK → DONE
4. 每阶段:
   ├─ 默认模式:完成后 AskUserQuestion 确认
   └─ --auto 模式:静默继续
5. 每阶段追加 PROCESS.md
6. 完成时追加 RESULT.md 缺陷清单
```

### 4.4 code-faq 流程

```
用户调 /code-faq [查询词] [--require <路径>] [--design <路径>] [--summary] [--template <路径>]

1. 无参数 → 执行 code-answer 逻辑:跨版本搜索+回答
2. --require <路径> → 从 req/<REQ>/REQUIRE.md 导出到指定路径
3. --design <路径> → 从 req/<REQ>/DESIGN.md 导出到指定路径
   --summary → 从 DESIGN.md 提取概要信息,单独导出
4. --template <路径> → 使用指定模板填充导出
```

## 5. 方案选型

### 决策 D-1: 旧技能在最后一个任务中删除(修订于 2026-06-30)

- **选择**:新技能开发完成后,在最后一个任务中统一删除 10 个旧技能目录
- **备选**:保留旧技能文件,追加 DEPRECATED 标记
- **选择理由**:① 用户明确要求不保留;② 避免新旧技能并存造成混淆;③ 新技能开发期间旧技能暂时保留,确保可参考旧逻辑
- **权衡**:删除后无法通过旧技能名调用,但新技能已覆盖所有功能

### 决策 D-2: 历史数据不迁移

- **选择**:V0.0.0~V0.0.4 的 `assistants/` 数据保持旧结构,不迁移
- **备选**:自动迁移脚本将旧结构转为新结构
- **选择理由**:① 旧版本数据有史料价值;② 迁移风险高,可能引入数据不一致;③ 新版本从 V0.0.5 开始使用新结构
- **权衡**:旧版本数据无法通过 `code-faq` 的新查询逻辑访问

### 决策 D-3: code-auto 完全删除

- **选择**:删除 `code-auto` 技能,由 `code-req --auto` 和 `code-fix --auto` 替代
- **备选**:保留 code-auto 作为兼容别名
- **选择理由**:`--auto` 是更自然的参数形式,不需要额外技能
- **权衡**:依赖 `code-auto` 的旧脚本需更新

### 决策 D-4: code-req 与 code-fix 共享 references

- **选择**:`code-fix` 复用 `code-req` 的 `references/design.md`、`plan.md`、`coding.md`、`check.md`
- **备选**:各自独立维护所有 references
- **选择理由**:两个技能在 DESIGN/PLAN/CODING/CHECK 阶段逻辑完全一致,仅 INIT/REQUIRE 阶段不同
- **权衡**:`code-fix/SKILL.md` 需通过相对路径引用 `code-req/references/`

### 决策 D-5: rules/ 规范文件更新

- **选择**:更新 `assistants/rules/` 中引用旧目录结构/旧技能名的规范
- **具体更新**:
  - `encoding-conventions.md`:更新目录结构示例
  - `skill-conventions.md`:更新技能名和文件引用
  - `directory-conventions.md`:更新为新 `req/`+`fix/` 结构
  - `dashboard-conventions.md`:更新看板解析锚点

## 6. 规范合规性

| 规范文件 | 检查项 | 结果 |
| --- | --- | --- |
| `skill-conventions.md` 规则 1 | 技能目录结构 | ✅ 新技能在 `plugins/code-skills/skills/` 下 |
| `encoding-conventions.md` | 编号格式 | ✅ 沿用 REQ-NNNNN / BUG-NNNNN |
| `directory-conventions.md` | 目录命名 | ✅ 新命名 `req/`/`fix/` 简洁明确 |

## 7. 关联设计

| 关联设计 | 版本 | 关联点 |
| --- | --- | --- |
| REQ-00041 | V0.0.4 | 新技能继承 references/ 架构 |
| REQ-00042 | V0.0.4 | 新技能继承代码注释禁止编号约束 |
| REQ-00043 | V0.0.4 | 新技能不再引用 fix-plan.md |

## 8. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-06-30 00:00 | v1 | 初始创建 | 概要设计完成,5 模块 / 5 决策 / 4 流程 | wangmiao |
| 2026-06-30 00:00 | v2 | 增量更新 | D-1 修订:旧技能从"保留+DEPRECATED"改为"最后一个任务中删除" | wangmiao |