# 材料登记 — REQ-00009
更新时间:2026-06-05 17:20
版本:V0.0.2

## 项目级规范
| 规范文件 | 类别 | 关键约束摘要 |
| --- | --- | --- |
| `skill-conventions.md` | 技能编写 | §规则 1:frontmatter 必含 name+description,name=目录名 |
| `module-conventions.md` | 模块规划(DEPRECATED) | §规则 1:资源放固定子目录(templates/checklists/guidelines) |
| `dashboard-conventions.md` | 看板与版本工作空间 | §规则 1:字段约定扩展需 3 处同步(本需求不触发) |
| `doc-conventions.md` | 文档编写 | §规则 1:中英同次提交;§规则 2:核心小节覆盖 |
| `marketplace-protocol.md` | Marketplace 协议 | §规则 1:skills 数组以 `./` 开头 |
| `encoding-conventions.md` | 编码格式 | §规则 1-4:任务编号 5+5 位嵌套式 |
| `migration-mapping.md` | 编码迁移 | §规则 1-4:EXISTING-NNN 不追溯 |

**占位规范(6 个,不影响)**:`directory-conventions.md` / `coding-style.md` / `commit-conventions.md` / `dependency-conventions.md` / `framework-conventions.md` / `naming-conventions.md`

## 上游需求
- 来源:`./assistants/V0.0.2/require/REQ-00009/RESULT.md`
- 版本:v1(已锁定)
- 提取的 FR / NFR / AC 数量:**7 FR / 8 NFR / ~25 AC**
- 3 项已锁定(Q-1/Q-2/Q-3)+ 4 项采纳默认(Q-4/Q-5/Q-6/Q-7)+ 1 项建议派生(Q-8)

## 上游概要设计
- 来源:`./assistants/V0.0.2/design/REQ-00009/RESULT.md`
- 版本:v1(已锁定)
- 提取的模块拆分 / 接口概要 / 数据结构 / 决策:**1 个模块 M-1 修改 + 8 决策 D-1~D-8 + 13 规范 0 冲突 0 偏离 0 授权**

### 关键交叉点
| 需求 FR | 概要设计章节 | 本详细设计章节 |
| --- | --- | --- |
| FR-1 新增守卫 | §4.1 + §7.1 | §3.1 + §4.1 |
| FR-2 守卫不通过 → 跳过 | §4.2 | §4.2 + §5.2 |
| FR-3 不留痕 | §4.2 | §4.2 + §6 |
| FR-4 不改"可测"流程 | §4.1 | §3.1.1 |
| FR-5 0 修改其他 9 技能 | §5.4 | §8 + §12 |
| FR-6 0 修改 marketplace | §5.4 | §12 |
| FR-7 报告与建议 | §6.2 | §5.2 |

## 项目现状(实现细节)
- **代码量**:`code-unit/SKILL.md` 453 行(待实施时为准)
- **既有子节结构**:`### 步骤 0` / `### 步骤 1` ~ `### 步骤 16`(原 16 步,既有)
- **既有边界结构**:`#### E-1` / `#### E-2(预留)` / `#### E-3` ~ `#### E-7`(本需求 E-2 编号冲突,**调整**:本需求"守卫不通过"边界使用 `#### E-2 守卫不通过`,与既有 `#### E-2(预留)` 替换;**或保留既有 E-2 编号 = "守卫不通过",改名既有 E-2(预留) → E-8**)
- **既有模板**:`templates/RESULT.md` / `templates/test-spec.md` / `templates/assistants-layout.md`(本需求**不**修改)
- **既有数据模型**:看板"任务清单"区段 12 列(沿用 V0.0.1)
- **既有第三方依赖**:**0**

> ⚠️ **本轮发现的实现细节冲突**:`code-unit/SKILL.md` 既有"边界 E-2"可能已存在(待 T-001 实施时确认),本需求"守卫不通过"边界建议用 `#### E-2 守卫不通过`(替换既有 E-2)或 `#### E-8 守卫不通过`(追加)。由 T-001 实施时**实际**判定:
> - 既有 E-2 是"预留"(空)→ 直接复用 E-2
> - 既有 E-2 已有内容 → 改用 E-8 / E-9 追加

## 本次变更源
- **不适用**(本计划为首次设计,无变更源)
- 未来若 `code-unit/SKILL.md` 增量追加触发变更,需重跑本技能增量更新
