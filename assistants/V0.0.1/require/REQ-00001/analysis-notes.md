# 分析笔记 — REQ-00001
更新时间:2026-06-03 20:20(v2 同步标题,内容不变)

## 需求理解
用户的核心诉求是:**让"marketplace 的名字"和"插件本身的名字"在概念上区分开**,通过给 marketplace 加 `-marketplace` 后缀的方式显式区分。这是命名层面的小重构,但属于**breaking change**:

- 当前安装链:`claude plugin install code-skills@code-skills`
  - 第一个 `code-skills` = plugin name(来自 `plugin.json` 的 `name`)
  - 第二个 `code-skills` = marketplace name(来自 `marketplace.json` 的 `name`)
- 改后安装链:`claude plugin install code-skills@code-skills-marketplace`
  - plugin name 不变
  - marketplace name 加后缀

这种命名区分的好处:
1. 用户看 `@xxx` 时一眼能识别"这是 marketplace 而不是 plugin"
2. 未来若同一 marketplace 加入多个插件,marketplace name 与各 plugin name 不会混淆
3. 符合"marketplace 是容器、plugin 是产品"的概念分层

## 关键决策
1. **范围最小化**:用户明确选 A(只改 marketplace.json 根 name),不动 plugin.json、owner.name、仓库目录、git 远端
2. **协议合规**:严格遵守 `marketplace-protocol.md §规则 1`:
   - `plugins[].name` **不能**跟着改(否则与 plugin.json 失配)
   - `$schema` 保持 `https://anthropic.com/claude-code/marketplace.schema.json`
   - `version` 保持 `1.0.0`(或按 Q-5 决定是否升 minor)
3. **文档同步是强制项**:不是"建议",而是 `doc-conventions §规则 1/2` 强制约束;README.md 与 README.en.md 必须**同次提交**同步

## 候选方案权衡

### 方案 A(已采纳):仅改 marketplace.json 根 name
- ✅ 影响最小,1 个字段 + 文档同步
- ✅ 概念清晰("marketplace = code-skills-marketplace, plugin = code-skills")
- ⚠ 不动 owner.name,理论上 owner 仍可叫 `code-skills`(与 marketplace 区分)
- ❌ install 命令变化 = breaking change(老用户需重新 `marketplace add` + `install`)

### 方案 B(未采纳):同时改 owner.name
- ⚠ owner 是"作者/组织"概念,与 marketplace name 不同维度,捆绑改名反而模糊语义

### 方案 C(未采纳):marketplace 内 4 个 name 都改
- ❌ 违反 `marketplace-protocol §规则 1`:`plugins[].name` 必须与 `plugin.json` 同步,会触发"未同步改 plugin.json"的规则违规

### 方案 D(未采纳):marketplace + plugin + 目录全部统一改
- ❌ 影响面巨大:文件系统、git 远端、所有 SKILL.md 路径、文档、缓存目录、slash 命令前缀(`/code-skills:` → `/code-skills-marketplace:`)全部变化
- ❌ 与用户"加 marketplace 后缀以区分"的本意不符 — 用户想区分,而不是统一

## 临时假设
- 假设 1:用户**不希望**升 marketplace.json 的 `version`(从 `1.0.0` 到 `1.1.0`)— 列为 Q-5 待澄清
- 假设 2:用户**不希望**修改 marketplace.json 的 `description` 字段 — 列为 Q-3 待澄清
- 假设 3:CLAUDE.md 仅含结构性描述,未硬编码 `code-skills@code-skills` 安装命令字符串,因此 CLAUDE.md 可能**无需修改**(FR-7 改为"核查并视情况更新")

## 下一轮要深挖
- 如果用户回答 Q-4(添加迁移指引),需评估指引应放在 README 哪个章节
- 如果用户回答 Q-5(升 version),需触发 `dashboard-conventions §规则 1` 之外的额外同步(marketplace.json `version` 与 `plugin.json` `version` 是**独立**的,但仍需在 README 中说明)
- 若实施阶段(`code-it`)发现 README 中还有其它隐藏 `code-skills` 引用需要区分(如"clone 仓库"段中的 git URL,与"marketplace name"不同维度),需在该阶段记录偏差并回头确认

## 风险
- **R-1**:用户当前已发布该 marketplace 给真实用户的话,改名 = breaking change,老 install 链路失效;需要在迁移指引中明示
- **R-2**:文档同步漏掉会触发 `doc-conventions §规则 2` 违规,且老用户跟着错的命令操作会失败 — `code-it` 阶段必须穷举搜索 `code-skills@code-skills` 串
