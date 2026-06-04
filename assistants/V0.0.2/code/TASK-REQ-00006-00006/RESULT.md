# 改修总结 — TASK-REQ-00006-00006

## 1. 任务信息

- **任务编码**:`TASK-REQ-00006-00006`
- **任务标题**:`[新增] 写 templates/assistants-layout.md 模板(沿用范式 + publish/qanda 段)`
- **类型**:新增
- **触发/来源**:需求新增
- **关联任务**:无
- **前置任务**:无
- **来源 PLAN.md**:`./assistants/V0.0.2/plan/REQ-00006/PLAN.md` v1.5
- **完成时间**:2026-06-04 18:00
- **完成人**:wangmiao
- **提交哈希**:`<不提交 — 留 dirty tree 由 T-007 后整体 commit>`

## 2. 改修内容总览

| 类别 | 路径 | 操作 | 大小 |
| --- | --- | --- | --- |
| 新增 | `plugins/code-skills/skills/code-publish/templates/assistants-layout.md` | Write | 172 行,~6 KB |

**总计**:1 个新文件,0 个修改文件,0 个删除文件。

## 3. 详细改动

### 新增 `plugins/code-skills/skills/code-publish/templates/assistants-layout.md`

#### 3.1 路径合规性

- ✓ 位于 `plugins/code-skills/skills/code-publish/templates/` 子目录
- ✓ 文件名 `assistants-layout.md`(沿用范式)
- ✓ 符合 `module-conventions.md §规则 1`

#### 3.2 章节结构(6 段标准 + 1 段本技能特定)

| 章节 | 范式 vs 本任务 |
| --- | --- |
| H1 | `# 工作目录布局参考 — code-publish` |
| 文首引言 | 本技能在 code-version 之上工作;**只描述 code-publish 特有扩展** |
| `## 整体布局` | **完整目录树**(含 publish/ 与 qanda/) |
| `## code-publish 的特定扩展` | **本任务新增**(4 段:qanda / publish / RESULT.md / .current-version) |
| `## 关键点` | 3 段(5 类资源 / 模板双向引用 / 可写目录边界) |
| `## 多版本隔离` | 范式 |
| `## 跨技能协作` | 范式 + 本技能"只读"角色 |
| `## 多项目隔离` | 范式 |

#### 3.3 目录树(关键段)

```
./assistants/
├── rules/                          ← 跨版本共享,只读
├── .current-version                ★ 当前激活版本标记(本技能只读)
├── qanda/                          ★ 项目级 Q&A 长期沉淀(本技能顺带创建)
│   ├── README.md
│   └── <主题>.md
├── v1.0.0/                         ← 版本工作空间
│   ├── RESULT.md                   (本技能只读消费 3 区段)
│   ├── require/  design/  plan/  code/  test/  review/
│   └── publish/                    ★ 本技能产出
│       ├── DEPLOY.md
│       ├── UPDATE.md                (基线跳过)
│       └── Q&A.md
```

## 4. 关键决策与权衡(7 项)

| # | 决策 | 选定 | 理由 |
| --- | --- | --- | --- |
| IT-1 | 沿用 code-version 范式 | 完全沿用 6 段结构 | 0 认知成本 |
| IT-2 | 目录树与 SKILL.md 完全一致 | 同一目录树,两种用途 | 所见即所得 |
| IT-3 | 目录树不写内联注释 | 注释放"## 关键点" | 代码块更易读 |
| IT-4 | 标注读/写角色 | 透明性 | FR-7/8 |
| IT-5 | 不写"如何使用本技能" | 属 SKILL.md "## 工作流程" | 模块边界 |
| IT-6 | 不反向引用 SKILL.md | 独立可读 | 模块边界 |
| IT-7 | 不写"未来扩展" | 当前布局参考 | NFR-5 |

## 5. 偏离设计/规范的地方

详 `deviations.md`。**0 项与设计冲突的偏离**,7 项实现细节增量/收敛(均为 NFR-5 / NFR-9 合规范围内的实现选择)。

## 6. 验证结果(详 `compile-and-run.md`)

| 验证项 | 结论 |
| --- | --- |
| 模板路径合规 | ✓ `plugins/.../templates/assistants-layout.md` |
| 6 段标准 + 1 段特定 | ✓ |
| 目录树含 `publish/` 与 `qanda/` | ✓ |
| 5 类资源与 4 类读/写角色 | ✓ |
| 不引用 SKILL.md(模块边界) | ✓ |
| 0 修改既有 | ✓ |

## 7. 已知问题/未完成项

### 已知问题
- **无**

### 未完成项(由后续任务承接)
- **T-007**:端到端验证 + 不变量自检(包含与 SKILL.md 一致性检查)
- **Q-D-1 / Q-D-3**(留 v2)

## 8. 关联任务与提交

- **关联原任务**:无
- **关联后续任务**:T-007, T-008
- **Git 提交**:**未提交**(NFR-3)

## 9. 与 `code-version` 范式 `assistants-layout.md` 的关键差异

| 差异点 | code-version 范式 | code-publish(本任务) |
| --- | --- | --- |
| H1 标题 | `# 工作目录布局参考 — code-version` | `# 工作目录布局参考 — code-publish` |
| 目录树 | **不**含 `publish/` + `qanda/` | **含** 两者 |
| `## 关键点` 关键点 5 | 10 个 `code-*` 技能 | **额外**加 code-publish 描述 |
| `## 跨技能协作` | 10 个 `code-*` 技能 | **额外**列 code-publish(纯只读) |
| 是否有"本技能特定段" | 否(范式本身) | 是(`## code-publish 的特定扩展`) |
| 反向引用 SKILL.md | 否 | 否 |

## 10. 模板的双向引用(SKILL.md ↔ assistants-layout.md)

| 文档 | 用途 | 目录树位置 |
| --- | --- | --- |
| `SKILL.md`(T-001) | 技能入口;目录树在"## 工作目录约定"小节 | 简版,~40 行 |
| `assistants-layout.md`(本任务) | 标准技能资产;目录树在"## 整体布局"独立小节 | 详版,~100 行 |

**两文档内容应保持一致**(同次维护);本任务执行时**已对齐**。

## 11. 步骤 14 状态更新(PLAN.md)

| 字段 | 旧值 | 新值 |
| --- | --- | --- |
| 开发状态 | 进行中 | **已完成** |
| 完成时间 | — | 2026-06-04 18:00 |
| 完成人 | — | wangmiao |
| 涉及文件 | (空) | `plugins/code-skills/skills/code-publish/templates/assistants-layout.md`(172 行,~6 KB) |
| 提交哈希 | (空) | (不提交) |

## 12. 下一步建议

1. **下一任务**:`/code-skills:code-it TASK-REQ-00006-00008`(双 README 同步,0.3d)
2. **收尾**:`/code-skills:code-it TASK-REQ-00006-00007`(不变量自检 + 端到端 3 场景)
