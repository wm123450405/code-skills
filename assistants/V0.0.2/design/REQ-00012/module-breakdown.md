# 模块拆分 — REQ-00012
更新时间:2026-06-05
版本:V0.0.2

## 新增模块(2 个文档)
| 模块名 | 路径 | 职责 | 规范依据 |
| --- | --- | --- | --- |
| 根 README(中文) | `./README.md` | 仓库门面:简介 + 快速开始 + 主要能力 + 详细文档链 + 许可证 | `doc-conventions §规则 1 / §规则 2`(主动) |
| 根 README(英文) | `./README.en.md` | 英文版,与中文版章节对仗 | `doc-conventions §规则 1` |

## 移动模块(1 个文档)
| 模块名 | 路径(原 → 新) | 职责 | 备注 |
| --- | --- | --- | --- |
| CLAUDE.md | `plugins/code-skills/CLAUDE.md` → `./CLAUDE.md` | Claude Code 自动读取的指引 | `git mv` 保留 blame;原位置不保留(FR-3 AC-3.3) |

## 复用既有模块(2 个文档,**不**修改)
| 模块名 | 路径 | 职责 | 规范依据 |
| --- | --- | --- | --- |
| 详细 README(中文) | `plugins/code-skills/README.md` | 详细技能文档(38,247 bytes) | NFR-4 不破坏 |
| 详细 README(英文) | `plugins/code-skills/README.en.md` | 详细技能文档英文版(41,949 bytes) | NFR-4 不破坏 |

## 删除模块(1 个文档位置)
| 位置 | 状态 | 依据 |
| --- | --- | --- |
| `plugins/code-skills/CLAUDE.md` | 移动后**不保留** | FR-3 AC-3.3 + NFR-8(不提供重定向) |
