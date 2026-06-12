# 模块详细化 — REQ-00032

更新时间:2026-06-12 16:40
版本:V0.0.3

## 模块 1:code-require 屏幕日志建议段(步骤 10A 内)

- **路径**:`plugins/code-skills/skills/code-require/SKILL.md` > §步骤 10A 段内文末
- **状态**:修改既有(纯追加,字节级保留既有"向用户汇报"段)
- **职责**:在 code-require 首次分析完成后,屏幕输出"下一步建议"
- **与概要设计的对应**:design/REQ-00032/RESULT.md §3.2 模块 1
- **符合的规范**:skill-conventions.md §规则 1(frontmatter L1-3 字节级保留)

### 内部结构

- 既有"### 步骤 10A — 完善过程文档"段标题保留
- 既有"向用户汇报:本次新增了哪些 FR/AC..."句子字节级保留
- **新增** 1 段"### 下一步建议(本需求 REQ-00032 新增,2026-06-12 起生效)"(在步骤 10A 段内文末)

### 关键类/函数(伪代码,本仓库无编程语言)

```
# 步骤 10A 末尾新增逻辑
determineIsTiny(materials, frs, acs)  # 见 §算法 1
is_tiny = determineIsTiny(materials, frs, acs)
outputNextStepSuggestion(is_tiny)    # 见 §算法 2
```

### 调用顺序

1. code-require 步骤 5A 提取候选需求 → 产出 `materials` / `frs` / `acs`
2. code-require 步骤 10A 既有"向用户汇报"段(0 改)
3. **新增** isTiny 判定 + 屏幕输出(步骤 10A 段内文末)
4. code-require 步骤 N 末尾兜底提交(0 改)

### 状态归属

- `isTiny`:本技能本轮内存变量,作用域 = 本轮 code-require 执行
- 不参与持久化 / 不写入 `RESULT.md`(FR-2 锁定)

## 模块 2:code-require 屏幕日志建议段(步骤 10B 内)

- **路径**:`plugins/code-skills/skills/code-require/SKILL.md` > §步骤 10B 段内文末
- **状态**:修改既有(纯追加,字节级保留既有"向用户汇报"段)
- **职责**:在 code-require 增量更新完成后,屏幕输出"下一步建议"
- **与概要设计的对应**:design/REQ-00032/RESULT.md §3.2 模块 2
- **符合的规范**:skill-conventions.md §规则 1(frontmatter L1-3 字节级保留)

### 内部结构

- 既有"### 步骤 10B — 汇报"段标题保留
- 既有"向用户汇报本次增量更新:..."段字节级保留
- **新增** 1 段"### 下一步建议(本需求 REQ-00032 新增,2026-06-12 起生效)"(在步骤 10B 段内文末)

### 关键类/函数(伪代码)

```
# 步骤 10B 末尾新增逻辑
determineIsTiny(materials_updated, frs_updated, acs_updated)  # 见 §算法 1
is_tiny = determineIsTiny(materials_updated, frs_updated, acs_updated)
outputNextStepSuggestion(is_tiny)                              # 见 §算法 2
```

### 调用顺序

1. code-require 步骤 5B 识别材料变更 → 产出 `materials_updated` / `frs_updated` / `acs_updated`
2. code-require 步骤 10B 既有"向用户汇报"段(0 改)
3. **新增** isTiny 判定 + 屏幕输出(步骤 10B 段内文末)
4. code-require 步骤 N 末尾兜底提交(0 改)

### 状态归属

- `isTiny`:本技能本轮内存变量,作用域 = 本轮 code-require 执行
- 不参与持久化 / 不写入 `RESULT.md`(FR-2 锁定)

## 算法 1:determineIsTiny(FR-1)

```python
def determineIsTiny(materials: list, frs: list, acs: list) -> bool:
    # 推荐判据(同时满足 → 微小)
    if len(materials) <= 1 and len(frs) <= 2 and len(acs) <= 5:
        return True
    # 强制排除
    if len(frs) >= 3:
        return False
    if len(acs) >= 6:
        return False
    # AI 综合判断(本判据中无法量化的部分)
    # 例如:"该需求在材料中明显跨多个模块" → False
    return ai_comprehensive_judgment(materials, frs, acs)


def determineIsTinySafe(materials, frs, acs) -> bool:
    """失败降级:异常 → False(走 /code-design 建议)"""
    try:
        return determineIsTiny(materials, frs, acs)
    except Exception:
        return False
```

### 边界

| 输入 | 输出 | 依据 |
| --- | --- | --- |
| materials=[], frs=[3], acs=[8] | False | FR ≥ 3 → False |
| materials=['doc.md'], frs=[2], acs=[5] | True | 推荐判据满足 |
| materials=[], frs=[], acs=[] | False | materials=0 → 退化 |
| materials=['doc.md', 'img.png'], frs=[2], acs=[5] | False | materials > 1 → 强制非微小 |
| 异常 | False | 退化(走 /code-design) |

## 算法 2:outputNextStepSuggestion(FR-3)

```python
def outputNextStepSuggestion(is_tiny: bool) -> None:
    if is_tiny:
        log("→ 下一步建议:本需求判定为\"微小需求\",建议直接执行 `/code-auto` 完成开发任务")
        log("  提示:code-auto 会自动跳过独立的概设/详设步骤,直接进入编码+评审流水线")
    else:
        log("→ 下一步建议:本需求判定为\"非微小需求\",建议先执行 `/code-design` 概设")
        log("  提示:概设完成后,code-plan → code-it → code-check 仍按既有主流程推进")
```

### 字符数校验(NFR-3)

| 路径 | 第 1 行字符数 | 第 2 行字符数 | 校验 |
| --- | --- | --- | --- |
| FR-3.1(微小) | 45 字 | 36 字 | ✅ ≤ 80 |
| FR-3.2(其他) | 45 字 | 36 字 | ✅ ≤ 80 |

### 路径串字节级保留(INV-10)

- `/code-auto`(FR-3.1):9 字符,1 个反引号包裹
- `/code-design`(FR-3.2):12 字符,1 个反引号包裹
- 中点 `→`(U+2192):1 字符
- 中文标点 `"..."` (U+201C / U+201D):1 字符
