# 材料登记 — REQ-00032

更新时间:2026-06-12 16:36
版本:V0.0.3

## 1. 项目级规范

> 本次参考 `./assistants/rules/` 下 7 个核心规范文件

| 规范文件 | 类别 | 关键约束摘要 | 与本详设关联 |
| --- | --- | --- | --- |
| skill-conventions.md | 技能 | frontmatter L1-3 字节级保留 | INV-1 |
| commit-conventions.md | 提交 | `chore(<skill>):` 前缀 | INV-3 |
| module-conventions.md | 模块 | 资源放 templates/ | 沿用 |
| dashboard-conventions.md | 看板 | 字段三方同步 | 沿用 |
| encoding-conventions.md | 编码 | 5 位纯数字生成端 | 沿用(任务编号 TASK-REQ-00032-00001) |
| naming-conventions.md | 命名 | kebab-case 目录 | 沿用 |
| doc-conventions.md | 文档 | README 中英版对仗 | 不直接相关 |

## 2. 上游需求

- 来源:`./assistants/V0.0.3/require/REQ-00032/RESULT.md`
- 版本:V0.0.3(2026-06-12 16:10)
- 提取:4 FR / 9 NFR / 18 AC
- 关键交叉点(每条 FR 对应的设计章节):

| FR | 对应概设章节 | 对应详设章节 |
| --- | --- | --- |
| FR-1(AI 自主判定) | design §6.1 算法 | plan §4.1 + module-details §算法 1 |
| FR-2(不修改 RESULT.md) | design §3.3 不修改 | plan §5(0 数据结构变更) + plan §12.2 INV-7 |
| FR-3(屏幕日志输出) | design §4.2 格式契约 | plan §6.2 + interface-specs §接口 1/2 |
| FR-4(不修改其他 8 个 SKILL.md) | design §3.3 | plan §12.2 INV-4 |

## 3. 上游概要设计

- 来源:`./assistants/V0.0.3/design/REQ-00032/RESULT.md`
- 版本:V0.0.3(2026-06-12 16:32)
- 提取:8 决策 / 0 接口 / 0 数据结构 / 10 INV
- 关键交叉点(每条决策对应的详设章节):

| 设计决策 | 对应详设章节 |
| --- | --- |
| D-1 改造 `code-require/SKILL.md` | plan §3(模块 1+2) |
| D-2 步骤 10A / 10B 段内文末追加 | plan §3.1 + §3.2 |
| D-3 isTiny 判定位置 | plan §4.1 + module-details §算法 1 |
| D-4 屏幕日志编号 | plan §6.2 |
| D-5 isTiny 不持久化 | plan §6.3 |
| D-6 建议仅 2 条 | plan §6.2 |
| D-7 不联动 /code-unit | plan §12 INV-10 |
| D-8 `--minimal` + 功能性=中 | plan 顶部"## 设计目标" |

## 4. 项目现状(实现细节)

### 4.1 目标语言规范

- 仓库类型:Claude Code 插件市场(marketplace)
- 主要语言:**Markdown**(纯文档,无编程语言)
- 编码风格:沿用既有 `code-require/SKILL.md` 风格(标题层级、表格对齐)

### 4.2 既有相似功能实现风格

- 既有元技能改参考:`code-plan/SKILL.md` 步骤 7A(REQ-00030 FR-5 强化,2026-06-12 起生效)
- 既有元技能改参考:`code-plan/SKILL.md` 步骤 10A(REQ-00031 FR-1 新增,2026-06-12 起生效)
- 模式:**步骤末尾追加 1 段** + 段内行文包含「本需求 REQ-NNNNN FR-X 新增,YYYY-MM-DD 起生效」标注

### 4.3 既有测试用例

- **不适用**(本仓库无测试框架)
- 测试方法:**手工目检** + **git diff 校验**(沿用 REQ-00031 NFR-2)

### 4.4 可复用工具函数

- 不适用(本需求无编程语言代码)

## 5. 本次变更源(增量更新时填写)

不适用(本需求是首次详设)。

## 6. 命令行参数

无(`--result` / `--plan` 模板参数未传,沿用主产出物 RESULT.md + PLAN.md,无模板填充)
