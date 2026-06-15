# 材料登记 — REQ-00034

更新时间:2026-06-15 12:00
版本:V0.0.3
需求编码:REQ-00034

## 1. 项目级规范(本需求相关)

(本节沿用 code-require 既有约束,无新增)

| 规范文件 | 类别 | 关键约束摘要(本需求相关) |
| --- | --- | --- |
| skill-conventions.md | 技能 | SKILL.md frontmatter L1-3 字节级保留(INV-1) |
| module-conventions.md | 模块 | 资源文件放 templates/ 子目录(本需求**移除** `code-unit/templates/`) |
| commit-conventions.md | 提交 | `chore(<skill>):` 前缀(INV-3) |
| dashboard-conventions.md | 看板 | 看板字段三方同步(本需求触发 1 次) |
| encoding-conventions.md | 编码 | 需求编号生成端 5 位纯数字;接收端可放宽(本需求沿用) |
| plugin-conventions.md | 插件 | plugin.json / marketplace.json 注册项同步(本需求触发 1 次) |

## 2. 上游需求

- 来源:用户口头/文本输入(2026-06-15 11:30,经 1 轮 AskUserQuestion 澄清)
- 形式:1 段 ~80 字的技能合并声明
- 提取:无新材料,需求直接来自用户口头/文本输入
- 用户原始输入(verbatim):
  > 移除技能 `/code-unit`,将技能能力整合进 `/code-it` 技能中,功能代码编写完成根据需要直接编写单元测试或针对不适用的工程跳过单元测试编写。

## 3. 项目现状(本次扫描)

### 3.1 涉及文件清单(全量,Grep `code-unit|单元测试`)

#### 3.1.1 直接删除(本需求唯一"硬删除"对象)

| 路径 | 类型 | 行数 | 备注 |
| --- | --- | --- | --- |
| `plugins/code-skills/skills/code-unit/SKILL.md` | SKILL.md | 635 | `code-unit` 技能本体 |
| `plugins/code-skills/skills/code-unit/templates/RESULT.md` | 模板 | (待扫描) | `code-unit` 产出物模板 |
| `plugins/code-skills/skills/code-unit/templates/` | 目录 | (整体) | `code-unit` 模板目录 |

#### 3.1.2 必须改 5 个 SKILL.md(本需求核心)

| 路径 | 关键行(L) | 修改内容 |
| --- | --- | --- |
| `plugins/code-skills/skills/code-it/SKILL.md` | L14 | 文档头"## 目标"段:**删除**"`code-it` 不含单元测试(那属于 `code-unit` 职责)"反向声明;**改写**为"含编写单元测试(按需)或跳过" |
| `plugins/code-skills/skills/code-it/SKILL.md` | L18 | **删除**"`code-unit` 不得修改生产代码"声明(本需求后 `code-unit` 退场) |
| `plugins/code-skills/skills/code-it/SKILL.md` | L54, L83, L531, L632, L735-736 | `test-results.md` 收窄语义(从"含单元测试结果" → "项目自身的集成/冒烟测试结果") |
| `plugins/code-skills/skills/code-it/SKILL.md` | L795 | **删除**"`(可选)调 code-unit 补/验证单测`"步骤 3 |
| `plugins/code-skills/skills/code-it/SKILL.md` | L907-908 | 衔接段`code-unit` 引用**改写**为"由 `code-it` 自含" |
| `plugins/code-skills/skills/code-plan/SKILL.md` | L368, L431, L445, L454, L1105 | 测试状态字段收窄为"`code-it` 内化"(原"由 `code-unit` 另起流程"改写) |
| `plugins/code-skills/skills/code-auto/SKILL.md` | L45 | 工作目录约定段:`test/<任务编码>/` 目录**删除** |
| `plugins/code-skills/skills/code-auto/SKILL.md` | L213-227 | 子技能调用表:**删除** `code-unit` 4 行(任务路径 / 派生任务路径 / BUG 路径 / 条件触发) |
| `plugins/code-skills/skills/code-auto/SKILL.md` | L388-411 | 步骤 4.b `code-unit` 步骤**整段删除**(本需求后步骤 4 只剩 4.a 任务循环) |
| `plugins/code-skills/skills/code-auto/SKILL.md` | L432-433, L449 | 派生任务循环段:`code-unit` 引用**删除** |
| `plugins/code-skills/skills/code-auto/SKILL.md` | L624-625, L672, L692, L711, L741 | 屏幕日志 + 报告段:`code-unit` 字面**删除** |
| `plugins/code-skills/skills/code-auto/SKILL.md` | L797, L806, L834 | 衔接 + 依赖 + "不要做的事"段:`code-unit` 字面**删除** |
| `plugins/code-skills/skills/code-check/SKILL.md` | L3, L21, L40-41, L56, L72, L96, L151, L281, L608, L615 | `test/<任务编码>/` 引用全部**删除**或**改写**为"`code-it` 自含的 `test-results.md`" |

#### 3.1.3 必须改 2 个 JSON 文件(注册项)

| 路径 | 关键行 | 修改内容 |
| --- | --- | --- |
| `plugins/code-skills/.claude-plugin/plugin.json` | L15 | `keywords[]` 数组:**删除** `"code-unit"` |
| `.claude-plugin/marketplace.json` | L24 | `keywords[]` 数组:**删除** `"code-unit"` |
| `.claude-plugin/marketplace.json` | L39 | `plugins[0].skills[]` 数组:**删除** `"./skills/code-unit"` |

#### 3.1.4 必须改 4 README / CLAUDE.md(描述段)

(待 code-plan 阶段精确定位;本需求基线扫描 4 个 README 全文 + 仓库根 CLAUDE.md 引用 `code-unit` 关键词的所有位置)

| 路径 | 备注 |
| --- | --- |
| `README.md`(仓库根) | 技能表 + 工作流总览 |
| `README.en.md`(仓库根) | 同上(英文) |
| `plugins/code-skills/README.md` | 同上 |
| `plugins/code-skills/README.en.md` | 同上(英文) |
| `CLAUDE.md`(仓库根) | "code-unit" 字面引用 |

#### 3.1.5 必须改 7 个项目级规范

(待 code-plan 阶段精确定位;主要在 `encoding-conventions.md` 任务"双状态"段 + `review-checklist.md` 8.7 测试质量段 + `plugin-conventions.md` keyword 清单)

| 路径 | 备注 |
| --- | --- |
| `assistants/rules/encoding-conventions.md` | 任务"双状态"测试状态字段语义 |
| `assistants/rules/review-checklist.md` | 8.7 测试质量维度(若引用 `code-unit`) |
| `assistants/rules/skill-conventions.md` | SKILL.md 描述段引用 |
| `assistants/rules/module-conventions.md` | templates/ 子目录引用 |
| `assistants/rules/dashboard-conventions.md` | 看板字段引用 |
| `assistants/rules/plugin-conventions.md` | plugin.json / marketplace.json 同步 |
| `assistants/rules/migration-mapping.md` | 迁移映射(若引用 `code-unit`) |

#### 3.1.6 必须改其他 7 个 `code-*` 技能 SKILL.md 描述段

| 路径 | 备注 |
| --- | --- |
| `plugins/code-skills/skills/code-require/SKILL.md` | 描述段引用 `code-unit` |
| `plugins/code-skills/skills/code-design/SKILL.md` | 描述段引用 `code-unit` |
| `plugins/code-skills/skills/code-fix/SKILL.md` | 描述段引用 `code-unit` |
| `plugins/code-skills/skills/code-init/SKILL.md` | 描述段引用 `code-unit` |
| `plugins/code-skills/skills/code-publish/SKILL.md` | 描述段引用 `code-unit` |
| `plugins/code-skills/skills/code-version/SKILL.md` | 描述段引用 `code-unit` |
| `plugins/code-skills/skills/code-rule/SKILL.md` | 描述段引用 `code-unit` |
| `plugins/code-skills/skills/code-merge/SKILL.md` | 描述段引用 `code-unit` |
| `plugins/code-skills/skills/code-answer/SKILL.md` | 描述段引用 `code-unit` |
| `plugins/code-skills/skills/code-dashboard/SKILL.md` | 描述段 / 算法 4 引用 `code-unit` |
| `plugins/code-skills/skills/code-auto/SKILL.md` | 描述段引用 `code-unit` |

#### 3.1.7 历史文件保留(本需求**不**追溯)

| 范围 | 数量 | 备注 |
| --- | --- | --- |
| `assistants/V0.0.2/test/<TASK-...>/RESULT.md` | (N 个) | 历史 `code-unit` 产出,本需求**保留** |
| `assistants/V0.0.2/code/<TASK-...>/test-results.md` | (N 个) | `code-it` 历史产出 `test-results.md`,本需求**保留** |
| `assistants/V0.0.3/code/<TASK-...>/test-results.md` | (N 个) | 同上,本需求**保留** |
| `assistants/V0.0.2/require/REQ-.../auto-report.md` | (N 个) | `code-auto` 历史报告,本需求**保留**(报告中含"code-unit 跳过"日志,字节级保留) |
| `assistants/V0.0.3/require/REQ-.../auto-report.md` | (N 个) | 同上 |
| `assistants/V0.0.2/plan/REQ-00015/PLAN.md` 等 | (N 个) | 任务"测试状态"含历史 4 枚举值,本需求**不**追溯重写 |
| `assistants/V0.0.3/plan/REQ-00020-00032/PLAN.md` | (N 个) | 同上 |

### 3.2 现状结论(本需求基线)

| 维度 | 现状 | 本需求后 |
| --- | --- | --- |
| 技能数量 | 12 个 `code-*`(`code-require` / `code-design` / `code-plan` / `code-it` / `code-unit` / `code-check` / `code-fix` / `code-version` / `code-init` / `code-rule` / `code-auto` / `code-merge` / `code-answer` / `code-dashboard` / `code-publish`) | 11 个 `code-*`(**移除 `code-unit`**) |
| `code-it` 职责 | 编码 + 编译/运行 + **不含**单元测试(反向声明) | 编码 + 编译/运行 + **含**单元测试(按需)或跳过 |
| `code-unit` 职责 | 编写单元测试 + 执行测试(独立、可选) | **退场**(能力整合进 `code-it`) |
| `code-auto` 步骤 4.b | "code-unit 是否调用"判定 + 屏幕日志(恒等跳过) | **删除**整段;步骤 4 只剩 4.a |
| `code-auto` 子技能调用表 | 7 行(RE-00001 ~ RE-00007) | 减 4 行(`code-unit` 全部) |
| `code-plan` 任务"测试状态" | `已运行-通过` / `不适用` 2 枚举(REQ-00031 已收窄) | 沿用(本需求不重复收窄) |
| 模板 | `code-unit/templates/RESULT.md` + `code-it/templates/RESULT.md` | **删除**前者;`code-it` 模板新增"## 单元测试"小节 |
| plugin 注册 | plugin.json + marketplace.json 11 skills | 减 `code-unit` = 10 skills |
| 历史档案 | V0.0.2 / V0.0.3 既有 `test/` + `code-*/test-results.md` 保留 | 字节级保留(不追溯) |

### 3.3 相关既有需求(本需求相关)

| 需求 | 版本 | 关联点 | 对本需求的影响 |
| --- | --- | --- | --- |
| REQ-00031 | V0.0.3 | "外移单元测试"+"任务粒度收窄" — 5 任务已落地 | **前置基础**;本需求是 REQ-00031 的"实际删除"补完 |
| BUG-00001 | V0.0.3 | "不修改 SKILL.md"硬约束(范式) | 本需求**突破**此约束(必须改 5 SKILL.md),但 NFR 字节级保留 frontmatter 仍沿用 |
| REQ-00009 | V0.0.2 | `code-unit` 守卫"项目可测性"(7 项检查) | **随 `code-unit` 退场**;`code-it` 是否接管该守卫逻辑,见 RESULT.md FR-2 |
| REQ-00026 | V0.0.3 | SKILL.md 描述通用化扫除 | 沿用"最小化变更"原则 |
| REQ-00030 | V0.0.3 | 元技能改 + 12 维度评审 + INV 字节级保留 | 沿用 INV 校验 |
| REQ-00032 | V0.0.3 | `code-require` 屏显契约 | 沿用 |
| REQ-00033 | V0.0.3 | `code-require` 不涉及技术选型 | 沿用(本需求不涉及) |

## 4. 用户原始输入(verbatim)

> 移除技能 `/code-unit`,将技能能力整合进 `/code-it` 技能中,功能代码编写完成根据需要直接编写单元测试或针对不适用的工程跳过单元测试编写。
