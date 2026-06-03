# 工作目录布局参考 — code-require(版本感知)

> `code-require` 技能强制约定。所有路径以**当前工作目录(CWD)**为基准。
> 本技能受 `code-version` 管理,实际工作空间 = `./assistants/<版本号>/`(由 `./assistants/.current-version` 决定)。

## 整体布局
```
<项目根目录>/
└── assistants/
    ├── rules/                          ← 项目级规范(只读,跨版本共享)
    │   └── ...
    ├── .current-version                ← 当前激活版本标记
    │   (内容示例:v1.0.0)
    └── <版本号>/                       ★ 版本工作空间
        ├── RESULT.md                   ← 版本开发进度看板(code-version 初始化,本技能追加"需求清单"区段)
        └── require/                    ← 本技能的目录粒度
            ├── REQ-2026-0001/
            │   ├── prd-v1.md              # ← 用户放置
            │   ├── design-login.png       # ← 用户放置
            │   ├── design-home.png        # ← 用户放置
            │   ├── meeting-0512.md        # ← 用户放置
            │   ├── demo.mp4               # ← 用户放置
            │   ├── recording-0515.m4a     # ← 用户放置
            │   ├── RESULT.md              # 技能产出
            │   ├── materials-index.md     # 技能产出
            │   ├── clarifications.md      # 技能产出
            │   ├── related-requirements.md# 技能产出
            │   └── analysis-notes.md      # 技能产出(可选)
            ├── REQ-2026-0002/
            │   └── ...
            └── REQ-2025-0099/
                └── ...
```

## 命名建议
- 版本号:由 `code-version` 设定(推荐 semver 如 `v1.0.0` 或日期如 `2026-Q2`)
- 需求编码:`REQ-YYYY-NNNN`(可由用户自定义)
- 原始材料:用文件内容相关的名字,如 `prd-v1.md` / `design-login.png`,**避免**命名为 `需求文档.md` 这种无信息量名字
- 技能产出物文件名固定:`RESULT.md` / `materials-index.md` / `clarifications.md` / `related-requirements.md` / `analysis-notes.md`

## 用户 vs 技能产出
| 类别 | 写入方 | 修改方 |
| --- | --- | --- |
| 原始材料(文档/设计稿/音视频等) | 用户 | 用户 |
| `RESULT.md` | 技能 | 技能(增量更新) |
| 过程文档(materials-index 等) | 技能 | 技能 |
| `<版本号>/RESULT.md`(看板) | code-version 初始化;本技能追加区段 | 只能追加,不能重写 |
| `./assistants/.current-version` | code-version | code-version |

> 用户不应手动改 `RESULT.md`,如有调整请追加材料并重新触发技能。

## 多项目隔离
不同项目的 `assistants/` 完全独立:
- 在项目 A 下调用,材料在 `A/assistants/<版本号>/require/`
- 在项目 B 下调用,材料在 `B/assistants/<版本号>/require/`
- 互不污染,跨项目不会误检索到对方的需求

## 跨需求检索
技能会扫描 `./assistants/<版本号>/require/*/RESULT.md` 寻找关联需求(同版本);
可选:跨版本扫描 `./assistants/*/require/*/RESULT.md`(需用户授权)。
为保证检索质量,建议:
- `RESULT.md` 中明确写出"关联需求"章节(见 templates/requirements.md §11),若跨版本则注明所在版本
- 关键功能名/接口名/字段名在 `RESULT.md` 中保持一致命名,避免同义词导致检索失败

