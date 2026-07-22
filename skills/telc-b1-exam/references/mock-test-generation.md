# Generating original telc-B1-format practice tests

This is the spec the `[mock exam]` command follows to produce a **fresh, original** practice
test in the telc Deutsch B1 *format* — for learners who don't have their own practice PDFs,
or who want unlimited extra material. Format calibrated to real exams; **text written from
scratch every time.**

## ⚠️ Originality & copyright rules (read first — this repo is public)

The telc B1 exam **format** (section order, item counts, task types, difficulty band) is a
method/structure and is fine to imitate. The **specific text** of any real exam — reading
passages, question wording, answer options, listening scripts, ad wording — is copyrighted
telc GmbH material and must **never** be reproduced.

When generating a test, Claude MUST:
- **Write every passage, item, option, and script from scratch.** Invent new characters,
  places, companies, dates, and situations. No sentence should be copyable back to a real
  exam.
- Use real exams (if the user has any) **only to observe format and difficulty** — never as
  a text source to copy, translate, or lightly reskin. "Inspired by" = same *shape and
  level*, new *content*.
- Avoid real brand names, real people, and real telc passage topics reproduced verbatim.
  Use invented but realistic names (e.g. *Frau Berger*, *Sprachschule Lindenhof*).
- If ever unsure whether something echoes a real item too closely, change it.

This keeps both the generated material **and this repository** free of third-party
copyrighted content. Everything the generator emits is new, original work.

### Using web_search to ground generation (optional) — and how to stay legal
Web search can make generated material more authentic, but **"freely available on the
internet" does NOT mean "free to copy."** Almost all web content is copyrighted by default;
reproducing it into a shared or public test is the same infringement problem with a
different owner. Use it like this:
- ✅ **Ground & calibrate.** Search to confirm the current telc format and difficulty, the
  common exam topics, and *natural, current German* (authentic vocabulary/collocations) —
  then **write your own items** from that understanding.
- ✅ **Novelty check.** If unsure whether a generated passage echoes a known text, search a
  distinctive phrase from it; if it matches a published source, rewrite it. This is the
  closest thing to an actual check on accidental copying (the guardrail above is otherwise
  just an instruction).
- ✅ **Reproduce only what's free to reuse.** You may adapt/reproduce text **only** if it's
  genuinely public-domain or under an open licence (CC0/CC-BY, license-free public-sector
  text) — and then attribute per that licence.
- ❌ **Never** copy or lightly reskin ordinary web content (blogs, textbooks, other practice
  tests, news articles) into the output.
Default remains: **write from scratch; treat the web as reference/signal, not a copy
source.**

---

## The blueprint (structure to match; content is always new)

Numbering runs 1–60 so results can be graded with `scripts/score_exam.py`.

| Section | Items | Task | Options / answer form | Notes |
|---|---|---|---|---|
| Leseverstehen T1 | 1–5 | Match 5 short texts to headings | headings **a–j** (10; ~5 unused) | global gist |
| Leseverstehen T2 | 6–10 | MC on one longer text | **A / B / C** | detail |
| Leseverstehen T3 | 11–20 | Match 10 situations to small ads | ads **a–l** (12) **+ X** | selective; ~1–2 genuine X |
| Sprachbausteine T1 | 21–30 | Cloze in a letter/email | **a / b / c** | grammar |
| Sprachbausteine T2 | 31–40 | Cloze with a word bank | bank **a–o** (15; 5 unused) | vocab/connectors in context |
| Hörverstehen T1 | 41–45 | 5 short texts, "heard once" | **+ / −** (richtig/falsch) | see listening note |
| Hörverstehen T2 | 46–55 | 1 conversation, "heard twice" | **+ / −** | detail; track who says what |
| Hörverstehen T3 | 56–60 | 5 announcements, "heard twice" | **+ / −** | selective detail |
| Schriftlicher Ausdruck | — | 1 letter task | (task only) | **grade via telc-b1-schreiben** |

The generator can produce the **full 60-item test**, or **one section** on request
(`[mock exam Lesen]`, `[mock exam Sprachbausteine]`, `[mock exam Hören]`).

### Listening is text, not audio
The real Hörverstehen is audio (T1 once, T2/T3 twice). Claude can't play audio, so it
generates **scripts** and runs them as a simulation: present the statements, then reveal the
script (or read it out turn-by-turn), enforcing "once vs. twice" by how many times it shows.
Always label this a **text approximation** of the listening section.

## B1 difficulty calibration (keep it authentic — not too easy, not C1)
- Sentences mostly short-to-medium; one subordinate clause at a time; avoid dense nominal
  style. Everyday + semi-formal register.
- High-frequency vocabulary on the common topics (below); gloss nothing inside the test.
- Reading texts ~120–200 words (T2 longer); ads terse and telegraphic; conversation natural.
- Grammar in the SB gaps must sit in the B1 in-scope set (see
  `grammar-for-sprachbausteine.md`) — prepositions+case, connectors, Konjunktiv II,
  reflexive verbs, relative pronouns, tense/verb forms.

## Topic pool (rotate; don't reuse one topic across sections in the same test)
Housing/WG · work & jobs · job applications · appointments · health/doctor · courses &
language learning · shopping & complaints · transport · travel · family · free time ·
environment · media/internet · neighbours · invitations & celebrations · everyday problems.
(Full seed lists in `vocabulary-by-topic.md`.)

## Embed the authentic traps (so practice is realistic)
Pull from the trap taxonomy in `section-strategies.md`, written as **new** items:
- **Lesen T1:** one keyword-echo distractor heading; one too-broad heading.
- **Lesen T2:** a comparison-direction option; a half-true option.
- **Lesen T3:** for each situation, a genuine match plus a near-miss decoy; include **1–2
  situations with no valid match (answer X)** — but never more, and never make X the lazy
  default.
- **SB T1:** at least two preposition+case gaps and one connector-choice gap; one
  reflexive-verb or Konjunktiv II gap.
- **SB T2:** 3–4 gaps that are connectors/collocations; keep 5 plausible decoys in the bank.
- **Hören (all):** at least one **setup→twist** statement (meaning flips after
  *aber/doch/eigentlich*); at least one **negation/qualifier** trap (*erst, nur, alle vs.
  die meisten*); at least one **similar-number** trap in T3.

## Answer key — emit in `score_exam.py` JSON
After the test, output a key the user can self-check, then grade with the script:
```json
{ "exam": "Mock-<topic>-<date>",
  "key":     { "1": "D", "…": "…", "60": "-" },
  "answers": { "1": "", "…": "", "60": "" } }
```
Answer forms by section: T1 = heading letter (a–j) · T2 = A/B/C · T3 = ad letter (a–l) or X ·
SB T1 = a/b/c · SB T2 = word-bank letter (a–o) · Hören = + / −.

## Workflow when the user runs `[mock exam]`
1. Ask **full test or one section**, and optionally a **topic/theme** (buttons if available).
2. If the user has exam PDFs and wants calibration, skim them for *format/difficulty only*
   (never to copy text).
3. Generate the original material section by section. Present the test **without the key**
   first so they can actually sit it; withhold answers until they've attempted it (or run it
   as a timed simulation like `[retake]`).
4. Provide the key + `score_exam.py` JSON; offer to grade, then run `[weaknesses]` and build
   `[practice]` drills from the misses.
5. For the **writing** section, generate only the *task* and hand grading to the
   `telc-b1-schreiben` skill (or call its `/written-examine`).

---

## Original worked mini-examples (Claude's own content — the quality target)

*These are illustrative originals. Generate new ones each time; never reuse these verbatim.*

### Leseverstehen T3 — 2 situations, ads a–c (+ X)
Situations:
1. Sie möchten am Wochenende einen Kochkurs für vegetarische Gerichte besuchen.
2. Sie suchen für Ihre Tochter (10) einen Schwimmkurs am Nachmittag.

Ads:
- **a)** *Kochstudio Lindenhof:* Vegetarisch kochen — Kurse samstags 10–14 Uhr. Anmeldung
  unter … .
- **b)** *Stadtbücherei:* Lesenachmittag für Kinder, mittwochs 15 Uhr.
- **c)** *Schwimmbad Ostpark:* Anfängerkurse für Erwachsene, montags abends.

Key: **1 → a** · **2 → X** (no afternoon children's swim course; ad c is adults/evening — a
near-miss). *Trap: c echoes "Schwimm-" but fails on age and time.*

### Sprachbausteine T1 — 2 gaps (a/b/c) + key
> Liebe Frau Berger, ich interessiere mich **(1)** die freie Wohnung. Ich würde sie gern
> ansehen, **(2)** ich zurzeit viel arbeite. Passt Samstag?

- (1) a) für b) auf c) an → **a) für** *(sich interessieren **für** — verb+preposition)*
- (2) a) weil b) obwohl c) deshalb → **b) obwohl** *(concession; verb-to-end — contrast with
  the cause reading that "weil" would force)*

### Hörverstehen T1 — script + statement (setup→twist) + key
Script (voicemail): *"Hallo, hier ist Tom. Wegen morgen — eigentlich wollte ich absagen,
weil ich Termine hatte. Aber die wurden verschoben, also komme ich doch."*
Statement 41: *Tom kann morgen nicht kommen.* → **−** (falsch). *Trap: the first clause says
he'd cancel; the meaning flips after "Aber … also komme ich doch."*
