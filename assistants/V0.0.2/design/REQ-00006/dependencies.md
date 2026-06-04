# 三方依赖评估 — REQ-00006

更新时间:2026-06-04 16:48
版本:V0.0.2

## 1. 复用既有依赖

### 1.1 Claude Code 内置工具
| 工具 | 用途 | 复用方式 |
| --- | --- | --- |
| `Read` | 读 `.current-version` / `RESULT.md` / 模板 / qanda 内容 | 直接调用 |
| `Glob` | 列出版本目录(基线判定)+ qanda/*.md | 直接调用 |
| `Write` | 写 publish/ 下 3 份手册 + qanda/README.md | 直接调用 |
| `Bash` | `mkdir -p` / `ls` 检测 | 直接调用 |
| `AskUserQuestion` | (本设计无需要;NFR-3 暗示不引入额外交互) | 不使用 |

### 1.2 项目内既有资产
| 资产 | 复用方式 |
| --- | --- |
| `./assistants/.current-version` 标记文件 | **只读** |
| `./assistants/<版本号>/RESULT.md` 主看板 | **只读** |
| `code-version/templates/version-RESULT.md` 看板结构参考 | **只读**(作为解析锚点对照) |
| `code-design/templates/assistants-layout.md` 范式 | 复制相同模板到本技能 |

## 2. 新增依赖

| 依赖 | 版本 | 用途 | 必要性 | 许可 | 风险评估 |
| --- | --- | --- | --- | --- | --- |
| **无** | — | — | — | — | — |

**结论**:0 新增依赖,严格遵循 NFR-1 + `dependency-conventions.md`(占位规范,无具体条款)。

## 3. 拒绝引入的依赖及理由

| 候选依赖 | 用途 | 拒绝理由 |
| --- | --- | --- |
| `remark` / `mistletoe` / 其他 Markdown 解析库 | 看板表格解析 | **D-2 决策**:违反 NFR-1;且按行硬解析在 V0.0.1 已被实证(多次 dashboard / publish 共用同一解析规则,稳定 4+ 月) |
| YAML/JSON 配置(配置驱动手册模板) | 替代纯 Markdown 模板 | 违反 NFR-9(可读性优先),用户审阅 Markdown 比 JSON 更直观 |
| `git` 命令(自动 commit / 自动 push) | 末尾自动提交 | **NFR-3 显式禁止**;Q-9 默认采纳 |
| `git log` 抽取(自动填 DEPLOY 的"变更说明") | 变更日志自动填入 | Q-6 默认采纳"不自动抽取",v2 可加 |
| 外部模板引擎(jinja / mustache) | placeholder 替换 | 简单字符串替换即可,无需引擎 |

## 4. 对照 `dependency-conventions.md` 自检

| 规范项 | 本设计状态 | 合规 |
| --- | --- | --- |
| 规则 1(待添加,占位) | 0 新增依赖,占位不影响 | ✓ |

**结论**:0 不合规项;**若未来 `dependency-conventions.md` 添加"禁止 X 类依赖"等规则,本设计仍合规**(零依赖)。
