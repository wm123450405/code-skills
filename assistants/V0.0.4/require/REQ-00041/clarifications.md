# 澄清记录 — REQ-00041

## 2026-06-29 13:50

- **问题**:references 按语言拆分时,需要覆盖哪些开发语言/模块类型?
- **选项**:A. 全部 6 类(推荐) B. 仅最常用 3 类 C. 先做框架+1 个示例
- **用户回答**:A. 全部 6 类(Node.js/TypeScript、Python、Rust、Go、Java(Maven)、Java(Gradle))
- **影响**:RESULT.md §4 FR-4(覆盖 6 类语言文档)

- **问题**:references 目录的放置方式?
- **选项**:A. 每个技能独立 references/ B. 共享 references/ 目录 C. 独立维护,不复用
- **用户回答**:A. 每个技能独立 references/
- **影响**:RESULT.md §4 FR-3(references/ 目录结构)

- **问题**:SKILL.md 简化到什么程度?
- **选项**:A. 激进简化(推荐) B. 适度简化 C. 保守简化
- **用户回答**:A. 激进简化(仅保留步骤编号+标题)
- **影响**:RESULT.md §4 FR-2(流程骨架化程度)、FR-6(简化目标)