# Technical Breakdown Infographic

This example demonstrates Nano Banana Pro's ability to generate technical diagrams with correct labeling - a task that historically resulted in "AI gibberish."

## The F-117 Nighthawk Example

```json
{
  "project": "F-117_Technical_Breakdown",
  "style": "engineering blueprint",
  "layout_engine": {
    "type": "exploded view",
    "background_color": "#003366",
    "line_color": "#FFFFFF",
    "font": "technical sans-serif"
  },
  "subject": {
    "name": "F-117 Nighthawk",
    "orientation": "isometric",
    "rendering": "wireframe with solid core"
  },
  "labels": [
    { "text": "Faceted Airframe", "target": "fuselage", "connector": "white line with arrow" },
    { "text": "Radar Absorbent Material", "target": "wing surface", "connector": "white line" },
    { "text": "V-Tail Assembly", "target": "tail", "connector": "white line" },
    { "text": "F404 Turbofan Engine", "target": "engine", "connector": "white line" },
    { "text": "Internal Weapons Bay", "target": "center fuselage", "connector": "white line" }
  ],
  "title_block": {
    "text": "LOCKHEED F-117 NIGHTHAWK",
    "position": "bottom center",
    "size": "large header"
  }
}
```

## Key Techniques

### The Labels Array

```json
"labels": [
  { "text": "Component Name", "target": "part_location", "connector": "line_style" }
]
```

By defining an array of label objects, we provide the Thinking Model with a to-do list:
1. Model identifies each `target` in its generated geometry
2. Draws a vector from that coordinate to clear space
3. Renders the `text` with specified `connector` style

### Exploded View

```json
"layout_engine": {
  "type": "exploded view"
}
```

Triggers spatial arrangement where components are separated along an axis, revealing internal details that would otherwise be hidden.

### Layout Types

| Type | Description | Best For |
|------|-------------|----------|
| `exploded view` | Components separated along axis | Mechanical assemblies |
| `cutaway` | Section removed to show interior | Buildings, vehicles |
| `orthographic` | Multiple flat views (top, front, side) | Engineering drawings |
| `isometric` | 3D view without perspective distortion | Technical illustrations |
| `cross-section` | Slice through object | Anatomy, geology |

## Automotive Technical Breakdown

```json
{
  "project": "Engine_Technical_Breakdown",
  "style": "automotive cutaway illustration",
  "layout_engine": {
    "type": "cutaway",
    "background": "gradient from #1a1a2e to #16213e",
    "accent_color": "#e94560",
    "font": "Eurostile Bold Extended"
  },
  "subject": {
    "name": "V8 Twin-Turbo Engine",
    "rendering": "photorealistic with selective cutaway",
    "angle": "three-quarter front view"
  },
  "labels": [
    { "text": "Twin-scroll Turbocharger", "target": "turbo housing", "style": "callout box" },
    { "text": "Forged Aluminum Pistons", "target": "piston", "style": "leader line" },
    { "text": "Direct Injection Rail", "target": "fuel rail", "style": "leader line" },
    { "text": "Variable Valve Timing", "target": "camshaft", "style": "leader line" },
    { "text": "Water-cooled Intercooler", "target": "intercooler", "style": "callout box" }
  ],
  "specifications_panel": {
    "position": "right side",
    "data": [
      "Displacement: 4.0L",
      "Power: 600 HP @ 6,500 RPM",
      "Torque: 550 lb-ft @ 3,500 RPM",
      "Compression: 10.5:1"
    ]
  }
}
```

## Product Breakdown (Consumer Electronics)

```json
{
  "project": "Smartphone_Teardown",
  "style": "iFixit-style teardown",
  "layout_engine": {
    "type": "exploded view",
    "background": "clean white (#FFFFFF)",
    "shadows": "soft drop shadows on components",
    "arrangement": "vertical stack with spacing"
  },
  "subject": {
    "name": "Premium Smartphone",
    "components_visible": [
      "display assembly",
      "battery",
      "motherboard",
      "camera module",
      "frame",
      "back glass"
    ]
  },
  "labels": [
    { "text": "6.7\" OLED Display", "target": "display", "details": "120Hz, 2K resolution" },
    { "text": "5000mAh Battery", "target": "battery", "details": "65W fast charging" },
    { "text": "A18 Pro Chip", "target": "motherboard", "details": "3nm process" },
    { "text": "48MP Main Camera", "target": "camera module", "details": "OIS, f/1.8" }
  ],
  "numbering": {
    "style": "circled numbers",
    "color": "#007AFF"
  }
}
```

## Label Styling Options

```json
"labels": [
  {
    "text": "Component Name",
    "target": "location",
    "connector": "white line",
    "style": {
      "type": "callout_box",
      "background": "semi-transparent black",
      "border": "1px white",
      "font_size": "12pt",
      "font_weight": "bold"
    }
  }
]
```

### Connector Types

- `leader line` - Simple line with arrow
- `elbow connector` - Line with 90-degree bend
- `curved connector` - Smooth curved line
- `bracket` - For grouping multiple parts

## Common Failures & Fixes

| Problem | Cause | Fix |
|---------|-------|-----|
| Labels overlap | Too many labels, no spacing logic | Reduce label count or specify `spacing: generous` |
| Text illegible | Wrong font size or color contrast | Specify explicit `font_size` and ensure contrast |
| Wrong component targeted | Ambiguous target name | Use specific part names matching technical terminology |
| Lines cross each other | No optimization | Add `connector_routing: optimized` |
