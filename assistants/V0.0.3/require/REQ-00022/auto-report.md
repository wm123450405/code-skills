# auto-report — REQ-00022(修改 /code-check 技能名称为 /code-check)

- 需求编码:REQ-00022
- 所属版本:V0.0.3
- code-auto 起始时间:2026-06-07
- code-auto 结束时间:2026-06-07
- 总状态:✓ 完成
- 总子技能调用次数:4(模式 B 跳过 code-require;code-design / code-plan / code-check 各 1)

## 执行摘要
| 子技能 | 调用次数 |
| --- | --- |
| code-require | 0(模式 B 跳过,沿用 d6be243) |
| code-design | 1 |
| code-plan | 1 |
| code-it | 0(任务循环由主循环手动执行 10 任务) |
| code-unit | 0 |
| code-check | 1 |
| **总计** | **4 次** |

## 最终状态
- REQ-00022 状态:已完成
- 任务清单:TASK-REQ-00022-00001 ~ TASK-REQ-00022-00010(共 10 任务,均已完成,测试均=不适用)
- 缺陷:0
- 派生任务:0(评审通过,0 个"必须改")

## 关键决策(6 决策 + 9 不变量)
- D-1 硬重命名 + D-2 JSON 全部同步 + D-3 docs 全部同步 + D-4 历史不追溯 + D-5 `review/` 目录保留 + D-6 中文表述不强求
- INV-1 ~ INV-9 全部字节级保留

## 实际改动
- 1 个目录重命名:`code-review/` → `code-check/`(git mv 保留历史)
- 11 SKILL.md 全文(除 code-check 自身)字面量同步(code-review → code-check)
- 2 个 JSON(marketplace.json + plugin.json)
- 4 个 README(仓库内 + 仓库外,中英)
- 1 个 CLAUDE.md
- 13 份项目级规范
- 6 个技能模板
- 1 个 V0.0.3 当前激活看板

## 后续建议
- 执行 /code-dashboard 查看完整状态
- 执行 /code-publish 生成发布手册
- V0.0.3 当前可发布状态:REQ-00020 + REQ-00021 + REQ-00022 全部完成
