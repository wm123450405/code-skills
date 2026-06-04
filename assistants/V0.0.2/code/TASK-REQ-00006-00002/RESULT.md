# 改修总结 — TASK-REQ-00006-00002

## 1. 任务信息

- **任务编码**:`TASK-REQ-00006-00002`
- **任务标题**:`[新增] 写 templates/DEPLOY.md 模板(8 章节 + placeholder + 默认示例)`
- **类型**:新增
- **触发/来源**:需求新增
- **关联任务**:无
- **前置任务**:无(独立任务)
- **来源 PLAN.md**:`./assistants/V0.0.2/plan/REQ-00006/PLAN.md` v1.1
- **完成时间**:2026-06-04 17:34
- **完成人**:wangmiao
- **提交哈希**:`<不提交 — 留 dirty tree 由用户在 T-007 后整体 commit>`

## 2. 改修内容总览

| 类别 | 路径 | 操作 | 大小 |
| --- | --- | --- | --- |
| 新增 | `plugins/code-skills/skills/code-publish/templates/DEPLOY.md` | Write | 245 行,~10 KB |

**总计**:1 个新文件,0 个修改文件,0 个删除文件。

## 3. 详细改动

### 新增 `plugins/code-skills/skills/code-publish/templates/DEPLOY.md`

#### 3.1 路径合规性

- ✓ 位于 `plugins/code-skills/skills/code-publish/templates/` 子目录
- ✓ 文件名 `DEPLOY.md`(kebab-case `<用途>.md`)
- ✓ 符合 `module-conventions.md §规则 1`

#### 3.2 章节结构(8 大章节 + 7 子章节 + 1 附录)

| 章节 | 内容 | 子章节 |
| --- | --- | --- |
| **1. 概述** | 版本号 / 目标环境 / 发布时间 / 发布者 / 软件名 | — |
| **2. 打包** | 3 种打包方式 | 2.1 软件包(tar.gz)/ 2.2 目录(rsync)/ 2.3 镜像(Docker) |
| **3. 获取成果物** | 列出本版本发布物 | — |
| **4. 上传服务器** | scp / sha256 校验 | — |
| **5. 初始化系统** | 4 步 | 5.1 环境准备 / 5.2 DB 建表 / 5.3 DB 初始化 / 5.4 配置修改 |
| **6. 启动运行** | systemd + 3 种其他方式 | — |
| **7. 首次进入软件系统** | URL / 默认账号 / 首次操作 | — |
| **8. 验证清单** | 15 项 checkbox | — |
| 附录 | 发布后通知(可选) | — |

#### 3.3 Placeholder 集合(14 种)

| Placeholder | 出现位置 | 自动/用户 |
| --- | --- | --- |
| `<本版本号>` | H1 标题 + §1 概述 | **自动**(`code-publish` 替换) |
| `<生产 / 预发 / 测试>` | §1 | 用户 |
| `<YYYY-MM-DD>` | §1 | 用户 |
| `<执行部署的人员>` | §1 | 用户 |
| `<你的软件名>` | §1 | 用户 |
| `<source_dir>` / `<output>` | §2 打包所有子节 | 用户 |
| `<image_name>` / `<version>` | §2.3 镜像 | 用户 |
| `<user>` / `<server>` / `/path/to/dest/` | §4 上传 | 用户 |
| `<DB 脚本路径>` / `<server_path>` / `<dbname>` | §5.2/5.3 | 用户 |
| `<user>` / `<passwd>`(数据库) | §5.2/5.3 | 用户 |
| `<环境依赖>`(隐含在 `apt install -y <runtime-package-name>`) | §5.1 | 用户 |
| `<配置文件路径>` + `<key>` / `<value>` | §5.4 | 用户 |
| `<启动命令>`(隐含在 `systemctl start <service-name>`) | §6 | 用户 |
| `<首次访问 URL>`(实现为 `<http://server:port>`,拆为 `<server>` + `<port>`) | §7 | 用户(更细粒度) |
| `<admin / root / ...>` / `<...>`(默认密码) | §7 | 用户 |

#### 3.4 默认示例清单(每章节至少 1 个,AC-3.2)

| 章节 | 默认示例 |
| --- | --- |
| 2.1 | `tar -czf <output>.tar.gz <source_dir>` + `sha256sum` 校验 |
| 2.2 | `rsync -avz --delete <source_dir>/ <user>@<server>:/path/to/dest/` |
| 2.3 | `docker build -t <image_name>:<version> .` + `docker save` |
| 4 | `scp <output>.tar.gz <user>@<server>:/path/to/dest/` + `sha256sum -c` 校验 |
| 5.1 | `sudo apt install -y <runtime-package-name>` + `sudo dnf install` |
| 5.2 | `mysql -u<user> -p<passwd> <dbname> < <server_path>/db/schema.sql` |
| 5.3 | `mysql -u<user> -p<passwd> <dbname> < <server_path>/db/init-data.sql` |
| 5.4 | `/etc/myapp/config.yaml`(路径示例)+ 3 项修改项示例 |
| 6 | `systemctl start myapp; systemctl status myapp` + 3 种替代方式 |
| 7 | `http://192.168.1.100:8080` URL 示例 |
| 8 | 15 项 checkbox 全部含"期望行为描述" |

#### 3.5 文首"使用说明"段(AC-3.3)

```markdown
> ⚠ **本手册为通用发布部署骨架**,由 `code-publish` 技能从 `plugins/code-skills/skills/code-publish/templates/DEPLOY.md` 复制生成。
>
> **请先手动补全所有 `<placeholder>`(除 `<本版本号>` 外),再按本手册的步骤执行部署。**
>
> 本手册**默认提供"最常见部署方式"的占位示例**(tar.gz 打包 + systemd 启动 + MySQL 数据库);若你的软件形态不同(目录/镜像/Python/Java/...),请按需调整各章节示例。
```

#### 3.6 与 `code-publish` 技能的集成

- **`<本版本号>` 自动替换**:由 `code-publish` 技能在 `Write ./assistants/<版本号>/publish/DEPLOY.md` 时直接渲染(详 SKILL.md 步骤 2.3)
- **其他 placeholder 保留**:用户必须手动补全
- **覆盖安全**:每次重跑 `code-publish` 都会覆盖 publish/DEPLOY.md(但**不**覆盖 templates/DEPLOY.md — 后者是源)

## 4. 关键决策与权衡

| # | 决策 | 选定 | 理由 |
| --- | --- | --- | --- |
| IT-1 | H1 标题格式 | `# 发布部署手册 — <本版本号>` | `code-publish` 替换后一目了然 |
| IT-2 | 2 节 3 子节 | 软件包 / 目录 / 镜像 | 互斥但常见,用户按需选 |
| IT-3 | 5 节 4 子节 | 环境/DB 建表/DB 初始化/配置 | 首次部署 4 步几乎必备 |
| IT-4 | SQL 段加注释行 | `-- <建表语句路径>:...` | 提示用户"替换路径" |
| IT-5 | 6 节默认 systemd | `systemctl start myapp` | Linux 主流;最常见 |
| IT-6 | 8 节用 Markdown checkbox | `- [ ] ...` | GitHub/IDE 可勾选;可复制为 issue 模板 |
| IT-7 | 不预设目标环境/软件名 | `<...>` / `myapp`(仅作示例) | NFR-5 通用性 |
| IT-8 | 模板聚焦"最常见" | 不写 HTTPS/防火墙/负载均衡等 | AC-3.2 已满足"每节 ≥ 1 示例" |

## 5. 偏离设计/规范的地方

详 `deviations.md`。**0 项与设计冲突的偏离**,3 项实现细节细化/增量:

- 偏离 1(细化):`<首次访问 URL>` 拆为 `<server>:<port>`(粒度优化)
- 偏离 2(增量):附录"发布后通知"(可选)
- 偏离 3(细化):6 节提供 3 种"其他启动方式"补充

## 6. 验证结果(详 `compile-and-run.md`)

| 验证项 | 结论 |
| --- | --- |
| 模板路径合规 | ✓ `plugins/.../templates/DEPLOY.md` |
| 8 大章节齐全 | ✓ |
| 子章节完整 | ✓ 7 个子节 |
| 文首"使用说明" | ✓ |
| placeholder 集合 | ✓ 14 种 |
| 默认示例每节 ≥ 1 | ✓ |
| 验证清单 checkbox | ✓ 15 个 |
| `module-conventions §规则 1` | ✓ |
| 0 修改既有 | ✓ |

## 7. 已知问题/未完成项

### 已知问题
- **无**

### 未完成项(由后续任务承接)
- **T-003**(UPDATE.md):结构与 DEPLOY 相似 + §8 回滚为新增
- **T-004**(Q&A.md):占位模板
- **T-005**(qanda-README.md):qanda 目录说明
- **T-006**(assistants-layout.md):工作目录约定
- **T-007**:端到端验证 + 不变量自检
- **Q-D-1**(留 v2):`code-publish` 注册到 marketplace.json
- **Q-D-3 ~ Q-D-7**(留 code-review / 其他 REQ)

## 8. 关联任务与提交

- **关联原任务**:无
- **关联后续任务**:T-003, T-004, T-005, T-006, T-007, T-008
- **Git 提交**:**未提交**(遵循 NFR-3 + 沿用 V0.0.0~V0.0.1 实践)

## 9. 步骤 14 状态更新(PLAN.md)

| 字段 | 旧值 | 新值 |
| --- | --- | --- |
| 开发状态 | 进行中 | **已完成** |
| 完成时间 | — | 2026-06-04 17:34 |
| 完成人 | — | wangmiao |
| 涉及文件 | (空) | `plugins/code-skills/skills/code-publish/templates/DEPLOY.md`(245 行,~10 KB) |
| 提交哈希 | (空) | (不提交) |

## 10. 下一步建议

1. **下一任务**:`/code-skills:code-it TASK-REQ-00006-00003`(UPDATE.md 模板,与本任务结构相似,0.3d)
2. **可并行**:`/code-skills:code-it TASK-REQ-00006-00004` / `00005` / `00006` / `00008`(4 任务独立,共 ~1.0d)
3. **收尾**:`/code-skills:code-it TASK-REQ-00006-00007`(不变量自检 + 端到端 3 场景)
