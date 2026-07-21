# telc B1 Coach — Claude Skills

Two companion [Claude Skills](https://docs.claude.com) that turn Claude into a strict,
exam-focused coach for the **telc Deutsch B1** exam (the general adult *Zertifikat Deutsch*
format — **not** the DTZ, and not Goethe B1). They're built for one goal: **passing**, with
exam strategy, pattern recognition, high-frequency language, and correction-heavy practice
on past papers.

| Skill | Covers | Trigger examples |
|---|---|---|
| **`telc-b1-exam`** | The objective sections — Leseverstehen, Sprachbausteine, Hörverstehen — plus the **mündliche Prüfung**, exam scoring, and the practice-on-past-papers workflow. | `[log exam]`, `[extract "Jan"]`, "grade my answers", "explain obwohl vs. trotzdem", "drill my Hörverstehen traps" |
| **`telc-b1-schreiben`** | The **written letter** (Schriftlicher Ausdruck) only — format, grading rubric, tasks, mistake drills, and a tracked bank of fluent B1 phrases. | `/written-grade`, "would this letter pass?", "give me a writing task", "correct my letter" |

**They pair automatically.** `telc-b1-exam` handles everything except the letter; when you
ask about writing (or run `[write "…"]`), it hands off to `telc-b1-schreiben`. Install both
for full coverage of the exam.

## What each skill does

**`telc-b1-exam`** — logs and grades your answers to a practice exam (via a code-based
scorer, not eyeballing), explains every miss with its trap type and the rule behind it,
mines vocabulary/connectors/grammar from a test, drills your weak points, simulates the
oral exam, and answers grammar questions by **searching a reputable German-grammar source
first** and grounding the explanation. Ships with a scoring script, a persistent logging
dashboard, and reference files for section strategy, grammar, connectors, the oral exam,
vocabulary, and error patterns. See [`telc-b1-exam/README.md`](telc-b1-exam/README.md) for
the full command list and the recommended study loop.

**`telc-b1-schreiben`** — teaches the letter format and the exact telc grading rubric,
generates exam-format tasks, grades letters the way telc graders do (including the "zero
rule"), drills the specific mistakes you keep making, and grows a tracked phrase bank until
those phrases are mastered.

## Install

These are Claude Skills. To use them with Claude:

1. Package a skill folder into a `.skill` file (or import the folder directly if your Claude
   surface supports it), then enable it in your Claude profile/settings.
2. Enable **both** skills so the exam ↔ writing hand-off works.

> Packaging tip: if you have the skill-creator tooling, run
> `python -m scripts.package_skill telc-b1-exam` to produce `telc-b1-exam.skill`.

## Repository layout

```
telc-b1-coach/
├── README.md               # this file
├── LICENSE                 # MIT — © 2026 Abdulla Abuhammam
├── .gitignore              # keeps exam PDFs and build artifacts out of git
├── telc-b1-exam/           # objective sections + oral coach
│   ├── SKILL.md
│   ├── README.md           # how to use this skill + command cheat-sheet
│   ├── references/         # strategy, grammar, connectors, oral, vocab, error patterns
│   ├── scripts/            # score_exam.py — the code-based grader
│   └── assets/             # pruefungsprotokoll.html — logging dashboard
└── telc-b1-schreiben/      # the letter-writing coach
    ├── SKILL.md
    └── references/          # rubric, templates, Redemittel, mistakes, drills, phrase bank
```

## Two notes for anyone cloning this

- **The exam PDFs are not included, by design.** The skills *reference* telc practice exams
  at runtime, but those are copyrighted telc GmbH material and must not be committed. Bring
  your own practice exams and point the skills at them. (`.gitignore` blocks `*.pdf`.)
- **Some paths assume a Claude project layout.** The skills read exams from `/mnt/project/`
  and the exam skill hands off to the writing skill at
  `/mnt/skills/user/telc-b1-schreiben/`. Those are correct inside the Claude environment
  where the skills run; adjust if your setup differs.

## Seed data

The skills ship with **seed content** — a starter weakness profile, example exam labels,
and a starter phrase bank — so they're useful from a cold start rather than empty. Claude
updates this from its own memory as you practise. No personal identifiers are included.

## License

MIT © 2026 Abdulla Abuhammam — see [`LICENSE`](LICENSE).
