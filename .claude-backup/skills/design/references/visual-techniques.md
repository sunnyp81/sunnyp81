# Visual Techniques Reference

Copy-pasteable CSS/Tailwind patterns for 21st.dev-level visual craft. Load this file before writing frontend CSS.

---

## Backgrounds and Atmosphere

### Aurora Blobs

2-3 large radial gradients with blur, absolutely positioned, slow animated drift.

```html
<div class="relative overflow-hidden">
  <!-- Aurora blob 1 -->
  <div class="absolute -top-40 -left-40 w-96 h-96 rounded-full opacity-30 blur-[80px] animate-aurora-1"
       style="background: radial-gradient(circle, var(--brand-400), transparent 70%)"></div>
  <!-- Aurora blob 2 -->
  <div class="absolute -bottom-20 -right-32 w-80 h-80 rounded-full opacity-20 blur-[100px] animate-aurora-2"
       style="background: radial-gradient(circle, var(--accent-400), transparent 70%)"></div>
  <!-- Content on top -->
  <div class="relative z-10">...</div>
</div>
```

Keyframes (add to Tailwind config or `<style>`):
```css
@keyframes aurora-1 {
  0%, 100% { transform: translate(0, 0) scale(1); }
  33% { transform: translate(30px, -20px) scale(1.1); }
  66% { transform: translate(-20px, 15px) scale(0.95); }
}
@keyframes aurora-2 {
  0%, 100% { transform: translate(0, 0) scale(1); }
  50% { transform: translate(-40px, 20px) scale(1.05); }
}
.animate-aurora-1 { animation: aurora-1 15s ease-in-out infinite; }
.animate-aurora-2 { animation: aurora-2 20s ease-in-out infinite; }
```

### Dot Grid

Subtle repeating dots that fade at edges via mask.

```html
<div class="absolute inset-0 opacity-20"
     style="background-image: radial-gradient(circle, rgba(255,255,255,0.3) 1px, transparent 1px);
            background-size: 24px 24px;
            mask-image: radial-gradient(ellipse at center, black 30%, transparent 70%);">
</div>
```

Dark mode variant (lighter dots):
```css
background-image: radial-gradient(circle, rgba(255,255,255,0.15) 1px, transparent 1px);
```

Light mode variant (darker dots):
```css
background-image: radial-gradient(circle, rgba(0,0,0,0.08) 1px, transparent 1px);
```

### Noise / Grain Texture

Inline SVG filter for film-grain depth. Apply as an overlay at low opacity.

```html
<svg class="absolute inset-0 w-full h-full opacity-[0.03] pointer-events-none" xmlns="http://www.w3.org/2000/svg">
  <filter id="grain">
    <feTurbulence type="fractalNoise" baseFrequency="0.65" numOctaves="3" stitchTiles="stitch"/>
    <feColorMatrix type="saturate" values="0"/>
  </filter>
  <rect width="100%" height="100%" filter="url(#grain)"/>
</svg>
```

Adjust opacity: 0.02-0.05 for subtle, 0.08-0.12 for gritty.

### Gradient Mesh

Multiple overlapping conic/radial gradients on separate layers, each animated at different speeds.

```html
<div class="absolute inset-0 overflow-hidden">
  <div class="absolute inset-0 opacity-40"
       style="background: conic-gradient(from 0deg at 30% 40%, var(--brand-500), transparent, var(--accent-500), transparent);
              animation: mesh-spin-1 25s linear infinite;"></div>
  <div class="absolute inset-0 opacity-30"
       style="background: radial-gradient(ellipse at 70% 60%, var(--brand-300), transparent 60%);
              animation: mesh-spin-2 30s linear infinite reverse;"></div>
</div>
```

```css
@keyframes mesh-spin-1 { to { transform: rotate(360deg); } }
@keyframes mesh-spin-2 { to { transform: rotate(-360deg); } }
```

### Vignette

Darkens edges to focus attention on center content.

```html
<div class="absolute inset-0 pointer-events-none"
     style="background: radial-gradient(ellipse at center, transparent 40%, rgba(0,0,0,0.5) 100%);">
</div>
```

---

## Borders and Containers

### Animated Gradient Border

Rotating conic gradient wrapper with solid inner background.

```html
<div class="relative p-[1px] rounded-2xl overflow-hidden group">
  <!-- Spinning gradient border -->
  <div class="absolute inset-0 rounded-2xl"
       style="background: conic-gradient(from var(--angle, 0deg), var(--brand-500), var(--accent-500), var(--brand-500));
              animation: border-spin 3s linear infinite;"></div>
  <!-- Inner content -->
  <div class="relative rounded-2xl bg-gray-950 p-6">
    ...
  </div>
</div>
```

```css
@property --angle {
  syntax: '<angle>';
  initial-value: 0deg;
  inherits: false;
}
@keyframes border-spin {
  to { --angle: 360deg; }
}
```

Fallback for browsers without `@property`: use a pseudo-element with `transform: rotate()` instead.

### Glow Border on Hover

Color-tinted box-shadow that appears smoothly on hover.

```html
<div class="rounded-2xl border border-white/10 bg-white/5
            transition-shadow duration-300 ease-out
            hover:shadow-[0_0_20px_rgba(var(--brand-rgb),0.3),0_0_60px_rgba(var(--brand-rgb),0.1)]">
  ...
</div>
```

For Tailwind-only (no CSS vars): replace with specific color values:
```html
hover:shadow-[0_0_20px_rgba(124,58,237,0.3),0_0_60px_rgba(124,58,237,0.1)]
```

### Glassmorphism Card

Frosted glass effect with translucent background + backdrop blur + subtle border.

```html
<div class="backdrop-blur-xl bg-white/5 border border-white/10 rounded-2xl p-6
            shadow-lg shadow-black/5">
  ...
</div>
```

Light mode variant:
```html
<div class="backdrop-blur-xl bg-white/70 border border-white/30 rounded-2xl p-6
            shadow-lg shadow-black/5">
  ...
</div>
```

Key: `backdrop-blur-xl` (or `backdrop-blur-2xl` for stronger effect), semi-transparent bg, thin semi-transparent border.

### Spotlight on Hover (CSS-only)

Card that reveals a radial glow following approximate mouse position via CSS. Uses `:hover` with a radial gradient positioned via padding trick.

Simplified version (centered glow):
```html
<div class="relative overflow-hidden rounded-2xl border border-white/10 bg-gray-950 p-6 group">
  <div class="absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-500"
       style="background: radial-gradient(600px circle at 50% 50%, rgba(var(--brand-rgb), 0.1), transparent 40%);">
  </div>
  <div class="relative z-10">...</div>
</div>
```

For true cursor-following, add a small JS snippet:
```js
card.addEventListener('mousemove', (e) => {
  const rect = card.getBoundingClientRect();
  card.style.setProperty('--x', `${e.clientX - rect.left}px`);
  card.style.setProperty('--y', `${e.clientY - rect.top}px`);
});
```
Then use `at var(--x) var(--y)` in the radial gradient position.

---

## Motion Patterns

### Fade-Up on Scroll

Elements start invisible and shifted down, animate in when visible.

CSS-only approach with `@starting-style` (modern browsers):
```css
.fade-up {
  animation: fade-up 0.6s ease-out both;
  animation-timeline: view();
  animation-range: entry 0% entry 30%;
}
@keyframes fade-up {
  from { opacity: 0; transform: translateY(24px); }
  to { opacity: 1; transform: translateY(0); }
}
```

IntersectionObserver fallback (broader support):
```html
<script>
const observer = new IntersectionObserver((entries) => {
  entries.forEach(e => { if (e.isIntersecting) {
    e.target.classList.add('visible');
    observer.unobserve(e.target);
  }});
}, { threshold: 0.1 });
document.querySelectorAll('.fade-up').forEach(el => observer.observe(el));
</script>
<style>
.fade-up { opacity: 0; transform: translateY(24px); transition: opacity 0.6s ease-out, transform 0.6s ease-out; }
.fade-up.visible { opacity: 1; transform: translateY(0); }
</style>
```

### Staggered Entrance

Child elements animate in sequence with increasing delay.

```html
<div class="grid grid-cols-3 gap-6">
  <div class="fade-up" style="transition-delay: 0ms">...</div>
  <div class="fade-up" style="transition-delay: 80ms">...</div>
  <div class="fade-up" style="transition-delay: 160ms">...</div>
  <div class="fade-up" style="transition-delay: 240ms">...</div>
  <div class="fade-up" style="transition-delay: 320ms">...</div>
  <div class="fade-up" style="transition-delay: 400ms">...</div>
</div>
```

Or generate with CSS custom property:
```css
.stagger-child { transition-delay: calc(var(--i, 0) * 80ms); }
```
```html
<div class="fade-up stagger-child" style="--i: 0">...</div>
<div class="fade-up stagger-child" style="--i: 1">...</div>
```

### Hover Lift

Card rises slightly with deeper shadow on hover.

```html
<div class="transition-all duration-300 ease-out
            hover:-translate-y-1 hover:shadow-xl hover:shadow-black/10">
  ...
</div>
```

Note: This is the ONE exception where `transition-all` is acceptable -- on a simple card lift. For complex components, be explicit: `transition: transform 0.3s, box-shadow 0.3s`.

### Shimmer Sweep

A light sweep animation across a button or card surface.

```html
<button class="relative overflow-hidden ...">
  <span class="relative z-10">Get Started</span>
  <div class="absolute inset-0 -translate-x-full animate-shimmer"
       style="background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);"></div>
</button>
```

```css
@keyframes shimmer {
  to { transform: translateX(100%); }
}
.animate-shimmer { animation: shimmer 2.5s ease-in-out infinite; }
```

### Spring Easing

Bouncy micro-interactions for buttons and interactive elements.

```css
.spring { transition-timing-function: cubic-bezier(0.34, 1.56, 0.64, 1); }
```

Use on `:active` scale-down:
```html
<button class="transition-transform duration-200 spring hover:scale-105 active:scale-95">
  ...
</button>
```

---

## Text Effects

### Gradient Text

Background-clip technique for colorful headings.

```html
<h1 class="text-5xl font-bold bg-gradient-to-r from-purple-400 via-pink-400 to-orange-400 bg-clip-text text-transparent">
  Ship faster
</h1>
```

Always pair with a solid-color fallback for accessibility:
```css
@supports not (background-clip: text) {
  h1 { color: var(--brand-400); }
}
```

### Text Glow

Soft light emission behind headings for dramatic effect.

```html
<h1 class="text-5xl font-bold text-white"
    style="text-shadow: 0 0 40px rgba(var(--brand-rgb), 0.4), 0 0 80px rgba(var(--brand-rgb), 0.2);">
  Launch day
</h1>
```

### Typewriter / Fade-Up Headline

Individual words or lines fade up with stagger.

```html
<h1 class="text-5xl font-bold">
  <span class="inline-block fade-up" style="--i:0">Build</span>
  <span class="inline-block fade-up" style="--i:1">something</span>
  <span class="inline-block fade-up" style="--i:2">beautiful.</span>
</h1>
```

---

## Font Pairings

Proven heading + body combinations. Load via Google Fonts `<link>`.

| Heading | Body | Mood |
|---|---|---|
| Inter (700) | Inter (400) | Clean tech / SaaS |
| Space Grotesk (700) | Inter (400) | Modern developer |
| Playfair Display (700) | Source Sans 3 (400) | Premium / editorial |
| Sora (700) | DM Sans (400) | Friendly SaaS |
| Bricolage Grotesque (800) | Inter (400) | Bold startup |
| Cabinet Grotesk (800) | Satoshi (400) | Ultra-modern |

Heading rules:
- `letter-spacing: -0.03em` on headings above 2rem
- `line-height: 1.1` on hero headlines
- `line-height: 1.7` on body text

---

## Color System

Never use raw Tailwind palette colors. Build a custom scale:

1. Pick a brand hue (e.g., purple at HSL 270)
2. Generate 50-950 scale with consistent saturation curve
3. Add to Tailwind config:

```html
<script>
tailwind.config = {
  theme: {
    extend: {
      colors: {
        brand: {
          50:  'hsl(270, 80%, 97%)',
          100: 'hsl(270, 75%, 93%)',
          200: 'hsl(270, 70%, 85%)',
          300: 'hsl(270, 65%, 72%)',
          400: 'hsl(270, 60%, 60%)',
          500: 'hsl(270, 55%, 50%)',
          600: 'hsl(270, 55%, 42%)',
          700: 'hsl(270, 55%, 34%)',
          800: 'hsl(270, 50%, 26%)',
          900: 'hsl(270, 45%, 18%)',
          950: 'hsl(270, 40%, 10%)',
        }
      }
    }
  }
}
</script>
```

Accent color: pick complementary or analogous hue (brand +/- 30-60 degrees).

---

## Bento Grid Layouts

### 2x2 Asymmetric
```html
<div class="grid grid-cols-2 gap-4 max-w-5xl mx-auto">
  <div class="col-span-2 row-span-1 ...">Wide feature</div>
  <div class="col-span-1 row-span-2 ...">Tall feature</div>
  <div class="col-span-1 row-span-1 ...">Small feature</div>
  <div class="col-span-1 row-span-1 ...">Small feature</div>
</div>
```

### 3-Column with Tall Card
```html
<div class="grid grid-cols-3 grid-rows-2 gap-4 max-w-6xl mx-auto">
  <div class="col-span-1 row-span-2 ...">Tall feature</div>
  <div class="col-span-2 row-span-1 ...">Wide feature</div>
  <div class="col-span-1 row-span-1 ...">Small</div>
  <div class="col-span-1 row-span-1 ...">Small</div>
</div>
```

Always make bento grids collapse to single column on mobile: `grid-cols-1 md:grid-cols-2 lg:grid-cols-3`.
