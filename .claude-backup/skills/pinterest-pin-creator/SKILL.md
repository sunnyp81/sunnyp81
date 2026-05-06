---
name: pinterest-pin-creator
description: Create high-performing Pinterest pin images using Gemini Pro Image via Node.js. Use when creating Pinterest pins for food, recipe, diet, or lifestyle content. Generates pins matching real top-performer patterns — photo collage grids, bold text blocks, large numbers, mixed typography, warm backgrounds. Auto-uploads to WordPress and posts to Pinterest via Activepieces MCP. Trigger on "create pin", "Pinterest image", "pin design", or "generate pin".
version: 3.0.0
user-invocable: true
allowed-tools: Read, Write, Bash, WebFetch
argument-hint: "[article URL or title] [topic]"
---

# Pinterest Pin Creator v3 — Top Performer Edition

Generate pins that match ACTUAL top-performing Pinterest food pin patterns. Based on analysis of real high-save-rate pins in the food/recipe niche.

## What Real Top Performers Look Like

Top-performing food pins are NOT cinematic single-hero shots. They are **graphic design collage layouts**:

- **Photo grids** showing 4-6 different dishes (variety = saves)
- **Bold coloured text blocks** (not transparent overlays — solid warm backgrounds)
- **Large numbers** for listicle pins ("15", "13+", "25")
- **Mixed typography** — heavy bold sans-serif + elegant script accent font
- **Warm earth-tone backgrounds** — cream, terracotta, sage, mustard
- **"READ MORE" buttons** or CTA elements
- **Decorative borders** — thin lines, frames, or geometric accents
- **Brand colour integration** in text blocks, borders, and accent elements

## Generation Method (Node.js Only)

Python is unreliable on this system. Always use Node.js with the Gemini REST API:

```javascript
const payload = JSON.stringify({
  contents: [{ parts: [{ text: JSON.stringify(prompt) }] }],
  generationConfig: { responseModalities: ['IMAGE', 'TEXT'], temperature: 1.0 }
});

const res = await fetch(
  'https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-image-preview:generateContent?key=' + GEMINI_KEY,
  { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: payload }
);
```

**API key:** Load from `C:\Users\sunny\.claude\skills\nano-banana\.env` -> `GEMINI_API_KEY`
**Model:** `gemini-3-pro-image-preview`
**Response:** Base64 image in `response.candidates[0].content.parts[].inlineData.data`

## The Top Performer Design System

### Pin Type A: Recipe Roundup / Listicle (Highest performers)

```json
{
  "meta": { "task": "pinterest_pin_collage", "aspect_ratio": "2:3", "design_tier": "top_performer_graphic" },
  "design_system": {
    "style": "graphic design collage pin — like a magazine article preview or recipe roundup. NOT a single photograph. This is a DESIGNED LAYOUT with multiple photos arranged in a grid pattern with bold text blocks between them.",
    "layout_type": "photo_grid_with_text_blocks",
    "structure": [
      "TOP 20%: solid warm background colour block with large bold headline text",
      "MIDDLE 55%: grid of 4-6 food photographs arranged in 2x2 or 2x3 grid with thin gaps between them",
      "BOTTOM 25%: solid warm background colour block with subtitle text, brand URL, and optional READ MORE button"
    ]
  },
  "typography": {
    "headline": {
      "text": "[LARGE NUMBER + SHORT PHRASE — e.g. '15 SYN FREE DINNERS']",
      "font_style": "ultra-bold heavy sans-serif like Impact or Bebas Neue",
      "color": "white #FFFFFF or dark charcoal for contrast",
      "size": "ENORMOUS — the number is the biggest element. '15' should dominate the top block",
      "position": "centered in top colour block"
    },
    "subtitle": {
      "text": "[Supporting phrase — e.g. 'Quick & Easy Family Recipes']",
      "font_style": "elegant script or thin italic serif — contrasts with the bold headline",
      "color": "white or cream",
      "size": "medium, decorative, sits below or integrated with headline"
    },
    "cta": {
      "text": "READ MORE",
      "font_style": "small caps, medium weight sans-serif, inside a pill-shaped button or underlined",
      "color": "white on darker background accent"
    },
    "footer": {
      "text": "shecookssheeats.co.uk",
      "font_style": "clean sans-serif, medium weight",
      "color": "white #FFFFFF",
      "position": "bottom of the pin, centered"
    }
  },
  "photo_grid": {
    "count": "4-6 food photographs",
    "arrangement": "2x2 or 2x3 grid with 4-6px white or cream gaps between images",
    "each_photo": "individual dish photograph — bright, warm lighting, overhead or 45-degree angle, appetising and colourful",
    "variety": "each photo shows a DIFFERENT dish — variety of colours, proteins, and presentation styles",
    "quality": "each photo looks like real food photography — NOT stock, natural warm lighting, visible texture"
  },
  "colour_palette": {
    "background_blocks": "[CHOOSE ONE: warm cream #F5E6D3, sage green #8B9A6B, terracotta #C67B5C, mustard gold #D4A843, or brand purple #473f99]",
    "text_on_background": "white #FFFFFF (on dark backgrounds) or dark charcoal #2D2D2D (on light backgrounds)",
    "grid_gaps": "white or cream #FFF8F0",
    "accents": "brand purple #473f99 as thin border lines, decorative elements, or button backgrounds"
  },
  "brand_integration": {
    "primary": "#473f99 deep purple",
    "usage": "thin decorative border around entire pin, accent lines between sections, CTA button background, or as one of the background block colours",
    "method": "Purple appears as graphic design elements — borders, lines, buttons. NOT as photographic effects or gradients over food."
  },
  "constraints": {
    "exclusions": ["single hero food photograph", "cinematic magazine cover style", "gradient overlays on food", "bokeh backgrounds", "dark moody lighting", "landscape format", "transparent text overlays"],
    "requirements": ["photo GRID/COLLAGE layout", "solid colour text blocks", "bold headline with large number", "mixed font styles (bold + script)", "warm colour palette", "brand URL visible", "vertical 2:3 ratio", "each food photo bright and appetising"]
  }
}
```

### Pin Type B: Single Dish Feature

For single-recipe pins, still use graphic design layout (not pure photography):

```json
{
  "meta": { "task": "pinterest_pin_single_recipe", "aspect_ratio": "2:3" },
  "design_system": {
    "style": "graphic design pin with one large hero food photo and bold text blocks above and below",
    "structure": [
      "TOP 25%: solid warm colour block with bold headline text stacked on 2 lines",
      "MIDDLE 55%: single large food photograph — bright, warm, overhead or 45-degree angle",
      "BOTTOM 20%: solid colour block with subtitle, brand URL, decorative border"
    ]
  },
  "typography": {
    "headline": {
      "text": "[2-4 WORDS, ALL CAPS, STACKED — e.g. 'CHICKEN\\nSTIR-FRY']",
      "font_style": "ultra-bold condensed sans-serif, extremely heavy weight",
      "color": "white #FFFFFF",
      "size": "MASSIVE — fills 85% of the text block width",
      "effects": "clean flat text on solid background — no drop shadows needed because background provides contrast"
    },
    "subtitle": {
      "text": "[Benefit hook — e.g. 'Syn Free & Ready in 20 Minutes']",
      "font_style": "elegant script or light italic",
      "color": "white or cream at 90% opacity"
    }
  },
  "food_photography": {
    "style": "bright, warm, appetising — real food photography look",
    "lighting": "natural window light, warm 4000K, soft shadows",
    "angle": "45-degree or overhead",
    "details": "visible steam, glistening sauce, fresh herbs, crisp vegetables — texture and colour"
  }
}
```

### Pin Type C: Tips / Guide Pin

```json
{
  "meta": { "task": "pinterest_pin_guide", "aspect_ratio": "2:3" },
  "design_system": {
    "style": "infographic-style pin with numbered sections or tip cards arranged vertically",
    "structure": [
      "TOP 20%: bold headline on solid colour background",
      "MIDDLE 60%: 3-5 tip cards or numbered items, each with small icon or food photo + short text",
      "BOTTOM 20%: CTA button + brand URL on solid colour background"
    ]
  }
}
```

## Headline Rules

| Rule | Detail |
|------|--------|
| Numbers first | "15 SYN FREE DINNERS" not "Syn Free Dinners — 15 Recipes" |
| Number is BIGGEST | The number should be 2-3x larger than other text |
| ALL CAPS for headline | Always uppercase for the main headline |
| Script for subtitle | Use elegant/script font for the supporting line |
| 3-8 words max | Scannable at thumbnail size |
| Benefit-driven | What does the reader GET? |

**Headline transformations:**
- "Syn Free Dinner Recipes" -> "15 SYN FREE DINNERS" + subtitle "Quick Family Meals"
- "Speed Foods List" -> "SPEED FOODS UNLOCKED" + subtitle "The Complete Guide"
- "Takeaway Syn Guide" -> "FAKEAWAY FRIDAY" + subtitle "Every Chain Counted"
- "Chicken Recipes" -> "25 CHICKEN DINNERS" + subtitle "The Family Will Love"

## Colour Palettes by Content Type

| Content | Primary Background | Accent |
|---------|-------------------|--------|
| Dinner recipes | Terracotta #C67B5C | Brand purple #473f99 |
| Healthy/diet | Sage green #8B9A6B | Cream #F5E6D3 |
| Desserts/treats | Warm pink #D4878F | Gold #D4A843 |
| Lists/guides | Brand purple #473f99 | Cream #F5E6D3 |
| Breakfast | Mustard gold #D4A843 | Sage #8B9A6B |
| Fakeaway/takeaway | Deep red #B84233 | Gold #D4A843 |

## Full Pipeline (Node.js)

```
1. Build collage-style JSON prompt for the pin
2. POST to Gemini 3 Pro Image API -> receive base64 PNG
3. Save locally to ~/Downloads/
4. Upload to WordPress via REST API (multipart form)
5. Post to Pinterest via Activepieces MCP (board_id, title, description, link, image_url)
```

See `references/food-pin-templates.md` for ready-to-use prompt templates per category.

## Activepieces MCP Details

- **URL:** `https://cloud.activepieces.com/api/v1/projects/ixFBjSaUSXD1p0cedG5uJ/mcp-server/http`
- **Token:** Load from config or use stored value
- **Tool:** `create_pinterest_pin_kexi_rfy0ow_mcp`
- **Params:** `board_id`, `title`, `description`, `link`, `image_url`
- **Response format:** SSE — parse last `data:` line for result

## Board IDs (shecookssheeats.co.uk)

```
synCount:    771523048604274536
foodInspo:   771523048604561727
weightLoss:  771523048604569270
dinner:      771523048604574770
yummy:       771523048603350488
breakfast:   771523048604564585
lowSyn:      771523048604570705
chicken:     771523048603322381
snacks:      771523048604561724
vegan:       771523048604562061
```

## Workflow

1. User provides: title, URL, topic
2. Choose pin type (A: roundup collage, B: single dish, C: guide)
3. Select colour palette based on content type
4. Transform title into bold headline + script subtitle
5. Build prompt using Top Performer Design System
6. Generate via Gemini 3 Pro Image REST API (Node.js)
7. Upload to WordPress media library
8. Post to Pinterest via Activepieces MCP
9. Create 3-5 variations per article for maximum reach

## References

- `references/food-pin-templates.md` — Ready-to-use prompt templates per pin type
- `references/pinterest-aesthetics.md` — Colour psychology and performance data
