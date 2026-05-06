# Troubleshooting Guide

Common issues and solutions for Nano Banana image generation.

---

## "Plastic Skin" Artifact

**Symptom**: Subjects look like wax figures or video game characters.

**Cause**: Model defaults to smooth, idealized skin without imperfections.

**Solution**:

```json
"texture_imperfections": {
  "skin": "visible pores, micro-wrinkles, slight asymmetry",
  "lighting": "harsh shadows (avoid soft lighting)"
}
```

Also add to exclusions:
```json
"exclusions": ["smooth", "airbrushed", "cartoon", "illustration"]
```

---

## Text Drift / Spelling Errors

**Symptom**: Text "COFFEE" renders as "COFEE" or floats in air.

**Cause**: Text gets lost in nested structures or lacks anchoring.

**Solutions**:

1. **Elevate text to root level** or dedicated `typography` block

2. **Use quote delimiters and strict flag**:
```json
"text_instruction": {
  "content": "'COFFEE'",
  "strict_spelling": true,
  "character_verification": "C-O-F-F-E-E"
}
```

3. **Use Logic Gates** for text-heavy designs:
```json
{
  "system_instruction": "ACTIVATE_LOGIC_CORE",
  "logic_constraints": {
    "text_accuracy": "100%"
  }
}
```

---

## Logic Drift (Counting, Shapes)

**Symptom**: Asked for pentagon, got hexagon. Asked for 5 items, got 7.

**Cause**: Diffusion models struggle with exact quantities and geometry.

**Solutions**:

1. **Use `ACTIVATE_LOGIC_CORE` header**

2. **State constraint multiple ways (triangulation)**:
```json
"shape": {
  "type": "pentagon",
  "sides_count": 5,
  "visual_description": "five-sided polygon",
  "verification": "count vertices: 5"
}
```

3. **Enumerate objects explicitly**:
```json
"objects": [
  { "id": "item_1", "position": "far left" },
  { "id": "item_2", "position": "left of center" },
  { "id": "item_3", "position": "center" },
  { "id": "item_4", "position": "right of center" },
  { "id": "item_5", "position": "far right" }
]
```

---

## Attribute Bleeding

**Symptom**: Colors or properties assigned to wrong objects. Blue car becomes blue house.

**Cause**: Attributes at the same nesting level can "bleed" across objects.

**Solution**: Increase nesting depth. Never put multiple objects at same level with shared attributes.

**Bad**:
```json
{
  "car": { "color": "blue" },
  "house": { "color": "red" }
}
```

**Good**:
```json
{
  "objects": [
    { "type": "car", "properties": { "color": "blue" } },
    { "type": "house", "properties": { "color": "red" } }
  ]
}
```

---

## Mirror Reflections Wrong

**Symptom**: Text in mirrors is reversed (physically correct but unusable). Phone screens show wrong content.

**Cause**: Model follows real-world physics.

**Solution**: Use physics override:

```json
"mirror_physics_override": {
  "instruction": "IGNORE mirror physics for text",
  "text_orientation": "legible to viewer (non-reversed)",
  "phone_screen": "blank or camera UI"
}
```

---

## API Errors

### "google-genai not installed"

```bash
pip3 install google-genai
```

### "Config file not found"

```bash
cp .config.example.json .config.json
# Add your API key to .config.json
```

### "Invalid API key"

- Check your key at https://aistudio.google.com/apikey
- Ensure the key is correctly copied (no extra spaces)

### "No image in response"

- The prompt may have been blocked by safety filters
- Try rephrasing to avoid sensitive content

### "Rate limit exceeded"

- Wait a moment and try again
- Consider using the Flash model for faster iterations

### "Image file not found"

- Check the path to your input image
- Use absolute paths for reliability

---

## Quick Diagnostic Checklist

| Issue | First Thing to Check |
|-------|---------------------|
| Plastic skin | Add `"skin_texture": "visible pores"` |
| Wrong text | Use `ACTIVATE_LOGIC_CORE` + `strict_spelling` |
| Wrong count | Enumerate objects explicitly |
| Colors swapped | Increase nesting depth |
| Mirror text reversed | Add `physics_override` block |
| API error | Check `.config.json` has valid key |
