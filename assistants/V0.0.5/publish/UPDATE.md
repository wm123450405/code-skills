# 更新日志 — V0.0.4 → V0.0.5

> 本版本相对 V0.0.4 的更新摘要。

## 新增需求(5)

| 编号 | 标题 | 摘要 |
| --- | --- | --- |
| REQ-00045 | 补充 REQ-00044 重构后丢失的旧技能能力 | 6 语言适配文件 + coding/check/require/design/plan/common 增强 + SKILL.md 5 处更新 |
| REQ-00046 | 恢复旧技能中与用户确认的交互方式 | require/design/plan 三阶段确认机制重塑 |
| REQ-00047 | 优化 REQUIRE.md 和 BUG.md 保留用户原始输入 | REQUIRE.md §0 原始输入段、BUG.md 强化 |
| REQ-00048 | 优化 code-dashboard 技能 | SKILL.md 456→306 行 (-33%) |
| REQ-00049 | 为 code-req、code-fix 增加 --confirm 模式 | common.md 三态阶段执行器 |

## 修复缺陷(8)

| 编号 | 标题 | 根因 |
| --- | --- | --- |
| BUG-00001 | code-req 未按阶段顺序执行 | 缺少阶段门控机制 |
| BUG-00002 | REQ-00044 重构后项目说明文档未更新 | 编码规范缺失同步规则 |
| BUG-00003 | 工作流强制指令位置不够靠前 | SKILL.md 前置指令薄弱 |
| BUG-00004 | DONE 阶段兜底提交未触发 | DONE 阶段指令不够显式 |
| BUG-00005 | 根 README.md 引用旧技能名 | 未及时同步 7 技能体系 |
| BUG-00006 | code-fix 缺少产出物强制约束 | 缺少强制阶段门控与产出物标注 |
| BUG-00007 | REQ-00049 执行中遗漏用户确认环节 | 3 个确认遗漏 |
| BUG-00008 | REQ-00049 阶段 references 未适配三态 | 6 个 reference 未适配 |

## 不兼容变更

无 API/接口级破坏性变更;SKILL.md 章节结构调整对消费方透明。

## 升级指引

- 用户:`/code ver V0.0.6` 切换后,旧流程仍按既有 SKILL.md 行为运行
- 维护者:`./assistants/rules/` 跨版本共享,无需迁移
