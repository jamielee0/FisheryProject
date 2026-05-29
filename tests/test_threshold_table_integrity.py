"""Integrity checks for threshold table parseability and uncertainty flags."""

from __future__ import annotations

import csv
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
THRESHOLD_TABLE_PATH = REPO_ROOT / "threshold_table.csv"

REQUIRED_COLUMNS = {
    "species",
    "life_stage",
    "variable",
    "threshold_type",
    "value",
    "units",
    "source_label",
    "evidence_type",
    "confidence",
    "model_use",
    "verified",
    "notes",
}


def load_threshold_rows() -> list[dict[str, str]]:
    with THRESHOLD_TABLE_PATH.open(newline="", encoding="utf-8") as file:
        data_lines = [line for line in file if line.strip() and not line.lstrip().startswith("#")]

    reader = csv.DictReader(data_lines)
    assert reader.fieldnames is not None
    assert REQUIRED_COLUMNS.issubset(reader.fieldnames)
    return list(reader)


def is_verified(value: str) -> bool:
    return value.strip().lower() in {"true", "yes", "1"}


def test_threshold_table_parses_and_has_required_columns() -> None:
    rows = load_threshold_rows()
    assert rows


def test_low_or_unknown_confidence_rows_are_not_marked_verified() -> None:
    rows = load_threshold_rows()
    weak_rows = [
        row
        for row in rows
        if "low" in row["confidence"].lower() or "unknown" in row["confidence"].lower()
    ]

    assert weak_rows
    assert all(not is_verified(row["verified"]) for row in weak_rows)


def test_blue_crab_endpoint_row_exists() -> None:
    rows = load_threshold_rows()
    assert any(
        row["species"] == "blue_crab"
        and row["variable"] == "endpoint"
        and row["threshold_type"] == "recruit_cutoff"
        for row in rows
    )


def test_croaker_endpoint_conflict_rows_exist() -> None:
    rows = load_threshold_rows()
    croaker_june_rows = [
        row
        for row in rows
        if row["species"] == "atlantic_croaker"
        and row["variable"] == "endpoint"
        and row["threshold_type"].startswith("june_juvenile_cutoff")
    ]

    assert len(croaker_june_rows) >= 2
    assert any("CONFLICT" in row["notes"] for row in croaker_june_rows)
    assert all(not is_verified(row["verified"]) for row in croaker_june_rows)


def test_spot_endpoint_row_exists() -> None:
    rows = load_threshold_rows()
    assert any(
        row["species"] == "spot"
        and row["variable"] == "endpoint"
        and row["threshold_type"] in {"june_juvenile_cutoff", "september_juvenile_cutoff"}
        for row in rows
    )
