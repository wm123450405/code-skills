# 规范遵循记录 — REQ-00012
更新时间:2026-06-05
版本:V0.0.2

## 1. 本次参考的规范文件
- ./assistants/rules/doc-conventions.md(核心)
- ./assistants/rules/commit-conventions.md(NFR-7)
- ./assistants/rules/directory-conventions.md(无直接约束)

## 2. 规范 vs 现状偏离
- **`doc-conventions §规则 2`**:适用范围是 `plugins/code-skills/README.md`,**不**包括新创建的根 README
  - 项目现状:根 README 不在 §规则 2 强制范围内
  - 影响:根 README 仅受 §规则 1 约束(中英对仗),**不**强受 §规则 2 核心小节要求
  - 本设计处理:实际编写时**主动**覆盖"简介 / 快速开始 / 主要能力 / 详细文档链 / 许可证"等核心小节,以满足 GitHub 门面级惯例(与 FR-1 AC-1.3 一致)
  - 评级:**非违规,主动善意**

## 3. 规范 vs 需求冲突
- 无冲突(FR-6 显式声明遵循 §规则 1 / §规则 2,与本设计一致)

## 4. 用户授权的偏离
- 无(所有决策均由 FR/NFR 锁定,无歧义需用户授权)

## 5. 规范变更响应(增量更新时填写)
- 本次为首次设计,无规范侧变更
