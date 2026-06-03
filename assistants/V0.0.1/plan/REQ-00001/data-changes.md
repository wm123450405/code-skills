# 数据结构完整变更 — REQ-00001(code-plan 阶段)
更新时间:2026-06-03 20:30
版本:V0.0.1

## 修改实体:.claude-plugin/marketplace.json

| 路径 | 字段 | 类型 | 改前 | 改后 | 约束 |
| --- | --- | --- | --- | --- | --- |
| `$.name` | 根 name | string | `"code-skills"` | `"code-skills-marketplace"` | 必填,kebab-case(Q-5 默认 A 保持) |
| `$.version` | 根 version | string | `"1.0.0"` | (不变) | 必填,semver |
| `$.description` | 根 description | string | (现状) | (不变) | 可选,纯文本(Q-3 默认 B 不改) |
| `$.owner.name` | owner.name | string | `"code-skills"` | (不变) | 必填 |
| `$.plugins[0].name` | plugin name | string | `"code-skills"` | (不变) | 必填,必须与 `plugin.json` 同步 |
| `$.plugins[0].version` | plugin version | string | `"1.0.0"` | (不变) | 必填,必须与 `plugin.json` 同步 |
| `$.plugins[0].source` | plugin 路径 | string | `"./plugins/code-skills"` | (不变) | 必填,以 `./` 开头 |
| `$.plugins[0].skills` | skills 列表 | string[] | 10 项 | (不变) | 必填,相对路径数组 |
| `$.plugins[0].keywords` | keywords | string[] | 10 项 | (不变) | 可选 |

- **关系**:本 JSON 描述本仓库对外暴露的 marketplace 与所含 plugin 列表
- **存储选型**:Claude Code 加载时解析(无需存储)
- **迁移脚本**:N/A(本次仅改 1 个字符串)
- **依据规范**:`marketplace-protocol.md §规则 1`(全部)

## 修改实体:plugins/code-skills/README.md
- **字段变更**(以 `code-it` 实施时 Read 实际行号为准):
  - 第 14 行 install 命令:`code-skills@code-skills` → `code-skills@code-skills-marketplace`
  - 第 22 行 marketplace name 解释:`code-skills` → `code-skills-marketplace`
- **索引变更**:N/A
- **迁移需求**:N/A(纯文本)
- **依据规范**:`doc-conventions.md §规则 1/2`

## 修改实体:plugins/code-skills/README.en.md
- **字段变更**:与中文版对应
  - 第 14 行 install 命令:`code-skills@code-skills` → `code-skills@code-skills-marketplace`
  - 第 22 行 marketplace name 解释:`code-skills` → `code-skills-marketplace`
- **索引变更**:N/A
- **迁移需求**:N/A
- **依据规范**:`doc-conventions.md §规则 1/2`

## 可能修改实体:plugins/code-skills/CLAUDE.md
- **字段变更**:**默认 0 变更**(Grep 验证后决定)
- **依据规范**:`doc-conventions.md §规则 2`

## 不修改实体清单
| 实体 | 不修改原因 |
| --- | --- |
| `plugins/code-skills/.claude-plugin/plugin.json` 任何字段 | `marketplace-protocol.md §规则 1.3` 同步约束(本需求改根 name,plugin 标识独立) |
| `plugins/code-skills/` 目录名 | NFR-2 / FR-2 显式禁止 |
| git 远端仓库名 | NFR-2 / FR-2 显式禁止 |
| 10 个 SKILL.md | FR-7 显式禁止 |
| 20+ 模板 | FR-7 显式禁止 |
| 5 个规范文件 | FR-7 显式禁止 |
| V0.0.0 基线 | FR-7 显式禁止 |
