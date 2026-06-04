# 澄清记录 — REQ-00006(设计阶段)

更新时间:2026-06-04 16:48
版本:V0.0.2

## 本阶段澄清状态

需求 v1 已锁定 4 项关键 Q(Q-1 ~ Q-4)+ 5 项默认 Q(Q-5 ~ Q-9)+ 1 项建议派生 Q(Q-10)。设计阶段**未发现**新的需要用户澄清的项,因为:

1. **架构走向无歧义**:决策 D-1 ~ D-8 全部可从"需求 v1 + 项目规范 + 项目现状"演绎得出
2. **规范无冲突**:`rule-compliance.md §3` 0 冲突
3. **关联设计无歧义**:`related-designs.md` 0 重复模块

## 本次设计决策映射

| 设计决策 | 来源 | 是否需要用户澄清 |
| --- | --- | --- |
| D-1 技能位置(独立第 9/11 个 code-* 技能) | 需求 §G-1 锁定 | 否 |
| D-2 看板解析方式(按行硬解析) | NFR-1 + NFR-8 + V0.0.1 现状 | 否 |
| D-3 基线识别规则 | NFR-7 显式锁定规则 1 | 否 |
| D-4 输入参数(可选 + 缺省 `.current-version`) | 需求 §S-3 含可选参数 | 否 |
| D-5 `--force` 强制发布 | **v1 不实现**(未在 FR/AC 显式) | 否(留作 v2,可派生) |
| D-6 Q&A 聚合规则(全部聚合) | FR-5 锁定 | 否 |
| D-7 文件覆盖策略(覆盖 + 报告) | NFR-6 显式覆盖 + 用户审阅模式 | 否 |
| D-8 报告格式(纯文本 + 少量图标) | 需求 §S-1 ~ §S-5 样例 + NFR-9 | 否 |

## 设计阶段已知的"未决项",但**不阻塞本设计**

下列项是"良好的 follow-up 候选",由 `code-review` 阶段决定是否派生改修任务:

### Q-D-1:`code-publish` 是否进入 `marketplace.json` 的 `plugins[].skills[]` 列表?
- **当前状态**:FR-8.AC-8.1 禁止修改 marketplace.json,即**不**进入
- **影响**:新技能 `code-publish` 在 marketplace 安装时**不会被注册**,用户调 `/code-publish` 可能找不到
- **决策**:本设计**显式接受**该约束;由独立的 v2 任务(`code-rule` 或新 REQ)处理 marketplace.json 同步
- **建议派生**:`code-review` 阶段派生"将 code-publish 注册到 marketplace.json + plugin.json"

### Q-D-2:`code-publish` 在 V0.0.2 看板的"技能映射表"位置?
- **当前状态**:V0.0.2 / V0.0.1 看板均无"技能映射表"区段(只有 13 个常规区段)
- **影响**:无;本设计不依赖看板增加新区段
- **决策**:不处理

### Q-D-3:`code-publish` 与 `code-init` / `code-version` / `code-rule` / `code-fix` 一样需要在 `plugins/code-skills/README.md` "主要能力"段追加吗?
- **当前状态**:需求 §2.3 末尾"若需要..."暗示**可选**
- **影响**:小;用户找到 `code-publish` 的方式可以靠 marketplace 注册(Q-D-1)或者 README
- **决策**:**纳入本设计**(由 `code-plan` 决定拆为独立任务);若拆任务,**必须**遵循 `doc-conventions.md §规则 1`(中英同次提交)
- **建议派生**:无需派生(本设计已纳入)

## 与需求 v1 待澄清项 Q-10 的关系

需求 v1 §12 标注的 Q-10 "派生任务预警":
- 建议派生 1:"code-dashboard 升级'全完成'建议为 code-publish"(由 REQ-00004 设计阶段或 code-review 决定)
- 建议派生 2:"用 code-rule 沉淀 publish-conventions.md"(由 code-review 决定)
- 建议派生 3:"把 code-publish 加入 REQ-00005 的'首步拉取+末步提交'3 技能之一"(由 code-review 决定)

**本设计的回应**:全部接受,在 RESULT.md §11 与 §15 显式列出,等待 `code-review` 阶段决策。

## 设计阶段未与用户做 `AskUserQuestion` 的理由

按本技能 SKILL.md "步骤 8A — 澄清冲突与不确定项"的工作流约定:**每轮聚焦 1-3 个最阻塞点**;本设计经全面自检,**0 阻塞点**,因此**不发起** `AskUserQuestion`,直接进入 §9A 模块拆分。

若用户在 review 本 RESULT.md 时发现需要澄清的设计走向,可:
- 调 `/code-design REQ-00006`(增量更新模式)+ 在对话中提出
- 或在 REQ-00006 评审阶段(`/code-review REQ-00006`)提出
