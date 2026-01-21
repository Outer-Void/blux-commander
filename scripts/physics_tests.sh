#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
cd "$ROOT_DIR"

fail=0

report_error() {
  echo "ERROR: $1" >&2
  fail=1
}

code_dirs=()
for dir in blux_commander tests scripts src app packages lib; do
  if [[ -d "$dir" ]]; then
    code_dirs+=("$dir")
  fi
done

exec_pattern='\bsubprocess\b|os\.system|exec\(|\bpopen\b|shell=True|child_process'
control_plane_pattern='["'\'']/(dispatch|run|execute|apply|mutate|approve|deny|issue|verify)\b'
enforcement_pattern='\benforce\b|\ballow\b|\bblock\b|\bdeny\b|\bdecision\b|\bpolicy_engine\b|\bmoderation\b'
trust_pattern='\btoken\b|\bcapability_token\b|\bsignature\b|\bverify\b|\bkey_id\b|\brevocation\b'
sibling_role_pattern='\bblux_guard\b|\bblux_lite\b|\bblux_reg\b|doctrine\.engine|doctrine_engine'

if [[ "${#code_dirs[@]}" -gt 0 ]]; then
  if rg -n -S -i "$exec_pattern" --glob '!.git/**' --glob '!scripts/physics_tests.sh' "${code_dirs[@]}"; then
    report_error "Found command-execution primitives in code directories."
  fi

  if rg -n -S -i "$control_plane_pattern" --glob '!.git/**' --glob '!scripts/physics_tests.sh' "${code_dirs[@]}"; then
    report_error "Found control-plane verbs in code paths."
  fi

  if rg -n -S -i "$enforcement_pattern" --glob '!.git/**' "${code_dirs[@]}"; then
    report_error "Found enforcement or decision keywords in code directories."
  fi

  if rg -n -S -i "$trust_pattern" --glob '!.git/**' "${code_dirs[@]}"; then
    report_error "Found token or trust keywords in code directories."
  fi

  if rg -n -S -i "$sibling_role_pattern" --glob '!.git/**' "${code_dirs[@]}"; then
    report_error "Found sibling-role or doctrine engine identifiers in code directories."
  fi
fi

if find . -type f -name "*.schema.json" -not -path "./.git/*" -not -path "./tests/fixtures/*" -print -quit | grep -q .; then
  report_error "Found local copies of contract schemas (*.schema.json)."
fi

if find . -type f \( -path "*/engine/*" -o -path "*/runner/*" -o -path "*/executor/*" -o -path "*/sandbox/*" \) -not -path "./.git/*" -print -quit | grep -q .; then
  report_error "Found files under execution-oriented paths (engine/, runner/, executor/, sandbox/)."
fi

if [[ "$fail" -ne 0 ]]; then
  echo "Physics tests failed." >&2
  exit 1
fi

echo "Physics tests passed."
