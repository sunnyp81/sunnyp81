# Root Object Schema Reference

Complete reference for the Nano Banana JSON prompt structure.

## The Canon Schema

```json
{
  "meta": {
    "version": "1.0",
    "intent": "string"
  },
  "subject": { },
  "environment": { },
  "cinematography": { },
  "style": { },
  "constraints": { }
}
```

---

## Meta Domain

Project metadata and intent declaration.

```json
"meta": {
  "version": "1.0",
  "intent": "photorealistic_commercial | infographic | artistic | technical_diagram",
  "project_id": "optional_tracking_id"
}
```

| Field | Type | Purpose |
|-------|------|---------|
| `version` | string | Schema version for compatibility |
| `intent` | string | Signals rendering mode to the model |
| `project_id` | string | Optional tracking identifier |

---

## Subject Domain

The primary focus of the image. Deep nesting isolates attributes.

### Human Subject (Anatomy Pattern)

```json
"subject": {
  "identity": "character_id",
  "physicality": {
    "demographics": "age, ethnicity description",
    "face": {
      "structure": "bone structure description",
      "skin_texture": "pores, imperfections, subsurface scattering",
      "eyes": "color, shape, focus",
      "expression": "micro-expression details"
    },
    "hair": {
      "style": "cut and arrangement",
      "color": "base and highlights",
      "physics": "movement, reaction to wind/gravity"
    },
    "body": {
      "build": "athletic, slim, muscular, etc.",
      "posture": "stance description"
    }
  },
  "apparel": {
    "upper_body": {
      "garment": "clothing type",
      "text_content": "any text on clothing",
      "fit": "loose, tight, oversized",
      "material_properties": "gloss, matte, texture"
    },
    "lower_body": {
      "garment": "clothing type",
      "material_properties": "visual properties"
    },
    "accessories": [
      { "item": "sunglasses", "style": "aviator", "position": "on face" }
    ]
  },
  "pose": {
    "action": "what subject is doing",
    "gesture": "hand/arm position",
    "micro_expression": "facial nuance",
    "eye_contact": "camera, off-frame, downward"
  }
}
```

### Object Subject

```json
"subject": {
  "type": "product | vehicle | architecture | abstract",
  "name": "specific object name",
  "orientation": "front, three-quarter, isometric",
  "rendering": "photorealistic | wireframe | cutaway",
  "material": {
    "primary": "metal, glass, wood, plastic",
    "finish": "matte, glossy, brushed, weathered"
  },
  "state": "new, worn, damaged, in-use"
}
```

### Multiple Subjects

```json
"subjects": [
  { "id": "subject_1", "type": "person", "position": "foreground left" },
  { "id": "subject_2", "type": "person", "position": "foreground right" },
  { "id": "subject_3", "type": "object", "position": "background center" }
]
```

---

## Environment Domain

The setting and atmospheric context.

```json
"environment": {
  "location": "specific place or type",
  "time_context": {
    "time_of_day": "dawn | morning | noon | afternoon | dusk | night | midnight",
    "season": "spring | summer | fall | winter",
    "weather": "clear | cloudy | rain | snow | fog | storm"
  },
  "spatial_elements": [
    {
      "element": "element name",
      "color": "color description",
      "state": "glowing | wet | dusty | etc.",
      "position": "foreground | midground | background",
      "focus": "sharp | blurred"
    }
  ],
  "atmosphere": "mood keywords",
  "scale": "intimate | human | grand | epic"
}
```

### Spatial Elements Array

Use arrays for distinct enumeration of background components:

```json
"spatial_elements": [
  { "element": "neon sign", "color": "cyan", "state": "flickering" },
  { "element": "wet pavement", "reflection_quality": "mirror-like" },
  { "element": "crowd", "density": "sparse", "focus": "motion blur" },
  { "element": "steam vents", "opacity": "semi-transparent" }
]
```

---

## Cinematography Domain

Virtual camera and lighting setup.

```json
"cinematography": {
  "camera_body": "camera model name",
  "lens": "lens specification",
  "settings": {
    "aperture": "f/1.4 to f/22",
    "shutter_speed": "1/1000 to 30s",
    "iso": "100 to 12800"
  },
  "composition": {
    "framing": "extreme close-up | close-up | medium close-up | medium | medium full | full | wide | extreme wide",
    "angle": "eye level | low angle | high angle | bird's eye | worm's eye | dutch angle",
    "depth_of_field": "shallow | medium | deep",
    "focus_point": "subject eyes | hands | product"
  },
  "lighting": {
    "setup": "studio | natural | mixed | dramatic",
    "key_light": {
      "type": "soft | hard | diffused",
      "direction": "from left | from right | frontal | backlit",
      "color_temperature": "2700K warm to 6500K cool"
    },
    "fill_light": {
      "intensity": "percentage of key",
      "direction": "opposite key"
    },
    "rim_light": {
      "purpose": "edge separation",
      "intensity": "subtle | strong"
    },
    "practical_lights": ["neon signs", "candles", "screens"]
  },
  "post_processing": {
    "color_grade": "LUT or color description",
    "grain": "none | subtle | heavy | 35mm film",
    "contrast": "flat | normal | high",
    "vignette": "none | subtle | heavy"
  }
}
```

---

## Style Domain

Aesthetic direction and artistic references.

```json
"style": {
  "aesthetic": "photorealistic | cinematic | editorial | artistic | technical",
  "genre": "portrait | landscape | product | fashion | documentary",
  "mood": "moody | bright | nostalgic | futuristic | romantic",
  "references": {
    "photographer": "Annie Leibovitz style",
    "film": "Blade Runner 2049 aesthetic",
    "era": "1980s film photography"
  },
  "color_palette": {
    "dominant": "primary color",
    "accent": "complementary color",
    "shadows": "cool or warm"
  }
}
```

---

## Constraints Domain

Exclusions and safety filters.

```json
"constraints": {
  "exclusions": [
    "blur",
    "low_resolution",
    "distorted_hands",
    "extra_limbs",
    "text_overlay",
    "watermark",
    "airbrushed",
    "cartoon",
    "illustration"
  ],
  "safety_filter": "block_nsfw",
  "aspect_ratio": "1:1 | 4:3 | 16:9 | 9:16 | 3:2",
  "output_format": "png | jpg | webp"
}
```

---

## Complete Example

```json
{
  "meta": {
    "version": "1.0",
    "intent": "photorealistic_commercial"
  },
  "subject": {
    "physicality": {
      "demographics": "woman, mid-20s",
      "face": {
        "skin_texture": "visible pores, natural",
        "eyes": "green, sharp focus"
      }
    },
    "apparel": {
      "upper_body": {
        "garment": "white silk blouse",
        "material_properties": "slight sheen, soft drape"
      }
    },
    "pose": {
      "action": "sitting at cafe table",
      "gesture": "holding coffee cup",
      "expression": "contemplative smile"
    }
  },
  "environment": {
    "location": "Parisian cafe terrace",
    "time_context": {
      "time_of_day": "golden hour",
      "weather": "clear"
    },
    "spatial_elements": [
      { "element": "bistro chairs", "material": "wrought iron" },
      { "element": "cobblestone street", "state": "slightly wet" }
    ]
  },
  "cinematography": {
    "camera_body": "Sony A7R IV",
    "lens": "85mm f/1.4",
    "composition": {
      "framing": "medium close-up",
      "depth_of_field": "shallow"
    },
    "lighting": {
      "setup": "natural golden hour",
      "key_light": "sun from camera right"
    },
    "post_processing": {
      "color_grade": "warm, lifted shadows",
      "grain": "subtle film grain"
    }
  },
  "constraints": {
    "exclusions": ["airbrushed", "plastic skin", "watermark"]
  }
}
```
