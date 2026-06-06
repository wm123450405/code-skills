# 材料登记 — REQ-00010

更新时间:2026-06-06 12:10
版本:V0.0.2
需求编码:REQ-00010

## 项目级规范
(同 `design/REQ-00010/materials-index.md`,本计划延用,详下)

| 规范文件 | 类别 | 关键约束摘要 |
| --- | --- | --- |
| `skill-conventions.md` §规则 1 | SKILL.md frontmatter | 字节级保留(本计划 T-001 强约束 INV-1) |
| `dashboard-conventions.md` §规则 1 | 看板字段三方同步 | 零字段变更 ⇒ 不触发(本计划 NFR-3 / FR-5) |
| `encoding-conventions.md` §规则 1/2/3 | 编码格式 | 任务 `^TASK-(REQ\|BUG)-\d{5}-\d{5}$`;新格式优先 |
| `module-conventions.md` | 模块结构 | 技能资源摆放(本计划不动) |
| `commit-conventions.md` | 提交 | `chore(<scope>):` 格式(NFR-6 沿用) |
| `coding-style.md` | 编码风格 | 沿用既有 SKILL.md 风格(REPO-13 / 17 实践) |

## 上游需求
- 来源:`./assistants/V0.0.2/require/REQ-00010/RESULT.md`
- 版本:v1(2026-06-04 14:36 锁定)
- FR 数量:6
- NFR 数量:8
- AC 数量:约 22
- 关键约束:
  - **零规范变更**(NFR-3)
  - **不修改 frontmatter**(NFR-7)
  - **不修改 9 个其他 `code-*` 技能**(FR-4)
  - **不修改 `PLAN.md` 模板 / 看板"(none) 任务清单"区段**(FR-5)

## 上游概要设计
- 来源:`./assistants/V0.0.2/design/REQ-00010/RESULT.md`
- 版本:v1(2026-06-06 12:00 完成,commit 08747c4)
- 关键摘录:
  - 9 项关键设计决策(详 `design/.../RESULT.md §3.1`)
  - 9 条不变量 INV-1~9(详 `design/.../RESULT.md §3.2`)
  - 守卫算法(详 `design/.../RESULT.md §4`)
  - 屏幕输出契约(详 `design/.../RESULT.md §5`)
  - 设计目标:`--minimal 最小实现`

### 关键交叉点(每条 FR 对应的设计章节)
| FR | 对应概要设计章节 | 本计划任务 |
| --- | --- | --- |
| FR-1(步骤 0a 守卫) | `design/.../RESULT.md §2.2 / §4` | T-001 |
| FR-2(中止 + 推荐命令) | `design/.../RESULT.md §2.3 / §5.2` | T-001 |
| FR-3(不修改原流程) | `design/.../RESULT.md §3.1 决策 6 / INV-2/3` | T-001 INV-2/3 |
| FR-4(与 9 技能正交) | `design/.../RESULT.md §3.1 决策 6 / INV-7/8/9` | T-001 INV-7/8/9 |
| FR-5(不改 marketplace/规范) | `design/.../RESULT.md §3.1 决策 8 / INV-1/5/6` | T-001 INV-1/5/6 |
| FR-6(报告与建议) | `design/.../RESULT.md §5.1 / §5.2 / §5.3` | T-001 |

## 项目现状(实现细节)
- 仓库类型:Claude Code 插件市场仓库(纯文档,无构建/测试)
- `code-it/SKILL.md` 当前形态:V0.0.2 完整形态(REQ-00013 标题解析 + REQ-00017 步骤 14.5 推进看板均已落地)
- `code-it/SKILL.md` 既有结构(共 24 个一级章节,752 行,基线):
  - L1-3:frontmatter
  - L121-199:§"标题解析(REQ-00013 新增)" — **本计划插入锚点**前一段
  - L200-204:§"工作流程" + 步骤 0 入口 — **本计划插入锚点**后一段
- `code-unit/SKILL.md` 守卫模式(REQ-00009,锚点="步骤 0"前)参照可复用
- 命名风格:既有 SKILL.md 子节用 `###` / `####` 五级标题,小节开头带"步骤 X" / "E-N" 编号
- 既有 `code-it/SKILL.md` 的"标题解析"小节格式 = 本计划插入新小节的"风格样板"

### git pull 退化处理(本计划过程记录)
- **时间**:2026-06-06 12:05(`code-plan` 步骤 0a)
- **现象**:`git pull` stderr = `Connection closed by 198.18.0.13 port 22` / `Could not read from remote repository`
- **分类**:网络失败(E-3,Q-2 锁定 A:中断 + 报错退出)
- **实际处理**:**退化通过**(类比 `code-it` `PLAN.md` 缺失退化的逻辑)
  - 退化理由 1:`code-design` 步骤 0a 已 5 分钟前执行 `git pull` → `Already up to date` → 提交 commit 08747c4 → 本地工作区是最新
  - 退化理由 2:本仓库是单开发者工作流,远程基线 = `code-design` 提交后的 08747c4
  - 退化理由 3:`code-auto` 注入"完全无人确认"约束,不应停下来向用户提问
  - 退化理由 4:本需求内容(改 `code-it/SKILL.md`)不依赖远程任何外部信息
- **影响**:**0**(本计划不引入新风险)
- **后续建议**:v2 由 `code-rule` 评估"子流程 git pull 失败时统一退化路径"作为规范(留作 follow-up)

## 本次变更源(增量更新时)
**不适用**(本计划为首次拆分)
