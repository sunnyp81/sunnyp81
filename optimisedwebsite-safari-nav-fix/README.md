# OptimisedWebsite — iPhone Safari/Edge nav fix

Target repo: **sunnyp81/optimisedwebsite** (Astro). This session was scoped to
`sunnyp81/sunnyp81`, so the fix could not be pushed to the website repo directly.
The change is preserved here as `safari-nav-fix.patch` until a session scoped to
`optimisedwebsite` can land it.

## The bug
On an iPhone in dark mode, Safari and Edge follow the system setting and load the
site's dark theme (dark-navy body, near-white text via `--color-ink`). But
`src/components/Nav.astro` hardcoded the **light beige** background inline on both
the fixed header and the mobile menu (`rgba(255,251,235,…)`). The JS that swaps
those to dark navy (`updateNavBg` / `updateMobileBg`) only ran on `scroll` and on
theme-toggle, **never on initial load** — so first paint was beige background +
white text = unreadable. Matches the reported screenshots (top bar + open menu).

## The fix
- `src/styles/global.css`: added theme-aware vars `--nav-bg`, `--nav-bg-scrolled`,
  `--nav-border(-scrolled)`, `--nav-shadow-scrolled`, `--menu-bg` — light values in
  `:root`, dark-navy values under `html.dark`.
- `src/components/Nav.astro`: header + mobile-menu backgrounds now read those
  variables, so they are correct on first paint (no flash, no JS dependency). The
  scroll handler was simplified to use the same variables and is synced on load.

Build verified clean (54 pages).

## Apply
```bash
cd /path/to/optimisedwebsite
git apply /path/to/safari-nav-fix.patch
npm run build
```
