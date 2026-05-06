# Autoresearch Domain Adaptations

How to configure the experiment loop for different domains.

## Configuration Template

For any domain, define these four things before starting:

| Config | Description | Example |
|--------|-------------|---------|
| **Modifiable artifact** | The single file/component the agent can change | `train.py`, `config.json`, `page-title.md` |
| **Fixed budget** | Time or cost cap per experiment | `5 minutes`, `$0.10`, `1 API call` |
| **Metric** | One number to optimize (and direction) | `val_bpb ↓`, `latency_ms ↓`, `CTR% ↑` |
| **Test command** | How to run the experiment | `uv run train.py`, `npm run bench`, `check GSC in 7 days` |

---

## ML Training (Original Use Case)

- **Modifiable artifact:** `train.py`
- **Budget:** 5 minutes wall-clock GPU time
- **Metric:** `val_bpb` (validation bits per byte) — lower is better
- **Test command:** `uv run train.py > run.log 2>&1`
- **Extract metric:** `grep "^val_bpb:" run.log`
- **Notes:** H100 tested. Community forks for lower-spec hardware. Use TinyStories + reduced vocab for smaller GPUs.

---

## Code Performance Optimization

- **Modifiable artifact:** target function/module (e.g., `src/core/indexer.py`)
- **Budget:** benchmark runtime (e.g., 30 seconds of profiling)
- **Metric:** `median_latency_ms ↓` or `memory_mb ↓`
- **Test command:** `python -m pytest benchmarks/ --benchmark-json=bench.json`
- **Extract metric:** `jq '.benchmarks[0].stats.median' bench.json`
- **Notes:** Always warm up; measure median not mean. Keep both before/after profiles.

---

## Prompt Engineering / Eval Optimization

- **Modifiable artifact:** `system_prompt.md` or `prompt_template.py`
- **Budget:** Fixed eval set (e.g., 50 test cases, same every run)
- **Metric:** `eval_score ↑` (accuracy, F1, or custom rubric)
- **Test command:** `python run_eval.py --prompt system_prompt.md --output results.json`
- **Extract metric:** `jq '.overall_score' results.json`
- **Notes:** Never change the eval set between experiments. Track token cost per run.

---

## SEO / CTR Optimization

- **Modifiable artifact:** `titles-meta.md` (list of title/meta candidates for a page)
- **Budget:** 7-day GSC data window per variant (or use Search Console Preview for faster signal)
- **Metric:** `CTR% ↑` for target page from GSC
- **Test command:** Deploy variant, note date, check GSC after budget window
- **Extract metric:** GSC → Performance → filter by page URL → CTR
- **Notes:** Only change one element at a time (title OR meta, not both). Seasonal effects can confound — note any unusual events.

---

## Content Quality Iteration

- **Modifiable artifact:** single article/page file
- **Budget:** `/semantic-audit` score (synchronous — no wait needed)
- **Metric:** audit score ↑ (0-100)
- **Test command:** Run `/semantic-audit` on the file
- **Extract metric:** Overall score from audit output
- **Notes:** This loop runs in a single session since the metric is instant. Target score ≥85 before publishing.

---

## Config/Hyperparameter Tuning

- **Modifiable artifact:** `config.yaml` or similar
- **Budget:** fixed test run duration
- **Metric:** application-specific (error rate ↓, throughput ↑, etc.)
- **Test command:** application-specific test suite
- **Notes:** Change one parameter at a time. Log parameter name + old value + new value in description column.
