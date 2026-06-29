# 关联需求 — REQ-00041

## REQ-00034 (code-it 模块识别,版本 V0.0.3)
- **关联点**:步骤 8a.0 模块识别逻辑(8 套 monorepo 声明文件解析 + 6 类语言描述文件检测)与本需求 FR-1 语言检测高度重叠
- **影响**:本需求实施时需整合 REQ-00034 的模块识别逻辑,将语言检测部分统一到 references 中;REQ-00034 的 8 套声明文件解析可复用为 references 文档内容
- **来源**:扫描 ./assistants/V0.0.3/require/REQ-00034/RESULT.md

## REQ-00018 (code-version CWD 描述文件同步,版本 V0.0.2)
- **关联点**:6 类工程描述文件清单(package.json / pom.xml / manifest.json / Cargo.toml / pyproject.toml / go.mod)与本需求 FR-4 的 6 类语言识别清单重合
- **影响**:本需求的语言检测可复用 REQ-00018 的描述文件识别逻辑;REQ-00018 的 5 类屏幕输出契约可参考
- **来源**:扫描 ./assistants/V0.0.2/require/REQ-00018/RESULT.md