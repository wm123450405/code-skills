# 三方依赖评估 — REQ-00020
更新时间:2026-06-06 17:30

## 本需求**0 新增**第三方依赖

| 项 | 状态 |
| --- | --- |
| 新增依赖数 | 0 |
| 新增工具链 | 0 |
| 新增运行依赖 | 0 |
| 新增构建依赖 | 0 |

## 沿用既有依赖

- 13 份规范文档(跨版本共享,本需求 0 改)
- 3 份待改 SKILL.md(本需求 0 改 frontmatter)
- 1 份需求提示词文档(`require/REQ-00020/RESULT.md`)

## 评估说明

- 本需求是**纯文档改造**,不涉及 CWD 下任何代码修改
- 改造对象:`plugins/code-skills/skills/<skill>/SKILL.md`(3 份)
- 改造内容:步骤 0b 简化 / 步骤 0b 扩展 / 任务粒度表 +3 行 / 步骤归并 M-1 ~ M-4
- 不需要新工具 / 新库 / 新框架

## 符合的规范

- `dependency-conventions` §规则 1:0 新增依赖 ✅
- `framework-conventions` §规则 1:0 引入新框架 ✅
- `marketplace-protocol` §规则 1:0 改 `marketplace.json` / `plugin.json` ✅
