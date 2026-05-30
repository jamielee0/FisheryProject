"""Tests for canonical schema definitions."""

from __future__ import annotations

import pytest

from trees_to_seas.qa.schema import (
    BIOLOGICAL_SCHEMA,
    ENDPOINT_SCHEMA,
    ENVIRONMENTAL_SCHEMA,
    FEATURE_SCHEMA,
    LANDCOVER_SCHEMA,
    optional_columns,
    required_columns,
    schema_columns,
)


def test_schema_definitions_include_key_columns() -> None:
    assert "tow_id" in BIOLOGICAL_SCHEMA
    assert "sample_depth_type" in ENVIRONMENTAL_SCHEMA
    assert "percent_impervious" in LANDCOVER_SCHEMA
    assert "endpoint_conflict_flag" in ENDPOINT_SCHEMA
    assert "leakage_safe" in FEATURE_SCHEMA


def test_schema_helpers_return_required_optional_and_all_columns() -> None:
    required = required_columns("biological")
    optional = optional_columns("biological")
    all_columns = schema_columns("biological")

    assert "dataset_source" in required
    assert "length_type" in optional
    assert all_columns == required + optional


def test_schema_helpers_accept_schema_suffix() -> None:
    assert schema_columns("feature_schema") == FEATURE_SCHEMA


def test_unknown_schema_name_raises_clear_error() -> None:
    with pytest.raises(ValueError, match="Unknown schema"):
        schema_columns("not_a_schema")
