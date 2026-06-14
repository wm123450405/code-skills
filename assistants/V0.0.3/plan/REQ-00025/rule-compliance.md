# 规范遵循 — REQ-00025
版本:V0.0.3

## 13 份项目级规范自检

| 规范 | 触发? | 结论 |
| --- | --- | --- |
| `skill-conventions.md §规则 1` | ✅ 强 | 8 个 SKILL.md frontmatter 字节级保留(INV 严守) |
| `module-conventions.md` | ❌ | DEPRECATED,本修复不引用 |
| `directory-conventions.md` | ❌ | 占位待填,本修复不触发 |
| `encoding-conventions.md §规则 1-4` | ✅ 强 | 本需求**直接修订**(1 处新增 §规则 1.5) |
| `dashboard-conventions.md §规则 1` | ❌ | 0 字段扩展,0 三同步 |
| `doc-conventions.md §规则 1-2` | ❌ | 本修复不涉及 README |
| `coding-style.md` | ❌ | 占位,SKILL.md 是自然语言不涉及代码风格 |
| `commit-conventions.md` | ⚠️ 软 | 沿用 `chore(code-xxx):` 格式 |
| `dependency-conventions.md` | ❌ | 0 新依赖 |
| `framework-conventions.md` | ❌ | 0 架构变更 |
| `naming-conventions.md` | ❌ | 0 新增命名实体 |
| `migration-mapping.md` | ❌ | 0 编码重命名 |
| `marketplace-protocol.md` | ❌ | 0 JSON 字段变更 |

## 自检结论

- **1 强约束触发修订**:`encoding-conventions.md`(本需求 code-it 阶段实施)
- **1 强约束严守**:`skill-conventions.md §规则 1`(frontmatter 字节级保留)
- **0 软约束变更**:`commit-conventions.md` 沿用既有
- **0 用户授权偏离**
- **0 待澄清冲突**(Q-1~Q-4 全部默认决策锁定)
- **0 字段新增**:**不**触发 `dashboard-conventions §规则 1` 三同步
- **0 派生"更新看板"任务**(沿用 REQ-00017 强约束)
