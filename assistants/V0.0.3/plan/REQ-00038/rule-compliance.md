# 规范遵循自检 — REQ-00038

版本:V0.0.3

> 本文档对 13 份项目级规范逐条自检,确认本需求是否完全合规,识别任何用户授权的偏离或待澄清冲突。

## 自检结论总览

- **完全合规**:13 份规范全部合规(仅消费,不修改)
- **用户授权的偏离**:0 项
- **待澄清的冲突**:0 项

## 逐份自检

### 1. `module-conventions.md` §规则 1(资源放 `templates/` / `checklists/` / `guidelines/` 子目录)

- **自检**:`code-it/templates/RESULT.md` 在 `code-it/templates/` 子目录,位置合规;`code-it/SKILL.md` / `code-plan/SKILL.md` 改动均在技能根目录的 SKILL.md 内(无新文件)
- **结论**:✅ 完全合规
- **依据**:本需求仅追加 1 个模板小节(在既有 `RESULT.md` 内),不新增模板文件;既有模板位置合规

### 2. `encoding-conventions.md` §规则 1(REQ/BUG/TASK 三类编码)

- **自检**:本需求不涉及编码产出(纯 Markdown 改造)
- **结论**:✅ 完全合规(N/A)

### 3. `encoding-conventions.md` §规则 2(5 位纯数字)

- **自检**:本需求不涉及编码产出
- **结论**:✅ 完全合规(N/A)

### 4. `encoding-conventions.md` §规则 3(嵌套式 TASK 编码)

- **自检**:本需求不涉及编码产出
- **结论**:✅ 完全合规(N/A)

### 5. `skill-conventions.md` §规则 1(SKILL.md frontmatter 含 name + description)

- **自检**:`code-it/SKILL.md` / `code-plan/SKILL.md` frontmatter 字节级保留(L1-3 字节级,INV-1 锁定)
- **结论**:✅ 完全合规
- **依据**:INV-1 锁定

### 6. `skill-conventions.md` §规则 2(SKILL.md 与 templates/ 不包含开发痕迹)

- **自检**:
 - 既有 `code-it/SKILL.md` "## 步骤 8a.0 — 模块识别"小节**新增** —— 不含本需求 REQ 编号 / BUG 编号 / 决策记录 / 生效日标记
 - `code-plan/SKILL.md` L473 / L496 字面改写 —— 不引入开发痕迹(只追加"步骤 8a.0 模块识别"字面)
 - `code-it/templates/RESULT.md` "## 各模块单测结果"小节**新增** —— 不含开发痕迹
- **结论**:✅ 完全合规
- **依据**:INV-2 锁定

### 7. `dashboard-conventions.md` §规则 1(看板字段约定扩展需多文件同步)

- **自检**:本需求不新增"区段/表格列/枚举值",仅追加 1 个模板小节(7 字段全部在 `unit-test-results.md` 模板内,不进看板)
- **结论**:✅ 完全合规(0 触发)
- **依据**:本需求**不**涉及 `RESULT.md` 看板字段约定扩展,0 触发三同步

### 8. `doc-conventions.md` §规则 1(README 多语言对仗)

- **自检**:本需求不修改 README
- **结论**:✅ 完全合规(N/A)

### 9. `coding-style.md`(命名/错误处理/安全/性能)

- **自检**:本需求为 Markdown 文档改造,不涉及代码命名/错误处理
- **结论**:✅ 完全合规(N/A)

### 10. `commit-conventions.md`(提交信息格式)

- **自检**:末尾兜底 commit 沿用既有 `chore(code-it): ...` 格式
- **结论**:✅ 完全合规(N/A)

### 11. `dependency-conventions.md` §规则 N(不引入未经评审的新依赖)

- **自检**:本需求 0 新增三方依赖(8 套声明文件解析手写,无 npm 库)
- **结论**:✅ 完全合规
- **依据**:INV-8 锁定

### 12. `directory-conventions.md` §规则 1(技能目录结构)

- **自检**:既有 `code-it/` / `code-plan/` 目录结构 0 改
- **结论**:✅ 完全合规

### 13. `framework-conventions.md` / `naming-conventions.md` / `migration-mapping.md` / `marketplace-protocol.md`

- **自检**:本需求不涉及
- **结论**:✅ 完全合规(N/A)

## 关键不变量(沿用概要设计 INV-1 ~ INV-8)

| INV | 约束 | 自检结论 |
| --- | --- | --- |
| INV-1 | frontmatter L1-3 字节级保留(`code-it` / `code-plan`) | ✅ 字面校验通过 |
| INV-2 | "## 不要做的事" 既有小节 0 改 | ✅ 字面校验通过 |
| INV-3 | "## 工作流程" 既有步骤字节级保留 | ✅ 字面校验通过(7 项守卫 / 3 类任务自动判定 0 改) |
| INV-4 | `code-it/templates/RESULT.md` "## 9. 单元测试(由 code-it 内化,新增,"小节 0 改(L138-153 字节级保留) | ✅ 字面校验通过 |
| INV-5 | 11 个其他 `code-*` 技能 SKILL.md 核心工作流 0 改 | ✅ 字面校验通过(仅 `code-check` 适配判定文件位置,无 SKILL.md 改动) |
| INV-6 | 12 个项目级规范 0 改核心约束 | ✅ 字面校验通过 |
| INV-7 | 既有 15 个 REQ 的 `code/<TASK-...>/RESULT.md` + `plan/<需求>/PLAN.md` 0 改 | ✅ 字面校验通过(本需求只追加新文件,0 修改既有) |
| INV-8 | 0 新增三方依赖(NFR-3 锁定) | ✅ 静态校验通过(8 套声明文件解析手写) |

## 待澄清冲突

无。

## 用户授权偏离

无。
