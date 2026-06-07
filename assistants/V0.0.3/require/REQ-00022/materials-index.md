# 材料登记 — REQ-00022
更新时间:2026-06-06 18:05
版本:V0.0.3

## 用户输入(原始材料)

| 输入来源 | 关键摘要 | 读取状态 |
| --- | --- | --- |
| 用户命令 `/code-skills:code-require` | 修改 `/code-review` 技能名称为 `/code-check` | 已读 |

## 关键澄清(本轮待问,4 问)

详见 `clarifications.md`(本概设执行 AskUserQuestion 后会更新)

## 项目级规范(沿用)
- `./assistants/rules/skill-conventions.md §规则 1`(`name` 与目录名必须一致)— 本需求必须改目录名
- `./assistants/rules/marketplace-protocol.md §规则 1`(`skills[]` 路径必须指向实际存在的目录)— 本需求必须改 marketplace.json
- `./assistants/rules/migration-mapping.md §规则 5`(V0.0.0 EXISTING-NNN 不追溯)— 沿用思路:V0.0.2/V0.0.3 历史 review 产物**不**追溯替换
- `./assistants/rules/dashboard-conventions.md §规则 1`(本需求 0 触发:看板字段 0 新增)
- `./assistants/rules/doc-conventions.md §规则 1`(中英 README 同步改)
- `./assistants/rules/encoding-conventions.md`(本需求 0 触发)
- `./assistants/rules/module-conventions.md §规则 1`(本需求 0 触发)
- `./assistants/rules/commit-conventions.md`(沿用既有)
- `./assistants/rules/naming-conventions.md`(基本名 `code-check` 用户原文锁定,沿用 REQ-00021 锁定逻辑)
- `./assistants/rules/dependency-conventions.md`(本需求 0 新增依赖)

## 上游需求
- 来源:用户 `/code-skills:code-require` 命令
- 提取的 FR / NFR / AC 数量:**TBD**(待 AskUserQuestion 完成后填充)
- 关键交叉点:`code-review` → `code-check` 全局字符串替换(11 类引用方 + 4 个待澄清问题)

## 项目现状(本次扫描)
- V0.0.3 工作空间:`./assistants/V0.0.3/RESULT.md` 看板(沿用 V0.0.2;本需求前含 REQ-00020 / REQ-00021 各 1 条)
- 当前里程碑:M0:工作空间就绪(已完成)
- 父版本:V0.0.2
- 命中 250+ 个含 `code-review` 字面量的文件,影响面**极广**

## 关键澄清(本轮)

详见 `clarifications.md`
