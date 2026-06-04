# Handoff: deadhangs.com homepage bug fixes

> The code is NOT in this repo (`sunnyp81/sunnyp81` is just the `.claude` config backup).
> The homepage lives in **`sunnyp81/deadhangs-com`** (local: `G:/My Drive/archive/deadhangs_site`, deploy via Wrangler).
> Open a web session scoped to `sunnyp81/deadhangs-com` and paste the task below.

## Task: fix two deadhangs.com homepage bugs

### 1. Eyebrow ticker renders doubled / ghosted
The line under the nav — "GRIP STRENGTH · LONGEVITY PROTOCOL · 90 SEC READ" — shows an
offset duplicate sitting behind it (looks like double-vision text).

Where to look: the marquee/ticker block on the homepage `index.html` (and its CSS/JS).
Likely causes:
- A duplicated track for infinite-scroll that's mispositioned (second copy not offset by
  exactly 100% / track width).
- An `animation`/`transform` left in a stale state (e.g. `translateX` not resetting).
- A doubled DOM node rendering on top of itself instead of after itself.

Fix so only one clean copy is visible (or a single seamless scroll).

### 2. Animated stats graph glitches
The area chart in the "mortality risk" / Lancet 2015 section has a tooltip/value box
clipping at the top-right corner and a jagged path draw.

Where to look: the chart script (inline SVG/canvas or a small JS animator) in the stats
section. Fix:
- Tooltip/value label clipping — give the chart container `overflow: visible` or clamp the
  label position so it stays inside the viewBox/bounds.
- The path/area draw animation jitter — check the stroke-dash / point interpolation.

## Ship
1. Develop on a feature branch (e.g. `claude/deadhangs-graph-glitch`).
2. Commit with clear messages, `git push -u origin <branch>`.
3. deadhangs needs a **manual** deploy after push (not auto-deployed):
   `wrangler pages deploy . --project-name deadhangs-com` (see `master-builds.md`).

## Reference screenshots
Two phone screenshots provided by Sunny:
- Hero "HANG. LONGER. LIVE. LONGER." with the doubled eyebrow ticker.
- Stats section with the glitchy animated area chart + clipped tooltip.
