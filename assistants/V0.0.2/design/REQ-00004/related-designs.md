# 关联设计 — REQ-00004

更新时间:2026-06-04 15:50
版本:V0.0.2

## 扫描范围
- 同版本:`./assistants/V0.0.2/design/`(空,本设计为首个)
- 跨版本:`./assistants/V0.0.1/design/REQ-0000{1,2,3}/`

## 关联设计清单

### REQ-00001(V0.0.1)— Marketplace 改名落地
- **路径**:`./assistants/V0.0.1/design/REQ-00001/RESULT.md`
- **关联点**:
  - 本需求的数据源(`./assistants/<版本号>/RESULT.md` 三大区段)的**首条历史样本**来自 REQ-00001 引入的看板模板
  - REQ-00001 创建的 4 任务 + 后续派生 1 任务(`REQ-00001-005`)是看板"任务清单"区段的内容
- **对本设计的影响**:
  - **数据兼容性**:`code-dashboard` 读取 REQ-00001 的任务行时,会看到字面 `REQ-00001-001`(无 `TASK-` 前缀)。这与 `encoding-conventions.md §规则 3`(v2 锁定嵌套式 `TASK-REQ-...`)不一致。
  - **NFR-3 已落定**:`code-dashboard` 解析任务编号时**同时**识别两种格式;新格式生成的 `/code-it TASK-...` 命令严格按新格式;旧格式**仅作为字符串原样显示**,不进入"路径解析"路径
  - **设计参照**:REQ-00001 设计第 §2.2 节"变更传播路径"图是本设计"下一步建议生成器"算法参照

### REQ-00002(V0.0.1)— 编码格式统一
- **路径**:`./assistants/V0.0.1/design/REQ-00002/RESULT.md`
- **关联点**:
  - 显式定义了 3 类编码的**权威源**(`./assistants/rules/encoding-conventions.md`)
  - `code-dashboard` 输出的"下一步建议"需要引用这些编码格式(例如 `建议执行 /code-it TASK-REQ-00004-001`),链接指向必须严格符合规范
- **对本设计的影响**:
  - **必须遵守**:`code-dashboard` 内部"任务编号 → 路径"映射必须按 §规则 3 嵌套式解析
  - **对历史的处理**:旧格式(`REQ-00001-001`)作为**字面字符串**透传,不解析;新格式才进入"指向路径"的解析路径
  - **Q-5/Q-6 算法参照**:REQ-00002 §3 的 Q-5 / Q-6 给出"父级类型推断 + 路径路由"算法,本设计模块"任务编号解析器"直接采纳

### REQ-00003(V0.0.1)— 优化 `code-rule` 技能
- **路径**:`./assistants/V0.0.1/design/REQ-00003/RESULT.md`
- **关联点**:
  - REQ-00003 的 SKILL.md 扩展明确写出:`code-rule` 是所有"项目级编码规范"的唯一添加入口
  - REQ-00004 的"展示"能力需要消费 `code-rule` 维护的规范(例如 `dashboard-conventions.md §规则 1`、`encoding-conventions.md`)
- **对本设计的影响**:
  - **规范遵循**:`code-dashboard` 自身若需要写"展示规则"或"字段说明",按 `code-rule` 的 Type B(CLAUDE.md)/ Type A(rules/)惯例;**本需求不**主动写规范(留作后续 `code-rule` 沉淀)
  - **CLAUDE.md 已有的"AI 工作约定"小节**(`plugins/code-skills/CLAUDE.md`)是 AI 协作者读取的入口;`code-dashboard` 自身的行为约定(尤其是"展示策略"与"建议策略")未来若纳入,应追加到此节
  - **module-conventions → directory-conventions 迁移**:REQ-00003 触发了该迁移;本设计在 `module-breakdown.md` 引用时显式标注

## V0.0.0 基线
- `./assistants/V0.0.0/design/` 不存在
- V0.0.0 EXISTING-NNN 编码在看板"任务清单"区段中不出现(`code-init` 登记的是"功能",不是"任务"),`code-dashboard` 不感知
- V0.0.0 EXISTING-010(`code-review`)是 `code-dashboard` 的"行为对标"对象(只读型)

## 跨需求聚合(本设计权衡)

| 维度 | 涉及需求 | 共性 | 处理 |
| --- | --- | --- | --- |
| 数据源格式 | REQ-00001 / 00002 | 看板"任务清单"区段中,旧/新两种任务编号字面共存 | 解析时**只解析新格式**;旧格式作为字符串原样显示(避免误判) |
| 规范消费 | REQ-00003 | `code-dashboard` 也要"读取" `code-rule` 维护的规范 | 至少读 `dashboard-conventions.md` + `encoding-conventions.md`(本设计**不**新增) |
| 边界继承 | 全部 3 条 | REQ-00004 是 V0.0.2 的首个设计,继承 V0.0.1 已有的"不修改范围"(`marketplace.json` / `plugin.json` / 其他 10 个 SKILL.md frontmatter) | `code-dashboard` 只新增自身技能目录 + 可选改 CLAUDE.md / README(同次提交) |
| 看板模板 | REQ-00001 | 看板"任务清单" / "缺陷清单" 列结构由 REQ-00001 锁定 | `code-dashboard` 解析时**严格按列定义**;不假设"标题列未来可能改" |
