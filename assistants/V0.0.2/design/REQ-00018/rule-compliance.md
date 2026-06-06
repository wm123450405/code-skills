# 规范遵循记录 — REQ-00018
更新时间:2026-06-06 13:00
版本:V0.0.2
需求编码:REQ-00018

## 1. 本次参考的规范文件

- `./assistants/rules/skill-conventions.md` — SKILL.md frontmatter 字节级保留
- `./assistants/rules/module-conventions.md` — 技能资源放固定子目录(已弃用,内容迁移到 directory-conventions)
- `./assistants/rules/directory-conventions.md` — 目录结构(承接 module-conventions 既有规则)
- `./assistants/rules/dependency-conventions.md` — 依赖管理
- `./assistants/rules/dashboard-conventions.md` — 看板字段扩展需三方同步
- `./assistants/rules/encoding-conventions.md` — REQ / BUG / TASK 编码权威源
- `./assistants/rules/commit-conventions.md` — commit 消息格式
- `./assistants/rules/doc-conventions.md` — 文档编写
- `./assistants/rules/marketplace-protocol.md` — marketplace 既有字段不变
- `./assistants/rules/naming-conventions.md` — 命名约定
- `./assistants/rules/coding-style.md` — 编码风格
- `./assistants/rules/framework-conventions.md` — 框架使用
- `./assistants/rules/migration-mapping.md` — 跨版本映射

**全部 13 份规范均参考**,无遗漏。

## 2. 规范 vs 现状偏离

无。

**说明**:本需求**不**修改项目结构(只改既有 SKILL.md 1 个文件),不修改规范,不修改 marketplace,不修改 `code-skills` 自身产物,因此无"现状偏离"。

## 3. 规范 vs 需求冲突

无。

**说明**:本需求与 13 份规范均无冲突 — 严守 NFR-1 零依赖 / NFR-2 增量改 / NFR-3 不改其他 12 个技能 / NFR-4 不改 code-skills 自身 / NFR-5 不改规范 / NFR-6 不改看板模板 / NFR-9 不参与 REQ-00005 扩展。

## 4. 用户授权的偏离

无。

**说明**:本需求**不**需要任何"用户授权的偏离" — 所有 5 项核心决策(D-1 增量追加 / D-2 扫描优先级 / D-3 解析模式 / D-4 失败不阻断 / D-5 不引入 CLI 参数)均严格遵循 Q-1 / Q-2 / Q-3~Q-7 已锁定 / 采纳默认,无新增偏离。

## 5. 规范变更响应(增量更新时填写)

不适用(本设计是首次创建,非增量更新)。

## 6. 规范自检总览

| 规范文件 | 自检结论 | 备注 |
| --- | --- | --- |
| skill-conventions.md §规则 1 | ✅ 严守 | frontmatter 字节级保留 — D-1 锁定 |
| module-conventions.md §规则 1 | ✅ 严守 | 本需求**不**新增资源文件 |
| directory-conventions.md | ✅ 严守 | 本需求**不**新增目录 |
| dependency-conventions.md | ✅ 严守 | 0 新增依赖 — NFR-1 严守 |
| dashboard-conventions.md §规则 1 | ✅ 严守 | 本需求**不**扩展看板字段 |
| encoding-conventions.md | ✅ 严守 | 本需求**不**涉及任务编号(由 `code-plan` 决定) |
| commit-conventions.md | ✅ 严守 | 由 `code-it` / `code-auto` 末步兜底,本设计**不**直接涉及 |
| doc-conventions.md | ✅ 严守 | 本设计**不**直接涉及源码 |
| marketplace-protocol.md | ✅ 严守 | 本需求**不**修改 marketplace.json / plugin.json — NFR-4 严守 |
| naming-conventions.md | ✅ 严守 | 本设计**不**直接涉及源码 |
| coding-style.md | ✅ 严守 | 本设计**不**直接涉及源码 |
| framework-conventions.md | ✅ 严守 | 本设计**不**直接涉及源码 |
| migration-mapping.md | ✅ 严守 | 本需求**不**涉及跨版本迁移 |

**总览**:**13 份规范全部严守,0 冲突 / 0 偏离 / 0 待澄清**。
