# telc-b1-schreiben — how to use it

Your strict coach for the **written letter** of the telc **Deutsch B1** exam (the
*Schriftlicher Ausdruck* — the one hand-written reply-letter/email). It teaches the format
and the exact telc grading rubric, hands you exam-format tasks, grades your letters the way
real telc graders do, drills the specific mistakes you keep making, and grows a tracked
bank of fluent B1 phrases until you own them. Goal: **pass**, not perfection.

> This is the *writing* half of the coach. The reading/listening/grammar/oral half lives in
> the companion skill **`telc-b1-exam`**, which hands off to this one whenever you work on
> the letter. Install both.

## Quick start
1. Install the skill (see the repo README for how, on Claude and other AIs).
2. Ask in plain language or use a command — e.g. *"give me a B1 writing task"*, paste a
   letter and ask *"would this pass?"*, or type `/written-grade`.

## Commands (cheat-sheet)
| Command | Use it to |
|---|---|
| `/written-teach [focus]` | Learn the format, rubric, letter templates, Redemittel, common mistakes, timing, or the pre-submit checklist. |
| `/written-examine` | Get **one** task in exact telc B1 format (scenario + received letter + 4 Leitpunkte). No help while you write. |
| `/written-grade` | Grade a letter by the real telc rubric: "would this pass?", the /45 score, criterion breakdown, and the mistakes that cost points. |
| `/written-drill [category]` | Drill the *specific* error types you keep repeating (verb position, cases, register…), pulled from your history. |
| `/written-upgrade` | Turn a *correct-but-flat* letter into a fluent one — sentence-surgery moves for variety and better phrasing. |
| `[write "Jan"]` | Do the letter task from a specific practice exam and grade it. (This is the bridge from `telc-b1-exam`.) |

Bracket or slash, either works (`/written-grade` = `[written-grade]`), and plain language
triggers them too.

## How the letter is scored (why the coach is strict about some things)
- **One letter, 30 minutes, ~120–150 words, 4 Leitpunkte** — all four points must be
  addressed. Worth **45 points** (15% of the exam).
- Graded on three criteria (each A/B/C/D): **I** did you cover all 4 points · **II**
  structure, linking, and correct register (du/Sie, greeting, closing) · **III** grammatical
  accuracy.
- **The zero rule:** if criterion **I and/or III is a D**, the whole letter scores **0**.
  So covering all four points and staying comprehensible matters more than fancy language.
The coach walks these criteria explicitly on every grade — never a vibe score.

## The workflow that gets the most out of it
1. **`/written-teach format & rubric`** once, so you know the target.
2. **`/written-examine`** → write a letter under the 30-minute clock, no help.
3. **`/written-grade`** → get the /45 and the point-costing mistakes.
4. **`/written-drill`** → hammer the exact error types the grade exposed.
5. When your letters *pass* but read flat, **`/written-upgrade`** for fluency.
6. Repeat with a fresh `/written-examine`, or feed a real exam's letter via `[write "…"]`.

## Tips for best results
- **Always cover all four Leitpunkte**, even briefly — dropping one is a 6-mark swing;
  covering only one triggers the zero rule.
- **Keep sentences simple and correct** — a comprehensible B1 letter beats an ambitious
  broken one. Verb-position errors hurt far more than a wrong case ending.
- **Let it track your phrase bank and recurring mistakes** in memory, so drills stay
  aimed at *your* leaks and the phrases resurface until they're automatic.
- **Register is fixed by the scenario** (company/authority → `Sie`; friend → `du`) — get it
  right; it's scored under criterion II.

## What it needs
- Nothing beyond Claude and, ideally, the `telc-b1-exam` skill installed so the
  exam↔writing hand-off works.
- Optional: your own practice-exam PDFs, if you want it to pull real letter tasks from them.
