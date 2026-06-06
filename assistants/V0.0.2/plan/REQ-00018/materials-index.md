# 材料登记 — REQ-00018
更新时间:2026-06-06 13:15
版本:V0.0.2
需求编码:REQ-00018

## 项目级规范(13 份全部严守)

| 规范文件 | 类别 | 关键约束摘要 | 本需求自检 |
| --- | --- | --- | --- |
| skill-conventions.md | 技能编写 | SKILL.md 必含 name + description;frontmatter 字节级保留 | ✅ INV-1 字节级保留 |
| module-conventions.md | 模块规划 | 资源放固定子目录 | ✅ 不新增资源文件 |
| directory-conventions.md | 目录结构 | 技能资源放固定子目录 | ✅ 不新增目录 |
| dependency-conventions.md | 依赖管理 | 零新增依赖优先 | ✅ NFR-1 严守 |
| dashboard-conventions.md | 看板 | 看板字段扩展需三方同步 | ✅ 0 触发 3 处同步 |
| encoding-conventions.md | 编码 | REQ / BUG / TASK 编码权威源 | ✅ 任务编号 5+5 位 |
| commit-conventions.md | 提交 | commit 消息格式 | ✅ 由 code-it 末步兜底 |
| doc-conventions.md | 文档 | 文档编写约定 | ✅ SKILL.md 行数变化在 ±20% |
| marketplace-protocol.md | marketplace | marketplace 既有字段不变 | ✅ 不修改 marketplace |
| naming-conventions.md | 命名 | 命名约定 | ✅ kebab-case |
| coding-style.md | 编码风格 | 编码风格约定 | ✅ 沿用 SKILL.md 既有风格 |
| framework-conventions.md | 框架 | 框架使用 | ✅ 不涉及 |
| migration-mapping.md | 迁移 | 跨版本映射 | ✅ 不涉及 |

## 上游需求

- 来源:`./assistants/V0.0.2/require/REQ-00018/RESULT.md`(v1)
- 提取的 FR / NFR / AC 数量:**6 / 9 / ~30**
- 关键决策:2 项已锁定(Q-1 范围 / Q-2 术语),5 项采纳默认(Q-3~Q-7),1 项建议派生(Q-8)

## 上游概要设计

- 来源:`./assistants/V0.0.2/design/REQ-00018/RESULT.md`(v1)
- 提取的模块拆分 / 接口概要 / 数据结构 / 决策:**1 模块修改 / 0 接口新增 / 0 数据结构新增 / 5 决策 D-1~D-5**
- 关键决策:`--balanced` 粒度 / 6 类描述文件 / 5 类屏幕输出 / 0 新增依赖 / 0 修改其他 12 技能

## 项目现状(实现细节)

### 仓库无测试框架
- 沿用 REQ-00009 守卫判定"项目不可测" — 所有任务测试状态 = `不适用`

### 仓库无构建/包管理工具
- 沿用 CLAUDE.md 严守 — 验证靠静态 `Read` + 人工场景验证

### SKILL.md 既有风格
- 207 行既有步骤 1-6 + 看板字段约定
- 既有"## 工作流程"小节(L74-164)
- 既有"## 看板字段约定"小节(L167-193)
- 本需求插入锚点 = "## 工作流程" 段后 / "## 看板字段约定" 段前

## 关键交叉点(每条 FR 对应详细设计章节)

| FR | 详细设计章节 | 算法/契约 |
| --- | --- | --- |
| FR-1(新增步骤 7) | §3 模块详细化 / §4 算法 | 7 步伪代码 |
| FR-1.AC-1.3(6 类描述文件 Edit 锚点) | §3.1 / §4 parseVersionField | 6 类独立锚点 |
| FR-1.AC-1.4(屏幕输出契约) | §6 屏幕输出契约 | 5 类格式 |
| FR-2(版本号取值) | §4 伪代码 `step7_syncCwdVersionFiles(newVersion)` | 默认 = `<版本号>` |
| FR-3(CWD 路径) | §4 伪代码 `step7_syncCwdVersionFiles(cwd)` | 默认 = `process.cwd()` |
| FR-4(不修改 code-skills 自身) | §3.1 / §1.2 范围 | 严守 |
| FR-5(屏幕输出契约) | §6 | 5 类全有 |
| FR-6(--skip-cwd-sync) | (本需求不实现) | 留作 v2 |
| NFR-1(零依赖) | §12 规范遵循 | ✅ 0 新增 |
| NFR-2(增量改 SKILL.md) | §3.1 / §4 锚点 | 严守 |
| NFR-3(不修改其他 12 技能) | §1.2 范围 | 严守 |
| NFR-4~6(不修改 code-skills 自身) | §1.2 范围 | 严守 |
| NFR-7(性能 < 5 秒) | §10 性能与资源 | 10 个文件 < 5 秒 |
| NFR-8(失败不阻断) | §7 异常处理 | 8 边界 0 阻断 |
| NFR-9(不参与 REQ-00005 扩展) | §3.1 锚点 | 本需求是 `code-version`,不是其他技能 |

## 关联编码计划(同版本)

| 关联计划 | 关联点 | 影响 |
| --- | --- | --- |
| REQ-00010 plan | 增量追加 SKILL.md 模式(沿用 `code-it` 步骤 0a 守卫) | 0 冲突(本需求改 `code-version`,不与 `code-it` 守卫耦合) |
| REQ-00013 plan | 屏幕输出"编号+标题"显示 | 0 冲突(本需求屏幕输出不含"编号+标题") |
| REQ-00017 plan | 1 任务 = 1 实际产出,0 派生"更新看板"任务 | 0 冲突(本需求 2 任务全为真实产出) |

## 本次变更源

不适用(本设计是首次创建,非增量更新)。
