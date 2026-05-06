# Puppeteer Pinterest Pin Generator — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Generate 50 June Pinterest pin images for shecookssheeats.co.uk using Puppeteer + real WP food photos — zero Gemini API cost.

**Architecture:** Node.js script fetches food photos from existing WP media library, injects them into HTML/CSS pin templates, screenshots with Puppeteer at 2000×3000px, uploads to WP, and saves a queue JSON compatible with the existing daily scheduler.

**Tech Stack:** Node.js 18+, Puppeteer (headless Chrome), WP REST API

---

## File Map

| File | Role |
|------|------|
| `C:\Users\sunny\AppData\Local\Temp\scse-pins\package.json` | npm project for puppeteer |
| `C:\Users\sunny\AppData\Local\Temp\scse-pins\scse_june_prep.js` | Main script |
| `C:\Users\sunny\Downloads\scse_june_queue.json` | Output queue (matches May format) |

**WP credentials:**
- Host: `shecookssheeats.co.uk`
- User: `sunny` | App password: `yuFd G7FS BarV AvUS W6ss 8KrQ`
- Auth header: `Basic ` + `Buffer.from('sunny:yuFd G7FS BarV AvUS W6ss 8KrQ').toString('base64')`

---

## Task 1: Project setup

**Files:**
- Create: `C:\Users\sunny\AppData\Local\Temp\scse-pins\package.json`

- [ ] **Step 1: Create project directory and package.json**

```bash
mkdir "C:\Users\sunny\AppData\Local\Temp\scse-pins"
cd "C:\Users\sunny\AppData\Local\Temp\scse-pins"
```

Create `package.json`:
```json
{
  "name": "scse-pins",
  "version": "1.0.0",
  "type": "module",
  "dependencies": {
    "puppeteer": "^22.0.0"
  }
}
```

- [ ] **Step 2: Install puppeteer**

```bash
cd "C:\Users\sunny\AppData\Local\Temp\scse-pins"
npm install
```

Expected: `node_modules/puppeteer` directory created. Puppeteer downloads its own Chromium (~170MB).

- [ ] **Step 3: Verify puppeteer works**

Create `test-puppeteer.js` in the same dir:
```javascript
import puppeteer from 'puppeteer';
const browser = await puppeteer.launch({ headless: 'new' });
const page = await browser.newPage();
await page.setContent('<h1 style="color:red">OK</h1>');
const buf = await page.screenshot({ type: 'png' });
await browser.close();
import { writeFileSync } from 'fs';
writeFileSync('C:/Users/sunny/Downloads/test-pin.png', buf);
console.log('Puppeteer OK — check Downloads/test-pin.png');
```

Run: `node test-puppeteer.js`
Expected: `Puppeteer OK` logged, `test-pin.png` visible in Downloads with red "OK" text.

---

## Task 2: WP image fetcher

**Files:**
- Create: `C:\Users\sunny\AppData\Local\Temp\scse-pins\scse_june_prep.js` (initial)

- [ ] **Step 1: Create the script file with fetchPostImages**

`C:\Users\sunny\AppData\Local\Temp\scse-pins\scse_june_prep.js`:
```javascript
import puppeteer from 'puppeteer';
import { writeFileSync, readFileSync, existsSync } from 'fs';

const WP_HOST = 'https://shecookssheeats.co.uk';
const WP_AUTH = 'Basic ' + Buffer.from('sunny:yuFd G7FS BarV AvUS W6ss 8KrQ').toString('base64');
const QUEUE_PATH = 'C:/Users/sunny/Downloads/scse_june_queue.json';

async function fetchPostImages(slug) {
  // 1. Get post by slug
  const postRes = await fetch(
    `${WP_HOST}/wp-json/wp/v2/posts?slug=${slug}&context=edit`,
    { headers: { Authorization: WP_AUTH } }
  );
  const posts = await postRes.json();
  if (!posts.length) throw new Error(`Post not found: ${slug}`);
  const post = posts[0];

  const images = [];

  // 2. Featured image
  if (post.featured_media) {
    const mediaRes = await fetch(
      `${WP_HOST}/wp-json/wp/v2/media/${post.featured_media}`,
      { headers: { Authorization: WP_AUTH } }
    );
    const media = await mediaRes.json();
    if (media.source_url) images.push(media.source_url);
  }

  // 3. Content images — parse <img src="..."> from rendered content
  const content = post.content?.rendered || '';
  const imgMatches = [...content.matchAll(/<img[^>]+src="([^"]+\.(jpg|jpeg|png|webp)[^"]*)"/gi)];
  for (const m of imgMatches) {
    const url = m[1].split('?')[0]; // strip query params
    if (!images.includes(url)) images.push(url);
    if (images.length >= 6) break;
  }

  // 4. Fallback: pull recent media if we don't have enough images
  if (images.length < 3) {
    const fallbackRes = await fetch(
      `${WP_HOST}/wp-json/wp/v2/media?per_page=20&mime_type=image/jpeg&orderby=date&order=desc`,
      { headers: { Authorization: WP_AUTH } }
    );
    const fallbackMedia = await fallbackRes.json();
    for (const m of fallbackMedia) {
      if (!images.includes(m.source_url)) images.push(m.source_url);
      if (images.length >= 6) break;
    }
  }

  return images.slice(0, 6);
}
```

- [ ] **Step 2: Test fetchPostImages manually**

Add this at the bottom of the file temporarily:
```javascript
// TEMP TEST — remove after verifying
const imgs = await fetchPostImages('low-syn-drinks');
console.log('Images found:', imgs.length);
imgs.forEach((u, i) => console.log(i, u));
```

Run: `node scse_june_prep.js`
Expected: 3–6 image URLs logged, all starting with `https://shecookssheeats.co.uk/wp-content/uploads/`.

Remove the temp test lines after verifying.

---

## Task 3: HTML templates

**Files:**
- Modify: `C:\Users\sunny\AppData\Local\Temp\scse-pins\scse_june_prep.js`

The three layout functions. Each returns a complete HTML string at 1000×1500px.
`deviceScaleFactor: 2` in Puppeteer will double this to 2000×3000px output.

Heights per layout A: header=330px, grid=795px, footer=375px (total=1500px)
Heights per layout B: header=300px, hero=675px, row=225px, footer=300px (total=1500px)
Heights per layout C: header=270px, cards=930px (310px×3), footer=300px (total=1500px)

- [ ] **Step 1: Add PALETTES constant and buildHtml dispatcher**

Add after `WP_AUTH` line:
```javascript
const PALETTES = {
  terracotta: { bg: '#C67B5C', text: '#FFFFFF', accent: '#473f99' },
  sage:        { bg: '#8B9A6B', text: '#FFFFFF', accent: '#473f99' },
  pink:        { bg: '#D4878F', text: '#FFFFFF', accent: '#473f99' },
  purple:      { bg: '#473f99', text: '#FFFFFF', accent: '#C67B5C' },
  mustard:     { bg: '#D4A843', text: '#2D2D2D', accent: '#473f99' },
  red:         { bg: '#B84233', text: '#FFFFFF', accent: '#D4A843' },
};

const GOOGLE_FONTS = `<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Dancing+Script:wght@700&family=Inter:wght@400;700&display=swap" rel="stylesheet">`;

function buildHtml(layout, { images, number, headline, subtitle, palette }) {
  const p = PALETTES[palette] || PALETTES.terracotta;
  if (layout === 'A') return layoutA(images, number, headline, subtitle, p);
  if (layout === 'B') return layoutB(images, headline, subtitle, p);
  if (layout === 'C') return layoutC(headline, subtitle, p);
  throw new Error(`Unknown layout: ${layout}`);
}
```

- [ ] **Step 2: Add layoutA (Collage Grid)**

```javascript
function layoutA(images, number, headline, subtitle, p) {
  // Pad to 6 images
  while (images.length < 6) images.push(images[images.length - 1] || '');
  const imgs = images.slice(0, 6).map(u => `<img src="${u}" alt="">`).join('');
  return `<!DOCTYPE html><html><head><meta charset="utf-8">${GOOGLE_FONTS}
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{width:1000px;height:1500px;overflow:hidden}
.pin{width:1000px;height:1500px;display:flex;flex-direction:column;outline:3px solid #473f99;outline-offset:-3px}
.header{background:${p.bg};height:330px;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:16px;gap:4px;border-bottom:3px solid #473f99}
.number{font-family:'Bebas Neue',sans-serif;font-size:180px;color:${p.text};line-height:0.9;letter-spacing:-2px}
.headline{font-family:'Bebas Neue',sans-serif;font-size:56px;color:${p.text};letter-spacing:3px;text-align:center}
.grid{flex:1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr 1fr;gap:4px;background:#fff}
.grid img{width:100%;height:100%;object-fit:cover;display:block}
.footer{background:${p.bg};height:375px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:16px;padding:20px;border-top:3px solid #473f99}
.subtitle{font-family:'Dancing Script',cursive;font-size:38px;color:#FFF8F0;text-align:center}
.cta{background:${p.accent};color:#fff;padding:10px 36px;border-radius:30px;font-family:'Inter',sans-serif;font-size:17px;font-weight:700;letter-spacing:2px}
.url{font-family:'Inter',sans-serif;color:rgba(255,255,255,0.8);font-size:18px;letter-spacing:1px}
</style></head><body>
<div class="pin">
  <div class="header">
    <div class="number">${number}</div>
    <div class="headline">${headline}</div>
  </div>
  <div class="grid">${imgs}</div>
  <div class="footer">
    <div class="subtitle">${subtitle}</div>
    <div class="cta">READ MORE</div>
    <div class="url">shecookssheeats.co.uk</div>
  </div>
</div>
</body></html>`;
}
```

- [ ] **Step 3: Add layoutB (Hero + Row)**

```javascript
function layoutB(images, headline, subtitle, p) {
  while (images.length < 3) images.push(images[images.length - 1] || '');
  return `<!DOCTYPE html><html><head><meta charset="utf-8">${GOOGLE_FONTS}
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{width:1000px;height:1500px;overflow:hidden}
.pin{width:1000px;height:1500px;display:flex;flex-direction:column;outline:3px solid #473f99;outline-offset:-3px}
.header{background:${p.bg};height:300px;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:16px;gap:8px;border-bottom:3px solid #473f99}
.headline{font-family:'Bebas Neue',sans-serif;font-size:80px;color:${p.text};letter-spacing:3px;text-align:center;line-height:0.95}
.hero{height:675px;overflow:hidden}
.hero img{width:100%;height:100%;object-fit:cover;display:block}
.row{height:225px;display:grid;grid-template-columns:1fr 1fr;gap:4px;background:#fff;border-top:4px solid #fff}
.row img{width:100%;height:100%;object-fit:cover;display:block}
.footer{background:${p.bg};height:300px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:16px;padding:20px;border-top:3px solid #473f99}
.subtitle{font-family:'Dancing Script',cursive;font-size:38px;color:#FFF8F0;text-align:center}
.cta{background:${p.accent};color:#fff;padding:10px 36px;border-radius:30px;font-family:'Inter',sans-serif;font-size:17px;font-weight:700;letter-spacing:2px}
.url{font-family:'Inter',sans-serif;color:rgba(255,255,255,0.8);font-size:18px;letter-spacing:1px}
</style></head><body>
<div class="pin">
  <div class="header"><div class="headline">${headline}</div></div>
  <div class="hero"><img src="${images[0]}" alt=""></div>
  <div class="row"><img src="${images[1]}" alt=""><img src="${images[2]}" alt=""></div>
  <div class="footer">
    <div class="subtitle">${subtitle}</div>
    <div class="cta">READ MORE</div>
    <div class="url">shecookssheeats.co.uk</div>
  </div>
</div>
</body></html>`;
}
```

- [ ] **Step 4: Add layoutC (Guide / Tips)**

```javascript
function layoutC(headline, subtitle, p) {
  const tips = [
    { icon: '✅', title: 'Free Foods', text: 'Eat without counting — lean meat, fish, eggs, veg, fruit and potatoes are all free' },
    { icon: '📊', title: 'Syns (Swips)', text: 'Your daily allowance of 5–15 for treats, sauces and extras that aren\'t free foods' },
    { icon: '🥛', title: 'Healthy Extras', text: 'Daily portions of calcium (HEA) and fibre (HEB) — milk, cheese, wholegrain bread, nuts' },
  ];
  const cards = tips.map((t, i) => `
    <div class="card" style="background:${i % 2 === 0 ? '#fff' : '#FFF8F0'}">
      <div class="card-icon">${t.icon}</div>
      <div class="card-body">
        <div class="card-title">${t.title}</div>
        <div class="card-text">${t.text}</div>
      </div>
    </div>`).join('');
  return `<!DOCTYPE html><html><head><meta charset="utf-8">${GOOGLE_FONTS}
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{width:1000px;height:1500px;overflow:hidden}
.pin{width:1000px;height:1500px;display:flex;flex-direction:column;outline:3px solid #473f99;outline-offset:-3px}
.header{background:${p.bg};height:270px;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:16px;gap:8px;border-bottom:3px solid #473f99}
.headline{font-family:'Bebas Neue',sans-serif;font-size:72px;color:${p.text};letter-spacing:3px;text-align:center;line-height:0.95}
.subhead{font-family:'Dancing Script',cursive;font-size:34px;color:#FFF8F0}
.cards{flex:1;display:flex;flex-direction:column}
.card{flex:1;display:flex;align-items:center;padding:28px 40px;gap:28px;border-bottom:3px solid #eee}
.card-icon{font-size:64px;flex-shrink:0}
.card-title{font-family:'Bebas Neue',sans-serif;font-size:44px;color:#2D2D2D;letter-spacing:1px;margin-bottom:8px}
.card-text{font-family:'Inter',sans-serif;font-size:22px;color:#555;line-height:1.4}
.footer{background:${p.bg};height:300px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:16px;padding:20px;border-top:3px solid #473f99}
.subtitle{font-family:'Dancing Script',cursive;font-size:38px;color:#FFF8F0;text-align:center}
.cta{background:${p.accent};color:#fff;padding:10px 36px;border-radius:30px;font-family:'Inter',sans-serif;font-size:17px;font-weight:700;letter-spacing:2px}
.url{font-family:'Inter',sans-serif;color:rgba(255,255,255,0.8);font-size:18px;letter-spacing:1px}
</style></head><body>
<div class="pin">
  <div class="header">
    <div class="headline">${headline}</div>
    <div class="subhead">${subtitle}</div>
  </div>
  <div class="cards">${cards}</div>
  <div class="footer">
    <div class="cta">READ MORE</div>
    <div class="url">shecookssheeats.co.uk</div>
  </div>
</div>
</body></html>`;
}
```

- [ ] **Step 5: Test all 3 layouts render correctly**

Add temporary test at bottom:
```javascript
// TEMP TEST
import puppeteer from 'puppeteer';
const browser = await puppeteer.launch({ headless: 'new' });
const page = await browser.newPage();
await page.setViewport({ width: 1000, height: 1500, deviceScaleFactor: 2 });

const testImgs = [
  'https://shecookssheeats.co.uk/wp-content/uploads/2023/01/low-syn-drinks.jpg',
  'https://shecookssheeats.co.uk/wp-content/uploads/2023/01/low-syn-drinks.jpg',
  'https://shecookssheeats.co.uk/wp-content/uploads/2023/01/low-syn-drinks.jpg',
];

const htmlA = buildHtml('A', { images: testImgs, number: '15', headline: 'SYN FREE DINNERS', subtitle: 'Quick Family Meals', palette: 'terracotta' });
await page.setContent(htmlA, { waitUntil: 'networkidle0' });
const bufA = await page.screenshot({ type: 'png' });
writeFileSync('C:/Users/sunny/Downloads/test-layout-a.png', bufA);

const htmlB = buildHtml('B', { images: testImgs, headline: 'SYN FREE\nCHICKEN', subtitle: 'Ready in 20 Minutes', palette: 'sage' });
await page.setContent(htmlB, { waitUntil: 'networkidle0' });
const bufB = await page.screenshot({ type: 'png' });
writeFileSync('C:/Users/sunny/Downloads/test-layout-b.png', bufB);

const htmlC = buildHtml('C', { images: [], headline: 'HOW SW WORKS', subtitle: 'The Complete Guide', palette: 'purple' });
await page.setContent(htmlC, { waitUntil: 'networkidle0' });
const bufC = await page.screenshot({ type: 'png' });
writeFileSync('C:/Users/sunny/Downloads/test-layout-c.png', bufC);

await browser.close();
console.log('Layout tests done — check Downloads/test-layout-*.png');
```

Run: `node scse_june_prep.js`
Expected: 3 PNG files in Downloads, each 2000×3000px. Open each and verify layout looks correct — brand purple border, correct fonts, correct colour blocks.

Remove test lines after verifying.

---

## Task 4: Puppeteer screenshot function

**Files:**
- Modify: `C:\Users\sunny\AppData\Local\Temp\scse-pins\scse_june_prep.js`

- [ ] **Step 1: Add screenshotPin function**

```javascript
async function screenshotPin(html) {
  const browser = await puppeteer.launch({
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });
  try {
    const page = await browser.newPage();
    await page.setViewport({ width: 1000, height: 1500, deviceScaleFactor: 2 });
    await page.setContent(html, { waitUntil: 'networkidle0', timeout: 30000 });
    const buffer = await page.screenshot({
      type: 'png',
      clip: { x: 0, y: 0, width: 1000, height: 1500 }
    });
    return buffer;
  } finally {
    await browser.close();
  }
}
```

Note: `clip` is in CSS pixels; with `deviceScaleFactor: 2` the output PNG will be 2000×3000px.

---

## Task 5: WordPress upload function

**Files:**
- Modify: `C:\Users\sunny\AppData\Local\Temp\scse-pins\scse_june_prep.js`

- [ ] **Step 1: Add uploadToWP function**

```javascript
async function uploadToWP(buffer, filename) {
  const res = await fetch(`${WP_HOST}/wp-json/wp/v2/media`, {
    method: 'POST',
    headers: {
      Authorization: WP_AUTH,
      'Content-Disposition': `attachment; filename="${filename}"`,
      'Content-Type': 'image/png',
    },
    body: buffer,
  });
  if (!res.ok) {
    const err = await res.text();
    throw new Error(`WP upload failed ${res.status}: ${err}`);
  }
  const data = await res.json();
  return data.source_url;
}
```

- [ ] **Step 2: Test uploadToWP with a real PNG**

Add temporary test:
```javascript
// TEMP TEST — upload test-layout-a.png to WP
import { readFileSync } from 'fs';
const testBuf = readFileSync('C:/Users/sunny/Downloads/test-layout-a.png');
const url = await uploadToWP(testBuf, 'pin-june-test-001.png');
console.log('Uploaded to WP:', url);
```

Run: `node scse_june_prep.js`
Expected: URL like `https://shecookssheeats.co.uk/wp-content/uploads/2026/04/pin-june-test-001.png` logged.
Go to WP Admin → Media Library and verify the image appears there at correct dimensions.

Remove test lines after verifying.

---

## Task 6: Pin data — 50 June pins

**Files:**
- Modify: `C:\Users\sunny\AppData\Local\Temp\scse-pins\scse_june_prep.js`

- [ ] **Step 1: Add PIN_DATA array**

Add after the constants:
```javascript
const PIN_DATA = [
  // Layout A — Collage Grid (roundups with numbers)
  { slug: 'low-syn-drinks',               layout: 'A', palette: 'terracotta', number: '20+', headline: 'LOW SYN DRINKS',         subtitle: 'Alcohol, Hot & Soft Drinks',    board: '771523048604570705', title: '20+ Low Syn Drinks on Slimming World',               desc: 'Every drink counted — from wine to hot choc to fizzy drinks. Save this for your next shop! #SlimmingWorld #LowSyn #SWDrinks', link: 'https://shecookssheeats.co.uk/low-syn-drinks/' },
  { slug: 'syns-nuts',                    layout: 'A', palette: 'sage',       number: '10+', headline: 'NUTS ON SW',             subtitle: 'Syns Per Portion Listed',       board: '771523048604274536', title: 'Syns in Nuts on Slimming World',                     desc: 'Almonds, cashews, peanuts and walnuts — how many syns? All here! #SlimmingWorld #SynsInNuts', link: 'https://shecookssheeats.co.uk/syns-nuts/' },
  { slug: 'syns-rice-cakes',              layout: 'A', palette: 'mustard',    number: '8',   headline: 'RICE CAKE SYNS',          subtitle: 'Not Quite Free — Here\'s Why', board: '771523048604274536', title: 'Rice Cakes on Slimming World — Syn Values Listed',   desc: 'Are rice cakes free on Slimming World? Not quite! Find out how many syns. #SlimmingWorld #RiceCakes', link: 'https://shecookssheeats.co.uk/syns-rice-cakes/' },
  { slug: 'best-slimming-world-recipes',  layout: 'A', palette: 'terracotta', number: '50+', headline: 'SW RECIPES',             subtitle: 'Low-Syn Meals That Work',       board: '771523048604574770', title: '50+ Best Slimming World Recipes',                    desc: 'The best SW recipes all in one place — from fakeaways to freezer meals. Save this board! #SlimmingWorld #SWRecipes', link: 'https://shecookssheeats.co.uk/best-slimming-world-recipes/' },
  { slug: 'yogurts-syn',                  layout: 'A', palette: 'pink',       number: '16',  headline: 'YOGURT SYNS',             subtitle: 'Which Brands Are Actually Free?', board: '771523048604274536', title: '16 Yogurts Ranked by Syns on Slimming World',       desc: 'Müller Light, Fage, Activia — which are syn free? Full list here. #SlimmingWorld #SynFreeYogurt', link: 'https://shecookssheeats.co.uk/yogurts-syn/' },
  { slug: 'syns-actimel',                 layout: 'A', palette: 'sage',       number: '6',   headline: 'ACTIMEL SYNS',            subtitle: 'Every Variety Listed',          board: '771523048604274536', title: 'Syns in Actimel on Slimming World',                  desc: 'Original, Fat Free, Kids — how many syns in each Actimel variety? #SlimmingWorld #Actimel', link: 'https://shecookssheeats.co.uk/syns-actimel/' },
  { slug: 'syns-fage-total-0',            layout: 'A', palette: 'purple',     number: '0',   headline: 'FAGE TOTAL 0%',           subtitle: 'Plain Is Free — Splits Are Not', board: '771523048604274536', title: 'Fage Total 0% Syns on Slimming World',               desc: 'Plain Fage is free! But the split pots have syns. Here\'s the full breakdown. #SlimmingWorld #FageTotal', link: 'https://shecookssheeats.co.uk/syns-fage-total-0/' },
  { slug: 'lowest-syn-bread',             layout: 'A', palette: 'mustard',    number: '1',   headline: 'LOWEST SYN BREAD',        subtitle: 'Some Slices Are Just 1 Syn',    board: '771523048604274536', title: 'Lowest Syn Bread on Slimming World',                 desc: 'Which bread has the fewest syns? Some slices are just 1 syn! Full list here. #SlimmingWorld #SWBread', link: 'https://shecookssheeats.co.uk/lowest-syn-bread/' },
  { slug: 'slimming-world-free-foods',    layout: 'A', palette: 'terracotta', number: '100+', headline: 'FREE FOODS LIST',         subtitle: 'Eat Without Counting',          board: '771523048604561727', title: '100+ Slimming World Free Foods 2026',                desc: 'Every food you can eat without counting syns — the complete Free Food list. #SlimmingWorld #FreeFoods', link: 'https://shecookssheeats.co.uk/slimming-world-free-foods/' },
  { slug: 'syns-aldi-yogurts',            layout: 'A', palette: 'sage',       number: '7',   headline: 'ALDI YOGURT SYNS',        subtitle: 'Which Brooklea Are Syn Free?',  board: '771523048604274536', title: 'Aldi Yogurt Syns on Slimming World',                 desc: 'Brooklea Light, Skyr, Greek Style — full syn breakdown for every Aldi yogurt. #SlimmingWorld #AldiFoods', link: 'https://shecookssheeats.co.uk/syns-aldi-yogurts/' },

  // Layout B — Hero + Row (single recipe features)
  { slug: 'lowest-calorie-chocolate-uk',  layout: 'B', palette: 'pink',       number: '',    headline: 'LOWEST CALORIE\nCHOCOLATE UK', subtitle: 'Treat Yourself Without the Guilt', board: '771523048604561724', title: 'Lowest Calorie Chocolate UK 2026',              desc: 'Which chocolate bar has the fewest calories? Dark, milk, white — all compared. #LowCalorie #HealthyTreats', link: 'https://shecookssheeats.co.uk/lowest-calorie-chocolate-uk/' },
  { slug: 'calories-in-banana-uk',        layout: 'B', palette: 'mustard',    number: '',    headline: 'CALORIES IN\nA BANANA',   subtitle: 'Small vs Medium vs Large',      board: '771523048604561727', title: 'Calories in a Banana — Small, Medium and Large', desc: 'How many calories in a banana? It depends on the size. All the details here! #CaloriesInFruit #HealthyEating', link: 'https://shecookssheeats.co.uk/calories-in-banana-uk/' },
  { slug: 'lowest-calorie-crisps-uk',     layout: 'B', palette: 'terracotta', number: '',    headline: 'LOWEST CALORIE\nCRISPS UK', subtitle: 'Under 100 Calories a Bag',   board: '771523048604561724', title: 'Lowest Calorie Crisps UK — Every Brand Compared',  desc: 'Quavers, Skips, Popchips — which crisps are lowest in calories? Full list! #LowCalorieCrisps #HealthySnacks', link: 'https://shecookssheeats.co.uk/lowest-calorie-crisps-uk/' },
  { slug: 'is-porridge-good-for-weight-loss', layout: 'B', palette: 'sage',   number: '',    headline: 'PORRIDGE FOR\nWEIGHT LOSS', subtitle: 'The Truth About Oats',       board: '771523048604569270', title: 'Is Porridge Good for Weight Loss?',              desc: 'Porridge is filling and low calorie — but is it good for weight loss? Here\'s what the research says. #Porridge #WeightLoss', link: 'https://shecookssheeats.co.uk/is-porridge-good-for-weight-loss/' },
  { slug: 'calories-in-eggs-uk',          layout: 'B', palette: 'mustard',    number: '',    headline: 'CALORIES IN\nAN EGG',     subtitle: 'Boiled, Fried, Scrambled',     board: '771523048604561727', title: 'Calories in an Egg — Every Way It\'s Cooked',     desc: 'How many calories in an egg? Boiled, fried, poached or scrambled — all here! #CaloriesInEggs #HealthyProtein', link: 'https://shecookssheeats.co.uk/calories-in-eggs-uk/' },
  { slug: 'calories-in-chicken-uk',       layout: 'B', palette: 'terracotta', number: '',    headline: 'CALORIES IN\nCHICKEN',    subtitle: 'Breast, Thigh & More',         board: '771523048603322381', title: 'Calories in Chicken — Every Cut Compared',        desc: 'Chicken breast, thigh, drumstick — how many calories in each? Full breakdown here! #CaloriesInChicken #HighProtein', link: 'https://shecookssheeats.co.uk/calories-in-chicken-uk/' },
  { slug: 'lowest-calorie-ice-lollies-uk', layout: 'B', palette: 'pink',      number: '',    headline: 'LOWEST CALORIE\nICE LOLLIES', subtitle: 'Summer Treats Under 50 Cal', board: '771523048604561724', title: 'Lowest Calorie Ice Lollies UK 2026',            desc: 'The best low calorie ice lollies to keep in the freezer this summer! #LowCalorie #IceLollies #SummerTreats', link: 'https://shecookssheeats.co.uk/lowest-calorie-ice-lollies-uk/' },
  { slug: 'healthiest-sausages-uk',       layout: 'B', palette: 'red',        number: '',    headline: 'HEALTHIEST\nSAUSAGES UK', subtitle: 'Which Brand Wins?',            board: '771523048604574770', title: 'Healthiest Sausages UK — Every Brand Ranked',     desc: 'Richmond, Heck, Linda McCartney — which sausages are actually healthiest? Full ranking! #HealthySausages #HealthyEating', link: 'https://shecookssheeats.co.uk/healthiest-sausages-uk/' },
  { slug: 'lowest-calorie-ready-meals-uk', layout: 'B', palette: 'sage',      number: '',    headline: 'LOWEST CALORIE\nREADY MEALS', subtitle: 'Under 400 Calories',      board: '771523048604569270', title: 'Lowest Calorie Ready Meals UK 2026',            desc: 'The best low calorie ready meals from M&S, Waitrose, Tesco and more! #LowCalorieMeals #ReadyMeals', link: 'https://shecookssheeats.co.uk/lowest-calorie-ready-meals-uk/' },
  { slug: 'lowest-calorie-takeaway-uk',   layout: 'B', palette: 'red',        number: '',    headline: 'LOWEST CALORIE\nTAKEAWAY', subtitle: 'Every Chain Counted',        board: '771523048604574770', title: 'Lowest Calorie Takeaway UK — All Chains Compared', desc: 'Ordering a takeaway? Here are the lowest calorie options from every major chain. #HealthyTakeaway #LowCalorie', link: 'https://shecookssheeats.co.uk/lowest-calorie-takeaway-uk/' },

  // Layout A — more roundups
  { slug: 'syns-rice-krispies',           layout: 'A', palette: 'mustard',    number: '6.5', headline: 'RICE KRISPIES SYNS',      subtitle: 'Cereal, Squares & Treats',     board: '771523048604274536', title: 'Syns in Rice Krispies on Slimming World',            desc: 'How many syns in Rice Krispies, Rice Krispie Squares and Treats? All here! #SlimmingWorld #RiceKrispies', link: 'https://shecookssheeats.co.uk/syns-rice-krispies/' },
  { slug: 'cuppa-soups-syn-free',         layout: 'A', palette: 'terracotta', number: '1.5', headline: 'CUP A SOUP SYNS',         subtitle: 'Are Any Syn Free?',            board: '771523048604274536', title: 'Syns in Cup a Soup — All Flavours Listed',           desc: 'Are any Cup a Soup flavours syn free? Here\'s the full breakdown! #SlimmingWorld #CupaSoup', link: 'https://shecookssheeats.co.uk/cuppa-soups-syn-free/' },
  { slug: 'syns-lucozade-original',       layout: 'A', palette: 'mustard',    number: '8.5', headline: 'LUCOZADE SYNS',           subtitle: 'Original, Zero & Sport',       board: '771523048604570705', title: 'Syns in Lucozade on Slimming World',                 desc: 'How many syns in Lucozade Original, Zero and Sport? All varieties counted. #SlimmingWorld #Lucozade', link: 'https://shecookssheeats.co.uk/syns-lucozade-original/' },
  { slug: 'syns-kefir-milk',              layout: 'A', palette: 'sage',       number: '4',   headline: 'IS KEFIR FREE?',          subtitle: 'Syn Values Per Brand',         board: '771523048604274536', title: 'Kefir on Slimming World — Is It Free?',              desc: 'Is kefir syn free on Slimming World? The answer depends on the brand. #SlimmingWorld #Kefir #GutHealth', link: 'https://shecookssheeats.co.uk/syns-kefir-milk/' },
  { slug: 'how-does-slimming-world-work', layout: 'C', palette: 'purple',     number: '',    headline: 'HOW SW WORKS',            subtitle: 'Free Foods, Syns & HE Explained', board: '771523048604561727', title: 'How Does Slimming World Work? Full Explainer 2026', desc: 'Free Foods, Syns, Healthy Extras — everything explained in plain English. Perfect for beginners! #SlimmingWorld #SWBeginners', link: 'https://shecookssheeats.co.uk/how-does-slimming-world-work/' },
  { slug: 'slimming-world-7-day-kick-start-menu', layout: 'A', palette: 'terracotta', number: '7', headline: 'DAY KICK START',  subtitle: 'A Full Week of SW Meals',      board: '771523048604574770', title: 'Slimming World 7-Day Kick Start Menu',               desc: 'A full week of Slimming World meals and snacks to get you started! #SlimmingWorld #MealPlan #SWKickStart', link: 'https://shecookssheeats.co.uk/slimming-world-7-day-kick-start-menu/' },

  // More Layout B — single topics
  { slug: 'calories-in-milk-uk',          layout: 'B', palette: 'mustard',    number: '',    headline: 'CALORIES IN\nMILK',       subtitle: 'Skimmed vs Semi vs Full Fat',  board: '771523048604561727', title: 'Calories in Milk — Skimmed, Semi and Full Fat',   desc: 'How many calories in a glass of milk? Skimmed, semi-skimmed and full fat compared. #CaloriesInMilk #HealthyDairy', link: 'https://shecookssheeats.co.uk/calories-in-milk-uk/' },
  { slug: 'calories-in-nuts-uk',          layout: 'B', palette: 'sage',       number: '',    headline: 'CALORIES IN\nNUTS',       subtitle: 'Per 30g Serving, All Types',   board: '771523048604561727', title: 'Calories in Nuts — Almonds, Cashews, Walnuts & More', desc: 'How many calories in a handful of nuts? All types compared per 30g serving! #CaloriesInNuts #HealthyFats', link: 'https://shecookssheeats.co.uk/calories-in-nuts-uk/' },
  { slug: 'calories-in-strawberries-uk',  layout: 'B', palette: 'pink',       number: '',    headline: 'CALORIES IN\nSTRAWBERRIES', subtitle: 'Low Cal Summer Fruit',      board: '771523048604561727', title: 'Calories in Strawberries — Full Breakdown',       desc: 'Strawberries are incredibly low in calories! Here\'s the full breakdown by portion. #CaloriesInFruit #StrawberrySeason', link: 'https://shecookssheeats.co.uk/calories-in-strawberries-uk/' },
  { slug: 'calories-in-grapes-uk',        layout: 'B', palette: 'purple',     number: '',    headline: 'CALORIES IN\nGRAPES',     subtitle: 'Red, Green & Seedless',        board: '771523048604561727', title: 'Calories in Grapes — Red vs Green',               desc: 'How many calories in grapes? Red, green and seedless — all compared by the handful and 100g. #CaloriesInGrapes', link: 'https://shecookssheeats.co.uk/calories-in-grapes-uk/' },
  { slug: 'calories-in-blueberries-uk',   layout: 'B', palette: 'purple',     number: '',    headline: 'CALORIES IN\nBLUEBERRIES', subtitle: 'Superfood, Low Calorie',     board: '771523048604561727', title: 'Calories in Blueberries — Superfood Stats',       desc: 'Blueberries are a superfood AND low in calories. Here\'s the full calorie breakdown! #Blueberries #SuperfoodSEO', link: 'https://shecookssheeats.co.uk/calories-in-blueberries-uk/' },

  // More Layout A — food roundups
  { slug: 'lowest-calorie-cereals-uk',    layout: 'A', palette: 'mustard',    number: '10',  headline: 'LOWEST CAL CEREALS',      subtitle: 'UK Brands Compared 2026',      board: '771523048604564585', title: '10 Lowest Calorie Cereals UK 2026',                  desc: 'The lowest calorie cereals in the UK — from Weetabix to Special K. Full list! #LowCalorieCereals #HealthyBreakfast', link: 'https://shecookssheeats.co.uk/low-calorie-cereals-uk/' },
  { slug: 'lowest-calorie-biscuits-uk',   layout: 'A', palette: 'terracotta', number: '10',  headline: 'LOWEST CAL BISCUITS',      subtitle: 'Under 50 Calories Each',       board: '771523048604561724', title: '10 Lowest Calorie Biscuits UK',                      desc: 'Which biscuits are lowest in calories? Rich Tea, Digestives, Jaffa Cakes — all compared! #LowCalorieBiscuits', link: 'https://shecookssheeats.co.uk/lowest-calorie-biscuits-uk/' },
  { slug: 'lowest-calorie-pasta-uk',      layout: 'A', palette: 'sage',       number: '5',   headline: 'LOWEST CAL PASTA',        subtitle: 'Per 100g, Cooked & Dry',       board: '771523048604574770', title: 'Lowest Calorie Pasta UK — Compared by Brand',        desc: 'Regular, wholewheat, protein, chickpea — which pasta has fewest calories? Full comparison! #LowCaloriePasta', link: 'https://shecookssheeats.co.uk/lowest-calorie-pasta-uk/' },
  { slug: 'lowest-calorie-pizza-uk',      layout: 'A', palette: 'red',        number: '8',   headline: 'LOWEST CAL PIZZA',        subtitle: 'Every Major Brand Ranked',     board: '771523048604574770', title: 'Lowest Calorie Pizza UK — Every Brand Ranked',       desc: 'Chicago Town, Goodfella\'s, Dr. Oetker — which frozen pizza has fewest calories? Full ranking! #LowCaloriePizza', link: 'https://shecookssheeats.co.uk/lowest-calorie-pizza-uk/' },
  { slug: 'lowest-calorie-soup-uk',       layout: 'A', palette: 'terracotta', number: '5',   headline: 'LOWEST CAL SOUPS',        subtitle: 'Under 100 Calories a Tin',     board: '771523048604574770', title: 'Lowest Calorie Soups UK — Supermarket Brands Compared', desc: 'The lowest calorie soups from Heinz, Baxters and supermarket own brands. #LowCalorieSoup #HealthyLunch', link: 'https://shecookssheeats.co.uk/lowest-calorie-soup-uk/' },
  { slug: 'lowest-calorie-alcoholic-drinks-uk', layout: 'A', palette: 'purple', number: '12', headline: 'LOWEST CAL ALCOHOL',    subtitle: 'What to Order on a Night Out', board: '771523048604570705', title: '12 Lowest Calorie Alcoholic Drinks UK',              desc: 'Wine, beer, spirits — which has the fewest calories? Everything compared for your night out! #LowCalcAlcohol #SkinnyDrinks', link: 'https://shecookssheeats.co.uk/lowest-calorie-alcoholic-drinks-uk/' },

  // Layout C — Guide pins
  { slug: 'slimming-world-healthy-extra-b-list', layout: 'C', palette: 'sage', number: '', headline: 'HEALTHY EXTRA B', subtitle: 'Your Daily Fibre Allowance', board: '771523048604561727', title: 'Slimming World Healthy Extra B List 2026', desc: 'Everything on the Healthy Extra B list — bread, cereals, nuts and oats. Your daily fibre sorted! #SlimmingWorld #HealthyExtras', link: 'https://shecookssheeats.co.uk/slimming-world-healthy-extra-b-list/' },
  { slug: 'slimming-world-changes-2026',  layout: 'C', palette: 'purple',     number: '',    headline: 'SW CHANGES 2026',         subtitle: 'Syns Are Now Swips',           board: '771523048604561727', title: 'Slimming World Changes 2026 — What\'s New?',         desc: 'Syns are now called Swips, food lists have changed — here\'s everything that\'s different in 2026! #SlimmingWorld2026 #SWChanges', link: 'https://shecookssheeats.co.uk/slimming-world-changes-2026/' },

  // More Layout A
  { slug: 'syns-snack-jacks',             layout: 'A', palette: 'terracotta', number: '3.5', headline: 'SNACK A JACKS SYNS',      subtitle: 'Every Flavour From 3.5 Syns',  board: '771523048604274536', title: 'Syns in Snack a Jacks — All Flavours Listed',        desc: 'How many syns in Snack a Jacks? Every flavour from caramel to salt & vinegar! #SlimmingWorld #SnackAJacks', link: 'https://shecookssheeats.co.uk/syns-snack-jacks/' },
  { slug: 'best-greek-yogurt-uk',         layout: 'A', palette: 'sage',       number: '5',   headline: 'BEST GREEK YOGURTS UK',   subtitle: 'Ranked by Taste & Protein',    board: '771523048604561727', title: 'Best Greek Yogurts UK 2026 — Ranked',                desc: 'Fage, Chobani, Yeo Valley — which Greek yogurt is actually best? We rank them all! #GreekYogurt #HealthyDairy', link: 'https://shecookssheeats.co.uk/best-greek-yogurt-uk/' },
  { slug: 'healthiest-chinese-takeaway-dishes-uk', layout: 'A', palette: 'red', number: '8', headline: 'HEALTHIEST CHINESE',     subtitle: 'What to Order on SW',          board: '771523048604574770', title: '8 Healthiest Chinese Takeaway Dishes UK',            desc: 'Fancy a Chinese? Here are the healthiest options to order — and what to avoid! #HealthyChineseTakeaway #SWFakeaway', link: 'https://shecookssheeats.co.uk/healthiest-chinese-takeaway-dishes-uk/' },
  { slug: 'lowest-calorie-indian-takeaway', layout: 'A', palette: 'red',      number: '6',   headline: 'LOWEST CAL INDIAN',       subtitle: 'What to Order at the Curry House', board: '771523048604574770', title: 'Lowest Calorie Indian Takeaway Dishes UK',        desc: 'Tandoori vs curry vs rice — what\'s lowest in calories at an Indian takeaway? Full guide! #LowCalorieIndian', link: 'https://shecookssheeats.co.uk/lowest-calorie-indian-takeaway/' },

  // More Layout B
  { slug: 'calories-in-mango-uk',         layout: 'B', palette: 'mustard',    number: '',    headline: 'CALORIES IN\nA MANGO',    subtitle: 'Tropical & Low Calorie',       board: '771523048604561727', title: 'Calories in a Mango — Full Breakdown',            desc: 'A mango has more calories than you might think! Here\'s the full breakdown by size and variety. #CaloriesInMango #TropicalFruit', link: 'https://shecookssheeats.co.uk/calories-in-mango-uk/' },
  { slug: 'calories-in-watermelon-uk',    layout: 'B', palette: 'pink',       number: '',    headline: 'CALORIES IN\nWATERMELON', subtitle: 'Summer\'s Lowest Cal Fruit',   board: '771523048604561727', title: 'Calories in Watermelon — Summer\'s Best Snack',   desc: 'Watermelon is one of the lowest calorie fruits you can eat! Here\'s the full breakdown. #CaloriesInWatermelon #SummerFruit', link: 'https://shecookssheeats.co.uk/calories-in-watermelon-uk/' },
  { slug: 'calories-in-mince-uk',         layout: 'B', palette: 'terracotta', number: '',    headline: 'CALORIES IN\nMINCE',      subtitle: 'Beef, Pork, Turkey & More',    board: '771523048603322381', title: 'Calories in Mince — Beef, Turkey and Pork Compared', desc: 'Lean vs regular beef mince, turkey mince, pork mince — all compared per 100g cooked and raw! #CaloriesInMince #MealPrep', link: 'https://shecookssheeats.co.uk/calories-in-mince-uk/' },
  { slug: 'calories-in-salmon-uk',        layout: 'B', palette: 'sage',       number: '',    headline: 'CALORIES IN\nSALMON',     subtitle: 'Fillet, Smoked & Tinned',      board: '771523048604561727', title: 'Calories in Salmon — Every Form Compared',        desc: 'Fresh fillet, smoked, tinned — how many calories in each type of salmon? Full breakdown here! #CaloriesInSalmon #HealthyFish', link: 'https://shecookssheeats.co.uk/calories-in-salmon-uk/' },
  { slug: 'lowest-calorie-yoghurt-uk',    layout: 'A', palette: 'pink',       number: '8',   headline: 'LOWEST CAL YOGURTS',      subtitle: 'UK Brands, All Types',         board: '771523048604561727', title: '8 Lowest Calorie Yogurts UK 2026',                   desc: 'The lowest calorie yogurts in the UK supermarkets — Greek, fruit, natural and more! #LowCalorieYogurt #HealthyDairy', link: 'https://shecookssheeats.co.uk/lowest-calorie-yoghurt-uk/' },
  { slug: 'lowest-calorie-snacks-uk',     layout: 'A', palette: 'sage',       number: '15',  headline: 'LOWEST CAL SNACKS',       subtitle: 'Under 100 Calories Each',      board: '771523048604561724', title: '15 Lowest Calorie Snacks UK',                        desc: '15 snacks all under 100 calories — from rice cakes to fruit to protein bars! #LowCalorieSnacks #HealthySnacking', link: 'https://shecookssheeats.co.uk/lowest-calorie-snacks-uk/' },
  { slug: 'calories-in-potatoes-uk',      layout: 'B', palette: 'mustard',    number: '',    headline: 'CALORIES IN\nPOTATOES',   subtitle: 'Boiled, Baked & Mashed',       board: '771523048604561727', title: 'Calories in Potatoes — Every Way They\'re Cooked', desc: 'Boiled, baked, mashed, roasted — how many calories in potatoes cooked different ways? #CaloriesInPotatoes', link: 'https://shecookssheeats.co.uk/calories-in-potatoes-uk/' },
  { slug: 'lowest-calorie-bread-uk',      layout: 'A', palette: 'mustard',    number: '5',   headline: 'LOWEST CAL BREADS',       subtitle: 'Per Slice, UK Brands Ranked',  board: '771523048604564585', title: 'Lowest Calorie Bread UK — Every Brand Ranked',       desc: 'Hovis, Warburtons, Nimble — which bread has fewest calories per slice? Full list! #LowCalorieBread #HealthyBreakfast', link: 'https://shecookssheeats.co.uk/lowest-calorie-bread-uk/' },
  { slug: 'calories-in-rice-uk',          layout: 'B', palette: 'sage',       number: '',    headline: 'CALORIES IN\nRICE',       subtitle: 'White, Brown & Basmati',       board: '771523048604574770', title: 'Calories in Rice — White, Brown, Basmati Compared', desc: 'White rice vs brown rice vs basmati — which has the fewest calories? Full comparison per 100g! #CaloriesInRice #HealthyCarbs', link: 'https://shecookssheeats.co.uk/calories-in-rice-uk/' },
  { slug: 'lowest-calorie-breakfast-uk',  layout: 'A', palette: 'mustard',    number: '10',  headline: 'LOWEST CAL BREAKFASTS',   subtitle: 'Start the Day Right',          board: '771523048604564585', title: '10 Lowest Calorie Breakfasts UK',                    desc: 'Ten breakfast ideas all under 300 calories — quick, easy and filling! #LowCalorieBreakfast #HealthyStart', link: 'https://shecookssheeats.co.uk/lowest-calorie-breakfast-uk/' },
];
```

---

## Task 7: Main loop and queue generation

**Files:**
- Modify: `C:\Users\sunny\AppData\Local\Temp\scse-pins\scse_june_prep.js`

- [ ] **Step 1: Add main function**

```javascript
async function main() {
  const startFrom = parseInt(process.argv[2] || '0', 10);
  const queue = { pins: [] };

  // Load existing queue if resuming
  if (startFrom > 0 && existsSync(QUEUE_PATH)) {
    const existing = JSON.parse(readFileSync(QUEUE_PATH, 'utf8'));
    queue.pins = existing.pins;
  }

  for (let i = startFrom; i < PIN_DATA.length; i++) {
    const pin = PIN_DATA[i];
    const pinNum = String(i + 1).padStart(3, '0');
    console.log(`\n[${i + 1}/${PIN_DATA.length}] ${pin.slug} — Layout ${pin.layout}`);

    try {
      // 1. Fetch images
      console.log('  Fetching images...');
      const images = await fetchPostImages(pin.slug);
      console.log(`  Got ${images.length} images`);

      // 2. Build HTML
      const html = buildHtml(pin.layout, {
        images,
        number: pin.number || '',
        headline: pin.headline,
        subtitle: pin.subtitle,
        palette: pin.palette,
      });

      // 3. Screenshot
      console.log('  Screenshotting...');
      const buffer = await screenshotPin(html);

      // 4. Upload to WP
      const filename = `pin-june-${pinNum}.png`;
      console.log(`  Uploading ${filename}...`);
      const imageUrl = await uploadToWP(buffer, filename);
      console.log(`  ✓ ${imageUrl}`);

      // 5. Add to queue
      queue.pins.push({
        id: i + 1,
        status: 'pending',
        board_id: pin.board,
        title: pin.title,
        description: pin.desc,
        link: pin.link,
        image_url: imageUrl,
      });

      // Save queue after every pin (safe resume point)
      writeFileSync(QUEUE_PATH, JSON.stringify(queue, null, 2));

    } catch (err) {
      console.error(`  ✗ Error on pin ${i + 1}:`, err.message);
      console.error('  Skipping — resume with: node scse_june_prep.js', i);
      break;
    }
  }

  const done = queue.pins.filter(p => p.status === 'pending').length;
  console.log(`\nDone. ${done} pins in queue at ${QUEUE_PATH}`);
}

main().catch(console.error);
```

- [ ] **Step 2: Test single pin end-to-end**

Run with just pin 0 (uses index 0 = low-syn-drinks):
```bash
node scse_june_prep.js 0
```

Wait for it to complete (30–60 seconds for first pin — Puppeteer launch + font loading).

Expected output:
```
[1/50] low-syn-drinks — Layout A
  Fetching images...
  Got 4 images
  Screenshotting...
  Uploading pin-june-001.png...
  ✓ https://shecookssheeats.co.uk/wp-content/uploads/2026/04/pin-june-001.png

Done. 1 pins in queue at C:/Users/sunny/Downloads/scse_june_queue.json
```

Verify:
1. Open `Downloads/scse_june_queue.json` — should have 1 entry with `status: "pending"`
2. Go to WP Admin → Media Library → check `pin-june-001.png` exists at 2000×3000px
3. Open the image — verify it looks like a proper pin with food photos and correct layout

- [ ] **Step 3: Run all 50 pins**

```bash
cd "C:\Users\sunny\AppData\Local\Temp\scse-pins"
node scse_june_prep.js
```

If it errors partway through at pin N, resume with:
```bash
node scse_june_prep.js N
```

Expected: Takes ~30–60 min total (Puppeteer launch per pin). All 50 pins generated, uploaded, saved to queue.

---

## Task 8: Clone Windows Task Scheduler for June

- [ ] **Step 1: Copy May queue file path to June**

The existing `scse_pinterest_scheduler.js` reads from a queue JSON path. Check which path it uses:
```bash
grep -n "queue" "C:\Users\sunny\AppData\Local\Temp\scse_pinterest_scheduler.js"
```

Note the path. The June queue is at `C:\Users\sunny\Downloads\scse_june_queue.json`.

- [ ] **Step 2: Copy scheduler script for June**

```bash
cp "C:\Users\sunny\AppData\Local\Temp\scse_pinterest_scheduler.js" "C:\Users\sunny\AppData\Local\Temp\scse_june_scheduler.js"
```

Edit `scse_june_scheduler.js` — update the queue path constant to point to `scse_june_queue.json` instead of `scse_may_queue.json`.

- [ ] **Step 3: Copy batch file for June**

```bash
cp "C:\Users\sunny\AppData\Local\Temp\pinterest_daily.bat" "C:\Users\sunny\AppData\Local\Temp\pinterest_june_daily.bat"
```

Edit `pinterest_june_daily.bat` — update the script name to `scse_june_scheduler.js`.

- [ ] **Step 4: Create Windows Task for June**

Open Task Scheduler → Create Task:
- Name: `Pinterest_June_Pins`
- Trigger: Daily at 8:00 PM
- Action: Start a program → `C:\Users\sunny\AppData\Local\Temp\pinterest_june_daily.bat`
- Settings: Run whether user is logged in or not

Or via command line:
```bash
schtasks /create /tn "Pinterest_June_Pins" /tr "C:\Users\sunny\AppData\Local\Temp\pinterest_june_daily.bat" /sc daily /st 20:00 /f
```

- [ ] **Step 5: Test scheduler manually**

```bash
node "C:\Users\sunny\AppData\Local\Temp\scse_june_scheduler.js"
```

Expected: First pending pin in `scse_june_queue.json` posted to Pinterest (or logged if no MCP), status updated to `posted`.

---

## Self-Review Checklist

- [x] **fetchPostImages** — handles featured image, content images, fallback media
- [x] **3 layouts** — A (collage), B (hero+row), C (guide) — all with correct pixel heights totalling 1500px
- [x] **All 50 pins** defined with real slugs, board IDs, titles, descriptions
- [x] **Resume support** — `node scse_june_prep.js N` restarts from pin N+1, preserves queue
- [x] **WP upload** — uses `sunny` admin account which can upload media
- [x] **Queue format** — matches `scse_may_queue.json` structure exactly
- [x] **Scheduler** — clones May pattern, runs at 8pm daily
- [x] **No Gemini API** — zero image generation cost
