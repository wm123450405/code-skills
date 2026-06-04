# 关联概要设计 — REQ-00005

更新时间:2026-06-04 16:00
版本:V0.0.2

## 1. 扫描范围

- **同版本**:`./assistants/V0.0.2/design/*/RESULT.md` — **空**(本需求为首个概要设计;同版本下 REQ-00004/00006/00007/00008/00009/00010/00011/00012/00013 均**未**进入 design 阶段)
- **跨版本**:
  - `./assistants/V0.0.1/design/REQ-00001/RESULT.md` — Marketplace 根名称添加 `-marketplace` 后缀
  - `./assistants/V0.0.1/design/REQ-00002/RESULT.md` — 编码格式统一
  - `./assistants/V0.0.1/design/REQ-00003/RESULT.md` — 优化 `code-rule` 技能
  - `./assistants/V0.0.0/` — 基线版本,**无 `design/` 子目录**

## 2. 关联设计清单

### 2.1 REQ-00003(V0.0.1)— 优化 `code-rule` 技能
- **关联点**:
  - **规范沉淀责任**:`code-rule` 是**唯一**写 `./assistants/rules/` 的技能
  - **本需求间接需要 `commit-conventions.md` 规则填充**(末尾 commit message 格式),但**不**在本需求中填充(NFR-6 显式留 follow-up)
  - **本需求间接需要 `plugins/code-skills/CLAUDE.md` "AI 工作约定"小节追加**(工作流变化),但**不**在本需求中追加(FR-6.AC-6.2 留 follow-up)
- **对本设计的影响**:
  - 本设计**不**触达 `code-rule` 范围
  - 本设计派生"用 `code-rule` 沉淀"为后续 follow-up(Q-9 / Q-10 / Q-11 — 见 `clarifications.md`)
- **来源**:`./assistants/V0.0.1/design/REQ-00003/RESULT.md` §1.2 / §1.3

### 2.2 REQ-00002(V0.0.1)— 编码格式统一
- **关联点**:
  - **`encoding-conventions.md` 权威源**:本需求**不**生成新 REQ/BUG/TASK 编码,**不**触发该规范
  - **commit message 模板中的 `REQ-NNNNN` 引用**:沿用 V0.0.1 实践,严格 5 位纯数字(本仓库实际 `REQ-00005`)
- **对本设计的影响**:弱;本设计所有"需求编码"引用严格遵循 `encoding-conventions.md §规则 1`
- **来源**:`./assistants/V0.0.1/design/REQ-00002/RESULT.md` §3 编码变更算法

### 2.3 REQ-00001(V0.0.1)— Marketplace 根名称添加 `-marketplace` 后缀
- **关联点**:
  - **commit 实践**:V0.0.1 建立了"每个任务显式 commit"的实践,本设计**不**取代(`code-it` 内部 commit 与本需求末尾兜底并存,Q-4 锁定 B)
  - **commit message 格式**:沿用 `chore(<scope>): <subject>`,subject 含 `REQ-NNNNN` 引用
- **对本设计的影响**:弱;本设计 §依赖管理 / §commit 模板直接沿用 V0.0.1 实践
- **来源**:`./assistants/V0.0.1/design/REQ-00001/RESULT.md` §3 Q-4 + V0.0.1 看板"执行的开发命令记录"

### 2.4 V0.0.0 基线(EXISTING-001 ~ EXISTING-010)
- **关联点**:V0.0.0 基线由 `code-init` 生成,**不**修改(`migration-mapping.md §规则 4` 强制不追溯)
- **对本设计的影响**:无;本设计不触达 V0.0.0
- **来源**:`./assistants/V0.0.0/INIT-REPORT.md`

## 3. 跨需求聚合(同版本,本设计为首个 design)

| 维度 | 涉及需求 | 共性 | 处理建议 |
| --- | --- | --- | --- |
| 同版本后续 design | REQ-00004 / 00006 / 00007 / 00008 / 00009 / 00010 / 00011 / 00012 / 00013 | 9 个需求均"已锁定需求分析",待 design 阶段 | 后续 `code-design` 阶段应**全部**先做"§0 规范摘要"时,引用本设计 §2.5.1 "规范适用清单"作为基线 |
| 末尾 commit 行为 | REQ-00005(本需求) | 末尾兜底 commit 是**新增** | 后续 design 阶段不应重复实现该行为(避免重复);`code-require` 末尾 commit 已覆盖 |
| 工作流变化 | REQ-00005 + REQ-00009(0a 守卫) + REQ-00010(0a 守卫) + REQ-00011(0b 守卫) | 4 个需求都在"步骤 0 之前"插入新步骤 | `code-plan` 阶段应确保 4 个技能的"步骤 0a" 实现一致(参考本设计 D-1 选定 A) |

## 4. 横向关联需求(来自上游)

| 关联需求 | 关联点 | 对本设计的影响 |
| --- | --- | --- |
| **REQ-00004**(V0.0.2) | 范围并列 | `code-dashboard` 纯只读,不受末尾 commit 影响(NFR-6 不修改) |
| **REQ-00003**(V0.0.1) | `commit-conventions.md` 占位 | 本需求**不**直接填充规则;末尾 commit 沿用 V0.0.1 实践格式 |
| **REQ-00002**(V0.0.1) | 编码权威源 | 末尾 commit 信息中 `REQ-NNNNN` 引用严格符合 `encoding-conventions.md` 规范 |
| **REQ-00001**(V0.0.1) | "每个任务显式 commit"实践 | 本需求**不**取代 `code-it` 内部 commit;二者并存(Q-4 锁定 B) |
| **REQ-00001-005 / REQ-00002-009**(V0.0.1 派生) | review 派生任务"留 dirty tree" | 本需求在"无变更"时跳过 commit,**不**强制 review 派生任务也走末尾提交 |

详细关联分析见 `related-requirements.md`(上游产物)。
