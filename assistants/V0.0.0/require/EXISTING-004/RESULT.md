# 现有功能需求 — EXISTING-004:需求分析(code-require)

> 本文档由 `code-init` 技能基于项目现有代码生成。
> 描述的是"**代码中已实现**"的功能,而非待开发的功能。
> 未来对该功能的**修改**应通过 `code-require`(增量更新本文件)进行。
> 最后更新:2026-06-03 18:10
> 适用版本:基线版本 `V0.0.0`

## 需求概述
`code-require` 是主流程的**第二步**(版本感知):接收用户提供的"需求编码"(如 `REQ-YYYY-NNNN`),从 `./assistants/<版本号>/require/<需求编码>/` 目录读取所有前置材料(需求文档/设计稿/会议记录/录音/...)分析并产出 `RESULT.md` 需求提示词文档;若 RESULT.md 已存在则做增量更新。同步追加/更新版本看板的"需求清单"与"变更记录"区段。

## 现有实现位置

| 维度 | 位置 |
| --- | --- |
| 主要文件 | `plugins/code-skills/skills/code-require/SKILL.md`(294 行) |
| 关键函数/类 | (N/A) |
| 涉及文件数 | 3(SKILL.md + 2 个模板) |
| 大致代码量 | 约 340 行 |

### 关键代码位置(可选)
- `plugins/code-skills/skills/code-require/SKILL.md` — 工作流(读 .current-version → 校验需求编码与目录 → 扫材料 → 分析 → 写 RESULT.md → 更新看板)
- `plugins/code-skills/skills/code-require/templates/requirements.md` — 需求提示词文档模板
- `plugins/code-skills/skills/code-require/templates/assistants-layout.md`

## 用户角色与场景

### 角色
- **产品/项目负责人**:新需求澄清、需求变更、跨模块需求对齐

### 场景
- 新功能/新模块的首次需求澄清
- 现有功能的重大变更
- 跨模块/跨系统的需求对齐
- 已有 RESULT.md,追加新材料做增量更新

## 功能点(FR)

- **FR-1**:读 `.current-version` 确认激活版本;若无,提示调 `code-version`
- **FR-2**:接收需求编码(交互式或参数),校验格式与目录存在性
- **FR-3**:扫描 `./assistants/<版本号>/require/<需求编码>/` 下所有前置材料(.md/.docx/.pdf/.png/.jpg/.mp3/.wav/.m4a/.mp4/聊天记录/邮件 等)
- **FR-4**:分析材料,产出"需求提示词文档"(基于 `requirements.md` 模板,含概述/角色/场景/FR/接口/数据模型/AC/关联/限制)
- **FR-5**:`RESULT.md` 已存在时,基于新材料做**增量更新**而非覆写
- **FR-6**:在 `<版本号>/RESULT.md` 看板追加"需求清单"行(若新建)或更新该行(若变更/撤回)
- **FR-7**:在"变更记录"追加条目
- **FR-8**:引导用户:调 `code-design` 继续

## 关键接口

### CLI
```
/code-skills:code-require REQ-2026-0001
/code-skills:code-require       # 交互式
```

### 输入
- `./assistants/<版本号>/require/<需求编码>/` 目录下用户预先放的需求材料

### 写入
- `./assistants/<版本号>/require/<需求编码>/RESULT.md` — 需求提示词文档
- `./assistants/<版本号>/RESULT.md` — 看板"需求清单" + "变更记录"

## 数据模型(若适用)

| 实体 | 字段 | 约束 |
| --- | --- | --- |
| 需求编码 | `REQ-YYYY-NNNN` | 4 位顺序号,同年内唯一 |
| 需求目录 | `require/<需求编码>/` | 必含 RESULT.md;前置材料由用户预先放入 |
| 需求状态 | 待开始/进行中/已完成/已取消/阻塞 | 看板字段,6 个枚举 |
| 需求模板字段 | 概述/角色/场景/FR-N/接口/数据模型/AC-N/关联/限制/变更记录 | 由 `requirements.md` 定义 |

## 验收标准(AC)

- **AC-1**:无 `.current-version` 时,`code-require` 立即中止并提示调 `code-version`
- **AC-2**:`require/<需求编码>/RESULT.md` 不存在时,基于前置材料生成(新需求)
- **AC-3**:`RESULT.md` 已存在 + 追加新材料 → 增量更新,**不**覆盖已有内容
- **AC-4**:版本看板"需求清单"新增一行(新需求)或更新状态(变更)
- **AC-5**:版本看板"变更记录"追加"需求新增"或"需求变更"条目
- **AC-6**:需求编码格式校验拒绝非 `REQ-YYYY-NNNN` 的输入

## 关联功能

| 关联编码 | 关联点 | 影响 |
| --- | --- | --- |
| EXISTING-002 | `code-version` 是前置门 | 必须先有激活版本 |
| EXISTING-003 | 读 `rules/` 作为约束 | 规范空时退化为无约束模式 |
| EXISTING-005 | `code-design` 读 `require/<id>/RESULT.md` 作为输入 | 需 `code-require` 完成才能进 `code-design` |
| EXISTING-001 | `code-init` 生成的 `EXISTING-NNN` 格式与 `REQ-YYYY-NNNN` 对齐 | 未来对 `EXISTING-NNN` 的修改可走 `code-require` 增量 |

## 已知限制/技术债

- 不解析二进制文件(.docx/.pdf/.mp3 等),只能"识别存在"与"建议 AI 主动读"
- "增量更新"靠 AI 自主判断,缺少 diff 工具防止误覆盖
- 需求编码全局唯一(同年内),不支持同一年内的版本化(`REQ-2026-0001-v2`)

## 变更记录

| 时间 | 变更类型 | 变更摘要 | 关联项 |
| --- | --- | --- | --- |
| 2026-06-03 18:10 | 需求登记 | code-init 识别并登记现有功能 EXISTING-004 | EXISTING-004 |
