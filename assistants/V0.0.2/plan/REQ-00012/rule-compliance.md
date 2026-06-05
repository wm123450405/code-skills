# 规范遵循记录 — REQ-00012
更新时间:2026-06-05
版本:V0.0.2

## 1. 本次参考的规范文件

- `./assistants/rules/doc-conventions.md`(核心):§规则 1 + §规则 2
- `./assistants/rules/commit-conventions.md`(NFR-7)
- `./assistants/rules/skill-conventions.md`(NFR-4 字节级保留)
- `./assistants/rules/directory-conventions.md`(无直接约束)
- 其他 9 个规范:本需求不涉及

## 2. 规范 vs 现状偏离

- **`doc-conventions §规则 2` 适用范围**:仅 `plugins/code-skills/README.md`,**不**包括新创建的根 README
  - 项目现状:根 README 不在 §规则 2 强制范围内
  - 本设计处理:实际编写时**主动**覆盖"简介 / 快速开始 / 主要能力 / 详细文档链 / 许可证"等核心小节,以满足 GitHub 门面级惯例(与 FR-1 AC-1.3 一致)
  - 评级:**非违规,主动善意**(本条由 `code-design` 阶段已记录,本阶段继承)

## 3. 规范 vs 设计/需求冲突

- 无冲突(本需求 100% 沿用上游)

## 4. 用户授权的偏离

- 无(所有决策均由 FR/NFR 锁定,无歧义需用户授权)

## 5. 规范变更响应(增量更新时)

- 本次为首次设计,无规范侧变更
