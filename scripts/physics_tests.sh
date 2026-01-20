#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
cd "$ROOT_DIR"

fail=0

report_error() {
  echo "ERROR: $1" >&2
  fail=1
}

exec_pattern='child_process|exec\(|spawn\(|subprocess|os\.system|Runtime\.getRuntime|ProcessBuilder|bash -c|sh -c|powershell|cmd\.exe|sudo'
if rg -n -S "$exec_pattern" --glob '!.git/**' --glob '!scripts/physics_tests.sh' .; then
  report_error "Found command-execution primitives in repository."
fi

mutation_pattern='iptables|mount\\s|chroot|setcap|cap_net_admin|ptrace|/proc/|/sys/'
if rg -n -S "$mutation_pattern" --glob '!.git/**' --glob '!scripts/physics_tests.sh' .; then
  report_error "Found state-mutation intent in repository."
fi

role_dirs=()
for dir in src app packages lib; do
  if [[ -d "$dir" ]]; then
    role_dirs+=("$dir")
  fi
done

role_pattern='receipt engine|enforcement|policy engine|capability token|issue token|verify token|execute tool|runner|sandbox profile'
if [[ "${#role_dirs[@]}" -gt 0 ]]; then
  if rg -n -S -i "$role_pattern" "${role_dirs[@]}"; then
    report_error "Found role-bleed keywords in code directories."
  fi
fi

responsibility_pattern='\\bguard\\b|\\breg\\b|\\blite\\b'
if [[ "${#role_dirs[@]}" -gt 0 ]]; then
  if rg -n -S -i "$responsibility_pattern" "${role_dirs[@]}"; then
    report_error "Found Guard/Reg/Lite responsibility signals in code directories."
  fi
fi

if [[ "$fail" -ne 0 ]]; then
  echo "Physics tests failed." >&2
  exit 1
fi

echo "Physics tests passed."
