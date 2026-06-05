# 规范遵循记录 — REQ-00013
更新时间:2026-06-05 21:00
版本:V0.0.2

## 1. 本次参考的规范文件

- `./assistants/rules/skill-conventions.md` §规则 1(frontmatter 必含 name + description)
- `./assistants/rules/module-conventions.md` §规则 1(资源放 `templates/` / `checklists/` / `guidelines/` 子目录)
- `./assistants/rules/directory-conventions.md`(本轮 0 新规则,占位)
- `./assistants/rules/encoding-conventions.md` §规则 1+3(RE/REQ/BUG/TASK 编码格式)
- `./assistants/rules/dashboard-conventions.md` §规则 1(看板字段扩展三方同步)
- `./assistants/rules/doc-conventions.md` §规则 1(中英 README 同次提交 + 章节对仗)
- `./assistants/rules/marketplace-protocol.md`(不动 marketplace.json / plugin.json)
- 其他:`commit-conventions.md` / `dependency-conventions.md` / `framework-conventions.md` / `migration-mapping.md` / `naming-conventions.md` / `coding-style.md`(本轮 0 触发,占位)

## 2. 规范 vs 现状偏离

- **0 项**:本仓库**0**规范-现状偏离。所有规范在本仓库中均已落地。

## 3. 规范 vs 需求冲突

- **0 项**:本需求 100% 沿用既有规范,无冲突点。所有 NFR-1~10 强约束均与规范一致(NFR-2 零规范变更 / NFR-7 frontmatter 不变 / NFR-8 增量修改 / NFR-1 零依赖)。

## 4. 用户授权的偏离

- **0 项**:本需求**0**偏离。设计严守所有 NFR 与上游锁定决策(Q-1~Q-4)。

## 5. 规范变更响应(增量更新时填写)

- N/A(本次为首次设计)

## 6. 关键自检结果

| 规范 | 条款 | 本设计是否满足 | 备注 |
| --- | --- | --- | --- |
| `skill-conventions` | §规则 1 frontmatter 必含 name + description | ✅ | 7 个 SKILL.md 增量追加,**frontmatter 字节级保留**(NFR-7 强约束)|
| `module-conventions` | §规则 1 资源放子目录 | ✅ | 0 新增资源,沿用既有 13 个技能结构 |
| `dashboard-conventions` | §规则 1 看板字段扩展三方同步 | ✅ | 0 触发 — 看板字段不扩展,0 新增/删除/重命名 8 列 |
| `encoding-conventions` | §规则 1+3 编码格式 | ✅ | 0 修改编码格式(本轮不涉及)|
| `doc-conventions` | §规则 1 中英 README 同次提交 | ✅ | 0 修改 README(本轮不涉及 README)|
| `marketplace-protocol` | 不动 marketplace.json / plugin.json | ✅ | 0 修改(本轮不涉及)|

## 7. 与上游锁定决策(Q-1~Q-4)一致性

- **Q-1 锁定**:"从已有内容派生,不新增字段"(零规范变更) — ✅ 本设计严守,标题来源 = `RESULT.md` 第 1 行 / `PLAN.md` "标题"列 / `fix/.../RESULT.md` "## 缺陷标题"(本轮新增)
- **Q-2 锁定**:"`REQ-00001 · 标题`"(中点 `·` 格式) — ✅ 6 技能所有屏幕输出位置采用中点 + 半角空格
- **Q-3 锁定**:"字符数 ≤ 30" — ✅ 共享 `truncateTitle` 工具函数,JavaScript `[...title].slice(0, 30).join('') + '...'`
- **Q-4 锁定**:"本轮升级 6 技能" — ✅ M-1~M-7 + M-8 协同 = 7 个 SKILL.md 增量追加(6 技能 + `code-publish` 协同)
