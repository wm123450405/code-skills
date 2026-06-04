# 模块拆分 — REQ-00004

更新时间:2026-06-04 15:50
版本:V0.0.2

## 1. 总览
本需求新增**单一**技能 `code-dashboard`,所有产出物收敛到 1 个新文件(`SKILL.md`)与 1 个新目录(技能目录本体)。**不**修改任何既有模块;**不**新增子目录(无模板/清单/规则资源)。

| 类别 | 数量 | 备注 |
| --- | --- | --- |
| 新增模块 | 1 | `plugins/code-skills/skills/code-dashboard/` |
| 复用既有模块 | 1 | `code-review` 行为契约(只读 / 工具集) |
| 修改既有模块 | 0 | NFR-6 严守 |
| 删除模块 | 0 | — |

## 2. 新增模块

### M-1:`code-dashboard` 技能目录
- **路径**:`plugins/code-skills/skills/code-dashboard/`
- **状态**:**新增**
- **职责**:作为"只读型"第 11 个 `code-*` 技能,在用户调用 `/code-dashboard` 时,从 `./assistants/<版本号>/RESULT.md` 与相关子文件读取数据,渲染 ASCII 进度表 + 文本柱状图,生成最多 5 条"下一步执行建议",并打印到屏幕。**不**写入任何文件。
- **对外暴露的接口**:Claude Code 技能协议
  - `/code-dashboard`(无参数 → 版本总览模式)
  - `/code-dashboard REQ-NNNNN`(1 个参数 → 需求粒度模式)
  - `/code-dashboard <非 REQ-NNNNN 格式>`(参数校验失败,打印用法)
- **依赖**:
  - **对内**:`./assistants/.current-version`、`./assistants/<版本号>/RESULT.md`(必读);`./assistants/<版本号>/require/<REQ>/RESULT.md` + `./assistants/<版本号>/plan/<REQ>/PLAN.md`(需求模式);`./assistants/rules/encoding-conventions.md`(任务编号解析权威)
  - **对外**:无(零运行时依赖,NFR-1)
- **关键决策**:
  - **单文件技能**:本技能**不**新增 `templates/` / `checklists/` / `guidelines/` 子目录(SKILL.md 单文件自包含,无独立资源)
  - **规范依据**:`module-conventions.md §规则 1`(资源子目录)是"如需"约束;本技能"无资源"故"无需子目录"
  - **授权偏离**:见 `rule-compliance.md §4 A-1`
- **符合的规范条款**:
  | 规范文件 | 条款 | 满足情况 |
  | --- | --- | --- |
  | `skill-conventions.md` | §规则 1:SKILL.md 必含 name + description,name 与目录名一致 | **必须满足**;在 SKILL.md 顶部 YAML frontmatter 落地 |
  | `module-conventions.md` | §规则 1:资源放 templates/ / checklists/ / guidelines/ 子目录 | **部分满足**(本技能无资源,无需子目录);已在 `rule-compliance §4 A-1` 显式标注为"用户授权的偏离" |
  | `marketplace-protocol.md` | §规则 1:不动 marketplace.json / plugin.json | **必须满足**;本设计不触碰(走 Claude Code 技能自动发现协议) |
  | `encoding-conventions.md` | §规则 3:任务编号解析用嵌套式正则 | **必须满足**;SKILL.md 步骤 3 解析器算法严格按此 |

## 3. 复用既有模块

### M-2:`code-review` 行为契约
- **路径**:`plugins/code-skills/skills/code-review/SKILL.md`
- **状态**:**复用**(不修改)
- **复用点**:
  - **只读契约**:`code-review` 是唯一现存的"只读型 `code-*` 技能",其工具集为 `Read` / `Glob` / `Grep`(不写任何文件)。`code-dashboard` 同样为只读,工具集与其完全一致。
  - **状态机范式**:`code-review` 的"读区段 → 解析 → 聚合 → 渲染 → 输出"5 步流程是本设计步骤 7A 步骤 0~4 的直接参照。
  - **NFR-7 幂等**:与 `code-review` 一致,多次执行结果完全相同。
- **对原模块影响**:**0**(NFR-6 严守"不修改其他技能 SKILL.md")
- **符合的规范条款**:`skill-conventions.md §规则 1` 不触发(本设计不修改其 frontmatter)

## 4. 修改既有模块
无(NFR-6 锁)。

## 5. 可选模块(用户授权才落地)

### M-3(可选):`plugins/code-skills/CLAUDE.md` "AI 工作约定"小节
- **路径**:`plugins/code-skills/CLAUDE.md` 末段
- **状态**:**修改**(可选,本设计**建议不**触发)
- **若触发**:在"AI 工作约定"小节追加一段"指引 N: `code-dashboard` 行为约定"——描述展示策略、建议策略、解析锚点
- **不触发的理由**:
  - 本节由 `code-rule` 维护(CLAUDE.md 显式声明),手动修改可能被覆盖
  - 本设计阶段不调用 `code-rule`,避免与 V0.0.2 其他并发需求产生交叉
  - `code-dashboard` 行为约定可留作后续 `code-rule` 沉淀(后续需求触发)
- **若改需同步的 2 处**:`plugins/code-skills/CLAUDE.md` + `plugins/code-skills/CLAUDE.md`(CLAUDE.md 暂未要求中英对仗,但建议附注)
- **符合的规范条款**:`doc-conventions.md §规则 1`(CLAUDE.md 不属 README,不强制中英对仗);`skill-conventions.md §规则 1`(不影响 SKILL.md)

### M-4(可选):`plugins/code-skills/README.md` + `README.en.md` 技能清单
- **路径**:`plugins/code-skills/README.md` + `plugins/code-skills/README.en.md`
- **状态**:**修改**(可选,本设计**建议不**触发)
- **若触发**:在两文件"主要能力"或"技能清单"段追加一行:
  - 中文:`| code-dashboard | 开发看板(只读) | 展示当前版本需求/任务/缺陷进度 + 下一步建议 |`
  - 英文:`| code-dashboard | Dev Dashboard (read-only) | Show version req/task/bug progress + next-step suggestions |`
- **不触发的理由**:本需求`code-dashboard` 实际可独立工作(走 Claude Code 技能协议),README 不改不影响功能;若改必须中英同次提交(`doc-conventions §规则 1`),并与 V0.0.2 其他需求(REQ-00012 也在改 README)协调
- **符合的规范条款**:`doc-conventions.md §规则 1`(中英结构对仗)+ `§规则 2`(核心小节必覆盖)

## 6. 后续子任务预想(供 `code-plan` 拆分参考)
`code-plan` 阶段可能将本设计拆分为以下 N 个开发任务(本设计**不强制**粒度,仅预想):

| 任务 | 路径 | 工作量 | 关键产出 |
| --- | --- | --- | --- |
| T-1 | `plugins/code-skills/skills/code-dashboard/SKILL.md` | 主体 | YAML frontmatter + 目标 + 适用 + 步骤 0~7 + 边界 + 工具约定 |
| T-2(可选) | `plugins/code-skills/CLAUDE.md` | 1 行 | 追加"指引 N: code-dashboard 行为约定" |
| T-3(可选) | `plugins/code-skills/README.md` + `README.en.md` | 2×1 行 | 中英同次提交,各追加一行 |
| T-4 | `assistants/V0.0.2/design/REQ-00004/RESULT.md` 等 7 文件 | 7 文件 | 本次 design 阶段已落地;`code-it` 阶段无需重复 |
| T-5 | `assistants/V0.0.2/RESULT.md` "概要设计清单" + "变更记录" | 2 处 | 本次 design 阶段已同步 |

> T-1 是**必须**任务,T-2 / T-3 是**可选**(用户授权才落地),T-4 / T-5 是 `code-design` 阶段的"同步动作",由本技能自身完成(不进入 `code-plan`)。

## 7. 自检(对照 `module-conventions.md §规则 1` 与 `directory-conventions.md`)
- [x] 技能名(`code-dashboard`)为 kebab-case,与目录名一致 — `skill-conventions §规则 1`
- [x] 技能根目录仅放 `SKILL.md`,无散落资源 — `module-conventions §规则 1` 反面示例规避
- [x] 无 `templates/` / `checklists/` / `guidelines/` 子目录(本技能无资源,授权偏离) — `module-conventions §规则 1` + A-1
- [x] 无循环依赖(对内:read-only;对外:0) — `module-conventions §规则 1` 隐含
- [x] 命名风格:`code-dashboard` = `code-` 前缀 + `dashboard` 词根,与既有 10 个技能一致 — `skill-conventions` 隐含
- [x] 路径:`plugins/code-skills/skills/code-dashboard/`,与既有 10 个技能同位
