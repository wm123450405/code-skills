# 材料登记 — REQ-00038

更新时间:2026-06-22 13:40
版本:V0.0.3

## 项目级规范

> 跨版本共享,本需求**仅消费**不修改;13 份规范全部沿用。

| 规范文件 | 类别 | 关键约束摘要 | 本需求应用 |
| --- | --- | --- | --- |
| `module-conventions.md` | 模块规划 | 资源放 `templates/` / `checklists/` / `guidelines/` 子目录(规则 1) | 模板 `RESULT.md` 在 `code-it/templates/` 内,位置合规 |
| `encoding-conventions.md` | 编码格式 | REQ/BUG/TASK 三类编码(规则 1);5 位纯数字(规则 2);嵌套式(规则 3) | 不涉及编码产出 |
| `skill-conventions.md` | 技能编写 | SKILL.md frontmatter 含 name + description(规则 1);不包含开发痕迹(规则 2) | INV:不修改 frontmatter;遵守"零开发痕迹" |
| `dashboard-conventions.md` | 看板 | 字段约定扩展需三方同步(规则 1) | INV:0 触发(本需求不新增列/区段/枚举) |
| `doc-conventions.md` | 文档 | README 多语言对仗(规则 1) | 不涉及 |
| `coding-style.md` | 编码风格 | 命名/错误处理/安全/性能 | 不涉及(本需求为 Markdown 改造) |
| `commit-conventions.md` | 提交 | 提交信息格式 | 末尾兜底 commit 沿用 |
| `dependency-conventions.md` | 依赖 | 不引入未经评审的新依赖 | INV-8 0 新增三方依赖 |
| `directory-conventions.md` | 目录 | 技能目录结构 | INV-1 不修改 SKILL.md frontmatter |
| `framework-conventions.md` | 框架 | 框架选型 | 不涉及 |
| `naming-conventions.md` | 命名 | 命名风格 | INV:不涉及 |
| `migration-mapping.md` | 迁移 | 新旧编码追溯 | 不涉及 |
| `marketplace-protocol.md` | 插件市场 | 插件发布协议 | 不涉及 |

**自检结论**:
- 13 份规范全部适用本需求(仅消费)
- 0 份规范触发修改
- 0 项用户授权偏离
- 0 项待澄清冲突

## 上游需求

- 来源:`./assistants/V0.0.3/require/REQ-00038/RESULT.md` (v1)
- 提取的 FR / NFR / AC 数量:**5 FR / 6 NFR / 7 AC**
- 关键交叉点(每条 FR 对应的设计章节):
  - FR-1 模块识别 → RESULT.md §5 算法 1 + `module-details.md` 模块 1
  - FR-2 步骤 8a 守卫位置 → RESULT.md §5 算法 2 + `module-details.md` 模块 2
  - FR-3 步骤 8.5 单测输出 → RESULT.md §5 算法 3 + `module-details.md` 模块 3
  - FR-4 模板多模块支持 → `interface-specs.md` 接口 1
  - FR-5 code-plan 字面改写 → `module-details.md` 模块 4

## 上游概要设计

- 来源:`./assistants/V0.0.3/design/REQ-00038/RESULT.md` (v1)
- 提取的模块拆分 / 接口概要 / 数据结构 / 决策:
  - **模块拆分**:5 个子模块(1 新增 + 3 修改 + 1 字面改写)
  - **接口概要**:5 个内部行为接口
  - **数据结构**:3 个运行时数据(`modules` / `moduleTestable` / `moduleTestDir`)
  - **关键决策**:8 项(D-1 ~ D-8)

## 项目现状(实现细节)

- 既有 `code-it/SKILL.md` 步骤 8a 守卫:**字节级沿用** REQ-00034 7 项守卫(检查位置 = CWD 根)
- 既有 `code-it/templates/RESULT.md` "## 9. 单元测试(由 code-it 内化,新增,"小节(L138-153):字节级保留
- 既有 `code-plan/SKILL.md` "测试类型已从本列表移除"段(L473):字面改写 1 句
- 既有 `code-plan/SKILL.md` "双状态语义"段(L496):字面改写 1 句
- 模块识别优先级链(FR-1 锁定):
  1. 声明文件(monorepo workspace):pnpm-workspace.yaml / package.json#workspaces / lerna.json / nx.json / turbo.json / pom.xml#modules / Cargo.toml#workspace.members / go.mod module 路径
  2. git diff 公共子目录
  3. CWD 根退化(原 REQ-00034 行为)
- 测试目录识别优先级链(FR-3 锁定):见 `module-details.md` 模块 3

## 本次变更源

- **需求侧**:REQ-00038 v1(2026-06-22 13:00)
- **概要设计侧**:REQ-00038 design v1(2026-06-22 13:30)
- **规范侧**:0 变化
- **代码侧**:既有 0 改,本次新增 3 个 SKILL.md 子节 + 1 模板小节追加 + 1 文档字面改写
