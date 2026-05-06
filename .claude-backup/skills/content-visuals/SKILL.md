---
name: content-visuals
description: Generate 2 semantically SEO-optimised inline SVG visuals per content page. SVGs embed directly in HTML — no image uploads, instant load, zero CLS. Improves dwell time, featured snippet eligibility, and topical comprehension.
user-invocable: true
allowed-tools: Read, Write
argument-hint: "[content-file-path] [--style clinical|comparison|process]"
version: 1.0.0
---

# Content Visuals — Inline SVG Generator

Generate 2 semantically SEO-optimised inline SVG visuals for every content page. Renders natively in HTML without image uploads, loads instantly (no CLS).

## Arguments

- `content_path` (required): Path to the markdown content file
- `style` (optional): `clinical` (default), `comparison`, `process`

---

## Visual Types (Pick 2 Per Page)

### Type 1: Data Visualisation
- **Horizontal bar chart** — evidence strength, comparison scores
- **Range chart** — frequency/dosage/timeline ranges
- **Comparison matrix** — features across products/methods
- **Timeline** — study progression, expected results

### Type 2: Conceptual Diagram
- **Process flow** — mechanism of action
- **Anatomy/body diagram** — affected areas
- **Hierarchy/tree** — benefit categories, decision trees
- **Cycle diagram** — feedback loops, recurring processes

### Selection Rules
1. Pick 1 data vis + 1 conceptual when possible
2. No quantitative data → 2 conceptual diagrams
3. Entirely data-driven → 2 data visualisations
4. Never duplicate same visual type

---

## SVG Design Rules

### Colour Palette (3-4 max)

| Role | Hex | Usage |
|------|-----|-------|
| Primary | `#2563EB` | Main data, primary bars |
| Secondary | `#059669` | Positive indicators, "strong" evidence |
| Accent | `#D97706` | Highlights, warnings, "moderate" |
| Neutral | `#6B7280` | Labels, gridlines |
| Background | `#F8FAFC` | SVG background fill |

No colours outside this palette. No red, purple, gradients, or opacity tricks.

### Typography
- Font: `font-family="system-ui, -apple-system, sans-serif"` on all text
- Min size: `12px`. Title: `16px` bold. Label: `13-14px`. Axis: `12px`
- High contrast only: `#1F2937` on light, `#FFFFFF` on coloured bars

### Layout
- Set `viewBox` on every SVG. Never set fixed `width`/`height` attributes
- Typical: `0 0 720 400` landscape, `0 0 720 500` taller diagrams
- Must work at both 720px and 320px rendered width
- Prefer vertical/stacked layouts for mobile. Labels directly on elements (avoid separate legends)

### Aesthetic
No gradients, drop shadows, rounded bar corners (`rx="0"`), decorative elements, or 3D effects. Clean, clinical, professional — medical journal chart aesthetic.

---

## SEO Requirements

Every SVG MUST include:
1. `role="img"` on `<svg>` element
2. `aria-labelledby` pointing to title and desc IDs
3. `<title>` with target keyword
4. `<desc>` with 2-3 sentence description
5. `<figure class="content-visual">` wrapper with keyword-rich `<figcaption>`

ID convention: Visual 1: `chart-title-1`/`chart-desc-1`, Visual 2: `chart-title-2`/`chart-desc-2`

## Output Format

```html
<figure class="content-visual">
  <svg role="img" aria-labelledby="chart-title-1 chart-desc-1" viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:720px;height:auto;">
    <title id="chart-title-1">[Keyword-rich title]</title>
    <desc id="chart-desc-1">[Full description, 2-3 sentences]</desc>
    <rect width="720" height="400" fill="#F8FAFC" />
    <text x="360" y="30" text-anchor="middle" font-family="system-ui, -apple-system, sans-serif" font-size="16" font-weight="bold" fill="#1F2937">[Chart Title]</text>
    <!-- SVG content -->
  </svg>
  <figcaption>[Keyword-rich caption — 1 sentence key takeaway]</figcaption>
</figure>
```

Use `class="content-visual"` on all `<figure>` elements. No inline styles on `<figure>` or `<figcaption>`.

---

## Placement Rules

- **Visual 1**: After introduction (before or just after first H2)
- **Visual 2**: Middle of content (~50-60% through), near most data-heavy section
- Never place both adjacent or directly before/after an HTML table
- Specify: **"Place after the H2: [exact heading text]"**

---

## Process

### Step 1: Read Content
Extract: primary entity/keyword, quantitative data, processes/mechanisms, H2 structure, British English check (.co.uk sites)

### Step 2: Select Visual Types
1. Identify strongest data set for data vis
2. Identify strongest concept for diagram
3. Apply selection rules

### Step 3: Extract Data
Extract exact data from content for each visual. **Do NOT invent data.** Every number/label must come directly from the content.

### Step 4: Generate SVGs
Build following all design rules: background rect → title → data elements → labels → `<title>`/`<desc>` → wrap in `<figure>`

### Step 5: Output
1. Visual 1 HTML + placement instruction
2. Visual 2 HTML + placement instruction
3. Placement summary
4. SEO checklist confirmation

---

## Quality Checklist

- [ ] Exactly 2 visuals generated
- [ ] Each SVG has `role="img"`, `aria-labelledby`, `<title>` with keyword, `<desc>` (2-3 sentences)
- [ ] Wrapped in `<figure class="content-visual">` with keyword-rich `<figcaption>`
- [ ] Placement specifies exact H2; visuals NOT adjacent; not next to HTML tables
- [ ] Colours from approved palette ONLY
- [ ] `system-ui` font family on all text, min 12px
- [ ] `viewBox` set, no fixed width/height
- [ ] Legible at 320px viewport width
- [ ] All data extracted from content (nothing invented)
- [ ] No gradients, shadows, rounded corners, decorative elements
- [ ] British English labels on .co.uk sites

---

## Style Presets

| Preset | Use For | Colour Coding |
|--------|---------|---------------|
| `clinical` | Health, medical, research | Green=strong, amber=moderate, blue=primary |
| `comparison` | Product reviews, buying guides | Blue=recommended, green=value, amber=caution |
| `process` | How-to guides, tutorials | Blue=current step, green=complete, amber=decision |

## Failure Patterns to AVOID

1. **Inventing data** — every label must come from content
2. **Decorative visuals** — every element must be informational
3. **Fixed dimensions** — use `viewBox` + CSS `width:100%`
4. **Web fonts** — system fonts only, no external resources
5. **Complex visualisations** — 4-8 data points max per chart
6. **Both visuals stacked** — separate with at least one H2 section
7. **Missing accessibility** — `role`, `aria-labelledby`, `<title>`, `<desc>` required
8. **Americanisms on .co.uk** — "Optimise" not "Optimize"
9. **Gradients or shadows** — flat fills only
