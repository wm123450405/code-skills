# 材料登记 — REQ-00041
更新时间:2026-06-29 13:50
版本:V0.0.4

## 项目级规范

| 规范文件 | 类别 | 关键约束摘要 |
| --- | --- | --- |
| skill-conventions.md | 技能编写 | name+description frontmatter;不得包含开发痕迹 |
| encoding-conventions.md | 编码格式 | 编码格式权威定义 |

## 上游需求

- 来源:./assistants/V0.0.4/require/REQ-00041/RESULT.md
- 提取的 FR / NFR / AC:8 FR / 5 NFR / 10 AC
- 关键交叉点:FR-2(SKILL.md 骨架化)→ 详细设计 §4 模块 1/3/5/7;FR-4(6 语言文档)→ 详细设计 §4 模块 2/4/6/8

## 上游概要设计

- 来源:./assistants/V0.0.4/design/REQ-00041/RESULT.md
- 提取的模块拆分:8 个模块(4 个 SKILL.md 修改 + 4 个 references/ 目录)
- 设计目标:`--extensible`

## 项目现状(实现细节)

- 项目类型:纯 Markdown 文档项目(Claude Code 技能)
- 4 个目标 SKILL.md 文件:code-design(~669 行)/code-plan(~1187 行)/code-it(~1551 行)/code-check(~703 行)
- 无构建系统/测试框架/运行命令