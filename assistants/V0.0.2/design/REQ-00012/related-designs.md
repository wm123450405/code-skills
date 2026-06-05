# 关联设计 — REQ-00012
更新时间:2026-06-05
版本:V0.0.2

## 同版本(V0.0.2)其他 design
- REQ-00001 ~ REQ-00011 共 8 个 design(已存在)
- **本需求与上述 design 0 交集**:本需求落地后**不**触发任何 8 个已落地需求的修改(FR-5 AC-5.5 + NFR-5 强制)

## 跨版本关联
| 关联需求 | 关联点 | 对本需求的影响 | 来源 |
| --- | --- | --- | --- |
| REQ-00001(V0.0.1) | `plugins/code-skills/README.md` 是 V0.0.1 主语言版本 | 本需求落地后:**仓库根 README 成为新主语言版本**(门面级) | `./assistants/V0.0.1/require/REQ-00001/RESULT.md` |
| REQ-00003(V0.0.1) | `code-rule` 维护 `doc-conventions.md` | FR-6 强制遵循 §规则 1 / §规则 2;本需求**不**触发规则修订 | `./assistants/rules/doc-conventions.md` |
| REQ-00002(V0.0.1) | `encoding-conventions.md` | 不影响(本需求不涉及编码) | `./assistants/V0.0.1/require/REQ-00002/RESULT.md` |
