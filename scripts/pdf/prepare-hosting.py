#!/usr/bin/env python3
"""Prepare merged markdown for hosting guide PDF build."""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from prepare_common import OUT_DIR, GuideConfig, build_merged_md

ROOT = Path(__file__).resolve().parents[2]
DOCS_HOSTING = ROOT / "docs" / "hosting"
DOCS_MIGRATE = ROOT / "docs" / "migrate"


def extract_h2_section(text: str, heading: str) -> str:
    pattern = rf"^## {re.escape(heading)}\s*\n(.*?)(?=^## |\Z)"
    match = re.search(pattern, text, flags=re.MULTILINE | re.DOTALL)
    return match.group(1).strip() if match else ""


def extract_h3_until(text: str, start_heading: str, stop_heading: str) -> str:
    pattern = (
        rf"^### {re.escape(start_heading)}\s*\n(.*?)"
        rf"(?=^### {re.escape(stop_heading)}\s*\n|\Z)"
    )
    match = re.search(pattern, text, flags=re.MULTILINE | re.DOTALL)
    return match.group(1).strip() if match else ""


def load_migrate_excerpt(filename: str) -> str:
    return (DOCS_MIGRATE / filename).read_text(encoding="utf-8")


def inject_migrate_excerpts(text: str, path: Path) -> str:
    name = path.name

    if name == "01-account.md":
        migrate02 = load_migrate_excerpt("02-hosting.md")
        steps = extract_h2_section(migrate02, "Сделайте")
        steps = re.sub(r"\n\n\*\*Проверка:\*\*.*$", "", steps, flags=re.DOTALL).strip()
        new_section = (
            "## Сделайте\n\n"
            "Регистрация и первый вход в панель хостинга:\n\n"
            "### Подробные шаги\n\n"
            + steps
            + "\n\n**Проверка:** вы в панели хостинга, URL сайта записан, "
            "найдены **MySQL Databases**, **File Manager**, **phpMyAdmin**."
        )
        text = re.sub(
            r"## Сделайте\n\n.*?(\n---\n\n## Если ошибка)",
            new_section + r"\1",
            text,
            count=1,
            flags=re.DOTALL,
        )

    elif name == "02-database.md":
        migrate04 = load_migrate_excerpt("04-database.md")
        db_steps = extract_h3_until(
            migrate04,
            "Создание базы в панели хостинга",
            "Запишите 4 поля для wp-config",
        )
        record_table = extract_h3_until(
            migrate04,
            "Запишите 4 поля для wp-config",
            "Импорт SQL через phpMyAdmin",
        )
        injected = (
            "### Создание базы в панели хостинга\n\n"
            + db_steps
            + "\n\n### Запишите 4 поля для wp-config\n\n"
            + record_table
        )
        text = re.sub(
            r"Создайте \*\*пустую\*\* базу — те же действия, что в .*?\n\n"
            r"\*\*Не выполняйте\*\* импорт SQL .*?\n\n"
            r"Запишите четыре поля:\n\n"
            r"\| Поле \| Ваше значение \|\n\|------\|----------------\|\n"
            r"\| DB_NAME \| \|\n\| DB_USER \| \|\n\| DB_PASSWORD \| \|\n\| DB_HOST \| \|",
            "Создайте **пустую** базу MySQL в панели хостинга.\n\n"
            "**Не выполняйте** импорт SQL — это только для переноса с Mac. "
            "Таблицы `wp_*` создаст мастер WordPress на шаге 3.\n\n"
            + injected
            + "\n\nЗапишите четыре поля в свою шпаргалку:\n\n"
            "| Поле | Ваше значение |\n|------|----------------|\n"
            "| DB_NAME | |\n| DB_USER | |\n| DB_PASSWORD | |\n| DB_HOST | |",
            text,
            count=1,
            flags=re.DOTALL,
        )

    elif name == "troubleshooting.md":
        pass

    return text


def simplify_pdf_tables(text: str) -> str:
    text = re.sub(
        r"\| Шаг \| Файл \| Содержание \|\n\|-----+\|------+\|------------+\|\n"
        r"\| 1 \| \[01-account\.md\]\([^)]+\) \| ([^|]+) \|\n"
        r"\| 2 \| \[02-database\.md\]\([^)]+\) \| ([^|]+) \|\n"
        r"\| 3 \| \[03-wordpress\.md\]\([^)]+\) \| ([^|]+) \|\n"
        r"\| 4 \| \[04-launch\.md\]\([^)]+\) \| ([^|]+) \|",
        r"| Шаг | Содержание |\n|-----|------------|\n"
        r"| 1 | \1 |\n"
        r"| 2 | \2 |\n"
        r"| 3 | \3 |\n"
        r"| 4 | \4 |",
        text,
    )
    return text.replace("*(как в migrate/02)*", "").replace("(как в migrate/02)", "")


def normalize_headings(text: str, filename: str) -> str:
    if filename == "README.md":
        text = re.sub(
            r"^# Часть 3: WordPress сразу на хостинге\s*$",
            "# WordPress на хостинге с нуля",
            text,
            count=1,
            flags=re.MULTILINE,
        )
    if filename == "troubleshooting.md":
        text = re.sub(
            r"^# Решение проблем \(хостинг\)\s*$",
            "# Приложение: Решение проблем",
            text,
            count=1,
            flags=re.MULTILINE,
        )
    return text


def hosting_strip_rule(stripped: str) -> str | None:
    if "Перенос с Mac" in stripped and "Migrate" in stripped:
        return (
            "> *Другой гайд (отдельный PDF): "
            "«Перенос WordPress с localhost на хостинг» (Часть 2)*"
        )
    if re.match(r"^\| Сайт на `localhost`", stripped):
        return "| Сайт на localhost | PDF «Перенос на хостинг» (Часть 2) |"
    if re.match(r"^\| Хотите сначала на Mac", stripped):
        return "| Хотите сначала на Mac | PDF «WordPress на Mac через MAMP» (Часть 1) |"
    return None


def fix_cross_part_links(text: str) -> str:
    text = re.sub(
        r"\[([^\]]*)\]\(\.\./migrate/troubleshooting\.md#([^\)]+)\)",
        r"[#\2](#\2)",
        text,
    )
    text = re.sub(
        r"\[([^\]]*)\]\(migrate/troubleshooting\.md#([^\)]+)\)",
        r"[#\2](#\2)",
        text,
    )
    text = re.sub(
        r"\[([^\]]*)\]\(\.\./local/[^)]+\)",
        r"PDF «WordPress на Mac через MAMP» (Часть 1)",
        text,
    )
    text = re.sub(
        r"\[шаг (\d+)\]\(\d{2}-[a-z]+\.md\)",
        r"шаг \1",
        text,
    )
    text = re.sub(
        r"\[шага (\d+)\]\(\d{2}-[a-z]+\.md\)",
        r"шага \1",
        text,
    )
    text = re.sub(
        r"\[([^\]]*)\]\(\.\./migrate/[^)]+\)",
        r"PDF «Перенос с localhost на хостинг» (Часть 2)",
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
        r"\[([^\]]+)\]\(README\.md\)",
        r"\1",
        text,
    )
    text = re.sub(
        r"migrate/02-hosting\.md",
        "шаг 2 Части 2",
        text,
    )
    text = re.sub(
        r"migrate/04-database\.md",
        "шаг 4 Части 2",
        text,
    )
    return text


def cleanup_hosting_artifacts(text: str) -> str:
    lines = []
    for line in text.splitlines():
        stripped = line.strip()
        if re.match(r"^\*\*Далее:", stripped):
            continue
        if "← Часть" in stripped:
            continue
        if re.match(r"^-\s+Перенос с Mac", stripped):
            continue
        lines.append(line)
    return "\n".join(lines)


def build() -> None:
    config = GuideConfig(
        source_files=[
            DOCS_HOSTING / "README.md",
            DOCS_HOSTING / "01-account.md",
            DOCS_HOSTING / "02-database.md",
            DOCS_HOSTING / "03-wordpress.md",
            DOCS_HOSTING / "04-launch.md",
            DOCS_HOSTING / "troubleshooting.md",
        ],
        out_file=OUT_DIR / "hosting.md",
        mermaid_dir=OUT_DIR / "mermaid-hosting",
        title="WordPress на хостинге с нуля",
        expected_images=None,
        normalize_headings=normalize_headings,
        simplify_tables=simplify_pdf_tables,
        extra_strip_rules=[hosting_strip_rule],
        extra_text_fixes=[fix_cross_part_links, cleanup_hosting_artifacts],
        pre_process=inject_migrate_excerpts,
    )
    build_merged_md(config)


if __name__ == "__main__":
    build()
