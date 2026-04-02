# Sunny Patel

**SEO Specialist & Developer** | Building tools at the intersection of search, analytics, and AI-assisted development.

sunny@sunnypatel.co.uk

---

## About

I work across SEO, web analytics, and software development -- building custom integrations and automation tools that connect marketing data platforms with modern AI workflows. My focus is on practical tooling that makes data-driven decisions faster and more reliable.

---

## Skills & Tech Stack

**Languages & Frameworks**
- Python, JavaScript
- Web development (HTML, CSS, JS)

**SEO & Analytics Platforms**
- Google Search Console
- Google Analytics 4
- Ahrefs
- Bing Webmaster Tools

**AI & Automation**
- Claude Code / Anthropic Claude
- MCP (Model Context Protocol) server development
- Custom API integrations

**Infrastructure & DevOps**
- Git, GitHub Actions
- Google Cloud Platform (GCP)
- pipx, virtualenvs, OAuth2 configuration

---

## Current Tools & Integrations

I maintain a set of MCP servers that connect Claude Code to live SEO and analytics data:

| Tool | Type | Description |
|------|------|-------------|
| **Ahrefs MCP** | HTTP (remote) | Direct connection to Ahrefs SEO data API via OAuth |
| **Google Search Console** | Custom Python server | Local MCP server for GSC data via OAuth2 |
| **Google Analytics 4** | Official Google MCP | GA4 data via `analytics-mcp` package and Application Default Credentials |
| **Bing Webmaster Tools** | Custom Python server | Local MCP server for Bing search data via API key |

Configuration and setup details are in [`.claude/mcp/claude-mcp-config.json`](.claude/mcp/claude-mcp-config.json).

---

## Workflow & Process Tools

**Code Review & Analysis**
- `code-review-graph` -- knowledge graph for AI-assisted code review, tracking patterns and context across sessions

**Static Analysis**
- `flake8` -- Python style and error checking
- `pylint` -- Python code analysis and quality scoring
- `mypy` -- Python static type checking
- `bandit` -- Python security linting
- `ESLint` -- JavaScript/TypeScript linting

**CI/CD**
- GitHub Actions for JSON validation, secret scanning, and markdown linting

---

## Contact

- **Email**: sunny@sunnypatel.co.uk
- **GitHub**: [sunnyp81](https://github.com/sunnyp81)
