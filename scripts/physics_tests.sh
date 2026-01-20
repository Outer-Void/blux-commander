#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
cd "$ROOT_DIR"

fail=0

report_error() {
  echo "ERROR: $1" >&2
  fail=1
}

find_dir_hits() {
  local hits
  hits=$(find . \
    -path './.git' -prune -o \
    -path './.venv' -prune -o \
    -type d \( "$@" \) -print)
  if [[ -n "$hits" ]]; then
    printf '%s\n' "$hits"
  fi
}

boundary_hits=$(find_dir_hits \
  -iname executor \
  -o -iname execution \
  -o -iname runner \
  -o -iname 'control-plane' \
  -o -iname 'control_plane' \
  -o -path '*/src/executor')

if [[ -n "${boundary_hits:-}" ]]; then
  report_error "Found execution/control-plane directories:\n${boundary_hits}"
fi

guard_hits=$(find_dir_hits \
  -iname guard \
  -o -iname reg \
  -o -iname lite)

if [[ -n "${guard_hits:-}" ]]; then
  report_error "Found Guard/Reg/Lite directories:\n${guard_hits}"
fi

code_globs=(
  --glob '*.sh'
  --glob '*.py'
  --glob '*.js'
  --glob '*.ts'
  --glob '*.go'
  --glob '*.rs'
  --glob '*.java'
  --glob '*.kt'
  --glob '!scripts/physics_tests.sh'
)

exec_pattern='subprocess|child_process|exec\(|spawn\(|system\(|os\.exec|Runtime\.getRuntime|ProcessBuilder'
if rg -n "$exec_pattern" "${code_globs[@]}" .; then
  report_error "Found command-execution primitives in code files."
fi

secret_pattern='BEGIN PRIVATE KEY|AKIA[0-9A-Z]{16}|ASIA[0-9A-Z]{16}|AWS_SECRET_ACCESS_KEY'
if rg -n -S "$secret_pattern" --glob '!.git/**' .; then
  report_error "Found possible secret material in repository."
fi

if [[ "$fail" -ne 0 ]]; then
  echo "Physics tests failed." >&2
  exit 1
fi

echo "Physics tests passed."
