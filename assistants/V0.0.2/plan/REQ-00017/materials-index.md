# 材料登记 — REQ-00017
更新时间:2026-06-05 16:35
版本:V0.0.2

## 项目级规范

| 规范文件 | 关键约束 |
| --- | --- |
| **dashboard-conventions.md §规则 1** | 看板字段扩展需 3 处同步;本需求 0 新增枚举值/列/区段,**不触发** |
| **module-conventions.md §规则 1** | 资源放技能子目录;本需求不涉及 |
| **directory-conventions.md** | 技能目录结构;本需求不涉及 |
| **skill-conventions.md §规则 1** | SKILL.md frontmatter 必含 name+description;2 个 SKILL.md 字节级保留 frontmatter |
| **encoding-conventions.md §规则 1+3** | 任务编码双格式;P-1 兼容 |
| **commit-conventions.md** | `chore(code-it): ...` 风格;末尾兜底沿用 |
| **doc-conventions.md** | 文档规范;2 个 SKILL.md 增量追加遵循 |
| **naming-conventions.md** | 命名规范;P-1 锚点名称"P-1 推进看板" |
| **coding-style.md** | 编码风格;2 个 SKILL.md 增量追加沿用既有风格 |

## 上游需求
- 来源:./assistants/V0.0.2/require/REQ-00017/RESULT.md
- 提取:4 FR / 6 NFR / 8 AC / 5 边界

## 上游概要设计
- 来源:./assistants/V0.0.2/design/REQ-00017/RESULT.md
- 提取:8 决策 D-1~D-8 / 7 不变量 INV-1~7 / 6 风险 R-1~6

## 项目现状(实现细节)
- `/code-plan` SKILL.md:详 Read 结果;锚点 A=步骤 10A "#### 任务类型"前;锚点 B=步骤 16A 第 3 款前
- `/code-it` SKILL.md:详 Read 结果;锚点 C=末尾兜底"步骤 5 commit 成功"后
- 看板"任务清单"区段:沿用既有 8 列(任务编码/任务标题/关联需求/触发/来源/开发状态/测试状态/完成时间/备注)
- 看板"变更记录"区段:沿用既有 10+ 事件类型(本需求使用"任务完成")

## 本次变更源
不涉及(本次为首次设计)。
