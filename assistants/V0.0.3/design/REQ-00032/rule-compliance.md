# 规范遵循记录 — REQ-00032

更新时间:2026-06-12 16:28
版本:V0.0.3

## 1. 本次参考的规范文件

- `./assistants/rules/skill-conventions.md`(SKILL.md 编写规范)
- `./assistants/rules/naming-conventions.md`(命名规范)
- `./assistants/rules/encoding-conventions.md`(编码规范)
- `./assistants/rules/module-conventions.md`(模块规划规范)
- `./assistants/rules/dashboard-conventions.md`(看板字段约定)
- `./assistants/rules/commit-conventions.md`(提交前缀)
- `./assistants/rules/doc-conventions.md`(文档编写规范;不直接相关)

## 2. 规范 vs 现状偏离

无。本需求**不**修改项目代码、不修改项目结构、不引入新依赖,与既有规范 0 偏离。

## 3. 规范 vs 需求冲突

| 规范条款 | 需求 | 冲突 | 解决 | 解决时间 |
| --- | --- | --- | --- | --- |
| `naming-conventions.md §规则 1` (待添加) | 本需求不涉及新命名 | 无冲突 | — | — |
| `skill-conventions.md §规则 1` (frontmatter L1-3 字节级保留) | 步骤 10A / 10B 末尾追加"### 下一步建议"段 | **无冲突**(本需求**不**修改 frontmatter) | 锚点限定在"## 工作流程 → 步骤 10A / 10B 段内文末" | 2026-06-12 16:28 |

## 4. 用户授权的偏离

无。本需求**不**偏离任何既有规范条款。

## 5. 规范变更响应(增量更新时填写)

不适用(本需求是首次设计,非增量更新)。

## 6. INV 字节级保留校验(本需求)

| INV | 校验项 | 结果 |
| --- | --- | --- |
| **INV-1** | `code-require/SKILL.md` frontmatter L1-3 字节级保留 | ✅ 0 改 |
| **INV-2** | `code-require/SKILL.md` 既有"## 工作流程"小节 0 改 | ✅ 0 改(本需求在 步骤 10A / 10B 段内**纯追加**;既有"向用户汇报"段字节级保留) |
| **INV-3** | 提交前缀 `chore(<skill>):` 沿用 | ✅ 沿用 `chore(code-require):` |
| **INV-4** | 既有 9 个 `code-*` 技能 SKILL.md 0 改 | ✅ 0 改 |
| **INV-5** | 既有 7 个项目级规范 0 改 | ✅ 0 改 |
| **INV-6** | 4 个 README/marketplace/plugin/CLAUDE 0 改 | ✅ 0 改 |
| **INV-7** | 既有 12 个 REQ 的 RESULT.md 0 改 | ✅ 0 改 |
| **INV-8** | 0 新增三方依赖 | ✅ 0 新增 |
| **INV-9** | 看板字段三方同步 0 触发 | ✅ 0 触发(本需求不修改看板字段) |
| **INV-10**(新增) | 屏幕日志格式字节级保留 | ✅ 字符数 ≤ 80 字 / 行数 ≤ 2 行 / 路径串 `/code-auto` `/code-design` 字节级 |

## 7. 自检结论

- 本需求**0**规范违反
- 本需求**0**现状偏离
- 本需求**0**用户授权偏离
- 本需求**10/10**INV 字节级保留校验通过
