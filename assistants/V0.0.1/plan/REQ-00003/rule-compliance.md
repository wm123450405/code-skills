# 规范遵循记录 — REQ-00003(plan 阶段)

更新时间:2026-06-04 09:15
版本:V0.0.1

> 继承 design 阶段 `design/REQ-00003/rule-compliance.md` 的全部结论,本 plan 阶段**无新增/修改**。

## 1. 本 plan 阶段参考的规范文件(6 个)

| 规范文件 | 类别 | 关键约束摘要 | 本 plan 阶段如何遵循 |
| --- | --- | --- | --- |
| `dashboard-conventions.md` | 看板 | 看板字段约定扩展需多文件同步 | 本 plan 阶段不扩展字段,仅追加区段(INV-6 0 变更) |
| `doc-conventions.md` §规则 1 | 文档 | README 多语言对仗 | 本 plan 不修改 README ✅ |
| `doc-conventions.md` §规则 2 | 文档 | 仓库级 README 必须存在并持续维护 | 本 plan 不修改 README ✅ |
| `marketplace-protocol.md` | marketplace | `marketplace.json` / `plugin.json` 字段约束 | INV-5 0 变更(FR-9 硬边界) |
| `module-conventions.md` | 模块 | 技能资源摆放在固定子目录 | INV-7 仅追加 DEPRECATED 标记;新规则放 `directory-conventions.md` |
| `skill-conventions.md` §规则 1 | 技能 | SKILL.md frontmatter 必含 `name`+`description` | INV-5 0 变更(本 plan 改 SKILL.md 正文,不改 frontmatter) |

## 2. plan 阶段对 design 阶段 rule-compliance 的继承

design 阶段的 §1-§7(本 plan 阶段逐条继承):
- §1 规范文件清单:6 个规范文件保持
- §2 规范 vs 现状偏离:3 条保持
- §3 规范 vs 需求冲突:无
- §4 用户授权的偏离:无
- §5 规范变更响应:无
- §6 本次设计新增的"硬性边界":B-1 ~ B-6 全部保持
- §7 自检表:14 条全部 ✅

## 3. plan 阶段新增的自检

| # | 自检项 | 自检结果 |
| --- | --- | --- |
| P-S-1 | `code-rule` SKILL.md frontmatter 一致性(本 plan 仅改正文) | ✅ |
| P-S-2 | 6 个新分类文件仅含骨架(无预填规则) | ✅(INV-2,Q-5=H1) |
| P-S-3 | 任务 REQ-00003-001~007 测试状态统一为"不适用" | ✅(INV-10,纯文档/规范) |
| P-S-4 | Type 识别合并到步骤 4 子段(plan 阶段微调) | ✅(Q-PLAN-2 答复) |
| P-S-5 | 7 任务 / 6 commit 粒度 | ✅(Q-PLAN-1 答复,D-PLAN-2) |

## 4. 冲突解决记录

### 冲突 C-PLAN-1:类型识别引擎在 SKILL.md 中的位置
- **冲突描述**:design M-1 定义"类型识别引擎"作为**独立子流程**插入步骤 4 之前;plan 阶段用户答复(2026-06-04 09:15)要求"合并到步骤 4 拆分归类之内"
- **解决方案**:**采纳 plan 阶段用户答复**;在 `design-notes.md` §Q-2 显式标注"plan 阶段微调 design M-1"
- **对 design 的影响**:M-1 在 plan 阶段被吸收到步骤 4;模块命名保留 M-1(便于追踪)但归类为"步骤 4 子模块"
- **依据规范**:本变更**不违反**任何强制规范(`skill-conventions.md` §规则 1 仅约束 frontmatter,本变更改正文)

### 冲突 C-PLAN-2:commit 粒度与任务粒度的关系
- **冲突描述**:design D-7 定义"5 commit 粒度";plan 阶段需明确 commit 与任务的对应关系
- **解决方案**:**7 任务 / 6 commit**(D-PLAN-2),其中 commit 1 含 T-001(扩展正文)+ T-006(更新工作目录约定)
- **依据规范**:本变更不违反任何规范(plan 阶段决策)

## 5. 总结

- 本 plan 阶段**无新增规范 vs 需求冲突**
- 本 plan 阶段**有 2 项对 design 的微调**(均不违反强制规范,均在 plan 阶段文档化)
- 实施后 `assistants/rules/` 共 11 个文件(4 保留 + 1 弃用 + 6 新建)
- 实施后 CLAUDE.md 末尾新增"## AI 工作约定"小节
- 实施后 `code-rule/SKILL.md` 正文扩展(frontmatter 不变)
- 严守 FR-9 边界(marketplace.json / plugin.json / 9 个其他 SKILL.md / 4 保留规范 / V0.0.0~V0.0.1 工作文件)
