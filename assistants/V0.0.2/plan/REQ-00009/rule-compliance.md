# 规范遵循记录 — REQ-00009
更新时间:2026-06-05 17:20
版本:V0.0.2

## 1. 本次参考的规范文件
- `./assistants/rules/skill-conventions.md`(技能编写)
- `./assistants/rules/module-conventions.md`(模块规划,DEPRECATED)
- `./assistants/rules/dashboard-conventions.md`(看板与版本工作空间)
- `./assistants/rules/doc-conventions.md`(文档编写)
- `./assistants/rules/marketplace-protocol.md`(Marketplace 协议)
- `./assistants/rules/encoding-conventions.md`(编码格式)
- `./assistants/rules/migration-mapping.md`(编码迁移)

**占位规范(6 个,不影响)**:`directory-conventions.md` / `coding-style.md` / `commit-conventions.md` / `dependency-conventions.md` / `framework-conventions.md` / `naming-conventions.md`

## 2. 规范 vs 现状偏离
- **现状**:本仓库为纯 Markdown 文档型项目(无源代码 / 无构建 / 无测试框架)
- **影响**:本详细设计让 `code-unit` 守卫在"项目不可测"时自动跳过,**正好匹配**本仓库现状
- **无需纠正**:本设计**不**需要纠正任何现状偏离

## 3. 规范 vs 需求冲突
- **冲突 0 条**
- 所有 FR-1~FR-7 / NFR-1~NFR-8 与本目录 7 个强约束规范**0** 冲突

## 4. 用户授权的偏离
- **偏离 0 条**
- 本详细设计**100% 沿用**需求 FR / NFR,**0** 偏离

## 5. 规范变更响应(增量更新时填写)
- **不适用**(本计划为首次设计,无规范变更)
- 未来若 `dashboard-conventions §规则 1` 新增枚举值 / 新增区段,本设计需回退评估(NFR-3 兼容性)

## 6. 详细自检表

### 6.1 `skill-conventions §规则 1`(frontmatter 必含 name+description)
| 检查项 | 结果 |
| --- | --- |
| `code-unit/SKILL.md` frontmatter 含 `name: code-unit` | ✅ 字节级保留(FR-1.AC-1.5) |
| `description` 非空,涵盖目标 + 适用场景 + 触发条件 | ✅ 字节级保留 |
| 修改后 frontmatter **不**变 | ✅ 本计划**不**改 frontmatter |

### 6.2 `module-conventions §规则 1`(资源放固定子目录)
| 检查项 | 结果 |
| --- | --- |
| SKILL.md 在技能根目录 | ✅(既有) |
| 资源在 `templates/` / `checklists/` / `guidelines/` 子目录 | ✅(既有 3 份 templates/,本计划**不**新增) |
| 修改后**不**引入新子目录 | ✅ 本计划**不**新增子目录 |

### 6.3 `dashboard-conventions §规则 1`(字段约定扩展需 3 处同步)
| 检查项 | 结果 |
| --- | --- |
| 是否新增/删除/重命名"区段" | ❌ 无 |
| 是否新增/删除/重命名"表格列" | ❌ 无 |
| 是否新增/删除/修改"枚举值" | ❌ 无(沿用"不适用"既有) |
| 是否调整"字段语义说明" | ❌ 无 |
| 结论 | ✅ **0 触发**本规则(沿用既有"不适用"枚举) |

### 6.4 `doc-conventions §规则 1`(中英同次提交)
| 检查项 | 结果 |
| --- | --- |
| 本计划是否改中英 README | ❌ 无(本计划**不**改 README) |
| 结论 | ✅ **不触达** |

### 6.5 `marketplace-protocol §规则 1`(skills 数组以 `./` 开头)
| 检查项 | 结果 |
| --- | --- |
| 本计划是否新增技能 | ❌ 无(本计划**不**新增技能) |
| 结论 | ✅ **不触达** |

### 6.6 `encoding-conventions §规则 1-4`(任务编号 5+5 位嵌套)
| 检查项 | 结果 |
| --- | --- |
| 本计划是否产出新编码 | ✅ 2 个任务(TASK-REQ-00009-00001 / 00002)严格遵循 5+5 位嵌套 |
| 结论 | ✅ **100% 遵循** |

### 6.7 `migration-mapping §规则 1-4`(EXISTING-NNN 不追溯)
| 检查项 | 结果 |
| --- | --- |
| 本计划是否追溯重命名 | ❌ 无(本计划**不**涉及 EXISTING-NNN) |
| 结论 | ✅ **不触达** |

## 7. 与既有 11 个 `code-*` 技能 SKILL.md 的字节级保留

| 技能 | 是否触碰 | 备注 |
| --- | --- | --- |
| `code-init` | ❌ | 独立 |
| `code-version` | ❌ | 独立 |
| `code-rule` | ❌ | 独立 |
| `code-require` | ❌ | 独立 |
| `code-design` | ❌ | 独立 |
| `code-plan` | ❌ | 独立(本计划**不**触发其变更) |
| `code-it` | ❌ | 独立(本计划**不**触发其变更) |
| `code-fix` | ❌ | 独立 |
| `code-review` | ❌ | 独立 |
| `code-dashboard` | ❌ | 沿用既有"不适用"枚举,**0** 改动 |
| `code-publish` | ❌ | 沿用既有"测试∈{已运行-通过, 不适用}",**0** 改动 |
| `code-auto` | ❌ | 协同关系,本计划**不**改其 SKILL.md |
| `code-merge` | ❌ | 独立 |

## 8. 总结

- **0 冲突 / 0 偏离 / 0 授权 / 0 触发 `dashboard-conventions §规则 1` 同步**
- **100% 沿用**需求 FR-1~FR-7 + NFR-1~NFR-8
- **100% 沿用**概要设计 8 决策 D-1~D-8
- **0 新增**模块 / 0 新增依赖 / 0 触发任何规范变更
- **2 任务**严格遵循 `encoding-conventions §规则 1+3` 5+5 位嵌套式
- **首次**应用 REQ-00014 新规则"按功能点拆分"100% 沿用
- **首次**应用 REQ-00017 新规则"不拆更新看板任务"100% 沿用
