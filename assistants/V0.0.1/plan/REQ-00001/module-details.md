# 模块详细化 — REQ-00001(code-plan 阶段)
更新时间:2026-06-03 20:30
版本:V0.0.1

## 模块:.claude-plugin/marketplace.json
- **路径**:`.claude-plugin/marketplace.json`
- **关键字段**:
  - 根 `name`(本次改):`"code-skills"` → `"code-skills-marketplace"`
  - 根 `$schema`(保持):`"https://anthropic.com/claude-code/marketplace.schema.json"`
  - 根 `version`(保持):`"1.0.0"`
  - 根 `description`(保持):现有文本(Q-3 默认 B 不改)
  - 根 `owner.name`(保持):`"code-skills"`
  - `plugins[0].name`(严禁改):`"code-skills"`
  - `plugins[0].version`(保持):`"1.0.0"`
  - `plugins[0].source`(保持):`"./plugins/code-skills"`
  - `plugins[0].skills`(保持):10 项
  - `plugins[0].keywords`(保持):10 项
- **调用顺序**:N/A(JSON 静态文件)
- **状态归属**:N/A
- **与概要设计的对应**:§6.1 marketplace.json 字段表
- **符合的规范**:`marketplace-protocol.md §规则 1.1/1.2/1.3/1.4/1.5/1.6`

## 模块:plugins/code-skills/README.md
- **路径**:`plugins/code-skills/README.md`
- **关键行**(本次改,以 `code-it` 实施时 Read 实际行号为准):
  - 第 14 行:`` `claude plugin install code-skills@code-skills` `` → `` `claude plugin install code-skills@code-skills-marketplace` ``
  - 第 22 行:`> ...marketplace name 是 `code-skills`...` → `> ...marketplace name 是 `code-skills-marketplace`...`
- **调用顺序**:N/A(纯文档)
- **状态归属**:N/A
- **与概要设计的对应**:§6.3 README 中需要替换的字面量清单
- **符合的规范**:`doc-conventions.md §规则 1/2`

## 模块:plugins/code-skills/README.en.md
- **路径**:`plugins/code-skills/README.en.md`
- **关键行**(本次改,以 `code-it` 实施时 Read 实际行号为准):
  - 第 14 行:`claude plugin install code-skills@code-skills` → `claude plugin install code-skills@code-skills-marketplace`
  - 第 22 行:`> ...marketplace name `code-skills`...` → `> ...marketplace name `code-skills-marketplace`...`
- **调用顺序**:N/A(纯文档)
- **状态归属**:N/A
- **与概要设计的对应**:§6.3 README 中需要替换的字面量清单
- **符合的规范**:`doc-conventions.md §规则 1/2`

## 模块:plugins/code-skills/CLAUDE.md
- **路径**:`plugins/code-skills/CLAUDE.md`
- **关键行**:本次**不主动改**;仅当 Grep `code-skills@code-skills` 或 `marketplace name` 命中时才改
- **预期结果**:0 命中(由 REQU M-7 材料登记明示)
- **状态归属**:N/A
- **与概要设计的对应**:§4 模块清单 #4
- **符合的规范**:`doc-conventions.md §规则 2`(保持 README 实际状态一致)
