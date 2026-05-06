---
description: Connect Claude to an external tool (Notion, email, etc.)
argument-hint: [tool-name] [setup-guide-url]
---

Help this user connect Claude to **$1** so Claude can interact with it directly.

The user is NOT technical - explain everything in plain language, one step at a time.

## Input
- **Tool they want to connect:** $1
- **Setup guide URL:** $2

## How to Help

### Step 1: Read the Setup Guide
Fetch the documentation at the URL provided. Understand what's needed before explaining anything to the user.

### Step 2: Check What's Needed
Figure out:
- Do they need an API token from the tool? (Most tools require this - explain it's like a password for remote access)
- Is there anything they need to install first?

### Step 3: Walk Them Through It
Guide them like you're sitting next to them:

**If they need an API token from the tool:**
- Tell them exactly where to go (e.g., "Go to notion.so, click Settings, then Integrations")
- Describe what they'll see on each screen
- Tell them what to click and what to copy
- Ask them to paste it here when they have it

**If they need to install something:**
- Explain what it is in simple terms
- Give them the exact command to run
- Tell them what "success" looks like

**If they need to approve permissions:**
- Explain what Claude will be able to do with this tool
- Reassure them about security if relevant

### Step 4: Choose the Right Setup Method

**Priority order (use the first one available):**

1. **Remote/hosted MCP** (BEST) - Runs on the provider's servers, nothing to install
   - Look for URLs like `https://mcp.toolname.com` or "hosted" in the docs
   - This is the easiest option - just needs an API token

2. **npx-based MCP** (GOOD) - Runs locally using Node.js (they already have this)
   - Look for commands like `npx @company/mcp-server`
   - No extra software needed

3. **Docker-based MCP** (LAST RESORT) - Requires Docker Desktop
   - ⚠️ Only use this if no other option exists
   - Warn the user: "This MCP requires Docker - that's extra software you'd need to install. Are you okay with that, or should we look for an alternative?"
   - If they don't want Docker, help them find a different MCP or suggest they skip this tool for now

### Step 5: Check Who Made This MCP

**If it's an official MCP** (made by the tool's company - e.g., DataForSEO's own MCP):
- Great! This is the most reliable and secure option

**If it's a third-party MCP** (made by someone else):
- ⚠️ Warn the user: "This MCP wasn't made by [tool name] directly - it was created by [publisher name]. Before we continue, do you trust this publisher? MCPs can access your data, so it's worth checking their reputation first."
- Wait for the user to confirm before proceeding

### Step 6: Set It Up
Once you have everything needed and trust is confirmed, use the `claude mcp add` CLI command (this is more reliable than editing `.mcp.json` directly due to a known bug).

**For npx-based MCPs (with environment variables):**
```
claude mcp add <name> npx <package-name> -e KEY1=value1 -e KEY2=value2
```
Example:
```
claude mcp add dataforseo npx dataforseo-mcp-server -e DATAFORSEO_USERNAME=xxx -e DATAFORSEO_PASSWORD=xxx
```

**For remote/HTTP MCPs:**
```
claude mcp add --transport http <name> <url>
```
With authentication header:
```
claude mcp add --transport http <name> <url> --header "Authorization: Bearer xxx"
```

**Important:** After adding the MCP, tell the user to restart Claude Code for it to take effect.

### Step 7: Test It
Make a simple request to the tool to prove it's working. Show them the result.

## Communication Style

- Use "you" and "your" - talk directly to them
- Use real terminology but explain it: "You'll need an API token - that's basically a password that lets Claude access the app remotely"
- One thing at a time - don't overwhelm with multiple steps at once
- If something goes wrong, explain what happened in plain terms and what to try

## When You're Done

```
✅ Done! Claude can now talk to $1.

Here's what Claude can do now:
- [list 2-3 things in plain language, e.g., "Read your Notion pages", "Create new entries"]

Try asking: "[simple example request]"
```
