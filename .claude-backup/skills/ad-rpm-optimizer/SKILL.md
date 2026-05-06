---
name: ad-rpm-optimizer
description: Ad network RPM and revenue optimizer for display advertising across Ezoic, AdSense, and Mediavine. Use when optimising ad revenue on content sites, deciding which ad network to use, improving EPMV/RPM, planning ad layout changes, or deciding when to switch networks. Covers the 44-site SEO portfolio with Ezoic, AdSense, and Mediavine setups.
version: 1.0.0
user-invocable: true
allowed-tools: Read, Write, WebSearch, mcp__gsc__*
argument-hint: "[domain or 'portfolio'] [--network ezoic|adsense|mediavine|auto]"
---

# Ad RPM Optimizer — Display Revenue Maximiser

Audit ad setup, identify RPM improvement opportunities, and produce a prioritised action plan across your ad-monetised content sites.

## Arguments

- `target` (required): A domain (`techloved.com`) or `portfolio` to audit all ad sites
- `--network` (optional): Force analysis for a specific network. Default: auto-detect from site data
- `--output` (optional): Save path. Default: `G:\My Drive\SEO\reports\ad-rpm-{target}-{date}.md`

## Step 1: Load Site Data

Read from `G:\My Drive\_SHARED\memory\ezoic-portfolio.md` and `G:\My Drive\SEO\sites\{domain}\` for:
- Current monthly RPM / EPMV
- Traffic (pageviews/month)
- Current ad network
- Content category / niche
- Device split (mobile vs desktop)

If running `portfolio` mode, load all ad-monetised sites from ezoic-portfolio.md.

## Step 2: Network Threshold Assessment

For each site, run this decision tree:

```
Monthly sessions < 10,000  → AdSense (Ezoic not worth it below this)
Monthly sessions 10k–50k   → Ezoic (better RPM than AdSense, lower threshold)
Monthly sessions > 50,000  → Mediavine (premium CPMs, typically 2–3× Ezoic)
Monthly sessions > 100,000 → Mediavine or Raptive (both viable, compare)
```

Flag any sites near a threshold upgrade:
- "X is at 38k sessions — 12k away from Mediavine. At current growth rate, eligible in ~{N} months."

## Step 3: RPM Benchmarks by Niche

Compare current RPM against typical niche benchmarks:

| Niche | Typical Ezoic RPM | Typical Mediavine RPM |
|-------|-------------------|----------------------|
| Finance / Credit | £12–£25 | £20–£40 |
| Health / Fitness | £6–£15 | £12–£25 |
| Home / Garden | £5–£12 | £10–£20 |
| Food / Recipe | £5–£10 | £8–£18 |
| Tech / Gadgets | £4–£10 | £8–£16 |
| Hobbies / Lifestyle | £3–£8 | £6–£14 |
| General / Mixed | £2–£6 | £5–£12 |

If a site is significantly below niche benchmark, flag as "RPM underperforming" and dig into causes.

## Step 4: Ezoic-Specific Optimisations

For Ezoic sites, check and recommend from this list:

### Ad Placement
- **Above-the-fold unit**: One sticky header or anchor ad — typically highest RPM unit
- **In-content ads**: Place every 300–400 words, minimum 3 units on 1000+ word articles
- **Sidebar**: Only if desktop traffic >40% — otherwise skip
- **Below-title**: High viewability, often 2nd highest RPM unit
- **Footer/anchor**: Always-on units — even low-traffic pages earn from these

### Ezoic Settings to Check
- **HUMIX** (video exchange): Enable if content is evergreen and family-safe — adds £0.50–£2.00 RPM
- **Link Units**: Deprecated — disable if still active
- **Interstitial ads**: Only on sites with multi-page flows — avoid on single-article sites
- **Ad Tester**: Enable "Test Balance" mode so Ezoic auto-optimises placements
- **Leap (site speed)**: Enable — faster sites have higher viewability = higher RPM

### Category Exclusions (what to BLOCK)
These ad categories typically pay low CPM AND harm user experience:
- Dating / Adult (blocks premium advertisers)
- Gambling (unless site is gambling-adjacent)
- Political advertising (CPMs spike then crash — inconsistent)
- Downloads / Freeware (very low CPM, attracts bot traffic)

Keep unblocked: Finance, Insurance, Health, Travel, Technology, Retail — highest CPMs.

### Floor Price Settings
Set a floor price to reject low-value bids:
- Recommend: £0.30–£0.50 floor for UK traffic
- £0.20 floor for US traffic
- Review monthly — too high = unfilled impressions; too low = leaving money

## Step 5: AdSense-Specific Optimisations

For AdSense sites:

### Layout Recommendations
- **Auto ads**: Enable and let Google experiment — usually outperforms manual placement by 10–20%
- **Anchor ads**: Enable for mobile — consistent earner with low intrusion
- **In-article ads**: Enable for long-form content (500+ word articles)
- **Matched content**: Only if you have 100+ indexed pages and Google shows the widget

### Category Blocking (AdSense)
- Block via AdSense > Content > Blocking Controls
- Block: "Get Rich Quick", "Dating", "Downloads & Utilities"
- Never block Finance, Insurance, Travel, Legal — top CPM categories

### AdSense → Ezoic Migration Trigger
Recommend Ezoic when:
- Site has 10,000+ monthly sessions AND
- AdSense RPM is below £3.00 AND
- Site has 50+ articles (enough content for Ezoic AI to test)

## Step 6: Mediavine-Specific Advice

For qualifying sites (50k+ sessions) or sites approaching qualification:

- **Application**: Apply when you hit 48,000 sessions for safety margin
- **Content requirements**: 70%+ original content, no thin pages
- **Session inflation prevention**: Don't artificially inflate with low-quality traffic — Mediavine checks
- **Expected RPM**: 2–3× your Ezoic RPM in the same niche
- **Onboarding**: Takes 2–4 weeks from acceptance to live

## Step 7: Seasonal RPM Calendar

Remind about high and low RPM periods:

| Period | RPM Trend | Action |
|--------|-----------|--------|
| Jan–Feb | Low (-30%) | Reduce floor prices, avoid major layout changes |
| Mar–May | Rising | Good time to test new placements |
| Jun–Aug | Stable | Maintain, focus on content growth |
| Sep–Oct | Rising fast | Prepare for Q4, increase floor prices |
| Nov–Dec | Peak (+50–100%) | Maximise ad density, no site changes |

## Step 8: Output Report

```markdown
# Ad RPM Optimisation Report — {target}
**Generated**: {date} | **Network(s)**: {networks}

## Summary

| Site | Network | Current RPM | Benchmark | Gap | Priority |
|------|---------|------------|-----------|-----|----------|
| {site} | Ezoic | £{X} | £{Y} | {+/-Z}% | HIGH/MED/LOW |

**Portfolio total monthly ad revenue**: ~£{X}
**Estimated uplift from recommendations**: £{X}–£{Y}/mo

---

## Site-by-Site Recommendations

### {site} — {network} — Current RPM: £{X}

**Status**: {Underperforming / On-target / Upgrade candidate}

**Actions** (ordered by expected impact):
1. {Action} — Est. uplift: £{X}/mo
2. {Action} — Est. uplift: £{X}/mo
3. {Action} — Est. uplift: £{X}/mo

**Network verdict**: {Stay / Migrate to Ezoic / Apply Mediavine in N months}

---

## Portfolio-Wide Actions

### Do This Week (quick wins)
- {action}: affects {N} sites, est. +£{X}/mo total

### Do This Month
- {action}: {why + expected impact}

### Watch List (threshold sites)
- {site}: {N}k sessions, Mediavine-eligible in ~{N} months

## Category Exclusions to Add Immediately
Across all Ezoic sites, add these blocks: {list}
```

## Notes

- RPM data must be entered manually from Ezoic/AdSense dashboards — this skill cannot read ad network data directly
- Recommendations are directional estimates; actual uplift varies by traffic quality and seasonal timing
- Never change more than 2–3 settings at once — changes need 2 weeks to stabilise before evaluation
- Ezoic RPM is influenced heavily by traffic geography: UK traffic is 2–3× higher CPM than Indian or African traffic
- techloved.com: 906 Bing clicks/mo — Bing traffic tends to skew older and UK-heavy = good CPMs
