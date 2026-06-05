# 材料登记 — REQ-00008
更新时间:2026-06-05 16:00
版本:V0.0.2
需求编码:REQ-00008
详细设计标题:`/code-review` 整版本模式 — 详细设计与编码计划

---

## 项目级规范(`./assistants/rules/**/*`)

> 13 个规范文件,7 强约束 + 6 占位;与 `design/REQ-00008/materials-index.md` 详表同构,本节简表。

| 规范文件 | 类别 | 关键约束 | 本详细设计对应章节 |
| --- | --- | --- | --- |
| `skill-conventions.md` | 技能编写 | §规则 1:SKILL.md frontmatter 必含 `name` + `description` | §4.1 模块 M-1 — 既有 frontmatter 字节级不变(INV-1) |
| `module-conventions.md` | 模块规划(DEPRECATED 仍引用 §规则 1) | 资源放 `templates/` / `checklists/` / `guidelines/` | §4.1 SKILL.md 范围限定;本设计**不**新增子目录(沿用 D-1) |
| `dashboard-conventions.md` | 看板 | §规则 1:字段约定扩展需 3 处同步;本设计**不**扩展字段 | §11 看板同步(0 触发 3 处同步) |
| `encoding-conventions.md` | 编码格式 | §规则 1-4:REQ / BUG / TASK 编码 | §6 接口 3 — 派生任务字段完全沿用模式 1 既有(INV-3) |
| `marketplace-protocol.md` | Marketplace | §规则 1:`marketplace.json` 字段约束 | §11.4 不修改(FR-8.AC-8.1) |
| `doc-conventions.md` | 文档 | §规则 1:README 中英同次;§规则 2:持续维护 | §11.4 0 主动写 README(Q-7 采纳默认) |
| `migration-mapping.md` | 编码迁移 | §规则 1-4:已落地/理论/EXISTING-NNN 不追溯 | (不触发) |

**占位规范(6 个,不影响)**:`directory-conventions.md` / `framework-conventions.md` / `naming-conventions.md` / `coding-style.md` / `commit-conventions.md` / `dependency-conventions.md`

**有效 + 占位 总计**:13 个文件

---

## 上游需求(`./assistants/V0.0.2/require/REQ-00008/RESULT.md`)

- 版本:v1(2026-06-04 14:07 锁定)
- 提取:**9 FR / 8 NFR / ~30 AC / 9 边界 / 7 项 Q-locked + 3 项采纳默认**
- 关键 FR-N 详细化对应:

| FR | 上游标题 | 本详细设计对应章节 |
| --- | --- | --- |
| FR-1 | 增加"无参"入口 | §4.1 + §5 算法 1(模式选择) |
| FR-2 | 整版本模式 — 评审范围过滤 | §5 算法 2(过滤需求) |
| FR-3 | 整版本模式 — 双写 REPORT | §5 算法 3(写聚合)+ §5 算法 4(单需求) |
| FR-4 | REVIEW.md 聚合文件结构 | §6.1 数据结构 — 5 章节 |
| FR-5 | 派生任务(沿用模式 1) | §5 算法 5(派生任务追加) |
| FR-6 | 与模式 1 完全兼容 | §4.2 INV-1/INV-2 约束 |
| FR-7 | 不修改 `code-review` 现有行为 | §4.2 INV-1/INV-4 约束 |
| FR-8 | 不修改其他 9 个 `code-*` 技能 | §11.4 0 触发 + 0 修改文件清单 |
| FR-9 | 报告与建议 | §5 算法 6(报告) |

---

## 上游概要设计(`./assistants/V0.0.2/design/REQ-00008/RESULT.md`)

- 版本:v1(2026-06-05 15:55,本次 `code-design` 完成)
- 状态:**已完成(首次概要设计)** — hash `9207f8c`
- 提取:**1 修改 + 0 新增 + 4 复用 = 5 模块**
- 关键交叉点:
  - §10.1 SKILL.md 增量追加边界 → §4.1 本详细设计模块 M-1 详细化
  - §7 REVIEW.md 5 章节结构 → §6.1 数据结构 — 5 章节字段级
  - §6 整版本模式状态机 → §5 算法 1-6
  - 6 项 DQ(关键决策)→ §3 规范遵循(全部沿用)
  - 10 项不变量(INV-1 ~ INV-10)→ §4.2 不变量自检
  - 6 类风险与缓解 → §8 风险分析(详化)

---

## 项目现状(实现细节 — 锚定 SKILL.md 既有字面)

> 本次 `code-plan` **不**重新读 `code-review/SKILL.md` 全文(已熟悉);只锁定**增量追加锚点**的具体字面。

### 既有 SKILL.md 关键锚点(L106-115 + L308-313)

#### 锚点 A(插入"步骤 1.5 模式选择"的位置)

**L106-109 字面**(严格保留):
```markdown
### 步骤 1 — 收集需求编码
- 若用户未提供,主动询问
- 校验 `./assistants/<版本号>/require/<需求编号>/RESULT.md` 与 `./assistants/<版本号>/plan/<需求编号>/PLAN.md` 都存在,否则:
  > 错误:上游缺失。请先运行 `code-require` 与 `code-plan` 产出必要文档。

### 步骤 2 — 定位 / 创建工作目录
- 检查 `./assistants/<版本号>/review/<需求编号>/` 是否存在
- 不存在 → `mkdir -p` 创建
- 存在 → 复用(意味着重跑,基于上次的发现做增量评审)
```

**插入位置**:`### 步骤 2 — 定位 / 创建工作目录` 之前(L111 上方)
**插入内容**:新增 `### 步骤 1.5 — 模式选择(本需求新增,整版本模式入口)` 段(详 §4.1 模块 M-1 + §5 算法 1)
**字节级不变量**:L106-110 字面**完全不变**(INV-1)

#### 锚点 B(插入"整版本模式 — 评审范围与适用场景"附录的位置)

**L308-313 字面**(步骤 15 末尾):
```markdown
### 步骤 15 — 汇报
- 评审了多少任务
- 发现了多少问题(按严重程度)
- 派生了多少新"审查改修"任务(列出任务编码)
- 哪些发现是"回 code-plan / code-design"的(若发现)
- 整体结论
- **版本看板同步情况**
```

**插入位置**:L313(`**版本看板同步情况**` 段后) + 空行 + `---` 分隔符 + 空行 + 新增 `## 整版本模式 — 评审范围与适用场景` 节
**字节级不变量**:L308-313 字面**完全不变**(INV-1)

### 既有 frontmatter 字面(L1-3 字节级不变 INV-4)

```yaml
---
name: code-review
description: 代码评审(版本感知)...
---
```

### 派生任务追加格式(INV-3 — 完全沿用模式 1 既有)

`code-review` 既有 SKILL.md 步骤 10 已支持"追加派生任务到 PLAN.md";整版本模式对每个被评审需求的 PLAN.md 追加 1 行,字段:

```markdown
| 任务编号 | 需求 | 类型 | 触发/来源 | 标题 | 开发状态 | 测试状态 | 涉及文件 | 完成时间 | 提交哈希 | 关联任务 |
| TASK-REQ-NNNNN-NNNNN | REQ-NNNNN | 修改 | 审查改修 | 修复 F-X(必须改) | 待开始 | 未编写 | ... | ... | ... | REQ-NNNNN-NNNNN |
```

> **关键**:本设计**不**自己生成 TASK 编码;编码生成走 `code-plan` 既有规则(`encoding-conventions §规则 4`:`code-plan` 阶段生成,`code-review` 不应重复)

### 既有 SKILL.md 既有 frontmatter 字面锚点(已确认)

- L1-3 frontmatter 字节级保留(INV-4 强约束)
- L106-110 步骤 1 字面保留(INV-1)
- L111-114 步骤 2 字面保留(INV-1)
- L308-313 步骤 15 字面保留(INV-1)

---

## 既有相似功能(模式 1 单需求评审)

- 既有 `code-review REQ-NNNNN` 模式 1 行为**完全不变**(FR-7.AC-7.1)
- 模式 1 派生任务追加到 `PLAN.md` 既有逻辑直接复用(DQ-5.B)
- 模式 1 模式 1 单需求 REVIEW-REPORT.md 字面 100% 一致(FR-6.AC-6.1 + INV-2)

---

## 关联编码计划(本版本其他)

| 关联计划 | 关联点 | 对本计划的影响 |
| --- | --- | --- |
| `plan/REQ-00004/`(V0.0.2) | `code-dashboard` 解析锚点 | 本设计步骤 1.5 解析需求状态沿用 `code-dashboard` 算法 1(NFR-8) |
| `plan/REQ-00006/`(V0.0.2) | `code-publish` 前置检查 | T-003 文档同步 5 处时不影响 `code-publish` 区段 |
| `plan/REQ-00007/`(V0.0.2) | `code-auto` 评审循环 | `code-auto` 继续用模式 1(本设计**不**触发 `code-auto` 升级) |
| `plan/REQ-00014/`(V0.0.2) | 任务拆分新规则(按功能点) | 本设计 T-001 = 1 个完整功能点(增量改 SKILL.md + 0 架构任务触发) |

---

## 本次变更源(本设计为首次,无变更源)

| 变更源 | 检测方式 | 变化列表 |
| --- | --- | --- |
| 需求侧 | 上游 RESULT.md 变更记录 | **0**(本设计为 v1 首次) |
| 概要设计侧 | 上游 RESULT.md 变更记录 | **0**(本设计为 v1 首次) |
| 规范侧 | `./assistants/rules/` 对比 | **0**(13 文件未变) |
| 代码侧 | 重跑项目探索 | **0**(`code-review/SKILL.md` 既有未变;既有的 3 模板 + 1 清单 + V0.0.1 评审产物 3 份未变) |
