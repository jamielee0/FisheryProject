"""Guardrails against committing raw data, generated results, or local secrets."""

from __future__ import annotations

import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

PROTECTED_PATHS = [
    "data/raw",
    "data/interim",
    "data/processed",
    "results",
    "figures",
]


def git_ls_files(*paths: str) -> list[str]:
    result = subprocess.run(
        ["git", "ls-files", *paths],
        cwd=REPO_ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def test_protected_data_and_output_directories_only_commit_gitkeep() -> None:
    tracked_files = git_ls_files(*PROTECTED_PATHS)
    unexpected = [path for path in tracked_files if Path(path).name != ".gitkeep"]

    assert not unexpected, f"Unexpected tracked data/output files: {unexpected}"


def test_env_file_is_not_present_or_tracked() -> None:
    assert not (REPO_ROOT / ".env").exists(), ".env file must not be present in the repo"
    assert not git_ls_files(".env"), ".env file must not be tracked"
