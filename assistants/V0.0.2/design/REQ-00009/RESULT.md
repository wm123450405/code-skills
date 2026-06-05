# REQ-00009 — 概要设计:优化 `/code-unit`,增加"项目可测性"守卫

- 需求编码:`REQ-00009`
- 所属版本:`V0.0.2`
- 上游需求:`./assistants/V0.0.2/require/REQ-00009/RESULT.md`(v1,已锁定,7 FR / 8 NFR / ~25 AC)
- 遵循规范:`./assistants/rules/` 下 13 个文件(7 强约束 + 6 占位 + 1 DEPRECATED;详见 §3 与 `rule-compliance.md`)
- 状态:已完成(首次概要设计)
- 责任人:wangmiao
- 创建:2026-06-05
- 最近更新:2026-06-05 17:10
- 当前版本:v1

---

## 1. 概要设计概述

在需求基础上,本概要设计把"系统长什么样"细化为"系统怎么写"。核心决策:**修改 1 个 `code-unit` SKILL.md**(1 个文件增量追加,**新增"步骤 0a 项目可测性检查"守卫**;不改 frontmatter / 不改"可测"流程 / 不改"步骤 0"及之后);**0** 模块新增,**0** 三方依赖新增,**0** 规范违反,**0** 其他 11 个 `code-*` 技能 SKILL.md 修改,**0** 看板字段修改(故**不**触发 `dashboard-conventions §规则 1` 三同步);**复用** V0.0.1 既有"不适用"枚举(Q-2 锁定 A),**0** 新增枚举值。**关键不变量**:本守卫仅在 `code-unit` 启动时检测项目根,纯文件存在性检查(< 1 秒,NFR-7),不影响 `code-it` 写码流程;`code-auto` 任务循环据此正确调 `code-unit` 并据"测试需要=Y"决定是否触发;`code-publish` 前置检查继续用"测试∈{已运行-通过, 不适用}"判定(已含"不适用",NFR-5 兼容)。

## 2. 需求回顾

引用上游 `./assistants/V0.0.2/require/REQ-00009/RESULT.md`(v1):

- **FR-1** 新增"步骤 0a 项目可测性检查"守卫 → §4.1 + §6.1 + §7.1 详细化
- **FR-2** 守卫不通过 → 跳过 + 看板"任务清单"区段测试状态 = `不适用` → §4.2 + §6.1 详细化
- **FR-3** 不留痕(不写 `test/<任务编码>/RESULT.md` 等)→ §4.2 + §7.1 详细化
- **FR-4** 不修改 `code-unit` 现有"可测"流程 → §4.1 详细化
- **FR-5** 与 9 个其他 `code-*` 技能正交(0 修改)→ §5.4 + §8 详细化
- **FR-6** 不修改 marketplace / plugin → §5.4 详细化
- **FR-7** 报告与建议(屏幕输出守卫检查结果)→ §6.2 详细化
- **NFR-1** 零新增依赖 → §6 依赖评估 = 0
- **NFR-2** 增量修改 SKILL.md(Edit 追加)→ §5.1 + §5.2 修改范围
- **NFR-3** 与 V0.0.1 看板"任务清单"区段枚举完全兼容 → §3.1 + §5.3 详细化
- **NFR-4** 与 `code-dashboard` 现有统计逻辑 0 冲突 → §5.4 + §8 详细化
- **NFR-5** 与 `code-publish` 前置检查 0 冲突 → §5.4 + §8 详细化
- **NFR-6** 与 `code-auto` 退出码兼容(守卫不通过 → 退出码 = 0)→ §4.2 详细化
- **NFR-7** 性能 < 1 秒 → §6.1 详细化
- **NFR-8** 不提供"强制调用"参数(无 `--force`)→ §5.4 详细化

## 3. 规范遵循(总账)

### 3.1 适用的规范文件

| 规范文件 | 类别 | 关键约束 | 本概要设计对应章节 |
| --- | --- | --- | --- |
| `./assistants/rules/skill-conventions.md` | 技能编写 | §规则 1:frontmatter 必含 name+description | §5.1(不触达,frontmatter 字节级保留) |
| `./assistants/rules/module-conventions.md` | 模块规划(DEPRECATED) | §规则 1:资源放固定子目录 | §6 依赖评估(不触达,无资源新增) |
| `./assistants/rules/dashboard-conventions.md` | 看板与版本工作空间 | §规则 1:字段约定扩展需 3 处同步 | **不触发**(本设计**不**改字段,沿用"不适用"既有枚举) |
| `./assistants/rules/doc-conventions.md` | 文档编写 | §规则 1:中英同次;§规则 2:持续维护 | (不触达,无中英 README 变更) |
| `./assistants/rules/marketplace-protocol.md` | Marketplace 协议 | §规则 1:skills 数组以 `./` 开头 | (不触达,本需求**不**新增技能) |
| `./assistants/rules/encoding-conventions.md` | 编码格式 | §规则 1-4:任务编号 5+5 位嵌套 | (不触达,本需求无新编码) |
| `./assistants/rules/migration-mapping.md` | 编码迁移 | §规则 1-4:EXISTING-NNN 不追溯 | (不触达) |

**占位规范(6 个,不影响)**:`directory-conventions.md` / `coding-style.md` / `commit-conventions.md` / `dependency-conventions.md` / `framework-conventions.md` / `naming-conventions.md`

### 3.2 自检结论

- **完全合规**的章节:§1 / §2 / §3 / §4 / §5 / §6 / §7 / §8 / §9
- **经用户授权偏离**的章节:**0**
- **待澄清冲突**:**0**

> 详细规范遵循记录见 `rule-compliance.md`(本目录)。

## 4. 模块详细化

### 4.1 模块 M-1:`code-unit/SKILL.md` 修改(对应概要设计 §7.1)

#### 关键"组件"(SKILL.md 的工作流视角)

| 组件 | 形式 | 职责 | 状态 |
| --- | --- | --- | --- |
| 步骤 0a 项目可测性检查 | 新增子节 | 检测项目根 7 项文件/目录(任一存在 → 可测,否则 → 不可测 → 跳过) | **新增** |
| 步骤 0 版本上下文检测 | 既有子节 | 读 `.current-version`(沿用既有,不修改) | 沿用 |
| 步骤 1-N 原有单测流程 | 既有子节 | 编写 / 跑 / 评估单测(沿用既有,不修改) | 沿用 |
| frontmatter | YAML | name=code-unit, description ~600 字符 | **字节级保留**(FR-1.AC-1.5) |
| 既有 E-1~E-7 边界 | 子节 | 原边界场景(沿用既有,不修改) | 沿用 |
| 既有"步骤 0" | 子节 | 版本上下文检测(沿用既有,不修改) | 沿用 |

#### 关键"调用顺序"(对应 `code-unit` 启动)

```
code-unit 启动(守卫改造后)
  ├─ 步骤 0a 项目可测性检查(新增,本需求)
  │   ├─ 7 项 Glob 存在性检查(package.json 含 scripts.test / pyproject.toml 含测试配置 / Cargo.toml / go.mod / pom.xml / build.gradle(.kts) / test/ 目录)
  │   ├─ 命中任一 → 守卫通过 → 跳到"步骤 0"
  │   └─ 全部不命中 → 守卫不通过 → 进入 FR-2 跳过流程
  ├─ 步骤 0 版本上下文检测(既有)
  ├─ 步骤 1-N 原有单测流程(既有)
  └─ 退出
      ├─ 守卫不通过(FR-2 跳过流程):
      │   ├─ 不调用任何 Bash
      │   ├─ 不写 test/<任务编码>/RESULT.md
      │   ├─ 写看板"任务清单"区段:测试状态 = 不适用
      │   └─ exit 0
      └─ 守卫通过(原流程):
          ├─ 写 test/<任务编码>/RESULT.md
          ├─ 写看板"测试状态" = 已运行-通过/失败
          └─ exit 0/非 0(原行为)
```

#### 内部状态

- **不维护内存状态**:`code-unit` 是无状态工作流定义
- **不写代码 / 配置 / 数据库**
- **不持有任何凭据**

#### 资源管理

- **N/A**(无连接 / 锁 / 缓存)

### 4.2 关键行为契约(对应 FR-2 / FR-3 / NFR-6)

| 场景 | 输入 | 行为 | 退出码 | 副作用 |
| --- | --- | --- | --- | --- |
| 守卫不通过(不可测项目) | 项目根无 7 项文件/目录 | 跳过 + 写看板"不适用" | 0 | 仅看板"任务清单"行 1 行 |
| 守卫通过 + 单测成功 | 项目根有 `package.json` 含 `scripts.test` 等 | 跑原单测流程 + 写 `test/<任务编码>/RESULT.md` | 0 | `test/.../RESULT.md` + 看板 |
| 守卫通过 + 单测失败 | 同上 | 跑原单测流程(原失败行为) | ≠ 0 | 看板"已运行-失败" |
| 守卫通过 + 单测崩溃 | 同上 | 原 `code-unit` 行为(退出码 ≠ 0) | ≠ 0 | 看板"已运行-失败" |
| 项目根无 `.current-version` | 既有 E-1 | 提示调 `code-version`,退出(原行为) | ≠ 0 | 无 |
| 任务编码不存在 | 既有 E-5 | 原 `code-unit` 行为(报错) | ≠ 0 | 无 |

> **关键**:守卫不通过时 `code-auto` 据此继续(NFR-6 + FR-5 兼容)。

## 5. 修改范围

### 5.1 修改方式(NFR-2 增量改,FR-1.AC-1.5)

- **方式**:`Edit` 工具**追加**"步骤 0a 项目可测性检查"子节(不重写既有章节)
- **锚点**:在 SKILL.md 的 `## 工作流程` 区段下,**在 `### 步骤 0 — 版本上下文检测` 之前**插入
- **预估新增行数**:~30 行(7 项检查清单 + 守卫判定逻辑 + 跳过流程)
- **删除行数**:0
- **净增**:~30 行

### 5.2 SKILL.md 既有内容保留清单

| 既有内容 | 行数范围(当前) | 状态 |
| --- | --- | --- |
| YAML frontmatter | L1-3 | **字节级保留** |
| §目标 / §适用场景 / §不适用 / §工作目录约定 | L6-50 | 字节级保留 |
| §输入 / §输出 / §工具使用约定 | L52-90 | 字节级保留 |
| §工作流程 → 步骤 0 版本上下文检测 | L94-95 | 字节级保留 |
| §工作流程 → 步骤 1-16(原 16 步) | L96-280 | 字节级保留 |
| §过程文档格式 | L283-300 | 字节级保留 |
| §衔接 / §不要做的事 | L303-330 | 字节级保留 |

> 实际行号以实施时 SKILL.md 最新版本为准(NFR-2 增量追加原则:只增不改)。

### 5.3 看板字段变化(NFR-3 零变更)

- **0** 新增区段
- **0** 新增列
- **0** 新增枚举值(沿用 V0.0.1 既有"不适用")
- **0** 字段语义变更

### 5.4 影响范围

- **`code-unit` 自身**:`Edit` 增量追加"步骤 0a",其他子节字节级保留
- **其他 11 个 `code-*` 技能**:0 触碰(FR-5 强约束)
- **`marketplace.json` / `plugin.json`**:0 触碰(FR-6 强约束)
- **`assistants/rules/`**:0 触碰
- **中英 README**:0 触碰(无新增技能)

## 6. 依赖评估

### 6.1 运行时依赖(FR-1 + NFR-7 守卫实现)

| 依赖 | 形式 | 必要性 | 体积/性能 | 评估 |
| --- | --- | --- | --- | --- |
| `Glob` 工具(已有) | Claude Code 内置 | 检查文件存在 | < 50 ms | **0 新增**(沿用) |
| `Read` 工具(已有) | Claude Code 内置 | 读 `package.json` / `pyproject.toml` 验证 scripts.test / [tool.pytest] | < 100 ms | **0 新增**(沿用) |
| `Bash` 工具(已有) | Claude Code 内置 | 仅在"可测"流程中跑测试命令 | 视项目而定 | **0 新增**(守卫不通过时不调用) |

**总依赖新增数**:**0**(NFR-1 锁零依赖)

**性能估算**(NFR-7 < 1 秒):
- 守卫 7 项 Glob 检查 = ~50 ms
- 必要时 Read 验证 `package.json` / `pyproject.toml` = ~100 ms
- 合计 < 200 ms,**远低于 1 秒**

### 6.2 兼容性

- 与 `code-auto` 退出码兼容(守卫不通过 → 0,`code-auto` 继续)
- 与 `code-publish` 前置检查兼容(测试=不适用 仍属"任务解决")
- 与 `code-dashboard` 现有统计逻辑兼容(复用"不适用"枚举,0 改动)
- 与 `code-review` 现有逻辑兼容(测试状态字段不变)

## 7. 关键算法与数据结构

### 7.1 守卫检查算法(对应 FR-1 / Q-1 锁定 A)

```
function guard_check_testable(project_root: str) -> {testable: bool, details: list}:
  checks = [
    ("package.json 含 scripts.test", lambda: read_json_if_exists(f"{project_root}/package.json")?.scripts?.test exists),
    ("pyproject.toml 含测试配置", lambda: read_toml_if_exists(f"{project_root}/pyproject.toml") 中 [tool.pytest] 等存在),
    ("Cargo.toml", lambda: file_exists(f"{project_root}/Cargo.toml")),
    ("go.mod", lambda: file_exists(f"{project_root}/go.mod")),
    ("pom.xml", lambda: file_exists(f"{project_root}/pom.xml")),
    ("build.gradle / build.gradle.kts", lambda: file_exists(f"{project_root}/build.gradle") or file_exists(f"{project_root}/build.gradle.kts")),
    ("test/ 目录", lambda: dir_exists(f"{project_root}/test"))
  ]
  results = [run(check) for check in checks]
  testable = any(result.hit for result in results)
  return {testable, details = [(name, hit) for each check]}
```

### 7.2 守卫判定逻辑

```
if guard_result.testable:
  log("✓ code-unit 守卫通过(项目可测)进入正常流程")
  log("  守卫检查:")
  for name, hit in guard_result.details:
    log(f"    - {name}: {'✓' if hit else '✗'}")
  goto step_0
else:
  log("⏭ code-unit 跳过(项目不可测)")
  log("  任务: <任务编码>")
  log("  守卫检查:")
  for name, hit in guard_result.details:
    log(f"    - {name}: {'✓' if hit else '✗'}")
  log("  状态:不适用")
  log("  看板"任务清单"区段:测试状态 → 不适用")
  update_dashboard(task_id, test_status="不适用")
  exit(0)
```

### 7.3 看板更新契约(FR-2.AC-2.1)

```
update_dashboard(task_id, test_status="不适用"):
  // 复用 code-unit 既有的"测试状态"列写入路径(NFR-3 沿用 V0.0.1 既有枚举)
  // 写入位置:VERSION/RESULT.md §任务清单
  // 写入列:测试状态(已有列,非新增)
  // 写入值:不适用(V0.0.1 既有枚举,Q-2 锁定 A)
  // 不调用任何 Bash(FR-2.AC-2.4)
  // 不写 test/<任务编码>/RESULT.md(FR-3.AC-3.1,Q-3 锁定 A)
```

## 8. 接口契约(与外部协作)

### 8.1 入口契约(`code-auto` / 用户调用)

| 调用者 | 输入 | 期望行为 | 退出码 |
| --- | --- | --- | --- |
| `code-auto` 任务循环 | `code-unit TASK-REQ-00009-00001`(根据 `code-it` 输出"测试需要=Y"触发) | 守卫检查 → 通过/跳过 | 0(无论守卫结果) |
| `code-auto` 派生任务循环 | `code-unit TASK-REQ-00009-00002`(派生改修任务) | 守卫检查 → 通过/跳过 | 0(无论守卫结果) |
| 用户直接调用 | `code-unit TASK-REQ-00009-00001` | 守卫检查 → 通过/跳过 | 0(无论守卫结果) |
| `code-publish` 前置检查 | 读 `PLAN.md` 任务"测试状态"列 | 不感知"守卫"概念,只认"不适用"枚举 | N/A |

### 8.2 退出码契约(与 `code-auto` 协同)

| 场景 | 退出码 | `code-auto` 响应 |
| --- | --- | --- |
| 守卫不通过 → 跳过 | 0 | 继续下一个任务 |
| 守卫通过 + 测试通过 | 0 | 继续下一个任务 |
| 守卫通过 + 测试失败 | ≠ 0 | 中断(NFR-6 兼容) |
| 守卫通过 + 崩溃 | ≠ 0 | 中断 |
| 任务编码不存在 | ≠ 0 | 中断(原行为) |

## 9. 异常与边界(对应 FR-7 + 既有 E-1~E-7)

| ID | 场景 | 处理 | 对应需求 |
| --- | --- | --- | --- |
| **E-1** | 无 `.current-version` | 提示调 `code-version`,退出(同其他 9 技能) | 既有 E-1 |
| **E-2(新增)** | 守卫不通过(不可测) | 跳过 + 写看板"不适用" | FR-2 + E-2 |
| **E-3** | 守卫通过 + 单测崩溃 | 原 `code-unit` 行为(退出码 ≠ 0,看板"已运行-失败") | 既有 E-6(本需求沿用) |
| **E-4** | 守卫通过 + 测试通过 | 原 `code-unit` 行为(看板"已运行-通过") | 既有 E-4(本需求沿用) |
| **E-5** | 任务编码不存在 | 原 `code-unit` 行为(报错) | 既有 E-5 |
| **E-6** | `code-auto` 调 `code-unit` 时守卫不通过 | 退出码 = 0,`code-auto` 继续 | NFR-6 |
| **E-7** | `code-unit` 自身在守卫检查中崩溃 | 退出码 ≠ 0,看板"测试状态" 不变 | 既有 E-7(本需求沿用) |
| **E-8(预留)** | 守卫检查项扩展(如未来加 `deno.json`) | v2 增量追加,本需求不实现 | NFR-8 |

> 边界 E-2 为本需求**新增**,E-3~E-7 沿用既有。

## 10. 关联设计(横向参考)

- **REQ-00005**(V0.0.2)——"首步拉取 + 末步兜底提交"模式:本需求沿用其"步骤 0a"模式命名(`code-unit` 步骤 0a 项目可测性检查)
- **REQ-00010**(V0.0.2)——`code-it` 步骤 0a 前置任务检查:本需求与之**同位**叠加(两个技能各自有"步骤 0a"),**0** 冲突
- **REQ-00004**(V0.0.2)——`code-dashboard` 现有"任务清单"区段:复用既有"不适用"枚举,**0** 改动
- **REQ-00006**(V0.0.2)——`code-publish` 前置检查:沿用"测试∈{已运行-通过, 不适用}",**0** 改动
- **REQ-00007**(V0.0.2)——`code-auto` 编排者:与守卫退出码 0 兼容,本需求让"无意义调用"自动消失
- **REQ-00008**(V0.0.2)——`code-review` 整版本模式:本需求**不**影响 review 逻辑

## 11. 变更记录

| 时间 | 版本 | 变更摘要 | 变更人 |
| --- | --- | --- | --- |
| 2026-06-05 17:10 | v1 | 初始创建:1 个 SKILL.md 增量追加"步骤 0a 项目可测性检查"守卫;7 项检查清单(`package.json` 含 `scripts.test` / `pyproject.toml` 含测试配置 / `Cargo.toml` / `go.mod` / `pom.xml` / `build.gradle`(.kts) / `test/` 目录);FR-1~FR-7 / NFR-1~NFR-8 全部继承;100% 沿用需求 3 项锁定(Q-1 只检查项目根 + Q-2 复用"不适用" + Q-3 不写 test/&lt;任务编码&gt;/RESULT.md);0 模块新增 + 0 三方依赖 + 0 规范违反 + 0 其他 11 个 `code-*` 技能修改 + 0 看板字段修改(故不触发 `dashboard-conventions §规则 1`);0 偏离 0 授权 0 待澄清 | wangmiao |

---

> **下游**:`code-plan` 消费本概要设计产出详细设计与任务计划。
