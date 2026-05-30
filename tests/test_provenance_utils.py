"""Tests for provenance metadata helpers."""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import pytest

from trees_to_seas.utils.provenance import (
    append_provenance_record,
    describe_file,
    expected_provenance_columns,
    file_checksum,
    validate_provenance_record,
    validate_provenance_table,
)


def _valid_record(checksum: str = "abc123") -> dict[str, object]:
    return {
        "source_name": "unit_test_source",
        "source_category": "test_metadata",
        "provider": "unit_test",
        "date_acquired": "2026-05-29",
        "access_url_or_contact": "not_applicable",
        "access_restrictions": "not_applicable",
        "raw_path": "not_applicable",
        "file_format": "txt",
        "years_covered": "not_applicable",
        "variables": "not_applicable",
        "row_count": 0,
        "checksum": checksum,
        "notes": "",
    }


def test_file_checksum_is_stable_for_temp_file(tmp_path: Path) -> None:
    path = tmp_path / "checksum.txt"
    path.write_text("checksum fixture\n", encoding="utf-8")

    first = file_checksum(path)
    second = file_checksum(path)

    assert first == second
    assert len(first) == 64


def test_describe_file_returns_metadata_and_checksum(tmp_path: Path) -> None:
    path = tmp_path / "metadata.txt"
    path.write_text("metadata fixture\n", encoding="utf-8")

    description = describe_file(path)

    assert description["name"] == "metadata.txt"
    assert description["size_bytes"] > 0
    assert description["checksum_sha256"] == file_checksum(path)


def test_validate_provenance_record_catches_missing_field() -> None:
    record = _valid_record()
    record.pop("provider")

    with pytest.raises(ValueError, match="missing required fields"):
        validate_provenance_record(record)


def test_validate_provenance_table_catches_missing_columns() -> None:
    df = pd.DataFrame({"source_name": ["unit_test_source"]})

    with pytest.raises(ValueError, match="missing required columns"):
        validate_provenance_table(df)


def test_validate_provenance_table_accepts_header_only_template() -> None:
    df = pd.DataFrame(columns=expected_provenance_columns())

    validate_provenance_table(df)


def test_append_provenance_record_creates_parent_and_appends(tmp_path: Path) -> None:
    path = tmp_path / "metadata" / "provenance_log.csv"
    record = _valid_record(checksum="def456")

    append_provenance_record(record, path)
    append_provenance_record(record, path)
    written = pd.read_csv(path)

    assert list(written.columns) == expected_provenance_columns()
    assert len(written) == 2
