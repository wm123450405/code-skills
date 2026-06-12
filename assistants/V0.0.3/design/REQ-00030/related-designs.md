# 关联设计 — REQ-00030

更新时间:2026-06-12 14:25
版本:V0.0.3

## 1. 同版本设计(本节只列关联点,详细依赖展开由 code-plan 处理)

| 关联设计编码 | 关联点 | 对本设计的影响 | 链接 |
| --- | --- | --- | --- |
| REQ-00020 | 步骤 0b"按维度问路"+ "职责分离"声明 | **沿用**职责分离思路;本需求 FR-1 / FR-2 收紧为"小需求 0 问" | [RESULT](../REQ-00020/RESULT.md) |
| REQ-00014 | 架构骨架作为首个任务(条件性) | **沿用**3 条件;本需求 FR-6 追加 2 条件 | 历史中 `code-plan/SKILL.md` 步骤 10A |
| REQ-00017 | 一个任务 = 一个"实际产出" | **沿用**;本需求**不**改"任务 = 实际产出"约束 | 历史中 `code-plan/SKILL.md` 步骤 10A |
| REQ-00025 | 任务编号接收端放宽 | **沿用**;本需求**不**改任务编号体系 | 历史中 `code-plan/SKILL.md` 步骤 10A |
| REQ-00021 | `--result` / `--plan` 模板参数 | **沿用**;本需求**不**改模板参数 | [RESULT](../REQ-00021/RESULT.md) |
| REQ-00023 | code-dashboard 屏显契约(本仓库"小需求"代表) | **实证**本需求痛点(design 425 行 vs plan 334 行) | [RESULT](../REQ-00023/RESULT.md) |
| REQ-00028 | 新增 code-answer 技能(本仓库"小需求"代表) | **实证**本需求痛点(design 142 行含"禁用工具列表"等过细内容) | [RESULT](../REQ-00028/RESULT.md) |
| REQ-00029 | 优化 code-dashboard 渲染层(本仓库"小需求"代表) | **实证**本需求痛点(design 177 行 vs plan 298 行反向更厚) | [RESULT](../REQ-00029/RESULT.md) |

## 2. 跨版本设计(可选,本节为完整性列出)

- **V0.0.0 / V0.0.1 / V0.0.2**:既有 `code-design` / `code-plan` / `code-check` 技能的设计基线,本需求**不**追溯修订;新需求应用本规则后,新 design 应明显瘦身(对照 G-1 / NFR-1)

## 3. 关联规范的"已锁定"基线

- **`skill-conventions.md §规则 1`**:frontmatter L1-3 字节级保留(INV-1,本需求**不**触发)
- **`module-conventions.md §规则 1`**(DEPRECATED,沿用历史):资源文件放 `templates/` 子目录(本需求 5 个被改文件均满足)
- **`doc-conventions.md §规则 1`**:README 多语言对仗(本需求**不**改 README,故**不**触发)
- **`dashboard-conventions.md §规则 1`**:看板字段三方同步(本需求**不**新增字段 / 枚举 / 区段,故**不**触发)
- **`commit-conventions.md`**:提交前缀 `chore(<skill>):`(本需求落地时沿用)

## 4. 本设计的"0 改"边界

- ✅ 0 改:`./assistants/rules/*.md`(7 个项目级规范)
- ✅ 0 改:其他 11 个 `code-*` 技能 SKILL.md
- ✅ 0 改:`marketplace.json` / `plugin.json` / `CLAUDE.md`
- ✅ 0 改:`README.md` / `README.en.md`
- ✅ 0 改:`code-design/{materials-index,design-notes,module-breakdown,dependencies,related-designs,rule-compliance,clarifications}.md` 既有过程文档模板
- ✅ 0 改:既有 9 个 REQ(REQ-00021 ~ REQ-00029)的 design / plan
