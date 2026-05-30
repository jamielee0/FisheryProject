"""Tests for safe table I/O helpers."""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import pytest

from trees_to_seas.utils.io import read_table, safe_write_csv


def test_safe_write_csv_refuses_data_raw_path(tmp_path: Path) -> None:
    df = pd.DataFrame({"value": [1]})
    raw_path = tmp_path / "data" / "raw" / "blocked.csv"

    with pytest.raises(PermissionError, match="data/raw"):
        safe_write_csv(df, raw_path)


def test_safe_write_csv_refuses_overwrite_unless_explicit(tmp_path: Path) -> None:
    df = pd.DataFrame({"value": [1, 2]})
    output_path = tmp_path / "safe" / "table.csv"

    safe_write_csv(df, output_path)
    with pytest.raises(FileExistsError, match="overwrite=True"):
        safe_write_csv(df, output_path)

    safe_write_csv(df, output_path, overwrite=True)
    reread = pd.read_csv(output_path)
    assert len(reread) == len(df)


def test_read_table_supports_csv_and_tsv(tmp_path: Path) -> None:
    csv_path = tmp_path / "table.csv"
    tsv_path = tmp_path / "table.tsv"
    df = pd.DataFrame({"value": [1, 2]})
    df.to_csv(csv_path, index=False)
    df.to_csv(tsv_path, index=False, sep="\t")

    assert read_table(csv_path).equals(df)
    assert read_table(tsv_path).equals(df)


def test_read_table_rejects_unsupported_extension(tmp_path: Path) -> None:
    path = tmp_path / "table.unsupported"
    path.write_text("not a supported table extension\n", encoding="utf-8")

    with pytest.raises(ValueError, match="Unsupported table extension"):
        read_table(path)
