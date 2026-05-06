# Nano Banana - AI Image Generation

Generate images using Google's Gemini models with structured JSON prompts for precise control over compositions.

## Installation

1. Download this zip file
2. In Claude Code, run:
   ```
   /install-skill nano-banana-v1.0.0.zip
   ```
3. Follow the prompts to configure your API key

## Dependencies

### Python Packages
This skill requires:
```
google-genai>=0.2.0
```

Install with:
```bash
pip3 install -r requirements.txt
```

## API Keys & Costs

| Key | Service | Free Tier | Paid Pricing |
|-----|---------|-----------|--------------|
| GEMINI_API_KEY | Google AI Studio | ~1,500 images/day | Flash: ~$0.039/image, Pro: ~$0.134-$0.24/image |

**Get your key:** [aistudio.google.com/apikey](https://aistudio.google.com/apikey)

### Setup Steps
1. Go to aistudio.google.com/apikey
2. Sign in with your Google account
3. Click "Create API Key"
4. Select "Create API key in new project"
5. Copy the key (starts with "AIza", 39 characters)

## Usage

Ask Claude to generate images:
```
Generate a professional headshot, cinematic lighting, shallow depth of field
```

Or with specific parameters:
```
Create a 16:9 YouTube thumbnail background with tech vibes, use the Pro model
```

### Models

| Model | Best For |
|-------|----------|
| Gemini 2.5 Flash ("nano banana") | Speed (~1.5s), simple compositions |
| Gemini 3 Pro ("nano banana pro") | Text rendering, complex scenes, high-res |

### Parameters

| Option | Values | Notes |
|--------|--------|-------|
| Model | flash, pro | Default: flash |
| Aspect Ratio | 1:1, 16:9, 9:16, 4:3, 3:2, 21:9 | Default: square |
| Resolution | 1K, 2K, 4K | 2K/4K require Pro |

## How It Works

See `WORKFLOW.md` for detailed usage instructions and examples.

The skill uses structured JSON prompts to give you precise control over image composition. This prevents common issues like attribute mixing (e.g., a "blue car next to a red house" accidentally becoming a blue house).

## Included Resources

- `references/json-schema.md` - Complete prompt schema documentation
- `references/advanced-techniques.md` - Logic gates, physics overrides, character consistency
- `references/troubleshooting.md` - Common issues and solutions
- `references/examples/` - Ready-to-use prompt examples for various use cases

---
Packaged with Claude Code /export-skill
