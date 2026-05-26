"""Smoke tests — verify the package installs and sub-packages are importable.

These tests do not require any data files.
"""

import importlib


SUBPACKAGES = [
    "trees_to_seas",
    "trees_to_seas.ingest",
    "trees_to_seas.qa",
    "trees_to_seas.endpoints",
    "trees_to_seas.features",
    "trees_to_seas.joins",
    "trees_to_seas.models",
    "trees_to_seas.evaluation",
    "trees_to_seas.visualization",
    "trees_to_seas.reports",
    "trees_to_seas.utils",
]


def test_package_importable():
    import trees_to_seas

    assert trees_to_seas.__version__ == "0.1.0"


def test_all_subpackages_importable():
    for name in SUBPACKAGES:
        mod = importlib.import_module(name)
        assert mod is not None, f"Failed to import {name}"


def test_primary_species_in_yaml():
    """species_traits.yaml must contain all primary and conditional species."""
    import yaml
    from pathlib import Path

    traits_path = Path(__file__).parents[1] / "species_traits.yaml"
    assert traits_path.exists(), "species_traits.yaml not found"

    with traits_path.open() as f:
        data = yaml.safe_load(f)

    species = data.get("species", {})
    required = {"blue_crab", "atlantic_croaker", "spot", "southern_flounder"}
    missing = required - set(species.keys())
    assert not missing, f"Missing species in species_traits.yaml: {missing}"


def test_threshold_table_has_header():
    """threshold_table.csv must exist and have the expected header columns."""
    from pathlib import Path

    table_path = Path(__file__).parents[1] / "threshold_table.csv"
    assert table_path.exists(), "threshold_table.csv not found"

    with table_path.open() as f:
        lines = [line.strip() for line in f if not line.startswith("#")]

    assert lines, "threshold_table.csv has no non-comment lines"
    header = lines[0].split(",")
    required_cols = {"species", "variable", "threshold_type", "value", "verified"}
    missing_cols = required_cols - set(header)
    assert not missing_cols, f"threshold_table.csv missing columns: {missing_cols}"


def test_claim_boundaries_exists():
    from pathlib import Path

    assert (Path(__file__).parents[1] / "CLAIM_BOUNDARIES.md").exists()


def test_endpoint_verification_exists():
    from pathlib import Path

    assert (Path(__file__).parents[1] / "endpoint_verification.md").exists()
