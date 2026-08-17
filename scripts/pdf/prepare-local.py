#!/usr/bin/env python3
"""Prepare merged markdown for local guide PDF build."""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from prepare_common import OUT_DIR, GuideConfig, build_merged_md

ROOT = Path(__file__).resolve().parents[2]
DOCS_LOCAL = ROOT / "docs" / "local"


def simplify_pdf_tables(text: str) -> str:
    return re.sub(
        r"\| Шаг \| Файл \| Содержание \|\n\|-----+\|------+\|------------+\|\n"
        r"\| 1 \| \[01-before\.md\]\([^)]+\) \| ([^|]+) \|\n"
        r"\| 2 \| \[02-mamp\.md\]\([^)]+\) \| ([^|]+) \|\n"
        r"\| 3 \| \[03-wordpress\.md\]\([^)]+\) \| ([^|]+) \|\n"
        r"\| — \| \[troubleshooting\.md\]\([^)]+\) \| ([^|]+) \|",
        r"| Шаг | Содержание |\n|-----|------------|\n"
        r"| 1 | \1 |\n"
        r"| 2 | \2 |\n"
        r"| 3 | \3 |\n"
        r"| — | \4 |",
        text,
    )


def normalize_headings(text: str, filename: str) -> str:
    if filename == "README.md":
        text = re.sub(
            r"^# Часть 1: WordPress на Mac через MAMP\s*$",
            "# WordPress на Mac через MAMP",
            text,
            count=1,
            flags=re.MULTILINE,
        )
    if filename == "troubleshooting.md":
        text = re.sub(
            r"^# Решение проблем \(локально\)\s*$",
            "# Приложение: Решение проблем",
            text,
            count=1,
            flags=re.MULTILINE,
        )
    return text


def local_strip_rule(stripped: str) -> str | None:
    if "Часть 2: перенос на хостинг" in stripped:
        return (
            "> *Следующий гайд (отдельный PDF): "
            "«Перенос WordPress с localhost на хостинг»*"
        )
    if re.match(r"\[([^\]]+)\]\(02-mamp\.md\)", stripped):
        return None
    return None


def fix_step_links(text: str) -> str:
    return re.sub(r"\[([^\]]+)\]\(02-mamp\.md\)", r"\1 (шаг 2)", text)


def build() -> None:
    config = GuideConfig(
        source_files=[
            DOCS_LOCAL / "README.md",
            DOCS_LOCAL / "01-before.md",
            DOCS_LOCAL / "02-mamp.md",
            DOCS_LOCAL / "03-wordpress.md",
            DOCS_LOCAL / "troubleshooting.md",
        ],
        out_file=OUT_DIR / "local.md",
        mermaid_dir=OUT_DIR / "mermaid",
        title="WordPress на Mac через MAMP",
        expected_images=10,
        normalize_headings=normalize_headings,
        simplify_tables=simplify_pdf_tables,
        extra_strip_rules=[local_strip_rule],
        extra_text_fixes=[fix_step_links],
    )
    build_merged_md(config)


if __name__ == "__main__":
    build()
