# 缺陷分析 — BUG-00011 · 技能中残余无意义板块清理

> 所属版本:V0.0.6
> 创建时间:2026-07-24 10:05

## 1. 缺陷描述

### 用户原始报告

> 需求 `REQ-OPT-00002` 中最后要求整理各个技能中的各个板块内容,若无实际有效的内容应当移除对应版本,目前发现依然有残余的无意义板块未被清洗或移除(比如主技能中最后一个板块"## 不要做的事"中已经没有具体的事项了,该板块应该被清理),请再次检查所有的技能,移除无意义的板块及其内容

### 复现步骤
1. 打开任一技能 SKILL.md(如 `plugins/code-skills/skills/code/SKILL.md`)
2. 滚到末尾查看"## 不要做的事"板块
3. 观察到该板块仅有 `- (本节保留位置;具体约束见上文"必须做事项清单")` 一行占位文字
4. 对所有 7 个技能 SKILL.md + 6 个 references 子命令 SKILL.md 重复步骤 1-3

### 期望行为 vs 实际行为
- **期望**:无意义/无内容的板块已彻底清理(REAE-OPT-00002 验收项 AC)
- **实际**:7 个文件仍保留"## 不要做的事"空板块,仅含 1 行占位文字,无任何实际约束内容

## 2. 触发条件

- **必要条件**:阅读任一残留"## 不要做的事"空板块的 SKILL.md
- **环境因素**:本仓库 `plugins/code-skills/skills/code/` 下 7 个文件
- **发生频率**:必现(7/7 文件均有此残余)

## 3. 可能成因

- **假设 1**:REQ-OPT-00002 的"不要做 → 必须做"整改过程中,只把原"不要做"清单条目迁入"必须做"清单,但保留了"## 不要做的事"空壳板块作为占位
- **假设 2**:设计者最初将"## 不要做的事"作为"反向必须不做"清单的语义占位,整改完成后未识别该语义已空
- **涉及文件**:
  - `plugins/code-skills/skills/code/SKILL.md:106-108`
  - `plugins/code-skills/skills/code/references/rule/SKILL.md:174-176`
  - `plugins/code-skills/skills/code/references/faq/SKILL.md:228-230`
  - `plugins/code-skills/skills/code/references/ver/SKILL.md:456-458`
  - `plugins/code-skills/skills/code/references/merge/SKILL.md:429-431`
  - `plugins/code-skills/skills/code/references/fix/SKILL.md:314-316`
  - `plugins/code-skills/skills/code/references/req/SKILL.md:343-345`

## 4. 影响范围

- **影响用户**:阅读本仓库 SKILL.md 的开发者(内部 + 外部)
- **影响模块**:7 个 SKILL.md(1 主 + 6 子命令 references)
- **严重程度**:P2
- **后果**:文档噪音,读者疑惑"为什么有空板块";与 REQ-OPT-00002 验收标准未完全对齐

## 5. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-07-24 10:05 | v1 | 初始创建 | 缺陷登记完成 | wangmiao |