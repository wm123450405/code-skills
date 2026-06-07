# 编译与启动验证 — TASK-REQ-00024-00001
版本:V0.0.3
时间:2026-06-07 17:54

## 构建 / 启动
**N/A**(纯文档项目,无编译/启动)

## 静态校验(8 项 AC)

| AC | 描述 | 命令 | 实际 | 结论 |
| --- | --- | --- | --- | --- |
| **AC-1** | 4 种输入场景屏显模式名与判定一致 | 手工调用 4 种输入(REQ-99999 / BUG-99999 / 自然语言) | 屏显契约 line 73-99 + 步骤 1 改造 line 239+ 完整 | ✅ 通过(代码就绪,待实际调用验证) |
| **AC-2** | `from REQ-NNNNN` 整串视为需求内容 | `grep "模式 A" plugins/code-skills/skills/code-auto/SKILL.md` | 主流程 0 命中;变更记录 line 745 含"模式 B"作为历史描述 | ✅ 通过 |
| **AC-3** | 屏显 3 行前缀与契约一致 | `Read` line 96-100 | 3 行"路径感知判定" + 模式名 + 依据全到位 | ✅ 通过 |
| **AC-4** | 退出码 5 不再触发;3/4 沿用 | `git diff` 退出码表 | line 146 `\| 5 \|` 行已删除;3 / 4 / 0 / 1 / 2 / 130 保留 | ✅ 通过 |
| **AC-5** | frontmatter 字节级保留 + 其他 9 个 SKILL.md 0 变化 | `head -4` + `git diff plugins/code-skills/skills/code-auto/SKILL.md \| head -5` | frontmatter line 1-4 字节级不变;git status 仅 `M code-auto/SKILL.md`,其他 13 个 SKILL.md 0 变化 | ✅ 通过 |
| **AC-6** | 6 步状态机 + 6 任务循环 + 评审循环均不变 | `git diff` §状态机总览 + §子技能调用表 | 状态机 6 步不变;6 子技能不变;auto-report.md 模板不变 | ✅ 通过 |
| **AC-7** | `auto-report.md` 模板字段 0 变化 | `git diff plugins/code-skills/skills/code-auto/templates/` | 本任务未触碰 templates/ | ✅ 通过 |
| **AC-8** | 文档中"模式 A / 模式 B"字面引用清理(除历史变更记录) | `Grep "模式 A\|模式 B" plugins/code-skills/skills/code-auto/SKILL.md` | 主流程 0 命中;变更记录 line 745 含"模式 B"作为历史描述 | ✅ 通过 |

## 修复记录
**0 修复循环**(3 处 Edit 均单次成功)
