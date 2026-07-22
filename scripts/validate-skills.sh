#!/usr/bin/env bash
# Validate every skill's SKILL.md against the Agent Skills spec.
# Hard failures -> exit 1. Warnings -> reported, non-fatal.
# Self-contained: no external dependencies beyond coreutils + awk.
set -u

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SKILLS_DIR="$ROOT/skills"
errors=0
warnings=0

err()  { printf '  [ERROR] %s\n' "$1"; errors=$((errors + 1)); }
warn() { printf '  [warn]  %s\n' "$1"; warnings=$((warnings + 1)); }
ok()   { printf '  [ok]    %s\n' "$1"; }

if [ ! -d "$SKILLS_DIR" ]; then
  echo "No skills/ directory found at $SKILLS_DIR"
  exit 1
fi

found=0
for dir in "$SKILLS_DIR"/*/; do
  [ -d "$dir" ] || continue
  found=$((found + 1))
  skill="$(basename "$dir")"
  file="${dir}SKILL.md"
  echo "* $skill"

  if [ ! -f "$file" ]; then
    err "$skill: missing SKILL.md"
    continue
  fi

  # Frontmatter = lines between the first two '---' markers.
  fm="$(awk 'NR==1 && $0=="---"{f=1; next} f && $0=="---"{exit} f{print}' "$file")"
  if [ -z "$fm" ]; then
    err "$skill: no YAML frontmatter"
    continue
  fi

  # --- name ---
  name="$(printf '%s\n' "$fm" | sed -n 's/^name:[[:space:]]*//p' | head -1 | tr -d '"' | tr -d '[:space:]')"
  if [ -z "$name" ]; then
    err "$skill: frontmatter missing 'name'"
  else
    [ "$name" = "$skill" ] || err "$skill: name '$name' must match folder name '$skill'"
    printf '%s' "$name" | grep -Eq '^[a-z0-9]+(-[a-z0-9]+)*$' \
      || err "$skill: name '$name' must be lowercase a-z/0-9/hyphens (no leading/trailing/double hyphen)"
    [ "${#name}" -le 64 ] || err "$skill: name exceeds 64 characters"
  fi

  # --- description (supports folded '>-' block scalar) ---
  desc="$(printf '%s\n' "$fm" | awk '
    /^description:/{cap=1; sub(/^description:[[:space:]]*>?-?[[:space:]]*/,""); if($0!="") print; next}
    cap && /^[[:space:]]+/{sub(/^[[:space:]]+/,""); print; next}
    cap && /^[^[:space:]]/{cap=0}
  ' | tr '\n' ' ' | sed 's/  */ /g; s/^ //; s/ *$//')"
  if [ -z "$desc" ]; then
    err "$skill: frontmatter missing 'description'"
  else
    len=${#desc}
    if [ "$len" -gt 1024 ]; then
      err "$skill: description is $len chars (max 1024)"
    else
      ok "$skill: name + description valid (description ${len} chars)"
    fi
  fi

  # --- body length (recommend < 500 lines) ---
  lines="$(wc -l < "$file" | tr -d ' ')"
  [ "$lines" -lt 500 ] || warn "$skill: SKILL.md is $lines lines (recommend < 500; move detail into references/)"
done

[ "$found" -gt 0 ] || err "No skill folders found under skills/"

# --- JSON manifests (if present) ---
for j in "$ROOT/.claude-plugin/plugin.json" "$ROOT/.claude-plugin/marketplace.json"; do
  [ -f "$j" ] || continue
  rel="${j#"$ROOT"/}"
  if command -v python3 >/dev/null 2>&1; then
    python3 -c "import json,sys; json.load(open(sys.argv[1]))" "$j" >/dev/null 2>&1 \
      && ok "valid JSON: $rel" || err "invalid JSON: $rel"
  fi
done

echo
echo "Result: ${errors} error(s), ${warnings} warning(s)."
[ "$errors" -eq 0 ] || exit 1
