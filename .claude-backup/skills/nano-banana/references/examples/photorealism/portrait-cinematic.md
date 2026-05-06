# Cinematic Portrait - Camera & Lighting Mastery

This example demonstrates how to leverage Nano Banana Pro's understanding of real-world photography equipment to achieve cinematic photorealism.

## Complete JSON Prompt

```json
{
  "meta": {
    "version": "1.0",
    "intent": "cinematic_portrait"
  },
  "subject": {
    "identity": "female_influencer_v1",
    "physicality": {
      "demographics": "age 24, mixed ethnicity (Japanese/Scandinavian)",
      "face": {
        "structure": "high cheekbones, soft jawline",
        "skin_texture": "hyper-detailed, visible pores, slight freckles on nose bridge",
        "eyes": "heterochromia (left blue, right hazel), sharp focus"
      },
      "hair": {
        "style": "messy bun with loose strands",
        "color": "platinum blonde with pink tips",
        "physics": "reacting to wind from left"
      }
    },
    "apparel": {
      "upper_body": {
        "garment": "oversized vintage band t-shirt",
        "text_content": "METALLICA",
        "fit": "loose, draping over shoulder"
      },
      "lower_body": {
        "garment": "black leather leggings",
        "material_properties": "high gloss, reflective, tight fit"
      }
    },
    "pose": {
      "action": "walking towards camera",
      "gesture": "adjusting sunglasses with right hand",
      "micro_expression": "subtle smirk, looking directly at lens"
    }
  },
  "environment": {
    "location": "Tokyo Shibuya Crossing",
    "time_context": {
      "time_of_day": "midnight",
      "weather": "heavy rain"
    },
    "spatial_elements": [
      { "element": "neon signage", "color": "cyan and magenta", "state": "glowing" },
      { "element": "wet asphalt", "reflection_quality": "mirror-like" },
      { "element": "crowd", "density": "sparse", "focus": "blurred" }
    ],
    "atmosphere": "cyberpunk, dystopian, moody fog"
  },
  "cinematography": {
    "camera_body": "Arri Alexa Mini LF",
    "lens": "Panavision T-Series Anamorphic 50mm",
    "settings": {
      "aperture": "f/2.8",
      "shutter_angle": "180 degrees",
      "iso": 800
    },
    "composition": {
      "framing": "medium shot",
      "angle": "low angle, looking up at subject",
      "depth_of_field": "shallow, bokeh on background lights"
    },
    "lighting": {
      "setup": "cinematic street lighting",
      "key_light": "cool blue neon from left",
      "fill_light": "warm amber street lamp from right",
      "rim_light": "bright white backlight for separation"
    },
    "post_processing": {
      "color_grade": "teal and orange LUT",
      "grain": "35mm film grain",
      "vignette": "subtle"
    }
  },
  "constraints": {
    "exclusions": [
      "blur on subject face",
      "distorted hands",
      "airbrushed skin",
      "cartoon style",
      "watermark"
    ]
  }
}
```

## Camera Body Reference

Different camera bodies produce distinct "looks":

| Camera | Characteristics | Best For |
|--------|-----------------|----------|
| Arri Alexa Mini LF | High dynamic range, soft highlight roll-off | Cinematic portraits, film look |
| Sony A7R IV | Sharp detail, accurate colors | Commercial photography |
| Canon EOS R5 | Warm skin tones, pleasing bokeh | Fashion, beauty |
| RED Komodo | High contrast, digital cinema | Action, dynamic scenes |
| Hasselblad X2D | Medium format, extreme detail | Editorial, luxury |
| GoPro Hero | High contrast, wide-angle distortion | Action, POV shots |

## Lens Reference

### Prime Lenses
- **35mm** - Environmental portraits, context
- **50mm** - Classic portrait, natural perspective
- **85mm** - Tight portraits, maximum subject isolation
- **135mm** - Compressed background, fashion

### Anamorphic Lenses
Trigger specific visual characteristics:
- Oval bokeh (not circular)
- Horizontal lens flares
- Subtle barrel distortion
- Cinematic aspect ratio feel

```json
"lens": "Panavision T-Series Anamorphic 50mm"
```

### Vintage Lenses
For character and imperfection:
```json
"lens": "Helios 44-2 58mm (vintage Soviet)",
"lens_characteristics": "swirly bokeh, soft glow, slight vignette"
```

## Three-Point Lighting Setup

```json
"lighting": {
  "key_light": {
    "type": "soft diffused",
    "direction": "45 degrees from left",
    "color_temperature": "5600K (daylight)"
  },
  "fill_light": {
    "type": "bounce reflector",
    "direction": "opposite key light",
    "intensity": "50% of key"
  },
  "rim_light": {
    "type": "hard backlight",
    "direction": "behind subject",
    "purpose": "edge separation from background"
  }
}
```

## Skin Texture Deep Dive

The difference between "AI plastic" and photorealism:

### Bad (Default AI Look)
```json
"skin": "beautiful, flawless"
```

### Good (Photorealistic)
```json
"skin_texture": {
  "pores": "visible, especially on nose and cheeks",
  "imperfections": "slight freckles, minor blemishes",
  "subsurface_scattering": "warm glow in backlit areas",
  "micro_details": "fine peach fuzz, natural skin oils"
}
```

## Color Grading Presets

Common cinematic looks:

```json
// Teal and Orange (Blockbuster)
"color_grade": "teal shadows, orange midtones, crushed blacks"

// Desaturated (Gritty Drama)
"color_grade": "desaturated except skin tones, high contrast, lifted blacks"

// Golden Hour
"color_grade": "warm highlights, soft shadows, amber tint"

// Noir
"color_grade": "high contrast black and white, deep shadows, bright highlights"
```
