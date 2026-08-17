#!/usr/bin/env python3
"""Shared markdown preparation for WordPress guide PDF builds."""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = ROOT / "tmp" / "pdfs"


@dataclass
class GuideConfig:
    source_files: list[Path]
    out_file: Path
    mermaid_dir: Path
    title: str
    expected_images: int | None = None
    normalize_headings: Callable[[str, str], str] | None = None
    simplify_tables: Callable[[str], str] | None = None
    extra_strip_rules: list[Callable[[str], str | None]] = field(default_factory=list)
    extra_text_fixes: list[Callable[[str], str]] = field(default_factory=list)
    pre_process: Callable[[str, Path], str] | None = None


def remove_html_comments(text: str) -> str:
    return re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)


def strip_navigation(text: str, extra_rules: list[Callable[[str], str | None]] | None = None) -> str:
    lines = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Вы здесь:"):
            continue
        if stripped.startswith("Если ошибка"):
            continue
        if stripped.startswith("Ошибки →"):
            continue
        if re.match(r"^\*\*Далее:", stripped):
            continue
        if stripped.startswith("- [") and ("Часть" in stripped or "оглавлению" in stripped):
            continue
        if re.match(r"^\*\*\[.*→.*\]\(.*\)\*\*$", stripped):
            continue
        if re.match(r"^\*\*\[←.*\]\(.*\)\*\*$", stripped):
            continue
        if re.match(r"^\[←.*\]\(.*\)$", stripped):
            continue
        if re.match(r"^\[← К оглавлению репозитория\]", stripped):
            continue
        if re.match(r"^\[← Часть \d\]", stripped):
            continue
        if re.match(r"^\[← К оглавлению\]", stripped):
            continue
        if re.match(r"^\[← Часть 2\]", stripped):
            continue
        if "перенос](../migrate/" in stripped or "сразу на хостинг](../hosting/" in stripped:
            continue
        if re.match(r"^\*\*\[Начать шаг", stripped):
            continue
        if "## Готово" in stripped and stripped.startswith("##"):
            pass

        replaced = None
        if extra_rules:
            for rule in extra_rules:
                replaced = rule(stripped)
                if replaced is not None:
                    break
        if replaced is not None:
            if replaced:
                lines.append(replaced)
            continue

        lines.append(line)
    return "\n".join(lines)


def expand_details(text: str) -> str:
    pattern = re.compile(
        r"<details>\s*<summary>(.*?)</summary>\s*(.*?)</details>",
        re.DOTALL | re.IGNORECASE,
    )

    def repl(match: re.Match[str]) -> str:
        title = match.group(1).strip()
        body = match.group(2).strip()
        return f"\n### Пояснение: {title}\n\n{body}\n"

    return pattern.sub(repl, text)


def fix_image_paths(text: str, source_dir: Path) -> str:
    def repl(match: re.Match[str]) -> str:
        alt = match.group(1)
        rel = match.group(2)
        if rel.startswith("http://") or rel.startswith("https://"):
            return match.group(0)
        abs_path = (source_dir / rel).resolve()
        return f"![{alt}]({abs_path})"

    return re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", repl, text)


def fix_troubleshooting_links(text: str) -> str:
    return re.sub(
        r"\[troubleshooting\.md#([^\]]+)\]\(troubleshooting\.md#\1\)",
        r"[#\1](#\1)",
        text,
    )


def extract_mermaid_blocks(text: str, mermaid_dir: Path) -> tuple[str, list[str]]:
    blocks: list[str] = []
    counter = 0

    def repl(match: re.Match[str]) -> str:
        nonlocal counter
        counter += 1
        blocks.append(match.group(1).strip())
        png = mermaid_dir / f"diagram-{counter}.png"
        return f"\n![Диаграмма {counter}]({png.resolve()})\n"

    updated = re.sub(
        r"```mermaid\s*\n(.*?)```",
        repl,
        text,
        flags=re.DOTALL,
    )
    return updated, blocks


def build_merged_md(config: GuideConfig) -> None:
    config.mermaid_dir.mkdir(parents=True, exist_ok=True)
    config.out_file.parent.mkdir(parents=True, exist_ok=True)

    parts: list[str] = []
    all_mermaid: list[str] = []

    for path in config.source_files:
        raw = path.read_text(encoding="utf-8")
        if config.pre_process:
            raw = config.pre_process(raw, path)
        raw = remove_html_comments(raw)
        if config.normalize_headings:
            raw = config.normalize_headings(raw, path.name)
        if config.simplify_tables and path.name == "README.md":
            raw = config.simplify_tables(raw)
        raw = strip_navigation(raw, config.extra_strip_rules)
        raw = expand_details(raw)
        raw = fix_troubleshooting_links(raw)
        for fix in config.extra_text_fixes:
            raw = fix(raw)
        raw, mermaid_blocks = extract_mermaid_blocks(raw, config.mermaid_dir)
        all_mermaid.extend(mermaid_blocks)
        raw = fix_image_paths(raw, path.parent)
        parts.append(raw.strip())

    for i, block in enumerate(all_mermaid, start=1):
        (config.mermaid_dir / f"diagram-{i}.mmd").write_text(block + "\n", encoding="utf-8")

    merged = "\n\n---\n\n".join(parts)
    screenshot_count = len(re.findall(r"assets/images/[^\)]+\.png", merged))
    if config.expected_images is not None and screenshot_count < config.expected_images:
        print(
            f"Warning: expected at least {config.expected_images} screenshot paths, "
            f"found {screenshot_count}",
            file=sys.stderr,
        )

    front_matter = (
        "---\n"
        f'title: "{config.title}"\n'
        "lang: ru\n"
        "documentclass: article\n"
        "---\n\n"
    )
    config.out_file.write_text(front_matter + merged + "\n", encoding="utf-8")
    print(f"Wrote {config.out_file}")
    print(f"Mermaid diagrams: {len(all_mermaid)}")
    print(f"Screenshots referenced: {screenshot_count}")
