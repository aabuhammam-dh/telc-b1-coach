# telc-b1-exam — how to use it

Your strict telc **Deutsch B1** coach for the objective sections (Leseverstehen,
Sprachbausteine, Hörverstehen) and the oral exam, built around practising on past papers.
It logs and grades your answers, explains every miss, finds recurring traps, drills your
weak points, mines vocab/grammar from a test, and prepares the Mündliche Prüfung. The
**letter (Schreiben)** is handled by its companion skill, `telc-b1-schreiben`, which this
one hands off to automatically.

> Not the DTZ. This is the general adult telc Deutsch B1 exam.

## Quick start
1. Install the skill (click **Save skill** on the `.skill` file).
2. Put your practice-exam PDFs where the coach can read them (in this project they live in
   `/mnt/project/`). The coach reads them directly — they can be ZIP-style `.pdf` exports.
3. Talk to it in plain language or with a command in brackets, e.g. `[log exam]` or
   *"grade my Vera answers"* or *"explain obwohl vs. trotzdem."*

## Commands (cheat-sheet)
| Command | Use it to |
|---|---|
| `[log exam]` | Enter your answers to one exam and get it **graded** (code-checked, never eyeballed). |
| `[score "Jan"]` | See a stored exam's score, weak areas, and what's still pending. |
| `[discuss "Jan"]` | Walk every wrong answer: the correct one, the trap type, the rule. |
| `[study "Jan"]` | A teaching session on that exam's grammar, vocab, connectors, traps. |
| `[practice "Jan"]` | Drill: re-ask your misses + fresh look-alike items, corrected B1-safe. |
| `[retake "Jan"]` | Timed full simulation, no help during, strict grading after. |
| `[extract "Jan"]` / `[extract all]` | Mine must-know **vocab (DE→EN)**, **connectors** (+ how each works), and the **critical grammar** the Sprachbausteine tests. |
| `[mock exam]` / `[generate test]` | **No exam PDF? Generate a fresh, original telc-format practice test** (full or one section) at real B1 difficulty, with an answer key. New content every time. |
| `[topic "<name>"]` / `[topic]` | **Teach + test one topic** (a grammar point, connectors, or a vocab theme), then give a ready/shaky/not-ready verdict and track it. `[topic]` alone recommends what to train next from your weak spots. |
| `[weaknesses]` | See your weakness profile across all exams and get targeted drills. |
| `[compare exams]` | Cross-exam patterns + which past papers reuse the same texts. |
| `[write "Jan"]` | Work on that exam's **letter** → activates `telc-b1-schreiben`. |
| `[help]` | Print the command list. |

Bracket or slash, it doesn't matter (`[log exam]` = `/log-exam`). Names in quotes are your
exams (Jan, Vera, Eva, Petra, …).

## The workflow that gets the most out of it
Run this loop per exam, then move to the next:
1. **`[log exam]`** → grade it. The coach records your strengths/weaknesses automatically.
2. **`[discuss "…"]`** → understand *why* each miss happened (trap type + rule).
3. **`[extract "…"]`** → pull the vocab, connectors, and grammar that exam tested.
4. **`[practice "…"]`** → drill the exact misses + look-alikes until the trap is dead.
5. Later, **`[retake "…"]`** cold to confirm it stuck.
6. Every week or so, **`[compare exams]`** and **`[weaknesses]`** to re-aim at what's
   currently costing you the most points.

Separately, keep the **letter** moving with `[write "…"]` (→ Schreiben skill) and rehearse
the **oral** by asking it to run Teil 1 / 2 / 3 practice — those are two of the biggest
point blocks and easy to neglect.

## Tips for best results
- **Give it your real answers**, not a summary — grading is question-by-question.
- **Ask "am I passing?"** and it reasons in *weighted* points (the letter is 45 of the 225
  written points), not just the raw x/60 tracker.
- **Grammar questions get grounded answers** — the coach web-searches a reputable German
  grammar source first, then explains simply. Ask freely (*"when is it dative after in?"*).
- **Prioritise Lesen & Hören accuracy over Sprachbausteine** when time is tight: each
  Lesen/Hören item is worth 2.5× an SB item in real points (though SB is the fastest to
  fix, being pattern-based).
- **Let it save to memory** so vocab, connectors, and your weakness profile compound
  across sessions.

## What it needs
- **No practice exams? No problem** — use `[mock exam]` and it generates original,
  telc-format practice for you. Practice-exam PDFs are optional: add them if you have them
  (answer keys are on the last page) and it'll grade and mine those too.
- Web access for grammar explanations (it searches, then grounds the answer).
- The `telc-b1-schreiben` skill installed for anything about the letter.
