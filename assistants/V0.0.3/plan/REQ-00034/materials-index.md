# 材料登记 — REQ-00034

更新时间:2026-06-15 14:00
版本:V0.0.3
需求编码:REQ-00034

## 1. 项目级规范(本需求相关)

| 规范文件 | 类别 | 关键约束摘要 |
| --- | --- | --- |
| skill-conventions.md | 技能 | SKILL.md frontmatter L1-3 字节级保留(INV-1) |
| module-conventions.md | 模块(已弃用) | 资源放 templates/ / checklists/ / guidelines/(本需求**删除** `code-unit/templates/`) |
| doc-conventions.md | 文档 | README 中英版本结构对仗;主语言版本完整 |
| dashboard-conventions.md | 看板 | 字段扩展三方同步 |
| commit-conventions.md | 提交 | `chore(<skill>):` 前缀(INV-3) |
| encoding-conventions.md | 编码 | 需求编号 5 位纯数字;接收端可放宽 |
| marketplace-protocol.md | 插件 | plugin.json / marketplace.json 引用一致 |

## 2. 上游需求

- 来源:`./assistants/V0.0.3/require/REQ-00034/RESULT.md`
- 提取:12 FR / 12 NFR / 8 大类共 50+ AC

### 关键交叉点(每条 FR 对应设计章节)

| FR | 详细设计章节 |
| --- | --- |
| FR-1 `code-unit` 硬删除 | §3 模块详细化 / §6 接口细节 / §9 边界 E-4 |
| FR-2 `code-it` 步骤 8a 守卫 | §3.2 模块详细化 / §6.1 接口 / §11 测试要点 |
| FR-3 `code-it` 步骤 8.5 按需写单测 | §3.2 模块详细化 / §6.2 接口 / §11 测试要点 / §9 边界 E-3 |
| FR-4 `code-it` 模板新增"## 单元测试" | §3.2 模块详细化 / §6.3 接口 |
| FR-5 `code-plan` 测试状态字段改写 | §6.4 接口 |
| FR-6 `code-auto` 步骤 4.b 整段删除 | §6.5 接口 |
| FR-7 `code-check` test 引用收窄 | §6.6 接口 |
| FR-8 2 JSON 注册项删除 | §6.7 接口 |
| FR-9 4 README + CLAUDE.md 字面改写 | §6.8 接口 |
| FR-10 7 项目级规范字面改写 | §6.9 接口 |
| FR-11 11 技能描述段字面改写 | §6.10 接口 |
| FR-12 不修改其他 8 个 `code-*` 技能核心工作流 | §10 不变量 INV-4 |

## 3. 上游概要设计

- 来源:`./assistants/V0.0.3/design/REQ-00034/RESULT.md`
- 提取:15 决策 / 12 不变量 / 0 新增模块 / 1 新增接口类 / 0 数据结构 / 0 依赖
- 整体设计目标:`--extensible`(功能性 = 中)
- 候选 14 任务(由 `code-plan` 阶段细化,本轮合并为 10 任务)

## 4. 项目现状(实现细节)

- **类型**:Claude Code skills 仓库(元技能仓库,纯 Markdown)
- **语言**:Markdown(无工程代码)
- **编码风格**:沿用既有 markdown 列表项 / frontmatter YAML / 锚点小节
- **既有相似功能**:REQ-00031 / REQ-00026 / REQ-00030 等元技能改任务(纯 SKILL.md 字面改写)
- **既有可复用资产**:`code-unit` 步骤 0a 7 项守卫 + 步骤 7 屏幕输出模板 + 步骤 11 错误修复循环(字节级沿用至 `code-it` 步骤 8a / 8.5 / 12)

## 5. 规范 vs 设计冲突(0 冲突)

- 0 冲突(同 design 步骤 4 预检)

## 6. 命令行参数解析(本轮无参,沿用主流程)

- 无 `--result` / `--plan` 参数
- 沿用 `code-auto` 上下文(E-4 锁定)
