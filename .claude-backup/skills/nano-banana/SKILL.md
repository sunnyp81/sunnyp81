---
name: nano-banana
description: Expert guidance for JSON prompting with Google's Gemini image models (Nano Banana / Nano Banana Pro). Use when the user asks to generate images with Gemini, create structured image prompts, design infographics, render text in images, or needs help with JSON prompting for AI image generation.
version: 1.0.0
user-invocable: true
allowed-tools: Read, Write, Bash
argument-hint: "[image description or design brief]"
requires_secrets:
  - key: GEMINI_API_KEY
    service: Google AI Studio
    url: https://aistudio.google.com/apikey
    description: API key for Gemini image generation models
    hint: "Starts with 'AIza', 39 characters total"
    pricing: |
      Free tier: ~1,500 images/day via AI Studio (no credit card)
      Paid: Gemini 2.5 Flash ~$0.039/image, Gemini 3 Pro ~$0.134/image (2K), ~$0.24/image (4K)
    instructions: |
      1. Go to aistudio.google.com/apikey
      2. Sign in with your Google account
      3. Click "Create API Key"
      4. Select "Create API key in new project"
      5. Copy the key that appears
    required: true
---

# Nano Banana JSON Prompting

Expert guidance for crafting structured JSON prompts for Google's Gemini image generation models.

---

## Models

| Model | Marketing Name | Best For |
|-------|---------------|----------|
| Gemini 2.5 Flash Image | Nano Banana | Speed (~1.5s), social media, simple compositions |
| Gemini 3 Pro Image | Nano Banana Pro | Complex logic, text rendering, spatial reasoning |

### Model Selection

| Task | Model | Reason |
|------|-------|--------|
| Social media graphics | Flash | Speed priority |
| Quick iterations | Flash | 1.5s latency |
| Text-heavy designs | Pro | OCR-grade text |
| Infographics with labels | Pro | Logic gates, accuracy |
| Complex spatial logic | Pro | Floor plans, diagrams |
| Character consistency | Pro | Identity preservation |
| High resolution (2K/4K) | Pro | Required for larger outputs |

---

## Why JSON > Natural Language

Natural language: "A blue car next to a red house" - attention mechanisms can "bleed," resulting in a blue house or red car.

With JSON:
```json
{
  "objects": [
    { "type": "car", "color": "blue" },
    { "type": "house", "color": "red" }
  ]
}
```

The brackets `{}` create **hard semantic boundaries**. The attribute `"color": "blue"` is encapsulated within the car object. This **Attribute Binding** is the core advantage of JSON prompting.

---

## Quick Start

```json
{
  "subject": {
    "physicality": {
      "demographics": "woman, mid-20s",
      "face": { "skin_texture": "visible pores, natural" }
    },
    "pose": { "action": "sitting at cafe table" }
  },
  "environment": {
    "location": "Parisian cafe terrace",
    "time_context": { "time_of_day": "golden hour" }
  },
  "cinematography": {
    "camera_body": "Sony A7R IV",
    "lens": "85mm f/1.4",
    "composition": { "framing": "medium close-up", "depth_of_field": "shallow" }
  },
  "constraints": {
    "exclusions": ["airbrushed", "plastic skin", "watermark"]
  }
}
```

---

## Instructions for Claude

When helping with Nano Banana / Gemini image prompts:

1. **Assess complexity first**
   - Simple compositions → natural language may suffice
   - Text rendering, counting, spatial logic → always use JSON

2. **Ask clarifying questions** about:
   - Target model (Flash vs Pro)
   - Whether text must be rendered
   - Need for character consistency
   - Specific camera/lighting aesthetic

3. **For photorealism**: Always include `cinematography` domain with camera/lens. For era-specific looks (2000s selfie, 90s film), use `era_style` field. For dramatic portraits, configure spotlight `focus` and `falloff`

4. **For infographics**: Use logic gates and explicit `labels` arrays

5. **Structure prompts hierarchically**:
   - Use deep nesting to isolate attributes
   - Never mix multiple objects at same level
   - Use arrays `[]` for enumerable elements

6. **Provide complete, ready-to-use JSON** that can be directly passed to the API

7. **Generate images directly** using the included Python script (see API Usage below)

---

## API Usage

### Setup (One-Time)

1. **Get API Key**: Visit https://aistudio.google.com/apikey

2. **Configure**:
   ```bash
   cd /path/to/nano-banana
   cp .config.example.json .config.json
   # Edit .config.json and add your key
   ```

3. **Install**: `pip3 install -r requirements.txt`

### CLI Reference

```bash
python3 scripts/generate_image.py [OPTIONS] < prompt.json
```

| Option | Description |
|--------|-------------|
| `--model flash\|pro` | Model selection (default: flash) |
| `--image PATH` | Input image for editing (repeatable) |
| `--aspect-ratio RATIO` | 1:1, 16:9, 9:16, 4:3, 3:2, 21:9 |
| `--resolution SIZE` | 1K, 2K, 4K (2K/4K require Pro) |
| `--no-open` | Don't auto-open result |

### Generation Workflow

1. **Write JSON prompt to temp file**:
   ```bash
   cat > /tmp/prompt.json << 'EOF'
   { "subject": { ... }, "environment": { ... } }
   EOF
   ```

2. **Execute**:
   ```bash
   python3 scripts/generate_image.py --model flash < /tmp/prompt.json
   ```

3. **Result**: Saved to ~/Downloads, auto-opened in Preview

### Examples

```bash
# Basic generation
python3 scripts/generate_image.py --model flash < /tmp/prompt.json

# With aspect ratio
python3 scripts/generate_image.py --aspect-ratio 16:9 < /tmp/prompt.json

# High-res
python3 scripts/generate_image.py --model pro --resolution 4K < /tmp/prompt.json

# Edit existing image
python3 scripts/generate_image.py --image /path/to/photo.jpg < /tmp/prompt.json
```

---

## References

Detailed documentation for specific topics:

### Core References
- [JSON Schema](references/json-schema.md) - Complete schema for all domains
- [Advanced Techniques](references/advanced-techniques.md) - Logic gates, physics overrides, character consistency
- [Troubleshooting](references/troubleshooting.md) - Common issues and solutions

### Examples

**Photorealism**
- [portrait-cinematic.md](references/examples/photorealism/portrait-cinematic.md) - Camera and lighting mastery
- [mirror-selfie.md](references/examples/photorealism/mirror-selfie.md) - Physics override for reflections
- [era-photography.md](references/examples/photorealism/era-photography.md) - 2000s selfies, 90s film, Polaroid styles

**Infographics**
- [technical-breakdown.md](references/examples/infographics/technical-breakdown.md) - Labeled technical diagrams
- [poster-layout.md](references/examples/infographics/poster-layout.md) - Multi-section typography layouts

**Use Cases**
- [character-consistency.md](references/examples/use-cases/character-consistency.md) - Identity preservation
- [spatial-logic.md](references/examples/use-cases/spatial-logic.md) - Floor plans, counting, math
- [crowd-composition.md](references/examples/use-cases/crowd-composition.md) - Multi-character scenes
- [virtual-tryon.md](references/examples/use-cases/virtual-tryon.md) - E-commerce product visualization
- [outpainting.md](references/examples/use-cases/outpainting.md) - Context extension

**Creative**
- [diorama-miniature.md](references/examples/creative/diorama-miniature.md) - Tilt-shift miniature worlds
