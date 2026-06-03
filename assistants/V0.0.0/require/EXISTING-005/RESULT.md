# 现有功能需求 — EXISTING-005:概要设计(code-design)

> 本文档由 `code-init` 技能基于项目现有代码生成。
> 描述的是"**代码中已实现**"的功能,而非待开发的功能。
> 未来对该功能的**修改**应通过 `code-require`(增量更新本文件)进行。
> 最后更新:2026-06-03 18:10
> 适用版本:基线版本 `V0.0.0`

## 需求概述
`code-design` 是主流程的**第三步**(版本感知):基于上游 `require/<需求编码>/RESULT.md` 的需求分析,结合 `./assistants/rules/` 项目级规范与项目结构,产出符合编码规范的概要设计文档。若 RESULT.md 已存在则做增量更新(需求侧/代码侧/规范侧变化)。同步追加/更新版本看板的"概要设计清单"与"变更记录"区段。

## 现有实现位置

| 维度 | 位置 |
| --- | --- |
| 主要文件 | `plugins/code-skills/skills/code-design/SKILL.md`(417 行) |
| 关键函数/类 | (N/A) |
| 涉及文件数 | 3(SKILL.md + 2 个模板) |
| 大致代码量 | 约 470 行 |

### 关键代码位置(可选)
- `plugins/code-skills/skills/code-design/SKILL.md` — 工作流(读 .current-version → 校验上游 → 读 require/ + rules/ → 结合项目结构 → 写 design/RESULT.md → 更新看板)
- `plugins/code-skills/skills/code-design/templates/design.md` — 概要设计模板
- `plugins/code-skills/skills/code-design/templates/assistants-layout.md`

## 用户角色与场景

### 角色
- **架构师 / 高级开发**:做新模块/新服务的架构设计、跨模块方案选型、重大重构的方案论证

### 场景
- 新模块/新服务的架构设计
- 跨模块的方案选型
- 重大重构的方案论证
- 需求变更后重新评估设计
- 已有 RESULT.md,要做增量更新(需求侧/代码侧/规范侧变化)

## 功能点(FR)

- **FR-1**:读 `.current-version` 确认激活版本
- **FR-2**:校验 `require/<需求编码>/RESULT.md` 存在(上游)
- **FR-3**:读 `./assistants/rules/` 项目级规范(只读)
- **FR-4**:读 `./assistants/<版本号>/require/<需求编码>/RESULT.md` 需求分析结果
- **FR-5**:结合项目结构与已有代码,产出符合编码规范的概要设计(基于 `design.md` 模板,含架构/模块划分/接口契约/数据流/选型论证/风险/依赖)
- **FR-6**:`design/RESULT.md` 已存在时做**增量更新**
- **FR-7**:同步追加/更新 `<版本号>/RESULT.md` 看板的"概要设计清单" + "变更记录"
- **FR-8**:引导用户:调 `code-plan` 继续

## 关键接口

### CLI
```
/code-skills:code-design REQ-2026-0001
```

### 输入
- `./assistants/<版本号>/require/<需求编码>/RESULT.md`(上游)
- `./assistants/rules/`(项目级规范,只读)
- 当前项目代码

### 写入
- `./assistants/<版本号>/design/<需求编码>/RESULT.md` — 概要设计
- `./assistants/<版本号>/RESULT.md` — 看板"概要设计清单" + "变更记录"

## 数据模型(若适用)

| 实体 | 字段 | 约束 |
| --- | --- | --- |
| 概要设计文档 | `design/<需求编码>/RESULT.md` | 字段:架构/模块划分/接口契约/数据流/选型论证/风险/依赖(由 `design.md` 定义) |
| 概要设计状态 | 待开始/进行中/已完成/已取消 | 看板字段 |
| 概要设计目录 | `design/<需求编码>/` | 与 `require/<需求编码>/` 编码对齐 |

## 验收标准(AC)

- **AC-1**:无 `.current-version` 时立即中止
- **AC-2**:`require/<需求编码>/RESULT.md` 不存在时立即中止并提示
- **AC-3**:生成的 `design/<需求编码>/RESULT.md` 符合 `design.md` 模板结构
- **AC-4**:存在 `design/RESULT.md` + 需求/代码/规范有变化 → 增量更新而非覆写
- **AC-5**:版本看板"概要设计清单"新增一行或更新状态
- **AC-6**:`code-design` 不修改项目源代码

## 关联功能

| 关联编码 | 关联点 | 影响 |
| --- | --- | --- |
| EXISTING-004 | 读 `require/<需求编码>/RESULT.md` 作为输入 | 强制上游 |
| EXISTING-003 | 读 `rules/` 作为约束 | 规范空时退化为无约束模式 |
| EXISTING-006 | `code-plan` 读 `design/<需求编码>/RESULT.md` 作为输入 | 需 `code-design` 完成才能进 `code-plan` |
| EXISTING-002 | `code-version` 是前置门 | 必须先有激活版本 |

## 已知限制/技术债

- "增量更新"靠 AI 自主判断,无 diff 工具
- 概要设计与详细设计的边界:某些团队习惯把架构/选型/数据流放在概要,把任务拆分/接口签名/测试要点放在详细;本技能依赖 AI 自主判断
- 不支持"概要设计阶段分多次"评审(只能一次产出 RESULT.md,后续靠增量更新)

## 变更记录

| 时间 | 变更类型 | 变更摘要 | 关联项 |
| --- | --- | --- | --- |
| 2026-06-03 18:10 | 需求登记 | code-init 识别并登记现有功能 EXISTING-005 | EXISTING-005 |
