---
name: slides
description: Create strategic HTML presentations with Chart.js, design tokens, responsive layouts, copywriting formulas, and contextual slide strategies. Use when building client pitch decks, internal reports, training materials, executive summaries, sales decks, conference talks, or any structured slide deliverable. Triggers on "make a deck", "create slides", "presentation for X", "pitch deck".
argument-hint: "[topic] [slide-count]"
user-invocable: true
allowed-tools: Read, Write, Bash
metadata:
  author: claudekit
  version: "1.0.0"
version: 1.0.0
---

# Slides

Strategic HTML presentation design with data visualization.

<args>$ARGUMENTS</args>

## When to Use

- Marketing presentations and pitch decks
- Data-driven slides with Chart.js
- Strategic slide design with layout patterns
- Copywriting-optimized presentation content

## Subcommands

| Subcommand | Description | Reference |
|------------|-------------|-----------|
| `create` | Create strategic presentation slides | `references/create.md` |

## References (Knowledge Base)

| Topic | File |
|-------|------|
| Layout Patterns | `references/layout-patterns.md` |
| HTML Template | `references/html-template.md` |
| Copywriting Formulas | `references/copywriting-formulas.md` |
| Slide Strategies | `references/slide-strategies.md` |

## Routing

1. Parse subcommand from `$ARGUMENTS` (first word)
2. Load corresponding `references/{subcommand}.md`
3. Execute with remaining arguments

## Quick Start Example

**Input:** `/slides create "5-slide SEO pitch for agency clients"`

**Output:** Self-contained HTML file with:

```html
<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="assets/design-tokens.css">
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
  <style>
    /* Slide container, navigation, responsive layout */
    .slide { width: 100vw; height: 100vh; display: flex; align-items: center; justify-content: center; }
    .slide h1 { font-size: var(--typography-font-size-4xl); color: var(--color-primary); }
  </style>
</head>
<body>
  <!-- Slide 1: Title -->
  <div class="slide" id="s1">
    <h1>Why SEO Still Beats Paid in 2026</h1>
    <p>Data-driven proof for decision makers</p>
  </div>

  <!-- Slide 2: Problem (with Chart.js) -->
  <div class="slide" id="s2">
    <h2>Ad Costs Are Rising 23% YoY</h2>
    <canvas id="costChart"></canvas>
  </div>

  <!-- ... slides 3-5 ... -->

  <!-- Navigation: arrow keys + click + progress bar -->
  <script>
    // Chart.js initialization
    new Chart(document.getElementById('costChart'), { /* ... */ });
    // Keyboard navigation
    let current = 0;
    document.addEventListener('keydown', e => { /* arrow key logic */ });
  </script>
</body>
</html>
```

**Key rules:**
- ALL slides use CSS variables from design-tokens.css (no hardcoded colors)
- Chart.js for all data visualizations (not CSS-only bars)
- Keyboard navigation (arrows), click, and progress bar included
- Each slide is persuasion-focused with copywriting formulas (PAS, AIDA, FAB)
- Center-aligned content, responsive to screen size

## Slide Strategy Selection

| Deck Type | Slides | Emotion Arc | Best For |
|-----------|--------|-------------|----------|
| Investor Pitch | 10-12 | Problem→Hope→Proof→Ask | Fundraising |
| Sales Demo | 7-9 | Pain→Solution→Results→CTA | Client meetings |
| Conference Talk | 15-20 | Hook→Story→Insight→Takeaway | Speaking events |
| Internal Update | 5-7 | Context→Progress→Blockers→Next | Team meetings |
| Case Study | 8-10 | Challenge→Approach→Results→Lessons | Portfolio |

For detailed strategies and layouts: `references/slide-strategies.md` and `references/layout-patterns.md`
