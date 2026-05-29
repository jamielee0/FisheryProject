"""Tests for QA validators that flag records without dropping data."""

from __future__ import annotations

import pandas as pd
import pytest

from trees_to_seas.qa.validators import (
    assert_required_columns,
    check_coordinate_ranges,
    check_datetime_parseable,
    check_no_duplicate_keys,
    check_numeric_range,
    check_required_columns,
    flag_impossible_biological_values,
    flag_impossible_environmental_values,
    summarize_missingness,
)


def test_required_column_checks_report_missing_columns() -> None:
    df = pd.DataFrame({"present": [1]})

    assert check_required_columns(df, ["present", "missing"]) == ["missing"]
    with pytest.raises(ValueError, match="missing required columns"):
        assert_required_columns(df, ["missing"], context="unit test")


def test_duplicate_key_checker_returns_duplicate_rows() -> None:
    df = pd.DataFrame({"key": ["a", "a", "b"], "value": [1, 2, 3]})

    duplicates = check_no_duplicate_keys(df, ["key"])

    assert len(duplicates) == 2
    assert set(duplicates["value"]) == {1, 2}


def test_coordinate_checker_flags_invalid_lat_lon() -> None:
    df = pd.DataFrame(
        {
            "latitude": [35.0, 91.0, 35.0, None],
            "longitude": [-76.0, -76.0, -181.0, -76.0],
        }
    )

    flagged = check_coordinate_ranges(df)

    assert len(flagged) == 3
    assert set(flagged["_qa_issue"]) == {"invalid_coordinates"}


def test_datetime_checker_returns_unparseable_values() -> None:
    series = pd.Series(["2024-01-01", "not a date", None])

    flagged = check_datetime_parseable(series)

    assert flagged.tolist() == ["not a date"]


def test_numeric_range_checker_flags_out_of_range_and_unparseable_values() -> None:
    df = pd.DataFrame({"value": [1, 5, "bad"]})

    flagged = check_numeric_range(df, "value", min_value=0, max_value=3)

    assert len(flagged) == 2
    assert set(flagged["value"].astype(str)) == {"5", "bad"}


def test_missingness_summary_works_without_groups() -> None:
    df = pd.DataFrame({"a": [1, None], "b": [None, None]})

    summary = summarize_missingness(df)

    missingness = dict(zip(summary["column"], summary["missingness_fraction"], strict=True))
    assert missingness["a"] == 0.5
    assert missingness["b"] == 1.0


def test_missingness_summary_works_with_groups() -> None:
    df = pd.DataFrame({"group": ["a", "a", "b"], "value": [1, None, None]})

    summary = summarize_missingness(df, group_cols=["group"])
    group_a = summary[(summary["group"] == "a") & (summary["column"] == "value")]

    assert group_a["missingness_fraction"].iloc[0] == 0.5


def test_flag_impossible_environmental_values_returns_flagged_rows() -> None:
    df = pd.DataFrame(
        {
            "temperature_c": [20, 46],
            "salinity_psu": [10, -1],
            "dissolved_oxygen_mg_l": [7, 26],
            "ph": [8, 12],
            "turbidity_ntu": [1, -1],
            "chlorophyll_a_ug_l": [5, -1],
            "depth_m": [2, -1],
        }
    )

    flagged = flag_impossible_environmental_values(df)

    assert len(flagged) == 1
    assert "temperature_c_outside_expected_range" in flagged["_qa_flags"].iloc[0]


def test_flag_impossible_biological_values_returns_flagged_rows() -> None:
    df = pd.DataFrame(
        {
            "count": [1, -1],
            "weight_kg": [0.5, -0.1],
            "length_mm": [100, -1],
            "carapace_width_mm": [50, -1],
            "effort": [1, 0],
        }
    )

    flagged = flag_impossible_biological_values(df)

    assert len(flagged) == 1
    assert "effort_outside_expected_range" in flagged["_qa_flags"].iloc[0]
