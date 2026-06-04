# 改修总结 — TASK-REQ-00006-00004

## 1. 任务信息

- **任务编码**:`TASK-REQ-00006-00004`
- **任务标题**:`[新增] 写 templates/Q&A.md 模板(占位章节 + 提示)`
- **类型**:新增
- **触发/来源**:需求新增
- **关联任务**:无
- **前置任务**:无
- **来源 PLAN.md**:`./assistants/V0.0.2/plan/REQ-00006/PLAN.md` v1.3
- **完成时间**:2026-06-04 17:52
- **完成人**:wangmiao
- **提交哈希**:`<不提交 — 留 dirty tree 由 T-007 后整体 commit>`

## 2. 改修内容总览

| 类别 | 路径 | 操作 | 大小 |
| --- | --- | --- | --- |
| 新增 | `plugins/code-skills/skills/code-publish/templates/Q&A.md` | Write | 63 行,~2 KB |

**总计**:1 个新文件,0 个修改文件,0 个删除文件。

## 3. 详细改动

### 新增 `plugins/code-skills/skills/code-publish/templates/Q&A.md`

#### 3.1 路径合规性

- ✓ 位于 `plugins/code-skills/skills/code-publish/templates/` 子目录
- ✓ 文件名 `Q&A.md`(特殊字符,严格按 needs §6.3 命名)
- ✓ 符合 `module-conventions.md §规则 1`

#### 3.2 模板结构(2 章节 + 5 子段)

| 章节 | 内容 |
| --- | --- |
| **H1** | `# 发布部署 Q&A — <本版本号>`(自动填充) |
| **文首引言** | `> 本手册聚合自 \`assistants/qanda/\`,供发布部署中遇到问题时查阅。` |
| **文首警示** | `⚠ 本手册当前为占位状态` + 提示 |
| **H2 占位章节** | `## 占位:常见问题(待补充)` |
| 占位章节内 | 4 步"如何添加 Q&A"指南 + 完整生成结果示例 + 排除规则 + 排序规则 |

#### 3.3 Placeholder 集合(1 个自动)

| Placeholder | 类别 | 出现位置 |
| --- | --- | --- |
| `<本版本号>` | **自动**(`code-publish` 替换) | H1 标题 + 工作流提示段 |

#### 3.4 占位章节内的 4 步指南

```
1. 阅读格式规范:assistants/qanda/README.md
2. 创建 Q&A 文件:在 assistants/qanda/ 下新建 <主题>.md
3. 写入 Q&A 内容:每个文件用 Markdown 写 Q&A
4. 重跑 code-publish
```

#### 3.5 完整生成结果示例(fenced code block)

假设 qanda/ 有 2 个文件 (`deploy-faq.md` + `db-init-faq.md`),生成结果会包含:
- H1
- 引言
- `## 1. deploy-faq(来源:qanda/deploy-faq.md)` + 内容
- `## 2. db-init-faq(来源:qanda/db-init-faq.md)` + 内容
- 占位章节(兜底,实际不再有内容)

#### 3.6 排除规则 + 排序规则(显式说明)

- **排除**:`assistants/qanda/README.md` 不被聚合
- **排序**:按文件名字典序(确保幂等 NFR-6)

#### 3.7 与 QandaAggregator(算法 6)的集成

| 阶段 | QandaAggregator 行为 |
| --- | --- |
| 0 个非 README .md | 用本模板原样写入 `publish/Q&A.md` |
| ≥ 1 个非 README .md | 渲染:`占位模板 + 占位章节前插入 N 个聚合章节` → 写入 `publish/Q&A.md` |
| qanda/ 不存在 | (由 QandaScaffolder 先创建 README.md);Aggregator 退化为"0 文件"分支 |

## 4. 关键决策与权衡(7 项)

| # | 决策 | 选定 | 理由 |
| --- | --- | --- | --- |
| IT-1 | H1 标题 | `# 发布部署 Q&A — <本版本号>` | 替换后即时可见 |
| IT-2 | 引言段 | 短句"聚合自 + 何时用" | NFR-9 |
| IT-3 | 占位章节命名 | `## 占位:常见问题(待补充)` | 强提示"待办" |
| IT-4 | 占位提示 | 指向 qanda/README.md + 提示重跑 | 模块间协作 |
| IT-5 | 不预设"问题分类" | 不假设 | NFR-5 通用性 |
| IT-6 | 不写"如何提交" | 属 qanda/README.md | 模块边界 |
| IT-7 | 不写"具体问答" | 由 qanda/ 动态聚合 | Q-2 锁定 |

## 5. 偏离设计/规范的地方

详 `deviations.md`。**0 项与设计冲突的偏离**,5 项实现细节增量/收敛(均为 NFR-5 / NFR-6 / NFR-9 合规范围内的实现选择)。

## 6. 验证结果(详 `compile-and-run.md`)

| 验证项 | 结论 |
| --- | --- |
| 模板路径合规 | ✓ `plugins/.../templates/Q&A.md` |
| H1 + 引言 + 占位章节 | ✓ |
| 4 步添加 Q&A 指南 | ✓ |
| 完整生成结果示例 | ✓ |
| 排除/排序规则说明 | ✓ |
| `module-conventions §规则 1` | ✓ |
| 0 修改既有 | ✓ |

## 7. 已知问题/未完成项

### 已知问题
- **无**

### 未完成项(由后续任务承接)
- **T-005**(qanda-README.md):`assistants/qanda/README.md` 骨架 — 模板中的"4 步指南"指向此文件
- **T-006**(assistants-layout.md)
- **T-007**:端到端验证
- **Q-D-1**(留 v2):`code-publish` 注册到 marketplace.json
- **Q-D-3 ~ Q-D-7**(留 code-review / 其他 REQ)

## 8. 关联任务与提交

- **关联原任务**:无
- **关联后续任务**:T-005, T-006, T-007, T-008
- **Git 提交**:**未提交**(NFR-3)

## 9. 步骤 14 状态更新(PLAN.md)

| 字段 | 旧值 | 新值 |
| --- | --- | --- |
| 开发状态 | 进行中 | **已完成** |
| 完成时间 | — | 2026-06-04 17:52 |
| 完成人 | — | wangmiao |
| 涉及文件 | (空) | `plugins/code-skills/skills/code-publish/templates/Q&A.md`(63 行,~2 KB) |
| 提交哈希 | (空) | (不提交) |

## 10. Q&A.md vs DEPLOY.md / UPDATE.md 对比

| 维度 | DEPLOY.md | UPDATE.md | Q&A.md |
| --- | --- | --- | --- |
| 篇幅 | 245 行 | 365 行 | **63 行** |
| 章节数 | 8 | 8 | **1 (占位)** |
| 内容来源 | 全部硬编码 | 全部硬编码 | **动态聚合**(QandaAggregator 渲染) |
| placeholder | 14 | 17+ | **1** |
| checkbox | 15 | 26 | **0** |
| 与 `code-publish` 集成 | 直接复制 + 替换 | 直接复制 + 替换 | **复制 + 动态插入** |

**为什么 Q&A.md 模板这么小?**
- DEPLOY.md / UPDATE.md 是"步骤手册",每一步需用户补全 → 内容丰富
- Q&A.md 是"问答手册",具体问答在 qanda/(用户管理) → 模板只占位
- 模板的"小"是**正确的设计选择**(data-changes.md §4.3 明确只要求"文首 + 引言 + 占位章节")
- QandaAggregator 负责把 qanda/ 内容**动态插入**,无需在模板中预设

## 11. 下一步建议

1. **下一任务**:`/code-skills:code-it TASK-REQ-00006-00005`(qanda-README.md,0.2d) — Q&A.md 模板的"4 步指南"明确指向此文件
2. **可并行**:`/code-skills:code-it TASK-REQ-00006-00006` / `00008`(2 任务独立,共 ~0.5d)
3. **收尾**:`/code-skills:code-it TASK-REQ-00006-00007`(不变量自检 + 端到端 3 场景)
