# 材料登记 — REQ-00004

更新时间:2026-06-04 16:10
版本:V0.0.2

## 项目级规范
扫描源:`./assistants/rules/**/*`(13 个文件,2026-06-04 16:10)
> 已在 `design/REQ-00004/materials-index.md` 详列;本节只列**详细设计阶段**重点引用的条款。

| 规范文件 | 类别 | 本阶段重点引用条款 | 落点 |
| --- | --- | --- | --- |
| `skill-conventions.md` | 技能元信息 | §规则 1:YAML frontmatter 必含 name + description,name 与目录名一致 | `module-details.md` §M-1 / `interface-specs.md` §I-1 |
| `module-conventions.md` | 模块规划(DEPRECATED) | §规则 1:资源放 templates/ / checklists/ / guidelines/ 子目录 | `rule-compliance.md §4 A-1`(本技能无资源,授权偏离) |
| `directory-conventions.md` | 目录(替代) | §规则 1 占位 | 沿用既有惯例,等正式生效再校准 |
| `dashboard-conventions.md` | 看板 | §规则 1:看板字段约定扩展需 3 文件同步 | **不触发**(NFR-1/7,纯只读) |
| `encoding-conventions.md` | 编码格式 | §规则 1/3/4:`REQ-NNNNN` / `TASK-(REQ\|BUG)-NNNNN-NNNNN`,5 位纯数字;§规则 4:解析入口必须用嵌套式正则 | `module-details.md` §M-1 函数 `parseTaskId` / `risk-analysis.md §8 异常 E-9` |
| `commit-conventions.md` | 提交 | §规则 1 占位 | `code-it` 阶段遵循,V0.0.1 既有 commit 走 conventional 风格 |
| `coding-style.md` | 代码风格 | §规则 1 占位 | `SKILL.md` 是 Markdown,无编程语言约束 |
| `naming-conventions.md` | 命名 | §规则 1 占位 | kebab-case(沿用既有惯例) |
| `framework-conventions.md` | 框架 | §规则 1 占位 | 不适用 |
| `dependency-conventions.md` | 三方依赖 | §规则 1 占位;NFR-1 锁零依赖 | `dependencies.md`(本设计阶段沿用 design 结论) |
| `doc-conventions.md` | 文档 | §规则 1/2:README 中英同次提交 + 核心小节必覆盖 | `module-breakdown §3.4` 可选 T-002/T-003 触发条件 |
| `marketplace-protocol.md` | 协议 | §规则 1:不动 marketplace.json / plugin.json | `module-details §M-1` / `risk-analysis §8` NFR-6 边界 |
| `migration-mapping.md` | 迁移 | §规则 1/4:已落地映射 + EXISTING-NNN 不追溯 | NFR-3 双格式兼容(透传旧字面) |

## 上游需求
- 来源:`./assistants/V0.0.2/require/REQ-00004/RESULT.md`
- 版本:v1(已锁定,2026-06-04 12:50)
- 提取:10 FR / 7 NFR / 30 AC / 3 项已锁定 Q-1~Q-3 / 2 项采纳默认 Q-4~Q-5 / 2 项未采用 Q-7~Q-8
- **关键交叉点(每条 FR 对应的设计章节)**:

| FR | 概要设计章节 | 详细设计落点 |
| --- | --- | --- |
| FR-1(SKILL.md frontmatter) | §3 模块拆分 / §11.1 规范遵循 | `module-details §M-1` / `interface-specs §I-1` |
| FR-2(总览模式 4 段) | §6.1 总览 / §7.1 状态机 / §7.2 建议生成 | `module-details §M-1` 步骤 3~5 / `algorithm-1` |
| FR-3(需求模式 5 段) | §6.5 需求粒度 | `algorithm-2` 需求模式 |
| FR-4(下一步建议) | §6.4 / §7.2 | `algorithm-3` 建议生成 / `data-changes §D-1 Suggestion` |
| FR-5(无激活版本引导) | §8 边界 E-1 | `risk-analysis §8` 异常 E-1 |
| FR-6(参数校验) | §7.1 启动流程 / §8 E-3/E-4 | `algorithm-0` 参数解析 / 异常 E-3/E-4 |
| FR-7(纯只读) | §3.3 修改 0 个 / NFR-6/7 | `module-details §M-1` 工具集 / `risk-analysis §8` NFR-6 边界 |

| NFR | 概要设计章节 | 详细设计落点 |
| --- | --- | --- |
| NFR-1 零外部依赖 | §9 三方依赖 | `dependencies.md` |
| NFR-2 不崩溃 | §8 边界 E-1~E-10 | `risk-analysis §8 异常处理` / `algorithm-1` L2 退化 |
| NFR-3 双格式兼容 | §4.4 任务编号 / §8 E-9 | `algorithm-4` parseTaskId |
| NFR-4 性能 < 5 秒 | §7.3 性能预期 | `risk-analysis §10 性能与资源` |
| NFR-5 看板字段不扩展 | — | `rule-compliance §6` 自检 11 条 |
| NFR-6 不改其他技能 | §3.3 / §11.1 | `module-details §M-1` 工具集 |
| NFR-7 幂等 | FR-7 + 工具集 | `module-details §M-1` 工具集 |

## 上游概要设计
- 来源:`./assistants/V0.0.2/design/REQ-00004/RESULT.md`
- 版本:v1(已完成,2026-06-04 15:50)
- 提取:8 个关键设计问题(Q-1~Q-8)+ 模块拆分 + 接口与数据结构 + 状态机 + 边界 + 性能
- **关键交叉点(详细设计细化)**:

| 概要设计章节 | 详细设计细化 |
| --- | --- |
| §3 模块拆分 M-1(单文件) | `module-details.md §M-1` 关键类/函数 + 调用顺序 |
| §4.2 文件契约(只读) | `interface-specs.md §I-1` CLI 入口 + §I-2 文件契约 |
| §4.4 任务编号数据结构 | `data-changes.md §D-2 TaskId` + `algorithm-4` parseTaskId |
| §4.5 建议数据结构 | `data-changes.md §D-1 Suggestion` + `algorithm-3` generateSuggestions |
| §7.2 建议生成算法 | `algorithm-3` 5 类优先级 + 最多 5 条 |
| §7.1 状态机 | `state-machine` Mermaid 图 |
| §8 边界 E-1~E-10 | `risk-analysis §8` 10 项边界详细处理 |

## 项目现状(实现细节)

### SKILL.md 骨架(以 `code-design/SKILL.md` 为参照)
- **frontmatter 必含字段**:`name` + `description`(`skill-conventions §规则 1`)
- **章节顺序(本设计严格遵循)**:
  1. 标题 `# code-dashboard — 名称(版本感知)`
  2. 目标
  3. 适用场景
  4. 不适用
  5. 工作目录约定(强制)
  6. 输入
  7. 输出
  8. 工具使用约定
  9. 工作流步骤(步骤 0 ~ N,本技能为 0~6)
  10. 边界与异常
  11. 衔接
  12. 不要做的事

### 既有 10 个 SKILL.md 关键风格
- frontmatter `description` 一句话讲清"做什么、何时用"(最长 ~250 字符)
- 步骤编号统一为"步骤 0 / 步骤 1 / 步骤 2 ..."
- 每个步骤有明确的"输入/输出/动作"
- 边界与异常用 `## 边界与异常` 区段 + 表格

### 既有 10 个 SKILL.md 行数
- `code-init`:未读(留作 code-it 阶段参考)
- `code-version`:10,187 bytes / ~250 行
- `code-rule`:未读
- `code-require`:未读
- `code-design`:19,665 bytes / ~530 行
- `code-plan`:未读
- `code-it`:未读
- `code-unit`:未读
- `code-fix`:未读
- `code-review`:20,806 bytes / ~520 行

> **预估**:`code-dashboard/SKILL.md` 在 ~350 ~ 450 行(单文件技能,无子目录资源)

### 命名约定(沿用既有惯例)
- 技能目录名:`code-dashboard`(kebab-case,与既有 10 个一致)
- 函数命名(伪代码):`parseTaskId()` / `parseDashboard()` / `generateSuggestions()` / `bar()`(camelCase)
- 常量:`BAR_WIDTH = 12` / `TASK_PATTERN_NEW` / `TASK_PATTERN_OLD`(UPPER_SNAKE_CASE)

### 错误处理风格(沿用既有惯例)
- 错误信息用 `✗` 前缀(参考 `code-version` 等 SKILL.md 既有风格)
- 引导信息用 `>` 前缀
- 状态字面用中文(`待开始` / `已完成` / `已运行-通过`)
- 严重度字面:`P0` / `P1` / `P2` / `P3`

### 既有可复用范式
- `code-version/templates/assistants-layout.md`:本技能不直接复用(无独立模板资源)
- `code-version/templates/version-RESULT.md`:本技能**只读**该模板(看板字段约定的源头)
- `code-review/SKILL.md`:状态机范式参照(读区段 → 解析 → 聚合 → 渲染 → 输出)

### 既有工具函数(无;本技能是新写)
- 本技能**不**复用既有任何工具函数(无共享 utility)
- 字符操作 / 正则匹配 / 行号定位均为内置 JavaScript 能力

## 关联编码计划(本版本)
- `./assistants/V0.0.2/plan/`:本目录当前为空(本技能为 V0.0.2 首个 `code-plan` 调用)
- 跨版本:`./assistants/V0.0.1/plan/REQ-0000{1,2,3}/PLAN.md`(均为"修改 10 SKILL.md"等大改动,与本技能"新增 1 SKILL.md"模式不同;无直接任务依赖,但状态字段定义、状态推进规则一致)

## 本次变更源
- **需求侧**:**无变化**(上游 v1 已锁定)
- **概要设计侧**:**无变化**(上游 v1 已完成)
- **规范侧**:**无变化**(本次扫描 `./assistants/rules/` 与 `design` 阶段无差异)
- **代码侧**:**无变化**(本技能为新增,不涉及既有代码)
