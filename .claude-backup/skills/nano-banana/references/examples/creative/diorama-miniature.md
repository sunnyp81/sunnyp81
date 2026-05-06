# 3D Diorama & Miniature Style

Tilt-shift miniature world compositions.

---

## Country as Floating Island

```json
{
  "meta": {
    "intent": "creative_diorama"
  },
  "style": {
    "type": "3D diorama",
    "effect": "floating island miniature"
  },
  "subject": {
    "concept": "Japan as floating island",
    "elements": [
      { "landmark": "Mount Fuji", "position": "center, prominent" },
      { "landmark": "Tokyo Tower", "position": "coastal area" },
      { "landmark": "cherry blossom trees", "scattered": true },
      { "terrain": "mountains", "position": "spine of island" },
      { "terrain": "rice paddies", "position": "lowlands" },
      { "detail": "tiny trains", "on": "rail lines" },
      { "detail": "miniature people", "scale": "barely visible" }
    ]
  },
  "environment": {
    "background": "soft gradient sky, clouds below island",
    "base": "island floating on clouds",
    "atmosphere": "dreamy, fantastical"
  },
  "cinematography": {
    "lens": "tilt-shift",
    "angle": "isometric, 45 degrees above",
    "depth_of_field": {
      "type": "extreme shallow",
      "effect": "toy-like blur on edges",
      "focus_band": "center of island"
    }
  },
  "lighting": {
    "type": "soft, even studio lighting",
    "purpose": "enhance miniature illusion",
    "shadows": "gentle, not harsh"
  },
  "rendering": {
    "scale": "clearly miniature, diorama feel",
    "materials": "slightly plastic/model quality",
    "detail": "intricate but toy-like"
  }
}
```

---

## City Block Diorama

```json
{
  "meta": {
    "intent": "urban_diorama"
  },
  "style": {
    "type": "architectural diorama",
    "effect": "tilt-shift miniature"
  },
  "subject": {
    "concept": "New York city block",
    "cutaway": "buildings sectioned to show interiors",
    "elements": [
      { "building": "brownstone", "interior_visible": "living rooms" },
      { "building": "high-rise", "interior_visible": "offices" },
      { "street_level": "tiny cars, yellow taxis" },
      { "street_level": "miniature pedestrians" },
      { "detail": "fire hydrants, street signs" }
    ]
  },
  "cinematography": {
    "angle": "3/4 view from above",
    "depth_of_field": "selective focus on center buildings",
    "composition": "block fills frame edge to edge"
  },
  "lighting": {
    "interior": "warm glows from windows",
    "exterior": "afternoon sun from upper left",
    "contrast": "cozy interiors vs bright street"
  }
}
```

---

## Product Miniature World

```json
{
  "meta": {
    "intent": "product_diorama"
  },
  "style": {
    "type": "product in miniature world"
  },
  "subject": {
    "product": {
      "item": "coffee mug",
      "scale": "giant compared to world",
      "position": "center"
    },
    "miniature_world": {
      "theme": "tiny coffee farm",
      "elements": [
        { "feature": "coffee plants", "scale": "tiny, around mug" },
        { "feature": "miniature farmers", "action": "harvesting" },
        { "feature": "tiny truck", "loaded": "coffee beans" },
        { "feature": "processing building", "scale": "matchbox size" }
      ]
    }
  },
  "cinematography": {
    "lens": "macro with tilt-shift effect",
    "focus": "product sharp, world has selective blur",
    "angle": "eye level with miniature world"
  },
  "lighting": {
    "product": "hero lighting, well-lit",
    "world": "natural daylight feel"
  }
}
```

---

## Diorama Techniques

### Scale Indicators
Include these to sell the miniature illusion:
- Tiny people (barely visible)
- Miniature vehicles
- Exaggerated texture on buildings
- Slightly imperfect, handmade quality

### Tilt-Shift Settings
```json
"depth_of_field": {
  "type": "tilt-shift",
  "focus_plane": "horizontal band across center",
  "blur_above": "gradual increase",
  "blur_below": "gradual increase",
  "bokeh": "soft, circular"
}
```

### Lighting for Miniatures
| Effect | Lighting Type | Purpose |
|--------|---------------|---------|
| Toy-like | Soft, even, diffused | Reduce harsh shadows |
| Architectural | Directional with fill | Show depth and form |
| Magical | Rim light + soft fill | Ethereal, floating feel |

### Common Diorama Subjects
- Countries/cities as floating islands
- Historical scenes as museum dioramas
- Products in miniature worlds
- Seasonal scenes (snow globes, terrariums)
- Cross-section/cutaway buildings
