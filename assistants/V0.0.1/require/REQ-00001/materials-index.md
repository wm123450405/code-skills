# 材料登记 — REQ-00001
更新时间:2026-06-03 20:20(v2 同步标题与本目录路径,内容不变)

## 概览
本需求由用户通过 `code-require` 技能的 `ARGUMENTS` 参数直接发起,**未在 `./assistants/V0.0.1/require/REQ-00001/` 目录下放置任何独立材料文件**。
所有原始信息来自:
1. 用户调用本技能时给出的自然语言描述(argument)
2. 第一轮澄清问答(见 `clarifications.md`)
3. 仓库当前状态(`marketplace.json` / `plugin.json` / README / CLAUDE.md)与项目级规范文件

## 材料表

| 材料编号 | 来源 | 类型 | 用途 | 读取状态 | 关键摘要 |
| --- | --- | --- | --- | --- | --- |
| M-1 | 用户原始 argument:`修改marketplace名称，增加-marketplace后缀` | 自然语言 | 需求主旨 | 已读 | 把 marketplace 的"名称"加上 `-marketplace` 后缀 |
| M-2 | 第一轮澄清(AskUserQuestion 回复) | 结构化问答 | 限定改名范围 | 已读 | 仅改 `.claude-plugin/marketplace.json` 根 `name` 字段;其它 name 不变 |
| M-3 | `.claude-plugin/marketplace.json`(仓库根) | JSON 协议清单 | 现状基线(待修改的目标文件) | 已读 | 根 `name="code-skills"`,`owner.name="code-skills"`,`plugins[0].name="code-skills"`,`plugins[0].author.name="code-skills"`,含完整 skills 数组 |
| M-4 | `plugins/code-skills/.claude-plugin/plugin.json` | JSON 协议清单 | 协议同步约束参照(本次不修改) | 已读 | `name="code-skills"`,`version="1.0.0"`,`author.name="code-skills"` |
| M-5 | `plugins/code-skills/README.md` | 文档 | 含安装命令与 marketplace name 引用,需同步 | 已读 | 第 11/14/22 行出现 `code-skills@code-skills`、"marketplace name 是 `code-skills`" 等引用 |
| M-6 | `plugins/code-skills/README.en.md` | 文档 | 多语言对仗版本,需同步 | 已读 | 与 README.md 结构对仗的英文版,含相同 install 命令与 marketplace name 引用 |
| M-7 | `plugins/code-skills/CLAUDE.md` | 文档 | 内部 AI 工作指引,需核查是否含 marketplace name 引用 | 已读 | 含"marketplace 仓库根"等结构描述,但未直接使用 `code-skills@code-skills` 安装命令字符串 |
| M-8 | `./assistants/rules/marketplace-protocol.md` | 规范(只读) | 协议字段约束(`$schema`/`name`/`version` 必填,plugins[].name 与 plugin.json 同步等) | 已读 | 见规则 1:本次改根 `name` 不影响 `plugins[].name` 与 `plugin.json` 的 `name`,符合约束 |
| M-9 | `./assistants/rules/doc-conventions.md` | 规范(只读) | README 多语言对仗(规则 1)与持续维护(规则 2) | 已读 | 强制:README.md 与 README.en.md 中任一改动必须同步 |
| M-10 | `./assistants/rules/dashboard-conventions.md` | 规范(只读) | 看板/模板扩展同步(规则 1) | 已读 | 本需求不修改看板字段约定,不触发本规则 |
| M-11 | `./assistants/V0.0.1/RESULT.md` | 版本看板 | 待同步目标(收尾追加"需求清单" + "变更记录") | 已读 | 当前"需求清单"为空,本需求将首次填入 |

## 不可读材料
- 无音视频/二进制材料

## 待用户补充
- 无(若后续追加迁移指引、changelog 草稿或其它素材,放入本目录再触发增量更新)
