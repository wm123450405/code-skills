# TASK-REQ-00045-00001 — 创建 6 个语言适配文件

- 任务编号:TASK-REQ-00045-00001
- 所属需求:REQ-00045
- 所属版本:V0.0.5
- 类型:新增
- 状态:已完成
- 创建:2026-06-30 19:47
- 完成:2026-06-30 19:50

## 1. 任务概述

在 `code-req/references/languages/` 下创建 6 个语言适配文件,为 CODING 和 CHECK 阶段提供语言感知的构建/测试/运行命令检测、编码约定、工具链检测能力。

## 2. 改动内容

### 文件变更
| 变更类型 | 文件路径 | 说明 |
| --- | --- | --- |
| 新增 | `references/languages/go.md` | Go 项目语言适配(38 行) |
| 新增 | `references/languages/python.md` | Python 项目语言适配(71 行) |
| 新增 | `references/languages/nodejs.md` | Node.js/TypeScript 项目语言适配(78 行) |
| 新增 | `references/languages/rust.md` | Rust 项目语言适配(33 行) |
| 新增 | `references/languages/java-gradle.md` | Java(Gradle)项目语言适配(30 行) |
| 新增 | `references/languages/java-maven.md` | Java(Maven)项目语言适配(33 行) |

### 详细改动
每个文件包含 7 个统一章节:
- §1 项目结构识别(描述文件/目录约定/包管理器)
- §2 构建命令检测
- §3 测试框架识别
- §4 启动/运行命令检测
- §5 Monorepo 声明文件解析
- §6 编码约定(命名规范/错误处理风格)
- §7 工具链检测(代码行数统计/Lint/格式化)

内容从旧 `code-it/references/` 中恢复,文件头注释更新为 `code-req`。

## 3. 关键决策

- 文件结构统一为 7 章节,与旧技能保持一致
- Go 和 Rust 文件较精简(语言生态简单),Python/Node.js 文件较详细(生态复杂)
- Gradle 引用 Maven 的编码约定(Java 语言层面一致)

## 4. 验证结果

| 验证类型 | 命令/方式 | 结果 |
| --- | --- | --- |
| 编译 | 不适用(文档) | 不适用 |
| 运行 | 不适用(文档) | 不适用 |
| 测试 | 不适用(文档) | 不适用 |

## 5. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-06-30 19:50 | v1 | 初始完成 | 任务完成,6 个语言适配文件创建 | wangmiao |