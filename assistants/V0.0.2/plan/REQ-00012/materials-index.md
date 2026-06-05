# 材料登记 — REQ-00012
更新时间:2026-06-05
版本:V0.0.2

## 项目级规范
| 规范文件 | 类别 | 关键约束摘要 |
| --- | --- | --- |
| doc-conventions.md | 文档 | §规则 1:中英 README 同次提交 + 章节对仗;§规则 2:核心小节覆盖(主语言版本) |
| commit-conventions.md | 提交 | 占位规则(NFR-7 要求 1 行 message 习惯) |
| directory-conventions.md | 目录 | 占位规则(本次无直接约束) |
| skill-conventions.md | 技能 | 规则 1:技能元信息一致性(本次不涉及) |
| module-conventions.md | 模块 | 模块边界(本次不涉及) |
| naming-conventions.md | 命名 | 命名约定(本次不涉及) |

## 上游需求
- 来源:./assistants/V0.0.2/require/REQ-00012/RESULT.md (v1, 2026-06-04 15:11)
- 提取的 FR / NFR / AC 数量:7 FR / 8 NFR / 约 25 AC

## 上游概要设计
- 来源:./assistants/V0.0.2/design/REQ-00012/RESULT.md (v1, 2026-06-05)
- 提取的模块拆分 / 接口概要 / 数据结构 / 决策:
  - 模块清单:2 新建(根 README 中/英)+ 1 移动(CLAUDE.md)+ 2 复用(详细 README 中/英)+ 1 删除(旧位 CLAUDE.md)
  - 接口:Markdown 内部链接(根 README → `plugins/code-skills/README.md`)
  - 数据结构:0 变更
  - 决策:0 冲突 / 1 规范-现状偏离(`§规则 2` 适用范围不含根 README)

## 项目现状(实现细节)
- 仓库类型:Claude Code marketplace 仓库(纯文档)
- 命名风格:仓库根与插件子目录双层结构(标准 GitHub 模式)
- 错误处理:N/A(本需求无代码)
- 既有相似功能:`plugins/code-skills/README.md` 38,247 bytes(已存在,作为详细文档模板)
- 可复用资产:0(本需求产出是全新文档)

## 本次变更源(增量更新时)
- 首次设计,无变更源
