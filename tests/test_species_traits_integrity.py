"""Integrity checks for species trait guardrails and unresolved endpoint conflicts."""

from __future__ import annotations

from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
SPECIES_TRAITS_PATH = REPO_ROOT / "species_traits.yaml"


def load_species_traits_document() -> dict:
    with SPECIES_TRAITS_PATH.open(encoding="utf-8") as file:
        parsed = yaml.safe_load(file)
    assert isinstance(parsed, dict)
    return parsed


def load_species_traits() -> dict:
    parsed = load_species_traits_document()
    assert isinstance(parsed, dict)
    assert isinstance(parsed.get("species_traits"), dict)
    return parsed["species_traits"]


def find_model_use_values(value: object) -> set[str]:
    if isinstance(value, dict):
        found = set()
        for key, child in value.items():
            if key == "model_use":
                assert isinstance(child, str)
                found.add(child)
            found.update(find_model_use_values(child))
        return found
    if isinstance(value, list):
        found = set()
        for child in value:
            found.update(find_model_use_values(child))
        return found
    return set()


def test_required_species_exist() -> None:
    traits = load_species_traits()
    required = {"blue_crab", "atlantic_croaker", "spot", "southern_flounder"}
    assert required.issubset(traits)


def test_all_model_use_values_are_declared() -> None:
    parsed = load_species_traits_document()
    allowed = set(parsed["allowed_model_use_values"])
    found = find_model_use_values(parsed)

    assert found
    assert found.issubset(allowed)


def test_croaker_june_cutoff_conflict_is_preserved() -> None:
    traits = load_species_traits()
    endpoints = traits["atlantic_croaker"]["life_stages"]["juvenile"]["endpoint_definitions"]

    latest = endpoints["program195_june_juvenile_latest_candidate"]
    alternate = endpoints["program195_june_juvenile_alternate"]

    assert latest["value"] == 140
    assert alternate["value"] == 160
    assert latest["unit"] == "mm total length"
    assert alternate["unit"] == "mm total length"
    assert latest["verified"] is False
    assert alternate["verified"] is False
    assert latest["conflict_flag"] is True
    assert "160" in latest["conflict_note"]


def test_spot_june_unit_conflict_is_preserved() -> None:
    traits = load_species_traits()
    endpoints = traits["spot"]["life_stages"]["juvenile"]["endpoint_definitions"]
    june = endpoints["program195_june_juvenile"]

    assert june["value"] == 140
    assert june["verified"] is False
    assert june["conflict_flag"] is True
    assert "FL" in june["conflict_note"]
    assert "TL" in june["conflict_note"]


def test_southern_flounder_juvenile_endpoint_remains_unverified() -> None:
    traits = load_species_traits()
    endpoint = (
        traits["southern_flounder"]["life_stages"]["juvenile"]["endpoint_definitions"][
            "program195_length_based_juvenile"
        ]
    )

    assert endpoint["value"] is None
    assert endpoint["unit"] is None
    assert endpoint["verified"] is False
    assert endpoint["model_use"] == "do_not_use_until_confirmed"


def test_menhaden_is_not_core_or_primary() -> None:
    traits = load_species_traits()
    menhaden = traits["atlantic_menhaden"]

    assert menhaden["model_role"] != "core"
    assert "primary" not in menhaden["model_role"].lower()
    assert "EXCLUDED" in menhaden["status"]


def test_oyster_is_separate_module_only() -> None:
    traits = load_species_traits()
    oyster = traits["eastern_oyster"]

    assert "separate_module_only" in oyster["model_role"]
    assert "SEPARATE MODULE ONLY" in oyster["status"]
