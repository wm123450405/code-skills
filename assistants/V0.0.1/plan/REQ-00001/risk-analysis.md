# 风险分析 — REQ-00001(code-plan 阶段)
更新时间:2026-06-03 20:30
版本:V0.0.1

## 异常处理

| 异常路径 | 描述 | 处理策略 | 监控指标 |
| --- | --- | --- | --- |
| E-1:marketplace.json 误改 plugins[].name | Edit 工具定位错误,把 `plugins[0].name` 误改 | Edit 前 Read 全文,确认 old_string 唯一指向根 name 行;code-review diff 审阅 | `grep "name" .claude-plugin/marketplace.json` 应仅 1 行变更 |
| E-2:marketplace.json 误删 $schema | Edit 时误删 `$schema` 行 | 同上,Edit 锁定仅改 name 行 | `grep "$schema"` 文件应仍命中 |
| E-3:README 中英不一致 | 中英两个 README 替换次数不一致 | code-review 并列 diff 对照;`code-it` 工作日志记录每次替换 | 两个文件 grep 命中数应一致 |
| E-4:working tree 不干净 | `code-it` 实施前已有未提交修改 | `git status` 检查,如有未提交修改则先 stash 或 commit | git status 输出 |
| E-5:用户已部分手改 | Grep 命中数与设计预期不符 | 偏差日志记录,继续完成 marketplace.json 改动(产品目标不变) | 偏差日志 |
| E-6:CLAUDE.md 命中 marketplace name 引用 | Grep 命中超出预期 | 按 FR-5 同步;`code-it` 工作日志记录 | Grep 命中数 |
| E-7:rename 影响老用户 | 已 marketplace add 旧 name 的用户无法自动迁移 | 在 commit message 显式标注 breaking change;NFR-1 兼容性已在 REQU 文档 §7 说明 | commit message |
| E-8:JSON 语法错误 | Edit 后 JSON 不合法 | Claude Code 加载时自动校验(若失败会报错);Edit 后 Read 全文确认 | 文件可被 Read 解析 |

## 安全边界

- **鉴权要求**:N/A(本仓库无应用代码)
- **输入校验**:N/A
- **敏感数据处理**:N/A
- **审计日志**:commit message + V0.0.1/RESULT.md 变更记录
- **依据规范**:无直接对应(N/A 本仓库类型)

## 性能与资源

- **关键路径预估**:N/A(纯字符串替换,无性能瓶颈)
- **资源限制**:N/A
- **缓存策略**:本需求不涉及

## 回退策略

- **触发条件**:实施后 code-review 发现不变量被破坏
- **步骤**:
  1. `git revert <commit-hash>` —— 1 个 commit 全部回退
  2. 验证:`git grep "code-skills-marketplace"` → 应为 0
  3. 重新走 `code-it` 流程
- **验证**:回退后 `git log --oneline -5` 确认

## 测试要点

> 本需求**纯文档/字符串层变更**,无应用代码,无单元测试。`code-unit` 阶段对本需求所有任务标记为 `不适用`。

- **单元测试范围**:N/A
- **集成测试范围**:N/A
- **端到端测试范围**:手动验证(README 中 install 命令可在测试环境跑通)
- **性能/安全测试**:N/A

### 替代验证手段(覆盖原"测试要点"角色)

| 验证项 | 方法 | 工具 |
| --- | --- | --- |
| marketplace.json 字段逐项 | `grep "name"` / `grep "$schema"` / `grep "version"` | Grep |
| README 旧字面量 0 残留 | `grep "code-skills@code-skills"` | Grep |
| CLAUDE.md 核查 | `grep "code-skills@code-skills"` / `grep "marketplace name"` | Grep |
| 全仓库 0 残留 | grep 全仓库 | Grep |
| 中英 README 同步 | 并列 diff | git diff / Read 对照 |
| 整体变更范围 | `git diff --stat` | Bash git |
| 不变量保持 | 11 条不变量逐条 grep / ls / `git remote -v` | Grep / Bash |
