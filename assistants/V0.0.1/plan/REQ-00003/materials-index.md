# 材料登记 — REQ-00003

更新时间:2026-06-04 09:15
版本:V0.0.1

## 项目级规范

| 规范文件 | 类别 | 关键约束摘要 | 本次如何遵循 |
| --- | --- | --- | --- |
| `dashboard-conventions.md` | 看板 | 看板字段约定扩展需多文件同步(`templates/version-RESULT.md` + `CLAUDE.md` + 本规范) | INV-6 0 变更;本 plan 阶段不扩展字段,仅追加区段 |
| `doc-conventions.md` §规则 1 | 文档 | README 多语言对仗 | 不修改 README(本 plan 不涉及) |
| `doc-conventions.md` §规则 2 | 文档 | 仓库级 README 必须存在并持续维护 | 不修改 README(本 plan 不涉及) |
| `marketplace-protocol.md` | marketplace | `marketplace.json` / `plugin.json` 字段约束 + 引用一致性 | INV-5 0 变更(FR-9 硬边界) |
| `module-conventions.md` | 模块 | 技能资源摆放在固定子目录(`templates/` / `checklists/` / `guidelines/`) | INV-7 仅追加 DEPRECATED 标记;新规则放 `directory-conventions.md` |
| `skill-conventions.md` §规则 1 | 技能 | SKILL.md frontmatter 必含 `name`+`description` 且与目录名一致 | INV-5 0 变更(本 plan 改 SKILL.md 正文,不改 frontmatter) |

## 上游需求

- 来源:`./assistants/V0.0.1/require/REQ-00003/RESULT.md`(v1,已锁定)
- 提取的 FR / NFR / AC 数量:**10 FR / 6 NFR / 10 AC**
- 待澄清:**3 项已锁定(Q-1/Q-2/Q-3)+ 5 项已在 design 阶段确认(Q-4/Q-5/Q-8)或采纳默认(Q-6/Q-7)**
- 关键交叉点:

| FR | 本详细设计章节 | 状态 |
| --- | --- | --- |
| FR-1(3 目标类型) | §3.1 核心架构 | 核心 |
| FR-2(6 核心规范) | §3.3 Type A 子流程(M-2) | 核心 |
| FR-3(条件性占位) | §3.3.2 占位流程(M-2 占位模式) | 核心 |
| FR-4(默认引导) | §3.3.3 引导流程(M-2 引导模式) | 核心 |
| FR-5(Type B 结构) | §3.4 Type B 子流程(M-3) | 核心 |
| FR-6(Type C 双位置) | §3.5 Type C 子流程(M-4) | 核心 |
| FR-7(类型识别) | §3.6 类型识别引擎(步骤 4 内合并) | 核心,本 plan 微调实现方式 |
| FR-8(Type A 不变) | INV-1 | 约束 |
| FR-9(不得修改) | INV-5 / INV-6 | 约束 |
| FR-10(不重写) | INV-3 / INV-4 | 约束 |

## 上游概要设计

- 来源:`./assistants/V0.0.1/design/REQ-00003/RESULT.md`(v1,已完成)
- 关键产出:
  - 核心架构:单技能 `code-rule` + 3 子流程(决策 D-1)
  - 9 个模块(M-1 ~ M-9)
  - Type A 6 分类(C-1~C-6) + 4 保留 + 1 弃用(决策 D-3,H2)
  - Type B/C 数据结构 5/4 字段(决策 D-4/D-5)
  - 9 条不变量
  - 5 commit 实施计划(决策 D-7)
- 已锁定的 design 阶段澄清:见 `design/REQ-00003/clarifications.md`(Q-1 ~ Q-8 + 3 项 design 决策 D-DESIGN-1/2/3)
- 本 plan 阶段对 design 的微调:**M-1 类型识别引擎从"独立子流程、步骤 4 之前"变更为"合并到步骤 4 拆分归类之内"**(详见 §plan 阶段微调与 `design-notes.md`)

## 项目现状(实现细节)

- 命名风格:规范文件名 kebab-case,主标题中文 + 英文括号
- 错误模型:N/A(`code-rule` 是 Markdown 文件处理技能,无运行时)
- 并发原语:N/A
- 既有相似功能:
  - `code-rule/SKILL.md` 步骤 4 关键词表(11 个旧分类):架构/模块规划/命名约定/错误处理/接口定义/数据结构/安全/性能/测试/可观测性/提交规范
  - `code-rule/templates/rule.md` 已有 8 字段规则模板(分类/规则简称/强制级别/适用范围/条款/正反示例/例外/关联规范/来源)
- 既有测试用例:N/A(技能扩展,无编程逻辑)
- 可复用的工具函数:`code-rule/SKILL.md` 步骤 4-9 的"分类确认 + 澄清 + 写文件"流程(FR-8 完全复用)
- 现有规则文件 5 个 + 本需求新建 6 个 = 实施后 11 个(`directory-conventions.md` 替代 `module-conventions.md`)

## 本次变更源(增量更新时)

> 本 plan 阶段为首版,无"变更源差异表"。

## 关联编码计划

- 同版本其他计划:
  - `plan/REQ-00001/`:Marketplace 改名,4 任务已全部完成(REQU-00001-001~004,M1 已达成)
  - `plan/REQ-00002/`:编码格式统一,8 任务待开始(M2 待开始)
- 关联点:
  - REQ-00001 与本 plan 无直接关联
  - REQ-00002 与本 plan 无直接关联(独立任务)
  - 看板 "详细设计与任务计划汇总" 区段需要追加本 plan 的一行
  - 看板 "任务清单" 区段需要追加本 plan 的所有任务
- 跨版本:本 plan 为 V0.0.1 独有;V0.0.0 为基线,无相关计划
