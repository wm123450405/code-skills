# 规范遵循记录 — REQ-00002
更新时间:2026-06-03 20:25
版本:V0.0.1

## 1. 本次参考的规范文件

| 规范文件 | 关联强度 | 适用条款 |
| --- | --- | --- |
| `./assistants/rules/dashboard-conventions.md` | **条件触发**(本需求只改示例值,不触发) | §规则 1(看板字段约定扩展需多文件同步 — **纯排版/格式调整例外**) |
| `./assistants/rules/doc-conventions.md` | **强** | §规则 1(README 中英同次提交);§规则 2(命令反映实际状态) |
| `./assistants/rules/marketplace-protocol.md` | 弱(不触发) | §规则 1(本需求不改协议清单字段) |
| `./assistants/rules/module-conventions.md` | 弱(不触发) | §规则 1(本需求不创建新资源) |
| `./assistants/rules/skill-conventions.md` | **中**(不改 frontmatter) | §规则 1(SKILL.md frontmatter 必含 `name` + `description`;本需求只改正文) |

## 2. 规范 vs 现状偏离

**无偏离**。本仓库所有现有结构均符合规范(本仓库本身就是按规范构建的基线),本需求在规范框架内执行。

## 3. 规范 vs 需求冲突

**无冲突**。本需求的 10 条 FR 全部在规范允许的范围内:
- FR-1(定义新编码格式):新建规则文件由 `code-rule` 维护,符合 `code-rule` 的语义边界
- FR-2(同步 10 SKILL.md):只改正文,不动 frontmatter,符合 `skill-conventions.md §规则 1`
- FR-3(同步模板):不改模板结构,符合 `module-conventions.md §规则 1`
- FR-4(同步 README):`doc-conventions.md §规则 1` 要求中英同次提交
- FR-5(同步 CLAUDE.md):`doc-conventions.md §规则 2` 要求命令与实际一致
- FR-6(追溯重命名):`marketplace-protocol.md §规则 1` 不触发
- FR-7(新建 `encoding-conventions.md`,条件 Q-8 = a):由 `code-rule` 创建,符合 `code-rule` 的语义边界
- FR-8(持久化 `migration-mapping.md`,条件 Q-9 = a):无规范冲突
- FR-9(版本看板同步):`dashboard-conventions.md §规则 1` 不触发(只改示例值,不改字段语义)
- FR-10(不修改 marketplace.json / plugin.json / 仓库目录 / git 远端):与 `marketplace-protocol.md §规则 1` 强一致

## 4. 用户授权的偏离

**无**。本设计无任何对规范的偏离。

## 5. 规范触发的工作流约束(本设计采纳清单)

| 规范条款 | 触发的工作流约束 | 本设计的实现 |
| --- | --- | --- |
| `dashboard-conventions.md §规则 1` | (条件)看板字段约定扩展需三处同步 | **本需求不触发** — 只改 `version-RESULT.md` 中的示例值,不改字段语义 / 区段结构 / 表格列 |
| `doc-conventions.md §规则 1` | README 中英同次提交 | `code-it` 阶段 T-3 子任务同时修改 `README.md` + `README.en.md`(1 个 commit) |
| `doc-conventions.md §规则 2` | README 中命令/路径反映实际 | T-3 子任务的全部替换都是"为反映新格式而更新" |
| `skill-conventions.md §规则 1` | SKILL.md frontmatter 必含 `name` + `description` | T-1 子任务的 `Edit` 操作**锁定只改正文**,不触碰 frontmatter |
| `module-conventions.md §规则 1` | 资源在固定子目录 | 本需求不创建新资源(除条件 Q-8 = a 的 `encoding-conventions.md` 在 `rules/`,由 `code-rule` 创建) |
| `marketplace-protocol.md §规则 1` | `marketplace.json` / `plugin.json` 字段约束 | FR-10 显式禁止修改;`code-it` 阶段 `git diff --stat` 兜底 |

## 6. 待澄清项的处理(本设计采用默认值的依据)

REQU 文档中 5 项未答复(Q-6 / Q-8 / Q-9 / Q-10 / Q-12),Q-7 已锁定 v2。本设计采用默认值。详细记录见 `clarifications.md`。这些默认值的选择**未触发**任何规范违反:

| Q | 默认值 | 规范层面是否合规 |
| --- | --- | --- |
| Q-6(EXISTING- 是否改 REQ-NNNNN) | 不改(保留 EXISTING-) | ✅ 符合 `module-conventions.md §规则 1`(资源不散落);`doc-conventions §规则 1` 仅约束中英 README,不约束基线版本 |
| Q-8(是否新建 `encoding-conventions.md`) | 新建(由 `code-rule` 创建) | ✅ 符合 `code-rule` 语义边界(CLAUDE.md §"版本感知工作空间约定") |
| Q-9(是否持久化 `migration-mapping.md`) | 持久化 | ✅ 符合 NFR-3(可观测性/追溯),无规范冲突 |
| Q-10(cache 同步 README 提示) | 不加(沿用现状) | ✅ 符合 NFR-5(最小化) |
| Q-12(TASK 嵌套前缀含 REQ- 与否) | 仅数字段(`TASK-REQ-00001-00001`) | ✅ 符合 NFR-5(简洁) |

## 7. 规范变更响应(本设计为首次,无历史)

N/A(首次设计,无既有规范变更需要响应)
