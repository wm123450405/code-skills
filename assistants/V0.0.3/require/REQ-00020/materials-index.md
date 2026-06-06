# 材料登记 — REQ-00020
更新时间:2026-06-06 16:45
版本:V0.0.3

## 用户输入(原始材料)

| 输入来源 | 关键摘要 | 读取状态 |
| --- | --- | --- |
| 用户命令 `/code-skills:code-require` | 4 项子需求(原文):1) `code-design` 不在概设阶段考虑架构设计目标;2) `code-plan` 架构设计目标增加封装性 / 可复用性;3) 架构设计目标增加可读性(非自然语言加详细注释);4) 按高封装性、高可复用性原则优化 `code-plan` / `code-it`,归并相同/相似执行步骤,减少 token | 已读 |

## 关键澄清(本轮无)
- 0 触发 `AskUserQuestion`(用户原文清晰,4 子需求边界明确)
- 用户笔误"code-desgin"已纠正(见历史 REQ-00011 沿用惯例)

## 项目级规范(沿用)
- `./assistants/rules/dashboard-conventions.md` §规则 1(本需求 0 触发三同步)
- `./assistants/rules/skill-conventions.md` §规则 1(frontmatter 字节级保留)
- `./assistants/rules/encoding-conventions.md` §规则 1/3(任务编号体系 0 触发)
- `./assistants/rules/marketplace-protocol`(本需求 0 触发)
- `./assistants/rules/module-conventions.md` §规则 1(过程文档摆放)
- `./assistants/rules/commit-conventions`(沿用既有)
- `./assistants/rules/doc-conventions`(本需求 0 改中英 README)
- `./assistants/rules/naming-conventions`(本需求 0 新增前缀)
- `./assistants/rules/dependency-conventions`(本需求 0 新增依赖)

## 上游需求
- 来源:用户 `/code-skills:code-require` 命令
- 提取的 FR / NFR / AC 数量:8 FR / 8 NFR / ~40 AC / 9 INV
- 关键交叉点:4 子需求映射到 FR-1 ~ FR-4

## 项目现状(本次扫描)
- V0.0.3 工作空间:`./assistants/V0.0.3/RESULT.md` 看板已初始化(沿用 V0.0.2)
- 当前里程碑:M0:工作空间就绪(已完成)
- 父版本:V0.0.2

## 关联需求(同版本)
- 暂无(本版本是 V0.0.3 第一个需求)

## 跨版本关联(V0.0.2)
- REQ-00011:`code-design` / `code-plan` 步骤 0b 设计目标确认(本需求扩展为 7 维度 + 简化为 1 维度)
- REQ-00019:`code-plan` BUG 模式同构(本需求保持 BUG 路径不动)
- REQ-00010:`code-it` 步骤 0a 前置任务守卫(本需求 0 修改,边界 E-1/E-4/E-8/E-9 合并)
- BUG-00001:脏标记文件修复(本需求沿用 24h 超时检测)

## 本次变更源
| 变更源 | 检测方式 | 变化列表 |
| --- | --- | --- |
| 需求侧(本需求) | 用户原文 4 项 | FR-1 ~ FR-4 全部锁定 |
| 概要设计侧 | 0 | 0(`code-design` 仅步骤 0b 改造,不改主体设计) |
| 规范侧 | 0 | 0(本需求 0 改规范) |
| 代码侧 | 0 | 0(本需求改 SKILL.md,无 CWD 代码改动) |
