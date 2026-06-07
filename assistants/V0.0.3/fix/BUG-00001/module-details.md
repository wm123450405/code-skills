# 模块详细化 — BUG-00001
更新时间:2026-06-07
版本:V0.0.3

> 本文档是 `code-plan BUG-00001` 阶段的辅助过程文档。详细内容已并入 `RESULT.md §7.4 模块详细化`(6 个 SKILL.md 各加 1 段)。本文档作为索引与速查表。

## 模块清单(6 个目标 SKILL.md)

| 模块(技能) | 路径 | 改动类型 | 锚点(语义化) | 触发来源 | 关联任务 |
| --- | --- | --- | --- | --- | --- |
| `code-require` | `plugins/code-skills/skills/code-require/SKILL.md` | 新增条目(段首插入) | `> §不要做的事` | BUG-00001 §4 方向 1 | TASK-BUG-00001-00001 |
| `code-design` | `plugins/code-skills/skills/code-design/SKILL.md` | 新增条目(段首插入) | `> §不要做的事` | BUG-00001 §4 方向 1 | TASK-BUG-00001-00002 |
| `code-plan` | `plugins/code-skills/skills/code-plan/SKILL.md` | 新增条目(段首插入) | `> §不要做的事` | BUG-00001 §4 方向 1 | TASK-BUG-00001-00003 |
| `code-fix` | `plugins/code-skills/skills/code-fix/SKILL.md` | 新增条目(段首插入) | `> §不要做的事` | BUG-00001 §4 方向 1 | TASK-BUG-00001-00004 |
| `code-it` | `plugins/code-skills/skills/code-it/SKILL.md` | 新增小节 | `> §目标 段后` | BUG-00001 §4 方向 2 | TASK-BUG-00001-00005 |
| `code-unit` | `plugins/code-skills/skills/code-unit/SKILL.md` | 新增小节 | `> §目标 段后` | BUG-00001 §4 方向 3 | TASK-BUG-00001-00005 |

## 关键调用顺序(无运行时,纯文档)

无函数/方法调用顺序。本修复**不**涉及运行时调用,仅追加 6 段静态文本。

## 状态归属

无运行时状态。本修复**不**新增任何状态变量、状态机、状态字段。

## 与概要设计的对应

- `fix/BUG-00001/RESULT.md §4 修复方案` 方向 1 → `code-require` / `code-design` / `code-plan` / `code-fix` 加硬约束
- `fix/BUG-00001/RESULT.md §4 修复方案` 方向 2 → `code-it` 加"唯一可改"声明
- `fix/BUG-00001/RESULT.md §4 修复方案` 方向 3 → `code-unit` 加"可改测试代码"边界
- `fix/BUG-00001/RESULT.md §4 修复方案` 方向 4 → **不**实施(本轮 0 触发 `code-rule`)
- `fix/BUG-00001/RESULT.md §4 修复方案` 方向 5 → **不**回滚历史 commit(仅约束未来)

## 符合的规范

- `skill-conventions.md §规则 1`(SKILL.md frontmatter 字节级保留)
- `encoding-conventions.md §规则 1-4`(BUG 任务编号 5+5 位嵌套式)
- `dashboard-conventions.md §规则 1`(0 字段扩展,0 三同步)
