# 材料登记 — BUG-00004

更新时间:2026-06-22 20:30
版本:V0.0.3

## 项目级规范

| 规范文件 | 类别 | 关键约束摘要 |
| --- | --- | --- |
| `./assistants/rules/skill-conventions.md` | SKILL.md 编写 | 规则 1:frontmatter L1-3 字节级保留(`name` + `description`);规则 2:SKILL.md / templates/ 不含 6 类开发痕迹 |
| `./assistants/rules/dashboard-conventions.md` | 看板/模板/CLAUDE.md 扩展 | 规则 1:看板字段扩展需 templates/version-RESULT.md + CLAUDE.md + 本规范三方同步(本需求**不**触发) |
| `./assistants/rules/doc-conventions.md` | 文档编写 | 规则 1:README 多语言对仗(本需求**不**触发) |
| `./assistants/rules/module-conventions.md` | 技能资源 | 规则 1:资源放 templates/ / checklists/ / guidelines/ 子目录(本需求**不**触发) |
| `./assistants/rules/encoding-conventions.md` | 编号格式 | 规则 1/3:BUG-NNNNN 接收端放宽为 `^BUG-[A-Za-z0-9.\-_]+$` |
| `./assistants/rules/naming-conventions.md` | 命名 | 规则 1:kebab-case(本需求**不**新增文件,沿用既有) |
| `./assistants/rules/dependency-conventions.md` | 依赖 | 规则 1:沿用既有 tokei/cloc(本需求**不**新增依赖) |
| `./assistants/rules/coding-style.md` | 代码风格 | (本需求改 SKILL.md,**不**改代码) |
| `./assistants/rules/commit-conventions.md` | 提交 | 沿用既有 chore(code-...):<ID> <title> 格式 |
| `./assistants/rules/directory-conventions.md` | 目录 | 规则 1:本仓库按 marketplace 协议布局(本需求**不**触发) |
| `./assistants/rules/framework-conventions.md` | 框架 | (本需求**不**改框架代码) |
| `./assistants/rules/marketplace-protocol.md` | marketplace 协议 | (本需求**不**触发) |
| `./assistants/rules/migration-mapping.md` | 迁移映射 | (本需求**不**触发) |

## 上游需求
- 来源:N/A(缺陷分支无上游 require)
- 提取的 FR / NFR / AC 数量:N/A

## 上游概要设计
- 来源:N/A(缺陷分支无上游 design)
- 提取的模块拆分 / 接口概要 / 数据结构 / 决策:N/A

## 上游缺陷详情
- 来源:./assistants/V0.0.3/fix/BUG-00004/RESULT.md (v1)
- 提取的关键交叉点:
 - §根因分析:`code-it/SKILL.md` "## 过程文档自适应判定" 章节(line 101-138)定义的判定准则未真正接入"## 工作流程"(line 438+)
 - §修复方案:在步骤 8 末尾(步骤 8.6 之后)新增 `### 步骤 8.7 过程文档自适应判定执行` + 步骤 9/10/11 加守卫 + 步骤 13/16 模板改造
 - §其他技能排查结论:6 个技能虽然结构相同问题,但实际不触发(因判定表几乎都是"始终生成")

## 项目现状(实现细节)
- **命名风格**:本仓库**无**源代码,全部是 Markdown 技能定义 + 模板
- **错误模型**:N/A
- **并发原语**:N/A
- **既有相似功能的实现风格**:
 - `code-it/SKILL.md` "## 过程文档自适应判定" 章节(101-138)是**判定准则**定义(其他 6 个技能同构)
 - `code-require/SKILL.md` / `code-design/SKILL.md` / `code-check/SKILL.md` / `code-plan/SKILL.md` 工作流同样**未**在步骤 0 之前显式执行判定,但因它们的判定表几乎都是"始终生成",实际不触发过度生成
- **既有测试用例的风格与覆盖度**:N/A(本仓库无单元测试)
- **可复用的工具函数/中间件**:
 - `code-it/templates/process-doc-decisions.md` —— 决策记录文件模板(已存在,**字节级保留**)
 - `code-it/templates/RESULT.md` —— 任务总结模板(需在 T-002 改造)
 - `plugins/code-skills/skills/code-it/lib/logic-loc.md` + `logic-loc-defaults.md` —— 逻辑行统计共享库(本需求**不**修改)

## 本次变更源(增量更新时)
| 变更源 | 检测方式 | 变化列表 |
| --- | --- | --- |
| 缺陷侧 | `fix/BUG-00004/RESULT.md` 变更记录 | 1 条:2026-06-22 20:15 缺陷登记 + 1 条:2026-06-22 20:15 状态推进 |
| 代码侧 | 既有 `code-it/SKILL.md` 步骤 9/10/11 | 本需求**不**复用既有代码,新增"步骤 8.7" + 改造步骤 9/10/11 守卫 |
| 规范侧 | `./assistants/rules/` 对比 | 无变化(本需求**不**改规范) |
| 概要设计侧 | N/A(缺陷分支无上游 design) | — |
| 需求侧 | N/A(缺陷分支无上游 require) | — |
