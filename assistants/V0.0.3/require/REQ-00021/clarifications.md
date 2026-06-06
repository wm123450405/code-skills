# 澄清记录 — REQ-00021

## 2026-06-06 16:50
- **问题**:用户提供的模板 .docx 文件实际是哪种?Claude Code 的 Write 工具只能写纯文本(无法写二进制 .docx zip),需要先确定模板格式。
- **用户回答**:docx只是例子,可能是其他格式文件如 xlsx、pdf 等,按照实际用户给定的模板格式输出,如用户提供的是.docx文件,则输出格式也为.docx文件,按实际二进制(对应数据格式)内容填充
- **影响**:FR-2 / FR-3 — 本需求**仅**实现可文本化格式(.md / .html / .txt / .json / .xml / .csv / .yaml);二进制格式(.docx / .xlsx / .pdf / .pptx)屏显 `⚠ 跳过`,**留作 follow-up**(需要用户提供 Python 脚本,本仓库无 Python/Node 工具链)

## 2026-06-06 16:52
- **问题**:3 技能在传 --result / --plan 时,生成的文件名应如何命名?
- **用户回答**:后缀名和用户提供的文件名保持一直,最终文件名按照 REQUIRE、DESGIN(详设、概设都是)、PLAN 命名
- **影响**:FR-1 表格 + FR-2 写出规则 — `code-require` → `REQUIRE.<ext>`,`code-design` → `DESGIN.<ext>`,`code-plan --result` → `DESGIN.<ext>`(详设),`code-plan --plan` → `PLAN.<ext>`

## 2026-06-06 17:00
- **问题**:DESGIN 拼写(用户原文)是否纠正为 DESIGN?
- **用户回答**:不纠正,沿用用户原文拼写 "DESGIN"
- **影响**:RESULT.md / SKILL.md 全部沿用 "DESGIN" 拼写(不"自动修正")

## 2026-06-06 17:05
- **问题**:二进制格式(.docx / .xlsx / .pdf)本需求**不**实现(因本仓库无 Python/Node 工具链),是否同意留作 follow-up?
- **用户回答**:同意(本需求范围只实现可文本化格式;二进制格式屏显 `⚠ 跳过` 不报错)
- **影响**:FR-3 锁定为本需求**不**实现,留作 follow-up
