# Debate Recipe — 3-Round Multi-Panelist Forecast

Copy-ready prompt templates for running a 5-panelist forecasting debate.

## Setup

Create a fact-sheet first: 15-20 key facts from real sources (search + deep extraction), with the Polymarket/market anchor if one exists. **Curate — do not dump raw data on the panelists.**

## Round 1 — Openings (parallel)

Send this to each panelist (change the lens per analyst):

```
You are Analyst N (<MODEL>, <LENS> lens) in a 5-analyst forecasting debate on <TOPIC>.

FACT-SHEET:
<15-20 curated facts>

BASE RATES:
<historical base rates relevant to the question>

QUESTIONS:
Q1: <falsifiable question>?
Q2: <falsifiable question>?

TASK (Round 1): For each question give: probability (0-100%) + 2-3 arguments + 1 counterargument. Be specific, use the data. Format:
Q1: NN% - args...
Q2: NN% - args...
Counterargument: ...
Max 180 words.
```

## Round 2 — Rebuttal (parallel)

Collect all 5 Round-1 positions. Send each analyst ALL positions and have them respond to two specific ones:

```
You are Analyst N (<MODEL>), Round 2.

ROUND 1 POSITIONS (all 5):
- <ANALYST A>: <position>
- <ANALYST B>: <position>
... (all 5)

TASK: Respond explicitly to <ANALYST X>'s position and <ANALYST Y>'s position, then give REVISED probabilities. Format:
ON <X>'S POINT: ...
ON <Y>'S POINT: ...
Q1: NN%. Q2: NN%.
Max 160 words.
```

## Round 3 — Finals (parallel)

```
You are Analyst N (<MODEL>), FINAL Round 3.

ROUND 2 REVISIONS:
- <all 5 revisions>

TASK: Give your FINAL probability for Q1 and Q2, and state in one line what the consensus changed for you. Format:
FINAL Q1: NN%
FINAL Q2: NN%
CONSENSUS EFFECT: one line.
Max 80 words.
```

## Oracle — Blend

- **Simple:** mean of the 5 finals.
- **Track-record weighted:** `weight = 1/(1+avg_brier)` per analyst, normalized. Use once 4-5 questions have resolved.

## What Success Looks Like

- Spread (max−min) collapses from Round 1 to Round 3 — the debate moved people with reasons.
- Outliers get pulled toward center: the 43% skeptic cites the escalation case; the 62% bulls cite mean-reversion.
- Q2 (tail risk) barely moves — nuclear-state base rates are robust.

## Cost

~$0.05-0.15 per full debate with cheap models (DeepSeek Flash, GLM Fast, Qwen Flash + two subscription CLIs).
