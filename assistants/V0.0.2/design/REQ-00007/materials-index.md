# 材料登记 — REQ-00007(增加 `/code-auto` 自动开发技能)

更新时间:2026-06-05 09:05
版本:V0.0.2

## 项目级规范(本次扫描)

| 规范文件 | 类别 | 关键约束摘要 |
| --- | --- | --- |
| `skill-conventions.md` | 技能编写 | §规则 1:SKILL.md frontmatter 必含 `name` + `description`,`name` 与目录名 kebab-case 严格一致 |
| `dashboard-conventions.md` | 看板与版本工作空间 | §规则 1:看板字段约定扩展需 `templates/version-RESULT.md` + `CLAUDE.md` + 本规范三同步(本设计**不**扩展字段) |
| `doc-conventions.md` | 文档编写 | §规则 1:README 中英同次提交 + 结构对仗;§规则 2:README 必须存在并持续维护 |
| `encoding-conventions.md` | 编码格式 | §规则 1-4:REQ/BUG `^REQ-\d{5}$` / `^BUG-\d{5}$`;TASK 嵌套式 `^TASK-(REQ\|BUG)-\d{5}-\d{5}$`;§规则 4 实施流程 |
| `marketplace-protocol.md` | Marketplace 协议 | §规则 1:`$schema` / `name` / `version` 必填;`source` 必须 `./` 开头;`skills` 必须是 `./` 开头的相对路径数组;**不**允许未知字段 |
| `migration-mapping.md` | 编码迁移 | §规则 1-4:已落地的旧→新映射;V0.0.0 `EXISTING-NNN` 不追溯重命名 |
| `module-conventions.md` | 模块规划 | ⚠️ DEPRECATED(已迁移到 `directory-conventions.md`);§规则 1 仍引用:`templates/` / `checklists/` / `guidelines/` 固定子目录 |
| `directory-conventions.md` | 目录与模块 | 占位(规则 1 待添加)— 不影响本设计 |
| `framework-conventions.md` | 框架 | 占位 — 不影响 |
| `naming-conventions.md` | 命名 | 占位 — 不影响 |
| `coding-style.md` | 代码风格 | 占位 — 不影响 |
| `commit-conventions.md` | 提交 | 占位;REQ-00007 NFR-3 显式不沉淀规则(留 follow-up) |
| `dependency-conventions.md` | 三方依赖 | 占位;REQ-00007 NFR-1 显式零新增依赖 |

**本设计必须强约束遵守的规范**:`skill-conventions.md §规则 1`(新建技能元数据)、`module-conventions.md §规则 1`(新建技能的资源子目录)、`marketplace-protocol.md §规则 1`(不修改 marketplace.json / plugin.json)、`encoding-conventions.md §规则 1-4`(不产生新编码,仅消费既有)、`doc-conventions.md §规则 1`(中英 README 同步)。

**占位规范 6 个**:不影响本设计(无相关约束)。

## 上游需求

- 来源:`./assistants/V0.0.2/require/REQ-00007/RESULT.md`
- 版本:v1(已锁定)
- 提取的 FR / NFR / AC 数量:10 FR / 10 NFR / ~40 AC / 5 锁定(Q-1~Q-5)+ 7 采纳默认(Q-6~Q-12)+ 1 建议派生(Q-13)
- 关联需求材料:`./assistants/V0.0.2/require/REQ-00007/{clarifications.md, materials-index.md, related-requirements.md}`(均已读)

## 项目现状(本次扫描)

### 项目类型
- **类型**:Claude Code 插件市场(marketplace)仓库
- **顶层目录**:`./plugins/code-skills/`(插件本体)+ `./assistants/`(版本工作空间)
- **关键协议文件**:`./.claude-plugin/marketplace.json`(市场清单)+ `./plugins/code-skills/.claude-plugin/plugin.json`(子插件清单)
- **仓库根 CLAUDE.md**:经 V0.0.2 REQ-00012 移动到 `./CLAUDE.md`(本设计不修改;与 NFR-9 对齐)

### 既有 skills 目录(11 个已存在的 code-* 技能)

```
plugins/code-skills/skills/
├── code-init/      SKILL.md + (无子目录)
├── code-version/   SKILL.md + (无子目录)
├── code-rule/      SKILL.md + (无子目录)
├── code-require/   SKILL.md + templates/
├── code-design/    SKILL.md + templates/  (assistants-layout.md, design.md)
├── code-plan/      SKILL.md + templates/
├── code-it/        SKILL.md + guidelines/ + templates/
├── code-unit/      SKILL.md + templates/
├── code-fix/       SKILL.md + (无子目录)
├── code-review/    SKILL.md + checklists/ + templates/
└── code-publish/   SKILL.md + templates/
```

### 已有模块(本设计可复用)

| 模块/路径 | 职责 | 是否可复用 | 复用方式 |
| --- | --- | --- | --- |
| `skills/code-require/SKILL.md` | 需求分析 | 是(FR-3 步骤 1) | `code-auto` 通过 `Skill` 工具调 |
| `skills/code-design/SKILL.md` | 概要设计 | 是(FR-3 步骤 2) | 同上 |
| `skills/code-plan/SKILL.md` | 详细设计与任务计划 | 是(FR-3 步骤 3) | 同上 |
| `skills/code-it/SKILL.md` | 开发编码 | 是(FR-4 任务循环) | 同上 |
| `skills/code-unit/SKILL.md` | 单元测试 | 是(FR-4 任务循环,按需) | 同上 |
| `skills/code-review/SKILL.md` | 代码评审 | 是(FR-5 评审循环) | 同上 |
| `skills/code-version/SKILL.md` | 版本管理 | 是(步骤 0 隐式) | `code-auto` 不直接调,沿用 `.current-version` |
| `assistants/V0.0.2/RESULT.md` | 版本看板 | 是(NFR-5/6 数据源) | 子技能按既有规则更新看板 |
| `assistants/.current-version` | 激活版本标记 | 是(步骤 0a 读取) | 同 code-version 用法 |
| `plugins/code-skills/README.md` + `README.en.md` | 中英 README | 是(FR-8.AC-8.5) | "主要能力"段同次提交追加 1 行 |

### 已有接口(本设计消费)

- **Claude Code `Skill` 工具**:跨技能调用标准方式 — `code-auto` 调子技能必须用它
- **`AskUserQuestion` 工具**(子技能内部):通过子技能自身支持,**不**修改其行为;`code-auto` 在驱动子技能时**总选"推荐项"**(本设计不直接拦截,需子技能自身行为适配 — 详见 §约束)
- **子技能产物**:`require/REQ-NNNNN/RESULT.md` / `design/REQ-NNNNN/RESULT.md` / `plan/REQ-NNNNN/{RESULT,PLAN}.md` / `code/TASK-.../RESULT.md` / `test/TASK-.../RESULT.md` / `review/REQ-NNNNN/REVIEW-REPORT.md` / `review/<任务编码>/RESULT.md`(审查派生)

### 已有数据模型(本设计消费)

- **任务编码解析**(FR-4.AC-4.1):沿用 `encoding-conventions.md §规则 1` + `code-dashboard` NFR-3
  - 新格式正则:`^TASK-(REQ|BUG)-\d{5}-\d{5}$`
  - 旧格式正则:`^(REQ|BUG)-\d{5}-\d{5}$`
- **看板 3 区段锚点**:复用 `code-dashboard` 解析规则(FR-5.AC-5.6 + NFR-5)
- **`code-review` "必须改"枚举**:复用 V0.0.1 REQ-00001 既有"必须改/建议改/可选"三档

### 已有第三方依赖
- **运行时**:无(纯文档/技能/Markdown)
- **协议**:`marketplace-protocol.md` + `plugin.schema.json` + `marketplace.schema.json`(均只读)
- **新增依赖**:0(NFR-1 强约束)

### 编码与构建约定
- **SKILL.md frontmatter 格式**:YAML,`name` + `description`(skill-conventions §规则 1)
- **commit 行为**:子技能按各自规则 commit;`code-auto` 自身**不**commit(NFR-3)
- **末尾兜底提交**:由 `code-require` / `code-design` / `code-plan` 各自完成(REQ-00005 加)
- **新增 SKILL.md**:`name` 字段必须等于目录名(本设计为 `code-auto` → `skills/code-auto/SKILL.md`)

## 与规范的交叉验证

| 规范条款 | 现状 | 评价 |
| --- | --- | --- |
| `skill-conventions §规则 1`(name+description) | 10 个子技能全部 frontmatter 合规 | ✅ 本设计新建的 `code-auto` 必须同样合规 |
| `module-conventions §规则 1`(固定子目录) | 7 个子技能用 `templates/`,2 个用 `checklists/`,1 个用 `guidelines/` | ✅ 本设计 `code-auto/` 不需子目录(无模板/清单/规则) |
| `marketplace-protocol §规则 1`($schema 必填) | marketplace.json / plugin.json 合规 | ✅ 本设计**不**修改它们(FR-8.AC-8.3) |
| `dashboard-conventions §规则 1`(字段扩展三同步) | V0.0.2 看板扩展已同步 | ✅ 本设计**不**扩展字段,只追加"概要设计清单"行 |
| `doc-conventions §规则 1`(中英 README 对仗) | 2 个 README 结构对仗 | ✅ 本设计同次提交追加 1 行能力描述(FR-8.AC-8.5) |
| `encoding-conventions §规则 1-4` | V0.0.1 REQ-00002 已落地 | ✅ 本设计**不**产生新编码,仅消费既有 |

**无规范偏离**,**无现状偏离**(所有现状与规范一致)。

## 预检:规范 vs 需求冲突

- **未发现冲突**。REQ-00007 NFR-1/3/4/8/9 与既有规范均无冲突。
- **关注点 1(规范未明确):** `code-auto` "总选推荐项"的实现位置 — 是 `code-auto` 拦截 `AskUserQuestion`,还是要求子技能新增"自动模式"参数?详见 `clarifications.md Q-A1`。
- **关注点 2(规范未明确):** `code-auto` 与 `code-require` 步骤 0a(REQ-00005 加)的协同 — `code-auto` 一次执行中,子技能首步会做 5~20 次 `git pull`;是否需要"批量模式"?NFR-4 显式不引入。详见 `clarifications.md Q-A2`。
