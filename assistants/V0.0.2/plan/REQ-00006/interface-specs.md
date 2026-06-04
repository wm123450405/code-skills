# 接口详细规格 — REQ-00006

更新时间:2026-06-04 17:01
版本:V0.0.2

本技能的"接口"是 Claude Code 协议的 CLI 接口(用户输入),以及内部模块的"函数接口"(SKILL.md 自然语言指令中的"调用关系")。

## 1. CLI 接口

### 接口 1:`/code-publish`(空参,默认当前版本)

- **形式**:Claude Code 协议触发(`/code-publish`)
- **路径/签名**:`/code-publish`
- **入参**:无
- **出参**(stdout):多行纯文本报告(见接口 3)+ 文件系统副作用
- **副作用**:
  - 写入:`./assistants/<.current-version>/publish/DEPLOY.md` + `UPDATE.md`(非基线) + `Q&A.md`
  - 可能写入:`./assistants/qanda/` + `README.md`(若不存在)
- **错误码**(实际是退出行为):
  - 无 `.current-version` → 文本提示 + 不写任何文件
  - `<版本号>/RESULT.md` 不存在 → 文本提示 + 不写
  - 看板缺区段 → 不通过分支(不写手册)
  - 前置检查不通过 → 不通过分支(不写手册)
  - publish/ 写入失败 → 报错 + 退出(无半成品)
- **示例**:
  - 正常(可发布):见 needs §S-1 样例输出
  - 异常(不通过):见 needs §S-2 样例输出
  - 基线版本:见 needs §S-3 样例输出
  - qanda 空:见 needs §S-4 样例输出
- **版本策略**:v1(本次)
- **兼容策略**:v2 可加 `--force` / `--auto-commit` 参数,本接口的"无参"行为保持向后兼容
- **依据规范**:`skill-conventions.md §规则 1`(SKILL.md frontmatter)

### 接口 2:`/code-publish <版本号>`(显式版本)

- **形式**:同上
- **路径/签名**:`/code-publish <版本号>`,如 `/code-publish V0.0.0`
- **入参**:1 个位置参数 = 版本号字符串
- **出参**:同接口 1
- **副作用**:写入 `./assistants/<版本号>/publish/...`(替代 `.current-version`)
- **错误码**:
  - 同接口 1 + `<版本号>/RESULT.md` 不存在 → 文本提示
- **示例**:`/code-publish V0.0.0` → S-3 基线场景
- **版本策略**:同上
- **兼容策略**:同上
- **依据规范**:同上

### 接口 3:报告输出格式(stdout)

#### 通过场景

```
✓ 发布前置检查通过(需求 N/N, 任务 M/M, 缺陷 0/0)

已生成 3 份手册:
  - assistants/<版本号>/publish/DEPLOY.md  (全新部署)
  - assistants/<版本号>/publish/UPDATE.md  (从 <源版本> 升级)
  - assistants/<版本号>/publish/Q&A.md     (常见问题)

[若已覆盖]
⚠ 已覆盖 N 个文件:[file1, file2, ...]

⚠ 提示: 3 份手册均为通用骨架,请手动补全 <软件名>、<版本号>、<服务器地址> 等占位符
⚠ 提示: 本技能不自动提交,补全后请手动 git add + commit
```

#### 不通过场景

```
✗ 发布前置检查未通过

未完成项明细:
  - [需求] REQ-NNNNN <标题> 状态=<当前>(应该=已完成)
  - [任务] TASK-REQ-NNNNN-NNNNN <标题> 开发状态=<当前>(应该=已完成)
  - [任务] TASK-REQ-NNNNN-NNNNN <标题> 测试状态=<当前>(应该 ∈ {已运行-通过, 不适用})
  - [缺陷] BUG-NNNNN <标题> 状态=<当前>(应该=已修复)

阻塞统计:
  - 需求:N / N 未完成
  - 任务:M / M 未完成
  - 缺陷:K / K 未修复

✗ 未生成任何手册。请先解决上述项后重试。
```

#### 基线场景

```
✓ 发布前置检查通过(本版本 <版本号> 是基线)

已生成 2 份手册(基线无 UPDATE.md):
  - assistants/<版本号>/publish/DEPLOY.md
  - assistants/<版本号>/publish/Q&A.md

⚠ 提示同上
```

#### qanda 空场景

```
✓ 发布前置检查通过(...)

已生成 3 份手册(...)

⚠ assistants/qanda/ 目录为空(仅有 README.md),Q&A.md 仅为占位
请先在 assistants/qanda/ 中添加 Q&A 内容,再重跑 code-publish
```

#### 无版本场景

```
✗ 未检测到激活版本(./assistants/.current-version 不存在)
请先调 /code-version <版本号> 创建或切换版本。
```

## 2. 内部模块函数接口

### PreflightChecker.preflight_check
- **入参**:`version_number: str`
- **出参**:
  ```
  PreflightResult {
    passed: bool,
    reason: str? (失败原因,仅 board 不存在/缺区段时填),
    undone: [UncompletedItem],
    stats: {
      需求: {总: int, 未完成: int, 状态分布: dict},
      任务: {总: int, 未完成: int, 状态分布: dict},
      缺陷: {总: int, 未完成: int, 状态分布: dict},
    }
  }
  ```
- **异常**:不抛(用 PreflightResult.passed=false 表达)

### BaselineDetector.detect_baseline
- **入参**:`target_version: str`
- **出参**:
  ```
  BaselineResult {
    is_baseline: bool,
    previous_version: str?,
    all_versions_sorted: [str],
  }
  ```
- **异常**:`target_version` 不在所有版本列表中 → 报错 + 退出(严重不一致)

### ManualBuilder.build_manuals
- **入参**:`version_number: str, baseline_result: BaselineResult`
- **出参**:
  ```
  ManualBuildResult {
    written: [str],         // 写入文件路径列表
    overwritten: [str],     // 覆盖文件路径列表
    skipped: [str],         // 跳过的文件(如基线时的 UPDATE.md)
  }
  ```
- **异常**:mkdir/Write 失败 → 报错 + 退出(不留半成品)

### QandaScaffolder.scaffold_qanda
- **入参**:无
- **出参**:
  ```
  QandaScaffoldResult {
    status: '已存在' | '本次创建' | '创建失败',
    error_msg: str?,
  }
  ```
- **异常**:不抛(用 status 表达)

### QandaAggregator.aggregate_qanda
- **入参**:无
- **出参**:`{content: str, source_files: [str], warnings: [str]}`
  - `content`:渲染后的 Q&A.md 完整字符串
  - `source_files`:聚合的文件列表(0 ~ N)
  - `warnings`:每个失败读取的文件警告
- **异常**:不抛

### ReportFormatter.format_report
- **入参**:`preflight_result, baseline_result, manual_result, qanda_result`
- **出参**:多行文本字符串(直接 stdout)
- **异常**:不抛

## 3. 关键决策

- **鉴权方式**:不适用(本机文件 IO,无网络)
- **错误码体系**:无数字错误码,全部用文本报告 + 是否生成文件作为"成功/失败"信号
- **限流策略**:不适用
- **幂等保证**:NFR-6 + DD-8;3 份手册内容字节级幂等(只要看板内容不变)
- **链路追踪字段**:不适用

## 4. 依据规范
- `skill-conventions.md §规则 1`(SKILL.md frontmatter)
- 无 API 规范文件(本项目无 API 接口)
