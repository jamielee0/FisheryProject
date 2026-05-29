"""Provenance helpers that record metadata without inspecting restricted data content."""

from __future__ import annotations

import csv
import hashlib
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import pandas as pd

_PROVENANCE_COLUMNS = [
    "source_name",
    "source_category",
    "provider",
    "date_acquired",
    "access_url_or_contact",
    "access_restrictions",
    "raw_path",
    "file_format",
    "years_covered",
    "variables",
    "row_count",
    "checksum",
    "notes",
]


def file_checksum(path: str | Path, algorithm: str = "sha256") -> str:
    """Return a checksum for a file using a hashlib-supported algorithm."""
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"File not found for checksum: {file_path}")
    if not file_path.is_file():
        raise ValueError(f"Checksum path is not a file: {file_path}")

    try:
        hasher = hashlib.new(algorithm)
    except ValueError as exc:
        raise ValueError(f"Unsupported checksum algorithm: {algorithm}") from exc

    with file_path.open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def describe_file(path: str | Path) -> dict[str, Any]:
    """Describe file metadata and checksum without parsing the file contents."""
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"File not found for description: {file_path}")
    if not file_path.is_file():
        raise ValueError(f"Description path is not a file: {file_path}")

    stat = file_path.stat()
    return {
        "path": str(file_path),
        "name": file_path.name,
        "suffix": file_path.suffix.lower(),
        "size_bytes": stat.st_size,
        "modified_time_utc": datetime.fromtimestamp(
            stat.st_mtime,
            tz=timezone.utc,
        ).isoformat(),
        "checksum_sha256": file_checksum(file_path),
    }


def expected_provenance_columns() -> list[str]:
    """Return the required provenance log columns in canonical order."""
    return list(_PROVENANCE_COLUMNS)


def _is_blank(value: Any) -> bool:
    if value is None:
        return True
    try:
        missing = pd.isna(value)
    except (TypeError, ValueError):
        missing = False
    try:
        if bool(missing):
            return True
    except (TypeError, ValueError):
        pass
    return isinstance(value, str) and not value.strip()


def validate_provenance_record(record: dict[str, Any]) -> None:
    """Validate that a provenance record has all required non-note fields."""
    if not isinstance(record, dict):
        raise TypeError(f"Provenance record must be a dict, got {type(record).__name__}")

    expected = expected_provenance_columns()
    missing = [column for column in expected if column not in record]
    if missing:
        raise ValueError(f"Provenance record missing required fields: {missing}")

    blank = [column for column in expected if column != "notes" and _is_blank(record[column])]
    if blank:
        raise ValueError(f"Provenance record has blank required fields: {blank}")


def validate_provenance_table(df: pd.DataFrame) -> None:
    """Validate provenance table columns and row-level required fields."""
    if not isinstance(df, pd.DataFrame):
        raise TypeError(f"Provenance table must be a pandas DataFrame, got {type(df).__name__}")

    expected = expected_provenance_columns()
    missing = [column for column in expected if column not in df.columns]
    if missing:
        raise ValueError(f"Provenance table missing required columns: {missing}")

    for row_index, row in df[expected].iterrows():
        try:
            validate_provenance_record(row.to_dict())
        except (TypeError, ValueError) as exc:
            raise ValueError(f"Invalid provenance record at row {row_index}: {exc}") from exc


def append_provenance_record(record: dict[str, Any], path: str | Path) -> None:
    """Append one provenance record to a CSV log, creating directories and headers if needed."""
    validate_provenance_record(record)

    log_path = Path(path)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    expected = expected_provenance_columns()
    file_exists = log_path.exists()
    write_header = not file_exists or log_path.stat().st_size == 0

    if file_exists and log_path.is_dir():
        raise IsADirectoryError(f"Provenance log path is a directory: {log_path}")

    fieldnames = expected
    if file_exists and not write_header:
        with log_path.open(newline="", encoding="utf-8") as file:
            existing_header = next(csv.reader(file), None)
        if not existing_header:
            write_header = True
        else:
            missing = [column for column in expected if column not in existing_header]
            if missing:
                raise ValueError(
                    f"Existing provenance log missing required columns {missing}: {log_path}"
                )
            fieldnames = existing_header

    with log_path.open("a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if write_header:
            writer.writeheader()
        writer.writerow({column: record.get(column, "") for column in fieldnames})
