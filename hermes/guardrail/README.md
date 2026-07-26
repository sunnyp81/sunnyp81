# content guardrail

A stdlib-only, offline check that fails a build when content carries the
fabrication and hygiene defects the 2026-07-26 portfolio UX audit found, so the
autonomous content pipeline (Hermes) cannot silently re-introduce them.

It is the standing counterpart to that one-off audit: the audit found the
defects, this keeps them out.

## What it catches

| rule | default severity | catches |
|------|------------------|---------|
| `no_dashes` | BLOCKER | em/en dashes and `&mdash;`/`&ndash;` in content (global house rule) |
| `no_conflict_markers` | BLOCKER | `<<<<<<<` / `=======` / `>>>>>>>` committed to content |
| `no_persona_schema` | BLOCKER | `"@type":"Person"` JSON-LD, `#persona` `@id` refs, named personas, `authored_by:`/`reviewedBy:` frontmatter |
| `no_fabricated_test` | WARN | first-person "we tested / we measured / our lab / N-week test" language (negation-guarded) |
| `pmid_shape` | WARN | `PMID:` values that are not 4-9 digit ids |

The two WARN rules are inherently fuzzy: a regex cannot tell "we tested" from
"we do not fabricate testing", so they surface for the reviewer rather than
block. A whole class of fabrication (invented studies, fake owner quotes,
mismatched-but-well-formed PMIDs) is NOT regex-detectable and is deliberately
out of scope here: that is what the audit's model verify pass is for. This
check is the cheap, deterministic floor, not the ceiling.

## Run it locally

```
python hermes/guardrail/check_content.py --root /path/to/site-repo
```

Exit 0 = clean, 1 = a BLOCKER matched, 2 = bad config.
Add `--warn-only` to report without failing.

## Per-repo config (optional)

Drop `.content-guardrail.json` at a site repo root to tune it:

```json
{
  "globs": ["src/content/**/*.md", "src/pages/**/*.astro", "public/*.txt"],
  "personas": ["Jasmine Sinclair", "David Okonkwo", "Ruth Pemberton"],
  "severities": { "no_fabricated_test": "BLOCKER" },
  "allow": ["src/content/legal/*"]
}
```

- `personas`: names to hard-block on sites that invented author bios
  (bestvibrationplates, redlighttherapy-expert). Leave empty elsewhere.
- `severities`: promote a WARN rule to BLOCKER on a site where you want the
  no-test-lab rule enforced hard (e.g. towerfanreviews, which states the rule).
- `allow`: glob(s) of files to skip.

## Wire it into a site repo's CI

Add this one file to the site repo as `.github/workflows/guardrail.yml`:

```yaml
name: guardrail
on:
  pull_request:
  push:
    branches: [main, master]
jobs:
  content:
    uses: sunnyp81/sunnyp81/.github/workflows/content-guardrail.yml@main
```

The reusable workflow checks out the caller, fetches this script from
`sunnyp81/sunnyp81`, and runs it. No secrets needed (this repo is public).

## Relationship to the rollout

`.github/workflows/ux-audit.yml` in this repo runs the same script across every
site in one manual dispatch and, when explicitly asked, opens branch-only fix
PRs. It never merges. See that file's header for the two secrets it needs.
