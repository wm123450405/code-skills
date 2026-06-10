# 规范遵循记录 — REQ-00029
更新时间:2026-06-10 11:30
版本:V0.0.3

## 1. 本次参考的规范文件

- `./assistants/rules/skill-conventions.md`(SKILL.md frontmatter 字节级保留)
- `./assistants/rules/module-conventions.md`(技能资源摆放)
- `./assistants/rules/dashboard-conventions.md`(看板字段三方同步)
- `./assistants/rules/doc-conventions.md`(文档格式)
- `./assistants/rules/encoding-conventions.md`(任务编号正则)
- `./assistants/rules/naming-conventions.md`(命名约定)
- `./assistants/rules/coding-style.md`(编码风格)
- `./assistants/rules/commit-conventions.md`(提交约定)
- `./assistants/rules/directory-conventions.md`(目录约定)

## 2. 规范 vs 现状偏离

**无偏离**。本需求 0 改其他 SKILL.md / 0 改 rules / 0 改 CLAUDE.md / 0 改 marketplace.json / 0 改 plugin.json。

## 3. 规范 vs 需求冲突

**无冲突**。本需求是"渲染层瘦身",所有 FR / NFR 均与既有规范兼容:
- NFR-1 "算法 1/2/3/4/5 字节级保留" → 本需求 0 改算法
- NFR-2 "不改其他 10 个 `code-*` 技能 SKILL.md frontmatter" → 本需求 0 改其他技能
- NFR-6 "5 段结构不删,只压缩" → 本需求保留 5 段结构(需求模式)
- NFR-7 "工具集 0 改" → 本需求 0 改工具集

## 4. 用户授权的偏离

**无**。所有改造均在既有规范框架内。

## 5. 规范变更响应

**不适用**(首次设计,非增量更新)。

## 6. 关键不变量(摘要)

| 编号 | 不变量 | 来源 |
| --- | --- | --- |
| INV-1 | code-dashboard/SKILL.md frontmatter 0 修改 | `skill-conventions.md §规则 1` |
| INV-2 | 算法 1/2/3/4 字节级保留 | NFR-1 |
| INV-3 | 算法 5(ASCII 比例条)字节级保留 | NFR-1 |
| INV-4 | 看板 RESULT.md 字段 0 修改 | `dashboard-conventions.md §规则 1`(避免触发三方同步) |
| INV-5 | 其他 10 个 `code-*` 技能 SKILL.md 0 修改 | NFR-2 |
| INV-6 | `marketplace.json` / `plugin.json` / `CLAUDE.md` / `./assistants/rules/` 0 修改 | NFR-2 |
| INV-7 | code-dashboard 工具集不变(只 Read/Glob/Grep) | NFR-7 |