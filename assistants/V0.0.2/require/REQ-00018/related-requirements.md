# 关联需求 — REQ-00018

更新时间:2026-06-06 12:45
版本:V0.0.2
需求编码:REQ-00018

## 同版本关联(`./assistants/V0.0.2/require/*/RESULT.md`)

| 关联需求 | 关联点 | 对本需求的影响 | 链接 |
| --- | --- | --- | --- |
| **REQ-00005** | 优化 `code-require` / `code-design` / `code-plan` 3 个技能,增加"首步拉取最新代码"与"末步兜底提交";**NFR-2 强约束**:"修改 SKILL.md 时不破坏 frontmatter"(本需求也遵守) | **0 冲突**(本需求是修改 `code-version/SKILL.md`,沿用 REQ-00005 同样的"增量追加,不改 frontmatter"模式) | [RESULT.md](../REQ-00005/RESULT.md) |
| **REQ-00009** | 优化 `code-unit` 技能,新增"步骤 0a 项目可测性检查"守卫(7 项 Glob 检查);**NFR-1 零新增依赖** | **0 冲突**(本需求**也**用 `Glob` 扫描 CWD 文件,与 REQ-00009 模式一致;零新增依赖 — NFR-1 严守) | [RESULT.md](../REQ-00009/RESULT.md) |
| **REQ-00015** | 新增第 12 个 `code-merge` 技能;**NFR-3** `marketplace.json` 仅追加,不修改既有字段 | **0 冲突**(本需求**不**修改 `marketplace.json` / `plugin.json` / `code-skills` 自身产物 — 详 Q1 选定 A"通用技能增强 + 扫描 CWD 项目类型") | [RESULT.md](../REQ-00015/RESULT.md) |
| **REQ-00017** | 优化 `code-plan` + `code-it` 2 个技能;**REQ-00017 强约束**:"一个任务 = 一个实际产出,看板更新不在候选集" | **0 冲突**(本需求本轮不拆任务,留作 `code-plan` 决定;若 `code-plan` 拆分时违反 REQ-00017 则退回) | [RESULT.md](../REQ-00017/RESULT.md) |

## 跨版本关联(可选,`./assistants/*/require/*/RESULT.md`)

| 关联需求 | 关联点 | 影响 | 链接 |
| --- | --- | --- | --- |
| (无) | 本需求是首次定义"通用 CWD 项目类型描述文件同步"语义,无跨版本先例 | — | — |

## 关键交叉点(每条 FR 对应关联需求)

| FR | 对应关联需求章节 | 影响 |
| --- | --- | --- |
| FR-1(`code-version` 切换后扫描 CWD 描述文件) | REQ-00009 NFR-1 零新增依赖 + 既有 `Glob` 模式 | 沿用既有 `Glob` + `Read` + `Edit` 工具,**不引入**新依赖 |
| FR-2(项目类型 → 描述文件映射) | REQ-00005 NFR-2 增量追加不破坏 frontmatter | 在 `code-version/SKILL.md` 锚点 = "## 工具使用约定" 后 / "## 工作流程" 前之间插入小节,**不**改 frontmatter + **不**改既有步骤 1~6 |
| FR-3(版本号同步默认值 = `<版本号>`) | REQ-00015 NFR-3 marketplace 既有字段不变(本需求不动 marketplace) | **不**修改 `code-skills` 自身的 `marketplace.json` / `plugin.json` |
| FR-4(屏幕输出契约) | REQ-00013 标题解析工具函数(本需求**不**直接复用 `code-it` 的工具函数,但屏显格式可参考中点 `·`) | 输出格式:`<文件名>: <旧版本号> → <新版本号>` |

## 关联需求无冲突确认

- ✅ **不修改** `code-skills` 自身任何文件(Q1 锁定)
- ✅ **不**违反 REQ-00017"不拆'更新看板'任务"约束(本轮不拆任务)
- ✅ **不**违反 REQ-00005 NFR-2 frontmatter 字节级保留(沿用既有"增量追加,不改 frontmatter"模式)
- ✅ **不**违反 REQ-00009 NFR-1 零新增依赖(仅用既有 `Glob` / `Read` / `Edit` 工具)
- ✅ **不**违反 REQ-00015 NFR-3 marketplace 既有字段不变(本需求不动 marketplace)
