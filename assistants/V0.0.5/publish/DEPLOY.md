# 部署手册 — V0.0.5

> 版本:`V0.0.5`
> 生成时间:2026-07-20
> 适用范围:V0.0.5 版本发布

## 1. 版本概述

V0.0.5 在 v2 简化版看板体系下,完成了对 REQ-00044 重构后丢失能力的补充、确认交互的恢复、模板强化与 `--confirm` 模式接入,以及多个工作流门控缺陷修复。

## 2. 适用范围

- 工作空间:`./assistants/V0.0.5/`
- 上游基线:`V0.0.4`
- 跨版本共享规范:`./assistants/rules/`

## 3. 发布前检查

| 检查项 | 状态 | 说明 |
| --- | --- | --- |
| 需求清单 | ✓ | 5 条全部 DONE |
| 缺陷清单 | ✓ | 看板登记缺陷全部 DONE |
| PROCESS.md | ✓ | 13 份全部含 DONE 记录 |
| 代码审查 | ✓ | 13/13 通过,0 必须改 |

## 4. 部署步骤

1. 拉取 V0.0.5 标签:`git fetch --tags && git checkout V0.0.5`
2. 验证工作空间:`ls assistants/V0.0.5/`
3. 加载跨版本规范:确认 `./assistants/rules/` 内容已就绪
4. 校验依赖:本版本不引入新运行时
5. 启动:无运行时入口(本仓库为技能集合)

## 5. 验证清单

- [x] `./assistants/V0.0.5/req/REQ-0004{5,6,7,8,9}/REQUIRE.md` 全部存在
- [x] `./assistants/V0.0.5/fix/BUG-0000{1..8}/BUG.md` 全部存在(看板登记子集)
- [x] `./assistants/V0.0.5/fix/BUG-0000{5,6}` 已在发布前纳入看板(本批次新增)
- [x] `./assistants/.current-version` 当前指向 `V0.0.5`(发布后切换时同步更新)

## 6. 回滚

```bash
git checkout V0.0.4
echo "V0.0.4" > ./assistants/.current-version
```

## 7. 备注

- 发布即切换的 `--publish` 入口:待用户切换到 V0.0.6 后生效
- 本文档由 `/code ver --publish` 生成,见 `references/ver/common.md`
