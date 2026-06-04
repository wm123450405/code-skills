# 规范遵循记录 — REQ-00004

更新时间:2026-06-04 15:50
版本:V0.0.2

## 1. 本次参考的规范文件
- `./assistants/rules/skill-conventions.md`(技能元信息)
- `./assistants/rules/module-conventions.md`(DEPRECATED,仅作历史参考)
- `./assistants/rules/directory-conventions.md`(替代 module-conventions,§规则 1 占位)
- `./assistants/rules/dashboard-conventions.md`(看板与版本)
- `./assistants/rules/encoding-conventions.md`(编码格式)
- `./assistants/rules/migration-mapping.md`(编码迁移)
- `./assistants/rules/marketplace-protocol.md`(marketplace 协议)
- `./assistants/rules/doc-conventions.md`(文档编写,仅在可选改 README 时引用)
- `./assistants/rules/dependency-conventions.md`(三方依赖,§规则 1 占位)

> 6 个占位规则(commit / coding-style / naming / framework / dependency / directory §1)未填充细则;本设计在引用处显式标注"以既有惯例落地"。

## 2. 规范 vs 现状偏离

| # | 规范条款 | 项目现状 | 影响 | 处理 |
| --- | --- | --- | --- | --- |
| D-1 | `module-conventions.md` 顶部声明 DEPRECATED,内容已迁移到 `directory-conventions.md` | `directory-conventions.md` §规则 1 仍占位(`2026-06-04 10:45` 起未填充) | 本设计在 `module-breakdown.md` 中按"既有惯例"落地,等正式规则生效再校准 | 显式记录偏离;不触发规范强制条款 |
| D-2 | `code-review/SKILL.md` frontmatter `description` 含 `<version>` 字面(笔误,应为 `<版本号>`) | 同上 | 阅读体验差,但与 `skill-conventions §规则 1` 不冲突 | **不在 REQ-00004 范围**;留作 follow-up |
| D-3 | `README.md` / `README.en.md` 中"技能清单"是否需要为 `code-dashboard` 追加一行 | V0.0.1 既有 README 已列 8 ~ 10 个技能,本设计**建议不改** | 避免与 V0.0.2 其他并发需求产生冲突;若改必须中英同次提交(`doc-conventions §规则 1`) | 显式标注为"用户授权的偏离" / "可选" |
| D-4 | `plugins/code-skills/CLAUDE.md` "AI 工作约定"小节是否需要为 `code-dashboard` 追加指引 | V0.0.1 REQ-00003 已落定"由 `code-rule` 维护,手动修改可能被覆盖" | 本设计**不主动写**,避免越权 | 显式标注为"留作后续 `code-rule` 沉淀" |

## 3. 规范 vs 需求冲突

> 本节追踪"规范条款"与"需求条目"之间的冲突,以及用户选择。

| # | 冲突点 | 选项 | 用户选择 | 解决时间 |
| --- | --- | --- | --- | --- |
| C-1 | 需求 FR-2.4 要求"P0/P1 醒目标记 + P2/P3 计入统计但不单列",与 `dashboard-conventions §规则 1` "字段枚举扩展需 3 文件同步" 看似冲突 | A. 视为"展示策略"不触发字段扩展(走 §规则 1 "纯排版"例外) | A | 2026-06-04 12:50(Q-3 锁定) |
| C-2 | 需求 NFR-3 要求"任务编号同时支持新旧两种字面",与 `encoding-conventions §规则 3` "严格嵌套式 TASK 编码" 冲突 | A. 仅展示侧兼容(显示透传 + 解析严格) | A | 2026-06-04 12:50(FR-3 / NFR-3 锁定) |
| C-3 | 需求 G-3 / NFR-1 锁"零外部依赖",与 `dependency-conventions §规则 1`(占位)无直接冲突 | — | 锁定 | 2026-06-04 12:50(FR / NFR 锁定) |
| C-4 | 需求 NFR-6 锁"不修改 marketplace.json / plugin.json / 其他 10 个 SKILL.md",与 `marketplace-protocol §规则 1` 字段约束无冲突(本设计不动) | — | 锁定 | 2026-06-04 12:50(NFR-6 锁定) |

> 4 项冲突已通过 `code-require` Q-1 ~ Q-3 锁定 + FR/NFR 隐含约束,本设计阶段不重新讨论。

## 4. 用户授权的偏离

| # | 章节 | 偏离内容 | 理由 | 授权时间 |
| --- | --- | --- | --- | --- |
| A-1 | `module-breakdown.md` 模块路径 | 不放 `templates/` / `checklists/` / `guidelines/` 子目录(本设计**不**新增子目录) | `code-dashboard` 是"只读渲染型"技能,不产出文档/清单/规则;`SKILL.md` 单文件足够承载 | 2026-06-04 12:50(FR-1 锁定 SKILL.md 是入口) |
| A-2 | `RESULT.md` §3.1 组件图 | 新增 `code-dashboard` 到 `marketplace.json` 列表项被刻意省略 | NFR-6 锁"不修改 marketplace.json";`/code-dashboard` 通过 Claude Code 技能协议自动发现,无需 marketplace 显式登记 | 2026-06-04 12:50(NFR-6 锁定) |
| A-3 | `RESULT.md` §6 接口 | 不提供"切到 V0.0.x 历史版本"能力 | Q-8 留作未采用(属 `code-version` 范畴) | 2026-06-04 12:50(Q-8 未采用) |

## 5. 规范变更响应(本设计阶段无变更)

> 本设计为首次设计(无既有 RESULT.md);`./assistants/rules/` 13 个文件在本次扫描时无新增/修改/删除。
> 若未来 `code-rule` 沉淀新规则(尤其 `directory-conventions §规则 1` / `dependency-conventions §规则 1`),需触发本设计增量更新,流程见 `code-design` 步骤 7B。

## 6. 自检清单(本设计阶段)
- [x] `SKILL.md` frontmatter 必含 `name: code-dashboard` + 完整 `description`(`skill-conventions §规则 1`)
- [x] `name` 与目录名 `code-dashboard` 一致(`skill-conventions §规则 1`)
- [x] `code-dashboard` 不修改 `marketplace.json` / `plugin.json` / 其他 10 个 SKILL.md frontmatter(`marketplace-protocol §规则 1` + NFR-6)
- [x] `code-dashboard` 不写看板字段扩展(`dashboard-conventions §规则 1` 不触发)
- [x] `code-dashboard` 不引入新三方依赖(`dependency-conventions` 占位 + NFR-1)
- [x] 任务编号解析严格按 `encoding-conventions §规则 3`(新格式优先;旧格式透传,NFR-3)
- [x] 不动 `module-conventions.md`(DEPRECATED,只读参考)
- [x] 不动 `directory-conventions.md`(只读)
- [x] 不写 `plugins/code-skills/CLAUDE.md` 的"AI 工作约定"小节(留作 `code-rule` 沉淀)
- [x] 不改 `plugins/code-skills/README.md` / `README.en.md`(可选且高风险,本设计建议不改)
- [x] `RESULT.md` 文档头标注"上游" + "遵循规范" + 关键 FR/NFR 编号引用
- [x] 架构图含 Mermaid 组件图 + ASCII 数据流(`code-design/SKILL.md` 步骤 13A 强制)
