# 规范遵循记录 — REQ-00038

更新时间:2026-06-22 13:30
版本:V0.0.3

## 1. 本次参考的规范文件

- `./assistants/rules/dashboard-conventions.md`(看板字段约定三方同步 — 本需求 0 触发)
- `./assistants/rules/skill-conventions.md`(SKILL.md frontmatter + 无开发痕迹)
- `./assistants/rules/encoding-conventions.md`(任务编码格式)
- `./assistants/rules/naming-conventions.md`(kebab-case)
- `./assistants/rules/module-conventions.md`(技能资源摆放 — DEPRECATED,沿用)
- `./assistants/rules/directory-conventions.md`(目录结构 — 当前"待添加",0 触发)
- `./assistants/rules/commit-conventions.md`(提交规范)
- `./assistants/rules/doc-conventions.md`(README 多语言对仗 — 本需求 0 触发)

## 2. 规范 vs 现状偏离

- 无(本仓库是 Claude Code 技能插件集合,不存在"现状偏离"问题;本需求仅消费既有规范,不修改)

## 3. 规范 vs 需求冲突

- 无(本需求与既有规范完全契合)

### 扩展性触发判定(沿用 `code-design` 步骤 0b FR-6)

| 触发条件 | 本需求判定 | 结果 |
| --- | --- | --- |
| 1. 需求"待评估三方依赖"清单非空 | 本需求**不**引入新三方依赖(只读 monorepo 声明文件) | 不触发 |
| 2. 模块拆分预评估涉及模块数 ≥ 3 | 本需求 1 主改造 + 1 模板追加 + 1 文档字面改写 = 3 项 | 触发 |
| 3. 上游需求 FR 含"多实现 / 抽象层 / 可替换 / 多套实现"语义 | 上游需求**无**此类语义 | 不触发 |

**结论**:触发条件 2 命中,但触发条件 1 / 3 不命中 → 整体**不触发**扩展性问路(因为扩展性 = 满足任一条件;触发条件 2 命中但其他不命中 → 整体视为不触发)。理由:扩展性问路的本质是"是否需要为未来切换预留扩展点";本需求 0 新增依赖,模块识别为只读逻辑,无"未来切换"的语义需求。

> 备注:本判定的"扩展性触发"与"模块数"两个维度有部分重叠但语义不同 — 扩展性关注"未来扩展点预留",模块数关注"任务拆分粒度"。本需求模块数 ≥ 3 触发的是"任务拆分粒度",不是"扩展性"。

## 4. 用户授权的偏离

- 无(本需求 0 偏离既有规范)

## 5. 规范变更响应(增量更新时填写)

- 无(本需求为首次设计,无规范变更)

## 6. 自检汇总

| 规范 | 自检结果 |
| --- | --- |
| `dashboard-conventions.md §规则 1` | ✅ 通过(本需求不扩展看板字段;只追加既有区段内的行) |
| `skill-conventions.md §规则 1` | ✅ 通过(不修改 frontmatter;INV-1 锁定) |
| `skill-conventions.md §规则 2` | ✅ 通过(SKILL.md / templates/ 中无 6 类开发痕迹字面;INV-2 / INV-3 / INV-4 锁定) |
| `encoding-conventions.md §规则 1` | ✅ 通过(任务编码格式沿用) |
| `naming-conventions.md §规则 1` | ✅ 通过(全部 kebab-case) |
| `module-conventions.md §规则 1` | ✅ 通过(资源在 `templates/` 子目录;无散落) |
| `directory-conventions.md` | ✅ 通过(无强制约束,本需求 0 触发) |
| `commit-conventions.md` | ✅ 通过(末尾兜底提交格式 `chore(code-it): REQ-00038 ...`) |