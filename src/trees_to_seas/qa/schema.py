"""Canonical schema definitions for future data harmonization steps."""

from __future__ import annotations

BIOLOGICAL_REQUIRED = [
    "dataset_source",
    "survey_program",
    "tow_id",
    "date",
    "year",
    "month",
    "species_common",
]

BIOLOGICAL_OPTIONAL = [
    "datetime",
    "season",
    "survey_wave",
    "station_id",
    "grid_id",
    "stratum",
    "estuary_zone",
    "latitude",
    "longitude",
    "depth_m",
    "tow_duration_min",
    "tow_distance_m",
    "swept_area_m2",
    "effort",
    "gear",
    "vessel",
    "species_code",
    "species_scientific",
    "count",
    "weight_kg",
    "biomass_kg",
    "cpue_count",
    "cpue_weight_kg",
    "length_mm",
    "length_type",
    "sex",
    "maturity",
    "carapace_width_mm",
    "onboard_temperature_c",
    "onboard_salinity_psu",
    "onboard_dissolved_oxygen_mg_l",
    "onboard_turbidity_ntu",
    "notes",
]

BIOLOGICAL_SCHEMA = BIOLOGICAL_REQUIRED + BIOLOGICAL_OPTIONAL


ENVIRONMENTAL_REQUIRED = [
    "dataset_source",
    "station_id",
    "datetime",
    "date",
    "year",
    "month",
    "latitude",
    "longitude",
    "sample_depth_type",
]

ENVIRONMENTAL_OPTIONAL = [
    "depth_m",
    "temperature_c",
    "salinity_psu",
    "dissolved_oxygen_mg_l",
    "turbidity_ntu",
    "secchi_m",
    "chlorophyll_a_ug_l",
    "ph",
    "water_level_m",
    "discharge_cms",
    "rainfall_mm",
    "drought_class",
    "storm_window",
    "quality_flag",
    "notes",
]

ENVIRONMENTAL_SCHEMA = ENVIRONMENTAL_REQUIRED + ENVIRONMENTAL_OPTIONAL


HYDROLOGY_REQUIRED = [
    "dataset_source",
    "station_id",
    "datetime",
    "date",
    "year",
    "month",
]

HYDROLOGY_OPTIONAL = [
    "provider",
    "gauge_id",
    "watershed_id",
    "latitude",
    "longitude",
    "discharge_cms",
    "gauge_height_m",
    "water_level_m",
    "rainfall_mm",
    "quality_flag",
    "notes",
]

HYDROLOGY_SCHEMA = HYDROLOGY_REQUIRED + HYDROLOGY_OPTIONAL


EVENT_REQUIRED = [
    "event_id",
    "event_type",
    "start_datetime",
    "end_datetime",
    "source_dataset",
]

EVENT_OPTIONAL = [
    "date",
    "year",
    "spatial_unit_id",
    "watershed_id",
    "storm_window",
    "drought_class",
    "source_variable",
    "threshold_definition",
    "event_holdout_flag",
    "notes",
]

EVENT_SCHEMA = EVENT_REQUIRED + EVENT_OPTIONAL


LANDCOVER_REQUIRED = [
    "year",
    "watershed_id",
    "spatial_unit_id",
    "landcover_source",
]

LANDCOVER_OPTIONAL = [
    "percent_forest",
    "percent_wetland",
    "percent_cropland",
    "percent_developed",
    "percent_impervious",
    "crop_class_summary",
    "geometry",
]

LANDCOVER_SCHEMA = LANDCOVER_REQUIRED + LANDCOVER_OPTIONAL


ENDPOINT_REQUIRED = [
    "species_common",
    "response_name",
    "endpoint_variant",
    "endpoint_value",
    "endpoint_conflict_flag",
]

ENDPOINT_OPTIONAL = [
    "species_scientific",
    "endpoint_confidence",
    "endpoint_source",
    "endpoint_warning",
]

ENDPOINT_SCHEMA = ENDPOINT_REQUIRED + ENDPOINT_OPTIONAL


FEATURE_REQUIRED = [
    "feature_name",
    "source_variable",
    "source_dataset",
    "model_use",
    "leakage_safe",
]

FEATURE_OPTIONAL = [
    "lag_window_days",
    "statistic",
    "sample_depth_type",
    "threshold_value",
    "threshold_confidence",
    "missingness_fraction",
]

FEATURE_SCHEMA = FEATURE_REQUIRED + FEATURE_OPTIONAL


_SCHEMAS = {
    "biological": (BIOLOGICAL_REQUIRED, BIOLOGICAL_OPTIONAL),
    "environmental": (ENVIRONMENTAL_REQUIRED, ENVIRONMENTAL_OPTIONAL),
    "hydrology": (HYDROLOGY_REQUIRED, HYDROLOGY_OPTIONAL),
    "event": (EVENT_REQUIRED, EVENT_OPTIONAL),
    "landcover": (LANDCOVER_REQUIRED, LANDCOVER_OPTIONAL),
    "endpoint": (ENDPOINT_REQUIRED, ENDPOINT_OPTIONAL),
    "feature": (FEATURE_REQUIRED, FEATURE_OPTIONAL),
}


def _normalize_schema_name(schema_name: str) -> str:
    normalized = schema_name.strip().lower()
    if normalized.endswith("_schema"):
        normalized = normalized.removesuffix("_schema")
    return normalized


def _schema_parts(schema_name: str) -> tuple[list[str], list[str]]:
    normalized = _normalize_schema_name(schema_name)
    try:
        required, optional = _SCHEMAS[normalized]
    except KeyError as exc:
        available = sorted(_SCHEMAS)
        message = f"Unknown schema '{schema_name}'. Available schemas: {available}"
        raise ValueError(message) from exc
    return list(required), list(optional)


def required_columns(schema_name: str) -> list[str]:
    """Return required columns for a named canonical schema."""
    required, _ = _schema_parts(schema_name)
    return required


def optional_columns(schema_name: str) -> list[str]:
    """Return optional columns for a named canonical schema."""
    _, optional = _schema_parts(schema_name)
    return optional


def schema_columns(schema_name: str) -> list[str]:
    """Return all columns for a named canonical schema in canonical order."""
    required, optional = _schema_parts(schema_name)
    return required + optional
