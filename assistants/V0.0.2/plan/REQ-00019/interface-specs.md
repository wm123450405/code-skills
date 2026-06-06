# 接口详细规格 — REQ-00019
版本:V0.0.2

## 接口:`code-plan` 步骤 28A+1 — 同步版本看板'任务清单'区段(本需求新增)

- **形式**:函数 / 章节(非 RESTful,文档内函数)
- **路径/签名**:
  ```
  ### 步骤 28A+1 — 同步版本看板'任务清单'区段(本需求 REQ-00019 新增,2026-06-06 起生效)
  ```
- **入参**:
  ```
  {
    "fix_dir_path": "./assistants/<version>/fix/<BUG-NNN>/",
    "plan_file": "./assistants/<version>/fix/<BUG-NNN>/PLAN.md",
    "board_path": "./assistants/<version>/RESULT.md",
    "task_overview_rows": [
      {
        "task_num": "TASK-BUG-NNNNN-NNNNN",
        "req": "BUG-NNN",
        "type": "修复",
        "trigger_source": "缺陷修复",
        "title": "<截断后的任务标题>",
        "dev_status": "待开始",
        "test_status": "不适用",
        "files": "",
        "completed_at": "",
        "commit_hash": "",
        "related_task": "BUG-NNN"
      }
    ]
  }
  ```
- **出参**:
  ```
  {
    "code": 0,
    "data": {
      "appended_rows": <N>,
      "board_path": "./assistants/<version>/RESULT.md"
    }
  }
  ```
- **错误码**:无(纯文档写入)
- **示例**:
  - 正常:`fix/BUG-00010/PLAN.md` 任务总览 1 条 `TASK-BUG-00010-00001` → 看板"任务清单"区段追加 1 行
  - 异常:无
- **版本策略**:本需求后所有新 BUG 适用(FR-3 NFR-3.1)
- **兼容策略**:沿用既有 12 列字段(0 新增字段)
- **依据规范**:`dashboard-conventions §规则 1`(0 触发)

## 接口:`code-it` 步骤 17 — 校验缺陷与修复方案存在(本需求修订)

- **形式**:函数 / 章节(非 RESTful,文档内函数)
- **路径/签名**:
  ```
  ### 步骤 17 — 校验缺陷与修复方案存在(本需求 REQ-00019 修订,2026-06-06 起生效)
  ```
- **入参**:
  ```
  {
    "fix_dir_path": "./assistants/<version>/fix/<BUG-NNN>/",
    "result_file": "./assistants/<version>/fix/<BUG-NNN>/RESULT.md",
    "plan_file": "./assistants/<version>/fix/<BUG-NNN>/PLAN.md"
  }
  ```
- **出参**:
  ```
  {
    "code": 0,  // 校验通过
    "data": {
      "bug_state": "修复规划中 | 修复编码中",
      "plan_task_count": <N>,
      "design_points": ["算法", "数据结构", "接口", "异常处理", "风险与回退"]
    }
  }
  ```
- **错误码**:
  - 缺 `RESULT.md` → "请先调 `code-fix <缺陷编号>` 登记缺陷"
  - 缺 `PLAN.md` → "请先调 `code-plan <缺陷编号>` 规划修复方案"
  - 状态不符(报告/调查中)→ 提示用户
- **示例**:
  - 正常:`fix/BUG-00010/PLAN.md` + `RESULT.md` 都存在 → 进入步骤 18
  - 异常 1:缺 `RESULT.md` → "请先调 `code-fix <缺陷编号>` 登记缺陷"
  - 异常 2:缺 `PLAN.md` → "请先调 `code-plan <缺陷编号>` 规划修复方案"
  - 异常 3:状态不符(报告/调查中)→ 提示用户:当前状态是 X,需要先 `code-fix` 推进到 `修复规划中` / `修复编码中`
  - 异常 4(E-7):`fix-plan.md` 存在 + `PLAN.md` 缺失 → 退化 + 提示
- **版本策略**:本需求后所有新 BUG 适用
- **兼容策略**:保留既有 3 类失败信息

## 接口:`code-it` frontmatter description 段(本需求修订)

- **形式**:YAML frontmatter 字段
- **路径/签名**:`plugins/code-skills/skills/code-it/SKILL.md` L5
- **入参**:无(纯文本字段修订)
- **出参**:
  - 变更前:
    ```
    - **缺陷编号**(格式 `BUG-NNNNN`,如 `BUG-00001`):所有产出物写入 `./assistants/<版本号>/fix/<缺陷编号>/`(以 `fix-` 前缀命名的过程文档),从 `./assistants/<版本号>/fix/<缺陷编号>/RESULT.md` 读取缺陷详情,从 `./assistants/<版本号>/fix/<缺陷编号>/fix-plan.md` 读取修复方案
    ```
  - 变更后:
    ```
    - **缺陷编号**(格式 `BUG-NNNNN`,如 `BUG-00001`):所有产出物写入 `./assistants/<版本号>/fix/<缺陷编号>/`(主详细设计 `RESULT.md` + 任务列表 `PLAN.md`,沿用 REQ 路径同构产出),从 `./assistants/<版本号>/fix/<缺陷编号>/RESULT.md` 读取缺陷详情,从 `./assistants/<版本号>/fix/<缺陷编号>/PLAN.md` 读取修复任务列表
    ```
- **版本策略**:本需求后所有新 BUG 适用
