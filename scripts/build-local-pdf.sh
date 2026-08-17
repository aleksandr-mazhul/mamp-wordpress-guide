#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

TMP_DIR="$ROOT/tmp/pdfs"
OUT_DIR="$ROOT/output/pdf"
PDF_FILE="$OUT_DIR/01-wordpress-local-mamp.pdf"
CSS_FILE="$ROOT/scripts/pdf/guide.css"
COVER_FILE="$ROOT/scripts/pdf/cover.html"
HTML_FILE="$TMP_DIR/local.html"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

echo "==> Checking dependencies..."

if ! command -v pandoc >/dev/null 2>&1; then
  echo "Error: pandoc not found. Install with: brew install pandoc"
  exit 1
fi

if [ ! -x "$CHROME" ]; then
  echo "Error: Google Chrome not found at $CHROME"
  exit 1
fi

if [ ! -d "$ROOT/node_modules/@mermaid-js/mermaid-cli" ]; then
  echo "==> Installing npm dependencies..."
  PUPPETEER_SKIP_DOWNLOAD=true npm install
fi

export PUPPETEER_EXECUTABLE_PATH="${PUPPETEER_EXECUTABLE_PATH:-/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}"

mkdir -p "$TMP_DIR" "$OUT_DIR"

echo "==> Preparing markdown..."
python3 "$ROOT/scripts/pdf/prepare-local.py"

echo "==> Rendering mermaid diagrams..."
node "$ROOT/scripts/pdf/render-mermaid.js"

echo "==> Building HTML..."
pandoc "$TMP_DIR/local.md" \
  --standalone \
  --toc \
  --toc-depth=2 \
  --css "$CSS_FILE" \
  --include-before-body "$COVER_FILE" \
  --metadata lang=ru \
  --metadata title="WordPress на Mac через MAMP" \
  -o "$HTML_FILE"

echo "==> Generating PDF..."
"$CHROME" \
  --headless=new \
  --disable-gpu \
  --no-pdf-header-footer \
  --print-to-pdf="$PDF_FILE" \
  "file://$HTML_FILE"

if [ ! -f "$PDF_FILE" ]; then
  echo "Error: PDF was not created."
  exit 1
fi

PAGE_COUNT=""
if command -v pdfinfo >/dev/null 2>&1; then
  PAGE_COUNT="$(pdfinfo "$PDF_FILE" 2>/dev/null | awk '/Pages:/ {print $2}')"
fi

echo "==> Done: $PDF_FILE"
if [ -n "$PAGE_COUNT" ]; then
  echo "    Pages: $PAGE_COUNT"
fi
