# 材料登记 — REQ-00027
更新时间:2026-06-08 15:35
版本:V0.0.3

## 项目级规范
| 规范文件 | 类别 | 关键约束摘要 |
| --- | --- | --- |
| skill-conventions.md | 技能元信息 | SKILL.md frontmatter 必含 `name` + `description`,`name` 与目录名一致 |
| doc-conventions.md | 文档编写 | README 多语言对仗;主语言 README 必须含完整小节 |
| encoding-conventions.md | 编码格式 | REQ/BUG/TASK 3 类编码权威源;生成端 5 位纯数字 |
| module-conventions.md | 模块 | 技能目录结构约定 |
| marketplace-protocol.md | 市场协议 | marketplace.json + plugin.json 路径/关键词/description 一致性 |
| commit-conventions.md | 版本控制 | commit 格式 / 分支策略 / PR / merge |
| coding-style.md | 代码风格 | 编码风格 |
| directory-conventions.md | 目录 | 目录约定 |
| framework-conventions.md | 框架 | 框架约定 |
| dashboard-conventions.md | 看板 | 看板 3 区段解析锚点 |
| dependency-conventions.md | 依赖 | 依赖管理 |
| naming-conventions.md | 命名 | 命名约定(占位) |
| migration-mapping.md | 迁移映射 | 新旧编码追溯表(占位) |

## 上游需求
- 来源:./assistants/V0.0.3/require/REQ-00027/RESULT.md (v1,2026-06-08 15:20)
- 提取的 FR / NFR / AC 数量:4 FR / 4 NFR / 4 类 AC(共 12 条 AC)
- 关键交叉点(每条 FR 对应的设计章节):
  - FR-1 → RESULT.md §2.1 模块 1(code-fix 重写)
  - FR-2 → RESULT.md §2.2 模块 2(code-auto 模式 C)
  - FR-3 → RESULT.md §2.1 步骤 4 状态推进表
  - FR-4 → RESULT.md §2.2 子技能调用表附加约束

## 上游概要设计
- 来源:./assistants/V0.0.3/design/REQ-00027/RESULT.md (v1,2026-06-08 15:30)
- 提取的模块拆分 / 接口概要 / 数据结构 / 决策:
  - 模块拆分:修改 1(code-fix)+ 修改 2(code-auto)+ 复用 4(code-plan/it/unit/check)
  - 数据结构:0 变更
  - 决策:4 项(状态机收敛 / 模式 C / BUG 路径子技能调用 / `code-check` 身份)
  - 不变量:8 条

## 项目现状(实现细节)
- 命名风格:全小写 kebab-case(目录名)+ PascalCase(章节标题)
- 错误模型:本仓库 0 错误处理代码
- 并发原语:本仓库 0 并发
- 既有相似功能:`code-auto` 模式 A / B 已存在;`code-fix` 既有"全生命周期跟踪"模式
- 既有测试用例:本仓库 0 单测
- 可复用的工具函数:`AskUserQuestion` 工具(本仓库具备)

## 本次变更源(增量更新时)
N/A(本轮为首次设计)
