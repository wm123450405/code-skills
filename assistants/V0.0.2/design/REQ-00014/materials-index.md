# 材料登记 — REQ-00014

更新时间:2026-06-05 12:30
版本:V0.0.2
需求:REQ-00014(优化技能 `/code-plan` 的任务拆分维度)

## 项目级规范

| 规范文件 | 类别 | 关键约束摘要 | 本需求相关 |
| --- | --- | --- | --- |
| `skill-conventions.md` | 技能编写 | §规则 1:SKILL.md frontmatter 必含 name+description | ✅ 强约束(本需求不改 frontmatter) |
| `module-conventions.md` | 模块规划(DEPRECATED 但沿用) | §规则 1:资源放固定子目录 templates/checklists/guidelines | ✅ 强约束(本需求不修改 `code-plan/` 目录结构) |
| `dashboard-conventions.md` | 看板与版本工作空间 | §规则 1:字段约定扩展需 3 处同步 | ✅ 强约束(本需求**不**改字段,只改 `code-plan` 技能,故**不**触发) |
| `doc-conventions.md` | 文档编写 | §规则 1:中英 README 同次 + 对仗;§规则 2:README 存在并维护 | ✅ 不触达 |
| `marketplace-protocol.md` | Marketplace 协议 | §规则 1:`$schema`/name/version 必填,`./` 路径,无未知字段 | ✅ 不触达 |
| `encoding-conventions.md` | 编码格式 | §规则 1-4:REQ/BUG 5 位;TASK 嵌套式 5+5 位;§规则 4 实施流程 | ✅ 强约束(任务编号格式不修改) |
| `migration-mapping.md` | 编码迁移 | §规则 1-4:EXISTING-NNN 不追溯 | ✅ 不触达 |
| 6 个占位规范(directory-conventions/coding-style/commit-conventions/dependency-conventions/framework-conventions/naming-conventions) | 各类 | 占位 | ❌ 不触达 |

**强约束全部满足(本需求不修改字段,只修改 `code-plan` 技能工作流)。**

## 上游需求

- **来源**:`./assistants/V0.0.2/require/REQ-00014/RESULT.md`(v1,已锁定)
- **提取的 FR / NFR / AC**:4 FR / 6 NFR / 13 AC
- **关键交叉点**:
  - FR-1(按"功能点"拆分)→ 详细化产出 §4 详细原则
  - FR-2(架构任务作为首个)→ 详细化产出 §5 架构任务触发条件
  - FR-3(仅未来需求生效)→ 详细化产出 §6 生效范围
  - FR-4(不破坏其他 12 个技能)→ 详细化产出 §7 影响范围(0 影响)

## 项目现状(本次扫描)

### 项目类型
- **类型**:Claude Code 插件市场(marketplace)仓库
- **代码语言**:Markdown(SKILL.md / README / RESULT.md / PLAN.md)+ JSON(`marketplace.json` / `plugin.json`)
- **构建/运行**:**N/A**(无构建过程,无运行时)
- **测试**:**N/A**(纯文档型)
- **关键依赖**:`@anthropic-ai/claude-code` SDK(由 Claude Code 自身提供,非三方)

### 目录结构(本需求涉及)
- `plugins/code-skills/skills/code-plan/SKILL.md`(L194-235 = `§10A 任务拆分`)— **本需求唯一修改点**
- 其他 18 个章节(L1-193 + L236-374)— **不修改**

### 已有模块(本次涉及)
- `plugins/code-skills/skills/code-plan/SKILL.md` — 入口技能文件
- `plugins/code-skills/skills/code-plan/templates/` — 2 个模板文件(`assistants-layout.md` + `design.md`)— **不修改**

### 已有接口(N/A)
- 本需求**不涉及** API 端点或方法签名
- 修改目标是 SKILL.md 的"工作流步骤"文字描述

### 已有数据模型(N/A)
- 本需求**不涉及**任何数据结构变更
- 任务编号格式(`TASK-(REQ|BUG)-NNNNN-NNNNN`)由 `encoding-conventions.md` 定义,**不修改**

### 已有第三方依赖
- **0 新增依赖**(NFR-1 强约束)

### 编码与构建约定
- 既有 `code-plan` SKILL.md 是纯 Markdown 文档
- 沿用同 V0.0.2 既有 8 个 `code-*` 技能的 SKILL.md 风格(章节式,无子目录)
- 修改产出 = 修改 `code-plan/SKILL.md` 中 §10A 的 5 行文字

### 关键参考:code-plan SKILL.md 现状
- **总行数**:374 行
- **§10A 位置**:L194-235(42 行)
- **§10A 当前内容**:
  - L195-199:原 4 行"任务拆分原则"(最小/单一/可独立/顺序友好)
  - L201-213:任务类型 + 任务编号(沿用)
  - L215-228:任务双状态字段(沿用)
  - L230-239:任务触发/来源字段(沿用)
- **修改范围**:**仅** L195-199 的 4 行原则(其他 38 行全部沿用)
- **修改目标**:**完全替换**原 4 行原则为新原则(Q-D1 用户锁定)

## 项目现状:既有 7 个已拆分 PLAN

| 需求 | PLAN 任务数 | 拆分模式 | 是否追溯 |
| --- | --- | --- | --- |
| REQ-00004 dashboard | 3 | 分层(算法 + 指令 + README) | ❌ 不追溯(Q-A3 锁定) |
| REQ-00005 首步拉取 | 5 | 分层(3 SKILL.md 增量 + 1 看板 + 1 派生) | ❌ 不追溯 |
| REQ-00006 publish | 9 + 1 派生 | 分层(1 SKILL.md + 5 模板 + 1 自检 + 1 看板 + 1 README) | ❌ 不追溯 |
| REQ-00007 auto | 5 | 偶然功能点化(完整 SKILL.md / JSON / README / 看板 / 自检) | ❌ 不追溯(已实施完成) |
| 未来需求(REQ-00008+) | TBD | **新规则生效**(按功能点) | — |

## 预检规范 vs 需求冲突

**0 冲突**。本需求**不修改**任何字段定义,只修改 `code-plan` 技能的工作流文字描述:
- 不修改任务编号格式(`encoding-conventions` 沿用)
- 不修改任务双状态字段(沿用)
- 不修改触发/来源枚举(沿用)
- 不修改看板字段定义(`dashboard-conventions` 沿用)
- 不修改 `code-design` / `code-it` / `code-unit` / `code-review` 等其他 12 个技能 SKILL.md

**触发三同步**:**否**(本需求**不修改看板字段**,只改"工作流定义";`code-plan` 技能的 SKILL.md 修改**不**在 `dashboard-conventions §规则 1` 的"看板字段扩展"范围)

## 关键观察

1. **本次是元需求**(meta-requirement):优化一个 `code-*` 技能的工作流定义本身
2. **修改面 = 1 个 SKILL.md 的 1 个章节(§10A)的 5 行文字**
3. **生效面 = V0.0.2 未来所有需求的 `code-plan` 任务拆分**
4. **影响面 = 0** (其他 12 个 `code-*` 技能 / 既有 7 个 PLAN / 看板 / 规范文件 全部不受影响)
