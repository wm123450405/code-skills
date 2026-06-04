# 设计 notes — REQ-00004

更新时间:2026-06-04 15:50
版本:V0.0.2

> 本文档记录概要设计阶段的关键设计问题、候选方案、选定理由与备选否决理由。
> 每条决策旁标注"依据规范"。

---

## 问题清单(8 个)

1. **SKILL.md 结构**:`code-dashboard` 技能入口文件的章节骨架
2. **解析器架构**:`RESULT.md` 区段解析的策略(单遍扫描 / 多遍)
3. **任务编号解析**:新格式 vs 旧格式优先级;路径生成
4. **建议生成器**:5 类建议的触发条件、优先级策略、命令格式
5. **ASCII 渲染器**:比例条宽度、字符选择、终端兼容性
6. **参数解析**:无参数 / `REQ-NNNNN` / 非法参数 三态
7. **性能策略**:NFR-4 < 5 秒的实现路径
8. **错误处理**:NFR-2 "不崩溃"的退化策略

---

## Q-1:SKILL.md 章节结构

### 候选
- **A(选定)**:**完全复用 `code-design` 既有 SKILL.md 骨架**(目标 / 适用场景 / 不适用 / 工作目录约定 / 输入 / 输出 / 工具使用约定 / 工作流步骤 / 边界与异常 / 衔接 / 不要做的事)
- **B**:简化版(只含"目标 / 适用 / 步骤 / 不要做")— 短小但与既有 10 个 SKILL.md 风格不一致
- **C**:详细版(加入"算法伪代码"段) — 与既有风格差异大,AI 阅读体验降低

### 选定:**A**
- **理由**:
  - 与既有 10 个 SKILL.md 章节顺序、命名、深度完全一致;`code-rule` / `code-init` 等未来升级时不会因风格漂移触发"全面重写"
  - 复用 `code-design` 的骨架:本技能与 `code-design` 同为"读取型 + 多区段解析",步骤流程天然同构
- **规范依据**:`skill-conventions §规则 1`(frontmatter 一致);隐含"`SKILL.md` 风格一致"项目惯例

---

## Q-2:`RESULT.md` 解析器架构

### 候选
- **A(选定)**:**单遍扫描 + 行号锚点定位**
  - 一次 `Read` 读全文(避免多次 IO,NFR-4)
  - 用正则 `^## .*$` 找出所有 `## ` 标题行 + 行号
  - 按"需求清单 / 任务清单 / 缺陷清单" 3 个目标区段,提取"标题行 + 1 → 下一个 `## ` 或 `---` 前一行"区间
  - 在区间内用 `^\| .* \|$` 匹配表格行 + `\|` 切分列
- **B**:多次 `Read` 每次只读一个区段 — IO 多,违反 NFR-4
- **C**:外部 Markdown 解析库 — 违反 NFR-1

### 选定:**A**
- **理由**:
  - 单次 IO + 内存解析 ≈ < 100ms(V0.0.2 看板 ≈ 280 行实测)
  - 不依赖外部库(NFR-1)
  - 行号锚点对齐 `## ` 标题,与"看板字段约定"自然契合
- **规范依据**:NFR-4 性能约束 + `dashboard-conventions §规则 1` 区段语义

### 子算法
```
parseDashboard(text):
  lines = text.split('\n')
  anchors = {}
  for i, line in enumerate(lines):
    m = re.match(r'^## (.+)$', line)
    if m: anchors[m.group(1).strip()] = i
  // 需求清单区段
  reqStart = anchors.get('需求清单', -1) + 1
  reqEnd = nextAnchor(anchors, '需求清单', -1)
  reqRows = extractTableRows(lines[reqStart:reqEnd])
  // 同理 tasks, bugs
  return { requirements: reqRows, tasks: taskRows, bugs: bugRows }
```

---

## Q-3:任务编号解析(NFR-3 双格式兼容)

### 候选
- **A(选定)**:**新格式优先 + 旧格式透传**
  - 第 1 步:用 `^TASK-(REQ|BUG)-(\d{5})-(\d{5})$` 匹配(新格式)
  - 第 2 步:若失败,用 `^(REQ|BUG)-(\d{5})-(\d{5})$` 匹配(旧格式)
  - 第 3 步:旧格式不参与"路径生成",仅作为 `displayId` 字符串保留
  - 第 4 步:输出 `/code-it TASK-REQ-00004-001` 等命令时,**强制**用新格式字面
- **B**:只支持新格式(违反 NFR-3,V0.0.1 REQ-00001 任务会显示为空)
- **C**:统一为新格式(改看板字面 — 违反 FR-7 AC-7.1 "不修改看板",NFR-6 边界)

### 选定:**A**
- **理由**:
  - NFR-3 显式要求"同时支持两种字面"
  - 旧格式只读透传(显示侧),不进入"路径解析"路径,避免误判
  - 生成命令时**严格按新格式**,与 `encoding-conventions §规则 3` 一致
- **规范依据**:`encoding-conventions.md §规则 1/3` + NFR-3 锁定

### 数据结构
```ts
type TaskId = {
  format: "new" | "old",
  type: "REQ" | "BUG",
  parentNum: string,  // 5 位父级数字段
  taskNum: string,    // 5 位任务序号
  displayId: string   // 字面原样
}
```

---

## Q-4:下一步建议生成器(FR-4)

### 候选
- **A(选定)**:**5 类建议的优先级排序 + 最多 5 条**
  - **优先级 P0(高)**:
    1. 版本无任何需求 → `建议: 执行 /code-require 添加首个需求`
    2. 版本有 P0 待修复缺陷 → `建议: 执行 /code-fix BUG-NNNNN`
    3. 需求已存在但无概要设计 → `建议: 执行 /code-design REQ-NNNNN`
  - **优先级 P1(中)**:
    4. 任务"开发状态=待开始" → `建议: 执行 /code-it TASK-REQ-NNNNN-NNNNN`
    5. 需求"概要设计=已完成 ∧ 详细设计≠已完成" → `建议: 执行 /code-plan REQ-NNNNN`
  - **优先级 P2(低)**:
    6. 任务"测试状态=已编写" → `建议: 执行 /code-unit TASK-...`
    7. 需求"已完成 + 评审发现汇总非空" → `建议: 执行 /code-review REQ-NNNNN`
  - **特殊**:
    8. 全版本已完成 → `建议: 执行 /code-version V0.0.x 创建下一个版本`
  - 取前 5 条按优先级降序输出
- **B**:仅按"任务待开始"一种类型生成 — 信息量不足(无法覆盖"无需求"边界)
- **C**:无限条建议(最多 N = 需求数 × 任务数)— 违反 AC-4.3 最多 5 条

### 选定:**A**
- **理由**:
  - 完整覆盖 FR-4 列出的 5 类触发条件
  - 优先级明确(高/中/低/—),与 AC-4.1 三字段对应
  - 5 条上限避免输出过长(AC-4.3)
- **规范依据**:FR-4 锁定 + AC-4.1/4.2/4.3

### 命令格式严格按既有 SKILL.md
- `/code-require`(无参数或主题词) — 见 `code-require/SKILL.md`
- `/code-design REQ-NNNNN` — 见 `code-design/SKILL.md` frontmatter `description`
- `/code-plan REQ-NNNNN` — 同上
- `/code-it TASK-REQ-NNNNN-NNNNN` — 见 `code-it/SKILL.md`
- `/code-unit TASK-REQ-NNNNN-NNNNN` — 见 `code-unit/SKILL.md`
- `/code-fix BUG-NNNNN` — 见 `code-fix/SKILL.md`
- `/code-review REQ-NNNNN` — 见 `code-review/SKILL.md`
- `/code-version V0.0.x` — 见 `code-version/SKILL.md`

---

## Q-5:ASCII 渲染器

### 候选
- **A(选定)**:**固定 12 字符 + Q-3 锁定的字符集**
  - `BAR_WIDTH = 12`(Q-D3 锁定)
  - 实心:`█`(U+2588)
  - 空心:`░`(U+2591)
  - P0 标记:`█`
  - P1 标记:`▓`(U+2593)
- **B**:动态宽度(按终端宽度)— 增加复杂度,无明显收益
- **C**:Unicode 块字符全集 — 终端兼容性差

### 选定:**A**
- **理由**:
  - 固定 12 字符在 80 字符终端下不换行
  - `█` / `░` / `▓` 均为 BMP 字符,主流终端(Windows Terminal / iTerm2 / GNOME Terminal)均支持
  - 与 Q-3 锁定的"醒目标记"字符集一致
- **规范依据**:Q-1 + Q-3 + Q-D3 锁定

### 算法
```ts
function bar(filled: number, total: number): string {
  if (total === 0) return '[' + '░'.repeat(12) + '] 0%'
  const pct = Math.round(filled / total * 100)
  const blocks = Math.round(pct / 100 * 12)
  return '[' + '█'.repeat(blocks) + '░'.repeat(12 - blocks) + '] ' + pct + '%'
}
```

---

## Q-6:参数解析(FR-6)

### 候选
- **A(选定)**:**三态机 + 正则校验**
  - 0 参数 → 总览模式
  - 1 参数匹配 `^REQ-\d{5}$` → 需求粒度模式
  - 1 参数不匹配 → 错误模式(打印用法 + 退出)
- **B**:Try/catch 包裹整个流程 — 异常粗粒度,用户感知差
- **C**:更宽松的参数(允许小写 `req-00001`) — 与既有 SKILL.md 严格大写不一致

### 选定:**A**
- **理由**:
  - 严格 `^REQ-\d{5}$` 与 `encoding-conventions §规则 1` 一致
  - 错误模式立即退出(无副作用,NFR-7 幂等)
- **规范依据**:FR-6.AC-6.3 + `encoding-conventions §规则 1`

---

## Q-7:性能策略(NFR-4 < 5 秒)

### 候选
- **A(选定)**:**并行 Read + 单遍解析**
  - 启动阶段:1 次 `Read` 读 `.current-version`
  - 总览模式:1 次 `Read` 读 `RESULT.md`(主)
  - 需求模式:**并行** 3 次 `Read`(`require/.../RESULT.md` + `plan/.../PLAN.md` + 主 `RESULT.md`)
  - 解析阶段:单遍 O(N) 扫行(N = 行数,典型 < 500)
  - 渲染阶段:O(M)(M = 表格行数,典型 < 200)
  - 估算:< 1 秒(V0.0.2 实测看板 280 行 < 500ms)
- **B**:单线程串行 Read — 慢 2-3 倍,违反 NFR-4
- **C**:加缓存层(例如把 `RESULT.md` 解析结果缓存到内存) — 引入状态,违反 NFR-7 幂等

### 选定:**A**
- **理由**:
  - NFR-4 显式要求 < 5 秒;预留 4 秒余量
  - 并行 Read 利用 Claude Code 工具并发能力
  - 无状态(NFR-7 幂等)
- **规范依据**:NFR-4 + NFR-7

---

## Q-8:错误处理(NFR-2 不崩溃)

### 候选
- **A(选定)**:**分 3 层退化**
  - **L1 启动错误**(`.current-version` 缺失 / 指向不存在版本):打印引导 + 退出(FR-5)
  - **L2 数据错误**(看板文件缺失 / 区段缺失 / 表格列错位):显示 `(无)` / `?` / `(未知)`,继续渲染
  - **L3 异常捕获**(任何未预期错误):打印 `✗ 内部错误: <msg>` + 退出(不污染 git status)
- **B**:任何错误都退出 — 用户体验差
- **C**:任何错误都吞掉继续 — 静默失败,违反 NFR-2 反馈性

### 选定:**A**
- **理由**:
  - L1 致命(无法继续,必须退出)
  - L2 可降级(展示 `(无)` 占位,NFR-2 AC)
  - L3 兜底(避免栈追踪污染屏幕)
- **规范依据**:NFR-2 + FR-5 + 边界 §9 E-1~E-10

### L2 退化策略详表

| 缺失项 | 退化显示 |
| --- | --- |
| 主 `RESULT.md` | `✗ 看板文件不存在,请先调 code-version` |
| `## 需求清单` 区段 | 段 1 整段显示 `(无)` + 计数 = 0/0/0/0 |
| `## 任务清单` 区段 | 段 2 整段显示 `(无)` + 计数 = 0 |
| `## 缺陷清单` 区段 | 段 3 显示 `P0 待修复: (无) P1 待修复: (无)` |
| 表格列错位 | 退化到"原始 markdown 块"原样输出 |
| 字段值缺失 | 显示 `?` |
| 需求模式:子文件缺失 | 同 E-3 列出本版本所有需求 |

---

## 备选方案被否决理由(汇总)

| Q | 备选 | 否决理由 |
| --- | --- | --- |
| Q-1 | B/C | 与既有 10 个 SKILL.md 风格不一致;增加 AI 协作者阅读成本 |
| Q-2 | B/C | NFR-4 / NFR-1 触发 |
| Q-3 | B/C | NFR-3 / FR-7 触发 |
| Q-4 | B/C | FR-4 / AC-4.3 触发 |
| Q-5 | B/C | 增加复杂度,无明显收益;字符兼容性差 |
| Q-6 | B/C | 与 `encoding-conventions` 严格正则不一致;异常粗粒度 |
| Q-7 | B/C | NFR-4 / NFR-7 触发 |
| Q-8 | B/C | NFR-2 触发(用户体验差 / 静默失败) |

---

## 风险与遗留

| 风险 | 缓解 |
| --- | --- |
| V0.0.x 看板"任务清单"区段中同时含新/旧格式任务字面,解析器必须容错 | Q-3 双格式兼容;边界 E-9 透传 |
| 未来 V0.0.x+ 看板"任务清单"列结构可能微调 | 解析器按列名定位(`任务编号 / 需求 / 类型 / 触发\/来源 / 标题 / 开发状态 / 测试状态 / ...`),不假设列数 |
| `code-dashboard` 自身被 V0.0.2 并发需求误调 | 边界 E-10:`code-dashboard` 自身异常 → 退出(无内部状态可污染) |
| `code-rule` 未来沉淀新规则(如 `dependency-conventions §规则 1`) | NFR-1 已锁零依赖,无需追溯 |
