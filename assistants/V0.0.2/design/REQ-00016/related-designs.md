# 关联设计 — REQ-00016
更新时间:2026-06-05 16:10
版本:V0.0.2
需求编码:REQ-00016
设计标题:`code-design` / `code-plan` 增加"快模式"+ 末尾提交无需确认

---

## 1. 扫描范围

- 同版本 `./assistants/V0.0.2/design/`:REQ-00004 / REQ-00005 / REQ-00006 / REQ-00007 / REQ-00008 / REQ-00014(共 6 个既有 design 文档)
- 跨版本 `./assistants/V0.0.1/design/`:REQ-00001 / REQ-00002 / REQ-00003(共 3 个历史 design 文档)

## 2. 关联设计清单(模块交集 / 接口约定)

| 关联 design | 版本 | 关联点 | 对本设计的影响 |
| --- | --- | --- | --- |
| **REQ-00005 design**(首步拉取+末步提交) | V0.0.2 | 3 技能"首步拉取(步骤 0a)"+ "末步兜底提交(步骤 N)"模式 | 本需求**完全沿用** REQ-00005 步骤 0a / 步骤 N 模式;本需求是 REQ-00005 的**自然延伸**(让 3 选 1 确认在特定条件下跳过) |
| **REQ-00007 design**(`code-auto` 编排) | V0.0.2 | `code-auto` 内部强制"所有 AskUserQuestion 自动选推荐项"(FR-6 + Q-4 锁定 A) | 本需求**不**触发 `code-auto` 升级;`code-auto` 用户显式设置 `CODE_FAST_MODE=1` 即可走快模式 |
| **REQ-00008 design**(`code-review` 整版本模式) | V0.0.2 | REQ-00008 增加了 `code-review` 的"无参模式" | 本需求延续"模式扩展"思路;本设计**不**改 `code-review`,仅改 `code-design` / `code-plan` |
| **REQ-00014 design**(`code-plan` 任务拆分维度) | V0.0.2 | `code-plan` 拆任务"按功能点拆" | 本需求**不**修改 REQ-00014 规则;快模式下 `code-plan` 仍按"按功能点拆",只是**减少**过程文档 |
| **REQ-00004 design**(`code-dashboard` 只读看板) | V0.0.2 | `code-dashboard` 解析看板 3 区段 | 快模式新增的"`已完成(首次-快模式)`"状态枚举值**不**触发 `code-dashboard` 解析失败(`code-dashboard` 状态字面严格按字面匹配,**不**归一化) |
| **REQ-00006 design**(`code-publish` 发布部署) | V0.0.2 | `code-publish` 前置检查 | 本需求**不**触发 `code-publish` 升级 |
| **REQ-00001 design**(V0.0.1) | V0.0.1 | `code-design` 既有行为(双格式正则等) | 快模式**完全复用**既有解析逻辑(双格式正则不变) |
| **REQ-00002 design**(V0.0.1) | V0.0.1 | `encoding-conventions.md` 编码规范 | 本需求**不**产生新编码(派生任务字段由 `code-plan` 既有规则决定) |
| **REQ-00003 design**(V0.0.1) | V0.0.1 | `code-rule` 维护项目级规范 | 本需求**不**写新规范(Q-P4 留作 follow-up) |

## 3. 关键结论

1. **0 反向影响**:本设计**不**影响上述 9 个 design 的章节与决策
2. **0 新增子目录**:本设计只改 2 个 SKILL.md,**不**新增 `templates/` / `checklists/` / `guidelines/` 子目录
3. **完整模式 100% 字节级保留**:本设计在 `code-design` / `code-plan` SKILL.md 中**只**追加,不改既有字面
4. **`code-auto` 正交**:本需求**不**触发 `code-auto` 升级,`code-auto` 行为**不变**;用户显式设置 `CODE_FAST_MODE=1` 才生效

## 4. 待澄清项(本设计阶段)

**无新增待澄清**。所有设计决策均由既有需求(REQ-00016 6 FR + 10 NFR) + 既有规范 + 既有 9 个 design 提供充分依据。
