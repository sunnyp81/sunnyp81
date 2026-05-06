# Spatial Logic - Floor Plans, Counting, Math

Techniques for tasks requiring precise spatial reasoning, dimensional accuracy, and logical constraints.

---

## Architectural Floor Plans

Nano Banana Pro can generate architectural plans when given explicit dimensional data.

### Basic Floor Plan

```json
{
  "system_instruction": "ACTIVATE_LOGIC_CORE",
  "mode": "strict_adherence",
  "task": "architectural_floor_plan",
  "logic_constraints": {
    "dimensional_accuracy": "strict",
    "spatial_relation": "absolute",
    "scale_consistency": "maintained"
  },
  "project": {
    "type": "residential floor plan",
    "style": "architectural blueprint",
    "overall_dimensions": {
      "width": "13m",
      "depth": "11m",
      "total_area": "143m²"
    }
  },
  "rooms": [
    {
      "name": "Entrance Hallway",
      "dimensions": "3m × 2.5m",
      "location": "south side, center",
      "connections": ["living room", "corridor"]
    },
    {
      "name": "Living Room + Kitchen",
      "dimensions": "7m × 5m",
      "location": "south-west corner",
      "features": [
        "large windows facing west",
        "sliding door to backyard (north wall)",
        "kitchen zone on east part"
      ],
      "layout": "open plan"
    },
    {
      "name": "Master Bedroom",
      "dimensions": "4.5m × 4m",
      "location": "north-west corner",
      "features": ["window facing north", "window facing west"]
    },
    {
      "name": "Bedroom 2",
      "dimensions": "4m × 3.5m",
      "location": "north-east corner",
      "features": ["window facing east"]
    },
    {
      "name": "Bathroom",
      "dimensions": "3m × 2.5m",
      "location": "center-north",
      "adjacency": "between Master Bedroom and Bedroom 2"
    }
  ],
  "rendering": {
    "style": "technical architectural drawing",
    "include": [
      "dimension lines with measurements",
      "door swings",
      "window representations",
      "room labels",
      "north arrow",
      "scale bar"
    ],
    "color_scheme": "blueprint blue and white"
  }
}
```

### Multi-Story Building

```json
{
  "project": "multi_story_floor_plans",
  "building": {
    "stories": 3,
    "footprint": "20m × 15m"
  },
  "floors": [
    {
      "level": "ground",
      "rooms": [
        { "name": "Lobby", "dimensions": "8m × 6m", "position": "front center" },
        { "name": "Retail Space", "dimensions": "10m × 8m", "position": "left wing" }
      ]
    },
    {
      "level": "first",
      "rooms": [
        { "name": "Office A", "dimensions": "10m × 7m" },
        { "name": "Office B", "dimensions": "8m × 7m" }
      ]
    },
    {
      "level": "second",
      "rooms": [
        { "name": "Conference Room", "dimensions": "12m × 8m" },
        { "name": "Break Room", "dimensions": "6m × 5m" }
      ]
    }
  ],
  "layout": {
    "arrangement": "floors stacked vertically",
    "alignment": "aligned by exterior walls",
    "stairwell": "consistent position on all floors"
  }
}
```

---

## Counting Challenges

### The "S" Object Challenge

Generate a specific number of people each holding unique objects.

```json
{
  "system_instruction": "ACTIVATE_LOGIC_CORE",
  "logic_constraints": {
    "count_enforcement": "strict",
    "uniqueness": "each object must be different"
  },
  "scene": {
    "setting": "office environment",
    "arrangement": {
      "total_people": 20,
      "rows": [
        { "row": "front", "count": 7 },
        { "row": "middle", "count": 6 },
        { "row": "back", "count": 7 }
      ]
    }
  },
  "constraint": {
    "rule": "each person holds unique object starting with 'S'",
    "verification": "20 different S-objects",
    "examples": [
      "scissors", "sunglasses", "stapler", "sandwich", "smartphone",
      "sunflower", "saxophone", "skateboard", "snowglobe", "stopwatch",
      "suitcase", "sword", "scarf", "soda", "spatula",
      "spider plant", "seashell", "stamp", "stethoscope", "sweater"
    ]
  }
}
```

### Grid Arrangements

```json
{
  "system_instruction": "ACTIVATE_LOGIC_CORE",
  "arrangement": {
    "type": "grid",
    "columns": 5,
    "rows": 4,
    "total_cells": 20,
    "verification": "5 × 4 = 20 items"
  },
  "items": {
    "type": "fruit",
    "variety": "mixed",
    "per_cell": 1,
    "spacing": "even"
  }
}
```

### Specific Quantities

```json
{
  "system_instruction": "ACTIVATE_LOGIC_CORE",
  "scene": "birthday party table",
  "items": [
    {
      "object": "candles on cake",
      "count": 7,
      "verification": "exactly seven candles",
      "arrangement": "circle on top of cake"
    },
    {
      "object": "party guests",
      "count": 12,
      "verification": "twelve people around table",
      "arrangement": "seated around circular table"
    },
    {
      "object": "balloons",
      "count": 15,
      "verification": "fifteen balloons",
      "arrangement": "floating at various heights"
    }
  ]
}
```

---

## Mathematical Visualizations

### Geometry Problems

```json
{
  "system_instruction": "ACTIVATE_LOGIC_CORE",
  "task": "geometry_visualization",
  "logic_constraints": {
    "geometric_accuracy": "strict",
    "angle_accuracy": "precise"
  },
  "problem": {
    "type": "triangle proof",
    "given": {
      "triangle": "ABC",
      "properties": [
        "angle A = 60°",
        "angle B = 60°",
        "angle C = 60°"
      ]
    },
    "show": "equilateral triangle",
    "labels": [
      { "point": "A", "position": "top vertex" },
      { "point": "B", "position": "bottom left" },
      { "point": "C", "position": "bottom right" }
    ],
    "annotations": [
      { "type": "angle arc", "at": "A", "label": "60°" },
      { "type": "angle arc", "at": "B", "label": "60°" },
      { "type": "angle arc", "at": "C", "label": "60°" },
      { "type": "side length", "side": "AB", "label": "a" },
      { "type": "side length", "side": "BC", "label": "a" },
      { "type": "side length", "side": "CA", "label": "a" }
    ]
  },
  "style": {
    "aesthetic": "clean mathematical diagram",
    "background": "white or graph paper",
    "line_weight": "medium"
  }
}
```

### Calculus Visualization

```json
{
  "system_instruction": "ACTIVATE_LOGIC_CORE",
  "task": "math_solution",
  "logic_constraints": {
    "symbolic_accuracy": "100%",
    "step_verification": true
  },
  "problem": {
    "expression": "∫4xcos(2−3x)dx",
    "type": "indefinite integral"
  },
  "display": {
    "format": "whiteboard solution",
    "requirements": [
      "correct mathematical notation",
      "integration by parts method shown",
      "clear intermediate steps",
      "proper alignment of equations",
      "final answer boxed"
    ]
  },
  "steps": [
    { "step": 1, "content": "Let u = 4x, dv = cos(2-3x)dx" },
    { "step": 2, "content": "du = 4dx, v = -1/3 sin(2-3x)" },
    { "step": 3, "content": "Apply integration by parts: uv - ∫vdu" },
    { "step": "final", "content": "boxed answer" }
  ]
}
```

---

## Organizational Charts

```json
{
  "system_instruction": "ACTIVATE_LOGIC_CORE",
  "task": "org_chart",
  "logic_constraints": {
    "hierarchy_accuracy": "strict",
    "connection_accuracy": "all lines connect correctly"
  },
  "structure": {
    "type": "corporate hierarchy",
    "levels": [
      {
        "level": 1,
        "title": "CEO",
        "count": 1
      },
      {
        "level": 2,
        "title": "C-Suite",
        "positions": ["CFO", "CTO", "COO"],
        "count": 3,
        "reports_to": "CEO"
      },
      {
        "level": 3,
        "title": "Directors",
        "count": 6,
        "distribution": "2 per C-Suite member"
      },
      {
        "level": 4,
        "title": "Managers",
        "count": 12,
        "distribution": "2 per Director"
      }
    ]
  },
  "rendering": {
    "style": "professional org chart",
    "boxes": "rounded rectangles",
    "connectors": "straight lines with right angles",
    "color_coding": "by level"
  }
}
```

---

## Seating Arrangements

```json
{
  "system_instruction": "ACTIVATE_LOGIC_CORE",
  "task": "seating_chart",
  "logic_constraints": {
    "count_enforcement": "strict",
    "spatial_relation": "absolute"
  },
  "venue": {
    "type": "wedding reception",
    "tables": [
      {
        "id": "head_table",
        "shape": "long rectangular",
        "seats": 8,
        "position": "front center"
      },
      {
        "id": "tables_1-5",
        "shape": "round",
        "seats_per_table": 10,
        "count": 5,
        "position": "left side of venue"
      },
      {
        "id": "tables_6-10",
        "shape": "round",
        "seats_per_table": 10,
        "count": 5,
        "position": "right side of venue"
      }
    ],
    "total_capacity": {
      "calculation": "8 + (5×10) + (5×10)",
      "total": 108
    }
  },
  "rendering": {
    "view": "bird's eye / top-down",
    "include": [
      "table numbers",
      "chair positions",
      "aisle spacing",
      "dance floor area",
      "DJ booth"
    ]
  }
}
```

---

## Common Failures & Fixes

| Problem | Cause | Fix |
|---------|-------|-----|
| Wrong room count | Rooms not enumerated | List each room explicitly |
| Dimensions ignored | Buried in description | Use structured `dimensions` field |
| Items miscounted | No verification | Add `count` AND `verification` |
| Shapes incorrect | Generic description | Use triangulation (type + sides + description) |
| Spatial relations wrong | Ambiguous positioning | Use absolute coordinates or explicit adjacency |

---

## Verification Techniques

Always include multiple verification paths:

```json
{
  "count": 7,
  "count_word": "seven",
  "verification": "exactly 7 items",
  "arrangement_verification": "arranged in single row of 7"
}
```

```json
{
  "shape": "hexagon",
  "sides": 6,
  "shape_description": "six-sided polygon",
  "vertices": 6,
  "interior_angle": "120 degrees each"
}
```

```json
{
  "room_dimensions": "4m × 3m",
  "area": "12 square meters",
  "perimeter": "14 meters"
}
```
