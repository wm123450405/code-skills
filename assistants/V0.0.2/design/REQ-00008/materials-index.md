# 材料登记 — REQ-00008
更新时间:2026-06-05 15:55
版本:V0.0.2
需求编码:REQ-00008
设计标题:`/code-review` 整版本模式(无参评审)

---

## 项目级规范(`./assistants/rules/**/*`)

| 规范文件 | 类别 | 关键约束摘要 | 本设计对应章节 |
| --- | --- | --- | --- |
| `skill-conventions.md` | 技能编写 | §规则 1:SKILL.md 必含 `name` + `description` frontmatter;`name` 与目录名 kebab-case 严格一致 | §10.1 SKILL.md 修改边界(只追加无参入口,**不**改 frontmatter) |
| `module-conventions.md` | 模块规划(**DEPRECATED** 标记,但**仍引用** §规则 1 资源子目录约定) | §规则 1:`templates/` / `checklists/` / `guidelines/` 是技能根目录下唯一允许的子目录名 | §10.1 SKILL.md 范围限定;本设计**不**新增子目录(无新模板) |
| `directory-conventions.md` | 目录与模块(**新替代 module-conventions**) | §规则 1 占位 — 暂无内容 | (不触发) |
| `dashboard-conventions.md` | 看板与版本工作空间 | §规则 1:看板字段约定扩展需 3 处同步(模板 + CLAUDE.md + 本文件);本设计**不扩展字段**,只追加"概要设计清单"行 | §11 看板同步(无 3 处同步触发) |
| `encoding-conventions.md` | 编码格式权威源 | §规则 1:REQ `^REQ-\d{5}$` / TASK `^TASK-(REQ\|BUG)-\d{5}-\d{5}$`;§规则 4:派生任务由 `code-plan` 生成 TASK ID | §10.3 PLAN.md 派生任务追加沿用 §规则 4 |
| `marketplace-protocol.md` | Marketplace 协议 | §规则 1:`marketplace.json` / `plugin.json` 字段约束;本设计**不**修改 marketplace.json(本需求**不**新增技能,只优化既有) | §10.1 修改边界 0 触发 |
| `doc-conventions.md` | 文档编写 | §规则 1:README 中英同次提交 + 结构对仗;§规则 2:README 必须持续维护;本设计**不**主动写 README(由 `code-rule` 沉淀 — Q-7 采纳默认) | §10.1 0 触发 |
| `migration-mapping.md` | 编码迁移追溯 | §规则 1-4:已落地/理论/EXISTING-NNN 不追溯;本设计**不触发** | (不触发) |
| `framework-conventions.md` | 框架选型(占位) | §规则 1 占位 | (不触发) |
| `naming-conventions.md` | 命名风格(占位) | §规则 1 占位 | (不触发) |
| `coding-style.md` | 代码风格(占位) | §规则 1 占位 | (不触发) |
| `commit-conventions.md` | 提交合并(占位) | §规则 1 占位 | (不触发) |
| `dependency-conventions.md` | 三方依赖(占位) | §规则 1 占位 | (不触发) |

**有效约束**:7 个文件(`skill` / `module`(DEPRECATED 仍引用) / `dashboard` / `encoding` / `marketplace` / `doc` / `migration`)
**占位规范**:6 个(不触发)
**有效 + 占位 总计**:13 个

> 注:本设计 100% 合规(对应 REQ-00008 的 NFR-8 隐含约束 — `code-review` 整版本模式"严格按既有 `code-dashboard` / `code-auto` / `code-publish` 既有规范落地")。

---

## 上游需求

- 来源:`./assistants/V0.0.2/require/REQ-00008/RESULT.md`
- 版本:v1(2026-06-04 14:07 锁定,wangmiao)
- 状态:已锁定(由 `code-require` 完成)
- 提取的 FR / NFR / AC 数量:9 FR(FR-1 ~ FR-9) / 8 NFR(NFR-1 ~ NFR-8) / ~30 AC / 9 个边界场景(E-1 ~ E-9) / 5 个 Q-locked + 3 个采纳默认 + 1 个新增待定(Q-8)
- 7 项已锁定决策:
  - **Q-1**:整版本模式**只**评审"已完成"状态的需求(B,过滤"进行中/待开始/已取消/阻塞")
  - **Q-2**:聚合文件 = `./assistants/<版本号>/REVIEW.md`(与 `RESULT.md` 同级)+ 单需求文件沿用 `review/REQ-NNNNN/REVIEW-REPORT.md` + 多次执行**覆盖**(B+C 混合)
  - **Q-3**:无任务可评审 → 报告 + 退出(默认,采纳)
  - **Q-4**:派生任务能力支持(与模式 1 一致,默认)
  - **Q-5**:`code-auto` 评审循环**继续**用模式 1;整版本模式由用户手动调(默认)
  - **Q-6**:`code-review` 不在 REQ-00005 改写范围(默认)
  - **Q-7**:`commit-conventions.md` 与 CLAUDE.md 追加**不**做(默认,留作 follow-up)
- 1 项新增待定:
  - **Q-8**:派生任务预警(建议派生:`code-rule` 沉淀 `review-conventions.md` + `code-review` 加入 REQ-00005 改写范围)— **不阻塞**本需求

### 规范 vs 需求预检冲突(扫描结果)

无冲突。本需求是"既有 `code-review` 技能的扩展",严格遵循既有 9 个技能 SKILL.md 的 frontmatter / 章节骨架,无字段约定扩展,无新规范沉淀。

---

## 项目现状(本次扫描)

### 项目类型
- **类型**:Claude Code 技能集合(无业务代码、无构建系统、无测试框架、无 Lint)
- **语言/框架**:Markdown(SKILL.md + templates/ + checklists/) + JSON(marketplace.json + plugin.json)
- **关键依赖**:**0 个**运行时依赖(所有技能复用 Claude Code 平台工具集 `Bash` / `Read` / `Write` / `Edit` / `Glob` / `Grep`)

### 目录结构(本技能相关)

```
code-skills/                          ← marketplace 仓库根
├── .claude-plugin/
│   └── marketplace.json              # 10 个 skills 已注册(待本需求变 0 增 — 既有 code-review 已存在)
└── plugins/
    └── code-skills/
        ├── .claude-plugin/
        │   └── plugin.json           # 子插件元信息
        ├── README.md                 # 中文
        ├── README.en.md              # 英文
        ├── CLAUDE.md                 # AI 工作约定
        └── skills/
            └── code-review/          ← 本需求目标技能
                ├── SKILL.md           # 既有 frontmatter(必须保持不变)
                ├── checklists/
                │   └── review-checklist.md   # 既有内置评审清单
                └── templates/
                    ├── REVIEW-REPORT.md      # 既有主报告模板
                    ├── REVIEW-FIX.md         # 既有派生改修要求模板
                    └── assistants-layout.md  # 既有目录布局参考
```

### 已有模块(本需求相关)

| 模块/路径 | 职责 | 是否可复用 |
| --- | --- | --- |
| `plugins/code-skills/skills/code-review/SKILL.md` | 既有 `code-review` 技能定义(模式 1:单需求评审) | ✅ 复用(本设计**仅**追加无参入口处理逻辑,**不**重写既有章节) |
| `plugins/code-skills/skills/code-review/checklists/review-checklist.md` | 内置评审清单(9 维度 + 评审结论判定) | ✅ 复用(整版本模式对每个被评审需求复用) |
| `plugins/code-skills/skills/code-review/templates/REVIEW-REPORT.md` | 模式 1 整体评审报告模板(8 章节) | ✅ 复用(整版本模式单需求文件**完全复用**此模板) |
| `plugins/code-skills/skills/code-review/templates/REVIEW-FIX.md` | 派生改修要求模板(给 `code-it` 消费) | ✅ 复用(整版本模式派生任务**完全复用**) |
| `plugins/code-skills/skills/code-review/templates/assistants-layout.md` | 目录布局参考 | ✅ 复用(新增聚合文件路径会**反注**到此模板的可写位置) |
| `assistants/V0.0.1/review/REQ-00001/REVIEW-REPORT.md` | 模式 1 历史产物(2 发现 + 1 派生 T-005) | 📚 参考(本设计"模式 2 聚合文件"的字面结构参考) |
| `assistants/V0.0.1/review/REQ-00002/REVIEW-REPORT.md` | 模式 1 历史产物(3 发现 + 2 派生) | 📚 参考(同上) |
| `assistants/V0.0.1/review/REQ-00003/REVIEW-REPORT.md` | 模式 1 历史产物(1 发现) | 📚 参考(同上) |
| `assistants/V0.0.2/RESULT.md`(主看板) | 需求清单 / 概要设计清单 / 任务清单 / 缺陷清单 | 📖 只读(整版本模式过滤"已完成"需求的数据源) |
| `assistants/V0.0.2/plan/REQ-NNNNN/PLAN.md` | 各需求任务清单 | 📖 只读(派生任务追加的目标;整版本模式对每个被评审需求的 PLAN.md 追加派生行) |
| `assistants/V0.0.2/review/REQ-NNNNN/REVIEW-REPORT.md` | 模式 1 路径(整版本模式可**覆盖**) | ✏️ 写(覆盖,模式 1 与模式 2 互覆盖,NFR-6 + FR-7.AC-7.1 允许) |

### 已有接口(本需求相关)

| 接口/方法 | 既有行为 | 整版本模式行为 |
| --- | --- | --- |
| `code-review REQ-NNNNN`(模式 1) | 评审单需求 → 写 `review/REQ-NNNNN/REVIEW-REPORT.md` + 派生任务 | **不变**(FR-7.AC-7.1 / FR-7.AC-7.2 / FR-7.AC-7.4) |
| `code-review`(无参) | (目前**无**此模式 — V0.0.1 仅支持模式 1) | **新增**(FR-1.AC-1.1):整版本评审 → 写 `REVIEW.md` + N 份 `REVIEW-REPORT.md` |

### 已有数据模型(本需求相关)

| 数据 | 既有形态 | 整版本模式新增/不变 |
| --- | --- | --- |
| **REVIEW-REPORT.md 顶层结构** | 8 章节(评审信息 / 评审清单 / 任务评审结果 / 发现汇总 / 派生的新任务列表 / 未派生任务的发现 / 超出本次评审范围的发现 / 整体结论 + 变更记录) | **不变**(FR-6.AC-6.1 + FR-7.AC-7.1 强约束) |
| **REVIEW.md 顶层结构**(本设计新增) | (不存在) | 5 章节:评审概览 / 各需求评审摘要 / 评审发现汇总(去重)/ 派生任务汇总 / 评审人/AI 备注 |
| **PLAN.md "任务总览"表追加派生任务** | 模式 1 已支持(触发/来源=审查改修) | 整版本模式对**多个**需求的 PLAN.md 各自追加 1 行(FR-5.AC-5.1) |
| **看板同步** | 模式 1 写"评审发现汇总" / "派生任务记录" / "缺陷清单" / "任务清单" / "变更记录" | 整版本模式**不**触发额外看板同步(模式 1 路径已覆盖所有区段) |

### 已有第三方依赖
- **0 个**(所有技能复用 Claude Code 平台工具集)

### 编码与构建约定
- **本仓库无构建系统、无 Lint、无测试框架**(CLAUDE.md §需与用户确认的约定 显式声明)
- SKILL.md 遵循 `skill-conventions §规则 1`(frontmatter + 章节骨架)
- 资源放 `templates/` / `checklists/` / `guidelines/`(`module-conventions §规则 1`,DEPRECATED 但仍引用)
- 看板字段约定扩展需 3 处同步(`dashboard-conventions §规则 1`)
- 任务编号遵循 `encoding-conventions §规则 1-4`(本设计派生任务追加到 PLAN.md,**不**生成新编码 — 沿用 `code-plan` 既有规则)

### 可复用资产
- ✅ `REVIEW-REPORT.md` 模板(模式 1) — **完全复用**(FR-3.AC-3.1)
- ✅ `REVIEW-FIX.md` 模板 — **完全复用**(派生改修要求文档化)
- ✅ `review-checklist.md` 清单 — **完全复用**(9 维度逐项)
- ✅ `code-review` SKILL.md 步骤 0-15 — **复用**步骤 0(版本上下文检测) + 步骤 4(读上游) + 步骤 5(列待评审) + 步骤 6(读代码) + 步骤 7(加载清单) + 步骤 8(逐任务评审) + 步骤 9(分类发现) + 步骤 10(分配新任务编号) + 步骤 11(写 review/新任务/RESULT.md) + 步骤 12(写整体 REPORT) + 步骤 13(同步看板) + 步骤 14(完善过程文档) + 步骤 15(汇报)
- ❌ `SKILL.md` frontmatter — **不**复用为"新增",**不**改(FR-7.AC-7.2 + `skill-conventions §规则 1`)
- ❌ 模式 1 行为 — **不**重写(FR-7.AC-7.4)

---

## 现状偏离 vs 规范自检

无偏离。本设计 100% 遵循既有 7 个有效规范 + 不触发 6 个占位规范。
