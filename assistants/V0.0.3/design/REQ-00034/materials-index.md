# 材料登记 — REQ-00034

更新时间:2026-06-15 13:30
版本:V0.0.3
需求编码:REQ-00034

## 1. 项目级规范(本需求相关)

| 规范文件 | 类别 | 关键约束摘要 |
| --- | --- | --- |
| skill-conventions.md | 技能 | SKILL.md frontmatter L1-3 字节级保留(INV-1) |
| module-conventions.md | 模块(已弃用,迁 directory-conventions) | 资源放 templates/ / checklists/ / guidelines/(本需求**删除** `code-unit/templates/`) |
| doc-conventions.md | 文档 | README 中英版本结构对仗;主语言版本完整 |
| dashboard-conventions.md | 看板 | 字段扩展三方同步 |
| commit-conventions.md | 提交 | `chore(<skill>):` 前缀(INV-3) |
| encoding-conventions.md | 编码 | 需求编号 5 位纯数字;接收端可放宽 |
| marketplace-protocol.md | 插件 | plugin.json / marketplace.json 引用一致 |

## 2. 上游需求

- 来源:`./assistants/V0.0.3/require/REQ-00034/RESULT.md`
- 提取:12 FR / 12 NFR / 8 大类共 50+ AC;14 任务规模(候选)

## 3. 项目现状(本次扫描)

### 3.1 待改造文件清单(全量,作为下游 `code-plan` 精确 Edit 清单)

#### 3.1.1 硬删除(1 技能 + 1 模板目录)

| 路径 | 类型 | 备注 |
| --- | --- | --- |
| `plugins/code-skills/skills/code-unit/SKILL.md` | SKILL.md | 635 行;`code-unit` 技能本体 |
| `plugins/code-skills/skills/code-unit/templates/RESULT.md` | 模板 | `code-unit` 产出物模板 |
| `plugins/code-skills/skills/code-unit/templates/` | 目录 | 整体删除 |

#### 3.1.2 必改 5 SKILL.md(本需求核心)

| 路径 | 关键位置 | 修改内容 |
| --- | --- | --- |
| `code-it/SKILL.md` | 文档头 ## 目标段 + L14 | 删除"不含单元测试"反向声明;**改写**为"含按需写单测" |
| `code-it/SKILL.md` | 步骤 9 前(## 步骤 8) | **新增**"## 步骤 8a — 项目可测性守卫"(字节级沿用 `code-unit` 步骤 0a 7 项检查) |
| `code-it/SKILL.md` | 步骤 8a 后 | **新增**"## 步骤 8.5 — 按需写单测"(自动判定 + 不弹 AskUserQuestion + 产出 `unit-test-results.md`) |
| `code-it/SKILL.md` | L18 / L795 / L907-908 | 删除"`code-unit` 不得修改生产代码"声明 + "(可选)调 code-unit 补/验证单测"步骤 3 + 衔接段引用 |
| `code-it/SKILL.md` | L54, L83, L531, L632, L735-736 | `test-results.md` 收窄语义(从"含单元测试结果" → "项目自身的集成/冒烟测试结果") |
| `code-it/SKILL.md` | L882 `test-results.md` 模板格式 | 既有章节保留;`unit-test-results.md` 新模板沿用 |
| `code-plan/SKILL.md` | L368 / L431 / L445 / L454 / L1105 | 测试状态字段收窄为"`code-it` 内化"(原"由 code-unit 另起流程"改写) |
| `code-auto/SKILL.md` | L45 | 工作目录约定段:`test/<任务编码>/` 目录**删除** |
| `code-auto/SKILL.md` | L213-227 | 子技能调用表:**删除** `code-unit` 4 行 |
| `code-auto/SKILL.md` | L388-411 | 步骤 4.b `code-unit` 步骤**整段删除** |
| `code-auto/SKILL.md` | L432-433, L449 | 派生任务循环段:`code-unit` 引用**删除** |
| `code-auto/SKILL.md` | L624-625, L672, L692, L711, L741 | 屏幕日志 + 报告段:`code-unit` 字面**删除** |
| `code-auto/SKILL.md` | L797, L806, L834 | 衔接 + 依赖 + "不要做的事"段:`code-unit` 字面**删除** |
| `code-check/SKILL.md` | L3, L21, L40-41, L56, L72, L96, L151, L281, L608, L615 | `test/<任务编码>/` 引用全部**删除**或**改写**为"`code-it` 自含的 `unit-test-results.md`" |

#### 3.1.3 必改 2 JSON

| 路径 | 关键行 | 修改 |
| --- | --- | --- |
| `plugins/code-skills/.claude-plugin/plugin.json` | L15 | `keywords[]` 数组**删除** `"code-unit"` |
| `.claude-plugin/marketplace.json` | L24 / L39 | `keywords[]` **删除** `"code-unit"` + `skills[]` **删除** `"./skills/code-unit"` |

#### 3.1.4 必改 4 README + CLAUDE.md

| 路径 | 修改 |
| --- | --- |
| `README.md`(仓库根) | 技能表 / 工作流总览:删除 `code-unit` 行;"12 个 code-* 技能" → "11 个" |
| `README.en.md`(仓库根) | 同上(英文) |
| `plugins/code-skills/README.md` | 同上 |
| `plugins/code-skills/README.en.md` | 同上(英文) |
| `CLAUDE.md`(仓库根) | 字面量删除 `code-unit` 引用 |

#### 3.1.5 必改 7 项目级规范

| 路径 | 修改 |
| --- | --- |
| `assistants/rules/encoding-conventions.md` | 任务"双状态"测试状态字段语义:沿用 REQ-00031 + 本需求 FR-5 |
| `assistants/rules/review-checklist.md` | §8.7 测试质量维度:`code-unit` 引用 → `code-it` 内化 |
| `assistants/rules/skill-conventions.md` | `code-unit` 引用 → `code-it` 内化 |
| `assistants/rules/module-conventions.md` | `code-unit/templates/` 引用删除 |
| `assistants/rules/dashboard-conventions.md` | 看板字段"code-unit 跳过"日志描述改写 |
| `assistants/rules/plugin-conventions.md` | plugin.json / marketplace.json `code-unit` 引用删除 |
| `assistants/rules/migration-mapping.md` | `code-unit` 引用 → `code-it` 内化 |

#### 3.1.6 必改 11 技能描述段

| 路径 | 修改 |
| --- | --- |
| `code-require/SKILL.md` | 描述段引用 `code-unit` 删除 |
| `code-design/SKILL.md` | 描述段引用 `code-unit` 删除 |
| `code-fix/SKILL.md` | 描述段引用 `code-unit` 删除 |
| `code-init/SKILL.md` | 描述段引用 `code-unit` 删除 |
| `code-publish/SKILL.md` | 描述段引用 `code-unit` 删除 |
| `code-version/SKILL.md` | 描述段引用 `code-unit` 删除 |
| `code-rule/SKILL.md` | 描述段引用 `code-unit` 删除 |
| `code-merge/SKILL.md` | 描述段引用 `code-unit` 删除 |
| `code-answer/SKILL.md` | 描述段引用 `code-unit` 删除 |
| `code-dashboard/SKILL.md` | 描述段引用 `code-unit` 删除 |
| `code-auto/SKILL.md` | 描述段引用 `code-unit` 删除(本身已大量删除,只改 description 字段) |
| `code-it/SKILL.md` | 描述段**改写**为"含按需写单测" |

#### 3.1.7 历史文件保留(本需求**不**追溯)

| 范围 | 处理 |
| --- | --- |
| V0.0.2 / V0.0.3 既有 `test/<TASK-...>/RESULT.md` | 字节级保留 |
| V0.0.2 / V0.0.3 既有 `code/<TASK-...>/test-results.md` | 字节级保留 |
| V0.0.2 / V0.0.3 既有 `auto-report.md` | 字节级保留 |
| 既有 12 个 REQ 的 `code/<TASK-...>/RESULT.md` + `plan/<REQ>/PLAN.md` | 字节级保留 |

### 3.2 项目类型
Claude Code skills 仓库(元技能仓库,纯 Markdown)

### 3.3 既有可复用资产
- `code-unit` 步骤 0a 7 项守卫检查(字节级沿用至 `code-it` 步骤 8a)
- `code-unit` 步骤 4 测试状态判定(简化至 2 枚举,沿用 REQ-00031 FR-3)
- `code-unit` 步骤 7 屏幕输出模板(沿用至 `code-it` 步骤 8.5)
- `code-unit` 步骤 9-12 错误修复循环 / 覆盖率(沿用至 `code-it` 步骤 11-12)

## 4. 步骤 4 预检(规范 vs 需求冲突)

- 需求要求"修改 SKILL.md"vs `skill-conventions.md` 要求"frontmatter 字节级保留"→ **不冲突**(本需求**不**改 frontmatter)
- 需求要求"删除 `code-unit/templates/`"vs `module-conventions.md` → **不冲突**(删除子目录符合资源目录约定)
- 需求要求"修改 2 JSON 注册项"vs `marketplace-protocol.md` → **不冲突**(去注册项符合 protocol)
- 需求要求"不修改工程代码"vs BUG-00001 → **不冲突**(NFR-7 锁定)

## 5. 设计目标确认(code-auto 上下文检测到,采纳 `--extensible` 默认)

- **整体设计目标**:`--extensible`(本需求触发扩展性条件 2:模块拆分预评估涉及模块数 ≥ 3 = 5 SKILL.md + 2 JSON + 4 README + 7 规范 + 11 描述段 = **29 个文件**;同时触发 REQ-00030 FR-6 触发 5"整体=--extensible")
- **触发条件判定**(本需求 REQ-00030 FR-1 锁定):
  - 触发 1(待评估三方依赖清单非空):**否**(NFR-5 0 新增)
  - 触发 2(模块拆分预评估涉及模块数 ≥ 3):**是**(29 个文件)
  - 触发 3(FR 含"多实现 / 抽象层 / 可替换 / 多套实现"语义):**否**
- **设计目标**:`--extensible`(触发条件 2 满足,采纳)

## 6. 关联需求

| 需求 | 关联点 |
| --- | --- |
| REQ-00031 | "外移单元测试"+"任务粒度收窄" — **前置依赖** |
| REQ-00009 | `code-unit` 守卫"项目可测性"(7 项检查) — **强继承** |
| BUG-00001 | 5 技能加"不修改 SKILL.md"硬约束 — **兼容性** |
| REQ-00026 | SKILL.md 描述通用化扫除 — 最小化变更原则 |
| REQ-00030 | 元技能改 + 12 维度评审 + INV 字节级保留 |
| REQ-00032 | `code-require` 屏显契约 |
| REQ-00033 | `code-require` 不涉及技术选型 |
