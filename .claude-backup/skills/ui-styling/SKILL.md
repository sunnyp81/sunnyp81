---
name: ui-styling
description: Create beautiful, accessible user interfaces with shadcn/ui components (built on Radix UI + Tailwind), Tailwind CSS utility-first styling, and canvas-based visual designs. Use when building user interfaces, implementing design systems, creating responsive layouts, adding accessible components, customizing themes, or establishing consistent styling patterns.
argument-hint: "[component or layout]"
user-invocable: true
allowed-tools: Read, Write, Bash
license: MIT
metadata:
  author: claudekit
  version: "1.0.0"
version: 1.0.0
---

# UI Styling Skill

Create accessible UIs with shadcn/ui + Tailwind CSS + canvas-based visual design.

## Reference
- shadcn/ui: https://ui.shadcn.com/llms.txt
- Tailwind CSS: https://tailwindcss.com/docs

## When to Use

- Building UI with React frameworks (Next.js, Vite, Remix, Astro)
- Implementing accessible components (dialogs, forms, tables, navigation)
- Utility-first CSS styling, responsive layouts, dark mode
- Building design systems, rapid prototyping
- Visual designs, posters, brand materials

## Core Stack

| Layer | What | Key Features |
|-------|------|-------------|
| Components | shadcn/ui (Radix UI) | Accessible, copy-paste, TypeScript-first, composable |
| Styling | Tailwind CSS | Utility-first, zero runtime, mobile-first, auto dead-code elimination |
| Visual Design | Canvas | Museum-quality compositions, philosophy-driven, minimal text |

## Quick Start

```bash
npx shadcn@latest init          # Setup shadcn/ui + Tailwind
npx shadcn@latest add button card dialog form  # Add components
```

**Tailwind-only (Vite):**
```bash
npm install -D tailwindcss @tailwindcss/vite
```
```javascript
// vite.config.ts
import tailwindcss from '@tailwindcss/vite'
export default { plugins: [tailwindcss()] }
```
```css
/* src/index.css */
@import "tailwindcss";
```

## Reference Files

| Topic | File | Covers |
|-------|------|--------|
| Components | `references/shadcn-components.md` | Forms, layout, overlays, feedback, display components |
| Theming | `references/shadcn-theming.md` | Dark mode, CSS variables, color customization |
| Accessibility | `references/shadcn-accessibility.md` | ARIA, keyboard nav, focus management, screen readers |
| Utilities | `references/tailwind-utilities.md` | Layout, spacing, typography, colors, borders |
| Responsive | `references/tailwind-responsive.md` | Breakpoints, container queries, mobile-first |
| Customization | `references/tailwind-customization.md` | @theme, custom tokens, plugins, layers |
| Visual Design | `references/canvas-design-system.md` | Design philosophy, composition, systematic patterns |

## Utility Scripts

```bash
python scripts/shadcn_add.py button card dialog   # Add components with deps
python scripts/tailwind_config_gen.py --colors brand:blue --fonts display:Inter  # Generate config
```

## Best Practices

1. **Utility-First**: Use Tailwind classes directly; extract components only for true repetition
2. **Mobile-First**: Start mobile, layer responsive variants (`sm:`, `md:`, `lg:`)
3. **Accessibility-First**: Use Radix primitives, focus states, semantic HTML
4. **Design Tokens**: Consistent spacing, color palettes, typography scale
5. **Dark Mode**: Apply dark variants to all themed elements; test both modes
6. **Performance**: Leverage CSS purging, avoid dynamic class names
7. **TypeScript**: Full type safety for better DX
8. **Visual Hierarchy**: Spacing and color guide attention intentionally

## Common Patterns

**Form with validation:** Use `react-hook-form` + `zod` + shadcn Form components. See `references/shadcn-components.md`.

**Responsive layout with dark mode:**
```tsx
<div className="min-h-screen bg-white dark:bg-gray-900">
  <div className="container mx-auto px-4 py-8">
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <Card className="bg-white dark:bg-gray-800 border-gray-200 dark:border-gray-700">
        <CardContent className="p-6">
          <h3 className="text-xl font-semibold text-gray-900 dark:text-white">Content</h3>
        </CardContent>
      </Card>
    </div>
  </div>
</div>
```

## Resources

- shadcn/ui: https://ui.shadcn.com
- Tailwind CSS: https://tailwindcss.com
- Radix UI: https://radix-ui.com
- v0 (AI UI Generator): https://v0.dev
