#!/usr/bin/env python3
"""查询和维护文章已读账本。仅使用 Python 标准库。"""

from __future__ import annotations

import argparse
import csv
import re
import sys
import unicodedata
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LEDGER = ROOT / "data" / "article_read_ledger.tsv"
FIELDS = ("source", "article_date", "title", "status", "processed_at", "raw_path", "note")


def normalize(value: str) -> str:
    value = unicodedata.normalize("NFKC", value).casefold().strip()
    return re.sub(r"[\W_]+", "", value)


def load_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        if tuple(reader.fieldnames or ()) != FIELDS:
            raise SystemExit(f"账本字段不正确: {path}")
        return list(reader)


def article_key(source: str, article_date: str, title: str) -> tuple[str, str, str]:
    return normalize(source), article_date.strip(), normalize(title)


def find_matches(rows: list[dict[str, str]], source: str, article_date: str, title: str) -> list[dict[str, str]]:
    wanted = article_key(source, article_date, title)
    return [row for row in rows if article_key(row["source"], row["article_date"], row["title"]) == wanted]


def write_rows(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def command_check(args: argparse.Namespace) -> int:
    matches = find_matches(load_rows(args.ledger), args.source, args.article_date, args.title)
    if not matches:
        print("NEW\t账本中没有该文章，可提取")
        return 0
    row = matches[-1]
    print(f"SEEN\t{row['status']}\t{row['processed_at']}\t{row['raw_path']}")
    return 10


def command_add(args: argparse.Namespace) -> int:
    rows = load_rows(args.ledger)
    matches = find_matches(rows, args.source, args.article_date, args.title)
    if matches and not args.update:
        row = matches[-1]
        print(f"SKIP\t已登记于 {row['processed_at']}\t{row['raw_path']}")
        return 10
    new_row = {
        "source": args.source,
        "article_date": args.article_date,
        "title": args.title,
        "status": args.status,
        "processed_at": args.processed_at,
        "raw_path": args.raw_path,
        "note": args.note,
    }
    if matches:
        target = matches[-1]
        rows[rows.index(target)] = new_row
        action = "UPDATE"
    else:
        rows.append(new_row)
        action = "ADD"
    rows.sort(key=lambda row: (row["source"], row["article_date"], normalize(row["title"])))
    write_rows(args.ledger, rows)
    print(f"{action}\t{args.title}")
    return 0


def command_list(args: argparse.Namespace) -> int:
    rows = load_rows(args.ledger)
    if args.source:
        rows = [row for row in rows if normalize(row["source"]) == normalize(args.source)]
    for row in rows:
        print("\t".join(row[field] for field in FIELDS))
    print(f"TOTAL\t{len(rows)}", file=sys.stderr)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="文章提取前去重、处理后登记")
    parser.add_argument("--ledger", type=Path, default=DEFAULT_LEDGER)
    sub = parser.add_subparsers(dest="command", required=True)

    check = sub.add_parser("check", help="提取前检查；已读返回退出码 10")
    check.add_argument("--source", required=True)
    check.add_argument("--date", dest="article_date", required=True)
    check.add_argument("--title", required=True)
    check.set_defaults(func=command_check)

    add = sub.add_parser("add", help="成功阅读/摄入后登记")
    add.add_argument("--source", required=True)
    add.add_argument("--date", dest="article_date", required=True)
    add.add_argument("--title", required=True)
    add.add_argument("--status", choices=("read", "ingested"), default="read")
    add.add_argument("--processed-at", default=date.today().isoformat())
    add.add_argument("--raw-path", default="")
    add.add_argument("--note", default="")
    add.add_argument("--update", action="store_true", help="覆盖同一去重键的已有记录")
    add.set_defaults(func=command_add)

    listing = sub.add_parser("list", help="列出账本")
    listing.add_argument("--source")
    listing.set_defaults(func=command_list)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
