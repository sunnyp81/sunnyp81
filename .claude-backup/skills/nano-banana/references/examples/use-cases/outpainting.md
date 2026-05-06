# Outpainting & Context Extension

Extending image boundaries while maintaining visual continuity.

---

## Horizontal Extension

```json
{
  "meta": {
    "intent": "outpainting"
  },
  "task": "extend_boundaries",
  "reference_image": {
    "provided": true,
    "position": "center of new canvas"
  },
  "extension": {
    "direction": "left and right",
    "amount": {
      "left": "50% of original width",
      "right": "50% of original width"
    },
    "final_aspect_ratio": "16:9"
  },
  "continuity": {
    "lighting": {
      "match": "existing shadows and highlights exactly",
      "direction": "maintain consistent light source"
    },
    "style": {
      "match": "color grading, contrast, saturation",
      "seamless": true
    },
    "elements": {
      "extend": "background naturally",
      "logic": "architecturally coherent if buildings",
      "avoid": "introducing new focal subjects"
    }
  },
  "constraints": {
    "preserve": "all original content pixel-perfect",
    "blend": "invisible seam at boundaries",
    "exclusions": ["new people", "new text", "style changes"]
  }
}
```

---

## Vertical Extension (Portrait to Landscape)

```json
{
  "meta": {
    "intent": "outpainting"
  },
  "task": "aspect_ratio_conversion",
  "reference_image": {
    "provided": true,
    "original_ratio": "9:16 portrait"
  },
  "extension": {
    "direction": "top and bottom",
    "target_ratio": "16:9 landscape",
    "content_priority": "subject remains centered"
  },
  "generation": {
    "above": {
      "content": "extend sky or ceiling naturally",
      "match": "existing color gradient and clouds"
    },
    "below": {
      "content": "extend ground or floor",
      "match": "existing texture and perspective"
    }
  },
  "continuity": {
    "perspective": "maintain existing vanishing points",
    "depth": "consistent with original scene depth"
  }
}
```

---

## Background Replacement with Extension

```json
{
  "meta": {
    "intent": "background_extension"
  },
  "task": "replace_and_extend",
  "subject": {
    "reference_image": "provided",
    "preserve": "subject only, mask background"
  },
  "new_background": {
    "type": "beach sunset",
    "elements": [
      { "element": "ocean", "position": "horizon" },
      { "element": "sand", "position": "foreground, beneath subject" },
      { "element": "sunset sky", "position": "upper half" }
    ]
  },
  "integration": {
    "lighting": {
      "relight_subject": "warm sunset tones from right",
      "rim_light": "golden edge on subject"
    },
    "shadows": {
      "subject_shadow": "long, toward left, on sand"
    },
    "color_harmony": {
      "subject_color_grade": "warm to match environment"
    }
  },
  "canvas": {
    "extend": "full 16:9 around subject",
    "subject_position": "rule of thirds, left side"
  }
}
```

---

## Crowd Removal with Fill

```json
{
  "meta": {
    "intent": "outpainting"
  },
  "task": "remove_and_fill",
  "reference_image": "provided",
  "removal": {
    "target": "crowd of people in background",
    "method": "intelligent fill"
  },
  "fill": {
    "content": "extend existing architecture and environment",
    "match": {
      "style": "identical to surrounding areas",
      "lighting": "consistent shadows and highlights",
      "texture": "seamless material continuation"
    }
  },
  "preserve": {
    "foreground_subject": "completely unchanged",
    "key_landmarks": "maintain architectural features"
  }
}
```

---

## Outpainting Guidelines

### Continuity Checklist
- [ ] Light direction consistent across seam
- [ ] Shadow angles match throughout
- [ ] Color temperature uniform
- [ ] Perspective lines continue correctly
- [ ] Texture resolution matches original

### Extension Content Rules
| Original Content | Safe to Extend | Avoid Generating |
|------------------|----------------|------------------|
| Sky | Clouds, gradients | New objects, text |
| Architecture | Building continuation | New structures |
| Nature | Trees, grass, water | Animals, people |
| Interior | Walls, floors | Furniture, art |

### Seam Quality
```json
"blend": {
  "method": "feathered edge",
  "width": "gradual transition",
  "verification": "invisible at normal viewing"
}
```
