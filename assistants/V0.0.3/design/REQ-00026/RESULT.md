# REQ-00026 概要设计 — 技能描述通用化

- **上游**:`./assistants/V0.0.3/require/REQ-00026/RESULT.md`
- **遵循规范**:`./assistants/rules/` 下 13 个文件(`skill-conventions.md` / `doc-conventions.md` / `encoding-conventions.md` / `commit-conventions.md` / `naming-conventions.md` 等)
- **版本**:V0.0.3
- **最后更新**:2026-06-08 12:30

## 1. 设计目标

回答"10 个 SKILL.md 的描述性段落如何去专属化":
- **目标 A:范围最小化** — 仅改"描述性段落",不动"硬约束段"(不变量、AC、INV、命令示例)
- **目标 B:占位符可读性** — `<本仓库>` 在每个被改 SKILL.md 概述段中显式声明含义
- **目标 C:0 改元信息** — `marketplace.json` / `plugin.json` / 仓库根 README / `CLAUDE.md` 全部 0 diff
- **目标 D:0 改 frontmatter** — 遵循 `skill-conventions.md §规则 1`

(源自:FR-1 / FR-2 / FR-3 / NFR-1 / NFR-3 / NFR-4)

## 2. 架构方案

### 2.1 整体架构:本项目架构不变

本需求为纯文案扫除,**不**改变本仓库的 marketplace 协议结构、`code-*` 技能家族拓扑、`./assistants/` 工作空间约定。

```
仓库根(marketplace 仓库,不变)
├── .claude-plugin/marketplace.json      (0 改)
└── plugins/code-skills/                 (0 改结构)
    ├── .claude-plugin/plugin.json      (0 改)
    ├── CLAUDE.md                        (0 改)
    ├── README.md / README.en.md         (0 改)
    └── skills/                          (改 SKILL.md 文字,不改结构)
        ├── code-require/SKILL.md         ← 改
        ├── code-design/SKILL.md          ← 改
        ├── code-plan/SKILL.md            ← 改
        ├── code-it/SKILL.md              ← 改
        ├── code-unit/SKILL.md            ← 改
        ├── code-check/SKILL.md           ← 改
        ├── code-fix/SKILL.md             ← 改
        ├── code-publish/SKILL.md         ← 改
        ├── code-publish/templates/*.md   ← 改 3 个 templates
        ├── code-rule/SKILL.md            ← 改(含 L336/363/370 CLAUDE.md 字面)
        ├── code-init/SKILL.md            ← 改
        ├── code-init/templates/INIT-REPORT.md  ← 改(L3/L8)
        ├── code-version/SKILL.md         (本需求 0 改,不在 FR-1 10 个内)
        ├── code-dashboard/SKILL.md       (本需求 0 改,不在 FR-1 10 个内)
        ├── code-auto/SKILL.md            (本需求 0 改,不在 FR-1 10 个内)
        ├── code-merge/SKILL.md           (本需求 0 改,不在 FR-1 10 个内)
```

### 2.2 数据流(逻辑视图)

本需求**不**引入新数据流。以下是"改动"层面的数据流:

```
原描述性文字(描述段)
  ↓ grep 命中 plugins/code-skills/... / 本项目 / 本仓库 / 本插件
  ↓ 段落级二分类(描述性 vs 硬约束)
  ↓ 描述性段 → 替换为 <本仓库> / 泛用表述
  ↓ 硬约束段 → 0 改动
  ↓ 末尾 grep 校验
RESULT
```

### 2.3 关键架构决策

| 决策 | 选定 | 理由 | 规范依据 |
| --- | --- | --- | --- |
| 占位符 | `<本仓库>` | 视觉上明显是占位符,可读 | (无) |
| 占位符声明 | 每个被改 SKILL.md 概述段加 1 句"`<本仓库>` 指代本 marketplace 仓库的根目录" | 避免读者自悟 | (无) |
| 段落识别 | 规则预筛 + 段落级复核(Q1 选 C) | 行级粒度过细,纯段落切片成本高 | (无) |
| 工具辅助 | 不新增脚本(方案 B 否决) | 本项目不写工程代码 | `dependency-conventions.md` |
| 新增规则 | 不新增(本需求范围外) | NFR-1 | NFR-1 |

(源自:design-notes.md §3)

## 3. 组件 / 模块拆分

详见 `module-breakdown.md`。共修改 13 个文件:
- 10 个 SKILL.md 描述性段
- 3 个 templates
- 1 个 INIT-REPORT.md

无新增模块,无复用既有之外的资产。

## 4. 接口与数据结构

本需求**不**新增 / 修改任何接口或数据结构。

## 5. 三方依赖

本需求**不**新增任何第三方依赖。详见 `dependencies.md`。

## 6. 关联概要设计

详见 `related-designs.md`。
- **无强关联设计**
- 旧设计 REQ-00020 / REQ-00022 / REQ-00024 / REQ-00025 的 module-breakdown 段使用 `plugins/code-skills/...` 路径,均为"模块定位字面",**不**被本需求波及

## 7. 规范遵循

### 7.1 本次参考的规范
- `skill-conventions.md §规则 1`:SKILL.md frontmatter 必含 `name` + `description` 且 `name` 与目录名一致 → 本需求 0 改 frontmatter,严守
- `doc-conventions.md §规则 1`:README 中英对仗 → 本需求 0 改 README,0 触发
- `encoding-conventions.md §规则 1+2`:编码格式 → 本需求 0 新增编码,0 触发
- `commit-conventions.md`:本需求 `code-it` 阶段 commit message 沿用 `chore(code-it):` 前缀(沿用既有)

### 7.2 规范 vs 现状偏离
- 详见 `rule-compliance.md §2`

### 7.3 规范 vs 需求冲突
**无冲突**(详见 `rule-compliance.md §3`)。

### 7.4 用户授权的偏离
**无**(本需求严守所有规范)。

## 8. 设计不变量(INV)

- **INV-1**:10 个 SKILL.md 的 frontmatter `name` + `description` **0 改**
- **INV-2**:`marketplace.json` / `plugin.json` **0 改**
- **INV-3**:仓库根 `README.md` / `README.en.md` / `CLAUDE.md` **0 改**
- **INV-4**:插件根 `plugins/code-skills/README.md` / `README.en.md` **0 改**
- **INV-5**:`./assistants/rules/` **0 改**
- **INV-6**:旧需求档案 `assistants/V0.0.3/require/REQ-*/**` **0 改**
- **INV-7**:本需求自身产出文件 `assistants/V0.0.3/require/REQ-00026/**` 与 `design/REQ-00026/**` **0 改**
- **INV-8**:`./assistants/` 路径在所有 SKILL.md 中**保持原样**
- **INV-9**:硬约束段(不变量 / AC / INV / 命令示例)字面**保持原样**

## 9. 待澄清 / 未决项

| 编号 | 项 | 状态 |
| --- | --- | --- |
| Q1 | Q5(硬约束是否替换为 `<本仓库>`) | 已决策:保留字面 |
| Q2 | Q6(后续 `code-check` 评审发现冲突如何裁决) | 留待评审阶段 |

## 10. 变更记录

- `2026-06-08 12:30` 概要设计完成(13 个目标文件 + 0 新增模块 + 9 条 INV)
