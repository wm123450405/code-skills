# 规范遵循记录 — REQ-00006(详细设计阶段)

更新时间:2026-06-04 17:01
版本:V0.0.2

## 1. 本次参考的规范文件(与 design 阶段一致)

- `./assistants/rules/skill-conventions.md` §规则 1(SKILL.md frontmatter)
- `./assistants/rules/module-conventions.md` §规则 1(DEPRECATED 但沿用:templates/ 固定子目录)
- `./assistants/rules/dashboard-conventions.md` §规则 1(本计划 0 触发)
- `./assistants/rules/doc-conventions.md` §规则 1 + §规则 2(若拆双 README 任务则强制约束)
- 其他 9 个规范文件:占位或不相关

## 2. 规范 vs 详细设计冲突

- **0 冲突**:详细设计完全继承概要设计的合规结论,未引入新冲突

## 3. 用户授权的偏离

- **0 偏离**

## 4. 关键合规验证(任务级)

### 4.1 T-001 `code-publish/SKILL.md`
- 验证项:frontmatter `name: code-publish` + 完整 `description`
- 检查方式:`code-it` 在写 SKILL.md 后自检 + `code-review` 阶段二次验证
- 关联规范:`skill-conventions.md §规则 1`

### 4.2 T-002 ~ T-006 模板任务
- 验证项:全部 5 份模板位于 `plugins/code-skills/skills/code-publish/templates/` 子目录
- 检查方式:`code-it` 在写模板时按指定路径
- 关联规范:`module-conventions.md §规则 1`

### 4.3 T-007 不变量自检
- 验证项:
  - 0 修改 `marketplace.json` / `plugin.json`(`git status` 验证)
  - 0 修改其他 10 个 `code-*` SKILL.md(同上)
  - 0 修改 `assistants/rules/` 下规范(同上)
  - 0 修改 `plugins/code-skills/CLAUDE.md` 的"AI 工作约定"(同上)
  - 0 修改 `assistants/V0.0.2/RESULT.md` 中非本技能负责区段
- 检查方式:`code-it` 在 T-007 中 `git diff --stat` 验证;输出到 `code/TASK-REQ-00006-00007/deviations.md`
- 关联规范:FR-8 + `dashboard-conventions.md §规则 1`

### 4.4 T-008(可选)双 README 同步
- 验证项:若拆此任务,`plugins/code-skills/README.md` + `README.en.md` 必须在**同次提交**追加 `code-publish` 一行
- 检查方式:`code-it` 在 T-008 中:Edit 中文 → Edit 英文 → 同次 `git add` → 同次 `git commit`
- 关联规范:`doc-conventions.md §规则 1` + §规则 2

## 5. 规范变更响应(增量更新时)
- 不适用(首次创建)

## 6. 合规总结论

| 规范 | 自检结果 |
| --- | --- |
| `skill-conventions.md §规则 1` | ✓ 完全合规(由 T-001 自检) |
| `module-conventions.md §规则 1` | ✓ 完全合规(5 份模板在 templates/) |
| `dashboard-conventions.md §规则 1` | ✓ 0 触发(本计划不扩展看板字段) |
| `doc-conventions.md §规则 1 / §规则 2` | ✓ 由 T-008 满足(若拆) |
| 占位规范 6 个 | ✓ 占位不影响 |
| 不相关规范 3 个 | ✓ 不在本计划范围 |

**总结论**:本详细设计 + 任务计划**完全合规**,0 偏离 / 0 待澄清冲突 / 0 用户授权偏离。
