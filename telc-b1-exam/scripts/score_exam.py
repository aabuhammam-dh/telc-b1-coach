#!/usr/bin/env python3
"""
score_exam.py — mandatory code-based grader for a telc Deutsch B1 practice exam.

WHY THIS EXISTS
---------------
Eyeballing a "correct vs. submitted" table drifts toward false agreement and has produced
fabricated scores. ALWAYS grade through this script. Transcribe the answer key into data
FIRST (before looking at the user's answers, so the correct column can't be contaminated),
verify the Hoeren +/- key against the zoomed answer-sheet image, then run this.

INPUT
-----
A JSON file (or the two dicts inline) with the answer KEY and the user's ANSWERS, each a
mapping from question number (as a string "1".."60") to the answer. Answer formats:
  - Leseverstehen T1 (1-5)   : a letter, e.g. "D"        (headline/topic match)
  - Leseverstehen T2 (6-10)  : "A" | "B" | "C"
  - Leseverstehen T3 (11-20) : a letter "a".."l" or "X"  (situation -> ad, or no match)
  - Sprachbausteine T1 (21-30): "a" | "b" | "c"
  - Sprachbausteine T2 (31-40): a letter "a".."o"        (word bank)
  - Hoerverstehen (41-60)    : "+" (richtig) | "-" (falsch)
Comparison is case-insensitive and whitespace-trimmed. "X"/"x" are treated the same.

JSON shape:
{
  "exam": "Jan",
  "key":     { "1": "D", "2": "G", ..., "60": "-" },
  "answers": { "1": "D", "2": "A", ..., "60": "+" }
}

USAGE
-----
  python3 score_exam.py path/to/exam.json
  python3 score_exam.py --template   # prints a blank JSON template to fill in

OUTPUT
------
Per-Teil correct counts, the raw x/60, the real telc weighted points (Lesen/75, SB/30,
Hoeren/75, objective/180), a list of every miss (with the correct answer), and the weak
Teile (<60%). Missing questions are reported, not silently skipped.
"""

import json
import sys

# (label, first_q, last_q, section)
TEILE = [
    ("Leseverstehen T1", 1, 5, "Leseverstehen"),
    ("Leseverstehen T2", 6, 10, "Leseverstehen"),
    ("Leseverstehen T3", 11, 20, "Leseverstehen"),
    ("Sprachbausteine T1", 21, 30, "Sprachbausteine"),
    ("Sprachbausteine T2", 31, 40, "Sprachbausteine"),
    ("Hoerverstehen T1", 41, 45, "Hoerverstehen"),
    ("Hoerverstehen T2", 46, 55, "Hoerverstehen"),
    ("Hoerverstehen T3", 56, 60, "Hoerverstehen"),
]

# telc B1 weighting: points per correct item, by section
POINTS_PER_ITEM = {
    "Leseverstehen": 75 / 20,     # 3.75
    "Sprachbausteine": 30 / 20,   # 1.50
    "Hoerverstehen": 75 / 20,     # 3.75
}
SECTION_MAX = {"Leseverstehen": 75, "Sprachbausteine": 30, "Hoerverstehen": 75}


def norm(v):
    if v is None:
        return None
    s = str(v).strip()
    if s == "":
        return None
    return "X" if s.upper() == "X" else s.upper()


def grade(key, answers):
    key = {str(k): v for k, v in key.items()}
    answers = {str(k): v for k, v in answers.items()}

    teil_rows = []
    misses = []
    missing_answers = []
    missing_key = []
    section_correct = {"Leseverstehen": 0, "Sprachbausteine": 0, "Hoerverstehen": 0}

    total_correct = 0
    total_items = 0

    for label, lo, hi, section in TEILE:
        correct = 0
        items = 0
        for q in range(lo, hi + 1):
            qs = str(q)
            k = norm(key.get(qs))
            a = norm(answers.get(qs))
            if k is None:
                missing_key.append(q)
                continue
            items += 1
            total_items += 1
            if a is None:
                missing_answers.append(q)
                misses.append((q, label, key.get(qs), "(blank)"))
                continue
            if a == k:
                correct += 1
            else:
                misses.append((q, label, key.get(qs), answers.get(qs)))
        total_correct += correct
        section_correct[section] += correct
        pct = (correct / items * 100) if items else 0.0
        teil_rows.append((label, correct, items, pct))

    return {
        "teil_rows": teil_rows,
        "misses": sorted(misses),
        "missing_answers": sorted(missing_answers),
        "missing_key": sorted(missing_key),
        "section_correct": section_correct,
        "total_correct": total_correct,
        "total_items": total_items,
    }


def render(result, exam_name=""):
    out = []
    title = f"telc B1 grading — {exam_name}" if exam_name else "telc B1 grading"
    out.append("=" * 60)
    out.append(title)
    out.append("=" * 60)

    out.append("\nPer-Teil:")
    out.append(f"  {'Teil':<22}{'score':>10}{'%':>8}   flag")
    for label, correct, items, pct in result["teil_rows"]:
        flag = "  <-- weak (<60%)" if items and pct < 60 else ""
        out.append(f"  {label:<22}{f'{correct}/{items}':>10}{pct:>7.0f}%{flag}")

    # section + weighted
    out.append("\nBy section (raw items and real telc points):")
    obj_pts = 0.0
    for section in ("Leseverstehen", "Sprachbausteine", "Hoerverstehen"):
        c = result["section_correct"][section]
        pts = c * POINTS_PER_ITEM[section]
        obj_pts += pts
        out.append(
            f"  {section:<18}{c:>3} correct  ->  {pts:>5.1f} / {SECTION_MAX[section]} pts"
        )
    out.append(f"  {'OBJECTIVE TOTAL':<18}{result['total_correct']:>3} correct  ->  "
               f"{obj_pts:>5.1f} / 180 pts")

    out.append(f"\nRaw item score: {result['total_correct']}/{result['total_items']}  "
               f"(proxy pass ~36/60)")
    out.append(f"Objective weighted: {obj_pts:.1f}/180 pts")
    out.append("Note: written pass = 135/225 and INCLUDES the 45-pt letter. "
               "To judge 'passing', add the Schreiben score (telc-b1-schreiben skill).")

    if result["misses"]:
        out.append("\nMisses (question: your answer -> correct):")
        for q, label, correct_ans, given in result["misses"]:
            out.append(f"  Q{q:<3} [{label}]  {given}  ->  {correct_ans}")
    else:
        out.append("\nNo misses — full marks on the objective sections.")

    if result["missing_answers"]:
        out.append(f"\n! No answer supplied for: {result['missing_answers']} "
                   f"(counted as blank/wrong)")
    if result["missing_key"]:
        out.append(f"! No key entry for: {result['missing_key']} "
                   f"(these questions were skipped — check the key transcription)")

    return "\n".join(out)


TEMPLATE = {
    "exam": "<name>",
    "key": {str(q): "" for q in range(1, 61)},
    "answers": {str(q): "" for q in range(1, 61)},
}


def main(argv):
    if len(argv) == 2 and argv[1] == "--template":
        print(json.dumps(TEMPLATE, indent=2, ensure_ascii=False))
        return 0
    if len(argv) != 2:
        print(__doc__)
        return 1
    with open(argv[1], encoding="utf-8") as f:
        data = json.load(f)
    result = grade(data["key"], data["answers"])
    print(render(result, data.get("exam", "")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
