# 关联设计 — REQ-00001
更新时间:2026-06-03 20:25
版本:V0.0.1

## 扫描范围
- 本版本(V0.0.1):`./assistants/V0.0.1/design/*/RESULT.md`
- 跨版本(可选):`./assistants/*/design/*/RESULT.md`
- 扫描关键词:`marketplace`、`name`、`install`、`plugin`、`REQ-`、`code-skills@`

## 扫描结果

### V0.0.1(本版本)
| 关联设计 | 关联点 | 影响 | 备注 |
| --- | --- | --- | --- |
| (本设计为首个,无同版本其他设计) | — | — | — |

### 跨版本
| 关联设计 | 关联点 | 影响 | 备注 |
| --- | --- | --- | --- |
| (无 V0.0.0 概要设计) | — | — | V0.0.0 仅 `require/EXISTING-NNN/`,无 `design/` 子目录 |

## 横向关联需求(影响本设计的下游需求)

| 关联需求 | 关联点 | 对本设计的影响 |
| --- | --- | --- |
| **REQ-00002**(编码统一) | REQ-00002 v2 锁定 TASK 编码为 `TASK-REQ-<REQ 数字段>-NNNNN`,并计划在 `code-it` 阶段清理 SKILL.md / 模板 / README / CLAUDE.md 中残留的 `REQ-2026-0001` 字符串 | **弱**:本设计产出的 `code/REQ-00001-NN/RESULT.md` 等下游路径(在 `code-it` 阶段产生)届时可能需要再补一次小批量重命名(从 `<REQ-00001>-NN` → `TASK-REQ-00001-NNNNN`);但本设计的概要设计阶段不涉及此维度(任务拆分在 `code-plan` 阶段) |
| (V0.0.0 EXISTING-001 ~ EXISTING-010) | V0.0.0 基线需求的 10 个 `RESULT.md` 中含大量 `REQ-2026-0001` 示例字符串(EXISTING-004 / EXISTING-005 / EXISTING-006 / EXISTING-007 / EXISTING-008 / EXISTING-010) | **弱**:本需求 FR-7 显式禁止修改 V0.0.0;这些旧示例字符串在 REQ-00002 实施阶段统一清理(沿用 REQ-00002 的"统一 SKILL.md / 模板 / README 旧编码"工作) |

## 关联规范(已在 `rule-compliance.md` 中详细分析)

| 规范 | 关联 |
| --- | --- |
| `marketplace-protocol.md §规则 1.3` | marketplace 与 plugin 的 `name` 同步约束,本需求保持(plugin 标识不变) |
| `doc-conventions.md §规则 1` | README 中英结构对仗 + 同次提交同步 |
| `doc-conventions.md §规则 2` | README 命令/路径必须反映仓库实际状态 |

## 无关联确认

- 本设计不涉及任何**应用代码模块** → 无 `module-breakdown.md` 维度的"复用既有模块 / 扩展既有模块"
- 本设计不涉及任何**对外 API** → 无 `api-standards` 维度的契约变更
- 本设计不涉及任何**数据模型** → 无 `data-modeling` 维度的实体变更
- 本设计不涉及任何**部署形态** → 本仓库是"纯文档/清单/SKILL.md 集合",无部署概念
