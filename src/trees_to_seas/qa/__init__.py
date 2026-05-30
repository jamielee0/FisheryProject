"""Quality assurance schemas, validators, and documented unit conversions.

Functions here flag surface-vs-bottom observation type, sparse bottom-water
records, known endpoint conflicts, missingness, and implausible values without
dropping rows.
"""

from trees_to_seas.qa.schema import (
    BIOLOGICAL_SCHEMA,
    ENDPOINT_SCHEMA,
    ENVIRONMENTAL_SCHEMA,
    EVENT_SCHEMA,
    FEATURE_SCHEMA,
    HYDROLOGY_SCHEMA,
    LANDCOVER_SCHEMA,
    optional_columns,
    required_columns,
    schema_columns,
)
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

__all__ = [
    "BIOLOGICAL_SCHEMA",
    "ENDPOINT_SCHEMA",
    "ENVIRONMENTAL_SCHEMA",
    "EVENT_SCHEMA",
    "FEATURE_SCHEMA",
    "HYDROLOGY_SCHEMA",
    "LANDCOVER_SCHEMA",
    "add_unit_conversion_record",
    "assert_required_columns",
    "celsius_to_fahrenheit",
    "cfs_to_cms",
    "check_coordinate_ranges",
    "check_datetime_parseable",
    "check_no_duplicate_keys",
    "check_numeric_range",
    "check_required_columns",
    "cm_to_mm",
    "cms_to_cfs",
    "fahrenheit_to_celsius",
    "feet_to_meters",
    "flag_impossible_biological_values",
    "flag_impossible_environmental_values",
    "inches_to_mm",
    "kg_to_pounds",
    "meters_to_feet",
    "normalize_salinity_to_psu",
    "optional_columns",
    "pounds_to_kg",
    "required_columns",
    "schema_columns",
    "summarize_missingness",
]
