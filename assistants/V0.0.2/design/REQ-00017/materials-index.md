# 材料登记 — REQ-00017
更新时间:2026-06-05 16:30
版本:V0.0.2

## 项目级规范

| 规范文件 | 类别 | 关键约束摘要 |
| --- | --- | --- |
| architecture.md | (本项目无此文件) | — |
| api-standards.md | (本项目无此文件) | — |
| data-modeling.md | (本项目无此文件) | — |
| **dashboard-conventions.md** | 看板与版本工作空间 | §规则 1 看板字段扩展需 3 处同步(模板/CLAUDE.md/规范);本需求 0 新增枚举值,**不**触发同步 |
| **module-conventions.md** | 模块规划(已弃用,迁移到 directory-conventions) | §规则 1 资源放技能子目录;本需求不涉及 |
| **skill-conventions.md** | 技能规范 | §规则 1 SKILL.md frontmatter 必含 name+description;本需求 2 个 SKILL.md 字节级保留 |
| **encoding-conventions.md** | 任务编码 | §规则 1+3 任务编码双格式 `TASK-(REQ|BUG)-\d{5}-\d{5}` 新 + `(REQ|BUG)-\d{5}-\d{5}` 旧;P-1 兼容 |
| **commit-conventions.md** | 提交规范 | `chore(code-*)` 风格;末尾兜底沿用 |
| **doc-conventions.md** | 文档规范 | 2 个 SKILL.md 增量追加遵循 |
| **naming-conventions.md** | 命名规范 | P-1 锚点名称"P-1 推进看板" |
| **coding-style.md** | 编码风格 | 2 个 SKILL.md 增量追加沿用既有风格 |
| **directory-conventions.md** | 目录规范 | 技能目录结构 |
| **framework-conventions.md** | 框架约定 | 不涉及 |
| **dependency-conventions.md** | 依赖管理 | 0 新增依赖 |
| **marketplace-protocol.md** | 插件协议 | 不涉及 |
| **migration-mapping.md** | 迁移映射 | 不涉及 |

## 上游需求

- 来源:./assistants/V0.0.2/require/REQ-00017/RESULT.md
- 版本:V0.0.2(2026-06-05 16:25)
- 提取:4 FR / 6 NFR / 8 AC / 5 边界

## 项目现状(本次扫描)

### 项目类型
- `code-skills` 工具集仓库(本仓库),含 9 个 `code-*` 技能(实际 V0.0.2 共 11 个,本需求"非目标"列出 7 个"0 修改")
- 主目录:`plugins/code-skills/skills/<技能名>/SKILL.md`

### 目录结构(本次涉及)
- `plugins/code-skills/skills/code-plan/SKILL.md` — 待修改(步骤 4A + 步骤 9A)
- `plugins/code-skills/skills/code-it/SKILL.md` — 待修改(末尾兜底后 P-1)

### 已有模块
| 模块/路径 | 职责 | 是否可复用 |
| --- | --- | --- |
| `/code-plan` 步骤 4A 拆任务 | 拆真实任务 | 需修改(加"实际产出候选集"约束) |
| `/code-plan` 步骤 9A 看板同步 | 把任务写入看板"任务清单" | 需修改(只写真实任务) |
| `/code-it` 末尾兜底 | commit 提交 | 复用 + 追加 P-1 |
| `/code-dashboard` 看板解析 | 3 区段解析 | 复用(P-1 沿用同锚点) |

### 已有看板"任务清单"列(8 列)
任务编码 / 任务标题 / 关联需求 / 触发/来源 / 开发状态 / 测试状态 / 完成时间 / 备注

### 已有看板"变更记录"事件类型(10+ 种)
需求新增 / 需求变更 / 概要设计完成 / 详细设计完成 / **任务完成** / 测试完成 / 审查完成 / 派生任务完成 / 缺陷修复 / 发布 / 开发状态更新

本需求使用"任务完成"(既有),**不新增**枚举值。
