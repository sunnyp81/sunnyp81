# Design: Puppeteer Pinterest Pin Generator
**Date:** 2026-04-02  
**Site:** shecookssheeats.co.uk  
**Replaces:** Gemini image generation (nano-banana)  
**Goal:** Generate Pinterest pin images for free using Puppeteer + existing WP media

---

## Problem

Gemini 3 Pro Image API (`gemini-3-pro-image-preview`) charges per image generation call. With 50 pins/month, costs are significant. Quality is also non-deterministic — the model sometimes ignores layout instructions.

## Solution

Replace Gemini image generation with:
1. **Real food photos** pulled from the site's own WordPress media library via REST API
2. **HTML/CSS pin templates** rendered deterministically with all layout, typography, and brand rules baked in
3. **Puppeteer** to screenshot the rendered HTML at 1000×1500px (2:3 ratio)

Cost: **free**. Quality: **deterministic** (no hallucinated layouts). Photos: **authentic** (real recipe images from the site).

---

## Data Flow

```
Input: article slug + board ID + layout type
    ↓
WP REST API: GET /wp/v2/posts?slug={slug}
    → extract featured_media ID
    → parse content.rendered for <img> src URLs (up to 6)
    → if <6 images: GET /wp/v2/media?per_page=20 for fallback food photos
    ↓
buildHtml(layout, { images, headline, subtitle, colour, url })
    → returns HTML string with inline styles + Google Fonts CDN
    ↓
Puppeteer: launch headless Chrome
    page.setViewport({ width: 1000, height: 1500 })
    page.setContent(html, { waitUntil: 'networkidle0' })
    page.screenshot({ type: 'png' }) → Buffer
    ↓
WP media upload: POST /wp/v2/media (multipart)
    → returns { source_url }
    ↓
Append to scse_june_queue.json:
    { status: 'pending', board_id, title, description, link, image_url }
    ↓
Existing Task Scheduler (pinterest_daily.bat) posts 2 pins/day
```

---

## HTML Templates

### Fonts (Google Fonts CDN — loaded in every template)
- **Bebas Neue** — headline (bold condensed, impact-style)
- **Dancing Script** — subtitle (elegant script)
- **Inter** — body, URL, CTA

### Layout A: Collage Grid (primary — used for roundups)
```
┌─────────────────────────┐
│   [SOLID COLOUR BLOCK]  │ 22%
│   15  SYN FREE DINNERS  │
├─────────┬───────────────┤
│ photo 1 │   photo 2     │ 
├─────────┼───────────────┤ 53%
│ photo 3 │   photo 4     │
├─────────┼───────────────┤
│ photo 5 │   photo 6     │
├─────────┴───────────────┤
│   [SOLID COLOUR BLOCK]  │ 25%
│  Quick & Easy Family    │
│  [READ MORE] [url]      │
└─────────────────────────┘
```
- Grid: CSS Grid, `gap: 4px`, `background: white` (gap colour)
- Number: Bebas Neue, ~180px, white
- Headline: Bebas Neue, ~60px, white
- Subtitle: Dancing Script, ~36px, cream
- Purple `#473f99` border 3px around entire pin

### Layout B: Hero + Row
```
┌─────────────────────────┐
│   [SOLID COLOUR BLOCK]  │ 20%
│   CHICKEN STIR-FRY      │
├─────────────────────────┤
│                         │
│     [LARGE PHOTO]       │ 45%
│                         │
├─────────┬───────────────┤
│ photo 2 │   photo 3     │ 15%
├─────────────────────────┤
│   [SOLID COLOUR BLOCK]  │ 20%
│  Syn Free & Ready in 20 │
│  [READ MORE] [url]      │
└─────────────────────────┘
```

### Layout C: Guide / Tips
```
┌─────────────────────────┐
│   [SOLID COLOUR BLOCK]  │ 18%
│   SYN COUNT GUIDE       │
├─────────────────────────┤
│ ① Tip card (icon+text) │
├─────────────────────────┤ 62%
│ ② Tip card (icon+text) │
├─────────────────────────┤
│ ③ Tip card (icon+text) │
├─────────────────────────┤
│   [SOLID COLOUR BLOCK]  │ 20%
│  [READ MORE] [url]      │
└─────────────────────────┘
```
- Tip cards: alternating white / light-cream backgrounds
- Icons: Unicode food emoji or CSS shapes (no external assets needed)

### Colour Palette Assignment (by content type)
| Content type | Background | Text |
|---|---|---|
| Dinner recipes | Terracotta `#C67B5C` | White |
| Healthy/diet | Sage `#8B9A6B` | White |
| Desserts/treats | Warm pink `#D4878F` | White |
| Lists/guides | Brand purple `#473f99` | White |
| Breakfast | Mustard `#D4A843` | Dark charcoal |
| Fakeaway/takeaway | Deep red `#B84233` | White |

---

## Script Structure

**File:** `C:\Users\sunny\AppData\Local\Temp\scse_june_prep.js`

```javascript
// Dependencies: puppeteer, node-fetch (built-in fetch in Node 18+)
// No Gemini API key needed

async function fetchPostImages(slug)     // → string[] of image URLs
async function buildHtml(layout, data)   // → HTML string
async function screenshotPin(html)       // → Buffer (PNG)
async function uploadToWP(buffer, name)  // → { source_url }
// main: loop 50 pins → scse_june_queue.json

// Resume support: node scse_june_prep.js 10 → starts from pin 11
```

### fetchPostImages(slug)
1. `GET /wp/v2/posts?slug={slug}&context=edit` with Basic auth
2. Extract `featured_media` → `GET /wp/v2/media/{id}` → `source_url`
3. Parse `content.rendered` with regex for `<img[^>]+src="([^"]+)"` → collect up to 5 more
4. Deduplicate, filter to `.jpg|.jpeg|.png|.webp`
5. If total < 3: `GET /wp/v2/media?per_page=20&mime_type=image/jpeg&orderby=rand` → pad to 6

### buildHtml(layout, data)
- Inline all styles (no external CSS files)
- Google Fonts via `<link>` CDN (loads before Puppeteer screenshots)
- Images loaded via `<img src="[wp_url]">` — Puppeteer fetches them directly
- Brand purple border via CSS `outline` on the outermost div

### screenshotPin(html)
```javascript
const browser = await puppeteer.launch({ headless: 'new' });
const page = await browser.newPage();
await page.setViewport({ width: 1000, height: 1500, deviceScaleFactor: 2 });
await page.setContent(html, { waitUntil: 'networkidle0' });
const buffer = await page.screenshot({ type: 'png', clip: { x:0, y:0, width:1000, height:1500 } });
await browser.close();
return buffer;
```
`deviceScaleFactor: 2` → outputs 2000×3000px retina-quality image, saved at 2x resolution for Pinterest sharpness.

### Queue format (matches existing scheduler)
```json
{
  "pins": [
    {
      "id": 1,
      "status": "pending",
      "board_id": "771523048604574770",
      "title": "15 Syn Free Slimming World Dinners",
      "description": "...",
      "link": "https://shecookssheeats.co.uk/...",
      "image_url": "https://shecookssheeats.co.uk/wp-content/uploads/2026/04/pin-june-001.png"
    }
  ]
}
```

---

## Pin Data (June — 50 pins)

Same articles as prior months — new layouts, new image selections, rotated colour palettes. No new articles needed; re-pin high-traffic pages with fresh designs.

Top articles to re-pin (by WP traffic/impressions):
- `/low-syn-drinks/` — 906 impr
- `/syns-nuts/` — 485 impr
- `/syns-rice-cakes/` — 544 impr
- `/best-slimming-world-recipes/` — high Bing impr
- All "Calories in X" pages published Mar 2026

---

## Dependencies

| Package | Purpose | Install |
|---|---|---|
| `puppeteer` | Headless Chrome screenshots | `npm install puppeteer` |
| Node 18+ built-in `fetch` | WP API calls | None |

No Gemini API key. No new accounts. No cost.

---

## What Stays the Same

- `scse_pinterest_scheduler.js` — unchanged
- `pinterest_daily.bat` — unchanged  
- `Pinterest_May_Pins` Windows Task — clone for June (`Pinterest_June_Pins`)
- Activepieces MCP for posting — unchanged
- Queue JSON format — identical

---

## Success Criteria

- [ ] 50 pin images generated without any API image generation costs
- [ ] Each pin uses real food photos from the target article (or WP media fallback)
- [ ] All 3 layout types render correctly at 2000×3000px
- [ ] Uploaded to WP media library successfully
- [ ] Queue JSON compatible with existing scheduler
- [ ] `node scse_june_prep.js N` resume works correctly
