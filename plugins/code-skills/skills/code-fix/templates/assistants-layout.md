# 目录结构 — code-fix

本技能在 `./assistants/<版本号>/fix/` 下创建/维护以下结构:

```
<当前工作目录(CWD)>/
└── assistants/
 └── <版本号>/
 ├── RESULT.md # 版本看板(本技能追加"缺陷清单" / "变更记录")
 └── fix/ # ★ 本技能维护的缺陷工作空间
 ├── RESULT.md # ★ 缺陷总览(本技能首次/追加)
 ├── BUG-00001/ # 第一个缺陷
 │ ├── RESULT.md # ★ 缺陷详情(本技能首次/更新)
 │ ├── investigation.md # 调查笔记(可选)
 │ ├── fix-plan.md # 修复方案(由 code-plan 写入)
 │ ├── fix-work-log.md # 实施日志(由 code-it 写入)
 │ ├── fix-compile-and-run.md # 编译/运行(由 code-it 写入)
 │ ├── fix-test-results.md # 测试结果(由 code-it 写入)
 │ └── deviations.md # 偏离记录(由 code-it 写入)
 ├── BUG-00002/
 │ └── ...
 └── ...
```

## 关键约束

- 本技能**只**操作 `./assistants/<版本号>/fix/` 下的文件
- 本技能**只**修改 `./assistants/<版本号>/RESULT.md` 的"缺陷清单" / "变更记录"区段
- 本技能**不**触碰项目源代码、`rules/`、其他 `code-*` 技能负责的文件
- 实际修复代码改动由 `code-plan <BUG-NNNNN>` + `code-it <BUG-NNNNN>` 完成,本技能**不**调用它们

## 文件名约定

- `BUG-NNNNN`:`BUG-` 前缀 + 五位数字,从 `00001` 起递增
- `RESULT.md`:缺陷详情(由本技能维护)与缺陷总览(由本技能维护)同名但位于不同层级
- `fix-plan.md` / `fix-work-log.md` 等:以 `fix-` 前缀与主流程的 `work-log.md` 等区分(避免和 `code/<任务>/work-log.md` 冲突)
- `investigation.md` / `deviations.md`:与主流程同名约定保持一致
