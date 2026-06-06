# 三方依赖评估 — REQ-00021

更新时间:2026-06-06 17:30
版本:V0.0.3

## 1. 结论

**本需求 0 新增三方依赖**。

## 2. 评估明细

### 2.1 可文本化格式填充(本需求实现)

- 工具链:Claude Code `Read` + `Write` 工具(内置)
- 第三方库:**无**(字符串替换是 Python/JS 内置 `String.prototype.replace`,但本技能**不**写代码,只在 SKILL.md 中描述)
- 评估结果:**0 新增依赖** ✅

### 2.2 二进制格式填充(本需求**不**实现,留作 follow-up)

- 工具链:需引入外部脚本(Python `python-docx` / Node `docx` / Java `Apache POI` 等)
- 第三方库候选:
  - Python:`python-docx`(写 .docx)、`openpyxl`(写 .xlsx)、`reportlab`(写 .pdf)
  - Node:`docx`(写 .docx)、`exceljs`(写 .xlsx)
  - Java:`Apache POI`(写 .docx/.xlsx)
- 评估结果:**0 新增依赖**(本需求范围外,留作 follow-up)

## 3. 拒绝引入的依赖及理由

| 候选依赖 | 用途 | 否决理由 |
| --- | --- | --- |
| `python-docx` | 写 .docx | 1. 本仓库 CLAUDE.md 强约束"不假设任何工具链",引入 Python 违反 `dependency-conventions.md`;2. `Bash: python` 不在 4 个核心工具范围内;3. 引入需 `package.json` 或 `requirements.txt`,违反"0 新增包管理配置";4. **本需求**用户已确认二进制格式**留作 follow-up** |
| `openpyxl` | 写 .xlsx | 同上 |
| `docx` (Node) | 写 .docx | 1. 同 1-3;2. 本仓库无 Node 工具链 |
| `exceljs` (Node) | 写 .xlsx | 同上 |
| `Apache POI` (Java) | 写 .docx/.xlsx | 1. 同 1-3;2. 本仓库无 Java 工具链 |

## 4. 复用既有依赖(本需求 0)

- 本需求**0**新增 / 修改既有三方依赖
- 沿用既有:Claude Code `Read` / `Write` / `Grep` / `Glob` 工具
- 沿用既有:`git`(Bash 工具,用于步骤 0a 拉取)

## 5. 规范遵循

### 5.1 对照 `dependency-conventions.md`(本需求 `规则 1` 待添加,本概设引用既有)

- ✅ **0** 新增依赖(NFR-2.8 + FR-2.AC-2.8 强约束)
- ✅ 二进制格式填充**留作 follow-up**(NFR-2.8 沿用)
- ✅ 0 改 `package.json` / `requirements.txt` / 任何包管理配置

### 5.2 对照 `CLAUDE.md` 强约束

- ✅ "本仓库不包含任何源代码、构建系统、测试框架、Lint 工具或包管理配置"
- ✅ "不要假设存在任何工具链"

## 6. 下一轮(本概设不实现,留作 follow-up)

- **follow-up-1**:用户提供 Python 脚本(`fill_docx.py` / `fill_xlsx.py` / `fill_pdf.py`),技能调 `Bash: python fill_<format>.py <模板> <输出> <数据 json>`,实现真正的二进制格式填充
- 用户提供脚本时,需在 `assistants/rules/` 沉淀"二进制格式填充"规范(本概设**不**主动写)
