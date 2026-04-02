# Development Workflow, Tools, and Skills Refinement

This document captures Sunny Patel's complete development workflow, tooling stack, and skills growth plan.

---

## Current MCP Server Stack

| MCP Server | Purpose | Implementation |
|---|---|---|
| **Ahrefs** | SEO data API | HTTP-based MCP server |
| **Google Search Console** | Search performance data | Custom Python MCP server |
| **Google Analytics 4** | Traffic and engagement metrics | Official Google MCP via pipx |
| **Bing Webmaster Tools** | Bing search data and indexing | Custom Python MCP server |

These servers provide real-time SEO and analytics data directly within the AI-assisted development workflow, enabling automated analysis pipelines without leaving the editor.

---

## Code Review Process — code-review-graph Integration

[code-review-graph](https://github.com/tirth8205/code-review-graph) builds a local knowledge graph of the codebase using Tree-sitter parsing and provides blast-radius analysis for code changes.

### Installation

```bash
pip install code-review-graph && code-review-graph install && code-review-graph build
```

### What It Does

- Builds a local knowledge graph (SQLite) of the codebase using **Tree-sitter parsing**
- Provides **blast-radius analysis** for code changes — traces callers, dependents, and affected tests
- Achieves **8.2x average token reduction** for AI-assisted code review
- Works as an **MCP server with 20+ tools** for Claude Code
- Supports **19 languages** including Python, TypeScript, JavaScript, Go, and Rust

### Slash Commands

| Command | Usage |
|---|---|
| `/code-review-graph:build-graph` | Build or rebuild the knowledge graph for the current repo |
| `/code-review-graph:review-delta` | Review uncommitted changes with blast-radius context |
| `/code-review-graph:review-pr` | Review a pull request with full dependency analysis |

### Daily Workflow Integration

1. **On repo init** — Run `build-graph` to index the codebase into the local SQLite knowledge graph.
2. **Before commits** — Run `review-delta` to understand the blast radius of staged changes, trace callers and dependents, and catch issues early.
3. **For pull requests** — Run `review-pr` to get a comprehensive review with affected-test identification and dependency-aware context.

---

## Static Analysis Toolkit

Recommended tools from [awesome-static-analysis](https://github.com/awesome-security/awesome-static-analysis), organized by adoption priority.

### Priority 1 — Must-Have for Python

| Tool | Purpose |
|---|---|
| **flake8** | PEP 8 style enforcement + pyflakes + mccabe complexity checks |
| **mypy** | Static type checking for Python type annotations |
| **bandit** | Security vulnerability scanning for Python code |
| **pylint** | Comprehensive linting with code smell detection |

### Priority 2 — Web Development

| Tool | Purpose |
|---|---|
| **ESLint** | JavaScript/TypeScript linting and code quality |
| **Stylelint** | CSS/SCSS linting and style enforcement |
| **HTMLHint** | HTML markup validation and best-practice checks |

### Priority 3 — Advanced

| Tool | Purpose |
|---|---|
| **vulture** | Dead code detection for Python |
| **xenon** | Code complexity monitoring and threshold enforcement |
| **prospector** | Meta-linter wrapper that combines multiple Python analysis tools |
| **Snyk** | Dependency vulnerability scanning across ecosystems |

---

## Skills Refinement Plan

### Python

- Advance **type annotations** — leverage mypy strict mode across all projects
- Deepen **async patterns** — asyncio, aiohttp, structured concurrency
- Strengthen **testing discipline** — pytest fixtures, parametrize, coverage targets

### SEO Automation

- Expand the MCP server stack with additional data sources
- Build **custom analysis pipelines** combining Search Console, GA4, and Ahrefs data
- Automate recurring SEO audits and reporting

### AI-Assisted Development

- Leverage **code-review-graph** for smarter, context-aware reviews
- Build **custom MCP tools** tailored to specific project needs
- Integrate AI review into the standard PR workflow

### Security

- Integrate **bandit + Snyk** into CI pipelines for every push
- Schedule **regular dependency audits** and automate upgrade PRs
- Adopt security-focused linting rules in ESLint and pylint configs

### Code Quality

- Enforce **flake8 + mypy** in pre-commit hooks (see below)
- Set complexity thresholds with xenon and track trends over time
- Run vulture periodically to eliminate dead code

---

## Recommended Pre-commit Hook Setup

Install pre-commit and activate the hooks:

```bash
pip install pre-commit
pre-commit install
```

The project's `.pre-commit-config.yaml` includes the following hooks:

```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    hooks: [trailing-whitespace, end-of-file-fixer, check-yaml, check-json]
  - repo: https://github.com/pycqa/flake8
    hooks: [flake8]
  - repo: https://github.com/pre-commit/mirrors-mypy
    hooks: [mypy]
  - repo: https://github.com/PyCQA/bandit
    hooks: [bandit]
```

These hooks run automatically on every commit to catch style violations, type errors, and security issues before code reaches the remote.
