# REQ-00009 — 详细设计:`/code-unit` 守卫"项目可测性"

- 需求编码:`REQ-00009`
- 所属版本:`V0.0.2`
- 上游需求:`./assistants/V0.0.2/require/REQ-00009/RESULT.md`(v1,已锁定,7 FR / 8 NFR / ~25 AC)
- 上游概要设计:`./assistants/V0.0.2/design/REQ-00009/RESULT.md`(v1,已锁定,8 决策 D-1~D-8,13 规范 0 冲突 0 偏离 0 授权)
- 遵循规范:`./assistants/rules/` 下 13 个文件(7 强约束 + 6 占位;详见 §12 与 `rule-compliance.md`)
- 状态:已完成(详细设计)
- 责任人:wangmiao
- 创建:2026-06-05
- 最近更新:2026-06-05 17:20
- 当前版本:v1

---

## 1. 概述

本详细设计把概要设计"系统长什么样"细化为"系统怎么写"。**核心范围**:**修改 1 个 `code-unit` SKILL.md**(1 个文件增量追加"步骤 0a 项目可测性检查"守卫;**不改 frontmatter / 不改"可测"流程 / 不改"步骤 0"及之后**)。**0** 模块新增,**0** 三方依赖新增,**0** 规范违反,**0** 其他 11 个 `code-*` 技能修改,**0** 看板字段修改(故**不**触发 `dashboard-conventions §规则 1` 三同步);**复用** V0.0.1 既有"不适用"枚举(Q-2 锁定 A),**0** 新增枚举值。

**任务数**:2 个(T-001 `[修改]` SKILL.md + T-002 `[文档]` 收尾不变量自检),遵循 `encoding-conventions §规则 1+3` 5+5 位嵌套式;**首次**应用 REQ-00014 新规则"按功能点拆分"100% 沿用概要设计;**首次**应用 REQ-00017 新规则"不再为'更新看板'拆派生任务"100% 沿用概要设计;**0**"更新看板"派生任务;**0** 架构任务(本需求不满足 REQ-00014 3 触发条件);2 任务测试状态全 `不适用`(Q-P3 锁定 A,纯文档型)。

## 2. 上游引用

引用上游 `./assistants/V0.0.2/require/REQ-00009/RESULT.md`(v1):

| 需求条款 | 本详细设计对应 |
| --- | --- |
| FR-1 新增"步骤 0a 项目可测性检查"守卫 | §4 + §5.1 + §6 + §7 |
| FR-2 守卫不通过 → 跳过 + 看板"不适用" | §5.2 + §6.2 + §7.2 |
| FR-3 不留痕(不写 `test/<任务编码>/RESULT.md` 等) | §5.2 + §6.2 + §7.2 |
| FR-4 不修改 `code-unit` 现有"可测"流程 | §5.3 |
| FR-5 与 9 个其他 `code-*` 技能正交(0 修改) | §5.4 + §8 |
| FR-6 不修改 marketplace / plugin | §5.4 |
| FR-7 报告与建议(屏幕输出守卫检查结果) | §5.2 + §6.2 |
| NFR-1 零新增依赖 | §9 依赖评估 = 0 |
| NFR-2 增量修改 SKILL.md(Edit 追加) | §5.1 + §5.2 修改范围 |
| NFR-3 与 V0.0.1 看板"任务清单"区段枚举完全兼容 | §3.1 + §5.3 |
| NFR-4 与 `code-dashboard` 现有统计逻辑 0 冲突 | §5.4 + §8 |
| NFR-5 与 `code-publish` 前置检查 0 冲突 | §5.4 + §8 |
| NFR-6 与 `code-auto` 退出码兼容(守卫不通过 → 退出码 = 0) | §5.2 + §6.2 |
| NFR-7 性能 < 1 秒 | §9 性能估算 |
| NFR-8 不提供"强制调用"参数(无 `--force`) | §5.4 |

## 3. 模块详细化

### 3.1 模块 M-1:`code-unit/SKILL.md` 修改(本需求唯一)

| 维度 | 详情 |
| --- | --- |
| 路径 | `plugins/code-skills/skills/code-unit/SKILL.md` |
| 状态 | **修改(增量追加)** — 不重写既有 17 章节,仅在"步骤 0"之前插入"步骤 0a" |
| 关键子节 | **新增**:"步骤 0a 项目可测性检查"(锚点:在 `### 步骤 0 — 版本上下文检测` 之前) |
| 关键子节 | **新增**:"步骤 0a.1 守卫检查项清单"(7 项) |
| 关键子节 | **新增**:"步骤 0a.2 守卫判定逻辑" |
| 关键子节 | **新增**:"步骤 0a.3 守卫不通过 → 跳过流程" |
| 关键子节 | **新增**:"步骤 0a.4 屏幕报告格式" |
| 关键子节 | **新增**:"E-2 守卫不通过"边界场景 |
| 既有内容 | **字节级保留**:YAML frontmatter(L1-3)+ §目标 / §适用场景 / §不适用 / §工作目录约定 / §输入 / §输出 / §工具使用约定 / §工作流程(步骤 0-16)/ §过程文档格式 / §衔接 / §不要做的事 + 既有 E-1/E-3~E-7 |
| 依据规范 | `skill-conventions §规则 1`(frontmatter 字节级保留)+ `module-conventions §规则 1`(SKILL.md 在技能根目录) |

#### 3.1.1 调用顺序(本模块对应 `code-unit` 启动)

```
code-unit 启动(守卫改造后)
  ├─ 步骤 0a 项目可测性检查(新增,本需求)
  │   ├─ 7 项 Glob 存在性检查
  │   │   ├─ 检查项 1: package.json(Glob) + 读 + 验证 scripts.test(Read)
  │   │   ├─ 检查项 2: pyproject.toml(Glob) + 读 + 验证测试配置(Read)
  │   │   ├─ 检查项 3: Cargo.toml(Glob)
  │   │   ├─ 检查项 4: go.mod(Glob)
  │   │   ├─ 检查项 5: pom.xml(Glob)
  │   │   ├─ 检查项 6: build.gradle / build.gradle.kts(Glob)
  │   │   └─ 检查项 7: test/ 目录(Glob)
  │   ├─ 命中任一 → 守卫通过 → 屏幕报告"✓ 守卫通过" → 跳到"步骤 0"
  │   └─ 全部不命中 → 守卫不通过 → 屏幕报告"⏭ 跳过" → 进入 FR-2 跳过流程
  ├─ 步骤 0 版本上下文检测(既有,字节级保留)
  ├─ 步骤 1-16 原有单测流程(既有,字节级保留)
  └─ 退出
      ├─ 守卫不通过(FR-2 跳过流程):
      │   ├─ 不调用任何 Bash(FR-2.AC-2.4)
      │   ├─ 不写 test/<任务编码>/RESULT.md(FR-3.AC-3.1, Q-3 锁定 A)
      │   ├─ 写看板"任务清单"区段:测试状态 = 不适用
      │   └─ exit 0(NFR-6)
      └─ 守卫通过(原流程):
          ├─ 写 test/<任务编码>/RESULT.md
          ├─ 写看板"测试状态" = 已运行-通过/失败
          └─ exit 0/非 0(原行为)
```

#### 3.1.2 内部状态 / 并发 / 资源

- **不维护内存状态**:`code-unit` 是无状态工作流定义
- **不写代码 / 配置 / 数据库**
- **不持有任何凭据**
- **并发模型**:N/A(无运行时)
- **资源管理**:N/A(无连接 / 锁 / 缓存)

## 4. 算法与逻辑(对应概要设计 §7 详细化)

### 4.1 守卫检查算法(伪代码)

```python
def guard_check_testable(project_root: str) -> tuple[bool, list[tuple[str, bool]]]:
    """
    守卫检查:项目根 7 项文件/目录存在性
    :return: (testable, details)
        testable: True = 命中任一,False = 全部不命中
        details: [(检查项名, 命中?), ...]
    """
    checks = [
        ("package.json 含 scripts.test", check_package_json_test_script),
        ("pyproject.toml 含测试配置", check_pyproject_toml_test_config),
        ("Cargo.toml", check_file_exists("Cargo.toml")),
        ("go.mod", check_file_exists("go.mod")),
        ("pom.xml", check_file_exists("pom.xml")),
        ("build.gradle / build.gradle.kts", check_build_gradle),
        ("test/ 目录", check_dir_exists("test")),
    ]
    details = []
    for name, fn in checks:
        hit = fn(project_root)
        details.append((name, hit))
    testable = any(hit for _, hit in details)
    return testable, details


def check_package_json_test_script(project_root: str) -> bool:
    """Glob + Read 验证 scripts.test"""
    pj_path = f"{project_root}/package.json"
    if not file_exists(pj_path):
        return False
    content = read_json(pj_path)
    scripts = content.get("scripts", {})
    return "test" in scripts


def check_pyproject_toml_test_config(project_root: str) -> bool:
    """Glob + Read 验证测试配置"""
    pp_path = f"{project_root}/pyproject.toml"
    if not file_exists(pp_path):
        return False
    content = read_toml(pp_path)
    # 检查 [tool.pytest] / [tool.pytest.ini_options] / [tool.tox] 等
    return any(key.startswith("tool.pytest") for key in content)


def check_build_gradle(project_root: str) -> bool:
    """检查 build.gradle 或 build.gradle.kts"""
    return file_exists(f"{project_root}/build.gradle") or \
           file_exists(f"{project_root}/build.gradle.kts")
```

### 4.2 守卫判定逻辑

```python
def code_unit_main(task_id: str):
    # 步骤 0a 项目可测性检查(本需求新增)
    testable, details = guard_check_testable(project_root=CWD)
    if not testable:
        # FR-2 跳过流程
        log("⏭ code-unit 跳过(项目不可测)")
        log(f"  任务: {task_id}")
        log("  守卫检查:")
        for name, hit in details:
            log(f"    - {name}: {'✓' if hit else '✗'}")
        log("  状态:不适用")
        log("  看板'任务清单'区段:测试状态 → 不适用")
        # 写看板(沿用既有"测试状态"列写入路径)
        update_dashboard(task_id=task_id, test_status="不适用")
        # FR-2.AC-2.4:不调用任何 Bash
        # FR-3.AC-3.1:不写 test/<任务编码>/RESULT.md
        # NFR-6:退出码 = 0
        return 0

    # 守卫通过 → 走原"步骤 0"+ 既有单测流程(FR-4 不变)
    log("✓ code-unit 守卫通过(项目可测)进入正常流程")
    log("  守卫检查:")
    for name, hit in details:
        log(f"    - {name}: {'✓' if hit else '✗'}")
    return original_code_unit_main(task_id)
```

### 4.3 看板更新契约(FR-2.AC-2.1)

```python
def update_dashboard(task_id: str, test_status: str):
    """
    复用 code-unit 既有的"测试状态"列写入路径
    写入位置:VERSION/RESULT.md §任务清单
    写入列:测试状态(已有列,非新增)
    写入值:不适用(V0.0.1 既有枚举,Q-2 锁定 A)
    不调用任何 Bash(FR-2.AC-2.4)
    不写 test/<任务编码>/RESULT.md(FR-3.AC-3.1, Q-3 锁定 A)
    """
    # 实现沿用 code-unit 步骤 14 既有路径
    # 本需求不修改该路径,只复用
    ...
```

## 5. 接口细节(对应概要设计 §8 详细化)

### 5.1 入口契约(`code-auto` / 用户调用)

| 调用者 | 输入 | 期望行为 | 退出码 |
| --- | --- | --- | --- |
| `code-auto` 任务循环 | `code-unit TASK-REQ-00009-00001`(根据 `code-it` 输出"测试需要=Y"触发) | 守卫检查 → 通过/跳过 | 0(无论守卫结果,NFR-6) |
| `code-auto` 派生任务循环 | `code-unit TASK-REQ-00009-00002`(派生改修任务) | 守卫检查 → 通过/跳过 | 0(无论守卫结果) |
| 用户直接调用 | `code-unit TASK-REQ-00009-00001` | 守卫检查 → 通过/跳过 | 0(无论守卫结果) |
| `code-publish` 前置检查 | 读 `PLAN.md` 任务"测试状态"列 | 不感知"守卫"概念,只认"不适用"枚举 | N/A |

### 5.2 屏幕输出契约(FR-7.AC-7.1 + FR-7.AC-7.2)

**守卫不通过**:
```
⏭ code-unit 跳过(项目不可测)

任务:TASK-REQ-00009-00001
守卫检查:
  - package.json:✗
  - pyproject.toml:✗
  - Cargo.toml:✗
  - go.mod:✗
  - pom.xml:✗
  - build.gradle:✗
  - test/ 目录:✗
状态:不适用

看板"任务清单"区段:测试状态 → 不适用
```

**守卫通过**:
```
✓ code-unit 守卫通过(项目可测)进入正常流程

任务:TASK-REQ-00009-00001
守卫检查:
  - package.json:✓ (含 scripts.test)
  - pyproject.toml:✗
  - Cargo.toml:✗
  - go.mod:✗
  - pom.xml:✗
  - build.gradle:✗
  - test/ 目录:✗
项目可测,继续原有单测流程
...
(后续按原 code-unit 流程输出)
```

### 5.3 退出码契约(与 `code-auto` 协同)

| 场景 | 退出码 | `code-auto` 响应 |
| --- | --- | --- |
| 守卫不通过 → 跳过 | 0 | 继续下一个任务 |
| 守卫通过 + 测试通过 | 0 | 继续下一个任务 |
| 守卫通过 + 测试失败 | ≠ 0 | 中断(NFR-6 兼容) |
| 守卫通过 + 崩溃 | ≠ 0 | 中断 |
| 任务编码不存在 | ≠ 0 | 中断(原行为) |
| 无 `.current-version` | ≠ 0 | 中断(原行为) |

## 6. 数据结构完整变更(本需求)

### 6.1 看板字段变化(NFR-3 零变更)

| 字段 | 状态 | 备注 |
| --- | --- | --- |
| "任务清单"区段(既有) | **0** 修改 | 只追加 1 行(本计划任务) |
| "测试状态"列(既有) | **0** 修改 | 沿用既有"不适用"枚举 |
| 测试状态枚举值(既有 6 个) | **0** 新增 | Q-2 锁定 A 沿用 |
| "里程碑"区段(既有) | **0** 修改 | 本需求不引入新里程碑 |
| "变更记录"区段(既有) | **追加** 1 条 | 由 `code-plan` 步骤 16A 追加 |

### 6.2 SKILL.md 字段变化

| 字段 | 状态 | 备注 |
| --- | --- | --- |
| YAML frontmatter | **字节级保留** | FR-1.AC-1.5 |
| 既有 17 章节(除"步骤 0"前插入"步骤 0a"外) | **字节级保留** | NFR-2 |
| 新增"步骤 0a 项目可测性检查"子节 | **新增** | 本需求 |
| 既有 E-1/E-3~E-7 边界 | **字节级保留** | 沿用 |
| 新增 E-2 边界(守卫不通过) | **新增** | 本需求 |
| 新增 E-8 边界(守卫检查项扩展预留) | **新增** | NFR-8 留 v2 |

## 7. 异常处理(对应概要设计 §9)

| ID | 场景 | 处理 | 退出码 | 副作用 |
| --- | --- | --- | --- | --- |
| **E-1** | 无 `.current-version` | 提示调 `code-version`,退出(既有) | ≠ 0 | 无 |
| **E-2(新增)** | 守卫不通过(不可测) | 跳过 + 写看板"不适用" | 0 | 仅看板"任务清单"1 行 |
| **E-3** | 守卫通过 + 单测崩溃 | 原 `code-unit` 行为(退出码 ≠ 0,看板"已运行-失败") | ≠ 0 | 看板"已运行-失败" |
| **E-4** | 守卫通过 + 测试通过 | 原 `code-unit` 行为(看板"已运行-通过") | 0 | 看板"已运行-通过" |
| **E-5** | 任务编码不存在 | 原 `code-unit` 行为(报错) | ≠ 0 | 无 |
| **E-6** | `code-auto` 调 `code-unit` 时守卫不通过 | 退出码 = 0,`code-auto` 继续 | 0 | 无 |
| **E-7** | `code-unit` 自身在守卫检查中崩溃 | 退出码 ≠ 0,看板"测试状态" 不变 | ≠ 0 | 无 |
| **E-8(新增,预留)** | 守卫检查项扩展(如未来加 `deno.json`) | v2 增量追加,本需求不实现 | N/A | N/A |

## 8. 安全 / 状态机 / 性能

### 8.1 安全要求
- **不引入**新依赖 → **不增加**新攻击面
- **不**调网络命令 → **不**触发凭据泄露风险
- **不**写敏感数据 → 看板"不适用"是公开状态
- **不**调 `Bash` 跑任意命令 → 守卫不通过时**不**执行外部命令(FR-2.AC-2.4 强约束)

### 8.2 状态机
- **入口**:`code-unit` 启动
- **状态**:`待检查` → `守卫通过` / `守卫不通过` → `步骤 0` / `跳过流程` → `退出`
- **关键不变量**:守卫不通过时**不**进入"步骤 0";**不**调 `Bash`;**不**写 `test/<任务编码>/RESULT.md`;**只**写看板 1 行

### 8.3 性能(NFR-7 < 1 秒)

| 步骤 | 操作 | 预估耗时 |
| --- | --- | --- |
| 步骤 1 | `Glob` 7 项文件/目录 | ~50 ms |
| 步骤 2 | `Read` `package.json`(若存在) | ~50 ms |
| 步骤 3 | `Read` `pyproject.toml`(若存在) | ~50 ms |
| 步骤 4 | 判定 + 写看板"不适用"(若守卫不通过) | ~50 ms |
| **合计** | | **~200 ms** |

**远低于 1 秒**(NFR-7 强约束达成)。

## 9. 依赖评估(NFR-1 零新增)

| 依赖 | 类型 | 必要性 | 体积/性能 | 决策 |
| --- | --- | --- | --- | --- |
| `Glob` 工具 | Claude Code 内置 | 检查文件/目录存在 | < 50 ms | **复用** |
| `Read` 工具 | Claude Code 内置 | 验证 `package.json` / `pyproject.toml` | < 100 ms | **复用** |
| `Edit` 工具 | Claude Code 内置 | 增量追加 SKILL.md | < 200 ms | **复用** |
| `Bash` 工具 | Claude Code 内置 | **不调用**(守卫不通过时) | 0 ms | **不用** |

**总三方依赖新增数:0**(NFR-1 强约束达成)

## 10. 测试要点(本需求)

| 维度 | 内容 | 状态 |
| --- | --- | --- |
| 单元测试 | N/A(纯文档型,无运行时) | `不适用`(Q-P3 锁定 A) |
| 集成测试 | N/A | `不适用` |
| 端到端测试 | N/A | `不适用` |
| 性能/安全 | N/A | `不适用` |
| 静态自检 | 13 项不变量自检(INV-1~13)在 T-002 实施 | 由 T-002 收尾 |

> **静态自检 INVs**(在 T-002 实施,详 §"不变量自检 INV 列表"):
> 1. SKILL.md 存在 + frontmatter 字节级保留
> 2. 步骤 0a 5 子节齐全 + 7 项检查清单
> 3. 既有 17 章节字节级保留(除"步骤 0"前插入"步骤 0a"外)
> 4. 既有 E-1/E-3~E-7 边界字节级保留
> 5. 新增 E-2 边界
> 6. 新增 E-8 边界
> 7. SKILL.md 行数偏差 ≤ ±20%(既有 453 行 + 新增 ~30 行 = ~483 行,偏差 ~7%)
> 8. 8 个关键 token 全部存在(`步骤 0a` / `守卫` / `不适用` / `Q-1` / `Q-2` / `Q-3` / `NFR-6` / `NFR-7`)
> 9. 其他 11 个 `code-*` SKILL.md 字节级不变
> 10. `marketplace.json` / `plugin.json` 字节级不变
> 11. `assistants/rules/` 13 文件字节级不变
> 12. 看板"任务清单"区段测试状态字段写入路径 = 既有路径
> 13. 看板"测试状态"列不新增枚举值(沿用"不适用"既有)

## 11. 计划拆分准则应用(本轮 100% 沿用)

| 准则 | 应用 | 出处 |
| --- | --- | --- |
| **按功能点拆分** | 1 个任务 = 1 个完整功能点;**不拆分到多个任务** | REQ-00014 §10A |
| **架构任务作为首个任务(条件性)** | **0** 架构任务(本需求不满足 REQ-00014 3 触发条件) | REQ-00014 §10A |
| **拆任务约束(实际产出候选集 6 项)** | T-001 = SKILL.md 增量改写(代码改写)✓;T-002 = 自检 + 收尾(文档改写)✓ | REQ-00017 §10A |
| **不在候选集** | 0 个"更新看板"派生任务 ✓ | REQ-00017 §10A |
| **看板推进职责** | 由 `code-it` 末尾兜底后 P-1 小步承担 | REQ-00017 + REQ-00009 |

## 12. 规范遵循(总账)

| 规范文件 | 类别 | 关键约束 | 本设计对应章节 |
| --- | --- | --- | --- |
| `skill-conventions.md` | 技能编写 | §规则 1:frontmatter 必含 name+description | §3.1(字节级保留) |
| `module-conventions.md` | 模块规划(DEPRECATED) | §规则 1:资源放固定子目录 | §3.1(不触达,无资源新增) |
| `dashboard-conventions.md` | 看板与版本工作空间 | §规则 1:字段约定扩展需 3 处同步 | **不触发**(沿用"不适用"既有) |
| `doc-conventions.md` | 文档编写 | §规则 1:中英同次 | (不触达) |
| `marketplace-protocol.md` | Marketplace 协议 | §规则 1:skills 数组以 `./` 开头 | (不触达) |
| `encoding-conventions.md` | 编码格式 | §规则 1-4:任务编号 5+5 位嵌套 | §11(沿用既有) |
| `migration-mapping.md` | 编码迁移 | §规则 1-4:EXISTING-NNN 不追溯 | (不触达) |

**占位规范(6 个,不影响)**:`directory-conventions.md` / `coding-style.md` / `commit-conventions.md` / `dependency-conventions.md` / `framework-conventions.md` / `naming-conventions.md`

### 12.1 自检结论
- **完全合规**的章节:§1 / §2 / §3 / §4 / §5 / §6 / §7 / §8 / §9 / §10 / §11 / §12
- **经用户授权偏离**的章节:**0**
- **待澄清冲突**:**0**

## 13. 关联计划(横向参考)

| 关联需求 | 关联点 | 对本计划的影响 |
| --- | --- | --- |
| **REQ-00005**(V0.0.2) | 步骤 0a 模式命名 | 沿用"步骤 0a"在步骤 0 之前的命名 |
| **REQ-00010**(V0.0.2) | 步骤 0a 模式 | 同位叠加,**0** 冲突 |
| **REQ-00014**(V0.0.2) | 任务拆分维度 | 100% 沿用"按功能点拆分";0 架构任务(不满足 3 触发) |
| **REQ-00017**(V0.0.2) | 拆任务约束 | 100% 沿用"不拆更新看板任务" |
| **REQ-00007**(V0.0.2) | `code-auto` 协同 | NFR-6 退出码 0 兼容 |

## 14. 待澄清 / 未决项

- **冲突 0 条 / 澄清 0 条**

## 15. 变更记录

| 时间 | 版本 | 变更摘要 | 变更人 |
| --- | --- | --- | --- |
| 2026-06-05 17:20 | v1 | 初始创建:14 章节(覆盖模块详细化/算法/接口/数据/异常/安全/状态机/性能/依赖/测试要点/规范遵循)+ PLAN.md 2 个任务(T-001 SKILL.md 修改 + T-002 收尾自检);100% 沿用概要设计 8 决策 D-1~D-8 + 13 规范 0 冲突 0 偏离 0 授权;**首次**应用 REQ-00014 新规则"按功能点拆分"100% 沿用;**首次**应用 REQ-00017 新规则"不拆更新看板任务"100% 沿用;**0** 架构任务触发(不满足 REQ-00014 3 触发);2 任务测试状态全 `不适用`(Q-P3 锁定 A,纯文档型);13 项不变量自检 INV-1~13 在 T-002 实施 | wangmiao |

---

> **下游**:`code-it` 按 `PLAN.md` 的 2 个任务执行,逐任务更新状态;`code-unit` 守卫由 T-001 落地。
