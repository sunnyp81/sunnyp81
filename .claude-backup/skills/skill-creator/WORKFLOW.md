# How to Use: skill-creator

## Quick Start

1. **Trigger the skill** by saying:
   - "Create a skill for PDF editing"
   - "I need a new skill for managing my BigQuery queries"
   - "Help me build a skill to generate thumbnails"

2. **Provide context**:
   - What tasks should the skill handle?
   - Example user requests the skill should respond to
   - What resources (scripts, references, assets) it might need

3. **Iterate with Claude**:
   - Claude will ask clarifying questions
   - Review and refine the generated SKILL.md
   - Test the skill and improve based on real usage

## Example Workflows

### Creating a Simple Guidance Skill

```
Create a skill for writing commit messages in our team's style.
```

Claude will:
1. Ask about your commit message conventions
2. Create a SKILL.md with guidelines and examples
3. No scripts needed - pure documentation

### Creating a Skill with Scripts

```
Create a skill for rotating and cropping PDFs.
```

Claude will:
1. Ask what PDF operations you need
2. Create Python scripts in `scripts/`
3. Write SKILL.md with instructions for using the scripts
4. Test the scripts work correctly

### Creating a Skill with External APIs

```
Create a skill for generating images with Gemini.
```

Claude will:
1. Set up `requires_secrets` in frontmatter
2. Include `load_env()` pattern in scripts
3. Document API key setup instructions
4. Test the API integration works

## Skill Creation Process

1. **Understand** - Gather concrete examples of how the skill will be used
2. **Plan** - Identify what scripts, references, and assets are needed
3. **Initialize** - Run `scripts/init_skill.py` to create the template
4. **Edit** - Implement the skill resources and write SKILL.md
5. **Package** - Run `scripts/package_skill.py` to create distributable .skill file
6. **Iterate** - Improve based on real usage

## Using the Scripts

### Initialize a New Skill

```bash
python3 .claude/skills/skill-creator/scripts/init_skill.py my-skill --path .claude/skills
```

Creates:
- `my-skill/SKILL.md` - Template with TODOs
- `my-skill/scripts/` - Example script
- `my-skill/references/` - Example reference doc
- `my-skill/assets/` - Example asset placeholder

### Validate a Skill

```bash
python3 .claude/skills/skill-creator/scripts/quick_validate.py .claude/skills/my-skill
```

Checks:
- SKILL.md exists with valid frontmatter
- Required fields (name, description) present
- Naming conventions followed

### Package for Distribution

```bash
python3 .claude/skills/skill-creator/scripts/package_skill.py .claude/skills/my-skill
```

Creates `my-skill.skill` file ready to share with others.

## Tips

- **Keep SKILL.md lean** - Use progressive disclosure; put detailed docs in `references/`
- **Test scripts** - Run them before packaging to catch bugs
- **Include examples** - Show input/output pairs to demonstrate expected behavior
- **Delete unused folders** - Not every skill needs scripts/, references/, and assets/
- **Version your skills** - Use semantic versioning (1.0.0, 1.1.0, 2.0.0)

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "SKILL.md not found" | Ensure the skill directory has a SKILL.md file |
| "Missing 'name' in frontmatter" | Add `name: your-skill-name` to the YAML frontmatter |
| "Invalid YAML" | Check for syntax errors in the `---` block |
| "Name should be hyphen-case" | Use lowercase with hyphens only (e.g., `my-skill`) |
| Import error for yaml | Install PyYAML: `pip3 install PyYAML` |
