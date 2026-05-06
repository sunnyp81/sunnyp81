---
name: accessibility
description: |
  Build WCAG 2.1 AA compliant websites with semantic HTML, proper ARIA, focus management, and screen reader support. Includes color contrast (4.5:1 text), keyboard navigation, form labels, and live regions.

  Use when implementing accessible interfaces, fixing screen reader issues, keyboard navigation, or troubleshooting "focus outline missing", "aria-label required", "insufficient contrast".
user-invocable: true
allowed-tools: Read, Write, Bash, Grep
argument-hint: "[URL or file path to audit]"
version: 1.0.0
---

# Web Accessibility (WCAG 2.1 AA)

**Standards**: WCAG 2.1 Level AA | **Dependencies**: None (framework-agnostic)

---

## Quick Start

### 1. Semantic HTML — Use the right element, not `div` for everything

**Decision tree:**
```
Clickable? → Navigates: <a href> | Submits: <button type="submit"> | Action: <button type="button">
Grouping? → Article: <article> | Section: <section> | Nav: <nav> | Sidebar: <aside>
Form? → Text: <input> | Choice: <select>/<input type="radio"> | Toggle: <input type="checkbox"> | Long: <textarea>
```

### 2. Focus Management — Never remove focus outlines without replacement

Use `:focus-visible` for keyboard-only focus indicators. Ensure 3:1 contrast ratio on indicators.

### 3. Text Alternatives — Every non-text element needs alt text

- `<img>` → meaningful `alt` or `alt=""` for decorative
- Icon buttons → `aria-label="Close dialog"`

### 4. ARIA — Only when HTML can't express the pattern

Common patterns: `aria-label`, `aria-labelledby`, `aria-describedby`, `aria-live`, `aria-expanded`

### 5. Forms — Every input needs a visible `<label>`, not just placeholder

Use `aria-invalid` + `aria-describedby` for error states. Use `role="alert"` for dynamic errors.

---

## Critical Rules

### Always Do
- Use semantic HTML elements first (button, a, nav, article)
- Provide text alternatives for all non-text content
- Ensure 4.5:1 contrast for normal text, 3:1 for large text/UI
- Make all functionality keyboard accessible
- Test with keyboard only (unplug mouse)
- Test with screen reader (NVDA on Windows, VoiceOver on Mac)
- Use proper heading hierarchy (h1 > h2 > h3, no skipping)
- Label all form inputs with visible labels
- Provide focus indicators (never just `outline: none`)
- Use `aria-live` for dynamic content updates

### Never Do
- Use `div` with `onClick` instead of `button`
- Remove focus outlines without replacement
- Use color alone to convey information
- Use placeholders as labels
- Skip heading levels (h1 > h3)
- Use `tabindex` > 0
- Add ARIA when semantic HTML exists
- Forget to restore focus after closing dialogs
- Create keyboard traps (no way to escape)

---

## WCAG 2.1 AA Checklist

### Perceivable
- [ ] All images have alt text (or alt="" if decorative)
- [ ] Text contrast >= 4.5:1 (normal), >= 3:1 (large)
- [ ] Color not used alone to convey information
- [ ] Text can be resized to 200% without loss
- [ ] No auto-playing audio >3 seconds

### Operable
- [ ] All functionality keyboard accessible
- [ ] No keyboard traps
- [ ] Visible focus indicators
- [ ] Users can pause/stop moving content
- [ ] Page titles describe purpose
- [ ] Focus order is logical
- [ ] Link purpose clear from text or context
- [ ] Multiple ways to find pages
- [ ] Headings and labels describe purpose

### Understandable
- [ ] Page language specified (`<html lang="en">`)
- [ ] Language changes marked (`<span lang="es">`)
- [ ] No unexpected context changes on focus/input
- [ ] Consistent navigation across site
- [ ] Form labels/instructions provided
- [ ] Input errors identified and described
- [ ] Error prevention for legal/financial/data changes

### Robust
- [ ] Valid HTML (no parsing errors)
- [ ] Name, role, value available for all UI components
- [ ] Status messages identified (aria-live)

---

## Known Issues Prevention

| # | Issue | WCAG | Prevention |
|---|-------|------|------------|
| 1 | Missing focus indicators | 2.4.7 | Always provide custom focus-visible styles |
| 2 | Insufficient contrast | 1.4.3 | Test all text colors with contrast checker |
| 3 | Missing alt text | 1.1.1 | Add alt="" for decorative, descriptive for meaningful |
| 4 | Keyboard nav broken | 2.1.1 | Use semantic interactive elements (button, a) |
| 5 | Inputs without labels | 3.3.2 | Always use `<label>` with for/id association |
| 6 | Skipped heading levels | 1.3.1 | Use headings in order, style with CSS |
| 7 | No focus trap in dialogs | 2.4.3 | Implement focus trap for modal dialogs |
| 8 | No aria-live for dynamic content | 4.1.3 | Use aria-live="polite" or "assertive" |
| 9 | Color-only information | 1.4.1 | Add icon + text label, not just color |
| 10 | Non-descriptive link text | 2.4.4 | Use descriptive text or aria-label |
| 11 | Auto-playing media | 1.4.2 | Require user interaction to start media |
| 12 | Inaccessible custom controls | 4.1.2 | Use native elements or implement full ARIA pattern |

---

## Testing Workflow

### 1. Keyboard-Only Testing (5 min)
1. Tab through entire page — can you reach all interactive elements?
2. Enter/Space to activate buttons/links
3. Escape to close dialogs
4. Arrow keys in menus/tabs
5. Is focus order logical?

### 2. Screen Reader Testing (10 min)
- **NVDA** (Windows): Ctrl+Alt+N to start, arrows/Tab to navigate, NVDA+Q to stop
- **VoiceOver** (Mac): Cmd+F5 to start, VO+Right/Left to navigate

Check: Are all elements announced? Images described? Form labels read? Dynamic updates announced?

### 3. Automated Testing
- **axe DevTools**: Browser extension, F12 > axe tab > Scan
- **Lighthouse**: F12 > Lighthouse tab > Accessibility category. Score 90+ good, 100 ideal

---

## Key Patterns

### Dialog/Modal
- Focus first element on open, trap focus within, restore focus on close
- Use `role="dialog"`, `aria-modal="true"`, `aria-labelledby`
- Close on Escape key

### Tabs
- `role="tablist"` container, `role="tab"` buttons, `role="tabpanel"` content
- Arrow keys navigate tabs, `aria-selected` marks active, `tabindex="-1"` on inactive
- Home/End jump to first/last tab

### Skip Links
- Place `<a href="#main-content" class="skip-link">Skip to main content</a>` at top of body
- Visually hidden until focused (position absolute, show on :focus)

### ARIA Live Regions
- `aria-live="polite"` — non-critical updates (notifications, counters)
- `aria-live="assertive"` — errors and critical alerts
- `aria-atomic="true"` — read entire region on change

### SPA Focus Management
- Reset focus to main content on route change (React Router doesn't do this)
- Announce page title to screen readers via `role="status"` + `aria-live="polite"`

### Data Tables
- `<caption>` describes purpose, `scope="col"` / `scope="row"` on header cells

---

## Complete Page Checklist

- [ ] All interactive elements keyboard accessible
- [ ] Visible focus indicators on all focusable elements
- [ ] Images have alt text
- [ ] Text contrast >= 4.5:1
- [ ] Form inputs have associated labels
- [ ] Heading hierarchy logical (no skipped levels)
- [ ] Page has `<html lang="en">`
- [ ] Dialogs have focus trap and restore focus on close
- [ ] Dynamic content uses aria-live or role="alert"
- [ ] Color not used alone to convey information
- [ ] Tested with keyboard only
- [ ] Tested with screen reader
- [ ] axe DevTools scan: 0 violations
- [ ] Lighthouse accessibility >= 90

---

## References

- **WCAG 2.1**: https://www.w3.org/WAI/WCAG21/quickref/
- **ARIA Authoring Practices**: https://www.w3.org/WAI/ARIA/apg/
- **axe DevTools**: https://www.deque.com/axe/devtools/
- Bundled references: `references/wcag-checklist.md`, `semantic-html.md`, `aria-patterns.md`, `focus-management.md`, `color-contrast.md`, `forms-validation.md`
- Agent: `agents/a11y-auditor.md` for automated page auditing
