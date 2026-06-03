# 规范遵循记录 — REQ-00002
更新时间:2026-06-03 20:55
版本:V0.0.1

## 1. 本次参考的规范文件(5 个,全 Glob 命中)

| 规范文件 | 类别 | 关键约束摘要 | 本次如何遵循 |
| --- | --- | --- | --- |
| `dashboard-conventions.md` | 看板 | 看板字段约定、状态机 | §7 测试要点 / 看板字段保持原状 |
| `doc-conventions.md` §规则 1 | 文档 | README 多语言对仗 + 同次提交 | T-3 中英同次 commit |
| `doc-conventions.md` §规则 2 | 文档 | 仓库级使用说明文档存在并持续维护 | 模板占位符同步更新,无占位文本 |
| `marketplace-protocol.md` | marketplace | `marketplace.json` 与 `plugin.json` 引用一致性 | **零变更**(INV-3) |
| `skill-conventions.md` §规则 1 | 技能 | SKILL.md frontmatter 必含 `name`+`description` 且与目录名一致 | **frontmatter 零变更**(INV-2) |

## 2. 规范 vs 现状偏离

| # | 规范条款 | 项目现状 | 本次处理 |
| --- | --- | --- | --- |
| 1 | `doc-conventions.md §规则 2` "README 中命令/目录名/配置项必须与代码现状一致" | `README.md` + `README.en.md` 中示例编码仍用旧格式 `REQ-2026-0001` | 本需求**修复**(T-3) |
| 2 | `skill-conventions.md §规则 1` frontmatter 一致性 | 10 SKILL.md frontmatter 完好 | 本需求**不修改**(INV-2) |
| 3 | `marketplace-protocol.md` 引用一致性 | `marketplace.json` + `plugin.json` 已对齐 | 本需求**零变更**(INV-3) |

## 3. 规范 vs 需求冲突(无)

本需求**无规范 vs 需求冲突**。所有 FR / NFR 与既有规范兼容。

## 4. 用户授权的偏离(本设计授权 1 项)

### 偏离 D-1:`code-it` 创建新规范文件(范围扩展)
- **依据**:
  - 既有事实:`code-it` 不可修改 `./assistants/rules/`(本仓库"code-it 不可写 rules"既成事实)
  - 需求依据:本需求 FR-7 (Q-8=a) + FR-8 (Q-9=a) 要求创建 2 个新规范文件
  - 实际行为:由 `code-it` 创建(因本需求无 `code-rule` 调用的前置条件)
- **本设计授权**:
  - `code-it` **创建新文件** vs **修改既有文件** —— 是两种不同行为
  - 既有"不可修改"约束的是后者
  - 因此 `code-it` **创建** `encoding-conventions.md` + `migration-mapping.md` **不违反**既有约束
- **后续维护**:新文件由 `code-rule` 接管维护
- **记录位置**:`code/REQ-00002-00005/deviations.md` + `code/REQ-00002-00006/deviations.md`(各 1 条)
- **授权时间**:2026-06-03 20:55(本设计阶段)

## 5. 规范变更响应(无)

本设计阶段**无规范侧变更**(`code-rule` 未在本设计前/中调用)。

## 6. 本次设计新增的"硬性边界"

### 边界 B-1:5 个现有 `rules/` 文件零变更
- 依据:`code-it` 既有约束 + 本需求 FR 范围
- 含义:`dashboard-conventions.md` / `doc-conventions.md` / `marketplace-protocol.md` / `module-conventions.md` / `skill-conventions.md` 中如含旧编码示例,**不修改**
- 例外:仅在 `code-rule` 调用时同步

### 边界 B-2:`marketplace.json` + `plugin.json` 零变更
- 依据:本需求 FR-10
- 含义:任何与编码格式相关的修改**不触及** marketplace 协议文件

### 边界 B-3:V0.0.0 EXISTING-* 零变更
- 依据:基线完整性原则
- 含义:V0.0.0 已发布基线中的旧编码引用**不修改**

### 边界 B-4:本工作目录历史文件中的旧串保留
- 依据:本工作目录的 `require/REQ-00001/*` + `design/REQ-00001/*` + `plan/REQ-00001/*` + `code/REQ-00001-001~004/*` 中的旧串**保留**
- 理由:历史工作文件需要保留"旧串 → 新串"对照,作为版本演进记录

## 7. 自检表

| # | 规范条款 | 自检结果 |
| --- | --- | --- |
| 1 | doc-conventions §规则 1(中英对仗) | T-3 强制中英同次 commit ✅ |
| 2 | doc-conventions §规则 2(与代码现状一致) | T-3 同步新格式示例 ✅ |
| 3 | skill-conventions §规则 1(frontmatter 一致) | INV-2 零变更 ✅ |
| 4 | marketplace-protocol(marketplace 与 plugin 引用一致) | INV-3 零变更 ✅ |
| 5 | dashboard-conventions(看板字段) | T-8 看板同步保持原字段 ✅ |
| 6 | module-conventions(模块结构) | 本需求不涉及模块结构变更,N/A |
| 7 | (规划中)encoding-conventions | 由本需求 T-5 创建,Q-8=a 默认 ✅ |
| 8 | (规划中)migration-mapping | 由本需求 T-6 创建,Q-9=a 默认 ✅ |
