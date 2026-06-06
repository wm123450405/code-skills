# 接口详细规格 — REQ-00020
版本:V0.0.3

## 接口:`code-design` 步骤 0b CLI 参数(沿用)

- **形式**:函数 / SKILL.md 段
- **路径/签名**:`/code-design <REQ>`(无新增参数)
- **入参**:`<REQ>` 需求编码
- **出参**:`design/<REQ>/RESULT.md` + 7 份过程文档
- **错误码**:N/A(纯 SKILL.md)
- **示例**:沿用既有
- **版本策略**:沿用既有
- **兼容策略**:沿用既有
- **依据规范**:`skill-conventions §规则 1`

## 接口:`code-plan` 步骤 0b CLI 参数(沿用)

- **形式**:函数 / SKILL.md 段
- **路径/签名**:`/code-plan <REQ>`(无新增参数)
- **入参**:`<REQ>` 需求编码
- **出参**:`plan/<REQ>/RESULT.md` + `plan/<REQ>/PLAN.md` + 7 份过程文档
- **错误码**:N/A(纯 SKILL.md)
- **示例**:沿用既有
- **版本策略**:沿用既有
- **兼容策略**:沿用既有
- **依据规范**:`skill-conventions §规则 1`

## 接口:`code-it` CLI 参数(沿用)

- **形式**:函数 / SKILL.md 段
- **路径/签名**:`/code-it <TASK-...>`(无新增参数)
- **入参**:`<TASK-...>` 任务编码
- **出参**:`code/<TASK-...>/RESULT.md` + 4 份过程文档
- **错误码**:N/A(纯 SKILL.md)
- **示例**:沿用既有
- **版本策略**:沿用既有
- **兼容策略**:沿用既有
- **依据规范**:`skill-conventions §规则 1`

## 接口:`--result` / `--plan` 模板参数(预留,本需求不实现)

- **形式**:CLI 参数(预留)
- **路径/签名**:`/code-require <REQ> --result <模板>` / `/code-design <REQ> --result <模板>` / `/code-plan <REQ> --result <模板> --plan <模板>`
- **入参**:模板文件路径(.md / .html / .docx / .xlsx 等)
- **出参**:`REQUIRE.<ext>` / `DESGIN.<ext>` / `PLAN.<ext>`
- **错误码**:N/A(纯 SKILL.md)
- **版本策略**:由 REQ-00021 锁定
- **兼容策略**:由 REQ-00021 锁定
- **依据规范**:本需求 D-6 预留语义
- **状态**:**不**在本需求实现(留 REQ-00021)
