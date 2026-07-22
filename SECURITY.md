# Security Policy

## Reporting a vulnerability

If you find a security issue, please **do not open a public issue**. Instead, use GitHub's
private [**Report a vulnerability**](https://github.com/aabuhammam-dh/telc-b1-coach/security/advisories/new)
flow, or email **abdulla.abuhammam@gmail.com**. You'll get a response within a few days.

## Scope / what to keep in mind

These skills are plain Markdown instructions plus one helper script
(`skills/telc-b1-exam/scripts/score_exam.py`). Relevant considerations:

- **Executable content:** `score_exam.py` is the only executable file. Review it before running
  in an environment where code execution is enabled. It performs offline scoring only — no
  network calls, no file writes outside its working directory.
- **No secrets or personal data** are stored in this repo. The skills do not require API keys.
- **Your practice exams stay local:** the skills only *read* exam files you provide; nothing is
  uploaded or committed (see `.gitignore`).

## Supported versions

The latest release on `main` is supported. Older tags are not maintained.
