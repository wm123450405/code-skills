# 规范遵循记录 — REQ-00018
更新时间:2026-06-06 13:15
版本:V0.0.2
需求编码:REQ-00018

## 1. 本次参考的规范文件

13 份全部参考(沿用概要设计严守范围):
- skill-conventions.md
- module-conventions.md / directory-conventions.md
- dependency-conventions.md
- dashboard-conventions.md
- encoding-conventions.md
- commit-conventions.md
- doc-conventions.md
- marketplace-protocol.md
- naming-conventions.md
- coding-style.md
- framework-conventions.md
- migration-mapping.md

## 2. 规范 vs 现状偏离

无。

## 3. 规范 vs 需求冲突

无。

## 4. 用户授权的偏离

无。

## 5. 规范变更响应

不适用(本设计是首次创建)。

## 6. 规范自检总览(13/13 严守)

| 规范文件 | 自检 | 严守点 |
| --- | --- | --- |
| skill-conventions §规则 1 | ✅ | frontmatter L1-3 字节级保留(锚点 = "## 工作流程" 段后) |
| module-conventions §规则 1 | ✅ | 不新增资源文件(只插入小节) |
| directory-conventions | ✅ | 不新增子目录 |
| dependency-conventions | ✅ | 0 新增依赖(NFR-1 严守) |
| dashboard-conventions §规则 1 | ✅ | 0 触发 3 处同步(NFR-6 + 任务推进由 /code-it 兜底) |
| encoding-conventions | ✅ | 任务编号 `TASK-REQ-00018-00001~00002` 严格 5+5 位 |
| commit-conventions | ✅ | 由 code-it / code-auto 末步兜底 |
| doc-conventions | ✅ | SKILL.md 行数变化在 ±20% 范围(预估 +50~80 行) |
| marketplace-protocol | ✅ | 不修改 marketplace.json / plugin.json(NFR-4 严守) |
| naming-conventions | ✅ | 函数名 kebab-case |
| coding-style | ✅ | 沿用 SKILL.md 既有风格 |
| framework-conventions | ✅ | 不涉及 |
| migration-mapping | ✅ | 不涉及 |

**总览**:**13 份规范全部严守,0 冲突 / 0 偏离 / 0 授权**。
