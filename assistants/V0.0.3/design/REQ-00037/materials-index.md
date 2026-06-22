# 材料登记 — REQ-00037

更新时间:2026-06-22 09:18
版本:V0.0.3

## 项目级规范

| 规范文件 | 类别 | 关键约束摘要 | 本设计对应章节 |
| --- | --- | --- | --- |
| `./assistants/rules/encoding-conventions.md` §规则 1, §规则 2, §规则 3, §规则 4 | 编码格式 | `^BUG-\d{5}$` 5 位纯数字;`^TASK-(REQ|BUG)-\d{5}-\d{5}$` 5+5 位嵌套式;接收端放宽为 `[A-Za-z0-9.\-_]+` | §6 功能架构(BUG 状态机扩展不引入新编码格式) |
| `./assistants/rules/migration-mapping.md` §规则 1, §规则 4 | 编码迁移 | `EXISTING-NNN` 不追溯;旧编码 → 新编码追溯表 | §6(本设计不引入新编码) |
| `./assistants/rules/dashboard-conventions.md` §规则 1 | 看板字段约定 | 字段扩展需**三方同步**(模板 + CLAUDE.md + 本规范) | §6 / §2.5(本设计**不**触发——状态字面是"自由字符串",不新增枚举列;见 §2.5.2 详细论证) |
| `./assistants/rules/skill-conventions.md` §规则 1, §规则 2 | SKILL.md 编写 | frontmatter `name` + `description` 必含;不得包含开发痕迹 | §4 约束清单(字节级保留 frontmatter;本设计产生的新增段落不引入开发痕迹) |
| `./assistants/rules/module-conventions.md`(DEPRECATED)| 模块规划 | (已迁到 `directory-conventions.md`) | §6(本设计不新增模块,沿用 REQ-00036 判定) |
| `./assistants/rules/directory-conventions.md` §规则 1 | 目录与模块 | (待添加,占位) | §6(无冲突) |
| `./assistants/rules/doc-conventions.md` §规则 1, §规则 2 | 文档编写 | README 多语言对仗 + 主语言完整性 | §6(SKILL.md 不是 README,本规则不适用) |
| `./assistants/rules/naming-conventions.md` §规则 1 | 命名 | (待添加,占位) | §6(无冲突) |
| `./assistants/rules/coding-style.md` §规则 1 | 代码风格 | (待添加,占位) | §6(无冲突) |
| `./assistants/rules/framework-conventions.md` §规则 1 | 框架 | (待添加,占位) | §6(无冲突) |
| `./assistants/rules/dependency-conventions.md` §规则 1 | 依赖 | (待添加,占位) | §6(无新增依赖) |
| `./assistants/rules/commit-conventions.md` §规则 1 | 提交 | (待添加,占位) | §11 集成点(本设计多次 commit 落地,沿用既有 `chore(...)` 模式) |
| `./assistants/rules/marketplace-protocol.md` §规则 1 | marketplace | 协议字段约束 | §6(本设计不动 `.claude-plugin/`) |

## 上游需求

- 来源:`./assistants/V0.0.3/require/REQ-00037/RESULT.md` (v1,2026-06-22 09:02)
- 提取:**8 FR / 8 NFR / 10 AC / 4 Q(待用户决策)**
- 关键交叉点(每条 FR 对应的本设计章节):

| FR | 本设计对应章节 |
| --- | --- |
| FR-1(`code-fix` 初始状态 `待处理`) | §6 功能域 1 + §9 数据结构 + §10 集成点 |
| FR-2(`code-plan` 完成 → `待开发`) | §6 功能域 2 + §10 集成点 |
| FR-3(`code-it` 第 1 任务 → `开发中`) | §6 功能域 3 + §8 接口概要 |
| FR-4(`code-it` 全部完成 → `待审查`) | §6 功能域 3 + §8 接口概要 |
| FR-5(`code-check` 完成 → `已完成`) | §6 功能域 4 + §10 集成点 |
| FR-6(`code-fix` 不再推进"待开发"及之后) | §6 功能域 1 + §11 备选 |
| FR-7(状态字面共存不归一化) | §9 数据结构 + §2.5 规范遵循 |
| FR-8(典型完整流程 SKILL.md 同步) | §6 各功能域 + §10 集成点 |

## 项目现状(本次扫描)

### 项目类型

- 语言 / 框架:Markdown 技能库(无业务代码);技能执行由 Claude Code 协议驱动
- 关键依赖:无运行时依赖;仓库元信息 `.claude-plugin/marketplace.json` + `plugin.json`

### 目录结构

- 顶层:`.claude-plugin/marketplace.json` + `plugins/code-skills/` 子目录
- `plugins/code-skills/skills/<14 技能名>/SKILL.md`:技能入口
- `plugins/code-skills/skills/<技能名>/{templates/, checklists/, guidelines/}`:技能资源(沿用 `module-conventions.md §规则 1`)

### 已有模块(本需求涉及 4 个)

| 模块 / 路径 | 职责 | 复用 / 修改 / 新增 |
| --- | --- | --- |
| `plugins/code-skills/skills/code-fix/SKILL.md` | 缺陷登记与跟踪(纯登记型,沿用 REQ-00027) | **修改既有**(FR-1 / FR-6 / FR-7 / FR-8) |
| `plugins/code-skills/skills/code-plan/SKILL.md` §"缺陷分支" | 详细设计 + 任务计划(REQ 路径 + BUG 路径) | **修改既有**(FR-2 步骤 27A / 28A 末尾追加状态回写) |
| `plugins/code-skills/skills/code-it/SKILL.md` §"缺陷分支"(17-25) | 开发编码(任务路径 + 缺陷路径) | **修改既有**(FR-3 步骤 21 / FR-4 步骤 24 末尾追加状态回写) |
| `plugins/code-skills/skills/code-check/SKILL.md` | 代码评审(REQ 路径为主,BUG 路径需扩展) | **修改既有**(FR-5 扩展接受 BUG-NNN 入参 + 评审后状态回写) |
| `plugins/code-skills/skills/code-dashboard/SKILL.md` | 开发看板(只读,无副作用) | **修改既有**(FR-7 扩展"待修复 / 已修复"分类规则) |

### 已有接口 / 数据结构 / 三方依赖

- BUG 编号:`^BUG-\d{5}$` 5 位纯数字(沿用 `encoding-conventions §规则 1/2`)
- BUG 任务:`TASK-BUG-\d{5}-\d{5}` 5+5 位嵌套式(沿用既有)
- 状态字段:`fix/<BUG-NNN>/RESULT.md` 文档头"状态"字段(自由字符串,15 个字面)
- 三方依赖:无新增

### 编码与构建约定

- `commit-conventions.md §规则 1`(待添加) → 沿用既有 `chore(code-<技能>): <需求编码> <摘要>` 模式(REPO 历史 commit message 风格)
- 末尾兜底提交:沿用 `code-design` 步骤 N(commit 后屏显 hash)

## CLI 参数

(本轮无 `--result` 参数,无模板填充)
