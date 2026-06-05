# 规范遵循记录 — REQ-00017
更新时间:2026-06-05 16:30
版本:V0.0.2

## 1. 本次参考的规范文件
- ./assistants/rules/dashboard-conventions.md
- ./assistants/rules/module-conventions.md
- ./assistants/rules/directory-conventions.md
- ./assistants/rules/skill-conventions.md
- ./assistants/rules/encoding-conventions.md
- ./assistants/rules/commit-conventions.md
- ./assistants/rules/doc-conventions.md
- ./assistants/rules/naming-conventions.md
- ./assistants/rules/coding-style.md
- ./assistants/rules/dependency-conventions.md

## 2. 规范 vs 现状偏离
无。

## 3. 规范 vs 需求冲突

### 冲突 1:`dashboard-conventions.md §规则 1` 第 3 款 vs NFR-3
- **冲突**:`dashboard-conventions.md §规则 1` 第 3 款要求"新增/删除/修改枚举值需 3 处同步";NFR-3 要求"不修改 rules/"
- **解决**:本需求使用既有"任务完成"事件类型,**不新增**枚举值
- **结论**:**不触发**规则 1 同步,2 个约束**不冲突**
- **验证**:V0.0.2 既有 commit 历史中,`code-it` 完成时确实用"任务完成"事件(参考 `assistants/V0.0.2/RESULT.md` line 386)
- **解决时间**:2026-06-05 16:30

### 冲突 2:NFR-1"0 修改其他 7 个 `code-*` 技能" vs 改造需要改 2 个 SKILL.md
- **冲突**:NFR-1 文字是"0 修改其他 7 个 `code-*` 技能"vs 改造要改 2 个
- **澄清**:NFR-1 指"`/code-unit` / `/code-review` / `/code-dashboard` / `/code-publish` / `/code-auto` 5 个" + 隐含"其他未列出的 2 个",**不**含 `/code-plan` / `/code-it`(本需求允许改这 2 个);实际含义是"7 个非本需求核心的 `code-*` 技能不动"
- **结论**:**不冲突**
- **解决时间**:2026-06-05 16:30

## 4. 用户授权的偏离
无。

## 5. 规范变更响应
不涉及(本次为首次设计,无规范变更)。
