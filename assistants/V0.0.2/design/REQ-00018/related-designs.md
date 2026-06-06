# 关联设计 — REQ-00018
更新时间:2026-06-06 13:00
版本:V0.0.2
需求编码:REQ-00018

## 同版本关联(`./assistants/V0.0.2/design/*/RESULT.md`)

| 关联设计 | 关联点 | 对本设计的影响 | 链接 |
| --- | --- | --- | --- |
| **REQ-00005**(V0.0.2) | 优化 `code-require` / `code-design` / `code-plan` 3 个技能;**NFR-2** 强约束"修改 SKILL.md 时不破坏 frontmatter" | **0 冲突**(本需求沿用 REQ-00005 同样的"增量追加,不改 frontmatter"模式 — D-1 选定 A) | [design/REQ-00005/RESULT.md](../REQ-00005/RESULT.md) |
| **REQ-00009**(V0.0.2) | `code-unit` 步骤 0a Glob 检查项目可测性;**NFR-1 零新增依赖** | **0 冲突**(本需求**也**用 `Glob` 扫描 CWD 文件,与 REQ-00009 模式一致 — 严守 NFR-1) | [design/REQ-00009/RESULT.md](../REQ-00009/RESULT.md) |
| **REQ-00015**(V0.0.2) | `code-merge` 技能加入 marketplace;**NFR-3** `marketplace.json` 仅追加,不修改既有字段 | **0 冲突**(本需求**不**修改 `marketplace.json` / `plugin.json` / `code-skills` 自身产物 — Q1 选定 A) | [design/REQ-00015/RESULT.md](../REQ-00015/RESULT.md) |
| **REQ-00017**(V0.0.2) | `code-plan` 不拆"更新看板"任务;**强约束** "1 任务 = 1 实际产出" | **0 冲突**(本需求拆任务时**不**包含"更新看板"派生任务,严守 REQ-00017) | [design/REQ-00017/RESULT.md](../REQ-00017/RESULT.md) |

## 跨版本关联(可选,`./assistants/*/design/*/RESULT.md`)

| 关联设计 | 关联点 | 影响 | 链接 |
| --- | --- | --- | --- |
| (无) | 本需求是首次定义"CWD 项目类型描述文件同步"语义,无跨版本先例 | — | — |

## 关键交叉点(每条 FR 对应关联设计章节)

| FR | 对应关联设计章节 | 影响 |
| --- | --- | --- |
| FR-1(新增步骤 7) | REQ-00009 NFR-1 零新增依赖 + 既有 `Glob` 模式 | 沿用既有 `Glob` + `Read` + `Edit` 工具,**不引入**新依赖 |
| FR-1(锚点) | REQ-00005 NFR-2 增量追加不破坏 frontmatter | 在 `code-version/SKILL.md` 锚点 = "## 工作流程" 之后 / "## 看板字段约定" 之前插入小节,**不**改 frontmatter + **不**改既有步骤 1~6 |
| FR-2(版本号同步默认值) | REQ-00015 NFR-3 marketplace 既有字段不变(本需求不动 marketplace) | **不**修改 `code-skills` 自身的 `marketplace.json` / `plugin.json` |
| FR-5(屏幕输出契约) | REQ-00013 标题解析工具函数(本需求**不**直接复用 `code-it` 的工具函数,但屏显格式可参考中点 `·`) | 输出格式:`<文件名>: <旧版本号> → <新版本号>` |

## 关联设计无冲突确认

- ✅ **不修改** `code-skills` 自身任何文件(Q1 锁定,NFR-4 严守)
- ✅ **不**违反 REQ-00017 "1 任务 = 1 实际产出"约束(本轮不拆"更新看板"派生任务)
- ✅ **不**违反 REQ-00005 NFR-2 frontmatter 字节级保留(沿用既有"增量追加,不改 frontmatter"模式)
- ✅ **不**违反 REQ-00009 NFR-1 零新增依赖(仅用既有 `Glob` / `Read` / `Edit` 工具)
- ✅ **不**违反 REQ-00015 NFR-3 marketplace 既有字段不变(本需求不动 marketplace)
- ✅ **不**违反 REQ-00013 标题解析约束(本需求屏幕输出格式与 `formatReqTitle` 不冲突)
