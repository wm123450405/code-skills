# 关联需求 — REQ-00013

更新时间:2026-06-04 15:24

## 扫描范围
- 同版本:`./assistants/V0.0.2/require/`
  - REQ-00004 ~ REQ-00012(9 个需求)
- 跨版本:`./assistants/V0.0.1/require/`
  - REQ-00001 ~ REQ-00003(3 个需求)
- 直接相关:
  - `./plugins/code-skills/skills/code-fix/`(SKILL.md 17,878 bytes)— 实际存在的 V0.0.0 技能
  - `./assistants/V0.0.1/require/REQ-*/RESULT.md` 标题(第 1 行)
  - `./assistants/V0.0.1/plan/REQ-00001/PLAN.md` 任务总览(列含"标题")

## 关联需求清单

### REQ-00004(版本:V0.0.2)— `/code-dashboard` 开发看板技能
- **关联点**:
  - **同一看板 3 大区段数据源**:`code-dashboard` 现有"任务清单"区段已含**"标题"列**(`req04/RESULT.md §NFR-8` 指出"任务编码 + 标题"是关键)
  - **本需求落地后**:`code-dashboard` 输出应使用"编号+标题"格式
- **对本需求的影响**:
  - **`code-dashboard` 现有 0 改动**(看板"标题"列已存在)
  - **本需求**让 `code-dashboard` 的"下一步建议"段 / "聚合视图"中显示"编号+标题"
  - **建议派生**:`code-dashboard` 升级"全部完成"建议中包含"REQ-NNNNN · 标题"
- **来源**:`./assistants/V0.0.2/require/REQ-00004/RESULT.md` §NFR-8

### REQ-00005(版本:V0.0.2)— 优化 3 技能,加首步拉取与末步提交
- **关联点**:
  - **`code-require` / `code-design` / `code-plan` 三个技能**被 REQ-00005 改写(增量追加"步骤 0a 拉取"与"末尾兜底提交")
  - **本需求**同样改写 `code-require` / `code-plan`(增加"标题"生成)
- **对本需求的影响**:
  - **叠加方式**:本需求在 `code-require` / `code-plan` 的 SKILL.md 中**再追加**"标题生成"步骤
  - **结构一致性**:本需求步骤命名沿用既有"步骤 0a / 0b / N"模式
  - **`code-fix` 不在 REQ-00005 改写范围**,本需求是**首次**改写 `code-fix`(从 V0.0.0 起 SKILL.md 17,878 bytes 未变)
- **来源**:`./assistants/V0.0.2/require/REQ-00005/RESULT.md` §FR-1 / §FR-3

### REQ-00006(版本:V0.0.2)— `/code-publish` 发布部署技能
- **关联点**:
  - **`code-publish` 前置检查报告**会列出"未完成项明细",目前是"REQ-00005 状态=进行中" — 用户原话"不是仅编号或'本需求'等字样"
  - **本需求落地后**:`code-publish` 报告应使用"REQ-00005 · 优化 3 技能"格式
- **对本需求的影响**:
  - **`code-publish` 需升级**前检查报告的"未完成项明细"格式
  - **是否触发 `code-review`**:本需求落地后,`code-publish` 的报告格式与"本需求"统一性可由 review 验证
  - **建议**:`code-publish` 升级范围有限(NFR-5 报告输出格式,**不**改前置检查逻辑)
- **来源**:`./assistants/V0.0.2/require/REQ-00006/RESULT.md` §FR-9 / §9 边界

### REQ-00008(版本:V0.0.2)— `/code-review` 整版本模式
- **关联点**:
  - **`code-review` 派生任务**写入 `PLAN.md` 任务总览时**有"标题"列**
  - **本需求落地后**:`code-review` 派生任务的"标题"自动生效
- **对本需求的影响**:
  - **`code-review` 0 改动**(派生任务本就有"标题")
  - **`code-review` 评审发现的"级别 + 描述"格式**保持不变(那是"发现"维度,不是"任务"维度)
- **来源**:`./assistants/V0.0.2/require/REQ-00008/RESULT.md` §FR-5

### REQ-00009(版本:V0.0.2)— `/code-unit` 项目可测性守卫
- **关联点**(间接):
  - **`code-unit` 不感知**"标题"概念
- **对本需求的影响**:
  - **不**触发 `code-unit` 升级
- **来源**:`./assistants/V0.0.2/require/REQ-00009/RESULT.md`

### REQ-00010(版本:V0.0.2)— `/code-it` 前置任务守卫
- **关联点**:
  - **`code-it` 守卫的"中止报告"含"推荐执行 /code-it TASK-...-... 完成后,再执行 /code-it ..."` — 没有标题**
  - **本需求落地后**:中止报告应使用"编号+标题"格式
- **对本需求的影响**:
  - **`code-it` 需升级**中止报告的"推荐执行命令"格式
  - **`code-it` 守卫不通过时**:从 `PLAN.md` 任务总览读出每个任务的"标题" → 拼成"推荐执行 TASK-...-... · 标题 完成后,..."
- **来源**:`./assistants/V0.0.2/require/REQ-00010/RESULT.md` §FR-2

### REQ-00007(版本:V0.0.2)— `/code-auto` 自动开发技能
- **关联点**:
  - **`code-auto` 调 `code-require` / `code-plan` / `code-it` / `code-unit` / `code-review` 时**,会触发"用户交互"(中)
  - **本需求落地后**:`code-auto` 的进度报告中应使用"编号+标题"
- **对本需求的影响**:
  - **`code-auto` 进度报告**(每步打印)应升级为"编号+标题"格式
  - **`code-auto` 完整报告**(`require/REQ-NNNNN/auto-report.md`)应升级
- **来源**:`./assistants/V0.0.2/require/REQ-00007/RESULT.md` §NFR-10

### REQ-00011(版本:V0.0.2)— `/code-design` / `/code-plan` 设计目标确认
- **关联点**:
  - **`code-plan` 步骤 0b 读 `design/.../RESULT.md` 的"## 设计目标"小节**
  - **本需求落地后**:`code-plan` 在"调整任务拆分粒度"时可读"任务标题"作为参考
- **对本需求的影响**:
  - **不**触发 `code-plan` 升级
- **来源**:`./assistants/V0.0.2/require/REQ-00011/RESULT.md`

### REQ-00001(版本:V0.0.1)— Marketplace 改名落地(REVIEW 派生任务样板)
- **关联点**(直接):
  - **现有 V0.0.1 任务的"标题"列**:`plan/REQ-00001/PLAN.md` 任务总览含"标题"列(如"改 marketplace.json 根 name")
  - **现有 2 个 V0.0.1 派生任务**(REQ-00001-005 / REQ-00002-009)由 `code-review` 派生,均有"标题"
- **对本需求的影响**:
  - **历史"标题"已存在**,本需求让用户交互/看板**显示**"标题" — 不需回填
  - **关键佐证**:V0.0.1 已建立"标题是任务的必须字段"
- **来源**:`./assistants/V0.0.1/plan/REQ-00001/PLAN.md` 任务总览区段

### REQ-00002(版本:V0.0.1)— 编码格式统一
- **关联点**(间接):
  - **`encoding-conventions.md`** 编码规范
- **对本需求的影响**:
  - **不**影响
- **来源**:`./assistants/V0.0.1/require/REQ-00002/RESULT.md`

### REQ-00003(版本:V0.0.1)— 优化 `code-rule` 技能
- **关联点**:
  - **`code-rule` 维护项目级规范**
  - **本需求**不直接写新规范
- **对本需求的影响**:
  - **建议派生**:`code-rule` 沉淀"标题字段约定"(留作 review 阶段)
- **来源**:`./assistants/V0.0.1/require/REQ-00003/RESULT.md`

## 跨需求聚合(供 `code-design` 阶段权衡)

| 维度 | 涉及需求 | 共性 | 处理建议 |
| --- | --- | --- | --- |
| 字段位置 | REQ-00001 | 现有任务的"标题"已存在 | 本需求**不**新增字段,从已有内容派生 |
| 步骤命名 | REQ-00005 | "步骤 0a / 0b"模式 | 本需求新增"步骤 1a 标题生成"或"步骤 2.5 标题校对" |
| 报告格式 | REQ-00004 / REQ-00006 / REQ-00007 / REQ-00010 | 报告含"编号"但无"标题" | 这些技能需**升级**报告输出格式 |
| 协同 0 冲突 | REQ-00008 / REQ-00009 / REQ-00011 | 不感知"标题"概念 | 不触发这些技能升级 |
| 规范沉淀 | REQ-00003 | `code-rule` 维护项目级规范 | 本需求**不**直接写规范,留作 follow-up |

## V0.0.0 EXISTING-* 任务
- **V0.0.0 起 7 个 `code-*` 技能**:`code-init` / `code-version` / `code-require` / `code-design` / `code-plan` / `code-it` / `code-unit` / `code-review` / `code-fix` / `code-rule` — 实际 10 个
- **V0.0.0 已有任务的"标题"**:`plan/.../PLAN.md` 任务总览的"标题"列 — **已有**
- **V0.0.1 已有需求的"标题"**:`require/.../RESULT.md` 第 1 行的 `# 需求提示词文档 — <需求标题>` — **已有**
- **V0.0.1 起派生任务的"标题"**:由 `code-review` 写入 `PLAN.md` 任务总览 — **已有**

## 关键事实扫描结果(供 clarifications.md 引用)
- 仓库实际有 **13 个 `code-*` 技能**(V0.0.0 共 10 个 + V0.0.2 新增 3 个: `code-dashboard` / `code-publish` / `code-auto`)
- `code-fix` 是 V0.0.0 起的**真实存在**的技能,SKILL.md 17,878 bytes
- 现有 12 个 V0.0.0~V0.0.2 需求(REQ-00001~00012)均有"标题":
  - REQ-00001:"Marketplace 改名落地" / "Marketplace 根名称添加 `-marketplace` 后缀"
  - REQ-00002:"编码格式统一(REQ/TASK/BUG 均 5 位,采用新规则)"
  - REQ-00003:"优化 `code-rule` 技能,增加不同类型的核心编码规范的解析或引导"
  - REQ-00004:"添加 `/code-dashboard` 开发看板技能"
  - REQ-00005:"优化 `code-require` / `code-design` / `code-plan`,增加"首步拉取最新代码"与"末步兜底提交""
  - REQ-00006:"增加 `/code-publish` 发布部署技能,生成 DEPLOY.md / UPDATE.md / Q&A.md"
  - REQ-00007:"增加 `/code-auto` 自动开发技能,驱动 6 子技能 + 评审循环 + 完全无人确认"
  - REQ-00008:"优化 `/code-review`,增加"不传入参数"的整版本模式"
  - REQ-00009:"优化 `/code-unit`,增加"项目可测性"守卫;不可测时跳过 + 看板标记"不适用""
  - REQ-00010:"优化 `/code-it`,增加"前置任务"守卫;按 PLAN.md 登记顺序判定,未完成则中止 + 引导"
  - REQ-00011:"优化 `/code-design` / `/code-plan`,增加"设计目标确认"环节;多问分别细化 + 回写 + 下游传导"
  - REQ-00012:"创建仓库根 README(中英)+ 移动 CLAUDE.md 到根(极简门面 + 详细子文档)"
- 现有 19 个 V0.0.1 任务的"标题"(抽样):
  - `REQ-00001-001`:改 `.claude-plugin/marketplace.json` 根 name
  - `REQ-00001-002`:同步中英 README
  - `REQ-00002-001`:同步 10 个 SKILL.md(只改正文)
  - `REQ-00003-001`:扩展 `code-rule/SKILL.md` 正文
  - ...
- 现有 2 个 V0.0.1 派生任务:
  - `REQ-00001-005`:同步中英 README 中 GitHub URL 仓库名(审查派生)
  - `REQ-00002-009`:同步 PLAN.md 任务总览 + M2 描述(审查派生)
- 现有 0 个 V0.0.1 缺陷(看板"缺陷清单"区段 0 行)
- **关键发现**:所有 19 个 V0.0.1 任务**均已含"标题"**!本需求**不**需"为每个任务生成标题"(已存在),**只**需"让用户交互/看板显示标题"
