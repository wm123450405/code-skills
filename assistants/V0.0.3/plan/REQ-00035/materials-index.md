# 材料登记 — REQ-00035
更新时间:2026-06-15 19:15
版本:V0.0.3

## 项目级规范

| 规范文件 | 类别 | 关键约束摘要 |
| --- | --- | --- |
| encoding-conventions.md | 编码格式 | TASK-(REQ\|BUG)-\d{5}-\d{5} 5+5 位嵌套;接收端宽松 |
| dashboard-conventions.md | 看板解析 | `^## .*$` 定位 + `^\| .* \|$` 匹配;字段约定不扩展(NFR-7) |
| skill-conventions.md | 技能 SKILL.md | 锚点(不修改 frontmatter / 不修改既有章节) |
| module-conventions.md | 模块边界 | 改既有模块不改边界;不触发本需求 |
| doc-conventions.md | 文档 | 变更记录 / 模板规范 |
| marketplace-protocol.md | marketplace 协议 | plugins/ 子目录布局;不触发本需求 |
| migration-mapping.md | 旧→新映射 | 不触发本需求 |

## 上游需求

- 来源:./assistants/V0.0.3/require/REQ-00035/RESULT.md (v1)
- 提取的 FR / NFR / AC 数量:8 FR / 9 NFR / 22 AC
- 关键交叉点(每条 FR 对应的设计章节):
  - FR-1(判定准则)→ §5.1 算法
  - FR-2(决策记录)→ §5.2 算法
  - FR-3(SKILL.md 改造)→ §4 模块 + §10 状态机
  - FR-4(模板新增)→ §4 M4 模块
  - FR-5(编排同步)→ §4 M2 模块
  - FR-6(看板解析)→ §4 M3 模块
  - FR-7(变更记录)→ §5.3 算法
  - FR-8(步骤跳过)→ §10 状态机

## 上游概要设计

- 来源:./assistants/V0.0.3/design/REQ-00035/RESULT.md (v1)
- 提取的模块拆分 / 接口概要 / 数据结构 / 决策:
  - 模块拆分:7 个改写点(M1×5 + M2 + M3)+ 5 模板新增(M4)
  - 接口概要:0 触发(本设计不引入新外部接口)
  - 数据结构:`ProcessDocDecision` + `ProcessDocDecisionsFile`
  - 关键决策:4 条(D-1 判定器位置 / D-2 决策文件有时无 / D-3 看板变更记录语义 / D-4 8.13 派生级别)

## 项目现状(实现细节)

- 命名风格:小写连字符(`code-require` / `code-it` 等)
- 错误模型:不适用(本仓库为 markdown 文件 + frontmatter 范式,无运行时错误)
- 并发原语:不适用
- 既有相似功能的实现风格:`code-design` 步骤 0b.0 / `code-plan` 步骤 0b.0(同源引用公共段)→ 本设计沿用此模式
- 既有测试用例的风格与覆盖度:不适用(纯元技能改,无单元测试,沿用 REQ-00031 范式)
- 可复用的工具函数/中间件:`code-design` 步骤 0b.0 / `code-plan` 步骤 0b.0 的 24 小时超时判断 / 三种决策 / 约束定义 → 本设计可复用其结构

## 本次变更源(增量更新时)

- 不适用(本设计为首次)
