# Virtual Try-On

E-commerce product visualization on subjects.

---

## Clothing Try-On

```json
{
  "meta": {
    "intent": "virtual_try_on"
  },
  "task": "clothing_visualization",
  "subject": {
    "reference_image": "provided",
    "face_consistency": {
      "preservation_level": "strict",
      "instruction": "maintain exact facial features and body proportions"
    },
    "pose": {
      "action": "standing, slight hip tilt",
      "preserve": "original pose exactly"
    }
  },
  "product": {
    "category": "apparel",
    "item": "oversized cashmere sweater",
    "specifications": {
      "color": "cream",
      "fit": "relaxed, slightly off-shoulder on one side",
      "length": "hip-length"
    }
  },
  "rendering": {
    "material_accuracy": {
      "texture": "visible cable knit pattern",
      "drape": "soft, natural fabric fall",
      "weight": "medium weight, slight structure"
    },
    "integration": {
      "lighting_match": "consistent with subject's existing lighting",
      "shadow": "natural fabric shadows where garment meets body",
      "wrinkles": "realistic at elbows and waist"
    }
  },
  "constraints": {
    "exclusions": ["floating fabric", "unnatural folds", "lighting mismatch"]
  }
}
```

---

## Accessories Try-On

```json
{
  "meta": {
    "intent": "virtual_try_on"
  },
  "task": "accessory_visualization",
  "subject": {
    "reference_image": "provided",
    "face_consistency": {
      "preservation_level": "strict"
    }
  },
  "product": {
    "category": "eyewear",
    "item": "aviator sunglasses",
    "specifications": {
      "frame": "gold metal",
      "lens": "gradient brown",
      "size": "medium, proportional to face"
    }
  },
  "rendering": {
    "fit": {
      "bridge": "natural rest on nose",
      "temples": "behind ears, not floating"
    },
    "reflections": {
      "lens": "subtle environment reflection",
      "frame": "metallic highlights matching scene lighting"
    },
    "shadows": {
      "on_face": "subtle shadow from frame on cheeks"
    }
  }
}
```

---

## Product on Model (Studio Setting)

```json
{
  "meta": {
    "intent": "product_photography"
  },
  "task": "model_product_shoot",
  "subject": {
    "description": "professional model",
    "pose": {
      "action": "holding handbag",
      "gesture": "elbow bent, bag at hip level"
    }
  },
  "product": {
    "category": "handbag",
    "item": "structured leather tote",
    "specifications": {
      "color": "burgundy",
      "material": "pebbled leather",
      "hardware": "gold-tone buckles"
    },
    "hero_status": "product is the focus, model supports"
  },
  "cinematography": {
    "lighting": {
      "setup": "studio three-point",
      "product_lighting": {
        "highlight": "leather texture visible",
        "hardware": "gold reflections, not blown out"
      }
    },
    "composition": {
      "framing": "3/4 body, product centered",
      "background": "seamless gray"
    }
  },
  "rendering": {
    "product_priority": {
      "sharpness": "product sharper than model",
      "color_accuracy": "true to product color",
      "detail": "stitching, texture, hardware visible"
    }
  }
}
```

---

## Try-On Best Practices

### Preserve Subject Identity
```json
"face_consistency": {
  "preservation_level": "strict",
  "instruction": "face, skin tone, body shape unchanged",
  "allow_changes": ["clothing only"]
}
```

### Material Rendering Checklist
- Texture visible at expected distances
- Drape follows body contours naturally
- Shadows form where fabric meets body
- Wrinkles appear at joints (elbows, waist)
- Lighting on garment matches scene

### Common Mistakes to Avoid
| Issue | Solution |
|-------|----------|
| Floating fabric | Specify `"drape": "natural gravity"` |
| Wrong proportions | Include `"fit": "true to size"` |
| Lighting mismatch | Add `"lighting_match": "consistent with subject"` |
| Unnatural stiffness | Request `"wrinkles": "realistic at joints"` |
