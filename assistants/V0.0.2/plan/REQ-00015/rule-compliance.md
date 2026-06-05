# 规范遵循记录 — REQ-00015
更新时间:2026-06-06 09:10
版本:V0.0.2

## 1. 本次参考的规范文件(13 份,全部)
详 `materials-index.md` 第 1 节。

## 2. 规范 vs 现状偏离
**0 项偏离**:
- 本需求是纯新增技能,**不**改既有 11 个 `code-*` SKILL.md / `assistants/rules/` / `marketplace.json` 既有字段

## 3. 规范 vs 需求冲突
**0 项冲突**:
- `marketplace-protocol.md §规则 1` vs FR-NFR-6:`marketplace.json` 需追加 `./skills/code-merge` → **一致**(本设计 INV-2 保证)
- `skill-conventions.md §规则 1` vs FR-NFR-1:新 SKILL.md frontmatter 必含 name + description → **一致**(本设计模块拆分保证)
- `encoding-conventions.md §规则 3` vs FR-6 看板自检:任务编码解析 → **一致**(本设计复用既有解析)
- `dashboard-conventions.md §规则 1` vs FR-6 看板自检:不触发 3 文件同步 → **一致**(本设计复用既有 5 区段,**不**扩展字段)

## 4. 用户授权的偏离
**0 项用户授权的偏离**(本设计严守所有规范)

## 5. 规范变更响应(增量更新时填写)
**不适用**(本需求是首次规划,非增量更新)

## 6. 任务级 INV 自检
| 任务 | INV-1 | INV-2 | INV-3 | INV-4 | INV-5 | INV-6 | INV-7 | INV-8 | INV-9 | INV-10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T-001 写 SKILL.md | ✅ 0 改其他 | ✅ 0 改 marketplace | ✅ 0 改 plugin | ✅ 0 改 rules | ✅ 0 --squash | ✅ 0 auto push | ✅ 0 follow-up | ✅ 0 git 模板 | ✅ 0 调子技能 | ✅ worktree 强约束 |
| T-002 改 marketplace.json | ✅ | ✅ +1 项 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| T-003 改 README | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| T-004 同步看板 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| T-005 自检 + 收尾 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**所有任务 INV 全通过** —— 0 违反 / 0 偏离

## 7. 与 REQ-00013 的协同
- REQ-00013 INV-1(8 个 SKILL.md 既有 frontmatter / 章节字节级保留)→ 本设计严守(NFR-5 + INV-1,**不**修改既有 11 个 SKILL.md)
- REQ-00013 INV-5(0 触发 `dashboard-conventions §规则 1` 3 处同步)→ 本设计严守(看板字段**不**扩展,FR-6 复用既有 5 区段)
- REQ-00013 INV-6(0 修改 `marketplace.json` / `plugin.json` / `assistants/rules/`)→ 本设计严守(仅追加 `marketplace.json` 的 `./skills/code-merge` 项,**不**触碰其他字段,符合 NFR-6)

## 8. 与 REQ-00017 的协同
- REQ-00017 强约束:0 拆"更新看板"派生任务 → 本设计严守(5 任务的"触发/来源"全部 = `详细设计`)
- REQ-00017 P-1 推进看板:`/code-it` 末尾兜底后 P-1 小步自行推进本任务看板状态 → 本设计**沿用**(每个 `code-it` 任务完成后,`code-it` 自行推进看板,**不**通过派生任务)

## 9. 拆任务约束检查(REQ-00017 强约束)
- [x] 5 任务的"触发/来源"列**全部** = `详细设计`
- [x] 5 任务的"实际产出"**全部** ∈ `{代码改写, 测试编写, 文档改写, 数据迁移, 配置变更, 部署脚本}` 候选集
- [x] 5 任务**不**含"看板更新" / "文档评审" / "任务分配" 等纯协调/汇报类
- [x] 看板推进职责由 `/code-it` 末尾兜底后 P-1 小步承担
