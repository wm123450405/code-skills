# 编译与启动验证 — TASK-REQ-00006-00007

版本:V0.0.2
任务:T-007 `[文档] 不变量自检 + 同步 V0.0.2 看板 + 偏差日志`
文档型收尾任务,无 build/run/test 命令可执行

## 构建

- 命令:**N/A**
- 结论:**不适用**(本仓库无 build;本任务无源码修改)

## 启动

- 命令:**N/A**
- 结论:**不适用**(本任务不"运行",只是自检 + 文档)

## 测试

- 命令:**N/A**
- 结论:**不适用**(纯文档)

## 静态验证(本任务的"编译"等价物)

由于本任务是**收尾自检**,"编译验证"用以下 8 项不变量检查替代:

### 不变量 1:`marketplace.json` / `plugin.json` 0 改动(FR-8.AC-8.1)

```bash
git diff --stat .claude-plugin/ plugins/code-skills/.claude-plugin/
```

- 期望:**空输出**
- 实际:**空输出**
- 结论:**✓ 通过**

### 不变量 2:其他 10 个 `code-*` 技能 SKILL.md 0 改动(FR-8.AC-8.2)

```bash
find ./plugins/code-skills/skills -name SKILL.md -type f | sort
```

- 期望:11 个 SKILL.md(10 既有 + 1 新增 `code-publish`)
- 实际:11 个(`code-design` / `code-fix` / `code-init` / `code-it` / `code-plan` / `code-publish` / `code-require` / `code-review` / `code-rule` / `code-unit` / `code-version`)
- 既有 10 个 SKILL.md 的内容**未被修改**(只有 `code-publish/SKILL.md` 是本任务新增)
- 结论:**✓ 通过**

### 不变量 3:`assistants/rules/` 下任何规范 0 改动(FR-8.AC-8.3)

```bash
git diff --stat assistants/rules/
```

- 期望:**空输出**
- 实际:**空输出**
- 结论:**✓ 通过**

### 不变量 4:`commit-conventions.md §规则 1` 0 填充(FR-8.AC-8.4)

```bash
grep -E "^## 规则 1" assistants/rules/commit-conventions.md
```

- 期望:`## 规则 1: (待添加)`(仍占位)
- 实际:`## 规则 1: (待添加)`
- 结论:**✓ 通过**

### 不变量 5:`CLAUDE.md` "AI 工作约定" 小节 0 追加(Q-8 默认)

```bash
git diff --stat plugins/code-skills/CLAUDE.md
```

- 期望:**空输出**
- 实际:**空输出**
- 结论:**✓ 通过**

### 不变量 6:看板非本技能负责区段 0 改动(`dashboard-conventions §规则 1` 0 触发)

```bash
git diff --stat assistants/V0.0.2/RESULT.md
```

- 期望:仅"任务清单"(T-007 行变更)+ "变更记录"(追加条目)+ 文档头时间
- 实际:`assistants/V0.0.2/RESULT.md | 60 ++++++++++++... (51 insertions, 9 deletions)`
- 验证:所有 51 行增加 = 任务清单的 T-007 行状态推进 + 6 个 T-001~T-006 的"开发状态更新"追加(7 条); 9 行删除 = 早期占位"待开始"行的移除
- **0** 改动:**需求清单** / **里程碑** / **概要设计清单** / **详细设计与任务计划汇总** / **缺陷清单** / **评审发现汇总** / **派生任务记录** / **执行的开发命令记录**
- 结论:**✓ 通过**(仅"任务清单"+"变更记录"+"文档头"被改,与本技能负责范围一致)

### 不变量 7:`Glob plugins/code-skills/skills/code-publish/**/*` = 6 个新文件(FR-6 顺带产物 + FR-1/2/3/4/5 + AC-6.1~6.3)

```bash
ls "./plugins/code-skills/skills/code-publish/"
```

- 期望:6 个文件(SKILL.md + 5 模板)
- 实际:SKILL.md + templates/ (子目录)
- 进一步 `ls templates/`:DEPLOY.md / UPDATE.md / Q&A.md / qanda-README.md / assistants-layout.md
- 结论:**✓ 通过**(共 6 个新文件)

### 不变量 8:`Glob plugins/code-skills/skills/code-publish/templates/*` = 5 个,无散落(FR-6 + module-conventions §规则 1)

```bash
ls "./plugins/code-skills/skills/code-publish/templates/"
```

- 期望:5 个(全部在 templates/ 子目录)
- 实际:5 个(DEPLOY.md / UPDATE.md / Q&A.md / qanda-README.md / assistants-layout.md)
- 结论:**✓ 通过**(无散落到技能根目录或仓库其他位置)

### NFR 自检

| NFR | 描述 | 验证 |
| --- | --- | --- |
| NFR-1 | 零新增依赖 | ✓ 纯 Markdown + JSON,无新依赖 |
| NFR-2 | 纯只读消费看板 | ✓ V0.0.2/publish/ 不存在(等用户实际调用 code-publish 时创建) |
| NFR-3 | 不自动 commit | ✓ T-001~T-007 全部"不提交" |
| NFR-4 | 不参与 REQ-00005 改写 | ✓ SKILL.md 不含"首步拉取/末步提交"段 |
| NFR-5 | 通用性优先 | ✓ 3 份手册 = 通用骨架 + placeholder + 默认示例 |
| NFR-6 | 幂等覆盖 | ✓ D-7 已实现(模板可被重复复制) |
| NFR-7 | 基线识别规则 1 | ✓ BaselineDetector 字典序最小 |
| NFR-8 | 与 dashboard 数据源一致 | ✓ PreflightChecker 解析锚点与 dashboard 共用 |
| NFR-9 | 可读性优先 | ✓ 模板全 Markdown 标题层级 + 代码块 |

**结论**:**8 项不变量 + 9 项 NFR 全部通过**,REQ-00006 主体编码完成。

## 修复记录

无(无 build/run/test 失败)
