# 规范遵循记录 — REQ-00006

更新时间:2026-06-04 16:48
版本:V0.0.2

## 1. 本次参考的规范文件

执行 `Glob "./assistants/rules/**/*"` 得 13 个文件,**有效约束 4 个**,其余 9 个为占位或不相关:

### 1.1 有效约束规范
- `./assistants/rules/dashboard-conventions.md` §规则 1(看板字段约定扩展需 3 处同步)
- `./assistants/rules/doc-conventions.md` §规则 1(README 多语言对仗)+ §规则 2(README 持续维护)
- `./assistants/rules/module-conventions.md` §规则 1(技能资源放固定子目录;**已 DEPRECATED 但本设计沿用**)
- `./assistants/rules/skill-conventions.md` §规则 1(SKILL.md frontmatter)

### 1.2 占位规范(不影响本设计)
- `coding-style.md` / `commit-conventions.md` / `dependency-conventions.md` / `framework-conventions.md` / `naming-conventions.md` / `directory-conventions.md`(均"待添加")

### 1.3 不相关规范
- `encoding-conventions.md`(本设计不产生新编码)
- `marketplace-protocol.md`(本设计不修改 marketplace.json/plugin.json)
- `migration-mapping.md`(追溯参考,本设计无追溯)

## 2. 规范 vs 现状偏离

- **0 偏离**:本设计是"新增技能"(non-modifying),不涉及对已有代码/规范的纠正

## 3. 规范 vs 需求冲突

- **0 冲突**:需求 v1 锁定的 4 个 Q + 5 个默认 Q 均与规范兼容;具体:

| 锁定/默认 | 规范覆盖 | 冲突 |
| --- | --- | --- |
| Q-1 全检查最严 | 无规范覆盖 | 无 |
| Q-2 创建 qanda/ 骨架 | 无规范覆盖 | 无 |
| Q-3 基线跳过 UPDATE | 无规范覆盖 | 无 |
| Q-4 通用骨架 | 无规范覆盖 | 无 |
| Q-5 不检查里程碑 | 无规范覆盖 | 无 |
| Q-6 不自动抽取 | 无规范覆盖 | 无 |
| Q-7 不参与 REQ-00005 | 无规范覆盖 | 无 |
| Q-8 不追加 CLAUDE.md | `dashboard-conventions §规则 1`(若追加需 3 处同步 — Q-8 默认"不追加"→ 不触发) | 无 |
| Q-9 不自动 commit | `commit-conventions.md`(占位) | 无 |

## 4. 用户授权的偏离

- **0 授权偏离**:本设计所有决策均完全遵循上述规范 + 需求 v1

## 5. 关键合规验证

### 5.1 `skill-conventions.md §规则 1`
- 验证项:`code-publish/SKILL.md` frontmatter 必含 `name: code-publish` + 非空 `description`
- 状态:**已设计**(`module-breakdown.md §2.1`)
- 检查方式:`code-it` 阶段在写 SKILL.md 时自检

### 5.2 `module-conventions.md §规则 1`
- 验证项:`code-publish/` 下 5 份模板放在 `templates/` 子目录,不散落
- 状态:**已设计**(`module-breakdown.md §1` 模块总览中 5 份模板路径全部为 `templates/...`)
- 检查方式:`code-it` 阶段在创建文件时自检

### 5.3 `dashboard-conventions.md §规则 1`
- 验证项:本设计**不**扩展看板字段(只读消费),不触发 3 处同步要求
- 状态:**自然合规**(`module-breakdown.md §4`"修改既有模块:0 个")
- 检查方式:`code-review` 阶段做最终验证

### 5.4 `doc-conventions.md §规则 1 / §规则 2`
- 验证项:若本设计在 `plugins/code-skills/README.md` 追加"主要能力"一行,**必须**在同次提交同步 `README.en.md`
- 状态:**本设计将此作为可选附加任务**(需求 §2.3 末尾"若需要..."),由 `code-plan` 决定是否拆为独立任务
- 检查方式:`code-plan` 拆任务时显式标"双 README 同步";`code-review` 在 PR 中验证

## 6. 规范变更响应(增量更新时填写)

- **本次为首次设计**,无规范变更响应
- 若未来 `assistants/rules/` 下任一规范修改且影响本设计,将在此节追加:
  ```
  - 规范文件:<X>,变更:<新增/修改/删除>
  - 时间:YYYY-MM-DD HH:mm
  - 对 RESULT.md 的影响:<章节/无>
  - 处理动作:<已修订/无需修订/用户授权保留>
  ```

## 7. 合规结论

| 规范 | 自检结果 |
| --- | --- |
| `dashboard-conventions.md` | ✓ 完全合规(0 触发) |
| `doc-conventions.md` | ✓ 完全合规(可选附加任务由 code-plan 验证) |
| `module-conventions.md` | ✓ 完全合规(已 DEPRECATED 但沿用其精神) |
| `skill-conventions.md` | ✓ 完全合规 |
| 占位规范(6 个) | ✓ 占位不影响 |
| 不相关规范(3 个) | ✓ 不在本设计范围 |

**总结论**:本设计**完全合规**,0 偏离 / 0 待澄清冲突 / 0 用户授权偏离。
