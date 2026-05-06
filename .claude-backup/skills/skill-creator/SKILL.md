---
name: skill-creator
description: Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends Claude's capabilities with specialized knowledge, workflows, or tool integrations.
version: 1.2.0
user-invocable: true
allowed-tools: Read, Write, Bash, Glob, Grep
argument-hint: "[skill name or description]"
license: Complete terms in LICENSE.txt
---

# Skill Creator

Guide for creating effective skills that extend Claude's capabilities.

## Core Principles

### Concise is Key
Context window is shared. Only add what Claude doesn't already have. Challenge each paragraph: "Does this justify its token cost?" Prefer concise examples over verbose explanations.

### Set Appropriate Degrees of Freedom
- **High freedom** (text instructions): Multiple valid approaches, context-dependent
- **Medium freedom** (pseudocode/parameterized scripts): Preferred pattern exists, some variation OK
- **Low freedom** (specific scripts): Fragile operations, consistency critical

### Anatomy of a Skill

```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter (name, description required)
│   └── Markdown instructions
└── Bundled Resources (optional)
    ├── scripts/      - Executable code
    ├── references/   - Documentation loaded as needed
    └── assets/       - Files used in output (templates, icons)
```

**SKILL.md** has two parts:
- **Frontmatter** (YAML): `name` + `description` determine when skill triggers. Be clear and comprehensive.
- **Body** (Markdown): Instructions loaded AFTER skill triggers.

**Scripts**: For repeatedly-rewritten code or deterministic tasks. Token efficient, may execute without loading into context.

**References**: Keeps SKILL.md lean. Loaded only when needed. For files >10k words, include grep patterns in SKILL.md.

**Assets**: Files used in output (templates, images, fonts). Not loaded into context.

**Do NOT create**: README.md, INSTALLATION_GUIDE.md, CHANGELOG.md, or other auxiliary docs.

### Progressive Disclosure

Three-level loading: metadata (~100 words, always loaded) → SKILL.md body (<5k words, on trigger) → bundled resources (as needed).

Keep SKILL.md under 500 lines. Split content into separate files when approaching limit. Reference files from SKILL.md with clear descriptions of when to read them.

**Key patterns:**
1. High-level guide linking to reference files for details
2. Domain-specific organization (user asks about sales → only load sales.md)
3. Conditional details (basic in SKILL.md, advanced in separate files)

**Rules:** Avoid deeply nested references (one level from SKILL.md). Structure files >100 lines with a table of contents.

## Skill Creation Process

### Step 1: Understand with Concrete Examples
Ask: What functionality? Example usage? What triggers it? Conclude when functionality is clear.

### Step 2: Plan Reusable Contents
For each example: How to execute from scratch? What scripts/references/assets would help when repeating? Create list of resources to include.

### Step 3: Initialize

```bash
scripts/init_skill.py <skill-name> --path <output-directory>
```

Creates skill directory with SKILL.md template, example `scripts/`, `references/`, `assets/` directories. Skip if skill already exists.

### Step 4: Edit the Skill

**Consult design pattern guides:**
- Multi-step processes: `references/workflows.md`
- Output formats/quality: `references/output-patterns.md`

Start with reusable resources (scripts, references, assets). Test scripts by running them. Delete unused example files. Then write SKILL.md.

#### Frontmatter

**Required fields:**
- `name`: hyphen-case, matches directory
- `description`: What it does AND when to use it (primary triggering mechanism)
- `version`: Semantic version for distribution

**Optional fields:**
- `requires_secrets`: API key declarations with `key`, `service`, `url`, `description`, `instructions`, `required`
- `agent`/`model`/`context`: Subagent configuration (`general-purpose`/`Explore`/`Plan`/`Bash`, `sonnet`/`opus`/`haiku`, `fork`)
- `user-invocable`: `false` to prevent slash command invocation
- `disable-model-invocation`: `true` to prevent auto-triggering

**Example with API keys:**
```yaml
requires_secrets:
  - key: GEMINI_API_KEY
    service: Google AI Studio
    url: https://aistudio.google.com/apikey
    description: API key for Gemini image generation
    required: true
```

**Scripts needing API keys** should include inline `load_env()` that reads from project `.env` file (walks up directories to find it).

### Step 5: Package

```bash
scripts/package_skill.py <path/to/skill-folder> [output-dir]
```

Validates (frontmatter, naming, structure, description quality) then creates `.skill` zip file. Fix errors and re-run if validation fails.

### Step 6: Iterate

Use on real tasks → notice struggles → update SKILL.md/resources → test again.
