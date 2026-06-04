# 关联需求 — REQ-00012

更新时间:2026-06-04 15:10

## 扫描范围
- 同版本:`./assistants/V0.0.2/require/`
  - REQ-00004 ~ REQ-00011(10 个需求)
- 跨版本:`./assistants/V0.0.1/require/`
- 直接相关:
  - `./plugins/code-skills/CLAUDE.md`(已存在,8,603 bytes)
  - `./plugins/code-skills/README.md`(已存在,36,492 bytes)
  - `./plugins/code-skills/README.en.md`(已存在,39,947 bytes)
  - `./assistants/rules/doc-conventions.md §规则 1`(中英 README 对仗)
  - `./assistants/rules/doc-conventions.md §规则 2`(README 主语言版本完整性)
  - `./assistants/rules/skill-conventions.md`(技能元信息约束)

## 关联需求清单

### REQ-00001(版本:V0.0.1)— Marketplace 改名落地
- **关联点**:
  - **首条 commit** `f147ea7` 包含:`.claude-plugin/marketplace.json` 根 name + 中英 README
  - **README 历史**:V0.0.1 中,`plugins/code-skills/README.md` / `README.en.md` 是当时**主语言版本 README**(`doc-conventions §规则 2` 适用对象)
  - **本需求落地后**:仓库根 `./README.md` 成为**新主语言版本**;`plugins/code-skills/README.md` 是否仍为主语言版本?需在 `code-design` 阶段明确
- **对本需求的影响**:
  - **`doc-conventions §规则 2`** 需要明确"主语言版本"是仓库根还是 `plugins/code-skills/`
  - **建议**:本需求落地后,仓库根 README 是主语言版本,`plugins/code-skills/README.md` 改为"技能详细说明"(子文档)
- **来源**:`./assistants/V0.0.1/require/REQ-00001/RESULT.md`

### REQ-00003(版本:V0.0.1)— 优化 `code-rule` 技能
- **关联点**:
  - **`code-rule` 维护项目级规范**
  - **`doc-conventions.md` 是 `code-rule` 维护的规范文件**:`§规则 1`(中英对仗)+ `§规则 2`(主语言版本完整性)+ `§规则 3`(插件命名)— `code-rule` 添加于 V0.0.1
  - **本需求落地时**需遵循这些规则
- **对本需求的影响**:
  - **强制遵循** `doc-conventions §规则 1`:中英同次提交
  - **强制遵循** `doc-conventions §规则 2`:仓库根 README 必须含核心小节(简介 / 安装 / 使用 / 能力)
  - **建议派生**:在 `code-review REQ-00012` 阶段,可派生"用 `code-rule` 沉淀 '仓库根 README 与子目录 README 关系' 约定"任务
- **来源**:`./assistants/rules/doc-conventions.md`

### REQ-00004(版本:V0.0.2)— `/code-dashboard` 开发看板技能
- **关联点**:
  - **`code-dashboard` 是新增技能**,在 `plugins/code-skills/README.md` 中有说明
  - **本需求落地后**:`code-dashboard` 是否在仓库根 README 提及?(应是)
- **对本需求的影响**:
  - 仓库根 README 链到 `plugins/code-skills/README.md` 后,`code-dashboard` 等**已自动**被介绍
  - **不**触发 `code-dashboard` 升级
- **来源**:`./assistants/V0.0.2/require/REQ-00004/RESULT.md`

### REQ-00005 ~ REQ-00011(版本:V0.0.2)— 其他 7 个需求
- **关联点**:
  - 7 个其他 V0.0.2 需求(005~011)涉及修改 `plugins/code-skills/skills/*/SKILL.md`
  - **本需求落地后**:这些技能均应在 `plugins/code-skills/README.md` 中被提及
- **对本需求的影响**:
  - **不**触发这 7 个需求的修改
  - **`plugins/code-skills/README.md` 内容由 V0.0.2 历次需求**已**更新(本轮不主动写)
- **来源**:`./assistants/V0.0.2/require/REQ-*/RESULT.md`

### REQ-00002(版本:V0.0.1)— 编码格式统一
- **关联点**(间接):
  - **`encoding-conventions.md` 编码规范**
- **对本需求的影响**:
  - **不**影响
- **来源**:`./assistants/V0.0.1/require/REQ-00002/RESULT.md`

## 跨需求聚合(供 `code-design` 阶段权衡)

| 维度 | 涉及需求 | 共性 | 处理建议 |
| --- | --- | --- | --- |
| README 主从关系 | REQ-00001 | `plugins/code-skills/README.md` 是 V0.0.1 主语言版本 | 本需求落地后:**仓库根 README 是主语言版本**,`plugins/code-skills/README.md` 改为"技能详细说明" |
| 规范遵循 | REQ-00003 | `doc-conventions §规则 1` / `§规则 2` 强制约束 | 必须同次提交中英;必须含核心小节 |
| 内容覆盖 | REQ-00004 ~ 00011 | 9 个 `code-*` 技能(原 7 + `code-dashboard` + `code-auto`) | 仓库根 README 概览 + 链到 `plugins/code-skills/README.md` 详情 |
| 规范沉淀 | REQ-00003 | `code-rule` 维护项目级规范 | 本需求**不**直接写新规范,留作 follow-up |

## V0.0.0 EXISTING-* 任务
- 仓库根目录**无** `README.md` / `CLAUDE.md` — 本需求**首次**创建
- `plugins/code-skills/CLAUDE.md` 是 V0.0.1 起 `code-rule` 维护的产物(8,603 bytes,含"AI 工作约定"小节 + 多个 H2 章节)
- `plugins/code-skills/README.md` / `README.en.md` 是 V0.0.1 起 `code-rule` 维护的"主语言版本 README"
- 现有 `CLAUDE.md` / `README.md` 内容丰富(均 30K+ bytes),**不是**"极简"风格 — 本需求新建的仓库根文档应是"门面级"极简

## 关键事实扫描结果(供 clarifications.md 引用)
- 仓库根 `D:\Workspaces\wm\code-skills/` 现有文件(2026-06-04 15:10 扫描):
  - `.claude/`
  - `.claude-plugin/`
  - `.git/`
  - `.gitignore`
  - `assistants/`
  - `plugins/`
  - **无** `README.md` / `CLAUDE.md` / `README.en.md`
- `plugins/code-skills/` 现有文件:
  - `CLAUDE.md`(8,603 bytes)
  - `README.md`(36,492 bytes)
  - `README.en.md`(39,947 bytes)
- `assistants/rules/doc-conventions.md` §规则 1 / §规则 2 是本需求的**强制约束**
- `assistants/rules/skill-conventions.md` §规则 1 与本需求**不**直接相关(本需求**不**涉及 SKILL.md)
- V0.0.1 看板"V0.0.1 已建立 4 个里程碑"与本需求**不**直接相关
- 9 个 `code-*` 技能(V0.0.2)+ `code-auto` + `code-dashboard` + `code-publish` + `code-rule` = 10 个技能(本轮不主动数,沿用 V0.0.2 已有统计)
