# 模块清单 — REQ-00005

更新时间:2026-06-04 16:00
版本:V0.0.2

## 1. 模块总览

| # | 模块/文件 | 路径 | 状态 | 变更类型 | 职责 | 对外契约(工作流步骤) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | `code-require` 技能 | `plugins/code-skills/skills/code-require/SKILL.md` | **修改** | 增量追加 3 步骤 | 需求分析(版本感知) | **新增**:步骤 0a(拉取) + 步骤 0b(版本对齐) + 步骤 N(兜底提交) |
| 2 | `code-design` 技能 | `plugins/code-skills/skills/code-design/SKILL.md` | **修改** | 增量追加 2 步骤 | 概要设计(版本感知) | **新增**:步骤 0a(拉取) + 步骤 N(兜底提交) |
| 3 | `code-plan` 技能 | `plugins/code-skills/skills/code-plan/SKILL.md` | **修改** | 增量追加 2 步骤 | 详细设计 & 计划(版本感知) | **新增**:步骤 0a(拉取) + 步骤 N(兜底提交) |
| 4 | 版本看板(本需求行) | `assistants/V0.0.2/RESULT.md` | **追加** | 新增 1 行 + 1 条 | 本版本"概要设计清单" + "变更记录" | (本设计产出) |

> **无新增模块**;**无复用既有模块**(本需求仅修改 3 个 SKILL.md + 追加看板行)。
> **未触达模块**(`code-version` / `code-it` / `code-unit` / `code-review` / `code-fix` / `code-init` / `code-rule` / `code-dashboard` / `code-publish` / `code-auto` 等)严格保留,见 §6。

## 2. 模块 #1 — `code-require` 技能(修改)

### 2.1 当前状态
- **路径**:`plugins/code-skills/skills/code-require/SKILL.md`
- **大小**:13,679 bytes(2026-06-04)
- **frontmatter**:`name: code-require` + `description: 需求分析(版本感知)......`(本设计**不修改**)
- **工作流章节**:已含"步骤 0 — 版本上下文检测"、"步骤 1 — 收集需求编码"、...、"步骤 9A — 同步版本看板(强制)"

### 2.2 本需求变更点(增量,3 处插入)

#### 2.2.1 插入 A:在"步骤 0 — 版本上下文检测"**之前**,新增"步骤 0a — 拉取最新代码"

```markdown
### 步骤 0a — 拉取最新代码(强制前置,新增)
所有其他 `code-*` 技能的第一步都是这一步。
1. 探测 `git` 可用性 → 失败 → 中断 + 提示"未检测到 git,本需求需要 git"(E-12)
2. 执行 `git pull`(默认 upstream / tracking 分支)
3. 拉取失败 3 种情况处理(Q-2 锁定 A):
   - 冲突 → `✗ git pull 失败:存在未解决的冲突` + 提示手动处理(E-2)
   - 网络 → `✗ git pull 失败:网络/remote 不可达` + 提示检查网络(E-3)
   - 凭据 → `✗ git pull 失败:权限/凭据` + 提示检查凭据(E-4)
4. 拉取成功(包含 no-op):
   - **立即** `Read "./assistants/.current-version"`,记为"拉取后版本"(NFR-8)
   - 进入步骤 0b
```

> **不重写**既有"步骤 0 — 版本上下文检测" — 仅在其前插入。

#### 2.2.2 插入 B:在"步骤 0a"**之后**,新增"步骤 0b — 工作版本号对齐检查"(仅 `code-require` 专属)

```markdown
### 步骤 0b — 工作版本号对齐检查(`code-require` 专属,新增)
仅 `code-require` 执行此步骤。`code-design` / `code-plan` 跳过。
1. 对比"拉取后版本"(步骤 0a 读取)与"用户意图版本"
   - **用户意图版本** = 拉取前读取的 `.current-version`,或用户口头/文本指定的目标版本
2. 一致 → 直接进入既有"步骤 0 — 版本上下文检测"
3. 不一致 → 中断(NFR-3 硬中断,**不**进入步骤 1) + 询问用户:
   ```
   ✗ 检测到上下文版本不一致
     本地(拉取后):<A>
     远端:.current-version = <B>
     需求 <需求编码> 在 <A> 中不存在,但在 <B> 中已存在
   ```
   弹 3 选 1(FR-2.AC-2.3):
   - A. 切到 <B> 后继续(推荐) — 调 `code-version <B>`,确认切换成功后**退出** `code-require`,提示"已切到 <B>,请重跑 `code-require`"
   - B. 在 <A> 中重新创建 <需求编码> — 继续原流程(走既有"步骤 1 收集需求编码")
   - C. 取消 — 退出 `code-require`,无任何文件变更
```

> **不重写**既有"步骤 0 — 版本上下文检测" — 仅在其前插入。

#### 2.2.3 插入 C:在原"步骤 10A — 完善过程文档"**之后**(作为最后一步),新增"步骤 N — 末尾兜底提交"

```markdown
### 步骤 N — 末尾兜底提交(强制收尾,新增)
所有其他步骤执行完毕后的**最后一步**。覆盖"过程文件 + 结果文件"。
1. 执行 `git status --porcelain`,获取 dirty 文件列表
2. 空列表 → 打印 `无文件变更,跳过末尾提交`,退出(AC-3.5 / NFR-4 幂等)
3. 非空 → 执行 `git add <所有文件>`(范围 = `git status --porcelain` 输出,FR-3.AC-3.2)
4. 生成 commit message 预览(NFR-6 沿用 V0.0.1 实践):
   ```
   chore(code-require): <需求编码> <需求标题>

   需求分析完成:<N> FR / <M> NFR / <K> AC
   过程文件 3 + 结果文件 1 = <N> 文件待提交
   ```
5. 弹 3 选 1 确认(Q-3 锁定 A):
   - A. 确认提交(推荐)
   - B. 修改 commit message(技能重新生成预览或用户编辑)
   - C. 取消提交(跳过 commit,打印"已取消提交",退出)
6. 选 A → 执行 `git commit -m "<message>"`:
   - 成功 → 打印 commit hash,退出
   - 失败(E-10,pre-commit hook / 其他)→ 打印 stderr,**不重试**,提示"末尾提交失败,文件已暂存,请手动处理后,执行 git commit"
```

> **不重写**既有"步骤 10A — 完善过程文档" — 仅在其后追加。
> **首次 / 增量都执行**:步骤 N 在两条分支(7A-15A / 7B-10B)的最后都执行。

### 2.3 强约束不动的部分

| 不动部分 | 依据 |
| --- | --- |
| YAML frontmatter(2 行) | `skill-conventions.md §规则 1` + FR-6 |
| 既有"步骤 0 — 版本上下文检测"全文 | NFR-2 增量修改 + 步骤 0a/0b 是**前置补充**,不取代步骤 0 |
| 既有"步骤 1-9 / 10A" | 同上 |
| 既有"过程文档格式"小节 | 同上 |
| 既有"衔接"小节(下游 = `code-design`) | 同上 |
| 既有"不要做的事"小节 | 同上 |

### 2.4 符合的规范条款

| 规范条款 | 满足度 | 说明 |
| --- | --- | --- |
| `skill-conventions.md §规则 1` | ✅ 满足 | frontmatter 字节级保留 |
| `dashboard-conventions.md §规则 1` | ✅ 不触发 | 不扩展看板字段 |
| `marketplace-protocol.md §规则 1` | ✅ 不触发 | 不改 marketplace / plugin 清单 |
| `doc-conventions.md §规则 1` | ✅ 不触发 | 不写 README |
| `commit-conventions.md` | ✅ NFR-6 显式不填充规则 | 沿用 V0.0.1 实践 |

## 3. 模块 #2 — `code-design` 技能(修改)

### 3.1 当前状态
- **路径**:`plugins/code-skills/skills/code-design/SKILL.md`
- **大小**:19,665 bytes(2026-06-04)
- **frontmatter**:`name: code-design` + `description: 概要设计(版本感知)......`(本设计**不修改**)
- **工作流章节**:已含"步骤 0 — 版本上下文检测"、"步骤 1 — 收集需求编码"、...、"步骤 14A — 同步版本看板(强制)"、"步骤 15A — 完善过程文档与汇报"

### 3.2 本需求变更点(增量,2 处插入)

#### 3.2.1 插入 A:在"步骤 0 — 版本上下文检测"**之前**,新增"步骤 0a — 拉取最新代码"

> 与 `code-require` 步骤 0a **结构相同**,但**不**含"步骤 0b"(FR-2 显式仅 `code-require` 专属)。
> 步骤 0a 完成后直接进入既有"步骤 0"。

#### 3.2.2 插入 B:在原"步骤 15A — 完善过程文档与汇报"**之后**(作为最后一步),新增"步骤 N — 末尾兜底提交"

> 与 `code-require` 步骤 N **结构相同**。
> commit message 模板差异:
> ```
> chore(code-design): <需求编码> <设计标题>
>
> 概要设计完成:<关键决策数> 项决策,<不变量数> 条不变量
> 过程文件 N + 结果文件 1
> ```

### 3.3 强约束不动的部分

| 不动部分 | 依据 |
| --- | --- |
| YAML frontmatter(2 行) | `skill-conventions.md §规则 1` + FR-6 |
| 既有"步骤 0 — 版本上下文检测"全文 | NFR-2 增量 |
| 既有"步骤 1-14A / 15A" | 同上 |
| 既有"过程文档格式"小节 | 同上 |
| 既有"7B 增量更新"分支 | 同上(增量也走步骤 N) |
| **新增"步骤 0b"** | FR-2 显式仅 `code-require` 专属;**`code-design` / `code-plan` 跳过** |

### 3.4 符合的规范条款

| 规范条款 | 满足度 | 说明 |
| --- | --- | --- |
| `skill-conventions.md §规则 1` | ✅ 满足 | frontmatter 字节级保留 |
| `dashboard-conventions.md §规则 1` | ✅ 不触发 | 不扩展看板字段 |
| 其他 | ✅ 不触发 | 同 #2.4 |

## 4. 模块 #3 — `code-plan` 技能(修改)

### 4.1 当前状态
- **路径**:`plugins/code-skills/skills/code-plan/SKILL.md`
- **大小**:33,016 bytes(2026-06-04)
- **frontmatter**:`name: code-plan` + `description: 详细设计与编码计划(版本感知)......`(本设计**不修改**)
- **双路径设计**:既接受 `REQ-NNNNN`(需求路径)也接受 `BUG-NNN`(缺陷路径)

### 4.2 本需求变更点(增量,2 处插入)

#### 4.2.1 插入 A:在"步骤 0 — 版本上下文检测"**之前**,新增"步骤 0a — 拉取最新代码"

> 与 `code-design` 步骤 0a **结构相同**;**不**含"步骤 0b"。
> 注意:`code-plan` 步骤 0 原文要求"验证 `require/.../RESULT.md` + `design/.../RESULT.md` 都存在" — 步骤 0a 完成后,该验证仍由步骤 0 负责(NFR-2 增量)。

#### 4.2.2 插入 B:在原"步骤 18A" / "步骤 13B"(原工作流最后一步)**之后**,新增"步骤 N — 末尾兜底提交"

> 与 `code-design` 步骤 N **结构相同**。
> commit message 模板差异:
> ```
> chore(code-plan): <需求编码> <计划标题>
>
> 详细设计与编码计划完成:<任务数> 个任务
> 过程文件 N + 结果文件 2(PLAN.md + RESULT.md)
> ```

### 4.3 强约束不动的部分

| 不动部分 | 依据 |
| --- | --- |
| YAML frontmatter(2 行) | `skill-conventions.md §规则 1` + FR-6 |
| 既有"步骤 0 — 版本上下文检测"全文 | NFR-2 增量 |
| 既有"步骤 1-18A" / "13B" | 同上 |
| 既有"BUG 路径"(步骤 19-28) | 同上(本需求不区分 REQ / BUG 路径,统一步骤 N) |
| **新增"步骤 0b"** | FR-2 显式仅 `code-require` 专属 |

### 4.4 符合的规范条款

| 规范条款 | 满足度 | 说明 |
| --- | --- | --- |
| `skill-conventions.md §规则 1` | ✅ 满足 | frontmatter 字节级保留 |
| `dashboard-conventions.md §规则 1` | ✅ 不触发 | 不扩展看板字段 |
| 其他 | ✅ 不触发 | 同 #2.4 |

## 5. 模块 #4 — 版本看板追加(本设计产出)

### 5.1 当前状态
- **路径**:`assistants/V0.0.2/RESULT.md`
- **大小**:27,488 bytes(2026-06-04)
- **本需求追加 2 处**(详见 `RESULT.md` §16 同步清单)

### 5.2 本需求变更点

| 区段 | 位置 | 追加内容 |
| --- | --- | --- |
| "概要设计清单" | 第 87-95 行之间 | 追加 1 行,记录 REQ-00005 概要设计完成(状态 = `已完成`,完成时间 = 2026-06-04) |
| "变更记录" | 第 173-189 行之间 | 追加 1 条,格式 `2026-06-04 16:00  设计新增  REQ-00005 概要设计完成  REQ-00005` |
| "索引:本版本所有文件" | 第 193-263 行之间 | 追加 1 段,链接 `design/REQ-00005/RESULT.md` + 7 个过程文档 |
| "文档头-最近更新" | 第 10 行 | 改为 `2026-06-04 16:00` |

### 5.3 强约束不动的部分

| 不动部分 | 依据 |
| --- | --- |
| 既有"需求清单"区段(本需求不属) | `dashboard-conventions.md §规则 1` 责任划分 |
| 既有"详细设计与任务计划汇总"区段 | 同上 |
| 既有"任务清单"区段 | 同上 |
| 既有"缺陷清单"区段 | 同上 |
| 既有"评审发现汇总"区段 | 同上 |
| 既有"派生任务记录"区段 | 同上 |
| 既有"执行的开发命令记录"区段 | 同上 |
| 既有"变更记录"区段的**其它行** | 本设计只追加,不修改既有行 |

## 6. 未触达模块(强约束保留)

| 技能 / 文件 | 路径 | 不动依据 |
| --- | --- | --- |
| `code-version` | `plugins/code-skills/skills/code-version/SKILL.md` | FR-5.AC-5.1(本需求**调用**但不**修改**) |
| `code-it` | `plugins/code-skills/skills/code-it/SKILL.md` | FR-4.AC-4.1(Q-4 锁定 B,内部 commit 行为不变) |
| `code-unit` | `plugins/code-skills/skills/code-unit/SKILL.md` | FR-6 / 不在本需求范围 |
| `code-review` | `plugins/code-skills/skills/code-review/SKILL.md` | 同上 |
| `code-fix` | `plugins/code-skills/skills/code-fix/SKILL.md` | 同上 |
| `code-init` | `plugins/code-skills/skills/code-init/SKILL.md` | 同上 |
| `code-rule` | `plugins/code-skills/skills/code-rule/SKILL.md` | 同上 |
| `code-dashboard` | `plugins/code-skills/skills/code-dashboard/SKILL.md` | REQ-00004 边界继承(NFR-6 不修改) |
| `code-publish` | `plugins/code-skills/skills/code-publish/SKILL.md` | REQ-00006 边界继承 |
| `code-auto` | `plugins/code-skills/skills/code-auto/SKILL.md` | REQ-00007 边界继承 |
| `plugin.json` | `plugins/code-skills/.claude-plugin/plugin.json` | FR-6 + `marketplace-protocol.md §规则 1.3` |
| `marketplace.json` | `.claude-plugin/marketplace.json` | FR-6 + `marketplace-protocol.md §规则 1` |
| `CLAUDE.md` | `plugins/code-skills/CLAUDE.md` | FR-6.AC-6.2(N-7 留 follow-up) |
| `README.md` / `README.en.md` | `plugins/code-skills/README*.md` | FR-6.AC-6.3(由 `code-rule` 沉淀) |
| 13 个规范文件 | `assistants/rules/*.md` | 本技能**只读**(`dashboard-conventions §规则 1` 责任划分) |
| V0.0.0 / V0.0.1 | `assistants/V0.0.0/` / `assistants/V0.0.1/` | 历史快照,不动 |

## 7. 自检 — `module-conventions.md`(已 DEPRECATED,迁至 `directory-conventions.md`)

> ⚠️ `module-conventions.md` § 1 标记 DEPRECATED(2026-06-04),内容已迁 `directory-conventions.md`,但**新 `directory-conventions.md` 规则 1 仍为占位**。
> 本需求**不**新增任何技能资源(模板 / 清单 / 指南),**不**触发该规范 — 走"无内容可放"的零状态。
> 若 `code-plan` / `code-it` 阶段需要新增模板(如"末尾 commit message 模板"),**应**放技能目录 `templates/` 子目录,遵循未来填充的 `directory-conventions.md §规则 1`。
