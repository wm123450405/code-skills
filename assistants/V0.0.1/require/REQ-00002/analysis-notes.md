# 分析笔记 — REQ-00002
更新时间:2026-06-03 20:18(v2 增量更新)

## v2 增量补充(Q-7 锁定)
用户在第 2 轮通过追加指令直接锁定 Q-7 答案:
> 任务编码命名规范:需求任务为 `TASK-REQ-需求编码-NNNNN`,修复任务为 `TASK-BUG-缺陷编码-NNNNN`

这是 v1 分析时未列出的**第四方案 G4 — 新嵌套式**,优于 G1/G2/G3:
- **G4 vs G1(全局独立)**:G4 通过编码本身保留"任务属于谁"的视觉关系,无需 PLAN.md 加"所属需求"列
- **G4 vs G2(REQ-TASK-嵌套)**:G4 用 `TASK-REQ` / `TASK-BUG` 双前缀清晰区分需求任务与修复任务,语义更精准
- **G4 vs G3(`REQ-NNNNN-NNN`)**:G4 显式 `TASK-` 前缀让任务在编码层面"自我介绍",不需依赖位置推断

### G4 带来的实施影响
- code-it 的 regex 从单一 `^REQ-\d{4}-\d{4}-\d{3}$` 改为联合表达 `^TASK-(REQ|BUG)-\d{5}-\d{5}$`,且需双路径分支
- code-plan 的"任务编号分配"逻辑:在父级(REQ 或 BUG)的工作目录内查最大 TASK 编号 + 1,无需全局扫描
- code-it / code-unit / code-review 中"由任务编码反推父级"的逻辑:直接从 TASK 编码第 2 段(REQ/BUG)与第 3 段(数字)即可确定,无需查 PLAN.md
- 派生任务(code-review 派生的"审查改修"任务)编码:仍属于同一父级,继续在父级内递增

### 遗留 Q-12(本 v2 新引入)
"需求编码"在 TASK 编码中含 REQ- 前缀吗?用户字面表达 `TASK-REQ-需求编码-NNNNN` 中"需求编码"是指完整字符串(REQ-00001)还是仅数字段(00001)?

- v2 默认采用 (a) **仅数字段**:`TASK-REQ-00001-00001`(更简洁,正则更短)
- 若 (b) 含 REQ- 前缀:`TASK-REQ-REQ-00001-00001`(更直观但啰嗦)

这是 v2 的最大不确定性,影响所有正则、模板示例、说明文字。

---

## 需求理解(v1)
用户希望把项目内三类编码格式统一:
- **需求编码**:`REQ-YYYY-NNNN`(年份 + 4 位)→ `REQ-NNNNN`(纯 5 位)
- **任务编码**:`<需求编号>-<任务序号>`(嵌套式,如 `REQ-2026-0001-001`)→ `TASK-NNNNN`(独立 5 位 — Q-7 待用户确认)
- **缺陷编码**:`BUG-NNN`(3 位)→ `BUG-NNNNN`(5 位)

核心理念变化:
1. **去年份化**:REQ 不再含年份段,纯递增编号
2. **去嵌套化(候选)**:TASK 可能从"父需求嵌套"改为"全局独立计数"
3. **位数统一**:三类均 5 位,视觉一致

## 涉及面分析(穷举式)

### A. 代码与协议文件(无)
- 仓库无源代码,无 CI/CD 配置,无 lint 规则;编码格式纯靠人工 + AI 遵守

### B. SKILL.md(10 个技能)
| 技能 | 含编码格式的位置 | 调整动作 |
| --- | --- | --- |
| code-init | 产生 EXISTING-NNN(3 位)的逻辑、INIT-REPORT 与 existing-requirement 模板示例 | 视 Q-6 决定保留或改为 REQ-NNNNN |
| code-version | 描述编码命名建议、版本看板模板字段 | 改示例 |
| code-rule | (不直接管编码) | 视 Q-8 决定是否新增 `encoding-conventions.md` |
| code-require | SKILL.md 第 17 行"建议 REQ-YYYY-NNNN";模板 requirements.md 中文档头与示例 | 改为 REQ-NNNNN |
| code-design | 模板与示例 | 改示例 |
| code-plan | 任务编号分配逻辑(`<需求编号>-<任务序号>`)、task-plan.md 模板 | **视 Q-7 重写分配逻辑** |
| code-it | regex `^REQ-\d{4}-\d{4}-\d{3}$`、拆分逻辑、模板示例 | **视 Q-7 重写 regex + 拆分** |
| code-unit | "任务编码"格式描述、模板示例 | 同 code-plan/it |
| code-fix | BUG 编号格式、fix-registry.md 模板 | 改为 BUG-NNNNN |
| code-review | 派生任务编码生成规则(基于父任务)、REVIEW-REPORT / REVIEW-FIX 模板 | 视 Q-7 重写派生规则 |

### C. 模板(20+ 文件)
- 主要影响:示例值 `REQ-2026-0001`、`BUG-001`、`REQ-2026-0001-001` 等需要批量替换
- 注意:**示例值与"格式占位符"(如 `<REQ-YYYY-NNNN>`)是两个维度**;占位符应改为 `<REQ-NNNNN>`,示例值应改为如 `REQ-00001`

### D. README.md / README.en.md
- 第 258-296 行典型流程示例段,大量使用 `REQ-YYYY-NNNN-001`、`BUG-NNN`
- 必须中英文同步(doc-conventions §规则 1)

### E. CLAUDE.md
- 第 24/88/99/100 行引用 BUG-NNN 与 REQ-YYYY-NNNN
- 需同步

### F. 历史工作目录
| 目录 | 当前编码 | 新编码 | 备注 |
| --- | --- | --- | --- |
| `./assistants/V0.0.1/require/REQ-00001/`(原 `REQ-2026-0001/`,2026-06-03 20:20 重命名) | REQ-2026-0001 | REQ-00001 | 重命名已部分落地(目录 + 本工作空间);SKILL.md/模板/README 维度的编码清理待 `code-it` 阶段 |
| `./assistants/V0.0.0/require/EXISTING-001 ~ EXISTING-010/` | EXISTING-NNN | ??? | **待 Q-6 决策** |

### G. 版本看板(V0.0.0 与 V0.0.1 的 RESULT.md)
- "需求清单"区段所有编码引用需同步;追加"重命名变更"到"变更记录"

### H. cache 副本
- `C:\Users\wm123\.claude\plugins\cache\code-skills\code-skills\1.0.0\skills\...`
- 本仓库无权写入用户 cache;依赖 `/reload-plugins` 由 Claude Code 自动同步
- 不在本仓库的可控范围,**仅在 README 提示"实施后需 /reload-plugins"**

## 候选方案权衡(关于 Q-7 — TASK 编码结构)

### 方案 G1:全局独立计数 `TASK-NNNNN`
- ✅ 与 BUG、REQ 维度齐平,三者同为顶级实体
- ✅ 任务编码可独立排序、独立列表
- ❌ 失去"任务属于哪个需求"的视觉提示;需在 PLAN.md / 任务清单加"所属需求"列
- ❌ code-it / code-unit 中"由任务编码反推需求编码"的逻辑需改为"查 PLAN.md"
- ✅ 与用户输入字面"TASK-NNNN"最一致

### 方案 G2:嵌套式 `REQ-NNNNN-TASK-NNNN`
- ✅ 保留父子关系直观性
- ❌ 编码变长(20+ 字符),不友好
- ❌ 与用户输入字面"TASK-NNNN"略不一致

### 方案 G3:轻度嵌套 `REQ-NNNNN-NNN`
- ✅ 与现行结构最接近,改动最小
- ❌ 不符合"统一 TASK- 前缀"的用户预期
- ❌ 与用户输入字面"TASK-NNNN"不一致

**推荐**:G1(全局独立计数)— 与用户字面表述吻合度最高;牺牲"目录树肉眼归属"换取"编码维度齐平"

## 候选方案权衡(关于 Q-6 — EXISTING- 是否一并改名)

### 方案 H1:保留 EXISTING- 前缀
- ✅ 保留 code-init 基线的特殊语义("代码现状的快照"vs"未来需求")
- ✅ code-init SKILL.md 改动最小
- ❌ "三类编码统一"目标不彻底 — 出现第四类前缀

### 方案 H2:全部改名为 REQ-NNNNN(从某个起点)
- ✅ 编码体系彻底统一(只剩 REQ/TASK/BUG)
- ❌ 失去"基线 vs 新需求"的视觉区分
- ❌ code-init SKILL.md 第 7-8 步需重写(改为生成 REQ-NNNNN)

### 方案 H3:折中 — EXISTING- 改为 REQ- 但标记 `existing=true` 元字段
- ⚠ 引入额外抽象,违反"避免过度设计"原则

**推荐**:H1(保留 EXISTING-)— 用户面 Q-2 选"追溯覆盖"主要意图是"REQ-2026-0001 → REQ-00001",EXISTING- 的语义本就独立;但仍由用户最终决定

## 临时假设
- **假设 A1**:本需求实施顺序在 REQ-2026-0001 之后(见 related-requirements.md 推荐)
- **假设 A2**:Q-7 选 G1(全局独立计数)— 用作 FR 撰写基准,若用户否决可增量更新
- **假设 A3**:Q-6 选 H1(保留 EXISTING-)— 用作 FR 撰写基准
- **假设 A4**:Q-8 选 (a)(新建 `encoding-conventions.md`)— 让规则文件成为强制约束源,而非散布于各 SKILL.md
- **假设 A5**:Q-9 选 (a)(持久化 migration-mapping.md)— 便于实施后回溯审计
- **假设 A6**:本需求**不**修改 cache 副本(超出仓库可控范围)

> 上述假设均在 RESULT.md §12 中列为待澄清,用户回答后做增量更新

## 风险
- **R-1(范围蔓延)**:涉及 30+ 文件;若 Q-7 决策反复,FR 重写代价大
- **R-2(同步遗漏)**:嵌入式 regex(code-it line 104)与文本叙述容易漏改;`code-review` 阶段必须穷举式 Grep
- **R-3(cache 滞后)**:Claude Code 加载的是 cache 副本,改源不立即生效;实施完成需依赖用户执行 `/reload-plugins`
- **R-4(自指悖论)**:本需求工作目录已使用 REQ-00002(新格式);若实施过程中暂时回滚,本目录名亦需考虑
- **R-5(EXISTING- 决策影响 code-init)**:若 Q-6 选 H2,code-init 的逻辑要重写,且未来再次跑 code-init 的新项目会用新格式 — 不可逆

## 下一轮深挖方向
- Q-7 决策后,补充 FR:`code-plan` 中"任务编号分配算法"的具体步骤(查最大 TASK-NNNNN + 1 全局递增)
- Q-8 决策后,若新建 encoding-conventions.md,起草规则文件的章节结构
- Q-9 决策后,设计 migration-mapping.md 的字段(原编码 / 新编码 / 改名时间 / 涉及文件清单)
