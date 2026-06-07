# 关联需求 — REQ-00024
更新时间:2026-06-07

## REQ-00005 (code-auto 初版,V0.0.2 已完成)
- **关联点**:同一 `code-auto` 技能;本需求是 REQ-00005 的第 2 次演化
- **影响**:本需求保留 REQ-00005 既定契约(6 步状态机、6 子技能编排、auto-report.md 输出)
- **来源**:扫描 `assistants/V0.0.3/require/REQ-00005/RESULT.md`

## REQ-00007 (code-auto v2 模式 B,2026-06-05 已完成)
- **关联点**:同一 `code-auto` 技能 v2;本需求**撤销** REQ-00007 的"模式 B from 关键字"逻辑,沿用其语义但改用路径感知触发
- **影响**:本需求保留 REQ-00007 既有"模式 B 跳过 code-require 沿用 RESULT.md"语义;屏显格式沿用 v2
- **来源**:扫描 `assistants/V0.0.3/require/REQ-00007/RESULT.md`

## BUG-00001 (code-require/code-design/code-plan/code-fix 职责混淆,V0.0.3 修复中)
- **关联点**:本需求是"code-auto 改造";BUG-00001 是"`code-fix` 职责修复"
- **影响**:0 直接影响;但 BUG-00001 修复路径中的 `/code-auto from BUG-00001` 调用方式将变为 `/code-auto BUG-00001`(移除 `from`)
- **来源**:扫描 `assistants/V0.0.3/fix/BUG-00001/RESULT.md`

## code-fix 技能的 from 关键字(REQ-00021 改后)
- **关联点**:`code-fix` 自身有 `from REQ-NNNNN` / `from BUG-NNNNN` 双模式
- **影响**:**不**在本需求修改范围;`code-fix` 改造属另一需求
- **依据**:`code-fix/SKILL.md` 步骤 1.2
