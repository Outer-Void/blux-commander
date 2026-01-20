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
for dir in blux_commander tests src app packages lib; do
  if [[ -d "$dir" ]]; then
    code_dirs+=("$dir")
  fi
done

exec_pattern='\bsubprocess\b|os\.system|exec\(|\bspawn\b|\bshell\b|child_process|pexpect|paramiko|\bsudo\b|\bsu\b'
enforcement_pattern='\benforce\b|\ballow\b|\bblock\b|\bdeny\b|\bdecision\b|\bpolicy_engine\b|\bmoderation\b'
trust_pattern='\btoken\b|\bcapability_token\b|\bsignature\b|\bverify\b|\bkey_id\b|\brevocation\b'
contracts_pattern='/contracts/|envelope\.schema\.json|guard_receipt\.schema\.json|discernment_report\.schema\.json'

if [[ "${#code_dirs[@]}" -gt 0 ]]; then
  if rg -n -S -i "$exec_pattern" --glob '!.git/**' "${code_dirs[@]}"; then
    report_error "Found command-execution primitives in code directories."
  fi

  if rg -n -S -i "$enforcement_pattern" --glob '!.git/**' "${code_dirs[@]}"; then
    report_error "Found enforcement or decision keywords in code directories."
  fi

  if rg -n -S -i "$trust_pattern" --glob '!.git/**' "${code_dirs[@]}"; then
    report_error "Found token or trust keywords in code directories."
  fi
fi

if rg -n -S -i "$contracts_pattern" --glob '!.git/**' --glob '!scripts/physics_tests.sh' .; then
  report_error "Found contract schema artifacts or /contracts/ paths."
fi

if find . -type f \( -path "*/engine/*" -o -path "*/runner/*" -o -path "*/executor/*" -o -path "*/sandbox/*" \) -not -path "./.git/*" -print -quit | grep -q .; then
  report_error "Found files under execution-oriented paths (engine/, runner/, executor/, sandbox/)."
fi

if [[ "$fail" -ne 0 ]]; then
  echo "Physics tests failed." >&2
  exit 1
fi

echo "Physics tests passed."
