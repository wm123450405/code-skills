# 规范遵循记录 — REQ-00008
更新时间:2026-06-05 16:00
版本:V0.0.2
需求编码:REQ-00008

---

## 1. 本次参考的规范文件

> 13 个文件(7 强约束 + 6 占位 + 1 DEPRECATED 仍引用);与 `design/REQ-00008/rule-compliance.md` 一致,本节简表。

| 规范文件 | 类别 | 状态 | 本详细设计对应章节 |
| --- | --- | --- | --- |
| `skill-conventions.md` | 技能编写 | ✅ 强约束 | §4.1 模块 M-1 — frontmatter 字节级不变(INV-4) |
| `module-conventions.md` | 模块规划(DEPRECATED) | ✅ 强约束(仍引用) | §4.1 SKILL.md 范围限定;0 新增子目录 |
| `dashboard-conventions.md` | 看板 | ✅ 强约束 | §11 看板同步(0 触发 3 处同步) |
| `encoding-conventions.md` | 编码格式 | ✅ 强约束 | §6.2 派生任务字段完全沿用模式 1 既有(INV-3) |
| `marketplace-protocol.md` | Marketplace | ✅ 强约束 | §11.4 0 触发(本需求**不**新增技能) |
| `doc-conventions.md` | 文档 | ✅ 强约束 | §11.4 0 主动写 README(Q-7 采纳默认) |
| `migration-mapping.md` | 编码迁移 | ✅ 强约束(不触发) | (不触发) |
| `directory-conventions.md` | 目录与模块 | ⏸️ 占位 | (不触发) |
| `framework-conventions.md` | 框架选型 | ⏸️ 占位 | (不触发) |
| `naming-conventions.md` | 命名风格 | ⏸️ 占位 | (不触发) |
| `coding-style.md` | 代码风格 | ⏸️ 占位 | (不触发) |
| `commit-conventions.md` | 提交合并 | ⏸️ 占位 | (不触发) |
| `dependency-conventions.md` | 三方依赖 | ⏸️ 占位 | (不触发) |

---

## 2. 规范 vs 现状偏离

**无**。本详细设计**严格遵循**所有有效约束:
- 既有 `code-review` 技能已存在(无新增技能 → `skill-conventions §规则 1` 仅"保持 frontmatter 不变"约束,本设计不触)
- 既有资源(3 模板 + 1 清单)全部在 `templates/` / `checklists/` 固定子目录 → `module-conventions §规则 1` 不触
- 本设计**不扩展**看板字段 → `dashboard-conventions §规则 1` 3 处同步不触
- 派生任务编码**不**由本设计生成(沿用 `code-plan` 既有规则 + `encoding-conventions §规则 4`)→ 不触
- 本设计**不**修改 `marketplace.json` / `plugin.json` / 其他 9 个 SKILL.md → `marketplace-protocol §规则 1` 不触
- 本设计**不**写 README(`code-rule` 沉淀,Q-7 采纳默认)→ `doc-conventions §规则 1-2` 不触
- 派生任务的"关联任务" / "触发/来源"列沿用 `code-review` 既有字段名 → `encoding-conventions §规则 1` 不触

---

## 3. 规范 vs 需求 / 设计冲突

**无冲突**。本需求是"`code-review` 既有技能的优化扩展",无字段约定扩展 / 编码约定扩展 / 资源目录扩展。

本详细设计阶段**无新增规范冲突**。

---

## 4. 用户授权的偏离

**无**。本详细设计 100% 合规。

---

## 5. 规范变更响应(增量更新时填写)

> 本次为首次详细设计(v1),无规范变更触发。后续增量更新时,需重新 `Glob "./assistants/rules/**/*"` 与本表对比,识别新增/修改/删除的规范文件,任何触发的设计修订都需在本表追加记录。

---

## 6. 规范自检结论

- **完全合规的章节**:§1 / §2 / §3 / §4 / §5 / §6 / §7 / §8 / §9 / §10 / §11 / §12(全部 12 个 RESULT.md 主章节)
- **经用户授权偏离的章节**:**0**
- **待澄清冲突**:**0**
- **建议派生(不影响本设计)**:
  - Q-8.1:用 `code-rule` 沉淀 `review-conventions.md`(整版本模式的检查清单)— **不阻塞**,留作 follow-up
  - Q-8.2:把 `code-review` 加入 REQ-00005 的"首步拉取+末步提交"改写范围 — **不阻塞**,留作 follow-up
  - Q-8.3:在 `code-review/templates/` 新增 `REVIEW-ALL.md` 模板 — **本设计倾向不新增**(D-1.B);由 `code-plan` 决定
- **13 项 INV 全部满足**(INV-1 ~ INV-13)
- **8 类风险全部有缓解**(R-1 ~ R-8)
