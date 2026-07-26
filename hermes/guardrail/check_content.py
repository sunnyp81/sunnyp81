#!/usr/bin/env python3
"""
Content guardrail for the affiliate-site portfolio.

Fails a build when content contains the fabrication and hygiene defects the
2026-07-26 UX audit found across the portfolio, so the autonomous content
pipeline (Hermes) cannot silently re-introduce them.

Rules (each can be toggled per repo via .content-guardrail.json):
  no_dashes            em/en dashes in user-facing content        (BLOCKER)
  no_conflict_markers  git conflict markers committed to content   (BLOCKER)
  no_persona_schema    Person JSON-LD / persona @id / persona
                       frontmatter authorship                      (BLOCKER)
  no_fabricated_test   first-person "we tested/measured/our lab"
                       claims on a site with no test lab           (BLOCKER)
  pmid_shape           PMID citations that are not 6-9 digit ids   (WARN)

The PubMed cross-check (does PMID N actually match the cited title?) needs
network and is intentionally NOT run here; it lives in the audit tooling.
This checker is offline, stdlib-only, and safe to run in any CI.

Config: optional .content-guardrail.json at repo root, e.g.
  {
    "globs": ["src/content/**/*.md", "src/pages/**/*.astro", "public/*.txt"],
    "rules": {
      "no_dashes": true,
      "no_conflict_markers": true,
      "no_persona_schema": true,
      "no_fabricated_test": true,
      "pmid_shape": true
    },
    "personas": ["jasmine", "david", "dr-ruth", "maya hollander"],
    "allow": ["src/content/legal/*"]
  }

Exit code 0 = clean, 1 = one or more BLOCKER hits, 2 = bad usage/config.
"""
from __future__ import annotations

import argparse
import fnmatch
import json
import os
import re
import sys

DEFAULT_GLOBS = [
    "src/content/**/*.md",
    "src/content/**/*.mdx",
    "src/content/**/*.astro",
    "src/data/**/*.ts",
    "src/data/**/*.json",
    "src/pages/**/*.astro",
    "src/components/**/*.astro",
    "public/*.txt",
]

DEFAULT_RULES = {
    "no_dashes": True,
    "no_conflict_markers": True,
    "no_persona_schema": True,
    "no_fabricated_test": True,
    "pmid_shape": True,
}

# Rules that fail the build. Everything else is reported as WARN only.
# no_fabricated_test and pmid_shape are inherently fuzzy (a regex cannot tell
# "we tested" fabrication from "we do not fabricate testing"), so they surface
# for the PR reviewer rather than blocking. Override per repo via
# .content-guardrail.json "severities": {"no_fabricated_test": "BLOCKER"}.
DEFAULT_SEVERITY = {
    "no_dashes": "BLOCKER",
    "no_conflict_markers": "BLOCKER",
    "no_persona_schema": "BLOCKER",
    "no_fabricated_test": "WARN",
    "pmid_shape": "WARN",
}

# Skip a fabricated-test match when the clause negates or hypothesises it
# (honest disclosures, reader-directed advice), e.g. "we do not fabricate
# hands-on testing", "if you want to test".
FAB_TEST_NEGATION_RE = re.compile(
    r"\b(?:not|never|no|without|do\s+not|don't|didn't|cannot|can't|if\s+you|"
    r"you\s+can|reader|yourself)\b",
    re.I,
)

# em dash, en dash, horizontal bar, and the &mdash;/&ndash; entities
DASH_RE = re.compile(r"[—–―]|&mdash;|&ndash;")
CONFLICT_RE = re.compile(r"^(?:<{7}|={7}|>{7})(?:\s|$)", re.MULTILINE)
PERSON_SCHEMA_RE = re.compile(r'"@type"\s*:\s*"Person"')
PERSONA_ID_RE = re.compile(r'"@id"\s*:\s*"[^"]*#(?:jasmine|david|dr-ruth|maya|persona)[^"]*"', re.I)
PERSONA_FM_RE = re.compile(r"^\s*(?:authored_by|reviewed_by|reviewedBy|author)\s*:", re.M)
# first-person testing claims that imply a lab / hands-on protocol
FAB_TEST_RE = re.compile(
    r"\b("
    r"we\s+tested|we\s+measured|our\s+testing|our\s+lab|hands[-\s]on\s+test(?:ing)?|"
    r"our\s+test\s+unit|we\s+weighed|we\s+brewed|we\s+filled\s+each|"
    r"\d+\s*[-\s]?(?:week|month|day)\s+test|our\s+methodology,\s*our\s+data|"
    r"measured\s+(?:with|at)\s+(?:a\s+)?(?:radiometer|solar\s+meter|spectrometer|luggage\s+scale)"
    r")\b",
    re.I,
)
PMID_RE = re.compile(r"PMID:?\s*([0-9A-Za-z]+)", re.I)


def load_config(root: str) -> dict:
    path = os.path.join(root, ".content-guardrail.json")
    cfg = {
        "globs": DEFAULT_GLOBS,
        "rules": dict(DEFAULT_RULES),
        "severities": dict(DEFAULT_SEVERITY),
        "personas": [],
        "allow": [],
    }
    if os.path.exists(path):
        try:
            with open(path, encoding="utf-8") as fh:
                user = json.load(fh)
        except (OSError, ValueError) as exc:
            print(f"guardrail: cannot read {path}: {exc}", file=sys.stderr)
            sys.exit(2)
        cfg["globs"] = user.get("globs", cfg["globs"])
        cfg["personas"] = user.get("personas", [])
        cfg["allow"] = user.get("allow", [])
        cfg["rules"].update(user.get("rules", {}))
        cfg["severities"].update(user.get("severities", {}))
    return cfg


def iter_files(root: str, globs, allow) -> list[str]:
    seen: list[str] = []
    for pattern in globs:
        for path in _glob(root, pattern):
            rel = os.path.relpath(path, root)
            if any(fnmatch.fnmatch(rel, a) for a in allow):
                continue
            if rel not in seen:
                seen.append(rel)
    return sorted(seen)


def _glob(root: str, pattern: str) -> list[str]:
    import glob as _g

    return [p for p in _g.glob(os.path.join(root, pattern), recursive=True) if os.path.isfile(p)]


def check_file(root: str, rel: str, rules: dict, severities: dict, personas):
    """Return list of (severity, lineno, rule, excerpt)."""
    hits: list[tuple[str, int, str, str]] = []
    path = os.path.join(root, rel)
    try:
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
    except (OSError, UnicodeDecodeError):
        return hits
    lines = text.splitlines()

    def line_of(idx: int) -> int:
        return text.count("\n", 0, idx) + 1

    def excerpt(lineno: int) -> str:
        s = lines[lineno - 1].strip() if 0 < lineno <= len(lines) else ""
        return (s[:100] + "...") if len(s) > 100 else s

    def sev(rule_key: str) -> str:
        return severities.get(rule_key, "BLOCKER")

    if rules.get("no_conflict_markers"):
        for m in CONFLICT_RE.finditer(text):
            ln = line_of(m.start())
            hits.append((sev("no_conflict_markers"), ln, "no_conflict_markers", excerpt(ln)))

    if rules.get("no_dashes"):
        for i, line in enumerate(lines, 1):
            if DASH_RE.search(line):
                hits.append((sev("no_dashes"), i, "no_dashes", line.strip()[:100]))

    if rules.get("no_persona_schema"):
        for m in PERSON_SCHEMA_RE.finditer(text):
            ln = line_of(m.start())
            hits.append((sev("no_persona_schema"), ln, "no_persona_schema:Person", excerpt(ln)))
        for m in PERSONA_ID_RE.finditer(text):
            ln = line_of(m.start())
            hits.append((sev("no_persona_schema"), ln, "no_persona_schema:@id", excerpt(ln)))
        # named personas anywhere in content
        for name in personas:
            for m in re.finditer(re.escape(name), text, re.I):
                ln = line_of(m.start())
                hits.append((sev("no_persona_schema"), ln, f"no_persona_schema:name:{name}", excerpt(ln)))
        # frontmatter authorship only within the leading --- block
        if text.startswith("---"):
            end = text.find("\n---", 3)
            fm = text[: end if end != -1 else len(text)]
            for m in PERSONA_FM_RE.finditer(fm):
                ln = line_of(m.start())
                hits.append((sev("no_persona_schema"), ln, "no_persona_schema:frontmatter", excerpt(ln)))

    if rules.get("no_fabricated_test"):
        for i, line in enumerate(lines, 1):
            m = FAB_TEST_RE.search(line)
            if not m:
                continue
            # skip negated / hypothetical / reader-directed clauses
            window = line[max(0, m.start() - 40):m.end() + 5]
            if FAB_TEST_NEGATION_RE.search(window):
                continue
            hits.append((sev("no_fabricated_test"), i, "no_fabricated_test", line.strip()[:100]))

    if rules.get("pmid_shape"):
        for m in PMID_RE.finditer(text):
            pid = m.group(1)
            if not (pid.isdigit() and 4 <= len(pid) <= 9):
                ln = line_of(m.start())
                hits.append((sev("pmid_shape"), ln, "pmid_shape", excerpt(ln)))

    return hits


def main() -> int:
    ap = argparse.ArgumentParser(description="Portfolio content guardrail.")
    ap.add_argument("--root", default=".", help="repo root (default: cwd)")
    ap.add_argument("--warn-only", action="store_true", help="never exit non-zero (report only)")
    args = ap.parse_args()

    root = os.path.abspath(args.root)
    cfg = load_config(root)
    files = iter_files(root, cfg["globs"], cfg["allow"])

    all_hits: list[tuple[str, str, int, str, str]] = []
    for rel in files:
        for sev, ln, rule, exc in check_file(root, rel, cfg["rules"], cfg["severities"], cfg["personas"]):
            all_hits.append((sev, rel, ln, rule, exc))

    blockers = [h for h in all_hits if h[0] == "BLOCKER"]
    warns = [h for h in all_hits if h[0] == "WARN"]

    for sev, rel, ln, rule, exc in all_hits:
        print(f"{sev:8} {rel}:{ln}  [{rule}]  {exc}")

    print(
        f"\nguardrail: scanned {len(files)} files, "
        f"{len(blockers)} blocker(s), {len(warns)} warning(s)."
    )
    if blockers and not args.warn_only:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
