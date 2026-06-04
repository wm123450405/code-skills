# 规范遵循记录 — REQ-00004(详细设计阶段)

更新时间:2026-06-04 16:10
版本:V0.0.2

---

## 1. 本次参考的规范文件
继承 `design/REQ-00004/rule-compliance.md §1` 的 9 个文件(本阶段未变更),新增 2 个引用:
- `./assistants/rules/commit-conventions.md`(占位,V0.0.1 既有 commit 走 conventional 风格,供 `code-it` 阶段参考)
- `./assistants/rules/doc-conventions.md §规则 1/2`(T-003 触发条件)

> 13 个规范文件总览与摘要见 `materials-index.md`。

---

## 2. 规范 vs 现状偏离(继承自 design 阶段,本阶段无新偏离)

| # | 规范条款 | 项目现状 | 影响 | 处理 |
| --- | --- | --- | --- | --- |
| D-1 | `module-conventions.md` DEPRECATED,`directory-conventions.md §1` 占位 | 现状同 design 阶段 | 本设计按既有惯例落地 | 显式记录,等正式生效再校准 |
| D-2 | `code-review/SKILL.md` frontmatter `<version>` 笔误 | 现状同 design 阶段 | 阅读体验差 | 不在本需求范围 |
| D-3 | README 是否追加 `code-dashboard` 行 | T-003 可选触发 | 中英同次提交 | `doc-conventions §规则 1` 强约束 |
| D-4 | CLAUDE.md "AI 工作约定" 是否追加 | T-002 可选触发 | 由 `code-rule` 维护 | 留作 `code-rule` 沉淀 |

---

## 3. 规范 vs 设计冲突(本阶段新发现 0 项,继承 4 项)

继承自 design 阶段 `rule-compliance.md §3` 的 4 项冲突(均已通过 `code-require` Q-1~Q-3 锁定):
- C-1 段 1 详细布局(展示策略,§规则 1 "纯排版"例外)— 锁定
- C-2 任务编号双格式兼容(NFR-3 + 严格按新格式生成命令)— 锁定
- C-3 NFR-1 零外部依赖(`dependency-conventions §规则 1` 占位)— 锁定
- C-4 NFR-6 不改 marketplace.json / plugin.json(`marketplace-protocol §规则 1` 字段约束无冲突)— 锁定

**本阶段新发现冲突**:**0 项**(`code-plan` 阶段对上游需求/设计/规范均无变更,无新冲突触发)

---

## 4. 用户授权的偏离(继承自 design 阶段,本阶段 0 项新增)

| # | 章节 | 偏离内容 | 理由 | 授权时间 |
| --- | --- | --- | --- | --- |
| A-1 | `module-breakdown.md` 模块路径 | 不放 `templates/` / `checklists/` / `guidelines/` 子目录 | `code-dashboard` 是"只读渲染型"技能,不产出文档/清单/规则 | 2026-06-04 12:50(FR-1 锁定) |
| A-2 | `RESULT.md` §3.1 组件图 | 新增 `code-dashboard` 到 `marketplace.json` 列表项被刻意省略 | NFR-6 锁"不修改 marketplace.json";走 Claude Code 技能自动发现 | 2026-06-04 12:50(NFR-6 锁定) |
| A-3 | `RESULT.md` §6 接口 | 不提供"切到 V0.0.x 历史版本"能力 | Q-8 留作未采用(属 `code-version` 范畴) | 2026-06-04 12:50(Q-8 未采用) |

---

## 5. 详细设计阶段新增/修订的偏离(本节)

> 本节专门追踪"本阶段相对 design 阶段"的新偏离或更严格执行的偏离。

### P-A1(本阶段新增):任务编号解析时 V0.0.2 状态子状态 `已完成(需求分析)` 不归一化
- **偏离内容**:`aggregate()` 严格按字面匹配;`已完成(需求分析)` 不归一到 `已完成`
- **理由**:避免"code-plan / code-it" 误判为"全部完成"
- **规范依据**:与 `encoding-conventions.md §规则 2` "5 位纯数字 / 不重用"精神一致(字面不归一化)
- **授权**:Q-P2 采纳默认 A

### P-A2(本阶段新增):T-001 测试状态 = `不适用`
- **偏离内容**:代码类任务默认 `测试状态=未编写`,本任务标 `不适用`
- **理由**:本技能是 Markdown 指令,无编程语言运行时,无单元测试载体
- **规范依据**:`code-plan` SKILL.md 步骤 10A "任务双状态初始化"段:"若任务范围明确不含可测代码(如纯配置变更),可在 `code-plan` 或 `code-it` 中讨论后设为 `不适用`"
- **授权**:本阶段(2026-06-04 16:10)默认采纳

### P-A3(本阶段新增):需求模式"里程碑"段不显示
- **偏离内容**:需求模式 5 段不含"里程碑"
- **理由**:Q-P3 锁定;里程碑是版本级概念
- **授权**:Q-P3 采纳默认 A

---

## 6. 详细设计阶段自检清单(15 条)

- [x] T-001 SKILL.md frontmatter 必含 `name: code-dashboard` + 完整 `description`(`skill-conventions §规则 1`)
- [x] T-001 `name` 与目录名 `code-dashboard` 一致(`skill-conventions §规则 1`)
- [x] T-001 SKILL.md 章节顺序与既有 10 个 SKILL.md 一致(目标/适用/不适用/目录/输入/输出/工具/步骤/边界/衔接/不要做)
- [x] T-001 工具集严格 `Read` / `Glob` / `Grep`,无 `Write` / `Edit` / `Bash`(`FR-7` + `code-review` 行为对标)
- [x] T-001 任务编号解析同时支持新格式 `^TASK-(REQ|BUG)-\d{5}-\d{5}$` + 旧格式 `^(REQ|BUG)-\d{5}-\d{5}$`(`encoding-conventions §规则 1/3` + NFR-3)
- [x] T-001 命令生成严格按既有 10 个 SKILL.md frontmatter 的真实语法(AC-4.2)
- [x] T-001 性能预期 < 5 秒(NFR-4 锁);并行 Read 3 文件(需求模式)
- [x] T-001 异常处理 3 层退化(L1 启动错 / L2 数据缺 / L3 异常兜底)(NFR-2)
- [x] T-001 ASCII 比例条固定 12 字符 + `█` / `░` / `▓`(Q-3 + Q-D3)
- [x] T-002 (可选)改 `CLAUDE.md` "AI 工作约定"段:由 `code-rule` 维护,**触发条件=用户授权**
- [x] T-003 (可选)改 `README.md` + `README.en.md`:中英同次提交(`doc-conventions §规则 1`)
- [x] T-001/2/3 不修改 `marketplace.json` / `plugin.json` / 其他 10 SKILL.md frontmatter(NFR-6 + `marketplace-protocol §规则 1`)
- [x] T-001/2/3 不引入新三方依赖(NFR-1 + `dependency-conventions §规则 1` 占位无冲突)
- [x] T-001 不写看板字段扩展(`dashboard-conventions §规则 1` 不触发)
- [x] T-001 完成后 `git status` 干净(只新增 1 个 `SKILL.md`,可选 +2 处文件)(FR-7 + NFR-7)

---

## 7. 规范变更响应(本阶段无变更)
- `./assistants/rules/` 13 个文件在本次扫描时无新增/修改/删除
- 若未来 `code-rule` 沉淀新规则(尤其 `directory-conventions §规则 1` / `dependency-conventions §规则 1` / `commit-conventions §规则 1`),需触发本设计增量更新,流程见 `code-plan` 步骤 7B
