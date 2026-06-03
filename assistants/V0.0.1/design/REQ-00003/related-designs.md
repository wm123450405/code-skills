# 关联设计 — REQ-00003
版本:V0.0.1

## 跨版本关联

### V0.0.0/require/EXISTING-003 — code-rule 基线
- **关联点**:`code-rule` 技能的基线能力定义(只支持 Type A 规则)
- **对本设计的影响**:
  - 本需求**扩展**该基线,行为兼容(FR-8 + NFR-1)
  - **不重写** EXISTING-003 中的任何内容
  - 实施时:`code-rule/SKILL.md` 在现有 9 步骤流程基础上扩展,不删除任何已有步骤
- **链接**:`./assistants/V0.0.0/require/EXISTING-003/RESULT.md`

### V0.0.0/require/EXISTING-001 ~ 010(基线 EXISTING 整体)
- **关联点**:V0.0.0 基线的 8 个 EXISTING-XXX 需求(已冻结)
- **对本设计的影响**:**无** — 本需求不修改基线任何内容
- **链接**:`./assistants/V0.0.0/require/EXISTING-XXX/RESULT.md`

## 同版本关联

### V0.0.1/require/REQ-00001 — Marketplace 改名
- **关联点**:`code-rule` 规则分类的"文件命名"在 REQ-00001 前后可能不同
- **对本设计的影响**:
  - REQ-00001 已落地:`.claude-plugin/marketplace.json` 根 name = `code-skills-marketplace`
  - 本需求**不涉及** marketplace 命名,无冲突
  - 实施时,新分类文件命名使用小写连字符(如 `coding-style.md`),与 REQ-00002 编码格式统一兼容
- **链接**:`./assistants/V0.0.1/require/REQ-00001/RESULT.md`

### V0.0.1/require/REQ-00002 — 编码格式统一
- **关联点**:本需求新建的 6 个 `*.md` 文件需符合 REQ-00002 的新编码格式(若 REQ-00002 已落地)
- **对本设计的影响**:
  - REQ-00002 状态:已 plan(本设计 21:00 时,V0.0.1 已完成 REQ-00002 的 plan 阶段)
  - REQ-00002 实施后,本需求涉及的所有文件路径(无编码)无需变更
  - **依赖**:本需求**应在** REQ-00002 code-it 实施**之后**执行,以确保文件命名格式与新规范一致
- **链接**:`./assistants/V0.0.1/require/REQ-00002/RESULT.md` + `plan/REQ-00002/PLAN.md`

### V0.0.1/require/REQ-00003 — 本需求
- (本节自指,无外部关联)

## 关联模块(`code-rule` 内部)

### code-rule/SKILL.md 步骤 4 关键词表
- **关联点**:现有 11 个分类关键词(架构/模块规划/命名约定/错误处理/接口定义/数据结构/安全/性能/测试/可观测性/提交规范)
- **对本设计的影响**:
  - 本需求**不删除**任何旧关键词
  - 本需求**新增** 6 个核心分类关键词 + 明确 4 个保留专项
  - 旧关键词中的"命名约定"映射到 C-3(naming-conventions);"提交规范"映射到 C-6(commit-conventions);等等
  - **行为兼容**:用户说"命名规范" → 旧版:归类到"naming.md"(可能不存在);新版:归类到 C-3 naming-conventions.md(本需求新建)
  - **差异**:文件路径变更,但分类语义不变
- **风险**:若有外部脚本依赖旧路径,会失败
- **缓解**:本仓库为内部插件,无外部脚本依赖

### code-rule/templates/rule.md
- **关联点**:规则小节标准结构(8 字段)
- **对本设计的影响**:
  - 本需求在 `rule.md` 头部追加"占位模式" + "引导模式"说明
  - **不修改**现有 8 字段结构
  - Type A 现有规则内容不受影响
- **风险**:无

## 共享约束(项目级规范)

### skill-conventions.md §规则 1
- **关联点**:SKILL.md frontmatter 必含 `name` + `description` 且与目录名一致
- **对本设计的影响**:
  - 本需求**修改** `code-rule/SKILL.md` 正文,但 frontmatter **不变**
  - 修改 description 字段(描述"3 种类型")?—— 本设计**决策**:**不改** description(只改正文,避免触发其他技能)
  - 理由:`code-rule` description 已被 9 个其他技能识别为"读取规范",本需求扩展其能力不需改 description
- **风险**:若有用户依赖现有 description 触发决策,本设计保持 description 不变 → 兼容

### doc-conventions.md §规则 1 + 规则 2
- **关联点**:README 多语言对仗 + 仓库级使用说明文档
- **对本设计的影响**:
  - 本需求**不修改** `plugins/code-skills/README.md` / `README.en.md`
  - **不修改** 5 个现有规范文件(4 保留 + 1 弃用)
- **风险**:无

## 关联总结

| 关联项 | 方向 | 关系强度 | 冲突风险 |
| --- | --- | --- | --- |
| V0.0.0/EXISTING-003 | 上游 | 强(基线) | 低(向后兼容) |
| V0.0.1/REQ-00001 | 同版本 | 弱(命名无关) | 无 |
| V0.0.1/REQ-00002 | 同版本 | 中(执行顺序) | 中(应 REQ-00002 之后) |
| code-rule/SKILL.md(现有) | 内部 | 强(扩展) | 低(向后兼容) |
| code-rule/templates/rule.md | 内部 | 中(扩展) | 低(头部追加) |
| 9 个其他 SKILL.md | 内部 | 弱(只读约束) | 无(本需求不修改) |
| 5 个现有规范文件 | 内部 | 中(4 保留 + 1 弃用) | 低(只追加不修改) |
| skill-conventions §规则 1 | 项目级 | 中(frontmatter 边界) | 低(不改 frontmatter) |
| doc-conventions §规则 1/2 | 项目级 | 弱(不修改 README) | 无 |
