# 规范遵循记录 — REQ-00021

更新时间:2026-06-06 17:40
版本:V0.0.3

## 1. 本次参考的规范文件

13 个项目级规范文件全部读取,本需求实际触发的有 9 个,其余 4 个(NFR/Architecture/Coding-style/Framework)不涉及。

| 规范文件 | 类别 | 关键约束摘要 | 本设计是否触发 | 触发后处理 |
| --- | --- | --- | --- | --- |
| `skill-conventions.md` | 技能规范 | §规则 1:frontmatter `name` 字节级保留 | ✅ 触发 | INV-1 / INV-2 锁定 0 改 frontmatter;新增 2 锚点小节 |
| `dashboard-conventions.md` | 看板规范 | §规则 1:看板字段约定扩展需三同步 | ✅ 触发 | INV-4 锁定 0 触发(模板产出物**不**是任务) |
| `encoding-conventions.md` | 编号规范 | §规则 1/3:任务编号 5+5 位嵌套式 | ❌ 不触发 | 本需求 0 改编号格式;0 派生任务 |
| `marketplace-protocol.md` | 市场协议 | 0 改 `marketplace.json` / `plugin.json` | ✅ 触发 | INV-5 锁定 0 改 |
| `module-conventions.md`(DEPRECATED,迁移到 `directory-conventions.md`) | 模块规范 | §规则 1:过程文档摆放位置 | ✅ 触发 | INV-3 / 自检 锁定 0 新增子目录 |
| `commit-conventions.md` | 提交规范 | `chore(<scope>): <subject>` 格式 | ✅ 触发 | INV-7 锁定 0 改;沿用既有 |
| `doc-conventions.md` | 文档规范 | 中英 README 同步 | ✅ 触发 | INV-7 锁定 0 改中英 README |
| `naming-conventions.md` | 命名规范 | 0 新增文件名前缀(规则 1 待添加) | ✅ 触发 | NFR-2.7 锁定基本名 `REQUIRE` / `DESGIN` / `PLAN` 用户原文 |
| `dependency-conventions.md` | 依赖规范 | 0 新增依赖(规则 1 待添加) | ✅ 触发 | NFR-2.8 锁定 0 新增依赖;二进制 follow-up 留作 |
| `directory-conventions.md` | 目录规范 | 子目录命名(规则 1 待添加) | ✅ 触发 | 沿用既有 `require/` / `design/` / `plan/` 目录 |
| `framework-conventions.md` | 框架规范 | 框架选型偏好(规则 1 待添加) | ❌ 不触发 | 本需求是 SKILL.md 文档改造,无框架选型 |
| `coding-style.md` | 编码风格 | 命名 / 注释 / 提交风格(规则 1 待添加) | ❌ 不触发 | 本需求 0 写代码 |
| `migration-mapping.md` | 迁移映射 | 旧 → 新格式映射 | ❌ 不触发 | 本需求 0 改旧格式 |

## 2. 规范 vs 现状偏离(本需求 0)

- 本需求**0**触发任何"现状偏离"——3 技能 SKILL.md 既有"## 工作流程"小节、`## 工具使用约定`小节、`## 衔接`小节、`## 不要做的事`小节**全部字节级保留**
- 模板产出物(`REQUIRE.<ext>` / `DESGIN.<ext>` / `PLAN.<ext>`)是**新文件**,**不**修改既有文件

## 3. 规范 vs 需求冲突(本需求 0)

- 本需求**0**触发任何"规范 vs 需求冲突"
- 全部 FR / NFR / AC / INV 均**不**违反 13 份项目级规范

## 4. 用户授权的偏离(本需求 1 条)

| 偏离维度 | 规范条款 | 偏离内容 | 理由 | 授权时间 |
| --- | --- | --- | --- | --- |
| **可维护性**(NFR-5.1) | SKILL.md 行数变化 -5% ~ +15% | `--extensible` 目标下,3 个 SKILL.md 行数变化可能 +20% ~ +30%(因新增 --map / --vars / --script 扩展点 + 占位符嵌套逻辑) | 用户选择 `--extensible`,要求为后续二进制 follow-up 预留 CLI 接口;新增扩展点不可避免 | 2026-06-06 17:10 |

## 5. 规范变更响应(本概设为首次设计,本节占位)

- 本概设为"首次设计"分支,非"增量更新"分支
- 规范变更响应节在后续增量更新时填写

## 6. 自检结论

### 6.1 完全合规的章节

- ✅ INV-1 frontmatter `name` 字段字节级保留
- ✅ INV-2 既有"## 工作流程"小节 0 改
- ✅ INV-3 既有步骤 0a / 0b / 0 / 1-N 字节级保留
- ✅ INV-4 "## 衔接" + "## 不要做的事" 段 0 改
- ✅ INV-5 0 改 `marketplace.json` / `plugin.json` / `./assistants/rules/` / 看板模板
- ✅ INV-6 0 派生"更新看板"任务
- ✅ INV-7 0 改其他 10 个 `code-*` SKILL.md
- ✅ INV-8 `code-auto` 0 传 `--result` / `--plan`
- ✅ INV-9 NFR-3 幂等(无参时 3 技能按原行为执行)

### 6.2 经用户授权偏离的章节

- NFR-5.1(可维护性,行数变化 -5% ~ +15%):**用户授权偏离**,可能 +20% ~ +30%(见 §4)

### 6.3 待澄清的规范冲突

- (无)本需求**0**待澄清冲突;7 FR / 6 NFR / ~30 AC / 9 INV 全部已锁定
