# 数据结构完整变更 — REQ-00020
版本:V0.0.3

## 新增实体:无

- 本需求**0**新增实体

## 修改实体:"## 设计目标"小节结构

- 字段变更(扩展 4 维度 → 7 维度):
  - 原:4 维度(`functionality` / `extensibility` / `robustness` / `maintainability`)
  - 新:7 维度(+ `encapsulation` / `reusability` / `readability`)
  - 维度选项扩展:`高 / 中 / 低` → `高 / 中 / 低 / 不适用`(本需求新增"不适用"选项)
- 索引变更:无
- 迁移需求:无(本需求 0 引入新存储)

## 详细结构(扩展后)

```ts
{
  writeTime: string,         // "YYYY-MM-DD HH:mm"
  writeTrigger: "code-design" | "code-plan"
  overallGoal: "--minimal" | "--extensible" | "--balanced"
  dimensionPriority: {
    functionality: "高" | "中" | "低",
    extensibility: "高" | "中" | "低",        // 沿用 REQ-00011
    robustness: "高" | "中" | "低",           // 沿用 REQ-00011
    maintainability: "高" | "中" | "低",       // 沿用 REQ-00011
    encapsulation: "高" | "中" | "低" | "不适用",  // 本需求新增
    reusability: "高" | "中" | "低" | "不适用",    // 本需求新增
    readability: "高" | "中" | "低" | "不适用"     // 本需求新增
  }
}
```

## 依据规范

- 沿用 REQ-00011 "## 设计目标"小节结构
- 本需求扩展 3 维度(FR-2)
