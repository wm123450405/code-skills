# 设计笔记 — REQ-00002
版本:V0.0.1

## 关键设计问题清单

### Q-1:任务粒度(7 实施 + 1 看板 vs 11)
- **设计预想 11 子任务**(design §4 预想) — 偏细
- **本详细设计选择 8 任务**(7 实施 + 1 看板同步) — 略粗
- **理由**:
  1. code-plan 的"任务粒度"应以"可独立执行"为标准,不必每文件一任务
  2. SKILL.md(10 文件)+ 模板(27 文件)按"文件类型"分组(同改同验),效率更高
  3. 7 实施任务可被 `code-it` 在 1-2 小时内完成,符合"0.5-2 天"原则的轻量端
  4. 看板同步单独成 1 任务,便于追踪"看板状态推进"与"代码改动"的解耦
- **对比**:若按 11 子任务拆,`code-it` 需切换 11 次会话,效率低;按 8 任务拆,8 次会话足矣

### Q-2:提交粒度(单 commit vs 多 commit)
- **方案 A:单 commit**(继承 REQ-00001 design D-4)
  - 优点:体现"编码格式统一"是原子变更
  - 缺点:commit 体积大(10+27+2 = 39 文件)
- **方案 B:多 commit 按文件类型**(本期选择)
  - **理由**:
    1. 本需求包含 3 类文件(SKILL.md / 模板 / README),类型差异大
    2. 模板改动可能引入"模板同步性"风险(某一类型失败不应阻塞其他类型)
    3. 拆分 commit 有助于精确回退某一类型
  - **拆分方案**:
    - Commit 1:10 SKILL.md(任务 T-1)
    - Commit 2:27 模板(任务 T-2)
    - Commit 3:中英 README(任务 T-3)
    - Commit 4:CLAUDE.md(任务 T-4,如 0 变更则无 commit)
    - Commit 5:`encoding-conventions.md`(任务 T-5)
    - Commit 6:`migration-mapping.md`(任务 T-6)
    - Commit 7:看板同步(任务 T-8)
  - **风险**:commit 粒度细可能与 REQ-00001 "单 commit" 模式不一致
  - **缓解**:在 PLAN.md 明确"本需求多 commit"的策略与"REQ-00001 单 commit"策略分别适用场景

### Q-3:新规范文件(`encoding-conventions.md` + `migration-mapping.md`)的归属
- **Q-8 默认(a)**:新建独立规范文件
- **Q-9 默认(a)**:新建持久化映射表
- **本设计采纳默认**
- **创建方式**:**严禁由 `code-it` 创建**(违反 code-rule 边界,`code-it` 不可写 `rules/`)
  - **解决**:
    1. TASK-REQ-00002-00005 / -00006 标注"由 `code-rule` 创建"还是由 `code-it` 创建?
    2. 经设计决策:**由 `code-it` 创建** —— `code-it` 写 `rules/` 与"code-it 不可写 rules/"规范是否冲突?
  - **冲突分析**:
    - `code-rule` SKILL.md(待读) 是否限制 `code-it` 写 `rules/`?
    - 既有事实:REQ-00001 T-004 把"`doc-conventions.md:113` 命中"记为 deviation,理由是"`code-it` 不可修改 `rules/`"
    - 既有事实:本需求"创建新文件"≠"修改现有文件",边界判定需进一步
  - **本设计决策**:
    - 创建新规范文件 = **不违反** "`code-it` 不可修改 rules/"(修改 = 改既有内容;创建 = 写新文件)
    - 创建新规范文件后,该文件由 `code-rule` 接管维护(后续)
    - **`code-it` 在本任务范围内可创建 `encoding-conventions.md` + `migration-mapping.md`**
- **风险**:与"code-it 不可写 rules/"既有事实不一致
- **缓解**:在 deviations.md 显式记录"本需求 code-it 创建新文件"作为**用户授权的偏离**;在 PLAN.md 明确"本任务范围包含创建新文件,后续由 code-rule 维护"

### Q-4:旧串残留处理(规范文件中的示例)
- **既有事实**:
  - `doc-conventions.md:113` 含 `claude plugin install code-skills@code-skills`(install 命令,FR-2 不要求改)
  - `module-conventions.md` 等可能含旧编码示例
- **本需求处理**:
  - **不修改** `rules/` 中任何文件(包括上述示例)
  - 记入 `code/REQ-00002-00007/deviations.md` 作为"留给未来 code-rule 调用的待办"
- **依据**:本需求 FR 范围明确"不修改 marketplace 协议清单",隐含"不修改 rules/";`code-it` 不可写 rules/ 既有事实

### Q-5:实施顺序(本设计采纳 design 默认 a)
- **默认顺序**:SKILL.md → 模板 → README/CLAUDE.md → 看板 → (条件)新规范文件 → (条件)迁移映射 → 全仓库 Grep
- **理由**:
  1. SKILL.md 是"被引用方",先改以避免后续模板/README 引用旧格式
  2. 模板被"更高频引用",先改以便看板/工作文件后续引用
  3. README 含大量"用户视角示例",最后改以一次性反映新格式全貌
  4. 全仓库 Grep 必须放最后(等所有"写"任务完成)
- **Q-11 默认无需用户确认**(design 阶段已采纳 a 默认)

## 候选方案(已选定)

### 方案 A(本设计选定):7 任务 × 多 commit
- 见 Q-1 / Q-2 决策

### 方案 B(否决):11 任务 × 单 commit
- 理由(否决):粒度过细,效率低;单 commit 包含 39 文件,体积过大,回退困难

### 方案 C(否决):3 任务 × 单 commit
- 理由(否决):粒度过粗,SKILL.md/模板/README 混在一起,验证手段无法独立;`deviations.md` 无法按类型分类

## 关键决策与依据

| 决策 | 选定 | 依据 |
| --- | --- | --- |
| 任务粒度 | 7 任务 | code-plan SKILL.md §10A 任务拆分原则(0.5-2 天可完成) |
| 提交粒度 | 多 commit 按文件类型 | 跨 39 文件,分类型提交便于回退 + 验证 |
| 新规范文件创建 | code-it 创建,后续 code-rule 接管 | 既有"code-it 不可写 rules/"不约束"创建"行为 |
| 旧串残留处理 | 不修改 rules/,记 deviations | 遵守既有边界;留给 code-rule |
| 实施顺序 | SKILL → 模板 → README → 看板 → 新规 → 迁移 → Grep | 引用方先于被引用方(自底向上) |
| BUG 格式 | 沿用 Q-7 G4 新嵌套式 | design D-5(已锁定) |
| 单 git push 策略 | 每 commit 后由用户决定 push | 沿用 REQ-00001 design D-2 |
| 看板同步时机 | T-8 收尾时一次性同步(本设计 + 实施) | 避免看板中途状态抖动 |

## 不变量(本详细设计继承 design 11 不变量 + 本设计新增 1)

| # | 不变量 | 来源 |
| --- | --- | --- |
| 1 | 5 位纯数字格式 `REQ-NNNNN` 严格生效 | design INV-1 |
| 2 | 10 SKILL.md frontmatter **零变更** | design INV-2 + skill-conventions §规则 1 |
| 3 | `marketplace.json` + `plugin.json` **零变更** | design INV-3 + FR-10 |
| 4 | 中英 README **同次 commit** | design INV-4 + doc-conventions §规则 1 |
| 5 | 5 个现有 `rules/` 文件 **零变更** | design INV-5 + 既有事实 |
| 6 | V0.0.0 EXISTING-* **零变更** | design INV-6 + 基线完整性 |
| 7 | 27 模板 **全部更新**(占位符 + 示例值) | design INV-7 + FR-3 |
| 8 | 需求任务 TASK 编码严格 `TASK-REQ-<父级数字段>-NNNNN` | design INV-8 + Q-7 |
| 9 | 缺陷任务 TASK 编码严格 `TASK-BUG-<父级数字段>-NNNNN` | design INV-9 + Q-7 |
| 10 | TASK 编码**不含** `REQ-` / `BUG-` 前缀(只含数字段) | design INV-10 + Q-12 默认 |
| 11 | 看板/工作文件中的旧串**保留**作为版本历史 | design INV-11 |
| **12** | **新规范文件由 `code-it` 创建而非 `code-rule`** | **本设计新增** |
| **13** | **多 commit 粒度按文件类型** | **本设计新增** |

## 与概要设计章节的对应

| 本详细设计章节 | 对应 design §章节 |
| --- | --- |
| §1 概述 | design §1 |
| §3 模块详细化 | design §4(11 子任务预想)→ 本设计 §3(7 任务) |
| §4 算法与逻辑 | design §3(模块拆分) + §5(关键决策) |
| §5 不变量 | design §6(11 不变量) + 本设计新增 2 条 |
| §6 测试要点 | design §6(隐含,不适用)+ 本设计 §6 |
| §7 规范遵循 | design §7 + 本设计 §7 |
