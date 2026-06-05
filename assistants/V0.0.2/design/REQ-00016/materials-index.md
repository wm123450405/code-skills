# 材料登记 — REQ-00016
更新时间:2026-06-05 16:10
版本:V0.0.2
需求编码:REQ-00016
设计标题:`code-design` / `code-plan` 增加"快模式"+ 末尾提交无需确认

---

## 项目级规范(`./assistants/rules/**/*`)

| 规范文件 | 类别 | 关键约束摘要 | 本设计对应章节 |
| --- | --- | --- | --- |
| `skill-conventions.md` | 技能编写 | §规则 1:SKILL.md frontmatter 必含 `name` + `description`;`name` 与目录名 kebab-case 严格一致 | §4.1 模块 M-1(本设计**不**改 frontmatter,仅追加"步骤 0.5 模式选择"段) |
| `module-conventions.md` | 模块规划(DEPRECATED 仍引用 §规则 1) | §规则 1:资源放 `templates/` / `checklists/` / `guidelines/` | §4.1 SKILL.md 范围限定(本设计**不**新增子目录,**不**新增模板) |
| `dashboard-conventions.md` | 看板与版本工作空间 | §规则 1:看板字段约定扩展需 3 处同步(模板 + CLAUDE.md + 本文件) | §10 看板同步(快模式仅写 1 行 + 0 触发 3 处同步) |
| `encoding-conventions.md` | 编码格式权威源 | §规则 1-4:REQ / BUG / TASK 编码 | §4.2(本设计**不**产生新编码) |
| `marketplace-protocol.md` | Marketplace 协议 | §规则 1:`marketplace.json` 字段约束 | §10.4 0 触发(本设计**不**新增技能) |
| `doc-conventions.md` | 文档编写 | §规则 1:README 中英同次提交 + 结构对仗;§规则 2:持续维护 | §10.4 0 主动写 README |
| `migration-mapping.md` | 编码迁移追溯 | §规则 1-4:已落地/理论/EXISTING-NNN 不追溯 | (不触发) |
| `framework-conventions.md` | 框架选型(占位) | §规则 1 占位 | (不触发) |
| `naming-conventions.md` | 命名风格(占位) | §规则 1 占位 | (不触发) |
| `coding-style.md` | 代码风格(占位) | §规则 1 占位 | (不触发) |
| `commit-conventions.md` | 提交合并(占位) | §规则 1 占位 | (不触发) |
| `dependency-conventions.md` | 三方依赖(占位) | §规则 1 占位 | (不触发) |
| `directory-conventions.md` | 目录与模块(**新替代** module-conventions) | §规则 1 占位 | (不触发) |

**有效约束**:7 个文件(`skill` / `module`(DEPRECATED 仍引用) / `dashboard` / `encoding` / `marketplace` / `doc` / `migration`)
**占位规范**:6 个(不触发)
**有效 + 占位 总计**:13 个文件

---

## 上游需求

- 来源:`./assistants/V0.0.2/require/REQ-00016/RESULT.md`
- 版本:v1(2026-06-05 16:05,本次 `code-require` 完成,hash `c29484a`)
- 状态:**已完成(需求分析)**
- 提取的 FR / NFR / AC 数量:**6 FR / 10 NFR / 10 大类 AC / 10 边界场景 / 6 项 Q-locked + 2 项默认 / 6 项 v1 follow-up**

### 关键 FR-N 详细化对应

| FR | 上游标题 | 本设计对应章节 |
| --- | --- | --- |
| FR-1 | 快模式入口(双触发方式) | §4.1 模块 M-1(本设计修改既有 `code-design` 与 `code-plan` SKILL.md)+ §5 算法 1(模式选择)+ §10.1 SKILL.md 修改边界 |
| FR-2 | `code-design` 快模式跳过哪些步骤 | §4.1.1 锚点 A + §6 状态机 + §7 算法 1-3 |
| FR-3 | `code-plan` 快模式跳过哪些步骤 | §4.1.2 锚点 B + §6 状态机(平行)+ §7 算法 4-5 |
| FR-4 | 快模式末尾兜底提交行为(无需确认) | §5 算法 6(快模式末尾提交)+ §10 末尾兜底 |
| FR-5 | 完整模式完全保留(默认行为不变) | §4.2 INV-1 ~ INV-5(完整模式字节级不变) |
| FR-6 | 0 修改其他 9 个 `code-*` 技能 | §10.4 不修改文件清单 + §4.2 INV-6 |

### 关键 NFR

| NFR | 描述 | 本设计响应 |
| --- | --- | --- |
| NFR-1 | 快模式默认行为由环境变量控制 | §4.1 + §5 算法 1 模式判定规则 |
| NFR-2 | 末尾兜底提交"过程文档必含" | §5 算法 6(`git add` 范围) + §10 |
| NFR-3 | 完整模式字节级不变 | §4.2 INV-1 ~ INV-5 |
| NFR-4 | `code-auto` 不自动启用快模式 | §10.4 0 触发 `code-auto` SKILL.md |
| NFR-5 | 快模式不修改其他 11 个 `code-*` 技能 | §10.4 0 修改其他 SKILL.md |
| NFR-6 | 快模式不修改 marketplace.json / plugin.json / rules/ | §10.4 0 触发 |
| NFR-7 | 快模式不产生"半自动"行为 | §5 算法 1(完全跳过 / 完全保留)+ §5 算法 6(完全跳过 3 选 1) |
| NFR-8 | 快模式不引入"批量模式" | §4.1 + §10.4 |
| NFR-9 | 快模式错误信息可读 | §11 边界 E-M1 ~ E-M10 |
| NFR-10 | 错误码语义 | §11 |

---

## 上游概要设计

> 概要设计 = 本轮 `code-design` 产出(本文件即完成)

---

## 项目现状(本次扫描)

### 项目类型
- **类型**:Claude Code 技能集合(无业务代码、无构建系统、无测试框架、无 Lint)
- **语言/框架**:Markdown(SKILL.md + templates/ + checklists/) + JSON(marketplace.json + plugin.json)
- **关键依赖**:**0 个**运行时依赖(所有技能复用 Claude Code 平台工具集 `Bash` / `Read` / `Write` / `Edit` / `Glob` / `Grep`)

### 已有模块(本需求相关)

| 模块/路径 | 职责 | 是否可复用 |
| --- | --- | --- |
| `plugins/code-skills/skills/code-design/SKILL.md` | 既有 `code-design` 技能(15 步骤 + 7 过程文档) | ✅ 复用(本设计**修改** — 增量追加"步骤 0.5 模式选择" + 快模式分支 + 末尾兜底 3 选 1 跳过条件) |
| `plugins/code-skills/skills/code-design/templates/design.md` | 模板(本技能 RESULT.md 章节结构) | ✅ 复用(快模式下**只写核心章节**) |
| `plugins/code-skills/skills/code-design/templates/assistants-layout.md` | 目录布局参考 | ✅ 复用 |
| `plugins/code-skills/skills/code-plan/SKILL.md` | 既有 `code-plan` 技能(18 步骤 + 8 过程文档) | ✅ 复用(本设计**修改** — 同 `code-design`) |
| `plugins/code-skills/skills/code-plan/templates/plan.md` | 模板(本技能 RESULT.md 章节结构) | ✅ 复用(快模式下**只写核心章节**) |
| `plugins/code-skills/skills/code-plan/templates/task-plan.md` | 模板(任务计划章节结构) | ✅ 复用(快模式下**只写核心**) |
| `plugins/code-skills/skills/code-plan/templates/fix-plan.md` | 缺陷分支模板(本需求**不**涉及) | (不触发) |
| `plugins/code-skills/skills/code-plan/templates/assistants-layout.md` | 目录布局参考 | ✅ 复用 |

### 已有接口(本需求相关)

| 接口/方法 | 既有行为 | 快模式行为 |
| --- | --- | --- |
| `code-design REQ-NNNNN`(完整模式) | 评审单需求 → 写 7 份过程文档 + 写 RESULT.md(15 章节)+ 同步看板多区段 + 末尾兜底 3 选 1 确认 | **不变**(完整模式字节级保留,INV-3) |
| `code-design REQ-NNNNN --fast`(快模式) | (目前**无**此模式 — V0.0.2 既有 11 个 `code-*` 技能不支持快模式) | **新增**(FR-1):模式选择 = 快 + 跳过 7A-8A + 11A-12A + 13A 仅核心 + 14A 仅 1 行 + 末尾兜底跳过 3 选 1 |
| `code-design REQ-NNNNN --full`(完整模式) | (目前无此标志) | **新增**(FR-1):显式覆盖环境变量 → 走完整模式 |
| `code-design`(环境变量 `CODE_FAST_MODE=1` 已设置) | (目前**不**支持) | **新增**(FR-1):默认走快模式 |
| `code-plan REQ-NNNNN`(完整模式) | 同 `code-design` | **不变**(完整模式字节级保留) |
| `code-plan REQ-NNNNN --fast`(快模式) | (目前**无**) | **新增**(FR-1 + FR-3):模式选择 = 快 + 跳过 7A-8A + 12A-13A + 14A/15A 仅核心 + 16A 仅 1 行 + 任务清单逐行 + 末尾兜底跳过 3 选 1 |

### 已有数据模型(本需求相关)

| 数据 | 既有形态 | 快模式新增/不变 |
| --- | --- | --- |
| **design/RESULT.md 顶层结构** | 15 章节(完整模式) | 快模式**仅写核心 4 章节**:§1 / §2 / §10 / §11(简化版);其他 11 章节**不**写(FR-2) |
| **plan/RESULT.md 顶层结构** | 14 章节(完整模式) | 快模式**仅写核心 4 章节**:§1 / §2 / §4 / §11(简化版) |
| **plan/PLAN.md 顶层结构** | 8 章节(完整模式) | 快模式**仅写核心 5 章节**:§1 / §2 / §4 / §5 / §8(FR-3) |
| **过程文档清单** | 7 份(`code-design`)/ 8 份(`code-plan`) | 快模式**仅生成 3-4 份**:`materials-index.md` + `related-requirements.md` + `RESULT.md`(`code-design`);`code-plan` 额外 + `PLAN.md` |
| **看板"概要设计清单" / "详细设计汇总" 同步** | 完整模式同步 1 行 + 变更记录 + 时间戳 | 快模式同步 1 行(状态字段带"-快模式"后缀)+ **不**追加变更记录 + **不**更新时间戳(FR-2 + FR-3) |
| **末尾兜底提交 3 选 1 确认** | 完整模式弹 AskUserQuestion | 快模式**完全跳过** + 直接 `git add` + `git commit`(FR-4) |

### 已有第三方依赖
- **0 个**(所有技能复用 Claude Code 平台工具集)

### 编码与构建约定
- **本仓库无构建系统、无 Lint、无测试框架**(CLAUDE.md §需与用户确认的约定 显式声明)
- SKILL.md 遵循 `skill-conventions §规则 1`(frontmatter + 章节骨架)
- 资源放 `templates/` / `checklists/` / `guidelines/`(`module-conventions §规则 1`,DEPRECATED 但仍引用)
- 看板字段约定扩展需 3 处同步(`dashboard-conventions §规则 1`)
- 本需求**不**触发 3 处同步(快模式仅追加 1 行,**不**修改字段)

### 可复用资产
- ✅ 13 规范文件 — 全部沿用,**不**修改
- ✅ 既有 `code-design` 步骤 0a / 0 / 1-6 / 9A / 10A / 15A / 步骤 N — **完全复用**(快模式**不**改这些步骤的字面)
- ✅ 既有 `code-plan` 步骤 0a / 0 / 1-6 / 9A / 10A / 11A / 17A / 18A / 步骤 N — **完全复用**
- ❌ 既有 `code-design` 步骤 0-15 字面 — **不**重写(完整模式字节级保留,INV-1)
- ❌ 既有 `code-plan` 步骤 0-18 字面 — **不**重写(完整模式字节级保留,INV-1)
- ❌ SKILL.md frontmatter — **不**改(FR-5 + `skill-conventions §规则 1`)

---

## 现状偏离 vs 规范自检

**无偏离**。本设计 100% 遵循既有 7 个有效规范 + 不触发 6 个占位规范。
