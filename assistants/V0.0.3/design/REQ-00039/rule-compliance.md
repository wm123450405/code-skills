# 规范遵循记录 — REQ-00039

更新时间:2026-06-22 14:30
版本:V0.0.3

## 1. 本次参考的规范文件

- `./assistants/rules/skill-conventions.md`(§规则 1 + §规则 2)
- `./assistants/rules/dashboard-conventions.md`(§规则 1)
- `./assistants/rules/encoding-conventions.md`(§规则 1 + §规则 2 + §规则 3 + §规则 4)
- `./assistants/rules/migration-mapping.md`(§规则 1 + §规则 4)
- `./assistants/rules/directory-conventions.md`(§规则 1)
- `./assistants/rules/doc-conventions.md`(§规则 1 + §规则 2)
- `./assistants/rules/naming-conventions.md`(§规则 1)
- `./assistants/rules/coding-style.md`(§规则 1)
- `./assistants/rules/framework-conventions.md`(§规则 1)
- `./assistants/rules/dependency-conventions.md`(§规则 1)
- `./assistants/rules/commit-conventions.md`(§规则 1)
- `./assistants/rules/marketplace-protocol.md`(§规则 1)
- `./assistants/rules/module-conventions.md`(§规则 1)

## 2. 规范 vs 现状偏离

(无 — 本需求沿用既有 SKILL.md / 模板结构,**不**修改既有章节)

## 3. 规范 vs 需求冲突

(无 — code-auto 上下文 + 1 轮 AskUserQuestion 全部搞定,无冲突)

## 4. 用户授权的偏离

(无 — 本需求**不**偏离既有规范)

## 5. 规范遵循自检

| 规范条款 | 自检结果 |
| --- | --- |
| `skill-conventions §规则 1`(frontmatter L1-3 字节级保留) | ✅ 字节级保留,**不**修改 |
| `skill-conventions §规则 2`(SKILL.md 不含开发痕迹) | ✅ 新写段落**不**含"本需求 REQ-NNNNN 新增"等 6 类字面 |
| `dashboard-conventions §规则 1`(字段扩展需三方同步) | ✅ 本需求**不**新增看板列(NFR 强化不触发) |
| `encoding-conventions §规则 1`(接收端宽松正则) | ✅ 任务编码正则沿用既有 |
| `module-conventions §规则 1`(`templates/` 留作历史不删) | ✅ 新建在 `code-it/lib/` 而非 `code-it/templates/` |
| `commit-conventions §规则 1`(`chore(code-<技能>):` 模式) | ✅ 末尾兜底 commit 沿用既有模式 |
| `marketplace-protocol §规则 1`(协议字段约束) | ✅ 本需求**不**改 `.claude-plugin/` |
| `directory-conventions §规则 1`(目录与模块) | ✅ 路径生成语义沿用既有 |
| `doc-conventions §规则 1 + §规则 2`(README 多语言 + 主语言完整性) | ✅ SKILL.md 不是 README,本规则不适用 |
| `dependency-conventions §规则 1`(依赖) | ✅ 本需求**不**新增三方依赖(沿用既有 tokei/cloc 系统命令) |
| `coding-style §规则 1`(代码风格) | ✅ 本需求是 Markdown 自然语言,沿用既有风格 |
| `naming-conventions §规则 1`(命名) | ✅ 模块名 `logic-loc` + `logic-loc-defaults` 符合 kebab-case |
| `framework-conventions §规则 1`(框架) | ✅ 无框架变更 |
| `migration-mapping §规则 1 + §规则 4`(编码迁移) | ✅ 5 位纯数字沿用,**不**引入新编码 |

**自检结论**:14 条规范全部满足,0 偏离、0 冲突、0 用户授权偏离。