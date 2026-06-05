# 材料登记 — REQ-00011

更新时间:2026-06-05
版本:V0.0.2

## 项目级规范

| 规范文件 | 类别 | 关键约束摘要 | 本计划对应章节 |
| --- | --- | --- | --- |
| skill-conventions.md | 技能编写 | SKILL.md 必含 name + description,frontmatter 不变;name 与目录名一致 | INV-1, T-001 / T-002 验证手段 |
| module-conventions.md(已 DEPRECATED) | 模块规划(已弃用) | 资源放技能子目录 `templates/` / `checklists/` / `guidelines/` | T-001 / T-002 涉及文件(均在 `templates/`) |
| directory-conventions.md | 目录与模块 | 替代 module-conventions.md | (沿用) |
| dashboard-conventions.md | 看板与模板 | 看板字段约定扩展需 3 处同步(本需求**不**触发) | INV-8, T-001 / T-002 备注 |
| encoding-conventions.md | 编码格式 | 3 类编码权威源(本需求**不**产生新编码) | (不涉及) |
| commit-conventions.md | 提交与合并 | (规则 1 待添加);沿用 V0.0.1 实践 `chore(<scope>): <subject>` | T-001 / T-002 完成时(由 code-it 实施) |
| doc-conventions.md | 文档编写 | README 多语言对仗 + 完整性(本需求**不**改 README) | (不涉及) |
| marketplace-protocol.md | Marketplace 协议 | $schema / name / version 必填(本需求**不**改) | (不涉及) |
| coding-style.md / framework-conventions.md / dependency-conventions.md / naming-conventions.md | 各类 | (规则 1 待添加) | (NFR-1 零新增依赖) |

## 上游需求

- 来源:./assistants/V0.0.2/require/REQ-00011/RESULT.md
- 版本:v1(2026-06-04 14:57)
- 提取的 FR / NFR / AC 数量:9 FR / 8 NFR / ~30 AC
- 关键交叉点(每条 FR 对应的本计划章节):
  - FR-1 → T-001 关键变更 §步骤 0b
  - FR-2 → T-002 关键变更 §步骤 0b(沿用)
  - FR-3 → T-002 关键变更 §步骤 0b(退化)
  - FR-4 → T-002 关键变更 §步骤 10A 末尾"按设计目标调整任务粒度"段
  - FR-5 → T-001 / T-002 关键变更(回写"## 设计目标"小节)
  - FR-6 → T-001 关键变更 §步骤 0b(1-5 问自适应)
  - FR-7 → 全部 2 任务涉及文件(0 修改其他 8 技能)
  - FR-8 → 全部 2 任务备注(0 改 marketplace / plugin / 规范)
  - FR-9 → T-001 / T-002 关键变更 §屏显模板

## 上游概要设计

- 来源:./assistants/V0.0.2/design/REQ-00011/RESULT.md
- 版本:v1(2026-06-05)
- 提取的模块拆分 / 接口概要 / 数据结构 / 决策:
  - 模块拆分:code-design SKILL + code-design 模板 + code-plan SKILL + code-plan 模板(4 文件改动)
  - 接口概要:`askDesignGoals` / `writeDesignGoalsSection` / `readDesignGoalsFromDesign` / `adjustTaskGranularityByGoals`(4 算法)
  - 数据结构:DesignGoals(内存)+ "## 设计目标"小节 Markdown 模板
  - 8 决策(D-1 ~ D-8)+ 8 不变量(INV-1 ~ INV-8)
- 本计划对概要设计的 100% 沿用 + 1 处扩展(§模块 4 步骤 0a L107 / L118 小注更新)

## 项目现状(实现细节)

### 命名风格
- SKILL.md frontmatter:`name: code-design` / `name: code-plan`(kebab-case)
- 文档头:Markdown 标题 + 元信息
- 章节命名:中文,统一格式

### 错误模型
- 本技能不涉及运行时错误(纯 Markdown 技能)
- 写文件失败 → 透传 stderr

### 并发原语
- **无**(单技能串行)

### 既有相似功能的实现风格
- REQ-00005(3 技能首步拉取与末步提交)落地模式:增量追加"步骤 0a" + 末尾兜底
- REQ-00009(`code-unit` 步骤 0a 守卫)落地模式:增量追加"步骤 0a" + 锚点字符串精度
- REQ-00010(`code-it` 步骤 0a 守卫)落地模式:同 REQ-00009
- REQ-00016(快模式)落地模式:增量追加"步骤 0.5" + "步骤 N 步骤 3.5"
- **本需求沿用同模式**:增量追加"步骤 0b" + 锚点字符串精度

### 既有测试用例的风格与覆盖度
- **无**(本项目无构建/测试框架,纯 Markdown 技能)
- `code-unit` 守卫"项目根 7 项"判定本项目为"不可测"(沿用 REQ-00009 实践)
- 故 2 任务测试状态均 = `不适用`

### 可复用的工具函数/中间件
- `AskUserQuestion`(Claude Code 既有工具)
- `Read` / `Write` / `Edit` / `Bash` / `Glob` / `Grep`(Claude Code 既有工具)
- 既有"步骤 0a 拉取"(REQ-00005 落地)— `Bash: git pull` + 错误处理分类

## 本次变更源(增量更新时)

| 变更源 | 检测方式 | 变化列表 |
| --- | --- | --- |
| 需求侧 | 上游 RESULT.md 变更记录 | 0(本计划 v1 沿用上游 v1) |
| 概要设计 | 上游 RESULT.md 变更记录 | 0(本计划 v1 沿用概要设计 v1) |
| 规范侧 | ./assistants/rules/ 对比 | 0(本计划不触发任何规范变更) |
| 代码侧 | 重跑项目探索 | 0(本计划不修改业务代码,仅 SKILL.md + 模板) |
