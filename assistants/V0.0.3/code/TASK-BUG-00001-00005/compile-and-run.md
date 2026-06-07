# 编译与启动验证 — TASK-BUG-00001-00005
版本:V0.0.3
时间:2026-06-07 17:53

## 构建 / 启动
**N/A**

## 静态校验(2 个文件)

| 校验项 | 命令 | 时间 | 退出码 | 输出 | 结论 |
| --- | --- | --- | --- | --- | --- |
| INV-14:`code-it` 含"唯一允许的生产代码改动"声明 | `grep -n "唯一.*生产代码改动" plugins/code-skills/skills/code-it/SKILL.md` | 2026-06-07 17:53 | 0 | `14:## 唯一允许的生产代码改动场景` + `58:...(这是唯一允许的生产代码改动场景)` (命中 2 行) | ✅ 通过 |
| INV-15:`code-unit` 含"可改测试代码"边界声明 | `grep -n "可改测试代码" plugins/code-skills/skills/code-unit/SKILL.md` | 2026-06-07 17:53 | 0 | `11:## 可改测试代码边界` (命中 1 行) | ✅ 通过 |
| INV-16:2 个 SKILL.md frontmatter 字节级保留 | `git diff plugins/code-skills/skills/code-it/SKILL.md plugins/code-skills/skills/code-unit/SKILL.md \| head -20` | 2026-06-07 17:53 | 0 | diff 范围仅 `## 目标` 段后;2 个文件 frontmatter 0 变化 | ✅ 通过 |

## 修复记录
**0 修复循环**(2 个 Edit 均单次成功)
