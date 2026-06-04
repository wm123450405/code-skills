# 三方依赖评估 — REQ-00005

更新时间:2026-06-04 16:00
版本:V0.0.2

## 1. 结论

**本需求零新增运行时三方依赖**。NFR-1 显式要求,且本仓库本身**无应用代码**(无 Node.js / Python / Go 等运行时),无法承载运行时依赖。

## 2. 复用既有依赖

| 依赖 | 形态 | 来源 | 用途 |
| --- | --- | --- | --- |
| `git` | **外部系统命令** | 系统 PATH(Bash 工具调用) | FR-1 `git pull` / FR-3 `git status` / `git add` / `git commit` |
| Claude Code 工具集 | **Claude Code 内置** | 工具:`Read` / `Edit` / `Bash` / `AskUserQuestion` | 工作流步骤执行 |
| Claude Code 技能调用机制 | **Claude Code 内置** | 工具:`Skill` | FR-2.AC-2.4 调 `code-version`(独立技能调用) |

> 上述**全部**是"已存在"的依赖,本需求不引入任何新条目。

## 3. 新增依赖

| 依赖 | 版本 | 用途 | 必要性 | 许可 | 风险评估 |
| --- | --- | --- | --- | --- | --- |
| (无) | — | — | — | — | — |

**本需求无新增依赖**。

## 4. 拒绝引入的依赖及理由

| 候选 | 否决理由 |
| --- | --- |
| 任何 Git 操作的 Python / Node.js 库(如 `simple-git` / `nodegit`) | 仓库无 Python / Node.js 运行时(CLAUDE.md 显式声明),引入即破坏"无技术栈"原则 |
| 任何 Git 操作 shell 包装脚本 | `git` 命令本身已足够;引入包装 = 多一层维护成本 + 与 Bash 工具调用重复 |
| 任何 commit message 模板库(如 `commitlint`) | 模板由技能按既定格式(`chore(<scope>): <subject>`)字符串拼接生成,无需外部库 |
| 任何"仓库状态检查"工具(如 `pre-commit` / `husky`) | FR-1.AC-1.3 / FR-3.AC-3.6 的失败处理已通过"读 git 退出码 + stderr 透传"完成,无需 hook |
| 任何版本号比较库(如 `semver`) | 本需求不涉及版本号比较逻辑(只读字符串对比),无需库 |

## 5. 规范遵循

| 规范条款 | 满足度 | 说明 |
| --- | --- | --- |
| NFR-1(零新增依赖) | ✅ 满足 | 0 新增 |
| `dependency-conventions.md §规则 1` | ✅ 不触发 | 占位文件,本需求不引入新依赖,无规则适用 |
| 隐式 §"是否有项目内已有可复用替代" | ✅ 满足 | `git` 已是 Bash 工具内置,无替代评估需求 |

## 6. 维护说明

- 本需求**不**修改 `dependency-conventions.md`
- 本需求**不**修改 `package.json` / `pyproject.toml` / `Cargo.toml` / `go.mod` / `pom.xml` / `build.gradle`(本仓库**无**这些文件)
- `git` 探测逻辑在 `code-require` / `code-design` / `code-plan` 三个技能的工作流中实现(命令:`git --version`),失败提示见 E-12
