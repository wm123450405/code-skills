# 材料登记 — REQ-00025
更新时间:2026-06-07
版本:V0.0.3

## 项目级规范
13 份规范自检(详 `design/REQ-00025/RESULT.md §12`),1 强约束触发修订(`encoding-conventions.md`),其他 12 份 0 触发

## 上游需求
- 来源:./assistants/V0.0.3/require/REQ-00025/RESULT.md
- 版本:v1(2026-06-07)
- 提取:8 FR / 7 NFR / 8 AC / 4 Q

## 项目现状(本次扫描)

### 项目类型
- 纯文档项目(Markdown)
- 关键依赖:无运行时

### 已有模块
- 8 个 `code-*` 技能 SKILL.md(本需求**修改**)
- 5 个 `code-*` 技能(本需求**不修改**)
- `encoding-conventions.md` 1 个规范(本需求**直接修订**)

### 编码与构建约定
- 沿用既有:SKILL.md 修订锚点(`## 工具使用约定` 段后 + `## 工作流程` 段前)
- frontmatter 字节级保留

## 本次变更源
- 需求侧:`require/REQ-00025/RESULT.md` 新建 v1
- 规范侧:`encoding-conventions.md` §规则 1.5(新增)
- 代码侧:8 个 SKILL.md 字面更新

## 命令行参数
- `--result`:无

## 模板填充结果
- 无(无参数)
