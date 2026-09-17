#!/usr/bin/env bash
# Thin wrapper → companion rql-repro download script (keeps binaries out of research repo).
set -euo pipefail
REPRO="${RQL_REPRO:-/workspace/rql-repro}"
SCRIPT="$REPRO/datasets/scripts/download_sift1m.sh"
if [[ ! -x "$SCRIPT" ]]; then
  echo "ERROR: companion script not found: $SCRIPT" >&2
  echo "Clone/checkout vijaykumarjob0701/rql-repro or set RQL_REPRO=" >&2
  exit 1
fi
exec bash "$SCRIPT" "$@"
