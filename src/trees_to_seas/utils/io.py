"""Safe table I/O utilities for data-processing code."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pandas as pd


def ensure_parent_dir(path: str | Path) -> Path:
    """Create a path's parent directory and return the path."""
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    return output_path


def assert_not_raw_output_path(path: str | Path) -> None:
    """Refuse writes under any ``data/raw`` path segment."""
    output_path = Path(path)
    parts = [part.lower() for part in output_path.parts]
    for index, part in enumerate(parts[:-1]):
        if part == "data" and parts[index + 1] == "raw":
            raise PermissionError(f"Refusing to write output under data/raw: {output_path}")


def read_table(path: str | Path, **kwargs: Any) -> pd.DataFrame:
    """Read a supported table file without changing row contents."""
    table_path = Path(path)
    if not table_path.exists():
        raise FileNotFoundError(f"Table file not found: {table_path}")

    suffix = table_path.suffix.lower()
    if suffix == ".csv":
        return pd.read_csv(table_path, **kwargs)
    if suffix == ".tsv":
        return pd.read_csv(table_path, sep="\t", **kwargs)
    if suffix == ".parquet":
        try:
            return pd.read_parquet(table_path, **kwargs)
        except (ImportError, ValueError) as exc:
            message = "Reading parquet requires an available pandas parquet engine."
            raise ImportError(message) from exc
    if suffix in {".xlsx", ".xls"}:
        try:
            return pd.read_excel(table_path, **kwargs)
        except ImportError as exc:
            message = "Reading Excel files requires an available pandas Excel engine."
            raise ImportError(message) from exc

    raise ValueError(f"Unsupported table extension for {table_path}: {suffix}")


def _assert_can_write(df: pd.DataFrame, path: str | Path, overwrite: bool) -> Path:
    if not isinstance(df, pd.DataFrame):
        raise TypeError(f"Expected a pandas DataFrame, got {type(df).__name__}")
    output_path = Path(path)
    assert_not_raw_output_path(output_path)
    if output_path.exists() and not overwrite:
        message = f"Refusing to overwrite existing file without overwrite=True: {output_path}"
        raise FileExistsError(message)
    return ensure_parent_dir(output_path)


def safe_write_csv(
    df: pd.DataFrame,
    path: str | Path,
    overwrite: bool = False,
    **kwargs: Any,
) -> None:
    """Write a CSV only when the destination is safe and overwrite is explicit."""
    output_path = _assert_can_write(df, path, overwrite)
    kwargs.setdefault("index", False)
    df.to_csv(output_path, **kwargs)


def safe_write_parquet(
    df: pd.DataFrame,
    path: str | Path,
    overwrite: bool = False,
    **kwargs: Any,
) -> None:
    """Write a parquet file only when the destination is safe and overwrite is explicit."""
    output_path = _assert_can_write(df, path, overwrite)
    kwargs.setdefault("index", False)
    try:
        df.to_parquet(output_path, **kwargs)
    except (ImportError, ValueError) as exc:
        raise ImportError("Writing parquet requires an available pandas parquet engine.") from exc
