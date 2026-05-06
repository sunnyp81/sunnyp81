# Logic Gates - Strict Adherence Patterns

Logic Gates are meta-instructions that signal to Nano Banana Pro's reasoning engine to prioritize accuracy over creativity. Essential for infographics, diagrams, counting tasks, and text rendering.

## The Logic Gate Wrapper

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

## When to Use Logic Gates

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
    "problem": "∫4xcos(2−3x)dx",
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

When you need to break physical rules.

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

### Common Physics Overrides

| Rule to Override | Instruction |
|-----------------|-------------|
| Mirror text reversal | Render text legible |
| Shadow direction | Force consistent shadows |
| Reflection accuracy | Simplify complex reflections |
| Gravity | Objects can float |
| Scale consistency | Allow impossible scales |

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
