# 材料登记 — REQ-00025
更新时间:2026-06-08
版本:V0.0.3

## 项目级规范

| 规范文件 | 类别 | 关键约束摘要 |
| --- | --- | --- |
| encoding-conventions.md | 编码 | §规则 1/2/4 软化 + 新增 §规则 1.5(本需求**直接修订**) |
| skill-conventions.md | 技能 | §规则 1:SKILL.md frontmatter 字节级保留(INV 严守) |
| dashboard-conventions.md | 看板 | §规则 1:看板字段扩展需 3 文件同步(本需求 0 触发) |
| doc-conventions.md | 文档 | §规则 1-2:本需求不涉及 README |
| commit-conventions.md | 提交 | 沿用 `chore(code-xxx):` 格式(本需求末尾提交用此格式) |
| 其余 8 份 | 占位 | 0 触发(module-conventions.md DEPRECATED;dependency-conventions.md 占位;framework-conventions.md 占位;naming-conventions.md 占位;migration-mapping.md 占位;marketplace-protocol.md 占位;coding-style.md 占位;directory-conventions.md 占位) |

## 上游需求

- 来源:`./assistants/V0.0.3/require/REQ-00025/RESULT.md` (v1, 已锁定)
- 提取的 FR:8(FR-1 解析端正则放宽 / FR-2 encoding-conventions 软化 / FR-3 解析两段式 / FR-4 屏显契约保留 / FR-5 INV 兼容 / FR-6 第三方前缀登记 / FR-7 旧新互操作 / FR-8 8 SKILL.md 字面更新)
- 提取的 NFR:7(性能 / 可用性 / 安全 / 可观测性 / 兼容性 / 国际化 / 可维护性 / 零外溢)
- 提取的 AC:8(AC-1~AC-8;既有 5 位兼容 / Jira 风格 / 非法前缀拒绝 / 非法后缀拒绝 / INV 兼容 / encoding-conventions 软化 / 8 SKILL.md 字面更新 / 屏显契约)

## 上游概要设计

- 来源:`./assistants/V0.0.3/design/REQ-00025/RESULT.md` (v1, 已锁定;2026-06-08 增量更新确认 no-op)
- 提取的模块拆分:9 文件改动(1 规范 + 8 SKILL.md)
- 提取的决策:D-1 生成 vs 接收分离 / D-2 后缀字符集 `A-Za-z0-9.\-_` / D-3 第三方平台前缀登记流程 / D-4 屏显保留完整编号 / D-5 0 破坏性变更 / D-6 8 个相关技能 SKILL.md 字面更新(本需求精确范围)
- 提取的算法:`parseID(raw, type)` + `generateID(type)`
- 13 份项目级规范自检:1 强约束触发修订(encoding-conventions),7 强约束严守(其他 8 SKILL.md),0 软约束变更

## 项目现状(实现细节)

- **本仓库是纯文档项目**:
  - 0 源代码文件
  - 0 测试框架
  - 0 包管理配置
  - 0 Lint/Build 工具链
- **既有 5 位纯数字编号分布**(V0.0.3):
  - `require/`:REQ-00020 ~ REQ-00025(6 个)
  - `fix/`:BUG-00001(1 个)
  - 任务:`TASK-REQ-00020-00001` ~ `TASK-REQ-00024-00001`(35+ 条;既有格式 `TASK-REQ-NNNNN-NNNNN`)
- **编号正则出现位置**(本需求锚点):
  - `encoding-conventions.md` §规则 1 / §规则 2 / §规则 4(3 处)
  - `code-require/SKILL.md` §"## 输入"段(1 处)+ §"## 标题解析"段(1 处)
  - `code-design/SKILL.md` §"## 输入"段(1 处)+ §"## 工作目录约定"段(1 处)
  - `code-plan/SKILL.md` §"## 输入"段(1 处)+ §"## 任务编号"段(1 处)+ §"## 步骤 9B"段(1 处)
  - `code-it/SKILL.md` §"## 输入"段(1 处)+ §"## 步骤 1"段(1 处)+ §"## 步骤 7"段(1 处)
  - `code-unit/SKILL.md` §"## 输入"段(1 处)
  - `code-check/SKILL.md` §"## 输入"段(1 处)
  - `code-fix/SKILL.md` §"## 输入"段(1 处)+ §"## 步骤 1"段(1 处)
  - `code-dashboard/SKILL.md` §"## 算法 4"段(1 处)
- **既有测试风格**:**无**(0 测试框架;code-unit 守卫"项目可测性"会拒测;沿用"测试状态=不适用")

## 本次变更源

| 变更源 | 检测方式 | 变化列表 |
| --- | --- | --- |
| 需求侧 | require/REQ-00025/RESULT.md v1(已锁定) | 0(无新变更) |
| 概要设计侧 | design/REQ-00025/RESULT.md v1 + 2026-06-08 增量更新确认 | 0(增量更新 no-op) |
| 规范侧 | encoding-conventions.md v1(2026-06-04 10:05) | 1 处软化待落地(本需求 plan/code-it 阶段实施) |
| 代码侧 | 8 个 in-scope SKILL.md 仍含旧 5 位正则 | 8 处待落地(本需求 code-it 阶段实施) |

## 命令行参数

- `--result`:**未传**(本需求不产出 `DESGIN.<ext>` 模板填充文件)
- `--plan`:**未传**(本需求不产出 `PLAN.<ext>` 模板填充文件)
- 沿用 REQ-00007 Q-4 锁定 + REQ-00021 E-4:`code-auto` 上下文不传 2 参数
