# 改修总结 — TASK-REQ-00044-00009 · 更新 plugin.json + marketplace.json

## 1. 任务概述
- 所属需求:REQ-00044
- 任务类型:修改
- 涉及文件:2 个修改文件

## 2. 改动内容

| 文件 | 说明 |
| --- | --- |
| `plugins/code-skills/.claude-plugin/plugin.json` | 更新 keywords(旧技能名→新技能名);新增 `skills` 字段,列出 7 个 v2 技能 |
| `.claude-plugin/marketplace.json` | 更新 keywords(旧技能名→新技能名);更新 `plugins[].skills` 列表为 7 个 v2 技能 |

### plugin.json 变更详情

| 变更项 | 旧值 | 新值 |
| --- | --- | --- |
| keywords | code-require, code-design, code-plan, code-it, code-check, code-fix, code-version, code-init, code-rule | code-ver, code-req, code-fix, code-faq, code-rule, code-merge, code-dashboard |
| skills | (不存在) | 新增 7 个技能路径 |

### marketplace.json 变更详情

| 变更项 | 旧值 | 新值 |
| --- | --- | --- |
| keywords | code-require, code-design, code-plan, code-it, code-check, code-fix, code-version, code-init, code-rule | code-ver, code-req, code-fix, code-faq, code-rule, code-merge, code-dashboard |
| plugins[].skills | 11 个旧技能路径 | 7 个新技能路径 |

### 7 个 v2 技能映射

| 新技能 | 旧技能 | 说明 |
| --- | --- | --- |
| code-ver | code-version + code-publish + code-init | 版本管理(合并 3 技能) |
| code-req | code-require + code-design + code-plan + code-it + code-check | 需求开发全流程(合并 5 技能) |
| code-fix | code-fix(重构) | 缺陷修复全流程 |
| code-faq | code-answer | 知识查询与导出 |
| code-rule | code-rule(适配) | 编码规范管理 |
| code-merge | code-merge(适配) | Worktree 自动合并 |
| code-dashboard | code-dashboard(适配) | 开发看板 |

> 注: code-auto 不再出现在 v2 技能列表中,其编排能力已内化到 code-req 的 `--auto` 参数中。

## 3. 关键决策

- **plugin.json 新增 `skills` 字段**:旧版 plugin.json 无此字段,本次新增以遵循 Claude Code 插件协议规范,使插件注册的技能可被自动发现
- **code-auto 退场**:v2 中 code-auto 的自动编排能力已内化到 code-req 的 `--auto` 参数中,不再作为独立技能
- **keywords 同步**:两文件 keywords 保持完全一致,均列出 7 个新技能名

## 4. 验证结果

- 编译:不适用(纯 JSON 配置)
- 运行:不适用
- 测试:不适用

## 5. 变更记录

| 时间 | 版本 | 变更类型 | 变更摘要 | 变更人 |
| --- | --- | --- | --- | --- |
| 2026-06-30 18:30 | v1 | 初始创建 | plugin.json + marketplace.json 更新为 v2 7 技能结构 | wangmiao |