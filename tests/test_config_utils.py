"""Tests for repository-scoped config utilities."""

from __future__ import annotations

from pathlib import Path

import pytest

from trees_to_seas.utils.config import (
    config_path,
    list_available_configs,
    load_config,
    load_yaml,
    require_keys,
)


def test_load_config_reads_existing_placeholder_mapping() -> None:
    config = load_config("data_sources")

    assert config["version"] == "0.1.0"
    assert config["status"] == "placeholder_no_data_ingested"


def test_config_path_accepts_configs_relative_path() -> None:
    path = config_path(Path("configs") / "data_sources.yaml")

    assert path.name == "data_sources.yaml"
    assert path.parent.name == "configs"


def test_malformed_yaml_raises_clear_error(tmp_path: Path) -> None:
    yaml_path = tmp_path / "malformed.yaml"
    yaml_path.write_text("key: [unterminated\n", encoding="utf-8")

    with pytest.raises(ValueError, match="Malformed YAML"):
        load_yaml(yaml_path)


def test_non_mapping_yaml_raises_clear_error(tmp_path: Path) -> None:
    yaml_path = tmp_path / "list.yaml"
    yaml_path.write_text("- item\n", encoding="utf-8")

    with pytest.raises(TypeError, match="expected a mapping"):
        load_yaml(yaml_path)


def test_empty_placeholder_yaml_returns_empty_dict(tmp_path: Path) -> None:
    yaml_path = tmp_path / "empty.yaml"
    yaml_path.write_text("# placeholder only\n", encoding="utf-8")

    assert load_yaml(yaml_path) == {}


def test_require_keys_catches_missing_keys() -> None:
    with pytest.raises(KeyError, match="missing required keys"):
        require_keys({"present": True}, ["present", "missing"], context="unit test")


def test_list_available_configs_includes_existing_configs() -> None:
    names = {path.name for path in list_available_configs()}

    assert "data_sources.yaml" in names
    assert "validation_config.yaml" in names
