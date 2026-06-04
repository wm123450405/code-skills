# 关联需求 — REQ-00006

更新时间:2026-06-04 13:44

## 扫描范围
- 同版本:`./assistants/V0.0.2/require/`
  - REQ-00004 / REQ-00005
- 跨版本:`./assistants/V0.0.1/require/`、`./assistants/V0.0.0/`
- 关联目录:`./assistants/qanda/`(用户原文引用,**当前不存在**)

## 关联需求清单

### REQ-00004(版本:V0.0.2)— `/code-dashboard` 开发看板技能
- **关联点**:
  - **同一数据源**:`code-dashboard` 与 `code-publish` 都消费 `./assistants/<版本号>/RESULT.md` 的 3 大区段(需求/任务/缺陷清单)
  - **本需求是"检查全部解决",`code-dashboard` 是"展示全部状态"** — 互为表里
  - **`code-dashboard` 的"下一步建议"段**已隐式暗示 `code-publish` 存在:
    > V0.0.1 看板"FR-4 优先级策略":
    > - **全完成** → `该版本已全部完成,可发布/归档` + 提示调 `code-version <新版本号>`
  - 即原 `code-dashboard` FR-4 的"全完成"分支**未直接**调 `code-publish`,本需求落地后,该分支应升级为"建议执行 `/code-publish`"
- **对本需求的影响**:
  - **数据格式兼容**:`code-publish` 检查时也应**同**消费同一看板结构,否则会出现"dashboard 显示全完成,publish 却报有未完成"
  - **判定阈值对齐**:`code-publish` 的"解决状态"判定必须**等于或严于** `code-dashboard` 的"真正可发布"定义
  - **建议派生**:在 `code-review REQ-00006` 阶段,可派生"`code-dashboard` 升级'全完成'建议为 `code-publish`"作为 follow-up 任务
- **来源**:`./assistants/V0.0.2/require/REQ-00004/RESULT.md` §FR-4 + §NFR-3(任务编号格式兼容)

### REQ-00005(版本:V0.0.2)— 优化 3 技能,加首步拉取与末步提交
- **关联点**:
  - **`code-publish` 与 `code-require` / `code-design` / `code-plan` 并列**为"管道第 5 步"(在 `code-review` 之后,`code-version` 之前)
  - **`code-publish` 也应享受** REQ-00005 提议的"首步拉取"与"末步提交"能力 — 但本需求是"独立"需求,需要在文档中**显式说明**:`code-publish` 不在 REQ-00005 改写范围内
- **对本需求的影响**:
  - **不在 REQ-00005 改写范围**:本需求只**消费** REQ-00005 的成果(在新鲜上下文中工作),不**反向**改写 REQ-00005 的边界
  - **建议派生**:可在 `code-review REQ-00006` 阶段派生"把 `code-publish` 也加入 REQ-00005 的'首步拉取+末步提交'3 技能之一"任务(由用户决定是否合入 v2)
  - **直接影响**:`code-publish` 自身**不**自动包含"首步拉取"(本需求范围外);但用户在执行本技能前**应**已处于"最新"上下文(由 REQ-00005 之后的会话状态保证)
- **来源**:`./assistants/V0.0.2/require/REQ-00005/RESULT.md` §FR-1 / §FR-3

### REQ-00001(版本:V0.0.1)— Marketplace 改名落地(里程碑 M1)
- **关联点**:
  - **里程碑定义的历史样本**:V0.0.1 看板"里程碑"段定义了"M1: Marketplace 改名落地"等 4 个里程碑,每个有"完成定义"
  - **M1 的完成定义 = "4 任务开发=已完成 ∧ 1 个 commit 已落地"** — 这是"任务清单区段'真正可发布' = 0 / 4"的间接表达
  - **`code-publish` 的"前置检查"实质上是"V0.0.x 全部里程碑均达完成定义"** 的自动化
- **对本需求的影响**:
  - **里程碑字段复用**:本需求的前置检查除了看板 3 大区段外,**应**叠加看板"里程碑"区段的"完成定义"判定
  - **决策点(待澄清)**:本需求的"全部解决"是否含"里程碑完成"?见 clarifications.md Q-6
- **来源**:`./assistants/V0.0.1/RESULT.md` "里程碑"段

### REQ-00003(版本:V0.0.1)— 优化 `code-rule` 技能
- **关联点**:
  - **`code-rule` 是规范唯一入口**:本需求新增 `publish/` 与 `qanda/` 两个**项目级共享目录**;若未来需要"发布规范"沉淀,应由 `code-rule` 维护
  - **CLAUDE.md "AI 工作约定"**:本需求落地的"前置检查逻辑"也可作为 AI 工作约定,后续可由 `code-rule` 沉淀
- **对本需求的影响**:
  - **不直接写规范**:本需求不创建 `publish-conventions.md` 之类的规范文件
  - **建议**:本需求评审时,可派生"用 `code-rule` 沉淀 `publish-conventions.md`"任务(类似 REQ-00001-005 / REQ-00002-009)
- **来源**:`./assistants/V0.0.1/require/REQ-00003/RESULT.md` + `commit-conventions.md`(占位)

### REQ-00002(版本:V0.0.1)— 编码格式统一
- **关联点**(间接):
  - **`encoding-conventions.md §规则 1`**:3 类编码权威源
  - **`code-publish` 产出的 commit 引用**:`publish/DEPLOY.md` 末尾的"提交哈希"应符合既有 commit 格式
- **对本需求的影响**:
  - **不强相关**:本需求主要是"消费看板 + 写文档",不直接产生新编码
  - **边界**:本需求不修改 `encoding-conventions.md`
- **来源**:`./assistants/V0.0.1/require/REQ-00002/RESULT.md`

## 跨需求聚合(供 `code-design` 阶段权衡)

| 维度 | 涉及需求 | 共性 | 处理建议 |
| --- | --- | --- | --- |
| 数据源对齐 | REQ-00004 | 同一看板 3 大区段 | `code-publish` 与 `code-dashboard` 共用同一解析规则(强一致) |
| 上下游 | REQ-00005 | `code-publish` 不在 REQ-00005 改写范围 | 本需求**只**消费 REQ-00005 后的会话状态,不**反向**改写 |
| 里程碑 | REQ-00001 | 看板"里程碑"段含"完成定义" | 本需求前置检查应**叠加**"所有里程碑=已完成"(Q-6 待定) |
| 规范沉淀 | REQ-00003 | 项目级规范由 `code-rule` 维护 | 本需求不直接写规范,留作 follow-up |

## V0.0.0 EXISTING-* 任务
- 项目级 `qanda/` 与 `publish/` 目录在 V0.0.0 不存在(无 EXISTING 任务)
- 本需求是 V0.0.2 中**首次引入**这两类目录结构的需求
- 与 `code-skills` 项目结构(工具集,无 DB)的边界:本仓库**不**是被发布的"软件",`code-publish` 实际发布的是**用户用本工具开发的项目**(跨仓库概念)

## 关键事实扫描结果(供 clarifications.md 引用)
- `assistants/qanda/` 目录在 2026-06-04 13:44 扫描时**不存在**(`ls` 返回 No such file)
- `assistants/V0.0.0/.../publish/` 不存在(无历史发布产物可参考)
- `assistants/V0.0.1/.../publish/` 不存在(同上)
- 看板"任务清单"区段含"真正可发布"概念(V0.0.1 看板 §"任务清单"末行统计) — 这是本需求"任务解决"判定的现成锚点
