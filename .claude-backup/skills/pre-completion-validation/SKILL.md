---
name: pre-completion-validation
description: >
  MANDATORY before marking ANY task done, saying "complete", "finished", "deployed", or "done" on ANY project.
  Runs two checks: (1) autoresearch quality loop — iterate semantic-audit on content/HTML files until score ≥85,
  (2) Playwright MCP browser validation — open deployed URL, check console errors, take screenshot.
  Triggers on: finishing a task, about to say done, pre-deploy, pre-handoff, completing Hummingbird pages,
  finishing site builds, writing content, UGC articles, any deliverable. NEVER skip.
version: 1.0.0
user-invocable: true
---

# Pre-Completion Validation

Run BOTH checks before marking anything done. Do not skip either step.

## Step 1 — Content Quality Loop (autoresearch pattern)

For every content file, HTML page, or article created/modified this session:

1. Run `/semantic-audit` on the file
2. Record score in `results.tsv`:
   ```
   iteration  file  score  change  status
   baseline   page.md  72  none  keep
   ```
3. If score < 85 → identify the lowest-scoring element → fix it → re-audit → repeat
4. If score ≥ 85 → mark `pass` → move to next file
5. After 10 iterations with no improvement → escalate to user with specific blocker

**Skip if:** session only involved config changes, MCP setup, git operations, or non-content work.

## Step 2 — Browser Validation (Playwright MCP)

If a URL was deployed or is available:

1. Use Playwright MCP to navigate to the URL:
   - `browser_navigate` → load the page
   - `browser_console_messages` → capture any console errors/warnings
   - `browser_evaluate` → check for JS errors: `() => window.__errors || []`
   - `browser_take_screenshot` → visual confirmation

2. Pass criteria:
   - No JS errors in console
   - Page loads without 404/500
   - Key elements visible in screenshot (hero, nav, main content)

3. Fail criteria → fix the issue → re-validate before marking done

**Skip if:** no URL deployed yet (note it as pending validation). If Playwright MCP not connected, fall back to `curl -sI` HTTP check + HTML source validation and note the limitation.

## Sign-off Format

Only after both steps pass, output:

```
VALIDATION PASSED
- Content quality: [file] score [X]/100
- Browser: [URL] — no console errors, screenshot taken
- Status: READY TO MARK DONE
```

If either fails, output what's blocking and fix it first.
