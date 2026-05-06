---
name: install-skill
description: Install a skill from a downloaded zip file or folder
user-invocable: true
allowed-tools: Read, Write, Bash, Glob, Grep, AskUserQuestion, TaskCreate, TaskUpdate, TaskList
argument-hint: "<path-to-skill.zip or skill-folder>"
version: 1.0.0
---

# Install Skill

**Input:** `$ARGUMENTS`

---

## MANDATORY FIRST STEP: Create Todo List

**You MUST use TaskCreate to create this todo list before doing anything else:**

```
1. Ensure project has .env, .env.example, and .gitignore
2. Locate skill package
3. Validate skill structure
4. Security review (CRITICAL)
5. Check existing installation
6. Install skill files
7. Install dependencies
8. Run install script & configure MCP server
9. Configure API keys
10. Validate installation
11. Show workflow overview
12. Ensure CLAUDE.md documents skill secrets pattern
```

---

## Todo 1: Ensure .env, .env.example, .gitignore

Check all three files exist. Create any that are missing:

- **.env**: Header comment + blank (for actual keys, git-ignored)
- **.env.example**: Header comment + blank (template, committed)
- **.gitignore**: Must exclude `.env`, `.env.local`, `.env.*.local`, `.mcp.json`, plus standard OS/Python/Node ignores

If .gitignore exists, ensure `.env` is excluded. Ensure `.env.example` is NOT gitignored.

---

## Todo 2: Locate Skill Package

Find skill from `$ARGUMENTS` — check absolute path, relative path, then search `./temp/` and `~/Downloads/`. If not found, use AskUserQuestion.

---

## Todo 3: Validate Skill Structure

If .zip, extract to temp dir first. Check for valid SKILL.md with YAML frontmatter (name, description, version, triggers). Parse and extract metadata. If invalid, report error and stop.

---

## Todo 4: Security Review (CRITICAL)

**Skills execute code on the user's machine. This step is MANDATORY.**

### Scan all script files (.py, .js, .sh, .ts)

**BLOCK installation if found:**
- Data exfiltration (HTTP requests sending env vars/files to unknown servers)
- Credential harvesting (reading ~/.ssh, ~/.aws, browser data, keychains)
- Remote code execution (eval/exec with external input, curl-pipe-bash)
- System compromise (writing to /usr/bin, modifying /etc, adding cron jobs)
- Obfuscated code (base64-decoded exec, char code arrays, hex payloads)

**Warn user (AskUserQuestion) if found:**
- Broad file access outside skill directory
- Subprocess calls (may be legitimate for media processing)
- Network requests to APIs (verify domains are known/legitimate)
- Undeclared environment variable access

**Report format:** List files checked, issues found (with file:line references), and verdict (passed / blocked / user decision required).

---

## Todo 5: Check Existing Installation

Check `.claude/skills/skill-name/`. If exists, compare versions and offer: Update / Keep current / Cancel.

---

## Todo 6: Install Skill Files

```shell
mkdir -p .claude/skills
cp -r path/to/skill-folder .claude/skills/
```

List installed files. Cleanup temp dir if extracted from zip.

---

## Todo 7: Install Dependencies

### Python (if requirements.txt exists)
- Show packages, detect Python env, warn if no venv
- AskUserQuestion: Install now / Skip / Show requirements
- On failure, retry with `--user` flag

### Node.js (if package.json exists)
- Detect package manager (yarn.lock / pnpm-lock.yaml / npm)
- AskUserQuestion: Install now / Skip
- Run appropriate install command

### System tools (if requires_system in frontmatter)
- Check each tool, show install commands for macOS/Linux/Windows if missing
- AskUserQuestion: Install now / Skip / Cancel

---

## Todo 8: Run Install Script & Configure MCP

If `install.sh` exists, chmod +x and run it. If `mcp_setup_guide` in frontmatter, follow it. Verify MCP with `claude mcp list`. Remind user to restart Claude Code if MCP configured.

---

## Todo 9: Configure API Keys

Skip if no `requires_secrets` in metadata. For each required key:

- Show service name, website, pricing info, how-to-get instructions, key format hint
- Check .env and .env.example for existing config
- AskUserQuestion: Ready to add / Skip / Add manually later
- Add to .env (real value) and .env.example (placeholder only)
- Never echo actual key values

---

## Todo 10: Validate Installation

Verify: files installed, Python packages importable, Node packages listed, API keys configured, system tools available. Show summary with pass/warn status for each.

---

## Todo 11: Show Workflow Overview

Display WORKFLOW.md Quick Start if it exists, otherwise generate brief usage overview from SKILL.md triggers/description.

**Always end with restart reminder:**
```
Restart Claude Code: Cmd/Ctrl+Shift+P > "Developer: Reload Window"
```

---

## Todo 12: Document in CLAUDE.md

If CLAUDE.md doesn't mention `.env`, append a section explaining the .env/.env.example/requires_secrets pattern for skills.

---

## Final Summary

```
Skill: <name> v<version>
Location: .claude/skills/<name>/
Security: Passed / Blocked / Warnings
Dependencies: All installed / Some missing
API Keys: Configured / Setup required
Usage: /<trigger> "Your prompt"

RESTART REQUIRED
```

---

## Error Handling

| Error | Message |
|-------|---------|
| File not found | Could not find skill package at [path] |
| Not a valid zip | File doesn't appear to be a valid zip archive |
| No SKILL.md | Invalid skill package - no SKILL.md found |
| Security blocked | Installation blocked - critical security issues found |
| Permission denied | Cannot write to .claude/skills/ |
| Dependency failed | Failed to install [package]. Try: pip3 install [package] |

---

## Key Principles

1. TaskCreate is mandatory — create todo list FIRST
2. Security review is CRITICAL — NEVER skip Todo 4
3. .env (git-ignored) + .env.example (committed) + .gitignore work together
4. Show pricing info for API keys
5. Never echo key values
6. Always update .env.example with placeholders
7. Warn about system Python, prefer venvs
8. Validate installation before declaring success
9. Cleanup temp files, remind to restart
