# 澄清记录 — REQ-00001
更新时间:2026-06-03 20:25
版本:V0.0.1

## 第 1 轮:本设计阶段(2026-06-03 20:25)

### 处理策略

REQU 文档(REQ-00001/RESULT.md §12)中列出 3 项待澄清 Q-3 / Q-4 / Q-5,均**非阻塞**且 REQU 文档已给出明确默认值。本次设计阶段不主动向用户追问,采用 REQU 文档默认假设推进,并在此文件中显式记录默认值与回退路径。如用户在 `code-plan` 阶段前改变主意,可触发 v2 增量更新。

---

### Q-3:`.claude-plugin/marketplace.json` 的 `description` 字段是否同步更新?

- **REQU 文档原始选项**:
  - A. 改 description(新增说明如 "marketplace container")
  - B. 不改(沿用现状)
- **REQU 文档默认**:B(基于 Q-2 选项 A"仅根 name"隐含)
- **本设计采用**:**B(不改)**
- **理由**:
  1. 范围最小化(NFR-5)
  2. `marketplace-protocol.md §规则 1.6` 不允许引入未知字段;description 虽已存在,改其内容需说明必要性
  3. 当前 description 已能表达"工具集合 + 版本感知工作空间",与改名无关
- **影响章节**:本设计 FR-1 / AC-1 / 关键不变量(`description` 保持原值)
- **回退路径**:若用户在 `code-plan` 前回答"改 description",需新增 FR-8 + AC-10

---

### Q-4:README.md / README.en.md 是否追加"老用户迁移指引"小节?

- **REQU 文档原始选项**:
  - A. 不加(在 commit message 中提及 breaking change)
  - B. 加(新增一节,中英同步)
- **REQU 文档默认**:A
- **本设计采用**:**A(不加)**
- **理由**:
  1. 范围最小化(NFR-5)
  2. 避免触发 `doc-conventions.md §规则 1` 同步负担(若加,中英都加)
  3. NFR-1 兼容性段落(`§7 交互逻辑`)已详细列出老用户的 5 步操作流程;若需要,可在后续版本中追加独立小节(走 `code-require` 全流程)
- **影响章节**:本设计 FR-3 / FR-4 不含"新增章节";NFR-1 兼容性提示**不在 README 体现**
- **回退路径**:若用户在 `code-plan` 前回答"加迁移指引",需新增 FR-8 + AC-10,且 `doc-conventions.md §规则 1` 同步触发

---

### Q-5:`marketplace.json` 的 `version` 是否从 `1.0.0` 升到 `1.1.0`?

- **REQU 文档原始选项**:
  - A. 保持 1.0.0
  - B. 升 1.1.0(以 semver 标识 breaking change)
- **REQU 文档默认**:A
- **本设计采用**:**A(保持 1.0.0)**
- **理由**:
  1. 范围最小化(NFR-5)
  2. `marketplace-protocol.md §规则 1.3` 要求 `plugins[].version` 与子插件 plugin.json 同步;本仓库 plugin.json 也是 1.0.0,升 marketplace 而不升 plugin 会引入新的不同步
  3. breaking change 可在 commit message 中显式标注,无需 `version` 字段强制
- **影响章节**:本设计 FR-1 / AC-1 / 关键不变量(`version` 保持 `1.0.0`)
- **回退路径**:若用户在 `code-plan` 前回答"升 1.1.0",需:
  - marketplace.json 根 `version` 改 `1.1.0`
  - 评估 plugins[].version 是否同步升(Q-5 选项 B 的次生问题:marketplace 与 plugin 同步)
  - 本设计采用"都升 1.1.0"作为联动默认(plugin 也升,与 marketplace 同步)

---

## 第 2 轮:实施阶段可能的新澄清(预占位)

> 本节为预占位,实际填写在 `code-plan` / `code-it` 阶段。如用户在实施前改主意回答 Q-3/Q-4/Q-5,在此追加。

(暂无)
