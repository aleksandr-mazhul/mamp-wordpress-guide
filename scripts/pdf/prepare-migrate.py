#!/usr/bin/env python3
"""Prepare merged markdown for migrate guide PDF build."""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from prepare_common import OUT_DIR, GuideConfig, build_merged_md

ROOT = Path(__file__).resolve().parents[2]
DOCS_MIGRATE = ROOT / "docs" / "migrate"


def simplify_pdf_tables(text: str) -> str:
    return re.sub(
        r"\| Шаг \| Файл \| Содержание \|\n\|-----+\|------+\|------------+\|\n"
        r"\| 1 \| \[01-prepare\.md\]\([^)]+\) \| ([^|]+) \|\n"
        r"\| 2 \| \[02-hosting\.md\]\([^)]+\) \| ([^|]+) \|\n"
        r"\| 3 \| \[03-upload\.md\]\([^)]+\) \| ([^|]+) \|\n"
        r"\| 4 \| \[04-database\.md\]\([^)]+\) \| ([^|]+) \|\n"
        r"\| 5 \| \[05-configure\.md\]\([^)]+\) \| ([^|]+) \|\n"
        r"\| 6 \| \[06-check\.md\]\([^)]+\) \| ([^|]+) \|",
        r"| Шаг | Содержание |\n|-----|------------|\n"
        r"| 1 | \1 |\n"
        r"| 2 | \2 |\n"
        r"| 3 | \3 |\n"
        r"| 4 | \4 |\n"
        r"| 5 | \5 |\n"
        r"| 6 | \6 |",
        text,
    )


def normalize_headings(text: str, filename: str) -> str:
    if filename == "README.md":
        text = re.sub(
            r"^# Часть 2: Перенос с localhost на хостинг\s*$",
            "# Перенос WordPress с localhost на хостинг",
            text,
            count=1,
            flags=re.MULTILINE,
        )
    if filename == "appendix-ftp.md":
        text = re.sub(
            r"^# Приложение: загрузка через FTP \(FileZilla\)\s*$",
            "# Приложение A: загрузка через FTP (FileZilla)",
            text,
            count=1,
            flags=re.MULTILINE,
        )
    if filename == "appendix-plugin.md":
        text = re.sub(
            r"^# Приложение: перенос через плагин\s*$",
            "# Приложение B: перенос через плагин",
            text,
            count=1,
            flags=re.MULTILINE,
        )
    if filename == "troubleshooting.md":
        text = re.sub(
            r"^# Решение проблем \(перенос\)\s*$",
            "# Приложение C: Решение проблем",
            text,
            count=1,
            flags=re.MULTILINE,
        )
    return text


def migrate_strip_rule(stripped: str) -> str | None:
    if "Часть 3: Hosting" in stripped or "Часть 3:" in stripped:
        return (
            "> *Следующий гайд (отдельный PDF): "
            "«WordPress на хостинге с нуля» (Часть 3)*"
        )
    if re.match(r"^-\s+Сайт с нуля на хостинге", stripped):
        return None
    if re.match(r"^\*\*\[Начать шаг 1", stripped):
        return None
    return None


def fix_cross_part_links(text: str) -> str:
    text = re.sub(
        r"\(например после \[[^\]]+\]\(\.\./local/[^)]+\)\)",
        "(например после PDF «WordPress на Mac через MAMP», Часть 1)",
        text,
    )
    text = re.sub(
        r"\[([^\]]*)\]\(\.\./local/[^)]+\)",
        r"PDF «WordPress на Mac через MAMP» (Часть 1)",
        text,
    )
    text = re.sub(
        r"\[([^\]]*)\]\(\.\./hosting/[^)]+\)",
        r"PDF «WordPress на хостинге с нуля» (Часть 3)",
        text,
    )
    text = re.sub(
        r"\[шаги 1–6\]\(README\.md\)",
        "ручной путь (шаги 1–6)",
        text,
    )
    text = re.sub(
        r"\[шага (\d+)\]\(\d{2}-[a-z]+\.md\)",
        r"шага \1",
        text,
    )
    text = re.sub(
        r"\[([^\]]*)\]\((\d{2})-([a-z]+)\.md\)",
        lambda m: (
            f"{m.group(1).strip()} (шаг {int(m.group(2))})"
            if m.group(1).strip()
            else f"шаг {int(m.group(2))}"
        ),
        text,
    )
    text = re.sub(
        r"appendix-plugin\.md \(приложение B\)",
        "Приложение B",
        text,
    )
    text = re.sub(
        r"appendix-ftp\.md \(приложение A\)",
        "Приложение A",
        text,
    )
    text = re.sub(
        r"appendix-ftp \(приложение A\)",
        "Приложение A",
        text,
    )
    text = re.sub(
        r"\(шаг (\d{2})\)",
        lambda m: f"(шаг {int(m.group(1))})",
        text,
    )
    text = re.sub(
        r"\[FTP\]\(appendix-ftp\.md\)",
        "Приложение A (FTP)",
        text,
    )
    text = re.sub(
        r"\[appendix-ftp\]\(appendix-ftp\.md\)",
        "Приложение A",
        text,
    )
    text = re.sub(
        r"\[appendix-ftp\.md\]\(appendix-ftp\.md\)",
        "Приложение A",
        text,
    )
    text = re.sub(
        r"\[appendix-plugin\.md\]\(appendix-plugin\.md\)",
        "Приложение B",
        text,
    )
    text = re.sub(
        r"\[([^\]]+)\]\(05-configure\.md\)",
        r"\1 (шаг 5)",
        text,
    )
    text = re.sub(
        r"\[05-configure\.md\]\(05-configure\.md\)",
        "шаг 5",
        text,
    )
    text = re.sub(
        r"\[([^\]]+)\]\(README\.md\)",
        r"\1",
        text,
    )
    return text


def cleanup_migrate_artifacts(text: str) -> str:
    lines = []
    for line in text.splitlines():
        stripped = line.strip()
        if re.match(r"^\*\*Далее:", stripped):
            continue
        if "← Часть" in stripped:
            continue
        lines.append(line)
    return "\n".join(lines)


def build() -> None:
    config = GuideConfig(
        source_files=[
            DOCS_MIGRATE / "README.md",
            DOCS_MIGRATE / "01-prepare.md",
            DOCS_MIGRATE / "02-hosting.md",
            DOCS_MIGRATE / "03-upload.md",
            DOCS_MIGRATE / "04-database.md",
            DOCS_MIGRATE / "05-configure.md",
            DOCS_MIGRATE / "06-check.md",
            DOCS_MIGRATE / "appendix-ftp.md",
            DOCS_MIGRATE / "appendix-plugin.md",
            DOCS_MIGRATE / "troubleshooting.md",
        ],
        out_file=OUT_DIR / "migrate.md",
        mermaid_dir=OUT_DIR / "mermaid-migrate",
        title="Перенос WordPress с localhost на хостинг",
        expected_images=None,
        normalize_headings=normalize_headings,
        simplify_tables=simplify_pdf_tables,
        extra_strip_rules=[migrate_strip_rule],
        extra_text_fixes=[fix_cross_part_links, cleanup_migrate_artifacts],
    )
    build_merged_md(config)


if __name__ == "__main__":
    build()
