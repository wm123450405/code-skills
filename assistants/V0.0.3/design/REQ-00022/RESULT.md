# 概要设计 — REQ-00022(修改 `/code-review` 技能名称为 `/code-check`)

- 需求编码:REQ-00022
- 所属版本:V0.0.3
- 文档版本:v1
- 状态:已锁定
- 责任人:wangmiao
- 创建:2026-06-07
- 最近更新:2026-06-07
- 当前版本:v1
- **上游**:`./assistants/V0.0.3/require/REQ-00022/RESULT.md`(v1,2026-06-07)
- **遵循规范**:`./assistants/rules/` 下 13 个文件(本需求实际触发 4 个,详 §2.5.1)
- **架构对象**:`code-skills` 仓库**自身**的 1 个 `code-*` 技能入口重命名 + 11 类引用方字面量同步(目录 + SKILL.md + JSON + README + 规范 + 模板 + 看板)

---

## 设计目标

> 本小节由 `code-design` 步骤 0b 自动生成,记录用户确认的设计目标。

- **回写时间**:2026-06-07
- **回写触发**:`code-design` 步骤 0b(code-auto 上下文,采纳 --balanced 默认)
- **调用上下文**:`./assistants/.code-auto-running` **存在** → code-auto 上下文
- **本会话沿用**:`code-require` 阶段已收集 4 项用户回答(Q-1 ~ Q-4 全部采纳推荐项)

### 整体设计目标
**`--balanced`**(code-auto 上下文默认;本需求为"硬重命名 + 全局字符串同步",不涉及架构层决策)

### 维度优先级

| 维度 | 优先级 | 依据 |
| --- | --- | --- |
| **功能性** | 中 | code-auto 上下文默认;本需求改造 11 类引用方,功能强度中等 |
| **其它 6 维度** | (略) | 本需求为"字面量重命名",不涉及架构维度;由 `code-plan` 阶段确认 |

### 设计目标对本设计的影响

- 整体=`--balanced` → 不强求扩展性 / 健壮性 / 可维护性;本需求是"字面量重命名"任务,设计意图**简单清晰**(FR-1 ~ FR-7 已锁定)
- 本设计重点关注"38-39 文件 + 1 目录重命名"的执行顺序 + 校验策略

---

## 1. 需求概述(引用上游)

上游 `./assistants/V0.0.3/require/REQ-00022/RESULT.md` 概括了 1 个核心子需求:

- **重命名**:`/code-review` 技能入口 → `/code-check`(硬重命名 + 11 类引用方同步)
- **不追溯**:V0.0.0/V0.0.1/V0.0.2/V0.0.3 历史 review 产物**不**重写(沿用 `migration-mapping §规则 5`)

**关键交叉点**(每条 FR 对应的设计章节):
- FR-1(技能入口重命名)→ §3 模块拆分(目录重命名 + frontmatter + H1)
- FR-2(JSON 同步)→ §3 路径(JSON 文件改动)
- FR-3(10 个其他 SKILL.md 同步)→ §3 模块拆分(SKILL.md description 字段)
- FR-4(README + 规范 + 模板 + 当前看板同步)→ §3 模块拆分(25 个文件改动)
- FR-5(历史不追溯)→ §3.2 关键决策(锁定不追溯范围)
- FR-6(0 改其他技能行为)→ §3.3 不变量
- FR-7(9 条 INV)→ §3.3

**本概设** 在 `code-require` 已产出 FR / NFR / AC 的基础上,给出"系统长什么样"的系统级架构方案(为 `code-plan` 进一步拆解做准备)。

---

## 2. 上游引用(规范遵循)

### 2.1 上游需求

- 来源:`./assistants/V0.0.3/require/REQ-00022/RESULT.md`(v1,2026-06-07)
- 提取的 FR / NFR / AC 数量:**7 FR / 6 NFR / ~33 AC / 9 INV**
- 关键交叉点:
  - FR-1(技能入口重命名)→ §3 步骤 1-2
  - FR-2(JSON 同步)→ §3 步骤 3
  - FR-3(10 个其他 SKILL.md)→ §3 步骤 4
  - FR-4(README + 规范 + 模板 + 看板)→ §3 步骤 5-6
  - FR-5(历史不追溯)→ §3.2 关键决策
  - FR-6(0 改行为)→ §3.3 不变量
  - FR-7(9 INV)→ §3.3

### 2.2 规范遵循清单

| 规范文件 | 类别 | 关键约束摘要 | 本设计遵循情况 |
| --- | --- | --- | --- |
| `skill-conventions.md` | 技能规范 | §规则 1:`name` 与目录名一致 | ✅ 必改(FR-1 硬重命名) |
| `dashboard-conventions.md` | 看板规范 | §规则 1:三同步(本需求 0 触发) | ✅ INV-7 锁定 0 触发 |
| `encoding-conventions.md` | 编号规范 | §规则 1/3:5+5 位嵌套式 | ✅ INV-8 锁定 0 触发 |
| `marketplace-protocol.md` | 市场协议 | 0 改 marketplace/plugin(实际必改) | ✅ FR-2 触发 |
| `module-conventions.md`(DEPRECATED) + `directory-conventions.md` | 模块/目录规范 | §规则 1:过程文档摆放在子目录根 | ✅ 沿用 |
| `commit-conventions.md` | 提交规范 | `chore(<scope>): <subject>` 格式 | ✅ 末步提交沿用 |
| `doc-conventions.md` | 文档规范 | 中英 README 同步 | ✅ FR-4 触发(25 文件) |
| `naming-conventions.md` | 命名规范 | 0 新增文件名前缀 | ✅ 基本名 `code-check` 用户原文锁定 |
| `dependency-conventions.md` | 依赖规范 | 0 新增依赖 | ✅ 0 新增 |
| `migration-mapping.md` | 迁移映射 | 旧 → 新格式映射 | ✅ FR-5 沿用 §规则 5 |
| `framework-conventions.md` | 框架规范 | 框架选型偏好 | N/A |
| `coding-style.md` | 编码风格 | 命名/注释/提交风格 | N/A |
| `encoding-conventions.md` | 编号规范 | 5+5 位嵌套式 | ✅ 0 触发 |

**本需求触发 4 个规范**:skill-conventions(FR-1) / marketplace-protocol(FR-2) / doc-conventions(FR-4) / migration-mapping(FR-5)

### 2.3 规范遵循(本设计对应章节,详 §3-§6)

#### 2.5.1 适用的规范文件
| 规范文件 | 关键约束 | 本设计对应章节 |
| --- | --- | --- |
| `skill-conventions.md §规则 1` | `name` 与目录名一致 | §3 模块拆分(FR-1 硬重命名) |
| `marketplace-protocol.md §规则 1` | `skills[]` 路径 + 关键词 + description 同步 | §3 模块拆分(FR-2) |
| `doc-conventions.md §规则 1` | 中英 README 对仗 | §3 模块拆分(FR-4 25 文件) |
| `migration-mapping.md §规则 5` | 历史不追溯 | §3.2 关键决策(FR-5 锁定) |

#### 2.5.2 规范自检结论
- **完全合规**的章节:§3, §4, §5, §6
- **经用户授权偏离**的章节:无
- **待澄清冲突**:无

#### 2.5.3 用户授权的偏离
(无)本需求为"硬重命名",**不**偏离任何规范

#### 2.5.4 待澄清的规范冲突
(无)本需求**0**待澄清冲突;7 FR / 6 NFR / ~33 AC / 9 INV 全部已锁定

---

## 3. 概要架构(模块拆分)

### 3.1 整体架构图(Mermaid)

```mermaid
graph TB
    subgraph "步骤 1:技能入口硬重命名(FR-1)"
        S1a[git mv code-review/ → code-check/]
        S1b[改 SKILL.md frontmatter name: code-check]
        S1c[改 SKILL.md H1 标题]
        S1d[Grep + Edit 替换全文字面量]
        S1a --> S1b --> S1c --> S1d
    end

    subgraph "步骤 2:JSON 同步(FR-2)"
        S2a[改 .claude-plugin/marketplace.json<br/>skills[] + keywords[] + description]
        S2b[改 plugins/code-skills/.claude-plugin/plugin.json<br/>keywords[] + description]
        S2c[Bash: jq . 校验 JSON 合法性]
        S2a --> S2c
        S2b --> S2c
    end

    subgraph "步骤 3:10 个其他 SKILL.md description 同步(FR-3)"
        S3a[Grep -l 定位 10 个 SKILL.md]
        S3b[Edit description 字段字面量]
        S3a --> S3b
    end

    subgraph "步骤 4:仓库级 README(FR-4)"
        S4a[改仓库根 README.md / README.en.md]
        S4b[改 plugins/code-skills/README.md / README.en.md]
        S4c[改仓库根 CLAUDE.md]
    end

    subgraph "步骤 5:项目级规范(FR-4)"
        S5a[改 13 份 ./assistants/rules/*.md]
    end

    subgraph "步骤 6:技能模板(FR-4)"
        S6a[改 6 份 plugins/code-skills/skills/*/templates/*.md]
    end

    subgraph "步骤 7:当前激活看板(FR-4)"
        S7a[改 V0.0.3/RESULT.md 规范引用]
    end

    subgraph "步骤 8:校验(本概设新增)"
        V1[Grep "code-review" 本需求范围内 → 应无匹配]
        V2[git diff 对照 code-check/SKILL.md 与原 code-review/SKILL.md → 仅字面量差异]
        V1 --> V2
    end

    S1d --> S2c --> S3b --> S4c --> S5a --> S6a --> S7a --> V2
```

### 3.2 关键设计决策(本需求 N=6 项)

| # | 决策 | 选定方案 | 备选 + 否决理由 | 依据规范 |
| --- | --- | --- | --- | --- |
| **D-1** | 技能入口重命名策略 | **硬重命名**(`git mv` + 改 frontmatter + 改 H1) | A. 软重命名(保留 `/code-review` 别名) — 否决,违反 `skill-conventions §规则 1` 不接受双 `name`;**B. 硬重命名**(选定) | Q-1 + `skill-conventions §规则 1` |
| **D-2** | JSON 同步策略 | **全部同步改**(`skills[]` + `keywords[]` + `description`) | A. 只改 `skills[]` 路径 — 否决,产品语义混乱;**B. 全部同步改**(选定) | Q-2 + `marketplace-protocol §规则 1` |
| **D-3** | docs 同步策略 | **全部同步改**(25 文件:4 README + 1 CLAUDE.md + 13 规范 + 6 模板 + 1 看板) | A. 只改 SKILL.md + JSON,docs 留 follow-up — 否决,会导致后续 PR 混乱;**B. 全部同步改**(选定) | Q-3 + `doc-conventions §规则 1` |
| **D-4** | 历史产物处理 | **不追溯**(V0.0.0/V0.0.1/V0.0.2/V0.0.3 review 目录内容保留) | A. 历史产物也同步改 — 否决,会破坏 git 历史 + 跨多个 REQ 重大变更;**B. 不追溯**(选定) | Q-4 + `migration-mapping §规则 5` |
| **D-5** | 产出物类型目录 | **`review/` 目录名保留**(目录名是"产出物类型",不是"技能名") | A. 同步改 `review/` → `check/` — 否决,会破坏 V0.0.2 全部历史 review 产物路径;**B. 保留**(选定) | 沿用既有约定 |
| **D-6** | 中文表述 | **不强求统一**(代码评审/代码检查可共存) | A. 全部改"代码检查" — 否决,过度约束;**B. 不强求**(选定) | 尊重用户原文 |

### 3.3 不变量(本需求 INV=9 条,字节级保留)

| INV | 描述 | 保留位置 |
| --- | --- | --- |
| **INV-1** | 11 个 SKILL.md(除 `code-check` 自身)的 frontmatter `name` 字段**字节级保留** | L1-3 |
| **INV-2** | 11 个 SKILL.md 的既有"## 工作流程"小节**不**被破坏,只追加新锚点 | 各 SKILL.md 工作流程段 |
| **INV-3** | 11 个 SKILL.md 的"## 衔接" + "## 不要做的事"段**不**改 | 各 SKILL.md 末尾 |
| **INV-4** | V0.0.3 看板"任务清单"区段字段**0 新增** | V0.0.3/RESULT.md |
| **INV-5** | 本需求**0** 修改 `marketplace.json` / `plugin.json` 之外的其他 JSON 配置 | JSON 配置 |
| **INV-6** | 本需求**0**派生"更新看板"任务(REQ-00017 强约束) | 看板 |
| **INV-7** | 本需求**0**触发 `dashboard-conventions §规则 1` 三同步(看板字段 0 新增) | 看板 |
| **INV-8** | 本需求**0**触发 `dependency-conventions`(0 新增依赖;硬重命名无需新工具) | 依赖 |
| **INV-9** | 本需求后 `code-check` 技能的行为与 `code-review` 技能**完全一致** | `code-check/SKILL.md` |

### 3.4 模块清单(本需求改造 + 复用)

#### 修改既有
- `code-review/SKILL.md` → 重命名为 `code-check/SKILL.md`(FR-1)

#### 字面量同步(11 类引用方)
- 10 个其他 SKILL.md 的 `description` 字段(FR-3)
- 2 个 JSON 清单(FR-2)
- 4 个 README + 1 个 CLAUDE.md(FR-4)
- 13 份项目级规范(FR-4)
- 6 个技能模板(FR-4)
- 1 个 V0.0.3 当前激活看板(FR-4)

#### 复用既有
- `code-auto/SKILL.md`:**0 改**(本需求**不**改 `code-auto` 子技能调用表)— **不对,FR-3 必改 `code-auto/SKILL.md` 中"code-review"字面量**(已计入 10 个其他 SKILL.md)

**更正**:本需求实际改 `code-auto/SKILL.md`(在 10 个其他 SKILL.md 之中),**不**仅是字面量,而是子技能调用表 / 屏显契约 / 状态机图全部需同步。

#### 不追溯
- V0.0.0 / V0.0.1 / V0.0.2 全部历史版本内容(FR-5)
- V0.0.3 历史 review 产物 `review/REQ-NNNN/*`(FR-5)
- `migration-mapping.md` 中"`EXISTING-010` → 代码评审(`code-review`)"行(沿用 `migration-mapping §规则 5`)

---

## 4. 接口与数据结构

### 4.1 CLI 接口(本需求 0 新增)

- 沿用既有:`/code-review` → 改名为 `/code-check`
- **不**新增参数
- **不**改行为(屏显契约 / 错误码 / 边界异常 / 任务循环)

### 4.2 数据结构(本需求 0 新增)

- 沿用既有:`code-check` 技能的产出物路径 / 文件结构 / 任务列表解析锚点
- **0**修改任何文件结构

### 4.3 字面量替换矩阵(本需求新增)

| 位置 | 旧字面量 | 新字面量 | 数量 |
| --- | --- | --- | --- |
| 技能目录名 | `code-review` | `code-check` | 1 |
| 技能 frontmatter `name` | `code-review` | `code-check` | 1 |
| 技能 H1 标题 | `code-review` | `code-check` | 1 |
| SKILL.md 全文引用 | `code-review` | `code-check` | ~20 处 |
| 10 个其他 SKILL.md description | `code-review` | `code-check` | 10 |
| `.claude-plugin/marketplace.json` | `code-review` | `code-check` | ~3 处 |
| `plugin.json` | `code-review` | `code-check` | ~2 处 |
| 仓库根 2 README + 仓库内 2 README + CLAUDE.md | `code-review` | `code-check` | ~10-20 处 |
| 13 份项目级规范 | `code-review` | `code-check` | ~5-10 处 |
| 6 个技能模板 | `code-review` | `code-check` | ~5-10 处 |
| V0.0.3 当前激活看板 | `code-review` | `code-check` | 6 处(已识别) |
| **总计** | — | — | **约 60-90 处字面量** |

---

## 5. 异常处理 / 安全 / 状态机

### 5.1 异常处理

| ID | 场景 | 处理 |
| --- | --- | --- |
| **E-1** | `git mv` 失败(权限/文件占用) | 透传 stderr,中断退出 |
| **E-2** | `Edit` 替换失败(文件被改) | 透传 stderr,中断退出 |
| **E-3** | `jq .` 校验失败(JSON 语法) | 透传 stderr,中断退出 |
| **E-4** | `Grep "code-review"` 残留(本需求范围内) | 屏幕输出未替换列表,提示手动处理 |
| **E-5** | 用户输入 `/code-review` | Claude Code 报"未知技能"错误(由路由层处理) |
| **E-6** | `code-check` 行为与 `code-review` 不一致 | 校验 `git diff` 应只有字面量差异,无语义差异 |
| **E-7** | 历史产物中"code-review"字面量 | **不**追溯替换(沿用 `migration-mapping §规则 5`) |

### 5.2 安全

- NFR-6.1:`git mv` 失败(权限/文件占用)→ 透传 stderr
- NFR-6.2:`Edit` 失败(文件被改)→ 透传 stderr
- NFR-6.3:`jq` 校验失败(JSON 语法)→ 透传 stderr

### 5.3 状态机

- 沿用既有"## 工作流程"状态机(本需求**不**引入新状态)
- `code-check` 技能状态机与 `code-review` 完全一致(沿用既有)
- `code-auto` 状态机 0 改(子技能名从 `code-review` 改为 `code-check`,状态机图 / 屏显契约同步)

### 5.4 性能 / 资源

- 重命名 + 同步约 38-39 文件 + 1 目录,预计耗时 < 5 秒
- `git mv` + `Edit` + `jq` + `Grep` 全部本地操作

---

## 6. 看板同步(本需求 0 触发三同步)

### 6.1 看板影响(本需求 0 改字段)

- ✅ 本需求**0**修改 `V0.0.3/RESULT.md` 看板的字段约定
- ✅ 本需求**0**触发 `dashboard-conventions §规则 1`(INV-7)
- ✅ 本需求**0**派生"更新看板"任务(INV-6)
- ⚠ 本需求**字面量同步**会改 V0.0.3/RESULT.md 中"code-review" → "code-check"(FR-4 已计入 25 文件)

### 6.2 本概设完成后需追加的看板条目

- **需求清单**:REQ-00022 的"概要设计"列从 `—` 改为 `[REQ-00022/RESULT.md](./design/REQ-00022/RESULT.md)`
- **变更记录**:追加 1 条 `YYYY-MM-DD  设计新增  REQ-00022 概要设计完成`

---

## 7. 测试要点

- **AC-1.x**:技能入口硬重命名
  - AC-1.1:`ls plugins/code-skills/skills/` 不含 `code-review/` 含 `code-check/`
  - AC-1.2:frontmatter L1-3 `name: code-check`
  - AC-1.3:H1 `# code-check — ...`
  - AC-1.4:`Grep "code-review" code-check/SKILL.md` 无匹配
- **AC-2.x**:JSON 同步
  - AC-2.1 ~ 2.4:`jq .` 校验合法 + `Grep` 无 `code-review` 残留
- **AC-3.x**:10 个其他 SKILL.md
  - AC-3.1 ~ 3.3:`Grep -l "code-review"` 仅匹配 `code-check/SKILL.md`
- **AC-4.x**:README + 规范 + 模板 + 看板
  - AC-4.1 ~ 4.8:`Grep` 校验 25 文件无 `code-review` 残留
- **AC-5.x**:历史不追溯
  - AC-5.1 ~ 5.2:`Grep "code-review" assistants/V0.0.X/` 命中
- **AC-6.x**:行为不变
  - AC-6.1:`git diff` 仅字面量差异
  - AC-6.2 ~ 6.3:工作流程 / 衔接 / 不要做的事 字节级保留
- **INV-1 ~ INV-9**:9 条不变量自检

---

## 8. 关联设计

### 8.1 本版本(V0.0.3)

- **REQ-00020**:架构设计目标重新归位 + 3 新维度(本需求 0 涉及)
- **REQ-00021**:优化 3 技能 --result / --plan 模板参数(本需求 0 涉及)

### 8.2 跨版本(V0.0.2)

- **REQ-00007**:`code-auto` 自动开发 — `code-auto/SKILL.md` 同步改(FR-3)
- **REQ-00013**:屏显"编号+标题" — 屏显格式契约沿用(NFR-4.1)
- **REQ-00017**:0 派生"更新看板"任务 — INV-6 沿用
- **REQ-00019**:BUG 模式同构 — BUG 路径评审仍走 `review/` 目录

### 8.3 关键引用方(本需求必须同步改)

详 `related-designs.md`

---

## 9. 待澄清 / 未决项

| 编号 | 内容 | 状态 |
| --- | --- | --- |
| (无) | 本需求**0**待澄清;6 项设计决策(D-1 ~ D-6)+ 9 条不变量(INV-1 ~ INV-9)全部已锁定;7 FR / 6 NFR / ~33 AC / 9 INV 全部已锁定;4 项 Q-locked(`clarifications.md` 已落) | 0 待澄清 |

---

## 10. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-06-07 | v1 | 初始创建 | 完成首次概要设计:6 决策(D-1 ~ D-6)+ 9 不变量(INV-1 ~ INV-9)+ 7 FR / 6 NFR / ~33 AC / 9 INV 全部锁定;整体=--balanced(code-auto 上下文默认);0 触发 `dashboard-conventions §规则 1` 三同步;0 派生"更新看板"任务;字面量替换矩阵:约 60-90 处字面量需同步;`code-check` 行为与 `code-review` 完全一致 | wangmiao |
