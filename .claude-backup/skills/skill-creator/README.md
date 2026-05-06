# Skill Creator

Create effective Claude Code skills that extend Claude's capabilities with specialized knowledge, workflows, and tools.

## Installation

1. Download this zip file
2. In Claude Code, run:
   ```
   /install-skill skill-creator-v1.2.0.zip
   ```
3. Follow the prompts to install Python dependencies

## Dependencies

### Python Packages
This skill requires these Python packages (installed automatically):
```
PyYAML>=6.0
```

If not auto-installed, run:
```bash
pip3 install PyYAML
```

## What This Skill Does

The skill-creator guides you through creating reusable skills for Claude Code:

- **Initialize skills** - Create skill templates with proper structure
- **Design workflows** - Break complex tasks into progressive disclosure patterns
- **Bundle resources** - Organize scripts, references, and assets
- **Validate & package** - Ensure skills meet requirements before distribution

## Usage

Ask naturally:
- "Create a skill for PDF editing"
- "Help me build a skill for my BigQuery queries"
- "I need a skill to generate thumbnails"

Or use the scripts directly:
```bash
# Initialize a new skill
python3 scripts/init_skill.py my-skill --path .claude/skills

# Validate skill structure
python3 scripts/quick_validate.py .claude/skills/my-skill

# Package for distribution
python3 scripts/package_skill.py .claude/skills/my-skill
```

## How It Works

See `WORKFLOW.md` for detailed usage instructions and examples.

## Skill Structure

Every skill you create follows this structure:
```
skill-name/
├── SKILL.md         # Required - frontmatter + instructions
├── scripts/         # Optional - executable Python/Bash
├── references/      # Optional - documentation loaded as needed
└── assets/          # Optional - files used in output
```

---
Packaged with Claude Code /export-skill
