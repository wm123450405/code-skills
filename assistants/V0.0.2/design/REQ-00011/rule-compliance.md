# 规范遵循记录 — REQ-00011

更新时间:2026-06-05
版本:V0.0.2

## 1. 本次参考的规范文件

- `./assistants/rules/skill-conventions.md`
- `./assistants/rules/module-conventions.md`(已 DEPRECATED,仅作历史参考)
- `./assistants/rules/directory-conventions.md`
- `./assistants/rules/dashboard-conventions.md`
- `./assistants/rules/encoding-conventions.md`(本需求不产生新编码,仅作约束参考)
- `./assistants/rules/migration-mapping.md`(本需求不涉及编码迁移)
- `./assistants/rules/commit-conventions.md`(本需求不填该规则)
- `./assistants/rules/doc-conventions.md`
- `./assistants/rules/marketplace-protocol.md`
- `./assistants/rules/coding-style.md`
- `./assistants/rules/framework-conventions.md`
- `./assistants/rules/dependency-conventions.md`
- `./assistants/rules/naming-conventions.md`

## 2. 规范 vs 现状偏离

**无**。`code-design` / `code-plan` 现行 SKILL.md **完全合规**所有适用规范(因规范大多为"待添加"状态);本需求**仅**增量追加"步骤 0b",不改既有章节。

## 3. 规范 vs 需求冲突

**无**。本需求**不**修改任何规范文件(FR-8.AC-8.1 ~ AC-8.4 强约束),也**不**修改看板(FR-8.AC-8.2),因此**不**触发 `dashboard-conventions §规则 1` 3 处同步(NFR-4 强约束)。

## 4. 用户授权的偏离

**无**。本需求**无**对规范的偏离 — 所有规范都**完全合规**;`code-auto` 沿用现行"总选推荐项"行为(NFR-5 强约束)。

## 5. 规范变更响应(增量更新时填写)

**不适用**(本需求为首次设计,非增量更新;V0.0.2 之后如有规范变更触发的本设计修订,在此追加)。

## 自检结论

### 完全合规的章节(所有章节)
- §1 设计目标与范围
- §2 现状与改造点
- §3 关键设计决策(D-1 ~ D-8)
- §4 模块拆分
- §5 接口与数据结构
- §6 三方依赖(0 新增)
- §7 集成点
- §8 风险与缓解
- §9 备选方案
- §10 关联概要设计
- §11 待澄清 / 未决项
- §12 变更记录

### 关键合规点
- **skill-conventions.md §规则 1**:SKILL.md 必含 name + description,frontmatter 不变 → 2 个技能 SKILL.md frontmatter 不动(INV-1)
- **module-conventions.md §规则 1**:资源放技能子目录 `templates/` / `checklists/` / `guidelines/` → 2 个 `templates/*.md` 顶部预留位(已在子目录内,不改位置)
- **dashboard-conventions.md §规则 1**:看板字段扩展需 3 处同步 → 本需求**不**改看板,触发条件不成立(NFR-4)
- **marketplace-protocol.md §规则 1**:marketplace 与 plugin 协议清单 → 本需求**不**改 marketplace.json / plugin.json(FR-8.AC-8.1)
- **doc-conventions.md §规则 1-2**:README 多语言对仗 + 完整性 → 本需求**不**改 README(FR-8.AC-8.4)
- **commit-conventions.md §规则 1**:(待添加)→ 本需求**不**填该规则(FR-8.AC-8.3)
- **encoding-conventions.md §规则 1-3**:3 类编码权威源 → 本需求**不**产生新编码
- **dependency-conventions.md §规则 1**:(待添加);NFR-1 零新增依赖 → 本需求无新增依赖
- **NFR-5**:`code-auto` 沿用现行"总选推荐项"行为;**不**触发 `code-auto` 升级
- **NFR-6**:"步骤 0b"命名沿用"步骤 0a"模式(与 REQ-00005 / REQ-00009 / REQ-00010 模式一致)

## 强制性结论

**本设计 0 处规范偏离,0 处用户授权偏离,0 处待澄清冲突** — 满足本轮所有强制约束。
