# 材料登记 — REQ-00002
更新时间:2026-06-03 20:18(v2 增量更新)

## 概览
本需求由用户通过 `code-require` 技能的 `ARGUMENTS` 参数直接发起,**未在 `./assistants/V0.0.1/require/REQ-00002/` 目录下放置任何独立材料文件**。
所有原始信息来自:
1. 用户调用本技能时给出的自然语言描述(argument)
2. 第一轮澄清问答(见 `clarifications.md`)
3. 仓库当前状态扫描结果(SKILL.md / templates / README / CLAUDE.md / 历史需求)
4. 项目级规范文件(`./assistants/rules/`)

## 材料表

| 材料编号 | 来源 | 类型 | 用途 | 读取状态 | 关键摘要 |
| --- | --- | --- | --- | --- | --- |
| M-1 | 用户原始 argument:`调整需求编码、任务编码、缺陷编码的规则，统一使用 REQ-NNNNN TASK-NNNN BUG-NNNNN 的格式` | 自然语言 | 需求主旨 | 已读 | 三类编码格式调整;TASK 位数与表述被在 Q3 中确认为 5 位 |
| M-2 | 第一轮澄清(AskUserQuestion 回复) | 结构化问答 | 限定本需求编码、追溯范围、位数 | 已读 | 本需求 = REQ-00002(新格式);追溯覆盖现有需求重命名;三类编码统一 5 位(REQ/TASK/BUG-NNNNN) |
| M-3 | 仓库扫描 — SKILL.md(10 个) | 文档 | 现状基线(嵌入旧格式) | 已读 | code-it / code-plan / code-unit / code-review / code-fix / code-init / code-version / code-require / code-rule / code-design 中均含 `REQ-YYYY-NNNN`、`BUG-NNN`、`<任务编码>`(格式 `<需求编号>-<任务序号>`)等说明;`code-it` 含 regex `^REQ-\d{4}-\d{4}-\d{3}$` |
| M-4 | 仓库扫描 — templates(20+ 文件) | 文档 | 模板示例引用旧格式 | 已读 | requirements.md / design.md / plan.md / task-plan.md / RESULT.md(it/unit) / REVIEW-REPORT.md / REVIEW-FIX.md / fix-registry.md / existing-requirement.md / INIT-REPORT.md / assistants-layout.md(多个技能下副本)等含示例 `REQ-2026-0001`、`BUG-001`、`REQ-2026-0001-001` |
| M-5 | 仓库扫描 — `plugins/code-skills/README.md` | 文档 | 用户面向的安装与流程示例 | 已读 | 含多段 `REQ-YYYY-NNNN`、`BUG-NNN`、`REQ-2026-0001`、`code-require REQ-YYYY-NNNN` 示例 |
| M-6 | 仓库扫描 — `plugins/code-skills/README.en.md` | 文档 | 英文对仗 | 已读 | 结构对仗,内含与 README.md 一致的格式示例 |
| M-7 | 仓库扫描 — `plugins/code-skills/CLAUDE.md` | 文档 | AI 工作指引,提到 `REQ-YYYY-NNNN`、`BUG-NNN` 概念 | 已读 | 第 24/88/99/100 行等含 BUG-NNN 与 REQ-YYYY-NNNN 引用 |
| M-8 | 历史数据 — `./assistants/V0.0.1/require/REQ-00001/`(原 `REQ-2026-0001/`,2026-06-03 20:20 重命名) | 工作目录 | 追溯对象 | 已读 | 当前编码 REQ-00001;本工作空间维度重命名已落地,SKILL.md/模板/README/CLAUDE.md 的旧编码引用仍待 `code-it` 阶段清理 |
| M-9 | 历史数据 — `./assistants/V0.0.0/require/EXISTING-001~010/` | 工作目录 | 追溯对象(语义为 code-init 基线特例) | 已读 | EXISTING- 前缀语义与 REQ- 不同(基线已存在功能 vs 新需求);本次是否纳入"追溯覆盖"待澄清(见 Q-6) |
| M-10 | `./assistants/rules/marketplace-protocol.md` | 规范(只读) | 与本需求无关 | 已读 | 未触发 |
| M-11 | `./assistants/rules/doc-conventions.md` | 规范(只读) | README 中英文同步、README 持续维护 | 已读 | 本需求改动 README → 触发 §规则 1 + §规则 2,中英文必须同次提交同步;README 中所有命令必须与改后实际状态一致 |
| M-12 | `./assistants/rules/dashboard-conventions.md` | 规范(只读) | 看板/模板扩展同步 | 已读 | 本需求改动 `version-RESULT.md` 模板(若含格式示例)或字段语义说明 → 触发 §规则 1,需同时改 `templates/version-RESULT.md` + `CLAUDE.md` + 本规范 |
| M-13 | `./assistants/rules/skill-conventions.md` | 规范(只读) | SKILL.md frontmatter 必含 name+description | 已读 | 本需求会修改 SKILL.md 正文(非 frontmatter)→ 不触发 §规则 1;但仍需保持 frontmatter 完整 |
| M-14 | `./assistants/rules/module-conventions.md` | 规范(只读) | 技能资源固定子目录 | 已读 | 若新增 `encoding-conventions.md` 规则文件,放在 `./assistants/rules/`(本规则适用 `skills/*/`,不直接管 `assistants/rules/`,但作为新增类规则,建议在 `code-rule` 维护下) |
| M-15 | `./assistants/V0.0.1/RESULT.md` | 版本看板 | 待同步目标 | 已读 | 已含 REQ-2026-0001;本需求需追加 REQ-00002 |
| M-16 | 第 2 轮用户追加指令(`/code-require REQ-00002 ...`) | 自然语言 | 锁定 Q-7 答案 | 已读 | 用户回答 Q-7:TASK 编码采用嵌套式 `TASK-REQ-<REQ>-NNNNN` / `TASK-BUG-<BUG>-NNNNN` |

## 不可读材料
- 无音视频/二进制材料

## 待用户补充
- 无(必要时后续追加迁移脚本草稿、changelog 草稿或其它素材,放入本目录再触发增量更新)
