# 运行环境探测与提示机制 — code-req / code-fix

> 本文件为 code-req 与 code-fix 技能在 CODING 阶段的最后编译/单测环节提供统一的运行环境处理规范,避免擅自安装运行环境造成不可预期的副作用。
>
> 在 CODING 阶段编译/单测步骤(对应 code-req references/coding.md §4.9-§4.11、code-fix SKILL.md 步骤 4)遇到"常规命令找不到运行环境"的场景时加载本文件。
>
> **本文件**也为各语言参考(`languages/<lang>.md`)提供统一的运行环境边界基线,使各语言文档能聚焦在命令模板而不是策略说明。

## §0 适用范围与术语

### 运行环境(runtime environment)

指"构建/运行/测试整套工具链本身",其缺失是**工具链整体**没装到机器上,即"命令行找不到 `go`、`python`、`node`、`mvn`、`gradle`、`cargo` 等可执行程序"。

### 依赖包(package dependency)

指"工具链能正常启动,但具体要用的库/模块在项目内没声明或在 lockfile 中缺失",例如 `npm install` 失败、Python `ModuleNotFoundError` 提示 `ModuleNotFoundError: No module named 'requests'`、Java `package xxx does not exist`、`go: cannot find package "xxx"`。

### 关键区分原则

| 失败信号 | 归类 | 处理方式 |
| --- | --- | --- |
| `command not found: go` / `'mvn' is not recognized` / `'python3' 不是内部或外部命令` | **运行环境缺失** | 走本文件 §2 确认机制 |
| `No module named 'xxx'` / `Cannot find package 'xxx'` / npm 找不到 `xxx@x.x.x` | **依赖包缺失** | 走各语言包管理器(`npm install` / `pip install` / `go get` / `cargo add` / 修改 `pom.xml`/`build.gradle`) |
| `Could not download` / 镜像源拉取失败 | **网络问题** | 走错误修复循环,询问用户处理 |
| 工具链存在但版本对不上 | **环境问题**(子集) | 按"运行环境缺失"流程处理 |
| 语法错误、断言失败、单测红 | **代码 bug / 设计缺陷** | 走错误修复循环 |

> **重要:必须先进行过实际尝试执行并确实因环境问题失败时,才触发本机制。**仅看一眼没有运行就推断"环境缺失"是不允许的——先把命令敲一遍、看到错误信息再判断。

## §1 三态处理模型

### 交互模式

| 触发条件 | 默认模式 / `--confirm` | `--auto` |
| --- | --- | --- |
| 编译/测试运行失败,且归类为"运行环境缺失" | 弹出 §2 确认提示,**等待用户决策** | 自动尝试通过包管理器或下载引导安装缺失的运行时,**无需询问** |
| 编译/测试运行失败,归类为"依赖包缺失" | **直接走包管理器**(无需询问) | **直接走包管理器**(无需询问) |
| 用户选择"放弃后续编译/测试运行" | 在 TASK-N.md 中标注"用户跳过运行环境配置,后续由用户自行验证",**仍然完成编码**,但跳过编译/测试运行/单测三步 | N/A |

### 关键规则

1. **绝对不要**未经确认就执行"下载并安装 Go/Python/Node/Java/Rust 这类系统级运行时"的命令(包括但不限于 `winget install golang`、`brew install python`、`apt install maven`、`curl -sSL https://install.python.today | bash` 等)
2. **依赖包** 不在本限制范围——按需使用 `npm install` / `pip install` / `go get` / `cargo add` / `mvn dependency:get` 等命令,**不需要询问**
3. 用户**放弃**后续编译/运行时,本任务仍然可以完成,只把状态标注为"用户跳过运行验证"——这是被允许的退出路径

## §2 确认提示模板(默认 / --confirm 模式)

```
⚠️ 检测到运行时缺失:
  - 在 CODING 阶段 <构建/运行/单测> 步骤中执行 <command> 时失败
  - 失败信息: <原始错误信息,例如 'go' 不是内部或外部命令>
  - 判定类别: <运行环境缺失 / 版本不匹配>

可能原因:本机未安装 <runtimeName>(<例如 Go / Python / Node.js / JDK / Maven / Rust>),或安装后未加入 PATH。

请选择:
A. 提供已安装的运行时位置 (推荐)
   - 请告知 <runtime> 的可执行文件绝对路径(例如 C:\Program Files\Go\bin\go.exe)
   - 我会用该路径继续本次任务的编译/测试

B. 让我尝试为你安装该运行时
   - 仅在你显式同意后,我会调用系统的包管理器(winget / choco / scoop / brew / apt 等)进行安装
   - 安装位置将遵循系统的默认约定,不会被写入任何文档

C. 跳过本任务的编译/运行/单测验证
   - 本任务的代码修改仍然完成
   - 在 TASK-N.md 的"验证结果"中标注 "用户跳过运行验证,由用户自行编译/运行"
   - 风险:后续 CHECK 阶段会缺少运行证据,可能产生"建议改"或"可选"类型的审查意见

D. 终止整个任务(回退本任务代码)
```

### 选项处理

- **选 A**:用户通常会在自然语言回答里给出路径。如用户给出的是相对路径或简化名(如"go 装在 `~/sdk/go1.21/bin`"),先尝试 `where <runtime>` / `which <runtime>` 探测,若仍未找到再以用户回答为准,把后续命令改为绝对路径执行。**不**把用户提供的路径写入任何文档(详见 §5)。
- **选 B**:`--auto` 模式自动进入此分支;非 `--auto` 模式必须用户显式选择。安装过程:检测可用包管理器(`winget` > `choco` > `scoop` > `brew` > `apt` …)→ 调用对应命令 → 验证 `command -v <runtime>` 或 `<runtime> --version` 通过后继续。
- **选 C**:在 TASK-N.md 第 4 节表格里把"编译 / 运行 / 测试"改为 `用户跳过`,并在该行附简短原因(不含路径与具体环境值,见 §5)。后续编码循环仍然可以往下推进,代码修改也已经落地。
- **选 D**:回退本任务在 CWD 下的代码改动(`git checkout -- <files>`),回到任务开始的快照。

### --auto 模式分支

`--auto` 模式下 **不询问用户**:

```
1. 尝试常规命令<command> → 失败
2. 判定失败类别 = "运行环境缺失"
3. 自动尝试通过系统包管理器安装该运行时(优先 winget / choco / scoop / brew / apt)
   - 若包管理器不在场 → 退化:失败信息原样上报 + 中断当前任务
4. 安装完成 → 重试失败命令 → 继续或继续失败(进入错误修复循环)
```

> **--auto 模式下用户已经授权"尽量自动搞定",所以包括运行时安装在内的所有动作都无需逐项确认。**

## §3 各语言常规运行环境判定

各语言参考(`languages/<lang>.md`)应当提供**该语言常规需要哪些运行时**,下面是基线:

| 语言 | 必装的运行时 | 检测命令 | 常见安装方式 |
| --- | --- | --- | --- |
| Node.js / TS | `node`(同时也是 `npm`)、可选 `yarn` / `pnpm` | `node --version` / `npm --version` | winget / nvm / fnm / brew |
| Python | `python`(≥3.x);项目级虚拟环境不算运行时缺失 | `python --version` / `python3 --version` | 官方安装包 / pyenv / brew |
| Java (Maven) | `java`(JDK)+ `mvn` | `java -version` / `mvn --version` | Adoptium / Temurin / Microsoft OpenJDK / brew |
| Java (Gradle) | `java`(JDK)+ `gradle` | `java -version` / `gradle --version` | 同上,`gradle` 可改用项目内 wrapper |
| Go | `go` | `go version` | winget / go.dev 官方安装包 / brew |
| Rust | `cargo`(常由 rustup 提供);`rustc` | `cargo --version` / `rustc --version` | rustup / brew |

> **wrapper 优先原则**:检测到 `mvnw` / `gradlew` / `cargo` 项目内置脚本时,优先使用 wrapper 而非全局命令——wrapper 自带下载能力,常能绕开"系统未装 maven/gradle"的问题;此时不应触发本机制。

## §4 不属于运行时的命令

以下情况不归本机制管辖,按各语言的正常依赖处理流程走:

- `npm install` / `yarn install` / `pnpm install` / `pip install -r requirements.txt` / `go mod download` / `cargo fetch` 等"拉依赖"的命令
- 项目内 `package.json` / `pom.xml` / `Cargo.toml` / `pyproject.toml` 缺失某个声明的包
- 上述命令的网络错误、镜像源错误、版本冲突错误

## §5 隐私约束(强制)

**绝不允许**将以下信息写入文档或记忆:

- 系统包管理器自动安装时的安装位置(如 `C:\Program Files\Go`、`/usr/local/bin/python3`、`~/.cargo/bin/cargo`)
- 用户在选项 A 中提供的运行时路径(如 `C:\Users\me\sdk\go1.21\bin`)
- 任何形式的"本机运行时配置"`facts`(含 `PATH` 内容、特定工具的 `which` 结果等)

**只允许记录**:

- "运行时检查结果"——枚举值:`已配置` / `由用户跳过` / `由用户授权自动安装` / `由用户提供路径`,不允许附加具体路径
- 上述枚举值在 TASK-N.md 第 4 节"验证结果"中以"运行时"行呈现

`MEMORY.md` / `user` / `feedback` 类型记忆项**不得**包含:

- "用户机器上 Go 装在 xxx 路径"等个性化配置
- "用户的 PATH 是 xxx"等环境快照

理由:不同用户的本地环境状况不同,记录会污染其他用户使用技能时的判断。

---

## 衔接

- 上游:`code-req references/coding.md` §4.9-§4.11(编译/运行/测试);`code-fix SKILL.md` 步骤 4(同一组步骤)
- 下游:`code-req references/coding.md` §7 错误修复循环 / 步骤 5 撰写 TASK-N.md
- 相关:`code-req/templates/TASK.md` 第 4 节验证结果(含一行运行时)

## 不要做的事

- 不要在没真正尝试运行前就推断"环境缺失"
- 不要把"依赖包缺失"误判为"运行时缺失"——前者必须用包管理器直接装,不需要询问
- 不要未经用户确认就执行系统级安装(`winget install`/`brew install`/`apt install` 等)
- 不要把运行时路径写进 TASK.md / PROCESS.md / LOG.md
- 不要把运行时路径存储为 MEMORY 项
