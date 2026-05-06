---
name: ui-ux-pro-max
description: "UI/UX design intelligence for web and mobile. Includes 50+ styles, 161 color palettes, 57 font pairings, 161 product types, 99 UX guidelines, and 25 chart types across 10 stacks (React, Next.js, Vue, Svelte, SwiftUI, React Native, Flutter, Tailwind, shadcn/ui, and HTML/CSS). Actions: plan, build, create, design, implement, review, fix, improve, optimize, enhance, refactor, and check UI/UX code."
user-invocable: true
allowed-tools: Read, Write, Bash, WebSearch
argument-hint: "[component/page/app to design or review]"
version: 1.0.0
---

# UI/UX Pro Max - Design Intelligence

50+ styles, 161 color palettes, 57 font pairings, 161 product types, 99 UX guidelines, 25 chart types across 10 stacks. Searchable database with priority-based recommendations.

## When to Apply

Use when task involves UI structure, visual design, interaction patterns, or UX quality control. Skip for pure backend, API/DB design, infra/DevOps, or non-visual automation.

## Rule Categories by Priority

| Pri | Category | Impact | Key Checks | Anti-Patterns |
|-----|----------|--------|------------|---------------|
| 1 | Accessibility | CRITICAL | Contrast 4.5:1, alt text, keyboard nav, aria-labels, focus rings | Icon-only buttons without labels, removing focus rings |
| 2 | Touch & Interaction | CRITICAL | Min 44×44px targets, 8px+ spacing, loading feedback | Hover-only interactions, 0ms state changes |
| 3 | Performance | HIGH | WebP/AVIF, lazy loading, CLS < 0.1, skeleton screens | Layout thrashing, cumulative layout shift |
| 4 | Style Selection | HIGH | Match product type, consistency, SVG icons (no emoji) | Mixing styles, emoji as icons |
| 5 | Layout & Responsive | HIGH | Mobile-first, viewport meta, no horizontal scroll | Fixed px widths, disabled zoom |
| 6 | Typography & Color | MEDIUM | Base 16px, line-height 1.5, semantic color tokens | Text <12px, gray-on-gray, raw hex |
| 7 | Animation | MEDIUM | 150-300ms duration, transform/opacity only, reduced-motion | Decorative-only, animating width/height |
| 8 | Forms & Feedback | MEDIUM | Visible labels, error near field, progressive disclosure | Placeholder-only labels, errors only at top |
| 9 | Navigation | HIGH | Predictable back, bottom nav ≤5, deep linking | Overloaded nav, broken back behavior |
| 10 | Charts & Data | LOW | Legends, tooltips, accessible colors, pattern/texture | Color-only meaning, no table alternative |

For detailed rules per category, search with: `python3 skills/ui-ux-pro-max/scripts/search.py "<keyword>" --domain ux`

---

## How to Use

### Step 1: Analyze Requirements
Extract: product type, target audience, style keywords, stack.

### Step 2: Generate Design System (REQUIRED)

```bash
python3 skills/ui-ux-pro-max/scripts/search.py "<product_type> <industry> <keywords>" --design-system [-p "Project Name"]
```

Returns complete design system: pattern, style, colors, typography, effects, anti-patterns.

**Persist with `--persist`** to save `design-system/MASTER.md` for cross-session retrieval. Add `--page "dashboard"` for page-specific overrides.

### Step 3: Detailed Domain Searches (as needed)

```bash
python3 skills/ui-ux-pro-max/scripts/search.py "<keyword>" --domain <domain> [-n <max_results>]
```

| Need | Domain | Example |
|------|--------|---------|
| Product patterns | `product` | `"entertainment social"` |
| Style options | `style` | `"glassmorphism dark"` |
| Color palettes | `color` | `"saas vibrant"` |
| Font pairings | `typography` | `"playful modern"` |
| Chart types | `chart` | `"real-time dashboard"` |
| UX practices | `ux` | `"animation accessibility"` |
| Google Fonts | `google-fonts` | `"sans serif variable"` |
| Landing structure | `landing` | `"hero social-proof"` |
| React perf | `react` | `"rerender memo list"` |
| App interface | `web` | `"accessibilityLabel touch"` |
| AI/CSS keywords | `prompt` | `"minimalism"` |

### Step 4: Stack Guidelines

```bash
python3 skills/ui-ux-pro-max/scripts/search.py "<keyword>" --stack react-native
```

Available stacks: `react-native`

---

## Prerequisites

Check Python: `python3 --version || python --version`

Install if needed: macOS `brew install python3` | Ubuntu `sudo apt install python3` | Windows `winget install Python.Python.3.12`

---

## Output Formats

```bash
# ASCII box (default)
python3 skills/ui-ux-pro-max/scripts/search.py "fintech crypto" --design-system

# Markdown
python3 skills/ui-ux-pro-max/scripts/search.py "fintech crypto" --design-system -f markdown
```

---

## Common Sticking Points

| Problem | Solution |
|---------|----------|
| Can't decide style/color | Re-run `--design-system` with different keywords |
| Dark mode contrast | Check `color-dark-mode` + `color-accessible-pairs` rules |
| Unnatural animations | Use `spring-physics` + `exit-faster-than-enter` |
| Poor form UX | Check `inline-validation` + `error-clarity` + `focus-management` |
| Confusing navigation | Check `nav-hierarchy` + `bottom-nav-limit` + `back-behavior` |
| Layout breaks on mobile | Check `mobile-first` + `breakpoint-consistency` |

---

## Pre-Delivery Checklist

### Visual Quality
- [ ] No emojis as icons (SVG only), consistent icon family
- [ ] Semantic theme tokens (no hardcoded hex per screen)
- [ ] Pressed states don't shift layout

### Interaction
- [ ] Touch targets ≥44×44pt, clear press feedback (150-300ms)
- [ ] Disabled states visually clear and non-interactive
- [ ] Screen reader focus order matches visual order

### Light/Dark Mode
- [ ] Primary text ≥4.5:1 contrast in both modes
- [ ] Borders/dividers visible in both modes
- [ ] Both themes tested before delivery

### Layout
- [ ] Safe areas respected for headers/tab bars
- [ ] Verified on 375px, large phone, tablet (portrait + landscape)
- [ ] 4/8dp spacing rhythm maintained
- [ ] No content hidden behind fixed bars

### Accessibility
- [ ] All images/icons have accessibility labels
- [ ] Color not the only indicator
- [ ] Reduced motion and dynamic text size supported
