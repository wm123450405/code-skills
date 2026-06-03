# 接口详细规格 — REQ-00001(code-plan 阶段)
更新时间:2026-06-03 20:30
版本:V0.0.1

## 接口:marketplace 根 name 字段
- **形式**:JSON Schema 字段(Claude Code marketplace 协议)
- **路径**:`$.name` in `.claude-plugin/marketplace.json`
- **改前值**:`"code-skills"`
- **改后值**:`"code-skills-marketplace"`
- **错误码**:N/A(配置层,无错误码概念)
- **示例**:
  - 改前:
    ```json
    {
      "$schema": "https://anthropic.com/claude-code/marketplace.schema.json",
      "name": "code-skills",
      ...
    }
    ```
  - 改后:
    ```json
    {
      "$schema": "https://anthropic.com/claude-code/marketplace.schema.json",
      "name": "code-skills-marketplace",
      ...
    }
    ```
- **版本策略**:`marketplace.json` 根 `version` 保持 `1.0.0`(Q-5 默认 A,详见 `clarifications.md`)
- **兼容策略**:`plugins[].name` 保持 `code-skills`(不触发兼容性问题,因 plugin 标识独立)
- **依据规范**:`marketplace-protocol.md §规则 1.2`(`name` 改后仍 kebab-case ✅)

## 接口:install 命令(用户外部接口)
- **形式**:Shell 命令
- **改前**:`claude plugin install code-skills@code-skills`
- **改后**:`claude plugin install code-skills@code-skills-marketplace`
- **错误码**:N/A(用户层命令,无错误码概念)
- **示例**:见 README §"安装"
- **版本策略**:N/A(命令字符串,无版本)
- **兼容策略**:
  - 老用户已 marketplace add 旧 name → 需先 `marketplace remove code-skills` + `marketplace add <git-url>` + `plugin install code-skills@code-skills-marketplace`
  - NFR-1 兼容性已在 REQU 文档 §7 交互逻辑 详述
- **依据规范**:`doc-conventions.md §规则 2`(命令必须反映实际状态)
