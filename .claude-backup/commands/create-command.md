---
description: Create a new custom command
argument-hint: [command-name] [what the command should do]
---

Create a custom command file at `.claude/commands/$1.md`.

## Input
- **Command name:** $1
- **Purpose:** $2

## Command File Format

```markdown
---
description: [One line - what it does, shown in /commands]
argument-hint: [Placeholder showing expected input]
---

[Your prompt instructions here]

$ARGUMENTS
```

## How to Write the Prompt

**Structure it with:**
1. **Role/Context** (optional) - Who Claude should act as
2. **Task** - What to do with the input
3. **Output format** - How to structure the response
4. **Constraints** - Length, style, or quality requirements

**Decide on arguments:**
- Use `$ARGUMENTS` when: user provides one blob of text (notes, content, topic)
- Use `$1`, `$2` when: user provides distinct pieces (recipient + topic, title + tone)

## Examples of Good Command Prompts

**Simple (single input):**
```markdown
---
description: Summarize meeting notes into decisions and action items
argument-hint: [paste meeting notes]
---

Summarize these meeting notes into:
1. Key decisions made
2. Action items (with owners if mentioned)
3. Open questions

Keep it concise - bullet points only.

$ARGUMENTS
```

**Multiple inputs:**
```markdown
---
description: Draft a professional email
argument-hint: [recipient context] [topic]
---

Write a professional email.

Recipient: $1
Topic: $2

Requirements:
- Friendly but professional tone
- Clear call to action
- Under 150 words
```

## Your Task

1. Create the command file at `.claude/commands/$1.md`
2. Write a focused, specific prompt based on: "$2"
3. Choose $ARGUMENTS or $1/$2 based on what input the user will provide
4. Keep the description under 60 characters

After creating, confirm with an example of how to use it:
```
/$1 [example input]
```
