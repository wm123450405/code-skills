# 澄清记录 — REQ-00003(plan 阶段)

更新时间:2026-06-04 09:15
版本:V0.0.1

> 本 plan 阶段新增 2 项澄清(2026-06-04);上游 REQU + design 阶段澄清见 `require/REQ-00003/clarifications.md` + `design/REQ-00003/clarifications.md`。

## plan 阶段新增 2 项(用户 2026-06-04 答复)

### Q-PLAN-1:本 plan 阶段拆任务的粒度策略
- **问题**:design 阶段 commit 粒度是 5 commit;但 plan 任务粒度可以与 commit 解耦
- **用户回答**:**按 5 commit 拆 7-9 任务(推荐)**
- **影响章节**:`design-notes.md` §Q-7 + `PLAN.md` 任务总览
- **本 plan 阶段具体拆分**:**7 任务 / 6 commit**
  - T-001(扩展 SKILL.md:类型识别 + Type A/B/C 文档化) + T-006(更新 SKILL.md 工作目录约定)合入 commit 1
  - T-002(创建 6 个新分类占位) → commit 2
  - T-003(追加 module-conventions.md DEPRECATED) → commit 3
  - T-004(扩展 templates/rule.md) → commit 4
  - T-005(追加 CLAUDE.md "AI 工作约定"小节) → commit 5
  - T-007(全仓库 Grep + 不变量自检 + commit 整理) → commit 6
- **处理时间**:2026-06-04 09:15(plan 阶段)

### Q-PLAN-2:类型识别引擎在 SKILL.md 中的位置
- **问题**:design 阶段方案是"独立子流程,步骤 4 之前插入";plan 阶段需明确是合并到步骤 4 还是独立
- **用户回答**:**合并到步骤 4 拆分归类之内**
- **影响章节**:`design-notes.md` §Q-2 + `RESULT.md` §3.6 类型识别引擎
- **微调后步骤 4 结构**(详见 `design-notes.md` §Q-2):
  - 4.1 拆分(`<原始描述>` → `Rule[1..N]`)
  - 4.2 类型识别(关键词 + 置信度 + 显式确认,标记 `type ∈ {A, B, C}`)
  - 4.3 初步归类(Type A 才走;B/C 路由到子流程)
- **对 design M-1 模块的影响**:M-1 内容(关键词表 + 置信度 + AskUserQuestion)并入步骤 4;模块命名保留 M-1 便于追踪,但归类为"步骤 4 子模块",非"独立子流程"
- **处理时间**:2026-06-04 09:15(plan 阶段)

## 待用户后续确认(无)

本 plan 阶段**无遗留待用户确认项**。
