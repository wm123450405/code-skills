# 模块详细化 — REQ-00012
更新时间:2026-06-05
版本:V0.0.2

## 模块 1:仓库根 README(中文)— T-001

- **路径**:`./README.md`(新建)
- **关键元素**:
  - 标题:`# code-skills`
  - 副标题:`> 面向 AI 协作的项目管理 + 编码工作流工具集(基于 Claude Code)`
  - 二级标题 5 个:`## 简介` / `## 快速开始` / `## 主要能力` / `## 📖 详细文档` / `## 许可证`
  - 11 技能表格(技能名 + 用途)
  - 链接:`./plugins/code-skills/README.md`
- **调用顺序**:N/A(纯文档)
- **状态归属**:N/A
- **与概要设计对应**:§3 模块拆分(根 README 中文)
- **符合的规范**:`doc-conventions §规则 1 / §规则 2`

## 模块 2:仓库根 README(英文)— T-002

- **路径**:`./README.en.md`(新建)
- **关键元素**:
  - 标题:`# code-skills`
  - 副标题:`> A suite of Claude Code skills for AI-assisted project management and development workflow.`
  - 二级标题 5 个:`## Introduction` / `## Quick Start` / `## Main Capabilities` / `## 📖 Detailed Documentation` / `## License`
  - 11 技能表格(技能名 + 用途,行顺序与中文版一致)
  - 链接:`./plugins/code-skills/README.md`
- **调用顺序**:N/A(纯文档)
- **状态归属**:N/A
- **与概要设计对应**:§3 模块拆分(根 README 英文)
- **符合的规范**:`doc-conventions §规则 1`

## 模块 3:`CLAUDE.md` 移动 — T-003

- **路径**:`./CLAUDE.md`(从 `plugins/code-skills/CLAUDE.md` 移动)
- **关键元素**:
  - 文件类型:Markdown
  - 大小:9,418 bytes(原文件大小)
  - 操作:`git mv plugins/code-skills/CLAUDE.md CLAUDE.md`
- **调用顺序**:N/A(单步操作)
- **状态归属**:N/A
- **与概要设计对应**:§3 模块拆分(移动模块 1 个)
- **符合的规范**:NFR-3(git mv)+ NFR-8(不提供重定向)
