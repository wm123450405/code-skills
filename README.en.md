# code-skills

> A suite of Claude Code skills for AI-assisted project management and development workflow.

## Introduction

`code-skills` is a set of Claude Code skills covering the full development cycle: requirements → design → planning → coding → unit tests → review → release.

## Quick Start

1. Add the marketplace:
   ```
   claude plugin marketplace add https://github.com/wm123450405/code-skills.git
   ```
2. Install the plugin:
   ```
   claude plugin install code-skills@code-skills
   ```
3. Invoke the first skill in your project:
   ```
   /code-version V0.0.0
   /code-require "Add user login feature"
   ```

## Main Capabilities

| Skill | Purpose |
| --- | --- |
| `code-version` | Version workspace management |
| `code-require` | Requirements analysis |
| `code-design` | High-level design |
| `code-plan` | Detailed design + task breakdown |
| `code-it` | Task coding |
| `code-unit` | Unit tests |
| `code-review` | Code review |
| `code-dashboard` | Dev dashboard |
| `code-publish` | Release deployment |
| `code-auto` | Automated development (orchestrator) |
| `code-rule` | Coding conventions |

## 📖 Detailed Documentation

Full skill descriptions, installation details, version management:[./plugins/code-skills/README.md](./plugins/code-skills/README.md)

## License

[MIT](LICENSE)
