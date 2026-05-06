# Advanced Techniques

Logic gates, physics overrides, character consistency, and other advanced patterns for Nano Banana Pro.

---

## Table of Contents

- [Logic Gates](#logic-gates)
- [Counting Enforcement](#counting-enforcement)
- [Text Accuracy](#text-accuracy)
- [Spatial Relations](#spatial-relations)
- [Geometric Shapes](#geometric-shapes)
- [Math and Equations](#math-and-equations)
- [Infographic Labels](#infographic-labels)
- [Physics Overrides](#physics-overrides)
- [Negative Prompting](#negative-prompting)
- [Character Consistency](#character-consistency)

---

## Logic Gates

Logic Gates are meta-instructions that signal to Nano Banana Pro's reasoning engine to prioritize accuracy over creativity. Essential for infographics, diagrams, counting tasks, and text rendering.

### The Logic Gate Wrapper

```json
{
  "system_instruction": "ACTIVATE_LOGIC_CORE",
  "mode": "strict_adherence",
  "task": "task_type",
  "logic_constraints": {
    "count_enforcement": "strict",
    "text_accuracy": "100%",
    "spatial_relation": "absolute"
  },
  "content": { }
}
```

### When to Use Logic Gates

| Task Type | Use Logic Gate? | Reason |
|-----------|----------------|--------|
| Artistic portrait | No | Creativity > accuracy |
| Infographic with labels | Yes | Text must be correct |
| Counting objects | Yes | Numbers must be exact |
| Floor plan | Yes | Dimensions matter |
| Math visualization | Yes | Equations must be correct |
| UI mockup | Yes | Layout must be precise |
| Atmospheric scene | No | Mood > precision |

---

## Counting Enforcement

For tasks where exact quantities matter.

### The Problem

Ask for 5 apples, get 4 or 7. Diffusion models struggle with counting.

### The Solution: Triangulation

State the constraint multiple ways:

```json
{
  "system_instruction": "ACTIVATE_LOGIC_CORE",
  "logic_constraints": {
    "count_enforcement": "strict"
  },
  "content": {
    "objects": {
      "type": "apple",
      "count": 5,
      "count_verification": "exactly five apples",
      "arrangement": "5 apples in a row"
    }
  }
}
```

### Advanced: Enumerated Objects

For guaranteed accuracy, enumerate each item:

```json
"objects": [
  { "id": "apple_1", "position": "far left" },
  { "id": "apple_2", "position": "left of center" },
  { "id": "apple_3", "position": "center" },
  { "id": "apple_4", "position": "right of center" },
  { "id": "apple_5", "position": "far right" }
]
```

---

## Text Accuracy

For tasks where text must render correctly.

### The Problem

"COFFEE" becomes "COFEE" or "COFFE". Text drifts or floats.

### The Solution: Typography Block

```json
{
  "system_instruction": "ACTIVATE_LOGIC_CORE",
  "logic_constraints": {
    "text_accuracy": "100%"
  },
  "typography": {
    "primary_text": {
      "content": "'COFFEE'",
      "strict_spelling": true,
      "character_verification": "C-O-F-F-E-E",
      "placement": "centered on mug",
      "font_style": "bold sans-serif",
      "color": "white on dark background"
    }
  }
}
```

### Multi-Text Elements

```json
"typography": {
  "texts": [
    {
      "id": "headline",
      "content": "'SALE'",
      "position": "top center",
      "size": "large"
    },
    {
      "id": "subhead",
      "content": "'50% OFF'",
      "position": "below headline",
      "size": "medium"
    },
    {
      "id": "fine_print",
      "content": "'Terms apply'",
      "position": "bottom",
      "size": "small"
    }
  ]
}
```

---

## Spatial Relations

For tasks requiring precise positioning and layout.

### Absolute Positioning

```json
{
  "system_instruction": "ACTIVATE_LOGIC_CORE",
  "logic_constraints": {
    "spatial_relation": "absolute"
  },
  "layout": {
    "grid": "3x3",
    "elements": [
      { "content": "Logo", "cell": "top-left" },
      { "content": "Title", "cell": "top-center" },
      { "content": "Date", "cell": "top-right" },
      { "content": "Main Image", "cell": "center", "span": "full-width" },
      { "content": "Footer", "cell": "bottom-center" }
    ]
  }
}
```

### Relative Positioning

```json
"spatial_relations": [
  { "subject": "A", "relation": "left of", "object": "B" },
  { "subject": "B", "relation": "in front of", "object": "C" },
  { "subject": "C", "relation": "above", "object": "D" }
]
```

---

## Geometric Shapes

For tasks involving specific shapes.

### The Problem

Pentagon becomes hexagon. Circle becomes oval.

### The Solution: Shape Triangulation

```json
{
  "system_instruction": "ACTIVATE_LOGIC_CORE",
  "logic_constraints": {
    "geometric_accuracy": "strict"
  },
  "shape": {
    "type": "pentagon",
    "sides_count": 5,
    "visual_description": "five-sided polygon",
    "regularity": "regular (equal sides and angles)",
    "verification": "count vertices: 5"
  }
}
```

---

## Math and Equations

For rendering mathematical content.

```json
{
  "system_instruction": "ACTIVATE_LOGIC_CORE",
  "task": "math_visualization",
  "logic_constraints": {
    "symbolic_accuracy": "100%",
    "step_verification": true
  },
  "content": {
    "problem": "integral of 4x*cos(2-3x)dx",
    "display": "whiteboard style",
    "requirements": [
      "correct mathematical notation",
      "clear intermediate steps",
      "legible handwriting style",
      "proper spacing and alignment"
    ],
    "solution_steps": "show integration by parts"
  }
}
```

---

## Infographic Labels

Ensuring labels match their targets.

```json
{
  "system_instruction": "ACTIVATE_LOGIC_CORE",
  "task": "generate_schematic",
  "logic_constraints": {
    "label_accuracy": "100%",
    "target_matching": "strict"
  },
  "labels": [
    {
      "text": "CPU",
      "target": "central processor chip",
      "target_verification": "largest chip on motherboard",
      "connector": "arrow pointing to exact location"
    },
    {
      "text": "RAM Slots",
      "target": "memory module slots",
      "target_verification": "elongated slots near CPU",
      "count": 4
    }
  ]
}
```

---

## Physics Overrides

When you need to break physical rules (e.g., legible text in mirrors).

### Basic Override

```json
{
  "system_instruction": "ACTIVATE_LOGIC_CORE",
  "physics_override": {
    "rule": "mirror reflection reverses text",
    "instruction": "IGNORE for text elements",
    "behavior": "render text legible to viewer"
  }
}
```

### Mirror Selfie Pattern

```json
"mirror_physics_override": {
  "instruction": "IGNORE mirror physics for text",
  "text_orientation": "legible to viewer (non-reversed)",
  "phone_screen": "blank or camera UI"
}
```

### Common Physics Overrides

| Rule to Override | Instruction |
|-----------------|-------------|
| Mirror text reversal | Render text legible |
| Shadow direction | Force consistent shadows |
| Reflection accuracy | Simplify complex reflections |
| Gravity | Objects can float |
| Scale consistency | Allow impossible scales |

---

## Negative Prompting

More effective than separate negative prompt fields - include exclusions in the JSON:

```json
"constraints": {
  "exclusions": [
    "blur",
    "low_resolution",
    "distorted_hands",
    "extra_limbs",
    "text_overlay",
    "watermark"
  ],
  "safety_filter": "block_nsfw"
}
```

---

## Character Consistency

Create a master character definition for reuse across multiple images.

### Method 1: Master Character File

```json
{
  "character_uuid": "sara_v1",
  "consistent_features": {
    "face_shape": "diamond",
    "eyes": "almond, dark brown",
    "hair": "shoulder length, wavy, jet black",
    "skin_tone": "warm olive",
    "distinctive_mark": "small scar on left eyebrow"
  }
}
```

Inject this block into every prompt for consistency.

### Method 2: Reference Image Anchoring

For strict consistency, pass a reference image:

```json
"subject": {
  "reference_image_id": "img_001",
  "instruction": "maintain facial structure strictly, change clothing to red dress"
}
```

### Method 3: Seed State Pipeline

1. Generate initial character with detailed prompt
2. Save as reference
3. Use reference + variations for subsequent images

---

## Combined Example: Technical Diagram

```json
{
  "system_instruction": "ACTIVATE_LOGIC_CORE",
  "mode": "strict_adherence",
  "task": "technical_diagram",
  "logic_constraints": {
    "count_enforcement": "strict",
    "text_accuracy": "100%",
    "spatial_relation": "absolute",
    "label_accuracy": "100%"
  },
  "content": {
    "subject": "Computer Motherboard",
    "view": "top-down orthographic",
    "components": [
      { "name": "CPU Socket", "position": "upper center" },
      { "name": "RAM Slots", "count": 4, "position": "right of CPU" },
      { "name": "PCIe Slots", "count": 3, "position": "lower half" },
      { "name": "SATA Ports", "count": 6, "position": "right edge" }
    ],
    "labels": [
      { "text": "LGA 1700 Socket", "target": "CPU Socket" },
      { "text": "DDR5 DIMM Slots (x4)", "target": "RAM Slots" },
      { "text": "PCIe 5.0 x16", "target": "first PCIe slot" }
    ]
  },
  "style": {
    "aesthetic": "technical illustration",
    "background": "neutral gray",
    "line_weight": "clean, consistent"
  }
}
```

---

## Era-Specific Photography

Recreate the aesthetic of specific time periods with period-accurate camera characteristics and environmental elements.

### Era Style Pattern

```json
{
  "photography": {
    "era_style": "early-2000s digital camera",
    "characteristics": {
      "flash": "harsh super-flash with blown-out highlights",
      "texture": "subtle grain, retro color cast",
      "resolution": "slightly soft, early CMOS sensor look"
    }
  },
  "background": {
    "period_elements": ["chunky wooden dresser", "CD player", "beaded door curtain", "butterfly clips"]
  }
}
```

### Common Era Presets

| Era | Camera Style | Lighting | Texture |
|-----|-------------|----------|---------|
| 1990s film | disposable camera | red-eye flash | heavy grain, muted colors |
| Early 2000s | first digital cameras | harsh flash, blown highlights | slight noise, oversaturated |
| 2010s smartphone | early iPhone/Android | mixed ambient + flash | HDR look, slight blur |
| Polaroid | instant film | natural with flash fill | faded edges, warm cast |

---

## Dramatic Lighting Control

Control spotlight focus and shadow falloff for cinematic, moody imagery.

### Spotlight Pattern

```json
{
  "cinematography": {
    "lighting": {
      "type": "narrow beam spotlight",
      "focus": "center of face only",
      "falloff": "high",
      "shadow_quality": "sharp, dramatic edges",
      "background_treatment": "fade into complete darkness"
    }
  },
  "style": {
    "mood": "dark, moody, mysterious",
    "reference": "film noir, Rembrandt lighting"
  }
}
```

### Falloff Settings

| Falloff | Effect | Use Case |
|---------|--------|----------|
| `"high"` | Rapid light decay, deep shadows | Dramatic portraits, noir |
| `"medium"` | Gradual transition | Editorial, fashion |
| `"low"` | Soft, even lighting | Commercial, beauty |

---

## Crowd & Multi-Character Composition

Manage complex scenes with multiple subjects interacting naturally.

### Multi-Character Pattern

```json
{
  "subjects": [
    {
      "id": "subject_1",
      "description": "woman in red dress",
      "position": "foreground left",
      "action": "laughing, gesturing"
    },
    {
      "id": "subject_2",
      "description": "man in navy suit",
      "position": "foreground right",
      "action": "listening, leaning in"
    },
    {
      "id": "subject_3",
      "description": "group of 3-4 people",
      "position": "background",
      "focus": "soft blur"
    }
  ],
  "interaction": {
    "type": "natural conversation",
    "eye_lines": "subjects 1 and 2 facing each other"
  },
  "cinematography": {
    "lens": "85mm f/1.4",
    "depth_of_field": "shallow, isolate foreground",
    "lighting": {
      "type": "golden rim light",
      "purpose": "separate subjects from background"
    }
  }
}
```

### Crowd Management Tips

- Use `"focus": "soft blur"` for background figures
- Apply `"golden rim light"` to separate subjects
- Specify `"natural interactions"` to avoid stiff poses
- Use 8K resolution for large group details

---

## Outpainting & Context Extension

Extend image boundaries while maintaining style and lighting continuity.

### Outpainting Pattern

```json
{
  "task": "outpainting",
  "reference_image": "provided",
  "extension": {
    "direction": "left and right",
    "amount": "50% on each side"
  },
  "continuity": {
    "lighting": "match existing shadows and highlights",
    "style": "seamless with original",
    "elements": "extend background naturally"
  },
  "constraints": {
    "preserve": "all original content exactly",
    "blend": "invisible seam"
  }
}
```

---

## Virtual Try-On

Visualize products on subjects for e-commerce applications.

### Try-On Pattern

```json
{
  "task": "virtual_try_on",
  "subject": {
    "reference_image": "provided",
    "preserve": "face, body shape, pose exactly"
  },
  "product": {
    "type": "clothing",
    "item": "oversized cashmere sweater",
    "color": "cream",
    "fit": "relaxed, slightly off-shoulder"
  },
  "rendering": {
    "material_accuracy": "visible knit texture, soft drape",
    "lighting_match": "consistent with subject lighting",
    "shadow_integration": "natural fabric shadows on body"
  }
}
```

---

## 3D Diorama / Miniature Style

Create tilt-shift miniature world compositions.

### Diorama Pattern

```json
{
  "style": {
    "type": "3D diorama",
    "effect": "tilt-shift miniature"
  },
  "subject": {
    "concept": "country as floating island",
    "elements": ["iconic landmarks", "terrain features", "tiny people"]
  },
  "cinematography": {
    "lens": "tilt-shift",
    "depth_of_field": "extreme shallow, toy-like blur",
    "angle": "isometric or slight bird's eye"
  },
  "lighting": {
    "type": "soft, even studio lighting",
    "purpose": "enhance miniature illusion"
  }
}
```

---

## Temporal Aging Effects

Progress or regress a subject's age while maintaining identity.

### Age Progression Pattern

```json
{
  "task": "temporal_aging",
  "subject": {
    "reference_image": "provided",
    "identity_preservation": "strict - same person, different age"
  },
  "transformation": {
    "direction": "age forward",
    "target_age": "70s",
    "changes": {
      "skin": "natural wrinkles, age spots, texture changes",
      "hair": "gray/white, possibly thinner",
      "structure": "subtle bone structure changes"
    }
  },
  "preserve": {
    "features": "eye color, distinctive marks, bone structure essence",
    "expression": "similar personality in face"
  }
}
```
