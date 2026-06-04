# 关联需求 — REQ-00004

更新时间:2026-06-04 12:50

## 扫描范围
- 同版本:`./assistants/V0.0.2/require/`
  - 空(V0.0.2 尚未有其他需求)
- 跨版本:`./assistants/V0.0.0/require/`、`./assistants/V0.0.1/require/`

## 关联需求清单

### REQ-00001(版本:V0.0.1)— Marketplace 改名落地
- **关联点**:
  - 本需求的"数据源"(`./assistants/<版本号>/RESULT.md` 三大区段)的**首条历史样本**来自 REQ-00001 引入的看板模板
  - REQ-00001 创建的 4 任务 + 后续派生 1 任务(`REQ-00001-005`)是看板"任务清单"区段的内容
- **对本需求的影响**:
  - **数据兼容性**:`code-dashboard` 读取 REQ-00001 的任务行时,会看到字面 `REQ-00001-001`(无 `TASK-` 前缀)。这与 `encoding-conventions.md §规则 3`(v2 锁定嵌套式 `TASK-REQ-...`)不一致。
  - **决策点(待澄清)**:是否在 `code-dashboard` 解析任务编号时**同时**识别两种格式?见 clarifications.md Q-1。
- **来源**:`./assistants/V0.0.1/require/REQ-00001/RESULT.md`(扫描于 2026-06-04 12:50)

### REQ-00002(版本:V0.0.1)— 编码格式统一
- **关联点**:
  - 显式定义了 3 类编码的**权威源**(`./assistants/rules/encoding-conventions.md`)
  - `code-dashboard` 输出的"下一步建议"需要引用这些编码格式(例如:`建议执行 /code-it REQ-00004-001`),链接指向必须严格符合规范
- **对本需求的影响**:
  - **必须遵守**:`code-dashboard` 内部如需"任务编号 → 路径"映射,必须按 §规则 3 嵌套式解析,不可降级到旧格式
  - **对历史的处理**:旧格式(`REQ-00001-001`)作为**字面字符串**透传,不解析;新格式才进入"指向路径"的解析路径
  - 见本文件"REQE-00001"条目的"决策点"
- **来源**:`./assistants/V0.0.1/require/REQ-00002/RESULT.md` + `./assistants/rules/encoding-conventions.md`(扫描于 2026-06-04 12:50)

### REQ-00003(版本:V0.0.1)— 优化 `code-rule` 技能
- **关联点**:
  - REQ-00003 的 SKILL.md 扩展明确写出:`code-rule` 是所有"项目级编码规范"的唯一添加入口
  - REQ-00004 的"展示"能力需要消费 `code-rule` 维护的规范(例如 `dashboard-conventions.md §规则 1`、`encoding-conventions.md`)
- **对本需求的影响**:
  - **规范遵循**:`code-dashboard` 自身若需要写"展示规则"或"字段说明",按 `code-rule` 的 Type B(CLAUDE.md)/Type A(rules/)惯例;**本需求不**主动写规范(留作后续 `code-rule` 沉淀)
  - **CLAUDE.md 已有的"AI 工作约定"小节**(`plugins/code-skills/CLAUDE.md`)是 AI 协作者读取的入口;`code-dashboard` 自身的行为约定(尤其是"展示策略"与"建议策略")未来若纳入,应追加到此节
- **来源**:`./assistants/V0.0.1/require/REQ-00003/RESULT.md` + `./assistants/rules/skill-conventions.md` §规则 1

## 跨需求聚合(供 `code-design` 阶段权衡)

| 维度 | 涉及需求 | 共性 | 处理建议 |
| --- | --- | --- | --- |
| 数据源格式 | REQ-00001 / REQ-00002 | 看板"任务清单"区段中,旧/新两种任务编号字面共存 | `code-dashboard` 解析时**只解析新格式**;旧格式作为字符串原样显示(避免误判) |
| 规范消费 | REQ-00003 | `code-dashboard` 也要"读取" `code-rule` 维护的规范 | 至少读 `dashboard-conventions.md` 与 `encoding-conventions.md` |
| 边界继承 | 全部 3 条 | REQ-00004 是 V0.0.2 的首个需求,需继承 V0.0.1 已有的"不修改范围"(marketplace.json / plugin.json / 其他 7 个 SKILL.md frontmatter) | `code-dashboard` 只新增自身技能目录 + 修改 CLAUDE.md(若需)+ 必要时改 README |

## V0.0.0 EXISTING-* 任务
- `./assistants/V0.0.0/` 无独立的需求文档(以 `EXISTING-NNN` 形式散落在 EXISTING 索引中)
- 看板模板与字段约定**已在 V0.0.1 REQ-00001 起固定**;`code-dashboard` 直接消费 V0.0.2 之后所有版本的看板
- **跨版本归档场景**:若用户在 `code-dashboard` 中输入"切到 V0.0.0"或类似指令,属于 `code-version` 范畴,本需求不实现(留作 follow-up)
