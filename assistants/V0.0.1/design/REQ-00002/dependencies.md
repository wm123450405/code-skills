# 三方依赖评估 — REQ-00002
更新时间:2026-06-03 20:25
版本:V0.0.1

## 结论

**本需求不新增任何第三方依赖**。本仓库是 Claude Code 技能定义集合,无应用代码、无构建工具、无运行时依赖;新增的"工具"是字符串编辑本身 + 1-2 个新文档文件(条件触发)。

## 现有依赖盘点

| 类别 | 数量 | 说明 |
| --- | --- | --- |
| 第三方运行时依赖 | 0 | 本仓库无 Node.js / Python / Go 等代码 |
| 第三方构建工具 | 0 | 本仓库无 package.json / requirements.txt / go.mod 等 |
| 第三方测试框架 | 0 | 本仓库无任何测试代码 |
| 第三方 Lint 工具 | 0 | 本仓库无任何 Lint 配置 |
| Claude Code 协议依赖 | 2(隐式) | `marketplace.json` / `plugin.json` 的 `$schema` 引用官方 JSON Schema;本需求不改 `$schema` 字段 |
| 自定义规则文件(项目级) | 5 | `dashboard-conventions.md` / `doc-conventions.md` / `marketplace-protocol.md` / `module-conventions.md` / `skill-conventions.md`;本需求不修改 |

## 评估本需求是否需要新增依赖

| 候选工具 | 评估 | 结论 |
| --- | --- | --- |
| 自动化字符串替换脚本(shell / sed / awk / Node.js) | 不必要 — `Edit` 工具已能精确替换;`Grep` 工具已能验证;引入脚本违反 NFR-5(最小化) | **不引入** |
| 编码格式自动校验脚本 | 不必要 — NFR-5 显式禁止"引入编码自动校验脚本"(本仓库无 lint 体系) | **不引入** |
| 编码格式自动生成器 | 不必要 — NFR-5 显式禁止"引入编码自动生成器"(沿用 AI + 人工) | **不引入** |
| JSON 校验工具(jq / jsonlint) | 不必要 — Claude Code 协议清单由 Claude Code 加载时解析,加载失败立即报错;`code-review` 阶段 diff 审阅即可 | **不引入** |
| 翻译辅助工具 | 不必要 — `code-review` 阶段并列对比 README.md 与 README.en.md 即可 | **不引入** |
| 编码"权威源"工具(Q-8 = a 时的 `encoding-conventions.md`) | **非运行时依赖**,仅文档文件;由 `code-rule` 维护,本需求不直接创建 | **不引入** |
| CI 流水线(实施后跑 lint) | 不必要 — 本仓库无 CI 配置,且 NFR-5 显式禁止 | **不引入** |
| Markdown 链接 / 格式校验工具 | 不必要 — 本仓库历史文档均人工维护 | **不引入** |

## 决策依据

- `NFR-5(可维护性 / 最小化)` 显式要求:"不引入编码自动校验脚本、不引入编码自动生成器"
- `REQU FR-7` 显式要求"本需求不直接写入 `./assistants/rules/`",仅"记录将由 code-rule 在实施阶段创建"(若 Q-8 = a)
- `REQU FR-10` 显式要求"不修改 marketplace.json / plugin.json / 仓库目录 / git 远端"
- `module-conventions.md §规则 1` 仅约束资源摆放,不约束依赖管理

## 后续需求可能引入的依赖(备注)

| 后续需求 | 可能引入 | 是否在本需求范围 |
| --- | --- | --- |
| (Q-8 = a) 由 `code-rule` 新建 `encoding-conventions.md` | 0 个(纯文档) | 否(Q-8 = a 时由 `code-rule` 在实施阶段创建) |
| 未来 CI 流水线 | GitHub Actions 等 | 否,需新建独立 REQ |
| 编码自动生成 / 校验 | 0 个(已被 NFR-5 显式禁止) | 否 |
