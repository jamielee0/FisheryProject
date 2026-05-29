"""Parseability checks for setup configuration placeholders."""

from __future__ import annotations

from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]

CONFIG_FILES = [
    "configs/data_sources.yaml",
    "configs/model_config.yaml",
    "configs/validation_config.yaml",
    "configs/endpoint_config.yaml",
    "configs/threshold_config.yaml",
    "configs/feature_config.yaml",
    "configs/join_config.yaml",
]


def test_all_config_yaml_files_parse_as_mappings() -> None:
    for relative_path in CONFIG_FILES:
        path = REPO_ROOT / relative_path
        assert path.exists(), f"Missing config file: {relative_path}"

        with path.open(encoding="utf-8") as file:
            parsed = yaml.safe_load(file)

        assert isinstance(parsed, dict), f"Config is not a mapping: {relative_path}"
        assert parsed, f"Config mapping is empty: {relative_path}"
