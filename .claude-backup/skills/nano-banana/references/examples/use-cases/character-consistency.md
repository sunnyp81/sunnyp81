# Character Consistency - Identity Preservation

Techniques for maintaining character identity across multiple generated images. Essential for brand mascots, virtual influencers, comic books, and product campaigns.

## The Challenge

Each generation is independent. Without explicit identity anchoring, the same "blonde woman" prompt produces different faces every time.

---

## Method 1: Master Character File

Create a JSON object that serves as the immutable source of truth.

### The Master Definition

```json
{
  "character_uuid": "sara_v1",
  "identity_anchor": {
    "face_shape": "diamond with soft angles",
    "face_proportions": {
      "forehead": "medium height",
      "eye_spacing": "slightly wide-set",
      "nose": "small, slightly upturned",
      "lips": "full, defined cupid's bow",
      "chin": "pointed but soft"
    },
    "distinctive_marks": [
      "small scar on left eyebrow",
      "beauty mark below right eye"
    ]
  },
  "consistent_features": {
    "eyes": {
      "shape": "almond",
      "color": "dark brown with amber flecks",
      "lashes": "naturally long"
    },
    "hair": {
      "texture": "wavy",
      "color": "jet black",
      "length": "shoulder length",
      "characteristic": "always has loose strand on left side"
    },
    "skin": {
      "tone": "warm olive",
      "texture": "visible pores on nose, light freckles on cheeks"
    }
  },
  "body_type": {
    "build": "athletic, lean",
    "height_impression": "average",
    "posture": "confident, shoulders back"
  }
}
```

### Scene Injection

Inject the master definition into each scene prompt:

```json
{
  "scene": {
    "action": "drinking coffee at cafe",
    "location": "Parisian terrace",
    "time": "morning"
  },
  "subject": {
    "character_reference": "sara_v1",
    "inject_definition": {
      "character_uuid": "sara_v1",
      "identity_anchor": { },
      "consistent_features": { }
    },
    "scene_specific": {
      "apparel": {
        "outfit": "casual summer dress",
        "color": "white with blue stripes"
      },
      "pose": "seated, holding cup with both hands",
      "expression": "warm smile, looking at camera"
    }
  }
}
```

---

## Method 2: Reference Image Anchoring

For strict consistency, pass a reference image with explicit instructions.

```json
{
  "subject": {
    "reference_image_id": "img_001",
    "reference_instruction": {
      "maintain_strictly": [
        "facial bone structure",
        "eye shape and color",
        "nose shape",
        "lip shape",
        "skin tone"
      ],
      "allow_variation": [
        "expression",
        "hair styling",
        "makeup"
      ],
      "change_explicitly": {
        "clothing": "red evening gown",
        "accessories": "diamond earrings",
        "hair": "styled in updo"
      }
    }
  },
  "scene": {
    "setting": "gala event",
    "lighting": "elegant ballroom"
  }
}
```

---

## Method 3: Seed State Pipeline

For production workflows, create a character "seed state" that includes visual anchors.

### Step 1: Generate Base Image

```json
{
  "task": "create_character_base",
  "subject": {
    "full_definition": { },
    "pose": "neutral, facing camera",
    "lighting": "flat studio lighting",
    "expression": "neutral"
  },
  "output": {
    "use_as": "identity_anchor",
    "save_as": "sara_base_v1"
  }
}
```

### Step 2: Reference in All Future Prompts

```json
{
  "subject": {
    "seed_reference": "sara_base_v1",
    "identity_instruction": "maintain exact facial features from seed",
    "modifications": {
      "expression": "laughing",
      "pose": "dynamic, mid-jump",
      "clothing": "athletic wear"
    }
  }
}
```

---

## Game Character Pipeline

For game development, create a character sheet first.

### Character Sheet Prompt

```json
{
  "project": "game_character_sheet",
  "character": {
    "name": "Kai",
    "role": "protagonist warrior",
    "definition": {
      "face": "angular, strong jaw, scar across right cheek",
      "hair": "short, spiky, silver-white",
      "eyes": "piercing blue, intense gaze",
      "build": "muscular, battle-worn"
    }
  },
  "sheet_layout": {
    "views": [
      { "angle": "front", "expression": "neutral" },
      { "angle": "three-quarter left", "expression": "determined" },
      { "angle": "three-quarter right", "expression": "battle rage" },
      { "angle": "profile left", "expression": "neutral" }
    ],
    "additional": [
      { "type": "expression_sheet", "emotions": ["happy", "angry", "sad", "surprised"] },
      { "type": "pose_reference", "poses": ["idle", "combat_ready", "victory"] }
    ]
  },
  "style": {
    "aesthetic": "AAA game character art",
    "rendering": "semi-realistic"
  }
}
```

### Using the Character Sheet

```json
{
  "subject": {
    "character_sheet_reference": "kai_sheet_v1",
    "use_view": "three-quarter left",
    "expression": "determined",
    "outfit_variant": "heavy armor set"
  },
  "scene": {
    "setting": "dark castle throne room",
    "action": "confronting enemy"
  }
}
```

---

## Virtual Influencer Pipeline

For social media content with consistent virtual personas.

### Brand Persona Definition

```json
{
  "persona": {
    "name": "Mika",
    "brand_identity": "tech-savvy lifestyle influencer",
    "age_presentation": "early 20s",
    "identity": {
      "face": {
        "type": "unique but aspirational",
        "features": "high cheekbones, almond eyes, small nose",
        "skin": "flawless but not plastic, subtle freckles"
      },
      "hair": {
        "signature": "pastel pink with darker roots",
        "length": "long, usually styled differently"
      },
      "style": {
        "aesthetic": "minimalist streetwear meets high fashion",
        "colors": "monochrome with one pop color"
      }
    }
  }
}
```

### Content Variations

```json
{
  "content_type": "instagram_post",
  "persona_reference": "mika_v1",
  "scene": {
    "setting": "minimalist apartment",
    "action": "unboxing tech product"
  },
  "identity_preservation": {
    "face": "exact match to reference",
    "hair": "current color, messy bun style",
    "body": "maintain proportions"
  },
  "variation": {
    "outfit": "oversized white hoodie, black leggings",
    "expression": "excited, looking at product"
  }
}
```

---

## Consistency Checklist

Before generating, verify your prompt includes:

| Element | Specified? | Consistency Level |
|---------|-----------|-------------------|
| Face shape | Yes/No | Critical |
| Eye color/shape | Yes/No | Critical |
| Skin tone | Yes/No | Critical |
| Distinctive marks | Yes/No | High |
| Hair color | Yes/No | High |
| Hair texture | Yes/No | Medium |
| Body type | Yes/No | Medium |
| Posture | Yes/No | Low |

---

## Common Failures & Fixes

| Problem | Cause | Fix |
|---------|-------|-----|
| Face changes between images | No identity anchor | Add detailed `face_proportions` block |
| Skin tone varies | Generic description | Specify exact tone with reference |
| Hair color shifts | Missing color details | Include base color AND highlights |
| Body proportions change | No body definition | Add `body_type` specifications |
| Distinctive marks disappear | Marks not prominent in prompt | Elevate marks to top-level subject |

---

## Multi-Character Scenes

When multiple consistent characters appear together:

```json
{
  "subjects": [
    {
      "id": "character_a",
      "reference": "sara_v1",
      "position": "foreground left",
      "action": "talking"
    },
    {
      "id": "character_b",
      "reference": "mika_v1",
      "position": "foreground right",
      "action": "listening, nodding"
    }
  ],
  "interaction": {
    "type": "conversation",
    "eye_contact": "character_a looking at character_b",
    "spatial_relation": "facing each other, arm's length apart"
  }
}
```
