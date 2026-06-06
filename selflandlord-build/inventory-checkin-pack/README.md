# Inventory & Check-In / Check-Out Pack — ready to ship

First product from the paid-template-ideas list. Built here because this session
is scoped to `sunnyp81/sunnyp81`; copy these into the `sunnyp81/selflandlord` repo.

## What's here

```
documents/
  inventory-schedule-of-condition.html   # flagship — room-by-room, meters, alarms, signatures
  check-in-report.html                   # start of tenancy, tenant acceptance + 7-day amend window
  check-out-report.html                  # end of tenancy, condition comparison + deposit deductions
inventory-pack.astro                     # landing page for /templates/inventory-pack/
```

The three HTML docs are A4 print-ready (open in any browser → Print → Save as PDF).
This matches the existing "raw HTML, no Brevo template dep" delivery. They are
also editable in Word. All carry the RRA-2025 disclaimer.

## Ship steps (in selflandlord repo)

1. **Zip the product:** add the 3 docs to `private/paid-pack/` and into the
   LemonSqueezy paid-pack zip (the same place the tenancy pack lives).
2. **Create the LS product** (£9) → paste the Share/Buy URL into the page's
   `BUY_URL` (and/or `src/config/paid-pack.ts` if you route through config).
3. **Add the page:** copy `inventory-pack.astro` to
   `src/pages/templates/inventory-pack.astro`, fix the `Layout` import path,
   confirm it uses the real `MoneyCTA` component for the bundle upsell.
4. **Lead magnet (optional):** add an `ASSETS` map entry in
   `src/pages/api/subscribe.ts` so the inventory doc can be drip-delivered free
   to capture the email, then upsell the £9 pack + £39 bundle.
5. **Internal links + nav + sitemap:** link from `/templates/tenancy-agreement/`
   ("next: protect the deposit") and add to nav/sitemap.
6. **Deploy:** Wrangler CLI (this site deploys via Wrangler, not GitHub).
7. **Bing/GSC:** submit the new URL via index-push.

## Why this one first

Proven Etsy seller, deposit-dispute pain is acute, low legal risk, and it pairs
naturally with the tenancy page that just sold. Email yesterday's buyer this
pack as the first cross-sell.

## SEO target

`landlord inventory template uk 2026`, `check in check out report template`,
`inventory schedule of condition`, with `renters rights act` modifiers — the
whole market's existing templates are now stale.
