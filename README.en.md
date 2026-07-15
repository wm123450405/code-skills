# code-skills

> A suite of Claude Code skills for AI-assisted software development lifecycle management (based on Claude Code).

## Introduction

`code-skills` is a set of Claude Code skills covering the full development cycle from requirements analysis to code review, with built-in version-aware workspace management.

## Quick Start

1. Add the marketplace:
   ```
   claude plugin marketplace add https://github.com/wm123450405/code-skills.git
   ```
2. Install the plugin:
   ```
   claude plugin install code-skills@code-skills-marketplace
   ```
3. Invoke skills in your project:
   ```
   /code-ver              ← Initialize project, create version (or view progress)
   /code-req "your req"   ← Start requirement development
   /code-fix "bug desc"   ← Fix a bug
   ```

## Skill Overview

| Skill | Purpose |
| --- | --- |
| `code-ver` | Version Management & Dashboard — init, switch version, publish, view progress |
| `code-req` | Requirement Development — full lifecycle from analysis to code review |
| `code-fix` | Bug Fix — full lifecycle from registration to fix review |
| `code-faq` | Knowledge Base — cross-version query with document export |
| `code-rule` | Coding Standards — describe standards in natural language |
| `code-merge` | Branch Merge — merge worktree changes back to main |

## 📖 Detailed Documentation

Full skill descriptions, installation details, and usage guide: [./plugins/code-skills/README.md](./plugins/code-skills/README.md)

## License

[MIT](LICENSE)