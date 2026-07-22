# code-skills 共享契约

> 本文件是 `code-skills` 仓库的**单一事实来源**,定义所有跨子命令共享的字段、状态、章节锚点和 schema。
> 所有子命令的 SKILL.md / common.md / 模板,凡涉及下列契约,**必须**按本文件定义实现,不得各自定义。

## 1. RESULT.md schema(`dashboard-v2`)

### 1.1 schema 标记

```
<!-- schema: dashboard-v2 -->
```

位于 `RESULT.md` 头部注释块。

### 1.2 强制结构

```markdown
# 版本开发进度看板 — <版本号>
<!-- schema: dashboard-v2 -->

## 文档头
- 版本号:<V>
- 创建时间:YYYY-MM-DD HH:mm
- 最近更新:YYYY-MM-DD HH:mm
- 创建人:<name>
- 负责人:<name>
- 状态:活跃
- 描述:<一行描述>

## 需求清单
| 需求编码 | 标题 | 进度文档 |
| --- | --- | --- |
| REQ-NNNNN | <标题> | [PROCESS.md](req/REQ-NNNNN/PROCESS.md) |

## 缺陷清单
| 缺陷编号 | 标题 | 进度文档 |
| --- | --- | --- |
| BUG-NNNNN | <标题> | [PROCESS.md](fix/BUG-NNNNN/PROCESS.md) |

## 变更记录
| 时间 | 变更类型 | 变更摘要 | 关联项 |
| --- | --- | --- | --- |
```

### 1.3 禁止列

以下动态列**不得**出现在 dashboard-v2 的"需求清单"/"缺陷清单"中(状态从 `PROCESS.md` / `PLAN.md` / `BUG.md` / `TASK-N.md` 派生):

- 状态 / 优先级 / 测试状态 / 开发状态 / 进度(百分比)
- 完成时间 / 起始时间 / 任何时间字段(时间数据只走 PROCESS.md)

### 1.4 不保留旧 schema 兼容模式

> 用户 2026-07-22 10:55 确认:`dashboard-v1`(含"统计"行、动态状态列)不再保留兼容模式。现存 V0.0.6 RESULT.md 由 REQ-OPT-00001 TASK-00014 就地升级。

---

## 2. 状态字面表

### 2.1 阶段(PROCESS.md 用)

```
INIT → REQUIRE → DESIGN → PLAN → CODING → CHECK → DONE
```

枚举值(严格匹配,大小写敏感):`INIT` / `REQUIRE` / `DESIGN` / `PLAN` / `CODING` / `CHECK` / `DONE`

### 2.2 任务开发状态(PLAN.md / TASK-N.md 用)

枚举值(中文,严格匹配):

```
待开始
进行中
已完成
已取消
阻塞
待重新评估
```

### 2.3 任务测试状态(PLAN.md / TASK-N.md 用)

枚举值(中文,严格匹配):

```
未编写
已编写
已运行-通过
已运行-失败
不适用
阻塞
```

**流转规则**(PLAN 模板附录,FR-7 来源):

| 触发事件 | 当前 → 转移后 |
| --- | --- |
| 任务创建(代码型) | 未编写 |
| 任务创建(文档型) | 不适用 |
| 任务创建(配置型) | 不适用 |
| 编译通过 | (无变化) |
| 单测编写完成 | 未编写 → 已编写 |
| 测试运行通过 | 已编写 → 已运行-通过 |
| 测试运行失败 | 已编写 → 已运行-失败 |
| 运行时缺失(经用户授权) | * → 阻塞 |
| 用户明示跳过 | * → 不适用 |

**判定"可发布"**:`已完成` ∩ {`已运行-通过`, `不适用`}

### 2.4 运行时状态(`TASK-N.md` 运行时行用)

机器值(机器记录、模板直接使用):

```
configured        — 运行时已就绪
user-provided     — 用户提供运行时路径
auto-installed    — 系统包管理器自动安装
skipped           — 用户跳过(明示同意)
unavailable       — 运行时不可用
```

展示映射(文档展示):

| 机器值 | 中文 |
| --- | --- |
| configured | 已配置 |
| user-provided | 由用户提供路径 |
| auto-installed | 由用户授权自动安装 |
| skipped | 由用户跳过 |
| unavailable | 未配置 |

> FR-10 来源:模板与 reference 统一为这 5 项机器值;文档展示再映射为中文。

---

## 3. 看板派生接口

### 3.1 `deriveItemStatus(reqOrBugId)`

**用途**:根据 `req/<REQ>/PROCESS.md`、`req/<REQ>/PLAN.md`、`fix/<BUG>/BUG.md` 派生某需求/缺陷的当前状态。

**签名**:
```js
function deriveItemStatus(reqOrBugId: string): ItemStatus
```

**返回结构**(`ItemStatus`):
```ts
type ItemStatus = {
  stage: 'INIT' | 'REQUIRE' | 'DESIGN' | 'PLAN' | 'CODING' | 'CHECK' | 'DONE' | 'UNKNOWN'
  devStatus: '待开始' | '进行中' | '已完成' | '已取消' | '阻塞' | '待重新评估' | 'N/A'
  testStatus: '未编写' | '已编写' | '已运行-通过' | '已运行-失败' | '不适用' | '阻塞' | 'N/A'
  completed: boolean
}
```

**异常行为**:编号 / PROCESS.md / PLAN.md 不存在 → 返回 `{ stage: 'UNKNOWN', devStatus: 'N/A', testStatus: 'N/A', completed: false }`,**不抛错**。

**判定 `completed`**:`stage === 'DONE' && devStatus === '已完成' && testStatus ∈ { '已运行-通过', '不适用' }`

**使用方**:`/code ver --publish`、看板高优先级缺陷统计、建议生成、`/code faq --summary`。

### 3.2 看板读取约定

- 看板(本 schema-v2 RESULT.md)**不存**任何动态状态
- 所有看板查询(高优先级缺陷、建议生成、统计)走 `deriveItemStatus()`
- 合并时按"已完成" = 发布就绪;否则归入"未完成"

---

## 4. FAQ 导出字段映射

### 4.1 字段映射表

| 字段 | 模板标题(章节号兜底) | 锚点(优先) |
| --- | --- | --- |
| FR_LIST | `## 3. 功能需求(FR)` | `<!-- code-skills:field=FR_LIST -->` |
| NFR_LIST | `## 4. 非功能需求(NFR)` | `<!-- code-skills:field=NFR_LIST -->` |
| AC_LIST | `## 5. 验收标准(AC)` | `<!-- code-skills:field=AC_LIST -->` |
| RELATED | `## 6. 关联需求` | `<!-- code-skills:field=RELATED -->` |
| CLARIFICATIONS | (来自 `clarifications.md`,无锚点) | (无) |

### 4.2 解析顺序

1. 优先匹配 `<!-- code-skills:field=<F> -->` 锚点
2. 锚点不存在 → 匹配章节标题 `## <N>. <标题>`
3. 都不存在 → 标记"未识别字段",**不抛错**

### 4.3 锚点语法

```markdown
<!-- code-skills:field=<FIELD_NAME> -->
## 3. 功能需求(FR)
...
```

- 字段名:大写 + 下划线(`FR_LIST` / `NFR_LIST` / `AC_LIST` / `RELATED`)
- 位置:对应章节标题**之前**(同段)或**之后**(单独段落)

---

## 5. 三态确认契约

| 模式 | 阶段边界 | 阶段内补充内容确认 |
| --- | --- | --- |
| 默认 | 自动继续,无需中断 | 需要用户确认补充的内容(需求澄清、方案选型、任务拆分等)等待用户确认,不自动跳过 |
| --confirm | 每阶段完成后强制确认(产出物路径 + 重读 + 继续/中止) | 正常询问 |
| --auto | 自动继续 | 所有需要用户确认补充的内容使用推荐选项自动继续,无需中断等待 |

**关键边界**(用户 2026-07-22 10:42 确认):

- 默认模式 ≠ 全部跳过询问;它跳过的是**阶段边界**,不跳过**阶段内补充内容确认**;--auto 才是两个都跳过
- --confirm 模式 = 阶段边界增强确认 + 阶段内正常询问
- --auto 模式 = 阶段边界自动继续 + 阶段内用推荐项

**适用范围**:所有引用三态的文档(README、CLAUDE.md、req/SKILL.md、fix/SKILL.md、req/common.md、help/SKILL.md)必须按本表统一表述。

---

## 6. `/code rule` Type A/B/C 写权限

| 类型 | 目标文件 | 允许动作 | 完成条件 |
| --- | --- | --- | --- |
| A | `assistants/rules/<category>.md` | 新建或末尾追加 | 分类、级别、范围、例外已记录 |
| B | 明确指定的 `CLAUDE.md` | 仅追加 AI 工作约定区段 | 指引编号唯一,未改仓库说明区 |
| C | 明确指定的 template | 末尾/字段内二选一并记录 | 提示位置和触发字段可定位 |

> FR-14 来源:本表是 `/code rule` 的写权限**唯一事实源**;`references/rule/SKILL.md` 必须引用本表,不得另行定义。

---

## 7. `/code ver` 版本同步四步流程

> 用户 2026-07-22 10:58 拍板方案 B:保留自动同步 CWD 描述文件的默认行为,加四步前置。

`/code ver <version>` 默认走四步流程:

1. **差异预览**:扫描 CWD 描述文件(`package.json` / `pom.xml` / `Cargo.toml` / `pyproject.toml` / `manifest.json` 等),`git diff --stat` + 每个文件的 diff 摘要
2. **用户确认**:屏显差异 + AskUserQuestion(继续 / 中止 / 仅修改特定文件)
3. **失败回滚**:写失败 → `git checkout -- <files>` 回退 + 返回非 0
4. **提交记录**:成功后写入版本切换 commit

**声明同步**:`references/ver/SKILL.md:48-53` 的"只读"声明必须改为"默认同步 + 加四步",与本节行为一致。

**`--no-sync` 参数**:若用户需跳过同步,使用此参数,仅更新 `assistants/.current-version`,不触碰 CWD。

---

## 8. `/code merge` worktree 操作契约

### 8.1 dirty 检查(前置)

```
1. 当前 worktree dirty → 拒绝
2. feature worktree dirty → 拒绝
3. target worktree dirty → 拒绝
```

### 8.2 merge 命令

```
git worktree list --porcelain  →  找到 target 主工作区
git -C <main-worktree> merge <feature-branch> --no-ff
```

### 8.3 退出语义

- 有 unresolved 冲突 → 返回非 0 + 屏显冲突文件列表 + **不**报告成功
- 看板自检(FR-13)失败 → 不报告成功 + 返回非 0

### 8.4 `CODE_MERGE_TARGET` 拆分

| 字段 | 含义 |
| --- | --- |
| 分支名 | 如 `main` |
| 远端 ref | 如 `origin/main` |
| 本地 checkout 目标 | 主工作区路径(从 `git worktree list --porcelain` 派生) |

---

## 9. 需求分析技术选型词表

> FR-11 来源:本节是技术选型过滤的**唯一事实源**;`references/req/require.md` 引用本节,不再重复定义。

### 9.1 `decisionKeywords`(只用于延迟到 DESIGN 阶段)

```
技术选型, 实现方式, 框架, 库, 工具, monorepo, single-package,
pnpm, npm, yarn, Jest, Vitest, Mocha, React, Vue, Angular,
数据库, ORM, 消息队列, 缓存, Redis, MongoDB,
架构风格, 部署形态
```

行为:命中任一 → 不弹出 AskUserQuestion,改为追加到 `clarifications.md` 的"延迟到 DESIGN 阶段"区段。

### 9.2 `conflictKeywords`(即使属于技术词也必须在 REQUIRE 阶段确认)

```
互斥, 冲突, 不一致, 版本号, 路径, 状态, 枚举, schema, 字段名
```

行为:命中任一 → 照常弹出 AskUserQuestion(§5c 强制确认);不被 §9.1 延迟。

### 9.3 关键区别

| 维度 | `decisionKeywords` | `conflictKeywords` |
| --- | --- | --- |
| 命中后行为 | 延迟到 DESIGN | 必须在 REQUIRE 确认 |
| 典型词 | 框架 / 库 / ORM / 数据库 | 互斥 / 冲突 / 状态 |
| 判定依据 | "这是怎么实现" | "这影响行为契约" |

### 9.4 校验

`references/req/require.md` 内应**不**重复定义关键词集;`grep -nE "技术选型.{0,3}框架" references/req/require.md` 应无散落定义(允许指向契约层 §9 的引用)。

---

## 10. CHECK 评审维度(9 维)

> FR-8 来源:`templates/req/CHECK.md` 与 `references/req/check.md` 的 9 个评审维度定义以本节为唯一事实源。

| 维度 | 检查项 | 阈值 |
| --- | --- | --- |
| 正确性 | 逻辑是否正确 | — |
| 需求一致性 | 是否覆盖 REQUIRE.md 的全部 FR / AC | FR/AC 对照表 |
| 设计一致性 | 是否与 DESIGN.md 一致(模块/接口/数据) | — |
| 规范 | 是否符合 `./assistants/rules/` 编码规范 | — |
| 安全 | 是否存在安全风险 | — |
| 性能 | 是否存在性能问题 | — |
| 可维护性 | 是否易于维护 | — |
| 测试覆盖 | 关键路径是否有单测覆盖 | 覆盖率 / 不适用理由 |
| 代码行数超标 | 单文件总逻辑行 ≤ 500 / 新增 ≤ 200 | tokei/cloc |

**结论生成**:`必须改` 数量 = 0 → ✅ 通过;否则 ❌ 需改修。CHECK.md 模板与 check.md reference 必须按本表补齐;不得自定义其他维度或减少维度。

---

## 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-07-22 11:08 | v1 | 初始创建 | TASK-REQ-OPT-00001-00001 产出;契约层 8 节:RESULT.md schema / 状态字面 / 看板派生 / FAQ 映射 / 三态确认 / rule Type A/B/C / ver 四步 / merge worktree 契约 | wangmiao |
| 2026-07-22 11:35 | v1.1 | 追加 §9 | 需求分析技术选型词表(decisionKeywords + conflictKeywords),来源 FR-11 | wangmiao |
