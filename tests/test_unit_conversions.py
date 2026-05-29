"""Tests for documented unit conversion helpers."""

from __future__ import annotations

import pandas as pd
import pytest

from trees_to_seas.qa.units import (
    add_unit_conversion_record,
    celsius_to_fahrenheit,
    cfs_to_cms,
    cm_to_mm,
    cms_to_cfs,
    fahrenheit_to_celsius,
    feet_to_meters,
    inches_to_mm,
    kg_to_pounds,
    meters_to_feet,
    normalize_salinity_to_psu,
    pounds_to_kg,
)


def test_temperature_conversions() -> None:
    assert fahrenheit_to_celsius(32) == pytest.approx(0)
    assert celsius_to_fahrenheit(0) == pytest.approx(32)


def test_length_conversions() -> None:
    assert feet_to_meters(10) == pytest.approx(3.048)
    assert meters_to_feet(3.048) == pytest.approx(10)
    assert inches_to_mm(2) == pytest.approx(50.8)
    assert cm_to_mm(2) == pytest.approx(20)


def test_mass_and_flow_conversions() -> None:
    assert pounds_to_kg(1) == pytest.approx(0.45359237)
    assert kg_to_pounds(1) == pytest.approx(2.2046226218487757)
    assert cfs_to_cms(1) == pytest.approx(0.028316846592)
    assert cms_to_cfs(0.028316846592) == pytest.approx(1)


def test_conversions_support_pandas_series() -> None:
    series = pd.Series([32, 212])

    converted = fahrenheit_to_celsius(series)

    assert converted.tolist() == pytest.approx([0, 100])


def test_normalize_salinity_to_psu_is_pass_through() -> None:
    assert normalize_salinity_to_psu(35) == 35


def test_add_unit_conversion_record_appends_metadata_without_mutating_input() -> None:
    records: list[dict[str, str]] = []

    updated = add_unit_conversion_record(
        records,
        source_column="temperature_f",
        target_column="temperature_c",
        original_unit="deg_F",
        target_unit="deg_C",
        method="fahrenheit_to_celsius",
        notes="unit test metadata only",
    )

    assert records == []
    assert updated[0]["source_column"] == "temperature_f"
    assert updated[0]["target_unit"] == "deg_C"


def test_add_unit_conversion_record_requires_documented_method() -> None:
    with pytest.raises(ValueError, match="method"):
        add_unit_conversion_record(
            [],
            source_column="source",
            target_column="target",
            original_unit="original",
            target_unit="target",
            method="",
        )
