# 接口详细规格 — REQ-00041

## 接口 1: SKILL.md → references 引用标记

- **形式**:Markdown 块引用指令
- **签名**:`> 详见 references/<文件>.md §<章节>`
- **入参**:`<文件>` = common / nodejs / python / rust / go / java-maven / java-gradle
- **入参**:`<章节>` = §1-§15(common.md) 或 §1-§7(语言文档)
- **示例**:
  - `> 详见 references/common.md §3`
  - `> 详见 references/nodejs.md §1`
  - `> 详见 references/nodejs.md §1, references/python.md §1`(多语言)

## 接口 2: 语言标签传递

- **形式**:design/RESULT.md 模块表"语言"列
- **写入方**:code-design 步骤 5
- **读取方**:code-plan / code-it / code-check
- **值域**:`nodejs` / `python` / `rust` / `go` / `java-maven` / `java-gradle` / `unknown`
- **示例**:
  ```
  | 模块名 | 路径 | 状态 | 职责 | 依赖 | 语言 |
  | --- | --- | --- | --- | --- | --- |
  | auth | src/auth/ | 修改既有 | 认证模块 | — | nodejs |
  ```

## 接口 3: 语言检测函数

- **形式**:伪代码算法(内嵌在 code-design/references/common.md §5)
- **签名**:`detectLanguage(moduleDir: string): string`
- **入参**:模块根目录路径
- **出参**:语言标签字符串
- **算法**:按优先级 Glob 描述文件 → 匹配 → 返回标签;无匹配 → "unknown"

## 接口 4: references 文档章节结构

- **形式**:Markdown 标题层级
- **common.md**:`## §1` ~ `## §15`(15 个二级标题)
- **<语言>.md**:`## §1` ~ `## §7`(7 个二级标题)
- **约束**:章节编号和标题字面在 4 个技能间保持一致