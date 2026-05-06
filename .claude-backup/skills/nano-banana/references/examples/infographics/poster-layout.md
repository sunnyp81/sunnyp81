# Complex Poster Layout - Multi-Section Typography

This example demonstrates Nano Banana Pro's ability to generate complex informational posters with multiple sections, varied typography, and structured data layouts.

## The Productivity Guide Poster

```json
{
  "project": "Productivity_Systems_Poster",
  "format": {
    "dimensions": "24x36 inches",
    "orientation": "portrait",
    "resolution": "print quality"
  },
  "style": {
    "aesthetic": "modern infographic",
    "color_palette": ["#F5F5DC", "#000000", "#1E90FF", "#FF6B35", "#2ECC71"],
    "typography_system": "mixed font families for hierarchy"
  },
  "sections": [
    {
      "id": "header",
      "type": "title_block",
      "content": {
        "main_title": "THE COMPLETE GUIDE TO HUMAN PRODUCTIVITY SYSTEMS",
        "subtitle": "2025 EDITION",
        "title_style": "massive bold condensed",
        "subtitle_style": "light serif"
      },
      "position": "top, full width"
    },
    {
      "id": "framework",
      "type": "pillars",
      "title": "THE 4-PILLAR MODEL",
      "title_style": "geometric sans",
      "content": [
        { "name": "Clarity", "description": "define priorities, workflows, boundaries", "icon": "target" },
        { "name": "Execution", "description": "reduce friction, focus intervals, micro-sprints", "icon": "checklist" },
        { "name": "Review", "description": "end-of-day reflection, adjust plan", "icon": "clock" },
        { "name": "Growth", "description": "skill development and system adaptation", "icon": "graph" }
      ],
      "position": "below header"
    },
    {
      "id": "typography_grid",
      "type": "mixed_font_mosaic",
      "content": [
        { "text": "Deep Work (90 minutes)", "style": "ultra bold" },
        { "text": "Micro Break (7 minutes)", "style": "thin serif" },
        { "text": "Task Clustering", "style": "italic condensed" },
        { "text": "Context Switching Cost", "style": "monospace" },
        { "text": "Weekly Reset Ritual", "style": "handwritten" },
        { "text": "Energy Curve Mapping", "style": "wide rounded" },
        { "text": "Protect Your Peak Hours", "style": "heavy display" }
      ],
      "background_shapes": ["circles", "hexagons", "arrows"]
    },
    {
      "id": "behavioral_loops",
      "type": "card_grid",
      "title": "Behavioral Loops That Drive Consistency",
      "title_style": "elegant serif",
      "cards": [
        {
          "heading": "Trigger → Action → Reward",
          "body": "Habits form by closing loops intentionally",
          "accent_color": "#FF6B35"
        },
        {
          "heading": "Identity-Based Motivation",
          "body": "You act like the type of person you believe you are",
          "accent_color": "#1E90FF"
        },
        {
          "heading": "Environment Shaping",
          "body": "Design surroundings for automatic productive behavior",
          "accent_color": "#2ECC71"
        },
        {
          "heading": "Momentum Bias",
          "body": "Small wins accumulate into higher output",
          "accent_color": "#9B59B6"
        }
      ]
    },
    {
      "id": "comparison_table",
      "type": "data_table",
      "title": "Workflow Systems Comparison",
      "columns": ["System", "Purpose", "Strengths", "Weaknesses", "Ideal For"],
      "rows": [
        ["GTD", "Capture everything", "Comprehensive", "Complex setup", "Knowledge workers"],
        ["PARA", "Organize by actionability", "Flexible", "Requires maintenance", "Digital workers"],
        ["Time-Blocking", "Dedicated focus periods", "Simple", "Rigid", "Deep work tasks"],
        ["Atomic Habits", "Behavior change", "Sustainable", "Slow results", "Long-term goals"]
      ],
      "style": {
        "header": "bold sans",
        "body": "small serif"
      }
    },
    {
      "id": "color_panels",
      "type": "mini_panel_grid",
      "panels": [
        {
          "title": "Focus Killers",
          "color": "#FF6B35",
          "items": ["notifications", "multitasking", "bad sleep", "energy dips"]
        },
        {
          "title": "Performance Boosters",
          "color": "#1E90FF",
          "items": ["hydration", "daily sorting", "25/5 cycles", "deep blocks"]
        },
        {
          "title": "Motivation Myths",
          "color": "#2ECC71",
          "items": ["You need motivation to start", "More hours = more output"]
        },
        {
          "title": "Brutal Truths",
          "color": "#000000",
          "text_color": "#FFFFFF",
          "items": ["Discipline beats inspiration", "Systems > willpower"]
        }
      ]
    },
    {
      "id": "footer",
      "type": "footnotes",
      "style": "dense small-serif text wall",
      "position": "bottom, full width"
    }
  ]
}
```

## Key Techniques

### Section-Based Layout

```json
"sections": [
  { "id": "unique_id", "type": "section_type", "position": "layout_position" }
]
```

Each section is a discrete content block. The model processes them sequentially and respects positioning instructions.

### Typography Hierarchy

```json
"typography_system": {
  "h1": "bold condensed sans, 72pt",
  "h2": "medium serif, 36pt",
  "h3": "regular sans, 24pt",
  "body": "light serif, 12pt",
  "caption": "monospace, 10pt"
}
```

### Mixed Font Mosaic

For dynamic visual interest with varied typography:

```json
{
  "type": "mixed_font_mosaic",
  "content": [
    { "text": "Primary Message", "style": "ultra bold display" },
    { "text": "Secondary Point", "style": "thin serif italic" },
    { "text": "Technical Detail", "style": "monospace" },
    { "text": "Emphasis", "style": "handwritten brush" }
  ]
}
```

## Brand Identity Poster

```json
{
  "project": "Brand_Identity_System",
  "brand_name": "Higgsfield AI",
  "sections": [
    {
      "id": "logo_system",
      "type": "logo_showcase",
      "variants": ["icon + wordmark", "stacked", "icon-only", "white version", "neon-outline"],
      "rules": "never warp the curve, maintain high contrast"
    },
    {
      "id": "color_palette",
      "type": "color_swatches",
      "colors": [
        { "name": "Neon Higgs Green", "hex": "#D7FF28", "meaning": "creativity" },
        { "name": "Absolute Black", "hex": "#000000", "meaning": "precision" },
        { "name": "Aqua Quantum", "hex": "#49FFE9", "meaning": "AI signal" },
        { "name": "Electric Violet", "hex": "#A04CFF", "meaning": "experimental mode" }
      ]
    },
    {
      "id": "typography",
      "type": "font_specimens",
      "fonts": [
        { "use": "headlines", "family": "TG Grotesk / Satoshi", "style": "rounded geometric" },
        { "use": "body", "family": "modern grotesk" },
        { "use": "UI/code", "family": "technical mono" }
      ]
    },
    {
      "id": "graphic_language",
      "type": "pattern_showcase",
      "elements": ["S-curve geometry", "wave lines", "neon arcs", "particle flows"]
    }
  ]
}
```

## Data Visualization Poster

```json
{
  "project": "Annual_Report_Infographic",
  "sections": [
    {
      "id": "hero_stat",
      "type": "large_number",
      "value": "247%",
      "label": "Year-over-year growth",
      "style": "massive bold, gradient fill"
    },
    {
      "id": "chart_section",
      "type": "chart_grid",
      "charts": [
        { "type": "bar_chart", "title": "Revenue by Quarter", "data_visualization": "ascending bars" },
        { "type": "pie_chart", "title": "Market Share", "segments": 5 },
        { "type": "line_graph", "title": "User Growth", "trend": "exponential" }
      ]
    },
    {
      "id": "key_metrics",
      "type": "stat_cards",
      "metrics": [
        { "value": "2.4M", "label": "Active Users" },
        { "value": "99.9%", "label": "Uptime" },
        { "value": "4.8/5", "label": "User Rating" }
      ]
    }
  ]
}
```

## Layout Position Keywords

| Keyword | Meaning |
|---------|---------|
| `top, full width` | Spans entire top |
| `left column` | Left 50% of layout |
| `right sidebar` | Narrow right column |
| `center` | Horizontally centered |
| `below [section_id]` | Positioned after specific section |
| `bottom, full width` | Footer position |
| `floating` | Overlaps other content |

## Common Failures & Fixes

| Problem | Cause | Fix |
|---------|-------|-----|
| Sections overlap | Missing position specs | Add explicit `position` to each section |
| Inconsistent fonts | No typography system | Define `typography_system` at root level |
| Color clashes | Random color selection | Define explicit `color_palette` |
| Unbalanced layout | Too much content in one area | Use grid system with `columns` and `rows` |
