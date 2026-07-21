# Phrase mastery & fluency upgrade (telc B1 writing)

This file does two connected jobs:

1. **Run the user's personal phrase bank** — turn the "Memorise these phrases" sets
   into a *tracked, spaced inventory* that gets introduced, circulated through
   drills/teaching, and retired only when the user uses a phrase correctly **unprompted
   in a real letter**. This is the answer to "remember my phrases and weave them into
   training until I master them."
2. **Power `/written-upgrade`** — teach the user how to turn flat, correct-but-stubby
   B1 German into fluent B1 German, using a fixed set of safe "sentence-surgery" moves,
   and harvest the resulting frames into the phrase bank.

Explanations in English; all German at A2–B1. Strict, concrete, no filler.

**Why this matters (be honest with the user).** The letter caps at 45/45 and is only
15% of the written score; a user already scoring ~40 is not going to find big marginal
points by writing "more beautifully." The real payoff is different and worth stating:
a **memorised, automatic frame cannot contain a verb-position or case error**, so
building the phrase bank attacks the user's *remaining error leaks* from the production
side, it **saves time** in the 30-minute handwritten exam (content + checking instead
of grammar assembly), and the same frames **transfer to the Sprechen exam** (25% of
the grade). Frame the value that way — not as chasing a perfect letter.

---

## Part A — The personal phrase bank

### The mastery states
Every tracked phrase carries one status. Store these in the phrase-bank memory note.

- **🌱 New** — just harvested from a graded letter or a teach session; the user has
  *seen* it but not produced it. Next teach/drill introduces it with a model.
- **🔁 Learning** — the user has produced it at least once *with the phrase given to
  them* (in a drill, an upgrade, or a prompted exercise). Keep resurfacing it.
- **✅ Mastered** — the user produced it **correctly and unprompted in a real
  `/written-grade` letter** (not because they were told to use it). Retire it from
  active rotation; spot-check occasionally.

The retirement bar is deliberate: prompted use is *recognition*; unprompted use in a
real letter is *acquisition*. This mirrors how error patterns are retired in SKILL.md
(only after the user nails a harder, unfamiliar instance unprompted).

### Harvesting rules (keep the bank from flooding)
- After each `/written-grade`, harvest **only the 2–4 highest-leverage phrases**, not
  everything. Prioritise phrases that (a) **plug the user's current error leaks** —
  e.g. a ready-made frame that embodies the grammar they keep getting wrong, so they
  can memorise a correct sentence instead of re-deriving the rule — or (b) are
  **high-frequency across telc topics** (openings, reactions, requests, closings) and
  therefore reusable in many letters *and* in speaking.
- Keep the **active set (🌱 + 🔁) at ~6–10 phrases max.** If it's already full, don't
  add new ones until some graduate — tell the user the bank is full and focus on
  mastering what's in it. Cognitive load is the enemy of automaticity.
- Never duplicate. If a new phrase is a variant of one already tracked, update the
  existing entry rather than adding a near-copy.

### Circulation — every command feeds and draws from the bank
- **`/written-grade`** → *harvests* new phrases (status 🌱) **and** checks whether any
  🔁 phrase was used correctly and unprompted → promote to ✅ and tell the user it
  graduated. If a 🌱/🔁 phrase would have fit naturally but the user reached for a
  clunkier construction, gently point to the phrase they're supposed to be building.
- **`/written-teach`** → whatever the session is about, *pull in the user's 🔁 phrases*
  and show them in worked model sentences; always demonstrate the flat→fluent upgrade
  for the relevant function.
- **`/written-drill`** → include a **production section** built from the active bank:
  the point is to make the user *generate* the phrase, not recognise it. Formats:
  - *Situationskarte:* give a one-line situation → user replies using a named phrase.
  - *Stub-Upgrade:* give a flat sentence → user rewrites it with a phrase they're
    learning.
  - *Lücken-Redemittel:* a gap that only the target phrase fills.
- **`/written-upgrade`** → *harvests* every reusable frame it produces (status 🌱).

### Memory hygiene
Store the phrase bank as a single, scannable memory note, grouped by **function**
(opening/thanks · reaction/opinion · request · suggestion · apology/refusal · closing ·
leak-plugging frames), each phrase tagged with its status emoji. Update in place; keep
it de-duplicated; never store sensitive personal data or verbatim command dumps.

---

## Part B — Sentence surgery (the `/written-upgrade` engine)

The user's writing is typically **correct but flat**: short subject–verb–object
sentences, almost every one starting with *Ich*, no intensifiers, plain verbs. The gap
to fluent B1 is closed by a *fixed, safe repertoire of moves* — none require
above-B1 grammar. Teach and apply these explicitly.

### The 7 upgrade moves
1. **Merge stubs.** Join two short sentences with *und / aber / weil / deshalb / denn*
   so the letter stops reading like a list.
   *Ich finde die Idee gut. Ich mache gern mit.* → *Ich finde die Idee gut und mache
   gern mit.*
2. **Open with a reaction/opinion frame** instead of bare "Das ist …":
   *Ich finde deinen Vorschlag wirklich toll* · *Deine Idee gefällt mir sehr* ·
   *Das klingt super*.
3. **Add cheap intensifiers** — free, native-sounding, near-zero error risk:
   *wirklich, sehr gerne, schon lange, unbedingt, bisher, richtig, natürlich,
   eigentlich, total*. This is the single highest lift-per-effort move.
4. **Vary sentence openings.** Not every sentence starts with *Ich*. Front some with
   *Übrigens, Außerdem, Zum Glück*, a time phrase (*Nächste Woche …* — verb 2nd, then
   subject!), or the object. This kills most of the "flat" feeling on its own.
5. **Upgrade the verb/collocation** to a richer B1 choice:
   *sich etwas wünschen* > *haben wollen*; *sich melden* > *schreiben*;
   *erzählen* > *sagen*; *sich freuen auf/über* > *froh sein*;
   *etwas vorhaben* > *etwas machen wollen*.
6. **Reference their letter** (Adressatenbezug, scores Kriterium II directly):
   *Wie du schreibst, …* · *Du hast ja gefragt, ob …* · *Danke, dass du an mich
   gedacht hast.*
7. **End a point with a small forward/interactive touch**: a question (*Was hältst du
   davon?*), *das wäre super*, *dann können wir …*.

**Fastest wins to push first:** moves 3 (intensifiers) and 4 (varied openings) — low
effort, zero added error surface, immediate fluency lift. Moves 5–6 add the most
"native" feel but carry slightly more risk, so introduce them once 3–4 are habitual.

### The `/written-upgrade` procedure
1. **Get the raw text.** Either the user pastes a plain letter, or use their most
   recent `/written-grade` letter as the source. If there's **neither** (fresh chat, no
   pasted text), don't stall or fabricate a letter for them — ask them to paste one, or
   offer to demonstrate the moves on a short flat sample and then have them upgrade a
   couple of their own sentences.
2. **First, fix any outright errors** (briefly — this isn't a full grade; if they want
   scoring they'd use `/written-grade`). The upgrade works on a *correct* base.
3. **Sentence-by-sentence surgery.** For each sentence worth upgrading, show:
   *You wrote:* (their line) → *Upgraded:* (fluent B1 version) → **which move(s)** it
   used, in a few words. Keep the upgraded version genuinely B1 — do **not** drift into
   C1 subordination or rare vocabulary; the goal is reusable, memorable frames the user
   can actually reproduce under exam pressure. Credit moves they *already* did well
   (e.g. if they varied an opening) so they know what to keep.
4. **Give the fully upgraded letter** as one clean block so they see the cumulative
   effect.
5. **Harvest 2–4 transferable frames** into the phrase bank (status 🌱), chosen for
   reusability across topics and speaking — not one-off phrasings tied to this letter.
6. **One "now you try":** hand them 2–3 of their own flat sentences (or a fresh mini
   task) and have them apply a specific move themselves. Confirm before moving on.

### Scaffolded imitation (an option inside `/written-upgrade` or `/written-teach`)
To train *production* of fluent structure with training wheels:
- Take a strong model letter and **blank the content but keep the frames**, e.g.
  *„Ich finde deine Idee ____! Ich ____ schon lange ____, aber ____. Übrigens ____.“*
  The user fills in their own content, practising fluent scaffolding without having to
  invent the structure. Over successive letters, remove more of the frame until they
  build it unaided. This is the bridge between reading good models and producing them.

---

## Worked micro-example (shape only — always regenerate fresh)

> **Source (user):** *Das ist eine gute Idee. Ich komme gern. Ich habe nächste Woche
> Zeit.*
>
> **Surgery:**
> - *Das ist eine gute Idee.* → *Ich finde deine Idee wirklich gut!* (moves 2, 3)
> - *Ich komme gern. Ich habe nächste Woche Zeit.* → *Ich komme sehr gern, denn nächste
>   Woche habe ich sowieso Zeit.* (moves 1, 3, 4 — note verb-2nd after the fronted time
>   phrase: *nächste Woche **habe** ich*)
>
> **Upgraded block:** *Ich finde deine Idee wirklich gut! Ich komme sehr gern, denn
> nächste Woche habe ich sowieso Zeit.*
>
> **Harvest → bank (🌱):** „Ich finde deine Idee wirklich gut!" · „…, denn nächste
> Woche habe ich sowieso Zeit."
