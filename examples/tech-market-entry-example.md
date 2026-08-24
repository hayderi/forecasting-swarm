# Worked Example — Regional Tech-Company Market-Entry Forecast

A full run of the 5-panelist debate, captured end to end. The scenario is **synthetic** — it demonstrates the method, not a real prediction.

## Questions

- **Q1:** Will the company's annual revenue in the target region exceed $50M in the next fiscal year?
- **Q2:** Will a major competitor launch a rival product in the same region within 24 months?
- **Q3:** If revenue growth materializes, when does it cross the $50M threshold (earliest quarter)?

## Scout Fact-Sheet (synthetic, for demonstration)

1. Current regional revenue run-rate is $38M, growing ~8% YoY.
2. Two enterprise deals worth a combined $9M are in late-stage negotiation.
3. A competitor announced an expanded regional sales team in the last quarter.
4. Regional economic indicators show modest growth; currency stable.
5. Regulatory environment unchanged; no new barriers expected.
6. Customer churn rate stable at 3.2% quarterly.
7. No prediction-market (e.g., Polymarket) contract exists for this specific question — thin external attention is itself a signal.

**Base rates:** Enterprise software expansion typically takes 2-3 quarters from deal signing to revenue recognition; competitor entry raises marketing costs by 15-25% in year one; market leaders retain ~60% of existing customers through competitive cycles.

## The Panel

Claude (CLI) · Codex (CLI) · DeepSeek V4 Flash · GLM-5.2 · Qwen 3.7

## Round-by-Round (Q1: revenue > $50M)

| Panelist | R1 | R2 | R3 Final |
|---|---|---|---|
| Claude | 62% | 58% | **57%** |
| Codex | 43% | 49% | **51%** |
| DeepSeek | 58% | 54% | **54%** |
| GLM | 62% | 60% | **58%** |
| Qwen | 52% | 55% | **55%** |
| **Mean** | **55.4%** | **55.2%** | **55.0%** |
| **Spread** | **19 pts** | — | **7 pts** |

### What moved people (Round 2 excerpts)

- **Codex (43→49):** "The pipeline deals and stable churn are real, but hitting $50M requires closing both deals — base effects alone don't get there."
- **Claude (62→58):** "Revenue recognition lag is the counterweight; even signed deals take 2-3 quarters to show in the top line."
- **DeepSeek (58→54):** "The competitor expansion changes the unit economics — that's a structural driver, not a blip."
- **GLM (62→60):** "Competitor-entry risk trims the upside but the pipeline momentum is still the dominant signal."
- **Qwen (52→55):** "The two late-stage deals plus stable churn push me slightly above the midpoint."

## Final Forecast

- **Q1: 55%** (revenue exceeds $50M next fiscal year — slightly favored)
- **Q2: 8.6%** (major competitor launches within 24 months — low; regulatory/scale barriers)
- **Q3: Q3 next year earliest** (Claude/Codex/DeepSeek); GLM Q1; Qwen H2

## Ledger

All 15 predictions (5 analysts × 3 rounds) recorded. On resolution (end of fiscal year), each analyst gets a Brier grade and weights adjust.
