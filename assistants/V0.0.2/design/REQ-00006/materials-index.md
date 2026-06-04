# 材料登记 — REQ-00006

更新时间:2026-06-04 16:48
版本:V0.0.2

## 1. 项目级规范(本次扫描 13 个文件,有效约束 4 个)

| 规范文件 | 类别 | 关键约束摘要 | 对本设计的影响 |
| --- | --- | --- | --- |
| `dashboard-conventions.md` | 看板与版本工作空间 | §规则 1:`RESULT.md` 字段约定扩展需 3 处同步(templates/version-RESULT.md + CLAUDE.md "看板字段约定"段 + 本规范) | 本设计**不**扩展看板字段(只**只读消费**),0 触发 |
| `doc-conventions.md` | 文档编写 | §规则 1:README 多语言版本必须结构对仗,同次提交;§规则 2:`plugins/code-skills/README.md` 必须存在并持续维护 | 本设计若在 README "主要能力"追加一行,中英必须同次同步 |
| `encoding-conventions.md` | 编码格式 | §规则 1:3 类编码格式权威源;§规则 3:嵌套式 TASK 解析正则 | 本设计**不**产生新编码(`code-publish` 不生成 TASK/REQ/BUG),0 触发;但**消费**这些编码作为前置检查的字符串匹配键 |
| `marketplace-protocol.md` | Marketplace 协议 | §规则 1:`marketplace.json` 与 `plugin.json` 字段约束 | 本设计**不**修改 marketplace.json/plugin.json(NFR — REQ-00006 §FR-8.AC-8.1 明确禁止),0 触发 |
| `module-conventions.md` | 模块规划(已 DEPRECATED) | §规则 1:`templates/` / `checklists/` / `guidelines/` 三类固定子目录 | 本设计**新增技能**:`templates/` 子目录摆放 3 份手册模板 |
| `directory-conventions.md` | 目录与模块(替代 module-conventions) | 占位,无实质规则 | 0 触发 |
| `skill-conventions.md` | 技能编写 | §规则 1:SKILL.md frontmatter 必含 `name` + `description`,`name` 与目录名一致 | 本设计**强约束**新技能 `code-publish` 的 SKILL.md |
| `coding-style.md` | 代码书写 | 占位,无实质规则 | 0 触发 |
| `commit-conventions.md` | 提交与合并 | 占位,无实质规则 | 0 触发 |
| `dependency-conventions.md` | 三方依赖 | 占位,无实质规则 | 0 触发(NFR-1 零新增依赖,与占位规范兼容) |
| `framework-conventions.md` | 框架选型 | 占位,无实质规则 | 0 触发 |
| `naming-conventions.md` | 语言与命名 | 占位,无实质规则 | 0 触发 |
| `migration-mapping.md` | 编码迁移映射 | 5 规则,均为追溯参考,不影响新设计 | 0 触发 |

**有效约束数**:4 个(dashboard-conventions / doc-conventions / module-conventions / skill-conventions),其余 9 个为占位或不相关。

## 2. 上游需求

- 来源:`./assistants/V0.0.2/require/REQ-00006/RESULT.md`
- 版本:v1(2026-06-04 13:45 已锁定)
- 提取摘要:
  - **9 FR**:FR-1 前置检查 / FR-2 生成 3 份手册 / FR-3 DEPLOY 模板 / FR-4 UPDATE 模板 / FR-5 Q&A 模板 / FR-6 创建 `qanda/` 骨架 / FR-7 错误处理 / FR-8 不修改其他 8 技能 / FR-9 报告
  - **9 NFR**:零依赖 / 纯只读检查 / 不自动 commit / 不参与 REQ-00005 / 通用性优先 / 幂等覆盖 / 基线识别 / 与 dashboard 数据源一致 / 可读性优先
  - **~33 AC**(详见 RESULT.md §10)
  - **10 边界**:E-1 ~ E-10(已穷尽)
  - **关联需求**:REQ-00004(code-dashboard 同看板数据源)/ REQ-00005(不在改写范围)/ REQ-00001(里程碑不检查,Q-5 默认)/ REQ-00003(不创建 publish-conventions 规范)/ REQ-00002(不产生新编码)
- **关键锁定**:
  - Q-1 锁定 A(全检查最严)
  - Q-2 锁定 A(创建 qanda/ 骨架)
  - Q-3 锁定 A(基线不生成 UPDATE.md)
  - Q-4 锁定 C(通用骨架 + 默认示例)
  - Q-5~Q-9 默认采纳(不检查里程碑 / 不自动抽取 / 不参与 REQ-00005 / 不沉淀规范 / 不自动 commit)

## 3. 项目现状(本次扫描)

### 3.1 项目类型
- **本仓库**:`code-skills`,Claude Code Marketplace 插件(纯文档型,无代码、无构建、无测试)
- **语言**:无源码;仅 Markdown(SKILL.md / templates / 规范 / 看板)+ JSON(marketplace.json / plugin.json)
- **运行时**:Claude Code(`claude` CLI) — 通过读取 `SKILL.md` 的 YAML frontmatter 触发技能
- **关键依赖**:无外部依赖

### 3.2 目录结构(根)
```
./
├── README.md              # 仓库根门面(REQ-00012 计划新建,V0.0.2 未实施)
├── README.en.md           # 仓库根英文门面(同上)
├── CLAUDE.md              # 仓库根 CLAUDE.md(REQ-00012 计划移动,V0.0.2 未实施)
├── .claude-plugin/
│   └── marketplace.json   # marketplace 协议清单
├── plugins/
│   └── code-skills/
│       ├── .claude-plugin/plugin.json
│       ├── README.md      # 详细技能文档(中)
│       ├── README.en.md   # 详细技能文档(英)
│       ├── CLAUDE.md      # 当前 CLAUDE.md 主体
│       └── skills/        # 10 个 code-* 技能子目录
│           ├── code-init/
│           ├── code-version/
│           ├── code-rule/
│           ├── code-require/
│           ├── code-design/
│           ├── code-plan/
│           ├── code-it/
│           ├── code-unit/
│           ├── code-fix/
│           └── code-review/
└── assistants/
    ├── .current-version   # 当前激活版本(本项目 = V0.0.2)
    ├── rules/             # 13 项目级规范文件(本次只读)
    ├── V0.0.0/            # 基线版本快照
    ├── V0.0.1/            # 上一个版本
    └── V0.0.2/            # 当前版本(本次工作空间)
```

### 3.3 已有 10 技能(全部为 SKILL.md + 可选 templates/checklists 子目录)

| 技能名 | 子目录 | 是否可复用 |
| --- | --- | --- |
| `code-init` | 无 | 不复用(项目级一次性引导) |
| `code-version` | `templates/version-RESULT.md` `templates/assistants-layout.md` | **关键复用**:读取 `.current-version`、读取 `<版本号>/RESULT.md` 模板与解析锚点 |
| `code-rule` | `templates/rule.md` `templates/assistants-layout.md` | 不复用(横向规范管理) |
| `code-require` | `templates/` | 不直接复用,但**消费**其产出物(`<版本号>/require/<REQ>/RESULT.md` 的"状态"字段) |
| `code-design` | `templates/design.md` `templates/assistants-layout.md` | **本技能即 code-design 自身**,使用其 design.md 模板 |
| `code-plan` | `templates/` | 不直接复用,但**消费**其产出物(`<版本号>/plan/<REQ>/PLAN.md` 的"任务清单"区段) |
| `code-it` | `templates/` | 不复用 |
| `code-unit` | `templates/` | 不复用 |
| `code-fix` | `templates/bug.md` `templates/fix-registry.md` `templates/assistants-layout.md` | 不直接复用,但**消费**其产出物(`<版本号>/fix/RESULT.md` 的"缺陷清单"区段);**注意**:本设计实际上消费的是 `<版本号>/RESULT.md`(主看板)中的"缺陷清单"区段,不是 fix/RESULT.md |
| `code-review` | `templates/` `checklists/review-checklist.md` | 不复用 |

### 3.4 看板("解决状态"判定的数据源)

`<版本号>/RESULT.md`(版本看板)有 13 个区段(见 `templates/version-RESULT.md`),本设计**只读消费** 3 个:

| 区段 | 锚点(`grep`/`sed` 规则) | 列字段 | 判定逻辑 |
| --- | --- | --- | --- |
| **需求清单** | `^## 需求清单` → 下一个 `^## ` | `需求编码` / `标题` / `状态` / `创建时间` / `完成时间` / ... | 解决 = `状态` ∈ {`已完成`} |
| **任务清单** | `^## 任务清单` → 下一个 `^## ` | `任务编号` / `需求` / `类型` / `触发/来源` / `标题` / `开发状态` / `测试状态` / `涉及文件` / `完成时间` / `提交哈希` / `关联任务` | 解决 = `开发状态` ∈ {`已完成`} ∧ `测试状态` ∈ {`已运行-通过`, `不适用`} |
| **缺陷清单** | `^## 缺陷清单` → 下一个 `^## ` | `缺陷编号` / `严重度` / `标题` / `状态` / `报告时间` / `修复时间` / `关联任务` / `修复提交` | 解决 = `状态` ∈ {`已修复`} |

**关键**:本设计沿用 V0.0.1 起稳定的 Markdown 表格结构(行格式 `| col1 | col2 | ... |`),解析方式为"按 `|` split + trim",不引入新 parser。

### 3.5 既有第三方依赖
- **无**(本仓库纯文档,Claude Code 运行时不需要任何包管理)
- `code-publish` 同样不引入任何依赖(NFR-1)

### 3.6 编码与构建约定
- **不存在**:本仓库无 `package.json` / `pyproject.toml` / `Cargo.toml` 等构建文件
- 技能"实现"全部在 `SKILL.md` 的自然语言指令中,由 Claude Code 在用户调用时解释执行

### 3.7 可复用资产

| 资产 | 路径 | 复用方式 |
| --- | --- | --- |
| `templates/assistants-layout.md` | 几乎每个技能都有一份 | 在 `code-publish/templates/` 下复制相同模板(标准模板) |
| `templates/version-RESULT.md` | `code-version/templates/` | 不复用,但**对照其结构**确定解析锚点 |
| `templates/design.md` | `code-design/templates/` | 本设计 `RESULT.md` 的章节结构来源 |
| `templates/review-checklist.md` | `code-review/checklists/` | 不复用(本技能不评审,只检查 3 区段) |
| `templates/bug.md` 等 | `code-fix/templates/` | 不复用(本技能不登记缺陷,只读取看板缺陷清单) |

### 3.8 与规范的交叉验证(现状偏离)

- **0 现状偏离**:本设计是"新增技能"(non-modifying),不涉及对已有代码/规范的纠正
