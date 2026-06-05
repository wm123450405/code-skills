# 风险分析 — REQ-00013
更新时间:2026-06-05 21:30
版本:V0.0.2

## 异常处理

| 异常路径 | 描述 | 处理 | 监控 |
| --- | --- | --- | --- |
| **E-1** | 无 `.current-version` | 提示调 `code-version`,退出(同其他 12 技能)| N/A |
| **E-2** | 标题 > 30 字符 | `truncateTitle` 自动截断到 30 字 + `...`(NFR-3)| 屏幕输出验证 |
| **E-3** | 标题字段缺失(理论不可能)| 退化:屏幕输出"编号+(无标题)"(D-4 选定 B)| 屏幕输出验证 |
| **E-4** | 历史任务(REQ-00001~00003 旧格式)| 透传旧格式 + 拼接标题(同 `code-dashboard` NFR-3)| `code-it` 任务编码解析 |
| **E-5** | `code-fix` 产出无"## 缺陷标题"小节(老缺陷)| 退化:用 `BUG-NNNNN` 占位(E-5 边界)| 屏幕输出验证 |
| **E-6** | `code-review` 派生任务标题 > 30 字 | `code-review` 写入 `PLAN.md` 时即截断(D-5 选定 A)| 任务总览"标题"列 ≤ 30 字 |
| **E-7** | `code-auto` 调子技能时标题解析失败 | 退化:屏幕输出"编号+(无标题)" | 屏幕输出验证 |
| **E-8** | 用户希望"不截断"标题 | 手动编辑 `RESULT.md` 第 1 行(本需求**不**提供 CLI 参数)| N/A |
| **E-9** | 多次执行 `code-require` / `code-plan` / `code-fix` | 标题覆盖(NFR-4 幂等)| 屏幕输出验证 |
| **E-10** | `code-publish` 报告标题解析失败 | 退化:用"编号"占位,报告"REQ-NNNNN 状态=..."(无标题)| 报告验证 |
| **E-11** | `code-auto` `auto-report.md` 写入失败 | 沿用 NFR-7 强约束 — 报告仅输出在屏幕 | stderr 告警 |
| **E-12** | `truncateTitle` 对 emoji / 特殊字符的处理 | `[...title]` 数组 spread 按 Unicode code point 计数,emoji 算 1 字 | 单元测试不适用(纯文档型)|

## 安全边界

- **N/A**:本轮 0 鉴权 / 0 加密 / 0 审计 / 0 敏感字段处理(纯文档型仓库)
- ✅ 0 新增三方依赖(NFR-1 强约束)
- ✅ 0 修改 `marketplace.json` / `plugin.json`(FR-11 强约束)
- ✅ 0 修改 `assistants/rules/` 13 文件(NFR-2 强约束)

## 性能与资源

- **屏幕输出**:`truncateTitle` / 拼接为 O(30) 操作,远低于人类感知阈值(< 1 ms)
- **文件读取**:
  - `code-auto` 自读 3 个生成源产物,3 次文件 I/O < 100 ms
  - `code-publish` 复用既有 PreflightChecker 解析逻辑,新增 1 次文件 I/O < 50 ms
  - 其他 5 技能各 1 次文件 I/O < 50 ms
- **内存**:0 内存压力(纯字符串操作)
- **CPU**:0 CPU 压力(纯字符串拼接)

## 回退策略

- **触发条件**:任一任务 T-001~T-008 实施后,发现 SKILL.md 字节级保留失败 / frontmatter 改变 / 既有章节误改
- **步骤**:
  1. `git checkout HEAD -- <修改的 SKILL.md>` 恢复
  2. 检查 T-001~T-008 锚点定位是否准确
  3. 重新实施(增量追加,既有章节不动)
- **验证**:`git diff --stat` 显示 0 误改 + 既有 frontmatter 字节级保留
- **最坏情况**:8 个 SKILL.md 全部回退到 HEAD,损失 = 0(本仓库为纯文档型,无数据丢失)

## 测试要点

- **单元测试**:**不适用**(本仓库无构建/测试文件,`code-unit` 守卫判定"不可测"— REQ-00009 强约束)
- **集成测试**:**不适用**(同上)
- **端到端测试**:**不适用**(同上)
- **静态自检**(由 T-001~T-008 各任务 + T-009 收尾执行):
  - **INV-1**:7 个 SKILL.md 增量追加后,既有 frontmatter / "## 工作流程" / "步骤 N" 字节级保留
  - **INV-2**:8 个 SKILL.md 锚点统一
  - **INV-3**:6 技能 13 类屏幕输出位置含"编号+标题"
  - **INV-4**:`truncateTitle` 伪代码 3 行完整性
  - **INV-5**:0 触发 `dashboard-conventions §规则 1` 3 处同步
  - **INV-6**:0 修改 `marketplace.json` / `plugin.json` / `assistants/rules/` 13 文件
  - **INV-7**:`code-fix` "## 缺陷标题"小节不写入看板
  - **INV-8**:`code-auto` 子技能零修改契约保持
