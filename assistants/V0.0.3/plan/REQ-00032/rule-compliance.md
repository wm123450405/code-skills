# 规范遵循记录 — REQ-00032

更新时间:2026-06-12 16:48
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
| `skill-conventions.md §规则 1` (frontmatter L1-3 字节级保留) | 步骤 10A / 10B 末尾追加"### 下一步建议"段 | **无冲突**(本需求**不**修改 frontmatter) | 锚点限定在"## 工作流程 → 步骤 10A / 10B 段内文末" | 2026-06-12 16:48 |

## 4. 用户授权的偏离

无。本需求**不**偏离任何既有规范条款。

## 5. 冲突解决记录(沿用需求阶段)

> 本节列出需求阶段已解决的 4 问(详 `require/REQ-00032/clarifications.md`):
- Q-1:AI 自主判定(无需阈值)
- Q-2:只追加到屏幕日志(零文档变更)
- Q-3:建议仅 2 条(微小 / 其他)
- Q-4:不联动 /code-unit(沿用 REQ-00031)

## 6. 规范变更响应(增量更新时填写)

不适用(本需求是首次详设,非增量更新)。

## 7. INV 字节级保留校验(本需求)

| INV | 校验项 | 结果 |
| --- | --- | --- |
| **INV-1** | `code-require/SKILL.md` frontmatter L1-3 字节级保留 | ✅ 0 改 |
| **INV-2** | `code-require/SKILL.md` 既有"## 工作流程"小节 0 改 | ✅ 0 改(本需求在 步骤 10A / 10B 段内**纯追加**;既有"向用户汇报"段字节级保留) |
| **INV-3** | 提交前缀 `chore(<skill>):` 沿用 | ✅ 沿用 `chore(code-it):`(本任务是 code-it 实施) |
| **INV-4** | 既有 9 个 `code-*` 技能 SKILL.md 0 改 | ✅ 0 改 |
| **INV-5** | 既有 7 个项目级规范 0 改 | ✅ 0 改 |
| **INV-6** | 4 个 README/marketplace/plugin/CLAUDE 0 改 | ✅ 0 改 |
| **INV-7** | 既有 12 个 REQ 的 RESULT.md 0 改 | ✅ 0 改 |
| **INV-8** | 0 新增三方依赖 | ✅ 0 新增 |
| **INV-9** | 看板字段三方同步 0 触发 | ✅ 0 触发(本需求不修改看板字段) |
| **INV-10**(本需求新增) | 屏幕日志格式字节级保留(字符数 ≤ 80 字 / 行数 ≤ 2 行 / 路径串字节级) | ✅ 通过(material-details §算法 2 字符数校验) |

## 8. 自检结论

- 本需求**0**规范违反
- 本需求**0**现状偏离
- 本需求**0**用户授权偏离
- 本需求**10/10**INV 字节级保留校验通过
