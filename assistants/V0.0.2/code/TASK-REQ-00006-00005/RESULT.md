# 改修总结 — TASK-REQ-00006-00005

## 1. 任务信息

- **任务编码**:`TASK-REQ-00006-00005`
- **任务标题**:`[新增] 写 templates/qanda-README.md 模板(用途/命名/引用/维护)`
- **类型**:新增
- **触发/来源**:需求新增
- **关联任务**:无
- **前置任务**:无
- **来源 PLAN.md**:`./assistants/V0.0.2/plan/REQ-00006/PLAN.md` v1.4
- **完成时间**:2026-06-04 17:56
- **完成人**:wangmiao
- **提交哈希**:`<不提交 — 留 dirty tree 由 T-007 后整体 commit>`

## 2. 改修内容总览

| 类别 | 路径 | 操作 | 大小 |
| --- | --- | --- | --- |
| 新增 | `plugins/code-skills/skills/code-publish/templates/qanda-README.md` | Write | 134 行,~5 KB |

**总计**:1 个新文件,0 个修改文件,0 个删除文件。

## 3. 详细改动

### 新增 `plugins/code-skills/skills/code-publish/templates/qanda-README.md`

#### 3.1 路径合规性

- ✓ 位于 `plugins/code-skills/skills/code-publish/templates/` 子目录
- ✓ 文件名 `qanda-README.md`(kebab-case)
- ✓ 符合 `module-conventions.md §规则 1`

#### 3.2 章节结构(4 大章节)

| 章节 | 内容 |
| --- | --- |
| H1 | `# assistants/qanda/ — 项目级 Q&A 长期沉淀目录` |
| 文首警示 | 当前人工维护(Q-2 锁定 A) |
| `## 用途` | 5 类典型内容(部署/升级/初始化/首次/安全性能) |
| `## 文件命名建议` | 7 个具体示例 + 命名约定(kebab-case / 简洁 / `-faq` 后缀 / 避免特殊字符) |
| `## 引用规范` | 4 段(被聚合规则 / 文件内容格式建议 / 与 publish/Q&A.md 区别) |
| `## 维护方式` | 4 步流程 + 当前 v1 / 未来 v2 / "不做的事"3 条 |

#### 3.3 与 T-004 Q&A.md 模板的交叉引用

| 文档 | 引用方向 |
| --- | --- |
| T-004 Q&A.md 模板 | 4 步"如何添加 Q&A 内容"指南**指向** `qanda/README.md` |
| T-005 qanda-README.md | "引用规范"章节**显式说明** `code-publish` 如何聚合本目录 |

**完整闭环**:
- T-004 告诉用户"做什么"(读 README / 创建文件 / 写内容 / 重跑)
- T-005 告诉用户"怎么做"(具体命名 / 具体内容格式 / 引用规则 / 维护步骤)

## 4. 关键决策与权衡(8 项)

| # | 决策 | 选定 | 理由 |
| --- | --- | --- | --- |
| IT-1 | H1 标题 | `# assistants/qanda/ — 项目级 Q&A 长期沉淀目录` | 与 design §4.4 严格一致 |
| IT-2 | 4 章节结构 | 用途/命名/引用/维护 | design 显式要求 |
| IT-3 | 命名示例 7 个 | 覆盖 7 大场景 | 表格形式更易扫描 |
| IT-4 | 显式排除 README.md | 与 Q-2 锁定 + FR-5 对齐 | 避免误聚合 |
| IT-5 | 维护方式"暂时人工" | Q-2 锁定 | 不假设 v2 |
| IT-6 | 不写"如何贡献"等元说明 | 项目无 PR 流程 | 收敛 |
| IT-7 | 不写"内容政策" | 项目无审查机制 | 收敛 |
| IT-8 | 不反向引用 SKILL.md | 模块边界 | qanda/ 是项目级共享,不应知道 code-publish |

## 5. 偏离设计/规范的地方

详 `deviations.md`。**0 项与设计冲突的偏离**,7 项实现细节增量/收敛/对比(均为 NFR-5 / NFR-9 合规范围内的实现选择)。

## 6. 验证结果(详 `compile-and-run.md`)

| 验证项 | 结论 |
| --- | --- |
| 模板路径合规 | ✓ `plugins/.../templates/qanda-README.md` |
| 4 大章节齐全 | ✓ |
| 命名建议 7 示例 | ✓ |
| 引用规范 4 段齐全 | ✓ |
| 维护方式 4 步 + 不做的事 3 条 | ✓ |
| 文首警示 Q-2 锁定 | ✓ |
| `module-conventions §规则 1` | ✓ |
| 0 修改既有 | ✓ |

## 7. 已知问题/未完成项

### 已知问题
- **无**

### 未完成项(由后续任务承接)
- **T-006**(assistants-layout.md)
- **T-007**:端到端验证
- **Q-D-3**(留 v2):`publish-conventions.md` 沉淀

## 8. 关联任务与提交

- **关联原任务**:无
- **关联后续任务**:T-006, T-007, T-008
- **Git 提交**:**未提交**(NFR-3)

## 9. qanda/README.md vs 其他 README 的对比

| 文档 | 位置 | 篇幅 | 主要读者 |
| --- | --- | --- | --- |
| `qanda/README.md`(本任务) | `assistants/qanda/`(项目级) | 134 行 | 项目维护者(向 qanda/ 添加内容的人) |
| `publish/Q&A.md`(T-004 模板) | `plugins/.../code-publish/templates/Q&A.md`(技能级) | 63 行(动态聚合后更大) | 运维 / 现场支持(发布后查阅) |
| `code-publish/README.md`(T-006 即将复制范式) | `plugins/.../code-publish/`(项目级) | ~100 行(标准) | 项目浏览者 |

**模块边界**:
- `qanda/README.md`:项目级共享,跨版本,**维护说明**
- `publish/Q&A.md`:版本产物,本版本发布,**问答本身**
- `code-publish/README.md`:项目级,描述技能本身,**使用文档**

## 10. 步骤 14 状态更新(PLAN.md)

| 字段 | 旧值 | 新值 |
| --- | --- | --- |
| 开发状态 | 进行中 | **已完成** |
| 完成时间 | — | 2026-06-04 17:56 |
| 完成人 | — | wangmiao |
| 涉及文件 | (空) | `plugins/code-skills/skills/code-publish/templates/qanda-README.md`(134 行,~5 KB) |
| 提交哈希 | (空) | (不提交) |

## 11. 下一步建议

1. **下一任务**:`/code-skills:code-it TASK-REQ-00006-00006`(assistants-layout.md,0.2d)
2. **可并行**:`/code-skills:code-it TASK-REQ-00006-00008`(双 README 同步,0.3d)
3. **收尾**:`/code-skills:code-it TASK-REQ-00006-00007`(不变量自检 + 端到端 3 场景)
