# Mirror Selfie - Physics Override Pattern

The mirror selfie is considered the "Turing Test" of AI image generation. It requires solving complex optical problems:

- Subject faces the mirror
- Camera (phone) faces the mirror
- Image we see is the reflection
- Text on clothing should be reversed, but users often want it legible

## The Challenge

Standard diffusion models struggle because mirror physics dictate text should be reversed. But users typically want legible text (breaking physics).

## Solved JSON Prompt

```json
{
  "prompt_id": "mirror_selfie_v4",
  "subject": {
    "description": "Influencer taking a mirror selfie",
    "pose": "standing, hip cocked, holding phone with right hand",
    "gaze": "looking at phone screen in reflection"
  },
  "mirror_physics_override": {
    "instruction": "IGNORE mirror physics for text",
    "text_orientation": "legible to viewer (non-reversed)",
    "phone_screen": "blank or camera UI"
  },
  "apparel": {
    "top": {
      "color": "white",
      "text": "VOGUE",
      "text_style": "bold black serif"
    }
  },
  "environment": {
    "setting": "minimalist bedroom",
    "mirror_type": "full-length floor mirror with gold frame",
    "reflection_details": {
      "smudges": "fingerprints on glass surface",
      "dust": "micro-dust particles on mirror surface"
    }
  },
  "photography": {
    "camera_simulation": "smartphone rear camera",
    "flash": "on, creating starburst flare on glass"
  }
}
```

## Key Techniques

### 1. The Physics Override Block

```json
"mirror_physics_override": {
  "instruction": "IGNORE mirror physics for text",
  "text_orientation": "legible to viewer (non-reversed)"
}
```

This is a direct instruction to Nano Banana Pro's reasoning engine. The model can logically isolate the text layer and either:
- Generate it non-reversed from the start
- Flip it post-process

### 2. Surface Imperfections

```json
"reflection_details": {
  "smudges": "fingerprints on glass surface",
  "dust": "micro-dust particles on mirror surface"
}
```

Adding imperfections places a texture layer on top of the reflected image. This creates depth by separating the "glass plane" from the "reflected room."

### 3. Flash Effects

```json
"flash": "on, creating starburst flare on glass"
```

The flash starburst is a signature element of authentic mirror selfies. It reinforces the "glass surface" and adds realism.

## Variations

### Bathroom Mirror Selfie

```json
{
  "environment": {
    "setting": "modern bathroom",
    "mirror_type": "rectangular vanity mirror with LED frame",
    "reflection_details": {
      "steam": "light condensation at edges",
      "water_spots": "dried water droplets"
    }
  },
  "lighting": {
    "primary": "LED ring light from mirror frame",
    "ambient": "soft overhead bathroom lighting"
  }
}
```

### Gym Mirror Selfie

```json
{
  "environment": {
    "setting": "commercial gym",
    "mirror_type": "wall-to-wall gym mirror",
    "background_elements": [
      { "element": "weight rack", "focus": "blurred" },
      { "element": "other gym-goers", "density": "sparse", "focus": "heavily blurred" }
    ]
  },
  "subject": {
    "pose": "flexing bicep with one arm",
    "apparel": {
      "top": "fitted tank top",
      "material_properties": "slightly sweaty, clinging to body"
    }
  }
}
```

## Common Failures & Fixes

| Problem | Cause | Fix |
|---------|-------|-----|
| Text reversed despite override | Override buried too deep | Move `mirror_physics_override` to root level |
| No glass surface visible | Missing surface details | Add smudges, dust, or reflections |
| Unrealistic phone position | Generic pose description | Specify exact hand and arm position |
| Wrong reflection angle | Inconsistent spatial logic | Explicitly state what should be visible in reflection |
