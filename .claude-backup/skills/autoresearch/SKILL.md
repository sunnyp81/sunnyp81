---
name: autoresearch
description: >
  Autonomous iterative experimentation loop based on Karpathy's autoresearch framework.
  Use when: running overnight ML training experiments, iteratively optimising code performance,
  A/B testing content or SEO changes, or any task where the goal is to minimize/maximize a
  single metric through repeated modify→test→measure cycles without human intervention.
  Triggers on: "run experiments", "optimize overnight", "iterative improvement loop",
  "autonomous optimization", "keep trying variations", "autoresearch", "experiment loop".
version: 1.0.0
user-invocable: true
allowed-tools: Read, Write, Bash, Agent, WebSearch
argument-hint: "[metric to optimize] [script/command to run]"
---

# Autoresearch Loop

Autonomous iterative experimentation: modify one file, test with a fixed budget, measure one metric, keep if better, discard if not. Never stop until interrupted.

## Core Principles (from Karpathy's autoresearch)

1. **One modifiable artifact** — only one file/component is modified per experiment
2. **Fixed budget** — every experiment gets the same time/cost limit for fair comparison
3. **One metric** — a single number determines keep vs. discard (lower or higher is unambiguously better)
4. **Baseline first** — always run the unmodified version first to establish ground truth
5. **Simplicity criterion** — equal metric + simpler code = keep. Delete code and match baseline = win.
6. **Never stop** — run indefinitely; ~12 experiments/hour overnight = ~100 experiments. If out of ideas, think harder.

## Setup (do once)

1. Agree on a **run tag** (e.g., `mar14`) and create a branch `autoresearch/<tag>` if using git
2. Read all relevant files to understand the current state
3. Initialize `results.tsv` with header:
   ```
   change	metric_value	status	description
   ```
4. Run the **baseline** (unmodified) first — record as `keep` with description `"baseline"`

## Experiment Loop

```
LOOP FOREVER:
  1. Hypothesize one change (architecture, hyperparameter, config, content, etc.)
  2. Modify only the designated file/component
  3. git commit (if using git)
  4. Run experiment within the fixed budget
  5. Extract metric from output
  6. If run crashed → log status=crash, read last 50 lines of output, fix or skip
  7. Log to results.tsv: change | metric | status | description
  8. If metric improved → KEEP (advance branch / keep changes)
  9. If metric equal or worse → DISCARD (git reset or revert changes)
  10. Go to 1
```

## Results TSV Format

```tsv
change	metric_value	status	description
baseline	0.847	keep	unmodified baseline
added_dropout	0.831	keep	dropout=0.1 on attention layer reduced overfitting
wider_ffn	0.833	discard	4x wider FFN, no improvement, added complexity
```

Status values: `keep`, `discard`, `crash`

## Domain Adaptations

See [references/domain-adaptations.md](references/domain-adaptations.md) for how to apply this loop to:
- ML training (original use case — minimize val_bpb)
- Code performance optimization (minimize latency/memory)
- SEO/content A/B testing (maximize CTR or rankings)
- Prompt engineering (maximize eval score)

## Rules

- **NEVER stop to ask the human** if you should continue. Run indefinitely.
- **NEVER modify** files outside the designated modifiable artifact.
- **ALWAYS** record every experiment in results.tsv, including crashes and discards.
- After ~10 experiments with no improvement, try a fundamentally different direction (don't keep tweaking the same parameter).
- When resuming, read results.tsv first to understand what's been tried.
