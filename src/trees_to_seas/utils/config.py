"""Configuration loading helpers for repository-scoped YAML files."""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path
from typing import Any

import yaml


def project_root() -> Path:
    """Return the repository root by walking upward from this module."""
    for candidate in Path(__file__).resolve().parents:
        if (candidate / "pyproject.toml").exists() and (candidate / "AGENTS.md").exists():
            return candidate
    raise RuntimeError("Could not locate repository root containing pyproject.toml and AGENTS.md.")


def config_path(name: str | Path) -> Path:
    """Return the repository-scoped path for a config name or relative path."""
    path = Path(name)
    if path.is_absolute():
        return path
    if not path.suffix:
        path = path.with_suffix(".yaml")
    if path.parts and path.parts[0] == "configs":
        return project_root() / path
    return project_root() / "configs" / path


def _is_empty_yaml_document(text: str) -> bool:
    """Return True when a YAML document has only whitespace, comments, or markers."""
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or stripped in {"---", "..."}:
            continue
        return False
    return True


def load_yaml(path: str | Path) -> dict[str, Any]:
    """Safely load a YAML mapping, returning ``{}`` only for empty placeholders."""
    yaml_path = Path(path)
    if not yaml_path.is_absolute():
        yaml_path = project_root() / yaml_path
    if not yaml_path.exists():
        raise FileNotFoundError(f"YAML file not found: {yaml_path}")

    text = yaml_path.read_text(encoding="utf-8")
    try:
        loaded = yaml.safe_load(text)
    except yaml.YAMLError as exc:
        raise ValueError(f"Malformed YAML in {yaml_path}: {exc}") from exc

    if loaded is None:
        if _is_empty_yaml_document(text):
            return {}
        raise TypeError(f"YAML file must contain a mapping, not null: {yaml_path}")
    return ensure_mapping(loaded, context=str(yaml_path))


def load_config(name: str) -> dict[str, Any]:
    """Load a YAML config from the repository ``configs`` directory."""
    return load_yaml(config_path(name))


def require_keys(
    mapping: dict[str, Any],
    required: list[str] | tuple[str, ...],
    context: str = "",
) -> None:
    """Raise a clear error when a mapping is missing required keys."""
    ensure_mapping(mapping, context=context)
    missing = [key for key in required if key not in mapping]
    if missing:
        prefix = f"{context}: " if context else ""
        raise KeyError(f"{prefix}missing required keys: {missing}")


def ensure_mapping(obj: Any, context: str = "") -> dict[str, Any]:
    """Return ``obj`` as a plain dict when it is a mapping, otherwise raise."""
    if isinstance(obj, Mapping):
        return dict(obj)
    prefix = f"{context}: " if context else ""
    raise TypeError(f"{prefix}expected a mapping, got {type(obj).__name__}")


def list_available_configs() -> list[Path]:
    """List YAML config files available under the repository ``configs`` directory."""
    config_dir = project_root() / "configs"
    return sorted(config_dir.glob("*.yaml"))
