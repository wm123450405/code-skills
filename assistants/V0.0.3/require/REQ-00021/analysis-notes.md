# 分析笔记 — REQ-00021

## 当前理解的疑点(已解决)

1. **Q-1 二进制格式是否可写?**
   - 解决:Claude Code `Write` 工具只能写纯文本;.docx / .xlsx / .pdf 是二进制 zip,**无法**用 `Write` 写
   - 决策:本需求**仅**实现可文本化格式;二进制格式屏显 `⚠ 跳过` 不报错,留作 follow-up(需要用户提供 Python 脚本)
   - 用户已确认接受(本仓库无 Python/Node 工具链,CLAUDE.md 强约束)

2. **Q-2 命名是否纠正 DESGIN → DESIGN?**
   - 解决:用户原文拼写 "DESGIN",**不**纠正(尊重用户原文)
   - 决策:全部 SKILL.md / RESULT.md 沿用 "DESGIN"

3. **Q-3 占位符风格?**
   - 解决:采用 `{{...}}` 风格(常见于 .docx 模板 / Vue 模板 / Jinja2)
   - 决策:内置 15 个常用占位符(REQ_ID / REQ_TITLE / 需求概述 / FR_LIST / NFR_LIST / AC_LIST / 关联需求 / 待澄清 / 设计概述 / 模块列表 / 接口列表 / 数据结构 / 任务列表 / 依赖图 / 里程碑)

4. **Q-4 大需求多模板?**
   - 解决:本需求**仅**支持每技能 1 个 `--result` + 1 个 `--plan`
   - 决策:多模板场景**不**支持(留作 follow-up)

## 候选方案权衡(已锁定)

### 方案 A:二进制格式用 Write 工具写(已排除)
- 优点:用户原文期望
- 缺点:`Write` 工具只能写纯文本,无法写二进制 zip
- 决策:不采纳

### 方案 B:可文本化格式 + 屏显 `⚠ 跳过` 二进制(本需求采纳)
- 优点:技术完全可行;尊重用户原文意图
- 缺点:二进制格式本需求**不**实现,留作 follow-up
- 决策:采纳(用户已确认)

### 方案 C:引入 Python 依赖(已排除)
- 优点:可写 .docx / .xlsx
- 缺点:本仓库 CLAUDE.md 强约束"不假设任何工具链",新增依赖违反 `dependency-conventions`
- 决策:不采纳

## 临时假设(已采纳)
- 用户传入的模板**主版本**是可文本化格式(.md / .html / .txt / .json / .xml / .csv / .yaml)
- 用户传入的 .docx / .xlsx / .pdf 模板**会被屏显 `⚠ 跳过`**,不报错
- 模板占位符约定为 `{{...}}` 风格(后续可由 `code-rule` 沉淀为正式规范)
- 模板文件大小限制 1MB(过大屏显 `⚠` 但继续)
- 模板路径不允许 `../` 跳出工作空间(安全约束)

## 下一轮要深挖的方向
- **follow-up-1**:用户提供 Python 脚本(`fill_docx.py` / `fill_xlsx.py` / `fill_pdf.py`),技能调 `Bash: python fill_<format>.py <模板> <输出> <数据 json>`,实现真正的二进制格式填充
- **follow-up-2**:大需求多模板场景(`--result` 可传多次,或新增 `--template-list` 参数)
- **follow-up-3**:`code-rule` 沉淀"占位符约定"规范(把内置 15 个占位符升级为项目级规范)
- **follow-up-4**:`code-auto` 升级:支持 `code-auto` 自动套模板(当前 E-4 锁定不传)
