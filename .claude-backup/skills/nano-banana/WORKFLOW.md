# How to Use: Nano Banana

Generate AI images using Google's Gemini models with structured JSON prompts.

## Quick Start

**1. Describe what you want:**
```
Generate an image of a professional headshot, cinematic lighting, shallow depth of field
```

**2. Claude builds the JSON prompt and runs the script**

**3. Image saves to ~/Downloads and opens automatically**

## Example Workflows

### Simple Image Generation
```
Generate a product photo of a coffee mug on a wooden table, morning light
```

### Photorealistic Portrait
```
Create a cinematic portrait: woman in her 30s at a Parisian cafe,
golden hour lighting, shot on Sony A7R with 85mm f/1.4 lens, shallow DOF
```

### With Specific Aspect Ratio
```
Generate a YouTube thumbnail background, 16:9 aspect ratio,
tech-focused with blue gradients and circuit patterns
```

### High Resolution (Pro Model)
```
Create a 4K image of a mountain landscape at sunset,
dramatic clouds, use the Pro model for maximum quality
```

### Edit an Existing Image
```
Take this photo [attach image] and make it look like a vintage 1970s polaroid
```

### Multiple Reference Images
```
Here are my brand colors [attach palette] and logo [attach logo].
Create a social media banner that incorporates both.
```

## Model Selection

| Use Case | Model | Why |
|----------|-------|-----|
| Quick iterations | Flash | ~1.5s generation |
| Social media graphics | Flash | Speed priority |
| Text in images | Pro | Better text rendering |
| Infographics with labels | Pro | Accurate text placement |
| 2K/4K resolution | Pro | Required for high-res |
| Complex compositions | Pro | Better spatial reasoning |

## Tips

1. **Be specific about style** - mention camera, lens, lighting for photorealism
2. **Use JSON for complex scenes** - prevents attribute mixing (blue car, red house staying separate)
3. **Reference the examples** - check `references/examples/` for proven prompt patterns
4. **Iterate quickly with Flash** - switch to Pro only when you need quality/text

## Common Parameters

| Parameter | Options | Notes |
|-----------|---------|-------|
| `--model` | flash, pro | Default: flash |
| `--aspect-ratio` | 1:1, 16:9, 9:16, 4:3, 3:2, 21:9 | Default: square |
| `--resolution` | 1K, 2K, 4K | 2K/4K require Pro |
| `--no-open` | flag | Don't auto-open result |

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "API key not found" | Add `GEMINI_API_KEY=your-key` to your project's .env file |
| "google-genai not installed" | Run `pip3 install google-genai` |
| Content blocked by safety | Rephrase prompt to avoid sensitive content |
| Rate limit exceeded | Wait a moment and retry |
| No image in response | Make prompt more visual/specific |

## Getting Your API Key

1. Go to [aistudio.google.com/apikey](https://aistudio.google.com/apikey)
2. Sign in with Google
3. Click "Create API Key"
4. Add to your `.env` file: `GEMINI_API_KEY=your-key-here`

## Pricing

- **Free tier**: ~1,500 images/day via AI Studio (no credit card needed)
- **Gemini 2.5 Flash**: ~$0.039/image
- **Gemini 3 Pro**: ~$0.134/image (2K), ~$0.24/image (4K)
