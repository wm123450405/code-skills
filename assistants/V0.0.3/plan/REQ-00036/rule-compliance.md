# 规范遵循记录 — REQ-00036(详设阶段)

更新时间:2026-06-16 17:33
版本:V0.0.3

## 1. 本次参考的规范文件
- `./assistants/rules/skill-conventions.md` §规则 1(frontmatter)
- `./assistants/rules/skill-conventions.md` §规则 2(开发痕迹禁令)
- `./assistants/rules/encoding-conventions.md` §规则 1/2/3/4
- `./assistants/rules/dashboard-conventions.md` §规则 1
- `./assistants/rules/module-conventions.md` §规则 1
- 其他 8 个规范(naming/coding/framework/dependency/commit/marketplace/migration):0 触发

## 2. 规范 vs 现状偏离
(无 — 本设计完全合规)

## 3. 规范 vs 设计冲突
(无)

## 4. 用户授权的偏离
(无)

## 5. 规范变更响应
- 规范文件:`./assistants/rules/skill-conventions.md §规则 2`
- 变更:新增(由 `code-rule` 阶段在 `commit a3102a5` 添加)
- 时间:2026-06-16
- 对本详细设计的影响:
  - 范围过滤(算法 0)直接采用该规则的"适用范围"作为输入
  - 6 条清理规则(算法 1-6)与该规则的 6 类字面一一对应
  - 4 类白名单(算法 1-6 的负向断言)与该规则的"例外(白名单)"一一对应
  - `code-fix` 技能 R-5 豁免与该规则的"例外 §code-fix"对齐
- 处理动作:已对齐(本详细设计是该规范的"实施细化")
