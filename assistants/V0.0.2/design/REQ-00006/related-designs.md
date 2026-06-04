# 关联概要设计 — REQ-00006

更新时间:2026-06-04 16:48
版本:V0.0.2

## 1. 同版本(V0.0.2)概要设计扫描

执行 `Glob "./assistants/V0.0.2/design/*/RESULT.md"`:
- **0 个已存在**(`design/` 目录在本设计前不存在,本设计是 V0.0.2 中**首次**概要设计)

## 2. 跨版本概要设计扫描

执行 `Glob "./assistants/V0.0.1/design/*/RESULT.md"`:
- REQ-00001:Marketplace 改名落地(主题:marketplace.json + README + skill 重命名)
- REQ-00002:编码格式统一(主题:REQ/TASK/BUG 5 位格式)
- REQ-00003:优化 code-rule 技能(主题:规范类型识别 + 6 个新分类占位文件)

**主题相关性**:0 个相关。3 个 V0.0.1 设计均不涉及"发布部署 / 看板状态检查 / 通用手册生成"。

## 3. 关联点(理论层面 — 虽无设计文档对应,但有需求层面的关联)

虽然 REQ-00004 / REQ-00005 / REQ-00007 ~ REQ-00013 同在 V0.0.2 已完成需求分析,但**均无对应概要设计**(`./assistants/V0.0.2/design/` 在本设计前为空)。本表记录"需求层面"的关联,供 v2 设计阶段或本设计 follow-up 参考:

| 关联需求 | 关联点 | 影响本设计 | 影响方向 |
| --- | --- | --- | --- |
| **REQ-00004**(`code-dashboard`) | 同消费看板 3 区段 | NFR-8:解决判定必须 ≥ dashboard 的"真正可发布" | 单向:本设计**只读**消费,与 dashboard 0 冲突 |
| **REQ-00005**(3 技能加首步拉取 + 末步提交) | `code-publish` 不在改写范围 | NFR-4:本设计**不**含首步拉取 / 末步提交;由用户保证调用上下文 | 单向:不影响 REQ-00005 |
| **REQ-00001**(基线版本约定) | NFR-7 基线识别规则 1 = 字典序最小 | 决策 D-3 选定规则 1 | 单向:本设计参考 V0.0.1 已有的版本号格式(V0.0.X) |
| **REQ-00003**(`code-rule`) | 项目级规范由 `code-rule` 维护 | 本设计**不**新建 `publish-conventions.md`;留作 follow-up | 双向:本设计为未来 `publish-conventions.md` 留接口 |
| **REQ-00002**(编码格式统一) | 看板表格中编码列遵循统一格式 | 本设计**只读**编码作为字符串 key,不验证格式 | 单向:不影响 REQ-00002 |
| **REQ-00007**(`code-auto`) | code-auto 链路含 code-publish? | 用户需求 §13 暗示**不含**(code-auto 仅驱动开发 6 技能);本设计与之 0 冲突 | 单向:不影响 REQ-00007 |
| **REQ-00008**(整版本评审) | REVIEW.md 在 `./assistants/<版本号>/` 顶层 | 本设计在 `./assistants/<版本号>/publish/` 子目录,与 REVIEW.md 0 冲突 | 单向 |
| **REQ-00009**(`code-unit` 可测性守卫) | "不适用" 测试状态进入"任务解决"集合 | 本设计 §FR-1 已含 {`已运行-通过`, `不适用`},与之自然对齐 | 双向:**已对齐** |
| **REQ-00010**(`code-it` 前置任务守卫) | 任务的"开发状态"判定 | 本设计 §FR-1 中"任务解决 = 开发=已完成 ∧ ..."与 REQ-00010 同口径 | 双向:**已对齐** |
| **REQ-00011**(`code-design` / `code-plan` 设计目标确认) | 本技能不引入"设计目标"环节(NFR-5 通用骨架) | 本设计是"非编辑型"技能,无需求需要"设计目标" | 单向:0 影响 |
| **REQ-00012**(仓库根 README + CLAUDE.md 移位) | `assistants/qanda/README.md` 是项目级文件,**不**受 REQ-00012 移位影响 | 本设计在 `./assistants/qanda/README.md`,REQ-00012 的"仓库根"指 `./README.md` | 单向:0 冲突 |
| **REQ-00013**(编号+标题显示升级) | `code-publish` 的报告中是否需要显示"REQ-NNNNN · 标题"格式? | 需求 v1 未要求 REQ-00006 自身做此升级(REQ-00013 §Q-4 锁定"本轮升级 6 技能",**不含 `code-publish`**);本设计沿用"REQ-NNNNN" 朴素格式 | 单向:0 冲突,但留作 v2 follow-up |

## 4. 关联设计文档(若 v2 实施)

| 关联需求 | 预期设计文档 | 关键关联点 |
| --- | --- | --- |
| REQ-00004 | `V0.0.2/design/REQ-00004/RESULT.md` | dashboard 与 publish 共用解析规则 |
| REQ-00005 | `V0.0.2/design/REQ-00005/RESULT.md` | 不参与本需求改写 |
| REQ-00007 | `V0.0.2/design/REQ-00007/RESULT.md` | code-auto 不驱动 code-publish |

## 5. 横向去重检查

- **0 重复模块**:本设计的所有模块(PreflightChecker / BaselineDetector / ManualBuilder / QandaScaffolder / QandaAggregator / ReportFormatter)在 V0.0.1 中**不存在**
- **解析锚点不去重**:与 REQ-00004 的 dashboard 共用相同锚点,但**这是 NFR-8 的强一致性约束,不是重复**;本设计与 REQ-00004 是"对称"关系(写时一致 / 读时一致)
