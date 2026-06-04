# 关联需求 — REQ-00011

更新时间:2026-06-04 14:47

## 扫描范围
- 同版本:`./assistants/V0.0.2/require/`
  - REQ-00004 / REQ-00005 / REQ-00006 / REQ-00007 / REQ-00008 / REQ-00009 / REQ-00010
- 跨版本:`./assistants/V0.0.1/require/`
- 直接相关:`./assistants/V0.0.1/require/REQ-00003/require/RESULT.md`(type A/B/C 类型识别可参考的"用户确认模式")

## 关联需求清单

### REQ-00007(版本:V0.0.2)— `/code-auto` 自动开发技能
- **关联点**:
  - **被高频调用的子技能**:`code-auto` 在工作流管道中调 `code-design` / `code-plan`(各 1 次)
  - **REQ-00007 Q-4 锁定 A**:`code-auto` 遇 `AskUserQuestion` 时"总选推荐项"(完全无人确认)
  - **本需求冲突**:`code-design` / `code-plan` 触发 `AskUserQuestion` 时,`code-auto` 仍会"总选推荐项"
- **对本需求的影响**:
  - **协同结果**:`code-auto` 调 `code-design` / `code-plan` 时,`AskUserQuestion` 触发 → `code-auto` 选"推荐项" → 无人确认实际发生
  - **影响有限**:本需求主要面向"用户手动调"场景;`code-auto` 场景下"总选推荐项"已是 V0.0.2 既定行为
  - **建议**:本需求**不**触发 `code-auto` 升级;**建议派生**"`code-auto` 升级:识别'设计目标确认'类询问时回传"任务(由用户决定)
- **来源**:`./assistants/V0.0.2/require/REQ-00007/RESULT.md` §FR-3 / §NFR-4

### REQ-00005(版本:V0.0.2)— 优化 3 技能,加首步拉取与末步提交
- **关联点**:
  - **`code-design` / `code-plan` 均在 REQ-00005 改写范围**(增量追加"步骤 0a 拉取"与"末尾兜底提交")
  - **本需求**也修改这 2 个技能,叠加在 REQ-00005 之上
- **对本需求的影响**:
  - **叠加方式**:本需求在 SKILL.md 中**再追加**一个步骤("步骤 0b 设计目标确认"),与 REQ-00005 的"步骤 0a 拉取"并列
  - **结构一致性**:本需求步骤命名沿用 REQ-00005 / REQ-00009 / REQ-00010 的"步骤 0a / 0b"模式
- **来源**:`./assistants/V0.0.2/require/REQ-00005/RESULT.md` §FR-1 / §FR-3

### REQ-00003(版本:V0.0.1)— 优化 `code-rule` 技能
- **关联点**:
  - **"用户确认"模式参考**:REQ-00003 中 `code-rule` 类型识别 FR-7 有"自动+显式"模式(关键词 + 用户追问)
  - **本需求**在 `code-design` / `code-plan` 中增加"显式用户确认"环节,与 `code-rule` FR-7 思路同源
- **对本需求的影响**:
  - **设计模式参考**:本需求可借鉴 REQ-00003 FR-7 的"自动推断 + 显式追问"模式
  - **建议**:本需求落地后,可派生"用 `code-rule` 沉淀 '设计目标' 字段约定" 任务
- **来源**:`./assistants/V0.0.1/require/REQ-00003/RESULT.md` §FR-7

### REQ-00004(版本:V0.0.2)— `/code-dashboard` 开发看板技能
- **关联点**(间接):
  - **`code-dashboard` 不感知**"设计目标"概念
  - **本需求**不修改看板(零规范变更)
- **对本需求的影响**:
  - **不**触发 `code-dashboard` 升级
  - **不**触发 `dashboard-conventions §规则 1`
- **来源**:`./assistants/V0.0.2/require/REQ-00004/RESULT.md` §NFR-5

### REQ-00006(版本:V0.0.2)— `/code-publish` 发布部署技能
- **关联点**(间接):
  - **`code-publish` 不感知**"设计目标"概念
- **对本需求的影响**:
  - **不**触发 `code-publish` 升级
- **来源**:`./assistants/V0.0.2/require/REQ-00006/RESULT.md`

### REQ-00008(版本:V0.0.2)— `/code-review` 整版本模式
- **关联点**(间接):
  - **`code-review` 不感知**"设计目标"概念
  - **本需求不影响** `code-review`
- **来源**:`./assistants/V0.0.2/require/REQ-00008/RESULT.md`

### REQ-00009(版本:V0.0.2)— `/code-unit` 项目可测性守卫
- **关联点**(间接):
  - **`code-unit` 不在改写范围**
- **对本需求的影响**:
  - **不**触发 `code-unit` 升级
- **来源**:`./assistants/V0.0.2/require/REQ-00009/RESULT.md`

### REQ-00010(版本:V0.0.2)— `/code-it` 前置任务守卫
- **关联点**(间接):
  - **`code-it` 不在改写范围**
- **对本需求的影响**:
  - **不**触发 `code-it` 升级
- **来源**:`./assistants/V0.0.2/require/REQ-00010/RESULT.md`

### REQ-00002(版本:V0.0.1)— 编码格式统一
- **关联点**(间接):
  - **本需求不直接产生新编码**
- **对本需求的影响**:
  - **不**影响
- **来源**:`./assistants/V0.0.1/require/REQ-00002/RESULT.md`

### REQ-00001(版本:V0.0.1)— 看板模板
- **关联点**(间接):
  - **本需求不修改看板**
- **对本需求的影响**:
  - **不**触发 `dashboard-conventions §规则 1`
- **来源**:`./assistants/V0.0.1/RESULT.md` 模板

## 跨需求聚合(供 `code-design` 阶段权衡)

| 维度 | 涉及需求 | 共性 | 处理建议 |
| --- | --- | --- | --- |
| 模式协同 | REQ-00007 | `code-auto` 调 `code-design` / `code-plan` 时遇 `AskUserQuestion` 选"推荐项" | 本需求**不**触发 `code-auto` 升级;Q-4 采纳默认 |
| 步骤命名 | REQ-00005 / REQ-00009 / REQ-00010 | "步骤 0a 守卫"模式 | 本需求新增"步骤 0b 设计目标确认" |
| 设计模式 | REQ-00003 | "自动推断+显式追问"模式 | 借鉴 REQ-00003 FR-7 模式 |
| 看板兼容 | REQ-00004 | 现有统计逻辑 | **不**修改看板,零规范变更 |
| 上游 | REQ-00006 | `code-publish` 前置检查 | **不**影响 |
| 评审 | REQ-00008 | `code-review` 整版本模式 | **不**影响 |
| 模式一致性 | REQ-00009 / REQ-00010 | 守卫模式 | 与本需求"步骤 0b"模式协同 |

## V0.0.0 EXISTING-* 任务
- `code-design` / `code-plan` 在 V0.0.0 已存在(7 个 `code-*` 之一/之二),V0.0.1 中所有概要设计 / 详细设计产物均无"用户确认环节"
- 本需求是 V0.0.1 起"`code-design` / `code-plan` 直接设计"模式基础上的"用户确认环节扩展"
- V0.0.0 ~ V0.0.1 中所有 `design/.../RESULT.md` / `plan/.../RESULT.md` 文档均**无**"设计目标"小节 — V0.0.2 之后由本需求支持(增量追加)

## 关键事实扫描结果(供 clarifications.md 引用)
- 现有 `code-design` SKILL.md(2026-06-04 14:47 扫描,需在 code-design 阶段精确读取):含"需求澄清" / "概要设计"等步骤
- 现有 `code-plan` SKILL.md:含"任务拆分" / "任务总览"等步骤
- 现有 3 个 V0.0.1 需求(REQ-00001~00003)的概要设计/详细设计产物:
  - `./assistants/V0.0.1/design/REQ-NNNNN/RESULT.md`
  - `./assistants/V0.0.1/plan/REQ-NNNNN/{RESULT,PLAN}.md`
  - 均**无**"设计目标"小节
- 现有 V0.0.2 需求(REQ-00004~00010)均处于"需求分析"阶段,无设计产物可参考
- `code-auto` 现行 FR-3 / FR-4.AC-4.1 / FR-4.AC-4.3 在"全自动"场景下会"总选推荐项"绕过用户确认
- 看板"需求清单"区段列(V0.0.1 起 11 列)无"设计目标"列
