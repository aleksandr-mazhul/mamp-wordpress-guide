#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

echo "==> Building Part 1: Local MAMP guide..."
bash "$ROOT/scripts/build-local-pdf.sh"

echo ""
echo "==> Building Part 2: Migrate guide..."
bash "$ROOT/scripts/build-migrate-pdf.sh"

echo ""
echo "==> Building Part 3: Hosting guide..."
bash "$ROOT/scripts/build-hosting-pdf.sh"

echo ""
echo "==> All PDFs ready in output/pdf/"
