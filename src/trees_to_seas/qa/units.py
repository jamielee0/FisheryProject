"""Unit conversion helpers for documented, source-confirmed units."""

from __future__ import annotations

from typing import Any

POUNDS_PER_KILOGRAM = 2.2046226218487757
KILOGRAMS_PER_POUND = 0.45359237
METERS_PER_FOOT = 0.3048
MILLIMETERS_PER_INCH = 25.4
CMS_PER_CFS = 0.028316846592


def fahrenheit_to_celsius(value: Any) -> Any:
    """Convert Fahrenheit to Celsius for scalars or pandas-like arrays."""
    return (value - 32) * 5 / 9


def celsius_to_fahrenheit(value: Any) -> Any:
    """Convert Celsius to Fahrenheit for scalars or pandas-like arrays."""
    return (value * 9 / 5) + 32


def feet_to_meters(value: Any) -> Any:
    """Convert feet to meters."""
    return value * METERS_PER_FOOT


def meters_to_feet(value: Any) -> Any:
    """Convert meters to feet."""
    return value / METERS_PER_FOOT


def inches_to_mm(value: Any) -> Any:
    """Convert inches to millimeters."""
    return value * MILLIMETERS_PER_INCH


def cm_to_mm(value: Any) -> Any:
    """Convert centimeters to millimeters."""
    return value * 10


def pounds_to_kg(value: Any) -> Any:
    """Convert pounds to kilograms."""
    return value * KILOGRAMS_PER_POUND


def kg_to_pounds(value: Any) -> Any:
    """Convert kilograms to pounds."""
    return value * POUNDS_PER_KILOGRAM


def cfs_to_cms(value: Any) -> Any:
    """Convert cubic feet per second to cubic meters per second."""
    return value * CMS_PER_CFS


def cms_to_cfs(value: Any) -> Any:
    """Convert cubic meters per second to cubic feet per second."""
    return value / CMS_PER_CFS


def normalize_salinity_to_psu(value: Any) -> Any:
    """Return salinity values already confirmed to be practical salinity/PSU-compatible."""
    return value


def _require_text(value: Any, name: str) -> None:
    if value is None or not str(value).strip():
        raise ValueError(f"Unit conversion record requires {name}.")


def add_unit_conversion_record(
    records: list[dict[str, Any]],
    *,
    source_column: str,
    target_column: str,
    original_unit: str,
    target_unit: str,
    method: str,
    notes: str = "",
) -> list[dict[str, Any]]:
    """Return records with one documented unit-conversion record appended."""
    if not isinstance(records, list):
        raise TypeError(f"records must be a list, got {type(records).__name__}")

    for name, value in {
        "source_column": source_column,
        "target_column": target_column,
        "original_unit": original_unit,
        "target_unit": target_unit,
        "method": method,
    }.items():
        _require_text(value, name)

    # Do not invent fork-length to total-length conversions. The spot June
    # FL/TL conflict requires verified source documentation before any formula.
    updated = list(records)
    updated.append(
        {
            "source_column": source_column,
            "target_column": target_column,
            "original_unit": original_unit,
            "target_unit": target_unit,
            "method": method,
            "notes": notes,
        }
    )
    return updated
