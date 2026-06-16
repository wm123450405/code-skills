# REQ-00036 — 清理技能文件(SKILL.md + templates/)中的开发痕迹

- 需求编码:REQ-00036
- 所属版本:V0.0.3
- 上游需求:./assistants/V0.0.3/require/REQ-00036/RESULT.md (v1)
- 上游概要设计:./assistants/V0.0.3/design/REQ-00036/RESULT.md (v1)
- 遵循规范:./assistants/rules/(13 个规范文件,详见 §3)
- 状态:草稿
- 责任人:用户
- 创建:2026-06-16
- 最近更新:2026-06-16 17:33
- 当前版本:v1

## 设计目标

<!-- 本节由 code-design / code-plan 步骤 0b 自动生成(写入或沿用),记录用户确认的设计目标;如需手动编辑,保留该注释以便步骤 0b 识别 -->

- 整体设计目标:`--minimal`(沿用 `design/REQ-00036/RESULT.md`)
- 维度优先级:
  - 功能性:中
  - 扩展性:不适用
  - 健壮性:中
  - 可维护性:中
  - 封装性:不适用
  - 可复用性:不适用
  - 可读性:不适用

## 1. 详细设计概述

本详细设计把概要设计的 6 条清理规则**精确化到正则字符集层面**,并产出 3 条 `code-it` 任务(T-1 扫描 / T-2 执行 / T-3 验证+提交)。

**关键决策**:
- **6 条规则的精确正则字符集**已在 §5 给出(`code-it` 步骤 8 实施时直接复用)
- **白名单例外**通过正则负向断言实现,**不**维护独立白名单文件
- **`code-fix` 技能对自身 `fix/` 目录的引用** = 任务级特例(正则不作用在该技能的目录级引用上)
- **任务拆分**:3 条,严格串行 T-1 → T-2 → T-3
- **不引入**任何新模块 / 接口 / 数据结构 / 三方依赖

**任务计划**:共 3 条任务(见 `PLAN.md`)。

## 2. 上游引用

### 上游需求摘录
- 来源:./assistants/V0.0.3/require/REQ-00036/RESULT.md
- 关键 FR:FR-1(段尾「本需求 REQ-NNNNN」)/ FR-2(「原 code-unit/fix-plan」)/ FR-3(「Q-N 锁定」)/ FR-4(「YYYY-MM-DD 起生效」)/ FR-5(退场文件名)/ FR-6(杂项) / FR-7(不动 checklists/guidelines) / FR-8(不动 assistants/)
- 关键 NFR:NFR-1(幂等)/ NFR-2(frontmatter 字节级保留)/ NFR-3(不重排章节)/ NFR-4(跨技能契约保留)/ NFR-5(生效日语义等价物)/ NFR-6(占位符保留)/ NFR-7(变更可审查)/ NFR-8(单次提交)/ NFR-9(不影响当前流程)/ NFR-10(可回退)
- 关键 AC:AC-1 ~ AC-8(grep 验证 + 抽查 + commit message)

### 上游概要设计摘录
- 来源:./assistants/V0.0.3/design/REQ-00036/RESULT.md
- 整体 = `--minimal`,功能性 = 中
- 6 条清理规则(R-1 ~ R-6)已命名
- 9 条硬约束(C-1 ~ C-9)
- 6 项风险(R-1 ~ R-6)
- 0 新增模块 / 接口 / 数据结构 / 三方依赖

### 关键交叉点(每条 FR 对应到本设计的章节)
| FR 编号 | 本设计对应章节 | 对应任务 |
| --- | --- | --- |
| FR-1 | §5 算法 1(R-1 段尾清理) | T-2 |
| FR-2 | §5 算法 2(R-2 回溯清理) | T-2 |
| FR-3 | §5 算法 3(R-3 决策记录清理) | T-2 |
| FR-4 | §5 算法 4(R-4 生效日清理) | T-2 |
| FR-5 | §5 算法 5(R-5 退场文件名清理) | T-2 |
| FR-6 | §5 算法 6(R-6 杂项清理) | T-2 |
| FR-7 | §4 模块 0(范围白名单)+ §5 算法 1 输入(过滤) | T-1 + T-2 |
| FR-8 | §4 模块 0(范围白名单)+ §5 算法 1 输入(过滤) | T-1 + T-2 |
| NFR-1 ~ NFR-10 | §5 算法 1-6 的边界 + §6 数据结构(不涉及) | T-2 + T-3 |
| AC-1 ~ AC-8 | §5 算法的 8 条 grep 验证 | T-3 |

## 3. 规范遵循

### 3.1 适用的规范文件
- `./assistants/rules/skill-conventions.md` §规则 1(frontmatter)— §5 算法边界:不动 frontmatter
- `./assistants/rules/skill-conventions.md` §规则 2(开发痕迹禁令)— **本设计的目标规范**,§5 算法 1-6 严格遵循其条款
- `./assistants/rules/encoding-conventions.md` §规则 1, §规则 1.5, §规则 2, §规则 3, §规则 4 — §5 算法 1/5 的正则不能误伤有效编号格式
- `./assistants/rules/dashboard-conventions.md` §规则 1 — §5 算法 0 范围,不动看板字段
- `./assistants/rules/module-conventions.md` §规则 1 — §5 算法 0 范围,只清 `templates/`,不动 `checklists/` / `guidelines/`
- `./assistants/rules/doc-conventions.md` §规则 1, §规则 2 — §5 算法 0 范围,SKILL.md 不属 README
- 其他 7 个规范(naming/coding/framework/dependency/commit/marketplace/migration)— 0 触发,占位规则

### 3.2 规范自检结论
- **完全合规**:§4 / §5 / §7(本节) / §8 / §9 / §10 / §11
- **经用户授权偏离**:无
- **待澄清冲突**:无

### 3.3 用户授权的偏离
(无)

### 3.4 待澄清的规范冲突
(无)

## 4. 模块详细化

**本节对应概要设计 §7 — 本设计 0 新增模块**。

### 模块 0:清理动作自身(对应概要设计 §6 功能域 1)

> 本设计**不新增任何代码模块**。清理动作由 `code-it` 任务循环承载,沿用既有 `code-it` 步骤 7-12。

- **关键类/函数**:
  - 无新类/函数;`code-it` 任务 = 1 段 Bash/Edit 序列(读文件 → 跑 6 条规则 → 写回 → 验证 diff)
- **内部状态**:
  - 文件级:`isModified:boolean` / `originalLineCount:number` / `newLineCount:number` / `skipped:boolean`
  - 任务级:`hitCountByRule:Map<ruleId, number>` / `fileList:List<path>`(T-1 产出 → T-2 消费)
- **关键调用顺序**:
  1. T-1:扫 14 技能 × (SKILL.md + templates/*.md) → 输出"待清理文件表 + 预估命中数"
  2. T-2:对每个文件依次跑 6 条规则(顺序: R-1 → R-2 → R-3 → R-4 → R-5 → R-6)→ 原地改写 → diff 校验
  3. T-3:跑 AC-1 ~ AC-7 grep 验证 → 1 次 `git commit` → 同步看板
- **并发模型**:
  - 串行执行(任务间严格依赖);**不**并发(避免文件写冲突)
  - 单文件内规则**顺序固定**(前序规则可能消除后续规则的上下文)
- **资源管理**:
  - 0 外部资源(纯文本 + Git)
  - 单文件读全量到内存(最大 ~ 1100 行,~ 50KB)→ 改写 → 写回
- **错误处理范式**:
  - 规则应用失败 → 跳过该文件,记 `analysis-notes.md`(E-3)
  - 文件改动后剩大段残缺(改动行数 > 30% 且无实质功能内容)→ 回退该文件原状
  - AC 验证失败 → 整个 commit 失败,git revert(走 NFR-10)
- **日志埋点**:
  - 每文件改动前/后用 `Bash: git diff --stat <file>` 屏显改动行数
  - 任务收尾在 `code/<TASK>/work-log.md` 记录命中计数
- **依据规范**:`./assistants/rules/skill-conventions.md §规则 2` + `code-it` SKILL.md 既有步骤

## 5. 算法与逻辑

### 算法 0:范围过滤器(所有算法的前置)

- **目的**:确定哪些文件需要被处理
- **输入**:文件路径字符串
- **输出**:`boolean`(true = 需要处理)
- **复杂度**:O(1)(纯字符串比较)
- **依赖**:无
- **伪代码**:
  ```
  function inScope(filePath):
      # 1. 必须匹配 "plugins/code-skills/skills/<name>/SKILL.md" 或 "templates/*.md"
      if not (filePath matches ^plugins/code-skills/skills/[^/]+/(SKILL\.md|templates/[^/]+\.md)$):
          return false
      # 2. 排除 checklists/ 和 guidelines/
      if filePath matches /checklists/ or /guidelines/:
          return false
      # 3. 排除 code-unit 目录(已退场)
      if filePath matches /code-unit/:
          return false
      # 4. code-fix 技能:对其 SKILL.md 应用 R-1 ~ R-4 + R-6,但 R-5 跳过
      #    (因 code-fix 自身职责范围是 fix/ 目录,fix-*.md 字面不算退场引用)
      return true
  ```
- **关键决策**:不用"通配 + 排除"方式,而用"白名单 + 5 条特例"——边界更明确,无歧义
- **边界条件**:
  - `code-fix` 自身 SKILL.md 中"本技能维护 fix/RESULT.md"等引用 → 保留(R-5 跳过)
  - `code-fix` 自身 SKILL.md 中其他痕迹(段尾/回溯/决策/生效日)→ 仍清理(R-1 ~ R-4 + R-6)
- **对应任务**:T-1
- **依据规范**:`skill-conventions §规则 2`

### 算法 1:R-1 段尾「本需求 REQ-NNNNN」清理

- **目的**:删除段尾括号内的「本需求 REQ-NNNNN / BUG-NNNN」类引用
- **输入**:文件原始内容(字符串)
- **输出**:清洗后内容(字符串)+ 改动行数
- **复杂度**:O(N)(N = 文件行数,单遍扫描)
- **依赖**:无
- **伪代码**:
  ```
  function applyR1(content):
      # 正则:段尾括号内,含"本需求"+ REQ-NNNNN 或 BUG-NNNN + 任意非闭合括号内容
      pattern = /\s*\(\s*本需求\s+(REQ|BUG)-\d{5}[^)]*\)\s*[,、)]\s*$/m
      repeat:
          prev = content
          content = content.replace(pattern, '')  # 删除匹配段
          # 若删除后该行只剩空白,删除整行
          content = content.replace(/^\s*\n/m, '\n')
      until content == prev  # 迭代至稳定(单行可能有多个匹配)
      return content
  ```
- **关键决策**:
  - 用 `$/m` 锚定行尾,避免跨行匹配误伤合规内容
  - 迭代至稳定(单行可能有多个段尾引用,例如"// (本需求 A 新增,本需求 B 锁定)")
  - **不**删除整段——只删括号,保留段落主旨
- **边界条件**:
  - 整个段落的唯一价值就是这条 REQ 编号引用(例如「### 标题解析(REQ-00013 新增)」括号内只这一串)→ 整行变空 → 删行
  - 「本仓库主动产出 ...」类不是 R-1 范围(无「本需求」关键字)→ 不匹配,保留
- **对应任务**:T-2
- **依据规范**:`skill-conventions §规则 2 §1`

### 算法 2:R-2 「原 code-unit / 原 fix-plan」清理

- **目的**:删除对已退场功能/旧版本的回溯性叙述
- **输入**:文件原始内容
- **输出**:清洗后内容 + 改动行数
- **复杂度**:O(N)
- **伪代码**:
  ```
  function applyR2(content):
      # 正则:括号内或行内含"原/沿用原" + 已退场对象名
      patterns = [
          /\s*\(\s*(原|沿用原)\s+(code-unit|fix-plan|fix-work-log|fix-compile-and-run|fix-test-results)[^)]*\)/g,
          /\b(原|沿用原)\s+(code-unit|fix-plan|fix-work-log|fix-compile-and-run|fix-test-results)\b[^。\n]*/g
      ]
      for p in patterns:
          content = content.replace(p, '')
      # 删除空行
      content = content.replace(/^\s*\n/gm, '\n')
      return content
  ```
- **关键决策**:
  - 两个正则:1 个匹配括号内(段尾);1 个匹配行内散落
  - **不**动"(既有 N 需求 NFR-5 字节级保留)"类合规条款(无"原 code-unit"关键字)→ 安全
- **边界条件**:
  - 「原 code-design 步骤 0b 的 4 问题 → 1 问题 → 0 问题」类回溯性叙述 → 整句删除(行内正则)
  - 「既有 7 个 PLAN(REQ-00004/05/06/07 + 部分其他)不追溯重拆」合规条款 → 不匹配(无"原"字)→ 保留
- **对应任务**:T-2
- **依据规范**:`skill-conventions §规则 2 §2`

### 算法 3:R-3 「Q-N 锁定 / Q-PN 锁定」决策记录清理

- **目的**:删除开发过程中与用户对齐的 Q&A 锚点编号
- **输入**:文件原始内容
- **输出**:清洗后内容
- **复杂度**:O(N)
- **伪代码**:
  ```
  function applyR3(content):
      # 正则:括号内或行内含 Q-N / Q-PN + 锁定/采纳/隐含答复
      pattern = /\s*\(?\s*Q-?P?\d+\s*(锁定|采纳|隐含答复)[^)]*\)?/g
      content = content.replace(pattern, '')
      content = content.replace(/^\s*\n/gm, '\n')
      return content
  ```
- **关键决策**:
  - 用 `(锁定|采纳|隐含答复)` 三选一收紧,避免误伤"Q1 季度"等正常字面
  - 同时匹配括号内外(`\(?` `\)?`),覆盖所有出现形式
- **边界条件**:
  - 「(沿用 V0.0.0 NFR-X)」类版本继承引用(无"Q-")→ 不匹配 → 保留
  - 「(沿用 encoding-conventions §规则 1)」类规范引用(无"Q-")→ 不匹配 → 保留
- **对应任务**:T-2
- **依据规范**:`skill-conventions §规则 2 §3`

### 算法 4:R-4 「YYYY-MM-DD 起生效」清理

- **目的**:删除回溯性生效日标记
- **输入**:文件原始内容
- **输出**:清洗后内容
- **复杂度**:O(N)
- **伪代码**:
  ```
  function applyR4(content):
      # 正则:括号内或行内含日期 + "起生效"
      pattern = /\s*\(?\s*\d{4}-\d{2}-\d{2}\s*起生效\s*\)?/g
      content = content.replace(pattern, '')
      content = content.replace(/^\s*\n/gm, '\n')
      return content
  ```
- **关键决策**:
  - 精确到日期格式 `\d{4}-\d{2}-\d{2}` 收紧
  - 允许 ≤ 3 处合规性例外(AC-4)—— 实施时若发现必要的合规条款,人工保留
- **边界条件**:
  - 「2026-06-15 起生效」类 → 删除
  - 「2026-06-15」(无"起生效")→ 不匹配 → 保留(可能是数据日期)
- **对应任务**:T-2
- **依据规范**:`skill-conventions §规则 2 §4`

### 算法 5:R-5 退场文件名清理

- **目的**:删除对已退场过程文档名的引用
- **输入**:文件原始内容
- **输出**:清洗后内容
- **复杂度**:O(N)
- **伪代码**:
  ```
  function applyR5(content, filePath):
      # 例外:code-fix 自身 SKILL.md / templates/ 不应用 R-5
      if filePath matches /skills/code-fix/(SKILL\.md|templates/):
          return content  # 跳过
      # 退场文件名清单
      deadNames = ['fix-plan\.md', 'fix-work-log\.md', 'fix-compile-and-run\.md', 'fix-test-results\.md']
      for name in deadNames:
          pattern = new RegExp(name, 'g')
          content = content.replace(pattern, '')
      # 清理可能产生的多余空格
      content = content.replace(/[ \t]+/g, ' ').replace(/^\s*\n/gm, '\n')
      return content
  ```
- **关键决策**:
  - **`code-fix` 技能整体豁免 R-5**(因为 `fix/` 目录是其职责,`fix-plan.md` 等不是"已退场"——它们是历史,但**目录语义仍存在**)
  - 删除文件名时**不替换**为新名(因为这些文件是历史档案,无新名可指)
- **边界条件**:
  - `code-plan` 自身 SKILL.md 中可能有"历史 fix-plan.md"引用 → R-5 删除该字面
  - `code-fix` 自身 SKILL.md 中"本技能维护 fix/RESULT.md" → 目录级引用,不含已退场文件名 → 不匹配
- **对应任务**:T-2
- **依据规范**:`skill-conventions §规则 2 §5`

### 算法 6:R-6 杂项清理

- **目的**:删除其他开发痕迹(自然人名等)
- **输入**:文件原始内容
- **输出**:清洗后内容
- **复杂度**:O(N)
- **伪代码**:
  ```
  function applyR6(content):
      # 自然人名(以"变更人:"等前缀出现)
      content = content.replace(
          /\b变更人[:：][\s]*[一-龥A-Za-z\s]{2,30}/g,
          '变更人:<责任人>'
      )
      # 旧版"本仓库主动产出 ... 原 X 位数字"类回溯
      content = content.replace(
          /\(本仓库主动产出[^)]*原\s*\d+\s*位数字[^)]*\)/g,
          ''
      )
      return content
  ```
- **关键决策**:
  - 自然人名统一替换为 `<责任人>` 占位(沿用本仓库已有占位风格)
  - 「原 X 位数字」类回溯整段删除
- **边界条件**:
  - 「变更人:wangmiao」 → 替换为「变更人:<责任人>」
  - 「变更记录」表格行中的具体人名(在「变更人」列)→ 替换
  - 「(本仓库主动产出时五位补零)」(无"原 X 位")→ 不匹配 → 保留(描述当前事实)
- **对应任务**:T-2
- **依据规范**:`skill-conventions §规则 2 §6`

### 算法 7:AC 验证序列

- **目的**:清理完成后跑 8 条 AC 验证
- **输入**:本仓库路径
- **输出**:`boolean`(全过 = true)
- **复杂度**:O(N) × 8(8 条 grep)
- **依赖**:Grep 工具
- **伪代码**:
  ```
  function runACValidation(workspacePath):
      results = []
      # AC-1:无「本需求 REQ-」段尾
      results += grep(workspacePath, /本需求\s+(REQ|BUG)-\d{5}/, expected=0)
      # AC-2:无「原 code-unit/fix-plan」(允许 ≤ 3 处例外)
      results += grep(workspacePath, /原\s+(code-unit|fix-plan|fix-work-log)/, expected<=3)
      # AC-3:无「Q-N 锁定」
      results += grep(workspacePath, /Q-?P?\d+\s*锁定/, expected=0)
      # AC-4:无「YYYY-MM-DD 起生效」(允许 ≤ 3 处例外)
      results += grep(workspacePath, /\d{4}-\d{2}-\d{2}\s*起生效/, expected<=3)
      # AC-5:跨技能契约 5 处抽查(人工)
      results += manualCheck(5 个跨技能引用未坏)
      # AC-6:占位符仍存在
      results += grep(workspacePath, /REQ-00001/, in='templates/*.md', expected>=1)
      # AC-7:code-dashboard 可运行
      results += runCodeDashboard(workspacePath)  # 调 /code-dashboard,期望无错
      # AC-8:单次 commit
      results += gitLogCount(since='1 hour', expected=1)
      return all(results)
  ```
- **关键决策**:
  - AC-5 / AC-7 / AC-8 不能纯靠 grep,需人工/工具调用 → 单独标记
  - AC-2 / AC-4 允许 ≤ 3 处例外(保留必要的合规性条款)
- **边界条件**:
  - grep 结果含非目标文件(例如 `assistants/` 历史档案)→ 应排除(只对 `plugins/code-skills/skills/` 跑)
- **对应任务**:T-3
- **依据规范**:REQ-00036 AC-1 ~ AC-8

## 6. 数据结构完整变更

**本节对应概要设计 §9 — 本设计 0 新增 / 0 修改实体**。

### 6.1 新增实体
- (无)

### 6.2 修改实体
- (无)

### 6.3 数据迁移
- (无)

## 7. 接口细节

**本节对应概要设计 §8 — 本设计 0 新增 / 0 修改 / 0 调用外部接口**。

### 7.1 接口总览
(无)

### 7.2 关键决策
- 不涉及

## 8. 异常处理

**详见 `risk-analysis.md` §异常处理**。

按异常类别:
- **输入校验**:本仓库是纯文本,无外部输入。grep 模式匹配的失败是"未命中",不是异常。
- **外部依赖**:Git 命令(`git add` / `git commit` / `git diff` / `git log`)失败 → 透传 stderr
- **并发冲突**:**不**并发(任务串行 T-1 → T-2 → T-3)
- **资源耗尽**:单文件最大 ~ 50KB,内存充足
- **业务异常**:
  - 改动后行数减少 > 30% → 回退该文件(E-3)
  - AC 验证失败 → 整体回退(NFR-10)
- **未知异常**:任务执行过程中任何非预期错误 → 中止当前任务 + git revert(已 commit 部分)

## 9. 安全要求

**本节是详细设计区别于概要设计的核心:必须给出可直接编码的细节**。本设计**不涉及**:
- 鉴权(无用户系统)
- 授权(无权限系统)
- 输入校验(无外部输入)
- 敏感数据处理(无敏感数据)
- 防注入(无 SQL / NoSQL / 命令注入面)
- 审计(无业务系统)

**依据规范**:N/A。

## 10. 状态机 / 流程

```
stateDiagram-v2
    [*] --> T1_Plan
    T1_Plan --> T1_Done: 文件清单 + 命中计数产出
    T1_Done --> T2_Apply: 顺序进入 T-2
    T2_Apply --> T2_Done: 6 条规则全部应用 + diff 校验通过
    T2_Apply --> T2_Revert: 任一文件改动后行数 > 30% → 回退该文件
    T2_Revert --> T2_Apply: 继续后续文件
    T2_Done --> T3_Verify: 顺序进入 T-3
    T3_Verify --> T3_Done: 8 条 AC 全过
    T3_Verify --> T3_Abort: 任一 AC 失败 → git revert + 中止
    T3_Done --> [*]: 1 次 commit + 看板同步
```

## 11. 性能与资源

**本仓库无性能要求,性能优化通过外部调优完成**。
- 预计执行时间:< 30 秒(14 SKILL.md + 23 templates = ~37 文件,单遍扫)
- 内存:单文件最大 ~ 50KB,合计 < 2MB
- CPU:纯文本处理,无计算密集
- 资源限制:无
- 缓存策略:无
- 批量/异步:无
- 降级策略:无

## 12. 测试要点

- **单元测试**:不适用(本仓库纯文档,无可测代码载体)
- **集成测试**:AC-7 — 调 `/code-dashboard` 验证 SKILL.md 仍可被解析
- **端到端测试**:AC-7 同上
- **性能/压力测试**:不适用
- **安全测试**:不适用
- **回归测试**:AC-5 — 抽查 5 个跨技能引用未坏

每条测试要点 → 对应任务 T-3(AC 验证序列)。

## 13. 关联需求

(无)

## 14. 待澄清 / 未决项

| 编号 | 问题 | 影响范围 | 阻塞方 | 期望回复时间 |
| --- | --- | --- | --- | --- |
| Q-1 | 清理后是否需要重新跑一次 `code-check` 对所有 SKILL.md 做静态评审? | 验证清理质量 | 用户 | (非阻塞) |
| Q-2 | `code-it` 阶段发现某些段落"剥离不了"——是回退整次清理,还是接受遗留? | E-3 | 用户 | (非阻塞,默认回退) |

## 15. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-06-16 17:33 | v1 | 初始创建 | 完成首次详细设计;6 条清理算法的精确正则 + 1 个范围过滤器 + 1 个 AC 验证序列;3 条 `code-it` 任务(串行);0 新增模块/接口/数据结构/依赖 | 用户 |