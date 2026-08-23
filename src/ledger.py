#!/usr/bin/env python3
"""Brier Scoring Ledger for forecasting-swarm.

Records predictions, resolves them, computes Brier scores, and outputs analyst weights.

A ledger is a scorebook: every forecast is written down, scored when the real
outcome arrives, and forecasters with better track records earn more voting
weight in future debates.

Usage:
  ledger.py record <question_id> <analyst> <probability> [round]
  ledger.py resolve <question_id> <outcome>       # outcome: 0 or 1
  ledger.py weights <question_id>                 # show analyst weights
  ledger.py status                                # all predictions
"""
import sqlite3, sys, os

DB = os.path.expanduser(os.environ.get("LEDGER_DB", "~/.forecasting/ledger.db"))

def connect():
    os.makedirs(os.path.dirname(DB), exist_ok=True)
    conn = sqlite3.connect(DB)
    conn.execute("""CREATE TABLE IF NOT EXISTS predictions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT NOT NULL,
        analyst TEXT NOT NULL,
        probability REAL NOT NULL,
        round INTEGER DEFAULT 1,
        created_at TEXT DEFAULT (datetime('now')),
        resolved INTEGER DEFAULT 0,
        outcome INTEGER,
        brier_score REAL
    )""")
    return conn

def record(question, analyst, prob, rnd=1):
    conn = connect()
    conn.execute("INSERT INTO predictions (question, analyst, probability, round) VALUES (?,?,?,?)",
                 (question, analyst, prob, rnd))
    conn.commit()
    print(f"recorded: {analyst} on '{question}' = {prob}% (R{rnd})")

def resolve(question, outcome):
    conn = connect()
    outcome = int(outcome)
    rows = conn.execute("SELECT id, analyst, probability FROM predictions WHERE question=? AND resolved=0",
                        (question,)).fetchall()
    if not rows:
        print("no unresolved predictions for that question")
        return
    for pid, analyst, prob in rows:
        p = prob / 100.0
        brier = (p - outcome) ** 2
        conn.execute("UPDATE predictions SET resolved=1, outcome=?, brier_score=? WHERE id=?",
                     (outcome, brier, pid))
        print(f"  {analyst}: {prob}% -> outcome {outcome}, Brier {brier:.4f}")
    conn.commit()

def weights(question):
    conn = connect()
    rows = conn.execute("""SELECT analyst, AVG(brier_score) as avg_brier, COUNT(*) as n
                           FROM predictions WHERE question=? AND resolved=1
                           GROUP BY analyst""", (question,)).fetchall()
    if not rows:
        print("no resolved predictions for that question")
        return
    print(f"Analyst weights for '{question}':")
    inv = {}
    for analyst, avg, n in rows:
        w = 1.0 / (1.0 + avg)
        inv[analyst] = w
    total = sum(inv.values())
    for analyst, avg, n in rows:
        print(f"  {analyst}: avg Brier {avg:.4f} (n={n}), weight {inv[analyst]/total:.3f}")

def status():
    conn = connect()
    rows = conn.execute("SELECT question, analyst, probability, round, resolved, brier_score FROM predictions ORDER BY created_at").fetchall()
    print(f"{'Question':<30}{'Analyst':<16}{'Prob':>6}{'R':>3}{'Res':>5}{'Brier':>8}")
    for q, a, p, r, res, b in rows:
        print(f"{q[:28]:<30}{a[:14]:<16}{p:>6.1f}{r:>3}{'Y' if res else '-':>5}{b if b is not None else '':>8}")

if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        status()
    elif args[0] == "record" and len(args) >= 4:
        record(args[1], args[2], float(args[3]), int(args[4]) if len(args) > 4 else 1)
    elif args[0] == "resolve" and len(args) == 3:
        resolve(args[1], args[2])
    elif args[0] == "weights" and len(args) == 2:
        weights(args[1])
    elif args[0] == "status":
        status()
    else:
        print(__doc__)
