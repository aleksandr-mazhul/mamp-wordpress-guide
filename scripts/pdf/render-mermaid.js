#!/usr/bin/env node
/**
 * Render mermaid .mmd files to PNG using @mermaid-js/mermaid-cli.
 * Usage: node render-mermaid.js [mermaid-dir]
 */

const { execFileSync } = require("child_process");
const fs = require("fs");
const path = require("path");

const ROOT = path.resolve(__dirname, "../..");
const MERMAID_DIR = path.resolve(
  ROOT,
  process.argv[2] || "tmp/pdfs/mermaid"
);
const MMDC = path.join(ROOT, "node_modules/.bin/mmdc");

if (!fs.existsSync(MMDC)) {
  console.error("mmdc not found. Run: npm install");
  process.exit(1);
}

if (!fs.existsSync(MERMAID_DIR)) {
  console.log(`Mermaid dir not found: ${MERMAID_DIR}`);
  process.exit(0);
}

const files = fs
  .readdirSync(MERMAID_DIR)
  .filter((f) => f.endsWith(".mmd"))
  .sort();

if (files.length === 0) {
  console.log("No mermaid files to render.");
  process.exit(0);
}

for (const file of files) {
  const input = path.join(MERMAID_DIR, file);
  const output = path.join(MERMAID_DIR, file.replace(/\.mmd$/, ".png"));
  console.log(`Rendering ${file} -> ${path.basename(output)}`);
  execFileSync(
    MMDC,
    [
      "-i",
      input,
      "-o",
      output,
      "-b",
      "white",
      "-w",
      "800",
      "--scale",
      "2",
    ],
    { stdio: "inherit", env: { ...process.env } }
  );
}

console.log(`Rendered ${files.length} diagram(s).`);
