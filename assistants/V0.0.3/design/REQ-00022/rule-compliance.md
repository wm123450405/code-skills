# 规范遵循记录 — REQ-00022
更新时间:2026-06-07
版本:V0.0.3

## 1. 本次参考的规范文件
13 个项目级规范文件全部读取,本需求实际触发的有 4 个,其余 9 个不触发或 N/A。

| 规范文件 | 类别 | 关键约束 | 本设计是否触发 | 触发后处理 |
| --- | --- | --- | --- | --- |
| skill-conventions.md | 技能规范 | §规则 1:frontmatter `name` 字节级保留 | ✅ 触发 | FR-1 必改(目录 + frontmatter + H1) |
| dashboard-conventions.md | 看板规范 | §规则 1:三同步 | ✅ 不触发 | INV-7 锁定 0 触发 |
| encoding-conventions.md | 编号规范 | §规则 1/3:5+5 位嵌套式 | ❌ 不触发 | 本需求 0 改编号 |
| marketplace-protocol.md | 市场协议 | 0 改 marketplace/plugin(实际必改) | ✅ 触发 | FR-2 全部同步改 |
| module-conventions.md(DEPRECATED) | 模块规范 | §规则 1:过程文档摆放 | ✅ 不触发 | 沿用既有 |
| commit-conventions.md | 提交规范 | chore(<scope>) 格式 | ✅ 触发 | 末步提交沿用 |
| doc-conventions.md | 文档规范 | 中英 README 同步 | ✅ 触发 | FR-4 25 文件同步改 |
| naming-conventions.md | 命名规范 | 0 新增文件名前缀 | ✅ 触发 | 基本名 `code-check` 用户原文锁定 |
| dependency-conventions.md | 依赖规范 | 0 新增依赖 | ✅ 不触发 | INV-8 锁定 0 触发 |
| directory-conventions.md | 目录规范 | 子目录命名 | ✅ 不触发 | 沿用既有 |
| framework-conventions.md | 框架规范 | 框架选型偏好 | ❌ N/A | 本需求是 SKILL.md 文档改造 |
| coding-style.md | 编码风格 | 命名/注释/提交风格 | ❌ N/A | 本需求 0 写代码 |
| migration-mapping.md | 迁移映射 | 旧 → 新格式映射 | ✅ 触发 | FR-5 沿用 §规则 5 |

## 2. 规范 vs 现状偏离(本需求 0)
- 本需求**0**触发任何"现状偏离"——硬重命名后,11 个 SKILL.md 既有"## 工作流程"小节、"## 工具使用约定"小节、"## 衔接"小节、"## 不要做的事"小节**全部字节级保留**

## 3. 规范 vs 需求冲突(本需求 0)
- 本需求**0**触发任何"规范 vs 需求冲突"
- 全部 FR / NFR / AC / INV 均**不**违反 13 份项目级规范

## 4. 用户授权的偏离(本需求 0)
- (无)本需求为"硬重命名",**不**偏离任何规范

## 5. 规范变更响应(本概设为首次设计,本节占位)
- 本概设为"首次设计"分支,非"增量更新"分支
- 规范变更响应节在后续增量更新时填写

## 6. 自检结论
- ✅ INV-1 ~ INV-9:全部字节级保留
- ✅ 0 用户授权偏离
- ✅ 0 待澄清冲突
