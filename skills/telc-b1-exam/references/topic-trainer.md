# Topic trainer — teach & test the high-frequency B1 topics

This is the spec for the `[topic]` command: a **standalone teach-then-test** loop on the
grammar, connector, and vocabulary topics that matter most for the telc B1 exam — not tied
to any single exam. It reuses the material already in the other references and is
**personalised** from what the coach tracks about the user (their misses and progress).

Three modes:
- **`[topic]`** (no name) → show the **readiness map** (what's ready / shaky / not started)
  and **recommend the highest-value topic to train**, based on the user's tracked weaknesses.
- **`[topic "<name>"]`** → **teach** that topic, then **test readiness**, then **log** it.
- **`[topic "<name>" test]`** → skip teaching, go straight to the readiness check.

Natural language triggers it too: "teach me the two-way prepositions", "quiz me on
connectors", "am I ready on Konjunktiv II?", "check my housing vocabulary".

## The high-frequency topic menu (what can be trained, and where its material lives)

**Grammar** → `grammar-for-sprachbausteine.md`
- Two-way prepositions + case (wo? = dative / wohin? = accusative)
- Verb + preposition chunks (+ da-compounds: *denken an → daran*)
- Connectors & word order (also `connectors-bank.md`)
- Konjunktiv II — polite (*hätte, wäre, könnte, würde, sollte*)
- Perfekt vs. Präteritum (incl. the *haben/sein* choice)
- Reflexive verbs (+ their fixed prepositions; reflexive Perfekt *hat sich …*)
- Relative pronouns (case from the job in the clause)
- Verb position (main = 2nd · subordinate = end · inversion after a fronted element)
- Adjective endings (light touch — the common pattern only)

**Connectors** → `connectors-bank.md`
- The contrast pairs the exam loves: *weil/deshalb, obwohl/trotzdem, als/wenn, dass/ob,
  denn/weil* — meaning + word-order class.

**Vocabulary** → `vocabulary-by-topic.md`
- The recurring telc themes: housing, work & applications, health/doctor, travel/transport,
  shopping/complaints, courses/language learning, invitations/celebrations, neighbours,
  family, free time, environment, media/internet.

## The teach → test → verdict → log loop

1. **Recommend / confirm the topic.** If `[topic]` with no name, read the user's tracked
   weaknesses and readiness map and propose the topic that's costing the most points (e.g.
   recurring SB T2 connector misses → recommend **connectors**). Offer the menu (buttons if
   available).
2. **Teach it — briefly and grounded.** Follow the **search-first rule**: web-search a
   reputable German-grammar source first, then teach in the standard format — *rule in plain
   English → 3 German examples with glosses → the common mistake → the exam shortcut → a 3–5
   item mini-drill.* Pull in the user's **known errors on this topic** and any **in-progress
   items** so the teaching targets their actual gaps, not the generic case.
3. **Test readiness.** Give a short **original** quiz (see originality note) of **5–8 items**
   in telc style:
   - grammar/connectors → SB-style cloze (a/b/c) or word-bank gaps, embedding the real trap
     types (preposition+case, connector-logic-then-word-order, Konjunktiv II, reflexive);
   - vocabulary → DE→EN recall or gap-in-context, mixing must-know items with near-synonym
     decoys.
   Present items **without answers first**, let the user attempt, then reveal the key.
4. **Verdict.** Score correct/total and give a clear level:
   - **✅ Ready** ≥ 80% · **🟡 Shaky** 50–79% · **🔴 Not ready** < 50%.
5. **Log & loop.** Update the **readiness map** in memory (below). If not ✅, re-teach the
   specific sub-point that was missed and offer one more short check; feed the misses into
   the weakness profile so `[practice]` and `[weaknesses]` stay aligned.

## Readiness map (track in memory; this is the "progress" the user asked for)
Keep a per-topic status so progress compounds and `[topic]` can recommend well:
- **🔴 not started** · **🟡 learning / shaky** (attempted, not yet ≥80%) · **✅ ready**
  (scored ≥80% unprompted) — with the **date last checked**.
Resurface 🟡 topics in future sessions; re-test a ✅ topic occasionally so it doesn't go
stale before exam day. Mirror this with the Schreiben skill's phrase-mastery convention so
the two feel consistent.

## Personalisation sources (what makes this better than a generic quiz)
- **Tracked weaknesses** (from graded exams / `error-patterns-and-drills.md`) → which topic
  to recommend and which traps to weight in the readiness test.
- **Extracted material** (from `[extract]`) → real vocab/connectors/grammar the user has
  actually seen, so training reflects their exams.
- **Readiness map + progress** → don't re-teach what's ✅; focus time on 🔴/🟡.

## Originality note (repo is public)
Any quiz items the trainer generates follow the same rule as `mock-test-generation.md`:
**write items from scratch**, invent names/places, never reproduce or lightly reskin real
telc exam text. Format may be imitated; text may not.

## Tiny worked readiness-check (original — the quality target; generate new ones each time)
Topic: **two-way prepositions + case.** Choose a/b/c:
1. Ich hänge das Bild ___ die Wand. — a) an der b) an die c) am → **b) an die** *(movement →
   accusative)*
2. Das Buch liegt ___ dem Tisch. — a) auf b) auf den c) auf das → **a) auf** (+ dative;
   *dem* already shows it) *(location → dative)*
3. Wir fahren am Wochenende ___ die Berge. — a) in den b) in die c) in der → **b) in die**
   *(movement → accusative, plural)*
Verdict example: 2/3 → 🟡 Shaky → re-teach *wohin? = accusative* with one more check.
