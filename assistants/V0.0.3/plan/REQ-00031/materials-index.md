# 材料登记 — REQ-00031

更新时间:2026-06-12 15:32
版本:V0.0.3

## 项目级规范

| 规范文件 | 类别 | 关键约束摘要 |
| --- | --- | --- |
| skill-conventions.md | 技能 | SKILL.md frontmatter L1-3 字节级保留 |
| module-conventions.md | 模块 | 资源文件放 templates/ 子目录(DEPRECATED) |
| doc-conventions.md | 文档 | README 多语言对仗 |
| dashboard-conventions.md | 看板 | 看板字段三方同步 |
| commit-conventions.md | 提交 | `chore(<skill>):` 前缀 |
| encoding-conventions.md | 编码 | 5 位纯数字生成端 + 字符集放宽接收端 |
| naming-conventions.md | 命名 | 沿用 kebab-case(目录) / 中英混排(标题) |

## 上游需求

- 来源:./assistants/V0.0.3/require/REQ-00031/RESULT.md
- 版本:v1(2026-06-12 15:13)
- 提取的 FR / NFR / AC 数量:**7 FR / 5 NFR / 3 大类共 20 AC / 5 Q(全部已澄清)**
- 关键交叉点(每条 FR 对应的详设章节):
  - FR-1 任务粒度内化 → §3.1 锚点 2
  - FR-2 任务类型移除 → §3.1 锚点 3
  - FR-3 任务"测试状态"收窄 → §3.1 锚点 4-5
  - FR-4 code-it 声明 → §3.2
  - FR-5 code-unit 声明 → §3.3
  - FR-6 code-auto 步骤 4.b → §3.4
  - FR-7 templates 同步 → §3.5

## 上游概要设计

- 来源:./assistants/V0.0.3/design/REQ-00031/RESULT.md
- 版本:v1(2026-06-12 15:25)
- 提取的模块拆分 / 接口概要 / 数据结构 / 决策:
  - 模块拆分(5 模块,5 列):code-plan / code-it / code-unit / code-auto / templates-plan
  - 接口概要(4 项):`code-plan §步骤 10A` / `code-it ## 目标` / `code-unit ## 目标` / `code-auto §步骤 4`
  - 数据结构(4 项):`PLAN.md 任务总览.任务类型` / `.测试状态` / `code-it ## 目标` 文档头 / `code-unit ## 目标` 文档头
  - 决策:D-1 ~ D-5(任务"测试状态"枚举收窄 / code-it 声明 / code-unit 声明 / code-auto 步骤 4.b 改写 / templates 同步)

## 项目现状(实现细节)

### 命名风格
- 目录:kebab-case(`code-plan` / `code-it` / `code-unit` / `code-auto`)
- 文件:中英混排(标题用中文,代码用英文)
- 锚点定位:以"### 子标题"或"**子段名**"开头

### 错误模型
- 异常处理字节级保留(INV-3)
- 既有"步骤 12 错误修复循环"(code-it)沿用
- 既有"步骤 5 子技能失败处理"(code-auto)沿用

### 既有相似功能实现风格
- 既有"code-it 步骤 9-12 编译/启动/测试验证" → 本需求"内化编译/运行"逻辑沿用
- 既有"code-auto 步骤 4.b 按需调用 code-unit" → 本需求改为"恒等跳过"逻辑

### 既有测试用例风格
- 本仓库**无**测试框架;**不**适用
- 本需求主动外移单元测试职责

### 可复用工具函数
- (本需求是文字修订,无算法逻辑,**不**涉及可复用函数)

## 命令行参数

- (本需求无 `--result` / `--plan` 参数,`code-auto` 上下文)

## 本次变更源(增量更新时)

| 变更源 | 检测方式 | 变化列表 |
| --- | --- | --- |
| 需求侧 | 上游 RESULT.md 变更记录 | (无 — 首次设计) |
| 概要设计侧 | 上游 RESULT.md 变更记录 | (无 — 首次设计) |
| 规范侧 | ./assistants/rules/ 对比 | (无 — 首次设计) |
| 代码侧 | 重跑项目探索 | (无 — 首次设计) |
