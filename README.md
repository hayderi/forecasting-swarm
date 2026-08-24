# Forecasting Swarm — Multi-LLM Prediction Tool

A **5-panelist forecasting system** that runs a structured debate between independent LLMs to produce calibrated probability forecasts — the same architecture used by Metaculus, Polymarket, and ForecastBench.

Designed around a simple idea: *more independent AI minds + real data + scored track records = better predictions than any single model.*

## 🔮 How It Works

```
SCOUT LAYER (data)
  Search (SearXNG) → Deep Extract (Scrapling) → Market Anchor (Polymarket)
  → CURATED FACT-SHEET (15-20 key facts with sources)

PANEL (5 independent analysts — different model families)
  1. Claude Code CLI        (Anthropic)
  2. Codex CLI              (OpenAI)
  3. DeepSeek V4 Flash      (DeepSeek)
  4. GLM-5.2                (Zhipu, China)
  5. Qwen 3.7               (Alibaba, China)

DEBATE (3 rounds)
  Round 1: each analyst states probabilities + arguments + counterargument
  Round 2: all positions relayed; each responds "ON X'S POINT..." + REVISED probability
  Round 3: FINAL probabilities + consensus effect

ORACLE: blended final (track-record weighted once scores exist)
LEDGER: every prediction recorded; Brier-scored on resolution; good forecasters earn more vote weight
```

## 🧠 Why 5 different models?

Different AI companies train their models differently. When 5 independent families debate:
- No echo chamber (one model arguing with itself)
- Genuine disagreement surfaces real uncertainty
- The **spread collapse** across rounds is the proof of learning

*Observed: a market-entry forecast spread collapsed from 19pts → 7pts across 3 rounds.*

## 📦 What's Inside

| File | Purpose |
|---|---|
| `src/ledger.py` | Brier scoring ledger (SQLite) — record/resolve/weights |
| `docs/debate-recipe.md` | Copy-ready prompt templates for all 3 rounds |
| `examples/` | Full worked example (synthetic market-entry forecast) |

## 🚀 Quick Start

### 1. The Ledger (works standalone — no LLMs needed)

```bash
python3 src/ledger.py record "question-1" "Analyst-A" 62 1
python3 src/ledger.py record "question-1" "Analyst-B" 43 1
python3 src/ledger.py resolve "question-1" 1          # outcome: 0 or 1
python3 src/ledger.py weights "question-1"            # track-record weights
python3 src/ledger.py status                          # all predictions
```

### 2. The Full Debate (needs the 5 CLIs/models)

See `docs/debate-recipe.md` for the exact prompts. Each analyst runs as a one-shot call:

```bash
# Panelist 1: Claude Code CLI
claude -p "$(cat round1_prompt.txt)" --output-format text

# Panelist 2: Codex CLI (needs a git repo)
cd /tmp/debate && codex exec --sandbox danger-full-access "$(cat round1_prompt.txt)"

# Panelists 3-5: any OpenAI-compatible provider
hermes chat -q "$(cat round1_prompt.txt)" --provider custom:commandcode --model deepseek/deepseek-v4-flash -Q
```

Then relay all positions into Round 2, relay revisions into Round 3, blend the finals.

## 🏆 The Scoring Loop (Brier Ledger)

A **ledger** is a scorebook. Every prediction is written down; when the real outcome arrives, each forecaster gets a grade:

```
Brier score = (probability − outcome)²
```

- Close guess = low score (good) · Wild guess = high score (bad)
- Analysts with better cumulative scores earn **more voting weight** in future debates
- Weights become meaningful after 4-5 resolved questions

This turns "bots arguing" into a **self-improving forecasting system** — the actual engine of Metaculus/ForecastBench.

## ⚠️ Honest Caveats

- **No model predicts deterministically.** The value is calibrated probabilities + scoring, not fortune-telling.
- **Scout data quality is everything** — real facts in = sharp debate; raw dumps = noise. Curate to 15-20 facts.
- **First 4-5 resolutions are calibration data** — weights are equal until track records exist.
- Cost per full debate: **~$0.05-0.15** (cache-heavy, cheap models) — pennies.

## 📜 License

MIT — free to use, modify, and share.

---

*Built with Hermes Agent. Inspired by Metaculus, ForecastBench (Forecasting Research Institute), and prediction-market methodology.*
