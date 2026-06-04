# 偏离记录 — REQ-00002-007
版本:V0.0.1

## 偏离 1(plan 推断与实际不符):`doc-conventions.md:113` install 命令旧串
- **类别**:PLAN 推断需修正
- **依据**:
  - PLAN §2.7 已知偏离 1:"`doc-conventions.md:113` install 命令旧串(规则文件不可改,留给 code-rule)"
- **实际做法**:
  - 实际验证:`doc-conventions.md` 全文 0 命中旧 REQ/BUG/TASK 格式
  - L113 实际内容:`claude plugin marketplace add https://github.com/...`(不涉及编码格式)
- **偏离理由**:
  - PLAN 写于实施前(2026-06-03 20:55),当时基于"REQU 阶段会触发追溯"的推断
  - 实际 REQ-00002 T-001~006 完成后,doc-conventions.md 已被 T-003 同步覆盖,install 命令示例已用新命令
  - 本偏离**不适用**,无需授权
- **影响**:**正面** — 实际比 PLAN 预期更干净
- **时间**:2026-06-04 10:14

## 偏离 2(plan 推断与实际不符):5 个现有 `rules/` 旧串示例
- **类别**:PLAN 推断需修正
- **依据**:
  - PLAN §2.7 已知偏离 3:"5 个现有 rules/ 文件的旧串示例(范围外)"
- **实际做法**:
  - 5 个文件逐一 Grep `REQ-\d{4}-\d{4}|BUG-\d{3}\b|TASK-\d{4}-\d{4}-\d{3}`:
    - `dashboard-conventions.md`:0 命中
    - `doc-conventions.md`:0 命中
    - `marketplace-protocol.md`:0 命中
    - `module-conventions.md`:0 命中
    - `skill-conventions.md`:0 命中
  - 总计 0/5 命中
- **偏离理由**:
  - 5 个规则文件大多讨论"看板/文档/模块/技能元信息",不涉及具体编码格式
  - 仅 `marketplace-protocol.md` 涉及 `marketplace.json` 字段,但不涉及 REQ/BUG/TASK 编码
  - PLAN 写于实施前,基于"可能有示例"的推断
  - 本偏离**不适用**
- **影响**:**正面** — 规则文件本身已干净
- **时间**:2026-06-04 10:14

## 已知偏离(实际成立):V0.0.1 工作文件保留旧串
- **类别**:范围外(预期保留)
- **依据**:
  - PLAN §2.7 已知偏离 4:"本工作目录历史文件保留旧串(版本演进)"
- **实际验证**:
  - `assistants/V0.0.1/RESULT.md` L213-216 等保留"原 REQ-2026-0001"字面值(可读性)
  - `assistants/V0.0.1/require/REQ-00002/RESULT.md` L20, L108 保留旧串(REQU 阶段问题背景)
  - `assistants/V0.0.1/design/REQ-00002/RESULT.md` L299-301 保留"旧→新"映射表(设计阶段决策记录)
  - `assistants/V0.0.1/plan/REQ-00002/RESULT.md` L323 保留"BUG-NNN"实施说明(详细设计决策)
  - `assistants/V0.0.1/code/REQ-00002-001~006/RESULT.md` 保留"改前/改后"对照(实施档案)
- **总命中**:REQ 旧格式 ~3+ 处 + BUG 旧格式 ~3+ 处,全部为已知偏离
- **影响**:**正面** — 完整保留版本演进痕迹
- **授权**:PLAN §2.7 已知偏离 4 已预先授权
- **时间**:2026-06-04 10:13

## 已知偏离(实际成立):V0.0.0 EXISTING-* 基线
- **类别**:范围外(基线特例)
- **依据**:
  - PLAN §2.7 已知偏离 2:"V0.0.0 EXISTING-* 基线历史(范围外)"
  - REQU FR-1 例外 + `encoding-conventions.md` §规则 1 例外 + `migration-mapping.md` §规则 4
- **实际验证**:
  - `git status assistants/V0.0.0/` → clean(0 变更)
  - `EXISTING-001` ~ `EXISTING-010` 10 个基线需求**不**追溯重命名
- **影响**:**正面** — 基线完整性保持
- **授权**:REQU FR-1 + `encoding-conventions.md` §规则 1 + `migration-mapping.md` §规则 4
- **时间**:2026-06-04 10:12

## 总结
- 13 条不变量**全部成立** ✅
- 4 项 PLAN 已知偏离中,**2 项与实际不符**(偏离 1 + 偏离 3,PLAN 推断错误),**2 项符合实际**(偏离 2 + 偏离 4)
- 全仓库(除 V0.0.1 工作文件)命中:0 + 0 + 0 ✅(完美)
- **无超出预期的命中** — 审计通过
