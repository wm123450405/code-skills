# 规范遵循记录 — REQ-00016
更新时间:2026-06-05 16:15
版本:V0.0.2

---

## 1. 本次参考的规范文件

| 规范文件 | 状态 | 本详细设计对应章节 |
| --- | --- | --- |
| `skill-conventions.md` | ✅ 强约束 | §4.1 模块 M-1 + §4.2 INV-4(frontmatter 字节级保留) |
| `module-conventions.md` | ✅ 强约束(DEPRECATED 仍引用) | §4.1 0 新增子目录 |
| `dashboard-conventions.md` | ✅ 强约束 | §11 看板同步(0 触发 3 处同步) |
| `encoding-conventions.md` | ✅ 强约束 | §6.2 0 触发(本设计**不**产生新编码) |
| `marketplace-protocol.md` | ✅ 强约束 | §11.4 0 触发 |
| `doc-conventions.md` | ✅ 强约束 | §11.4 0 主动写 README |
| `migration-mapping.md` | ✅ 强约束(不触发) | (不触发) |
| 6 占位 | ⏸️ 占位 | (不触发) |

---

## 2. 规范 vs 现状偏离

**无**。本详细设计**严格遵循**所有有效约束:
- 既有 `code-design` / `code-plan` 技能已存在(无新增技能 → `skill-conventions §规则 1` 仅"保持 frontmatter 不变"约束,本设计**不**改)
- 既有资源(模板 + 清单)全部在 `templates/` / `checklists/` 固定子目录 → `module-conventions §规则 1` 不触
- 本设计**不扩展**看板字段 → `dashboard-conventions §规则 1` 3 处同步不触
- 本设计**不**修改 `marketplace.json` / `plugin.json` / 其他 11 个 SKILL.md → `marketplace-protocol §规则 1` 不触
- 本设计**不**写 README(`code-rule` 沉淀)→ `doc-conventions §规则 1-2` 不触

---

## 3. 规范 vs 需求 / 设计冲突

**无冲突**。本需求是"`code-design` / `code-plan` 既有技能的优化扩展",无字段约定扩展 / 编码约定扩展 / 资源目录扩展。

本详细设计阶段**无新增规范冲突**。

---

## 4. 用户授权的偏离

**无**。本详细设计 100% 合规。

---

## 5. 规范变更响应(增量更新时填写)

> 本次为首次详细设计(v1),无规范变更触发。

---

## 6. 规范自检结论

- **完全合规的章节**:§1 / §2 / §3 / §4 / §5 / §6 / §7 / §8 / §9 / §10 / §11 / §12 / §13 / §14(全部 14 个 RESULT.md 主章节)
- **经用户授权偏离的章节**:**0**
- **待澄清冲突**:**0**
- **13/13 INV 全部满足**
- **8/8 风险全部有缓解**
