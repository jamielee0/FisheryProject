"""Smoke tests for repository parseability and package importability."""

from __future__ import annotations

import csv
import importlib
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]

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

REQUIRED_THRESHOLD_COLUMNS = {
    "species",
    "life_stage",
    "variable",
    "threshold_type",
    "value",
    "units",
    "source_label",
    "evidence_type",
    "confidence",
    "model_use",
    "verified",
    "notes",
}

REQUIRED_SPECIES = {
    "blue_crab",
    "atlantic_croaker",
    "spot",
    "southern_flounder",
}

REQUIRED_CONFIGS = [
    "configs/data_sources.yaml",
    "configs/model_config.yaml",
    "configs/validation_config.yaml",
    "configs/endpoint_config.yaml",
    "configs/threshold_config.yaml",
    "configs/feature_config.yaml",
    "configs/join_config.yaml",
]

REQUIRED_METADATA_TEMPLATES = [
    "metadata/data_inventory.csv",
    "metadata/provenance_log.csv",
    "metadata/data_dictionary.csv",
    "metadata/validation_folds.csv",
    "metadata/source_quality_audit.csv",
    "metadata/decision_log.csv",
]


def test_package_importable() -> None:
    import trees_to_seas

    assert trees_to_seas.__version__ == "0.1.0"


def test_all_current_subpackages_importable() -> None:
    for name in SUBPACKAGES:
        module = importlib.import_module(name)
        assert module is not None


def test_species_traits_yaml_exists_parses_and_has_required_species() -> None:
    traits_path = REPO_ROOT / "species_traits.yaml"
    assert traits_path.exists(), "species_traits.yaml not found"

    with traits_path.open(encoding="utf-8") as file:
        data = yaml.safe_load(file)

    assert isinstance(data, dict)
    assert "species_traits" in data, (
        "species_traits.yaml must use top-level key 'species_traits'. "
        "Older code that expected 'species' should be updated for this schema."
    )
    species_traits = data["species_traits"]
    assert isinstance(species_traits, dict)

    missing = REQUIRED_SPECIES.difference(species_traits)
    assert not missing, f"Missing species in species_traits.yaml: {sorted(missing)}"


def test_threshold_table_csv_exists_parses_and_has_required_columns() -> None:
    table_path = REPO_ROOT / "threshold_table.csv"
    assert table_path.exists(), "threshold_table.csv not found"

    with table_path.open(newline="", encoding="utf-8") as file:
        rows = [row for row in file if row.strip() and not row.lstrip().startswith("#")]

    reader = csv.DictReader(rows)
    assert reader.fieldnames is not None, "threshold_table.csv has no header"
    missing_columns = REQUIRED_THRESHOLD_COLUMNS.difference(reader.fieldnames)
    assert not missing_columns, (
        "threshold_table.csv missing required columns: "
        f"{sorted(missing_columns)}"
    )
    assert any(reader), "threshold_table.csv has no data rows"


def test_required_scientific_boundary_files_exist() -> None:
    required_files = [
        "AGENTS.md",
        "CLAIM_BOUNDARIES.md",
        "PROJECT_CHARTER.md",
        "endpoint_verification.md",
        "SOURCE_QUALITY_AUDIT.md",
        "RELATED_WORK_MATRIX.md",
    ]
    missing = [path for path in required_files if not (REPO_ROOT / path).exists()]
    assert not missing, f"Missing required project files: {missing}"


def test_config_placeholders_exist_and_parse() -> None:
    for relative_path in REQUIRED_CONFIGS:
        path = REPO_ROOT / relative_path
        assert path.exists(), f"Missing config placeholder: {relative_path}"
        with path.open(encoding="utf-8") as file:
            parsed = yaml.safe_load(file)
        assert isinstance(parsed, dict), f"Config did not parse as a mapping: {relative_path}"


def test_metadata_templates_exist_and_have_headers() -> None:
    for relative_path in REQUIRED_METADATA_TEMPLATES:
        path = REPO_ROOT / relative_path
        assert path.exists(), f"Missing metadata template: {relative_path}"
        with path.open(newline="", encoding="utf-8") as file:
            header = next(csv.reader(file), None)
        assert header, f"Metadata template has no header: {relative_path}"
