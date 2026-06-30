# 缺陷分析 — BUG-00002 · REQ-00044 重构后项目使用说明文档未更新

> 所属版本:V0.0.5
> 创建时间:2026-06-30 21:00

## 1. 缺陷描述

REQ-00044 将 14 个旧技能重构为 7 个新技能后,`plugins/code-skills/README.md` 和 `README.en.md` 仍描述旧技能体系(14 个技能、旧目录结构、旧命令名),与当前实际代码完全不一致。同时,编码规范中缺少"技能变更时须同步更新使用说明文档"的强制要求,导致各技能在修改流程逻辑时不会主动更新 README。

**严重程度**:高(用户无法通过 README 了解当前正确的使用方式)

## 2. 触发条件

1. REQ-00044 重构技能后,未更新 README
2. 编码规范 `doc-conventions.md` 中缺少"技能变更→文档同步"的强制条款
3. 各技能的 SKILL.md 中缺少"修改流程逻辑后须更新 README"的提示

## 3. 可能成因

### 根因 1: doc-conventions.md 缺少"技能变更→文档同步"规则

`doc-conventions.md` 规则 2 要求 README 必须存在且持续维护,但未明确"当技能目录、技能名、工作流发生变化时,README 必须同步更新"。这导致 REQ-00044 重构时,AI 未将 README 更新纳入任务范围。

### 根因 2: README 内容严重过时

两个 README 文件描述的是 14 个旧技能、旧目录结构、旧命令名,与当前 7 个新技能完全不匹配。具体过时内容:
- 技能概览表列出 13 个旧技能(code-init/code-version/code-rule/code-require/code-design/code-plan/code-it/code-fix/code-check/code-publish/code-dashboard/code-auto/code-merge),实际只有 7 个
- 工作流管道描述旧 5 段式(code-version→code-require→code-design→code-plan→code-it→code-check),实际已合并为 code-ver→code-req
- 仓库结构树展示旧技能目录(code-init/code-require/code-design/code-plan/code-it/code-check/code-auto/code-publish 等),实际已删除
- 命令参考列举旧命令(/code-require/code-design/code-plan/code-it/code-check 等),实际已合并为 /code-req
- 使用说明描述逐个调用旧技能,实际已合并为单入口 /code-req

### 根因 3: 各技能未强制读取编码规范

部分技能(如 code-ver)的 SKILL.md 中未明确要求"在修改流程逻辑时读取 doc-conventions.md 并检查是否需要更新 README",导致技能变更时 README 遗漏。

## 4. 影响范围

- `assistants/rules/doc-conventions.md`:需新增"规则 3:技能变更时须同步更新 README"
- `plugins/code-skills/README.md`:需全面重写为 7 技能体系
- `plugins/code-skills/README.en.md`:需同步重写
- `plugins/code-skills/skills/code-req/references/languages/*.md`:语言文件中须增加"读取编码规范"的说明
- 各技能 SKILL.md:检查是否明确要求读取编码规范

## 5. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-06-30 21:00 | v1 | 初始创建 | 缺陷登记完成 | wangmiao |