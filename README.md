# code-skills

> 面向 AI 协作的项目管理 + 编码工作流工具集(基于 Claude Code)。

## 简介

`code-skills` 是一组 Claude Code 技能,覆盖需求分析 → 概要设计 → 详细设计 → 编码 → 单测 → 评审 → 发布的完整开发周期。

## 快速开始

1. 添加 marketplace:
   ```
   claude plugin marketplace add https://github.com/wm123450405/code-skills.git
   ```
2. 安装插件:
   ```
   claude plugin install code-skills@code-skills
   ```
3. 在项目中调用首个技能:
   ```
   /code-version V0.0.0
   /code-require "添加用户登录功能"
   ```

## 主要能力

| 技能 | 用途 |
| --- | --- |
| `code-version` | 版本工作空间管理 |
| `code-require` | 需求分析 |
| `code-design` | 概要设计 |
| `code-plan` | 详细设计 + 任务拆分 |
| `code-it` | 任务编码 |
| `code-unit` | 单元测试 |
| `code-check` | 代码评审 |
| `code-dashboard` | 开发看板 |
| `code-publish` | 发布部署 |
| `code-auto` | 自动开发(编排) |
| `code-rule` | 编码规范管理 |

## 📖 详细文档

完整技能说明、安装细节、版本管理:[./plugins/code-skills/README.md](./plugins/code-skills/README.md)

## 许可证

[MIT](LICENSE)
