# 接口详细规格 — REQ-00005

更新时间:2026-06-04 16:30
版本:V0.0.2

> 本仓库**无运行时 API**。"接口" = SKILL.md 中描述的工作流步骤。本文档给出每个步骤的**完整伪代码 / 弹窗文本 / 错误码**,供 `code-it` 阶段直接落地。

---

## 步骤 0a — 拉取最新代码(FR-1,3 技能通用)

### 接口契约

| 维度 | 内容 |
| --- | --- |
| **形式** | SKILL.md 工作流步骤描述(自然语言)+ Bash 工具调用 |
| **前置条件** | 用户在 Claude Code 中启动 `code-require` / `code-design` / `code-plan` |
| **后置条件(成功)** | 工作树与远端同步(包含 no-op)+ `.current-version` 已被读取 |
| **后置条件(失败)** | 中断 + stderr 透传 + 分类提示 |
| **鉴权** | N/A(本仓库无应用代码) |
| **版本策略** | N/A(本仓库语义版本 V0.0.2,但工作流步骤不分版本) |

### 完整伪代码

```
# 步骤 0a — 拉取最新代码
# 输入:无
# 输出:无(全局副作用:git pull 成功 + 读取 .current-version)
# 异常:git --version 失败 / git pull 失败 → 中断退出

def step_0a_pull_latest_code():
    # 1. 探测 git 可用性
    result = bash("git --version")
    if result.exit_code != 0:
        print("✗ 未检测到 git,本需求需要 git,请先安装 git 后重试")
        sys.exit(1)  # E-12

    # 2. 执行 git pull
    result = bash("git pull")

    # 3. 失败分类
    if result.exit_code != 0:
        stderr = result.stderr.lower()

        if "conflict" in stderr or "unmerged" in stderr:
            # E-2:冲突
            conflict_files = extract_conflict_files(result.stderr)
            print(f"✗ git pull 失败:存在未解决的冲突,冲突文件:{conflict_files}")
            print("  请手动解决冲突后,重跑该技能")
            sys.exit(1)

        elif "could not resolve" in stderr or "connection" in stderr or "timeout" in stderr:
            # E-3:网络
            remote_url = bash("git remote get-url origin").stdout.strip()
            print(f"✗ git pull 失败:网络/remote 不可达,远程仓库:{remote_url}")
            print("  请检查网络/代理后重试")
            sys.exit(1)

        elif "permission denied" in stderr or "authentication failed" in stderr or "403" in stderr:
            # E-4:凭据
            print(f"✗ git pull 失败:权限/凭据")
            print(f"  请检查 git 凭据(SSH key / token)后重试")
            sys.exit(1)

        else:
            # 其他错误
            print(f"✗ git pull 失败:未知错误")
            print(f"  stderr: {result.stderr}")
            sys.exit(1)

    # 4. 拉取成功(包含 no-op)
    # NFR-8 强约束:立即读取 .current-version(不缓存)
    pulled_version = read("./assistants/.current-version").strip()
    return pulled_version
```

### 错误码 / 异常类

| 错误码 | 场景 | 提示 |
| --- | --- | --- |
| E-12 | `git --version` 失败 | `✗ 未检测到 git,本需求需要 git,请先安装 git 后重试` |
| E-2 | `git pull` 冲突 | `✗ git pull 失败:存在未解决的冲突,冲突文件:<列出>` |
| E-3 | `git pull` 网络失败 | `✗ git pull 失败:网络/remote 不可达,远程仓库:<url>` |
| E-4 | `git pull` 凭据失败 | `✗ git pull 失败:权限/凭据,请检查 git 凭据(SSH key / token)后重试` |
| (其他) | 未知错误 | `✗ git pull 失败:未知错误,stderr:<...>` |

### 示例(本仓库实际)

```bash
# 正常路径(本仓库 V0.0.2)
$ git --version
git version 2.45.2.windows.1

$ git pull
Already up to date.

$ cat .current-version
V0.0.2
```

### 验证手段
- `Bash: git status` → 应显示 "Your branch is up to date" 或已合并远端
- `Read .current-version` → 与远端 `git show HEAD:assistants/.current-version` 一致

### 对应任务
- `TASK-REQ-00005-00001`(步骤 0a 部分)
- `TASK-REQ-00005-00002`(步骤 0a 部分)
- `TASK-REQ-00005-00003`(步骤 0a 部分)

### 依据规范
- NFR-8(拉取后立即读 `.current-version`)
- Q-2 锁定 A(中断 + 报错退出)

---

## 步骤 0b — 工作版本号对齐检查(FR-2,仅 `code-require` 专属)

### 接口契约

| 维度 | 内容 |
| --- | --- |
| **形式** | SKILL.md 工作流步骤描述 + Read 工具 + AskUserQuestion 工具 + Skill 工具 |
| **前置条件** | 步骤 0a 成功(已读"拉取后版本") |
| **后置条件(一致)** | 进入既有"步骤 0 — 版本上下文检测" |
| **后置条件(不一致 + 选 A)** | 调独立技能 `code-version <拉取后版本>`,成功后**退出** `code-require` |
| **后置条件(不一致 + 选 B)** | 在当前 `<用户意图版本>` 继续,进入步骤 0 |
| **后置条件(不一致 + 选 C)** | 退出 `code-require`,无任何文件变更 |
| **鉴权** | N/A |
| **版本策略** | N/A |

### 完整伪代码

```
# 步骤 0b — 工作版本号对齐检查
# 输入:pulled_version(步骤 0a 的输出)
# 输出:无 / 退出(选 A) / 进入步骤 0(选 B 或版本一致) / 退出(选 C)

def step_0b_version_alignment(pulled_version):
    # 1. 读取"用户意图版本"
    pre_pull_version = read("./assistants/.current-version").strip()  # 步骤 0a 之前的快照
    # 注:本会话内若已读取则复用,否则新读(实际实现由 Claude Code 上下文管理)

    # 默认:用户意图 = 拉取前版本
    user_intent_version = pre_pull_version
    # 若用户在原始输入中显式指定了其他版本,则取用户指定(本需求 v1 不实现该解析)

    # 2. 对比
    if user_intent_version == pulled_version:
        # 一致:进入既有"步骤 0"
        return "proceed"

    # 3. 不一致:询问
    print(f"""
✗ 检测到上下文版本不一致
  本地(拉取后):{pulled_version}
  用户意图:{user_intent_version}
  需求 <需求编码> 在 {user_intent_version} 中可能不存在,但在 {pulled_version} 中已存在
""")

    choice = ask_user_question(
        question="请选择后续动作:",
        options=[
            {
                "label": f"A. 切到 {pulled_version} 后继续(推荐)",
                "description": f"调 code-version 切换到 {pulled_version},然后退出 code-require,提示重跑"
            },
            {
                "label": f"B. 在 {user_intent_version} 中重新创建 <需求编码>",
                "description": f"在当前 {user_intent_version} 中继续,会走原步骤 1 收集需求编码"
            },
            {
                "label": "C. 取消",
                "description": "退出 code-require,无任何文件变更"
            }
        ]
    )

    # 4. 处理选项
    if choice == "A":
        # 调独立技能 code-version
        invoke_skill("code-version", args=[pulled_version])
        print(f"已切到 {pulled_version},请重跑 code-require")
        sys.exit(0)  # 退出 code-require,无文件变更
    elif choice == "B":
        # 在当前版本继续
        return "proceed"
    elif choice == "C":
        # 取消
        sys.exit(0)  # 退出,无文件变更
```

### AskUserQuestion 弹窗示例

```yaml
question: "请选择后续动作:"
options:
  - label: "A. 切到 V0.0.3 后继续(推荐)"
    description: "调 code-version 切换到 V0.0.3,然后退出 code-require,提示重跑"
  - label: "B. 在 V0.0.2 中重新创建 REQ-00006"
    description: "在当前 V0.0.2 中继续,会走原步骤 1 收集需求编码"
  - label: "C. 取消"
    description: "退出 code-require,无任何文件变更"
```

### 错误码 / 异常类

| 错误码 | 场景 | 处理 |
| --- | --- | --- |
| (无) | 询问必须答,无超时 | E-11 |
| (透传) | `code-version` 调用失败 | 透传错误,提示"请手动运行 `code-version <version>` 后重试" |

### 示例

```yaml
# 假设场景:本机 V0.0.2,拉取后 V0.0.3,需求 REQ-00006
pulled_version: "V0.0.3"
user_intent_version: "V0.0.2"
需求 REQ-00006: V0.0.2 中不存在,但 V0.0.3 中已存在

# 输出
✗ 检测到上下文版本不一致
  本地(拉取后):V0.0.3
  用户意图:V0.0.2
  需求 REQ-00006 在 V0.0.2 中可能不存在,但在 V0.0.3 中已存在

[弹窗 3 选 1]
```

### 验证手段
- 本地与远端一致 → 步骤 0b 静默通过(无弹窗)
- 本地与远端不一致 → 弹窗正确显示 + 选项正确处理

### 对应任务
- `TASK-REQ-00005-00001`(步骤 0b 部分,仅 `code-require`)

### 依据规范
- FR-2 + NFR-3(硬中断)
- Q-1 锁定 A(询问用户二选一,默认推荐远端)

---

## 步骤 N — 末尾兜底提交(FR-3,3 技能通用)

### 接口契约

| 维度 | 内容 |
| --- | --- |
| **形式** | SKILL.md 工作流步骤描述 + Bash 工具 + AskUserQuestion 工具 |
| **前置条件** | 原工作流最后一步完成(无变更/有变更均可) |
| **后置条件(无变更)** | 跳过 commit + 打印"无文件变更,跳过末尾提交" |
| **后置条件(有变更 + 确认)** | commit 完成 + 打印 hash |
| **后置条件(有变更 + 取消)** | 跳过 commit + 打印"已取消提交" |
| **后置条件(commit 失败)** | stderr 透传 + 提示手动处理(不重试) |
| **鉴权** | N/A |
| **版本策略** | N/A |

### 完整伪代码

```
# 步骤 N — 末尾兜底提交
# 输入:无(读 git 状态)
# 输出:无(全局副作用:git add + git commit)

def step_N_end_commit(skill_scope, req_id, req_title, stats):
    # 1. 收集 dirty 文件
    result = bash("git status --porcelain")
    dirty_files = parse_porcelain(result.stdout)

    if not dirty_files:
        # AC-3.5 / NFR-4 幂等
        print("无文件变更,跳过末尾提交")
        return "skipped"

    # 2. 暂存
    add_result = bash(f"git add {' '.join(dirty_files)}")
    if add_result.exit_code != 0:
        print(f"✗ git add 失败:stderr={add_result.stderr}")
        sys.exit(1)

    # 3. 生成 commit message 预览
    message = generate_commit_message(skill_scope, req_id, req_title, stats)

    # 4. 弹窗确认(Q-3 锁定 A)
    choice = ask_user_question(
        question="请选择提交动作:",
        options=[
            {"label": "A. 确认提交(推荐)", "description": f"用上述 commit message 提交"},
            {"label": "B. 修改 commit message", "description": "重新生成预览或用户编辑"},
            {"label": "C. 取消提交", "description": "跳过 commit,文件保持暂存状态"}
        ],
        preview=message
    )

    if choice == "C":
        print("已取消提交,文件保持暂存/工作区状态")
        return "cancelled"  # E-9

    elif choice == "B":
        # 重新生成预览(本计划不实现"用户编辑"功能 — v1 仅"重新生成")
        # 实际实现可让用户输入新的 message
        new_message = input("请输入新的 commit message:")
        message = new_message
        # 再次弹窗确认(简化:直接 commit)
        return step_N_execute_commit(message)

    elif choice == "A":
        return step_N_execute_commit(message)


def step_N_execute_commit(message):
    result = bash(f"git commit -m {shlex.quote(message)}")
    if result.exit_code == 0:
        # 提取 commit hash
        hash_match = re.search(r"\[[\w-]+(?:\s[\w-]+)*\s([a-f0-9]+)\]", result.stdout)
        commit_hash = hash_match.group(1) if hash_match else "未知"
        print(f"commit 完成,hash: {commit_hash}")
        return "committed"
    else:
        # E-10:失败不重试
        print(f"✗ 末尾提交失败,文件已暂存")
        print(f"  退出码:{result.exit_code}")
        print(f"  错误:{result.stderr}")
        print(f"  请手动处理后,执行 git commit")
        return "failed"


def generate_commit_message(skill_scope, req_id, req_title, stats):
    """根据不同技能生成不同 commit message"""
    if skill_scope == "code-require":
        return f"""chore(code-require): {req_id} {req_title}

需求分析完成:{stats['FR']} FR / {stats['NFR']} NFR / {stats['AC']} AC
过程文件 3 + 结果文件 1 = {stats['total_files']} 文件待提交"""
    elif skill_scope == "code-design":
        return f"""chore(code-design): {req_id} {req_title}

概要设计完成:{stats['decisions']} 项决策,{stats['invariants']} 条不变量
过程文件 N + 结果文件 1"""
    elif skill_scope == "code-plan":
        return f"""chore(code-plan): {req_id} {req_title}

详细设计与编码计划完成:{stats['tasks']} 个任务
过程文件 N + 结果文件 2(PLAN.md + RESULT.md)"""
```

### AskUserQuestion 弹窗示例

```yaml
question: "请选择提交动作:"
options:
  - label: "A. 确认提交(推荐)"
    description: "用上述 commit message 提交"
  - label: "B. 修改 commit message"
    description: "重新生成预览或用户编辑"
  - label: "C. 取消提交"
    description: "跳过 commit,文件保持暂存状态"
preview: |
  chore(code-require): REQ-00005 优化 3 个技能,首步拉取+末步兜底提交

  需求分析完成:6 FR / 8 NFR / ~32 AC
  过程文件 3 + 结果文件 1 = 4 文件待提交
```

### 错误码 / 异常类

| 错误码 | 场景 | 处理 |
| --- | --- | --- |
| E-8 | `git status --porcelain` 空 | 打印"无文件变更,跳过末尾提交",退出 |
| E-9 | 用户选 C(取消) | 打印"已取消提交,文件保持暂存",退出 |
| E-10 | `git commit` 失败 | 透传 stderr,**不重试**,提示手动处理 |
| (无) | `git add` 失败 | 透传 stderr,中断退出 |

### commit message 模板(3 个技能)

| 技能 | 模板 |
| --- | --- |
| `code-require` | `chore(code-require): REQ-NNNNN <需求标题>` + 空行 + `需求分析完成:<N> FR / <M> NFR / <K> AC` + 空行 + `过程文件 3 + 结果文件 1 = <X> 文件待提交` |
| `code-design` | `chore(code-design): REQ-NNNNN <设计标题>` + 空行 + `概要设计完成:<D> 项决策,<I> 条不变量` + 空行 + `过程文件 N + 结果文件 1` |
| `code-plan` | `chore(code-plan): REQ-NNNNN <计划标题>` + 空行 + `详细设计与编码计划完成:<T> 个任务` + 空行 + `过程文件 N + 结果文件 2(PLAN.md + RESULT.md)` |

### 验证手段
- `Bash: git log -1` → 显示新 commit + 正确 message
- `Bash: git status --porcelain` → 应为空(已 commit)
- `Bash: git show HEAD` → 验证 commit 包含正确文件

### 对应任务
- `TASK-REQ-00005-00001`(步骤 N 部分)
- `TASK-REQ-00005-00002`(步骤 N 部分)
- `TASK-REQ-00005-00003`(步骤 N 部分)
- `TASK-REQ-00005-00004`(看板同步,因末尾 commit 涉及)

### 依据规范
- FR-3 / NFR-4(幂等) / NFR-5(错误透明) / NFR-6(commit 格式) / NFR-7(与 `code-it` 边界)
- Q-3 锁定 A(预览 + 确认) / Q-4 锁定 B(并存)

---

## 接口总览

| 接口名 | 形式 | 状态 | 对应任务 | 依据规范 |
| --- | --- | --- | --- | --- |
| 步骤 0a(拉取) | SKILL.md 步骤 + Bash | 新增(3 技能) | T-001 / T-002 / T-003 | NFR-8 / Q-2 |
| 步骤 0b(版本对齐) | SKILL.md 步骤 + Read + AskUserQuestion + Skill | 新增(仅 `code-require`) | T-001 | FR-2 / NFR-3 / Q-1 |
| 步骤 N(兜底提交) | SKILL.md 步骤 + Bash + AskUserQuestion | 新增(3 技能) | T-001 / T-002 / T-003 / T-004 | FR-3 / NFR-4~7 / Q-3 / Q-4 |

## 关键决策

- **鉴权方式**:N/A(本仓库无应用代码,无 API)
- **错误码体系**:E-1 ~ E-13 边界场景(见 `risk-analysis.md`)
- **限流策略**:N/A
- **幂等保证**:NFR-4(`git status --porcelain` 空时跳过) + 步骤 0a 幂等(no-op)
- **链路追踪字段**:N/A(无 trace_id)
