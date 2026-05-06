# Crowd & Multi-Character Composition

Managing complex scenes with multiple subjects.

---

## Celebrity Rooftop Gathering

```json
{
  "meta": {
    "intent": "crowd_composition"
  },
  "subjects": [
    {
      "id": "group_foreground",
      "count": 4,
      "description": "elegantly dressed individuals",
      "position": "foreground, varied heights",
      "interaction": "animated conversation, natural gestures",
      "focus": "sharp"
    },
    {
      "id": "group_midground",
      "count": 6,
      "description": "cocktail party attendees",
      "position": "midground left and right",
      "interaction": "mingling, holding drinks",
      "focus": "slightly soft"
    },
    {
      "id": "group_background",
      "count": "10-15",
      "description": "distant guests",
      "position": "background",
      "focus": "bokeh blur"
    }
  ],
  "environment": {
    "location": "luxurious rooftop terrace",
    "time_context": {
      "time_of_day": "sunset golden hour"
    },
    "spatial_elements": [
      { "element": "polished marble floor", "state": "reflective" },
      { "element": "city skyline", "position": "background" },
      { "element": "string lights", "state": "beginning to glow" }
    ]
  },
  "cinematography": {
    "lens": "35mm f/1.4",
    "composition": {
      "framing": "wide establishing shot",
      "depth_of_field": "shallow, focus on foreground group"
    },
    "lighting": {
      "key_light": {
        "type": "golden hour sun",
        "direction": "from right",
        "effect": "warm rim light on subjects"
      },
      "fill_light": {
        "type": "ambient bounce from marble"
      }
    },
    "settings": {
      "resolution": "8K",
      "detail": "visible fabric textures, jewelry details"
    }
  }
}
```

---

## Natural Group Interaction

```json
{
  "meta": {
    "intent": "group_portrait"
  },
  "subjects": [
    {
      "id": "subject_1",
      "description": "woman in red cocktail dress",
      "position": "foreground left",
      "action": "laughing, hand gesture mid-story",
      "eye_line": "toward subject_2"
    },
    {
      "id": "subject_2",
      "description": "man in charcoal suit",
      "position": "foreground right",
      "action": "listening intently, slight lean forward",
      "eye_line": "toward subject_1"
    },
    {
      "id": "subject_3",
      "description": "woman in emerald dress",
      "position": "between subjects 1 and 2, slightly back",
      "action": "smiling at the conversation",
      "eye_line": "alternating between both"
    }
  ],
  "interaction": {
    "type": "natural conversation",
    "chemistry": "genuine connection, not posed",
    "body_language": "open, engaged, comfortable proximity"
  },
  "cinematography": {
    "lens": "85mm f/1.4",
    "composition": {
      "framing": "medium shot",
      "depth_of_field": "shallow"
    },
    "lighting": {
      "type": "golden rim light",
      "purpose": "separate each subject from background",
      "ratio": "each subject has distinct edge light"
    }
  }
}
```

---

## Crowd Management Tips

### Depth Layering
```json
"layers": {
  "foreground": { "count": "2-4", "focus": "sharp", "detail": "high" },
  "midground": { "count": "4-8", "focus": "slightly soft", "detail": "medium" },
  "background": { "count": "many", "focus": "bokeh", "detail": "silhouettes" }
}
```

### Preventing Chaos
- Assign specific positions to key subjects
- Use `"eye_line"` to create visual connections
- Apply graduated focus: sharp → soft → blur
- Use rim lighting to separate overlapping figures

### Resolution for Crowds
| Crowd Size | Recommended | Why |
|------------|-------------|-----|
| 3-5 people | 2K | Sufficient detail |
| 6-15 people | 4K | Need facial clarity |
| 15+ people | 8K | Preserve individual features |
