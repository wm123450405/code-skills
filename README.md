# code-skills

> 面向 AI 协作的软件开发生命周期管理工具集(基于 Claude Code)。

## 简介

`code-skills` 是一组 Claude Code 技能,覆盖从需求分析到代码审查的完整开发周期,内置版本感知工作空间管理。

## 快速开始

1. 添加 marketplace:
   ```
   claude plugin marketplace add https://github.com/wm123450405/code-skills.git
   ```
2. 安装插件:
   ```
   claude plugin install code-skills@code-skills-marketplace
   ```
3. 在项目中调用技能:
   ```
   /code-ver              ← 初始化项目,创建版本(或查看进度)
   /code-req "你的需求"    ← 开始需求开发
   /code-fix "缺陷描述"    ← 修复缺陷
   ```

## 技能概览

| 技能 | 用途 |
| --- | --- |
| `code-ver` | 版本管理与开发看板 — 初始化项目、切换版本、发布、查看进度 |
| `code-req` | 需求开发 — 从需求分析到代码审查的全流程 |
| `code-fix` | 缺陷修复 — 从缺陷登记到修复审查的全流程 |
| `code-faq` | 知识查询 — 跨版本查询需求和缺陷,支持导出 |
| `code-rule` | 编码规范 — 用自然语言描述规范,自动整理为条款 |
| `code-merge` | 分支合并 — 将 worktree 改动合回主干 |

## 📖 详细文档

完整技能说明、安装细节、使用指南:[./plugins/code-skills/README.md](./plugins/code-skills/README.md)

## 许可证

[MIT](LICENSE)