# REQ-00013 详细设计 — 6 技能启用"编号+标题"显示

> 写入方:`code-plan` 技能
> 上游:./assistants/V0.0.2/require/REQ-00013/RESULT.md
> 上游:./assistants/V0.0.2/design/REQ-00013/RESULT.md
> 遵循规范:`./assistants/rules/` 下 13 个文件(详 `rule-compliance.md`)
> 创建时间:2026-06-05 21:30
> 状态:**已完成(详细设计)**

---

## 1. 概述

### 1.1 目标

把概要设计"8 个 SKILL.md 增量追加"落地为**可直接编码的**详细设计,产出 9 任务的编码计划(8 个 SKILL.md 增量追加 + 1 个收尾自检)。本详细设计 100% 沿用概要设计 8 项设计决策 + 8 项不变量,0 冲突 0 偏离 0 授权。

### 1.2 范围

- 8 个 SKILL.md 增量追加(`code-require` / `code-plan` / `code-fix` / `code-it` / `code-unit` / `code-review` / `code-auto` 7 个 + `code-publish` 1 协同)
- 1 个收尾任务(8 项 INV 自检 + 看板同步)
- 共 9 任务,**0**"更新看板"派生任务(REQ-00017 强约束)
- 0 新增依赖 / 0 新增模板 / 0 修改 `marketplace.json` / `plugin.json` / `assistants/rules/` 13 文件

### 1.3 与概要设计的关系

| 概要设计章节 | 本详细设计对应 |
| --- | --- |
| §1.4 8 项设计决策 D-1~D-8 | 100% 沿用 |
| §3 模块拆分 M-1~M-8 | 100% 沿用,转为 9 任务 |
| §4 接口与数据结构 | `interface-specs.md` 完整化 |
| §7 架构图(Mermaid)| `data-changes.md` + `interface-specs.md` 落地 |
| §8 关键不变量 INV-1~8 | T-009 收尾自检 |
| §9 边界与异常 E-1~E-12 | 各任务"边界与异常"段落 |

---

## 2. 上游引用

- **需求**:`./assistants/V0.0.2/require/REQ-00013/RESULT.md`(v1,2026-06-04 15:25,11 FR / 10 NFR / ~30 AC)
- **概要设计**:`./assistants/V0.0.2/design/REQ-00013/RESULT.md`(v1,2026-06-05 21:00,8 项决策 D-1~D-8 + 8 项不变量 INV-1~8)
- **规范**:`./assistants/rules/` 下 13 个文件
- **关联需求**:REQ-00005 / 00007 / 00008 / 00009 / 00010 / 00011 / 00014 / 00016 / 00017(同版本,详 `materials-index.md`)

---

## 3. 模块详细化

(详 `module-details.md`)

| 模块 | 路径 | 状态 | 锚点 | 对应任务 |
| --- | --- | --- | --- | --- |
| **M-1** | `code-require/SKILL.md` | 修改既有 | "## 工具使用约定"段后 + "## 工作流程"前 | **T-001** |
| **M-2** | `code-plan/SKILL.md` | 修改既有 | "## 工作流程"前 | **T-002** |
| **M-3** | `code-fix/SKILL.md` | 修改既有 | "## 工作流程"前 + 步骤 1 末尾追加"## 缺陷标题生成" | **T-003** |
| **M-4** | `code-it/SKILL.md` | 修改既有 | "## 工作流程"前 | **T-004** |
| **M-5** | `code-unit/SKILL.md` | 修改既有 | "## 工作流程"前 | **T-005** |
| **M-6** | `code-review/SKILL.md` | 修改既有 | "## 工作流程"前 | **T-006** |
| **M-7** | `code-auto/SKILL.md` | 修改既有 | "## 屏幕报告格式"前 | **T-007** |
| **M-8** | `code-publish/SKILL.md` | 修改既有(协同) | "PreflightChecker" 章节末尾 | **T-008** |

---

## 4. 算法与逻辑

(详 `design-notes.md` + `module-details.md`)

8 个算法(共享工具 + 6 技能标题解析入口 + `code-fix` "## 缺陷标题"小节生成 + `code-auto` 屏幕日志格式升级 + `code-publish` PreflightChecker 拼接升级)。

---

## 5. 数据结构完整变更

(详 `data-changes.md`)

**0 新增 / 0 修改 / 0 删除**既有数据模型;`code-fix` "## 缺陷标题"小节本轮**唯一新增字段**,在 `fix/.../RESULT.md` 内部。

---

## 6. 接口细节

(详 `interface-specs.md`)

- 4 个共享工具函数:`truncateTitle` / `formatReqTitle` / `formatTaskTitle` / `formatBugTitle`
- 3 个解析函数:`parseResultTitle` / `parsePlanTaskTitle` / `parseFixTitle`
- 13 类屏幕输出格式契约(启动 / 完成 / 中止 / 错误 / 派生任务 / 守卫跳过 / 报告 / 报告"未完成项"等)

---

## 7. 异常处理

(详 `risk-analysis.md`)

12 个边界场景 E-1~E-12 全部覆盖,9 任务"边界与异常"段落详 `PLAN.md`。

---

## 8. 安全要求

**N/A**(纯文档型仓库,0 鉴权 / 0 加密 / 0 审计 / 0 敏感字段处理)

---

## 9. 状态机 / 流程

**0 新增状态机**(6 技能既有状态机不变,仅屏幕输出格式升级)

---

## 10. 性能与资源

(详 `risk-analysis.md` §性能与资源)

- 屏幕输出:< 1 ms / 次
- 文件读取:`code-auto` 3 次 + `code-publish` 1 次 = 4 次文件 I/O 总计 < 200 ms
- 内存 / CPU:0 压力(纯字符串操作)

---

## 11. 测试要点

(详 `risk-analysis.md` §测试要点)

- **单元测试**:**不适用**(本仓库无构建/测试文件,`code-unit` 守卫判定"不可测")
- **静态自检**:T-001~T-008 各任务 + T-009 收尾执行 8 项 INV 自检

---

## 12. 规范遵循

(详 `rule-compliance.md`)

- ✅ 13 规范文件 0 冲突 0 偏离 0 授权
- ✅ 0 触发 `dashboard-conventions §规则 1` 3 处同步
- ✅ 0 修改 `marketplace.json` / `plugin.json` / `assistants/rules/` 13 文件
- ✅ 0 新增依赖 / 0 新增模板
- ✅ 与 REQ-00014 / REQ-00017 100% 协同

---

## 13. 待澄清 / 未决项

**0 项**

---

## 14. 变更记录

| 时间 | 版本 | 变更摘要 | 变更人 |
| --- | --- | --- | --- |
| 2026-06-05 21:30 | v1 | 初始创建:9 任务(8 SKILL.md 增量追加 + 1 收尾)+ 6 过程文档齐全(materials-index / design-notes / module-details / interface-specs / data-changes / risk-analysis / rule-compliance / clarifications)+ 8 项算法伪代码完整化(truncateTitle / 3 个 formatXxx / 3 个 parseXxx / code-fix 缺陷标题生成 / code-auto 屏幕日志)+ 8 项 INV-1~8 字节级保留 + 12 个边界场景 E-1~E-12 全覆盖;0 拆"更新看板"派生任务(REQ-00017 强约束);0 架构任务触发(本需求不满足 REQ-00014 3 触发条件);100% 沿用概要设计 8 项决策 D-1~D-8 + 8 项不变量 INV-1~8;13 规范文件 0 冲突 0 偏离 0 授权 | wangmiao |
