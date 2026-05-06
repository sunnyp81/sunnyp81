# Food Pin Templates — Top Performer Collage Style

## Template A: Recipe Roundup / Listicle (Highest Save Rate)

Use for: "15 Syn Free Dinners", "25 Chicken Recipes", "10 Speed Food Breakfasts"

```json
{
  "meta": { "task": "pinterest_pin_collage", "aspect_ratio": "2:3", "design_tier": "top_performer_graphic" },
  "design_system": {
    "style": "graphic design collage pin — a designed layout with multiple food photos in a grid, bold coloured text blocks, mixed typography. Looks like a recipe magazine article preview, NOT a single photograph.",
    "layout_type": "photo_grid_with_text_blocks",
    "structure": [
      "TOP SECTION (top 22%): solid [BACKGROUND_COLOUR] colour block. Contains the headline number '[NUMBER]' in enormous ultra-bold font, with '[HEADLINE_TEXT]' in bold condensed sans-serif below/beside it. A thin decorative line or accent in brand purple #473f99 separates text from photos.",
      "PHOTO GRID (middle 53%): [4-6] food photographs arranged in a [2x2 or 2x3] grid pattern. Each photo has a 4px white gap between them. Photos are bright, warm, overhead or 45-degree angle food photography showing different dishes.",
      "BOTTOM SECTION (bottom 25%): solid [BACKGROUND_COLOUR] colour block. Contains subtitle '[SUBTITLE]' in elegant script font, then 'READ MORE' in a small pill-shaped button in brand purple #473f99, then 'shecookssheeats.co.uk' in clean white sans-serif at the very bottom."
    ],
    "decorative_elements": [
      "thin brand purple #473f99 border around the entire pin (2-3px)",
      "thin decorative line between top text block and photo grid",
      "small decorative flourish or arrow near the subtitle"
    ]
  },
  "typography": {
    "number": {
      "text": "[NUMBER — e.g. '15', '25', '13+']",
      "font_style": "ultra-bold condensed sans-serif, enormous weight",
      "color": "white #FFFFFF",
      "size": "HUGE — this number is 3x bigger than any other text. It dominates the top section."
    },
    "headline": {
      "text": "[SHORT PHRASE — e.g. 'SYN FREE DINNERS', 'CHICKEN RECIPES']",
      "font_style": "bold condensed sans-serif, all caps",
      "color": "white #FFFFFF",
      "size": "large, sits directly below or beside the number"
    },
    "subtitle": {
      "text": "[BENEFIT — e.g. 'Quick & Easy Family Meals', 'The Whole Family Will Love']",
      "font_style": "elegant cursive script or thin italic serif — beautiful contrast with the bold headline",
      "color": "white or cream #FFF8F0",
      "size": "medium"
    },
    "cta": {
      "text": "READ MORE",
      "font_style": "small caps, medium weight, inside a pill-shaped or rounded rectangle button",
      "color": "white text on brand purple #473f99 button background",
      "size": "small, between subtitle and URL"
    },
    "footer": {
      "text": "shecookssheeats.co.uk",
      "font_style": "clean light sans-serif, letter-spaced",
      "color": "white at 80% opacity",
      "size": "small, at the very bottom"
    }
  },
  "photo_grid": {
    "count": "[4 or 6]",
    "arrangement": "[2x2 or 2x3] grid with 4px white gaps between each photo",
    "photos": [
      "[DISH 1: specific description — e.g. 'golden-brown roast chicken with crispy skin on a white plate, fresh rosemary visible']",
      "[DISH 2: specific description — e.g. 'colourful stir-fry with bright vegetables and glossy sauce in a dark bowl']",
      "[DISH 3: specific description — e.g. 'creamy pasta with cherry tomatoes and fresh basil, parmesan shavings on top']",
      "[DISH 4: specific description — e.g. 'grilled salmon fillet with lemon wedge and steamed green vegetables']"
    ],
    "photo_style": "each photo: bright natural lighting, warm tones, overhead or 45-degree angle, real food photography, appetising texture visible, NOT stock photography"
  },
  "colour_palette": {
    "background_blocks": "[CHOOSE: terracotta #C67B5C, sage green #8B9A6B, brand purple #473f99, mustard #D4A843, or deep red #B84233]",
    "text": "white #FFFFFF",
    "grid_gaps": "white #FFFFFF",
    "accent": "brand purple #473f99",
    "overall_warmth": "warm — the entire pin should feel warm, inviting, and appetising"
  },
  "brand_integration": {
    "primary": "#473f99 deep purple",
    "usage": ["thin border around entire pin", "READ MORE button background", "decorative accent lines", "optionally as the background block colour for lists/guides content"]
  },
  "constraints": {
    "exclusions": ["single hero photograph", "cinematic gradient overlays", "bokeh effects", "dark moody lighting", "transparent text on food", "landscape format", "cold tones"],
    "requirements": ["photo COLLAGE grid layout with multiple dishes", "solid colour text blocks (not transparent)", "enormous bold number as largest text element", "mixed fonts: bold sans-serif + script", "warm appetising colour palette", "brand purple accent elements", "READ MORE button or CTA", "brand URL at bottom", "vertical 2:3 ratio"]
  }
}
```

**Fill-in examples:**

| Article | Number | Headline | Subtitle | Grid | Background |
|---------|--------|----------|----------|------|------------|
| 15 Syn Free Dinners | 15 | SYN FREE DINNERS | Quick & Easy Family Meals | 2x3: 6 different dinner photos | Terracotta #C67B5C |
| 25 Chicken Recipes | 25 | CHICKEN RECIPES | Weeknight Winners | 2x3: 6 chicken dish photos | Sage #8B9A6B |
| Speed Foods List | 50+ | SPEED FOODS | Eat Free, Lose Weight | 2x3: 6 colourful ingredient photos | Brand purple #473f99 |
| Meal Plan | 7 | DAY MEAL PLAN | Your Week Sorted | 2x2: 4 different meal photos | Mustard #D4A843 |

---

## Template B: Single Dish Feature

Use for: individual recipe pins, hero dish features

```json
{
  "meta": { "task": "pinterest_pin_single", "aspect_ratio": "2:3" },
  "design_system": {
    "style": "graphic design pin with ONE large food photo framed by bold coloured text blocks. Still a designed layout — NOT a raw photograph with text overlaid on top of the food.",
    "structure": [
      "TOP SECTION (top 25%): solid [BACKGROUND_COLOUR] block. Bold stacked headline '[LINE1]\\n[LINE2]' in ultra-bold white condensed sans-serif. Thin brand purple accent line at bottom edge.",
      "HERO PHOTO (middle 55%): single large food photograph filling this entire zone. Bright, warm, shallow depth of field. The photo has clean edges meeting the colour blocks above and below.",
      "BOTTOM SECTION (bottom 20%): solid [BACKGROUND_COLOUR] block. Subtitle in elegant script font, brand URL in small clean text. Optional thin purple border around entire pin."
    ]
  },
  "typography": {
    "headline": {
      "text": "[2-4 WORDS STACKED — e.g. 'FAKEAWAY\\nFRIDAY' or 'CHICKEN\\nSTIR-FRY']",
      "font_style": "ultra-bold condensed sans-serif, all caps",
      "color": "white #FFFFFF",
      "size": "MASSIVE — fills 80% of top block width"
    },
    "subtitle": {
      "text": "[BENEFIT — e.g. 'Every Chain Counted' or 'Syn Free & 20 Minutes']",
      "font_style": "elegant script or light italic serif",
      "color": "white or cream"
    },
    "footer": {
      "text": "shecookssheeats.co.uk",
      "font_style": "clean light sans-serif",
      "color": "white at 80% opacity"
    }
  },
  "food_photography": {
    "subject": "[SPECIFIC DISH: e.g. 'a towering gourmet burger with melting cheese dripping down, golden sesame bun, fresh lettuce and tomato visible, served on brown kraft paper']",
    "style": "bright, warm, real food photography — natural window light, visible texture (steam, glistening sauce, crispy edges), appetising and crave-worthy",
    "angle": "30-45 degree angle showing food height and texture",
    "depth_of_field": "shallow — dish sharp, background soft warm blur"
  },
  "colour_palette": {
    "background_blocks": "[MATCH FOOD TYPE: terracotta for meat, sage for healthy, mustard for breakfast, deep red for fakeaway, purple for guides]",
    "text": "white #FFFFFF",
    "accent": "brand purple #473f99 — thin border or decorative line"
  }
}
```

---

## Template C: Tips / Guide / Infographic

Use for: "Beginner's Guide", "Syn Calculator", "Speed Foods Explained"

```json
{
  "meta": { "task": "pinterest_pin_guide", "aspect_ratio": "2:3" },
  "design_system": {
    "style": "infographic-style pin with numbered tip cards or sections stacked vertically on a warm background. Clean graphic design, not photography-focused.",
    "structure": [
      "TOP (20%): solid brand purple #473f99 block with white bold headline",
      "MIDDLE (60%): warm cream #F5E6D3 background with 3-5 numbered tip cards arranged vertically. Each card has a small circular food photo or icon + short text.",
      "BOTTOM (20%): solid brand purple #473f99 block with CTA button and brand URL"
    ]
  },
  "tip_cards": {
    "count": "[3-5]",
    "style": "each card: rounded rectangle with subtle shadow, white background, small circular food photo on left, numbered text on right",
    "font": "clean sans-serif, numbered with brand purple numbers"
  }
}
```

---

## Quick Selection Guide

| Article Type | Template | Grid | Background |
|-------------|----------|------|------------|
| Recipe roundup (5+ recipes) | A: Collage | 2x3 (6 photos) | Terracotta or sage |
| Recipe roundup (3-4 recipes) | A: Collage | 2x2 (4 photos) | Terracotta or sage |
| Single recipe | B: Single Dish | 1 hero photo | Match food type |
| Fakeaway guide | B: Single Dish | 1 hero photo | Deep red #B84233 |
| Food list / guide | A: Collage or C: Guide | 2x3 or tip cards | Brand purple #473f99 |
| Meal plan | A: Collage | 2x2 (4 photos) | Mustard #D4A843 |
| Tips / beginner guide | C: Guide | Tip cards | Brand purple #473f99 |

---

## Snazzy vs Top Performer — Why We Changed

### Snazzy v2 (old):
```
Single cinematic hero food shot
Gradient overlay from purple to transparent
Bokeh, rim lighting, 3D floating text
Magazine cover aesthetic
```

### Top Performer v3 (new):
```
Photo COLLAGE grid showing multiple dishes
Solid colour text blocks (not gradients)
Large bold numbers + script subtitle
READ MORE button
Graphic design layout, not photography
```

**Why:** Real Pinterest analytics show collage/grid pins with bold text blocks and numbers consistently outperform single-hero cinematic shots. Users save pins that show VARIETY and have clear, scannable headlines with numbers.
