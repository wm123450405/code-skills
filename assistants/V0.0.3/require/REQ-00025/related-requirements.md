# 关联需求 — REQ-00025
更新时间:2026-06-07

## REQ-00002 (V0.0.1) — 编码格式权威源初版
- **关联点**:同一 `encoding-conventions.md`;REQ-00002 是"5 位纯数字"强约束的初版
- **影响**:本需求是 REQ-00002 的"放宽版";保留 REQ-00002 既定契约(默认生成仍为 5 位纯数字)
- **来源**:扫描 `assistants/V0.0.3/require/REQ-00002/RESULT.md`

## REQ-00007 (V0.0.2) — code-auto v2 关键字
- **关联点**:本需求不涉及 code-auto;0 直接影响
- **影响**:无
- **来源**:扫描 `assistants/V0.0.3/require/REQ-00007/RESULT.md`

## REQ-00024 (V0.0.3) — 路径感知判定
- **关联点**:本需求放宽"需求编号"字面 → 路径感知下 `code-auto` 可识别任意前缀的需求(如 `JIRA-123`)
- **影响**:REQ-00024 路径感知逻辑继续工作;本需求不修改 REQ-00024 任何文件
- **来源**:扫描 `assistants/V0.0.3/require/REQ-00024/RESULT.md`

## `encoding-conventions.md` — 编码权威源
- **关联点**:本需求**直接修订** §规则 1 + §规则 2 + §规则 4 + 新增 §规则 1.5
- **影响**:0 字段新增;既有 `EXISTING-NNN` 旧格式继续工作(沿用 §规则 4 例外)
- **依据**:`assistants/rules/encoding-conventions.md`
