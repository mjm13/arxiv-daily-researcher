#!/usr/bin/env python3
"""Run trend_research once per configured monthly keyword for the previous calendar month."""

from __future__ import annotations

import json5
import subprocess
import sys
from calendar import monthrange
from datetime import date
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
CONFIG_CANDIDATES = (
    PROJECT_ROOT / "runtime" / "config.json",
    PROJECT_ROOT / "configs" / "config.json",
)


def previous_calendar_month(today: date | None = None) -> tuple[date, date]:
    """Return inclusive (first_day, last_day) of the calendar month before ``today``."""
    today = today or date.today()
    if today.month == 1:
        year, month = today.year - 1, 12
    else:
        year, month = today.year, today.month - 1
    last_day = monthrange(year, month)[1]
    return date(year, month, 1), date(year, month, last_day)


def load_trend_settings() -> dict:
    for path in CONFIG_CANDIDATES:
        if path.is_file():
            with path.open("r", encoding="utf-8") as handle:
                document = json5.load(handle)
            if not isinstance(document, dict):
                raise ValueError(f"{path} 根节点必须是对象")
            trend = document.get("trend_research", {})
            if not isinstance(trend, dict):
                raise ValueError("trend_research 必须是对象")
            return trend
    raise FileNotFoundError("未找到 runtime/config.json 或 configs/config.json")


def main() -> int:
    trend = load_trend_settings()
    keywords = trend.get("monthly_keywords", [])
    if not isinstance(keywords, list) or not keywords:
        print("错误: trend_research.monthly_keywords 必须是非空列表", file=sys.stderr)
        return 1

    normalized_keywords: list[str] = []
    for item in keywords:
        text = str(item or "").strip()
        if text:
            normalized_keywords.append(text)
    if not normalized_keywords:
        print("错误: trend_research.monthly_keywords 没有有效关键词", file=sys.stderr)
        return 1

    categories = trend.get("monthly_categories", [])
    if categories is None:
        categories = []
    if not isinstance(categories, list):
        print("错误: trend_research.monthly_categories 必须是列表", file=sys.stderr)
        return 1
    normalized_categories = [str(item).strip() for item in categories if str(item).strip()]

    sort_order = str(trend.get("sort_order", "ascending")).strip() or "ascending"
    max_results = int(trend.get("max_results", 200) or 200)
    date_from, date_to = previous_calendar_month()

    print(
        f"月度趋势回顾: {date_from.isoformat()} ~ {date_to.isoformat()}, "
        f"{len(normalized_keywords)} 个关键词, 上限 {max_results}/次"
    )

    main_py = PROJECT_ROOT / "main.py"
    failures = 0
    for index, keyword in enumerate(normalized_keywords, start=1):
        cmd = [
            sys.executable,
            str(main_py),
            "--mode",
            "trend_research",
            "--keywords",
            keyword,
            "--date-from",
            date_from.isoformat(),
            "--date-to",
            date_to.isoformat(),
            "--sort-order",
            sort_order,
            "--max-results",
            str(max_results),
        ]
        if normalized_categories:
            cmd.extend(["--categories", *normalized_categories])

        print(f"\n[{index}/{len(normalized_keywords)}] keyword={keyword!r}")
        print("Running:", " ".join(cmd))
        result = subprocess.run(cmd, cwd=PROJECT_ROOT)
        if result.returncode != 0:
            failures += 1
            print(f"警告: 关键词 {keyword!r} 的趋势分析失败 (exit {result.returncode})")

    if failures:
        print(f"\n完成: {len(normalized_keywords) - failures}/{len(normalized_keywords)} 成功")
        return 1
    print(f"\n完成: 全部 {len(normalized_keywords)} 个关键词趋势分析成功")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
