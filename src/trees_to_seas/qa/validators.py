"""QA validators that flag suspicious records without dropping rows."""

from __future__ import annotations

from typing import Any

import pandas as pd


def check_required_columns(
    df: pd.DataFrame,
    required: list[str],
    context: str = "",
) -> list[str]:
    """Return required columns that are absent from a DataFrame."""
    missing = [column for column in required if column not in df.columns]
    return missing


def assert_required_columns(
    df: pd.DataFrame,
    required: list[str],
    context: str = "",
) -> None:
    """Raise a clear error if required columns are absent from a DataFrame."""
    missing = check_required_columns(df, required, context=context)
    if missing:
        prefix = f"{context}: " if context else ""
        raise ValueError(f"{prefix}missing required columns: {missing}")


def check_no_duplicate_keys(
    df: pd.DataFrame,
    keys: list[str],
    context: str = "",
) -> pd.DataFrame:
    """Return rows whose key combinations are duplicated."""
    assert_required_columns(df, keys, context=context)
    return df.loc[df.duplicated(subset=keys, keep=False)].copy()


def check_coordinate_ranges(
    df: pd.DataFrame,
    lat_col: str = "latitude",
    lon_col: str = "longitude",
) -> pd.DataFrame:
    """Return rows with invalid global latitude or longitude values."""
    assert_required_columns(df, [lat_col, lon_col], context="coordinate check")
    lat = pd.to_numeric(df[lat_col], errors="coerce")
    lon = pd.to_numeric(df[lon_col], errors="coerce")
    mask = (
        df[lat_col].notna()
        & df[lon_col].notna()
        & (lat.between(-90, 90) & lon.between(-180, 180))
    )
    flagged = df.loc[~mask].copy()
    flagged["_qa_issue"] = "invalid_coordinates"
    return flagged


def check_datetime_parseable(series: pd.Series) -> pd.Series:
    """Return non-missing values that pandas cannot parse as datetimes."""
    parsed = pd.to_datetime(series, errors="coerce")
    mask = series.notna() & parsed.isna()
    return series.loc[mask].copy()


def _range_mask(
    series: pd.Series,
    min_value: Any = None,
    max_value: Any = None,
    *,
    lower_allows_equal: bool = True,
) -> pd.Series:
    numeric = pd.to_numeric(series, errors="coerce")
    present = series.notna()
    mask = present & numeric.isna()
    if min_value is not None:
        if lower_allows_equal:
            mask = mask | (numeric < min_value)
        else:
            mask = mask | (numeric <= min_value)
    if max_value is not None:
        mask = mask | (numeric > max_value)
    return mask.fillna(False)


def check_numeric_range(
    df: pd.DataFrame,
    column: str,
    min_value: Any = None,
    max_value: Any = None,
) -> pd.DataFrame:
    """Return rows where a numeric column is outside the supplied inclusive range."""
    assert_required_columns(df, [column], context="numeric range check")
    mask = _range_mask(df[column], min_value=min_value, max_value=max_value)
    flagged = df.loc[mask].copy()
    flagged["_qa_issue"] = f"{column}_outside_expected_range"
    flagged[f"_{column}_numeric"] = pd.to_numeric(flagged[column], errors="coerce")
    return flagged


def summarize_missingness(
    df: pd.DataFrame,
    group_cols: list[str] | None = None,
) -> pd.DataFrame:
    """Summarize missingness by column, optionally within groups."""
    if group_cols:
        assert_required_columns(df, group_cols, context="missingness summary")
        records = []
        grouped = df.groupby(group_cols, dropna=False)
        for group_key, group in grouped:
            group_values = group_key if isinstance(group_key, tuple) else (group_key,)
            group_info = dict(zip(group_cols, group_values, strict=True))
            row_count = len(group)
            for column in df.columns:
                missing_count = int(group[column].isna().sum())
                records.append(
                    {
                        **group_info,
                        "column": column,
                        "missing_count": missing_count,
                        "row_count": row_count,
                        "missingness_fraction": missing_count / row_count
                        if row_count
                        else 0.0,
                    }
                )
        return pd.DataFrame.from_records(records)

    row_count = len(df)
    return pd.DataFrame(
        {
            "column": df.columns,
            "missing_count": [int(df[column].isna().sum()) for column in df.columns],
            "row_count": row_count,
            "missingness_fraction": [
                int(df[column].isna().sum()) / row_count if row_count else 0.0
                for column in df.columns
            ],
        }
    )


def _flag_range_rules(
    df: pd.DataFrame,
    rules: dict[str, tuple[Any, Any, bool]],
) -> pd.DataFrame:
    flag_lists: list[list[str]] = [[] for _ in range(len(df))]
    for column, (min_value, max_value, lower_allows_equal) in rules.items():
        if column not in df.columns:
            continue
        mask = _range_mask(
            df[column],
            min_value=min_value,
            max_value=max_value,
            lower_allows_equal=lower_allows_equal,
        )
        for position, should_flag in enumerate(mask.to_numpy()):
            if should_flag:
                flag_lists[position].append(f"{column}_outside_expected_range")

    selected = pd.Series([bool(flags) for flags in flag_lists], index=df.index)
    flagged = df.loc[selected].copy()
    flagged["_qa_flags"] = [
        ";".join(flags)
        for flags, should_keep in zip(flag_lists, selected, strict=True)
        if should_keep
    ]
    return flagged


def flag_impossible_environmental_values(df: pd.DataFrame) -> pd.DataFrame:
    """Return rows with environmental values outside broad plausibility ranges."""
    rules = {
        "temperature_c": (-5, 45, True),
        "salinity_psu": (0, 50, True),
        "dissolved_oxygen_mg_l": (0, 25, True),
        "ph": (4, 11, True),
        "turbidity_ntu": (0, None, True),
        "chlorophyll_a_ug_l": (0, None, True),
        "depth_m": (0, None, True),
    }
    return _flag_range_rules(df, rules)


def flag_impossible_biological_values(df: pd.DataFrame) -> pd.DataFrame:
    """Return rows with biological measurements outside broad plausibility ranges."""
    rules = {
        "count": (0, None, True),
        "weight_kg": (0, None, True),
        "length_mm": (0, None, True),
        "carapace_width_mm": (0, None, True),
        "effort": (0, None, False),
    }
    return _flag_range_rules(df, rules)
