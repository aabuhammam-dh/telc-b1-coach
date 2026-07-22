# Contributing to telc B1 Coach

Thanks for helping make this a better study aid! Contributions of all sizes are welcome —
fixing a grammar explanation, improving a drill, adding a phrase, or sharpening the docs.

## Repository layout

```
telc-b1-coach/
├── skills/
│   ├── telc-b1-exam/         # exam practice, grading, speaking, mock generation
│   │   ├── SKILL.md          # entry point (YAML frontmatter + instructions)
│   │   ├── references/       # loaded on demand
│   │   ├── scripts/          # e.g. score_exam.py
│   │   └── assets/
│   └── telc-b1-schreiben/    # written-letter coaching
├── docs/                     # translated READMEs (README.<lang>.md)
├── README.md                 # English landing page (source of truth for translations)
└── scripts/validate-skills.sh
```

## Adding or editing a skill

1. A skill is a folder under `skills/` whose entry point is `SKILL.md`.
2. `SKILL.md` frontmatter must include:
   - `name` — lowercase letters, digits, hyphens; **must match the folder name**; ≤ 64 chars.
   - `description` — ≤ 1024 chars, third person, saying **what it does and when to trigger it**
     (list the exact commands and natural phrases users say). This drives activation accuracy.
3. Keep `SKILL.md` **under 500 lines**. Move long material into `references/*.md` and point to it
   by relative path so it loads only when needed.
4. Run the validator before opening a PR:
   ```bash
   ./scripts/validate-skills.sh
   ```

## Translations

`README.md` (English) is the source of truth. If you change it, update each
`docs/README.<lang>.md` and bump its `<!-- Translated from README.md at commit … -->` marker.
Keep code, commands, badges, links, and the Mermaid diagram byte-identical across languages —
translate prose only.

## Pull request flow

1. Fork → branch (`git checkout -b my-change`).
2. Make the change; run `./scripts/validate-skills.sh` (and, if you can, test the skill live in
   Claude Code or the Claude app).
3. Open a PR filling in the template checklist.

## What not to commit

Never commit copyrighted telc exam material (PDFs, scans, exam text). The skills only ever
*read* exams you supply locally; `.gitignore` already blocks `*.pdf`, `exams/`, etc.

## License

By contributing, you agree your contributions are licensed under the repository's
[MIT License](LICENSE).
