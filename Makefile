.PHONY: help install test smoke lint clean

help:
	@echo "Available targets:"
	@echo "  make install  Install the package in editable mode with dev dependencies"
	@echo "  make test     Run the full pytest suite"
	@echo "  make smoke    Run only smoke tests"
	@echo "  make lint     Run ruff against source and tests"
	@echo "  make clean    Remove local Python build, lint, and test artifacts"

install:
	python -m pip install -e ".[dev]"

test:
	python -m pytest

smoke:
	python -m pytest tests/test_smoke.py

lint:
	python -m ruff check src tests

clean:
	python -c "import pathlib, shutil; [shutil.rmtree(p, ignore_errors=True) for p in pathlib.Path('.').rglob('__pycache__')]"
	python -c "import pathlib, shutil; [shutil.rmtree(p, ignore_errors=True) for p in pathlib.Path('.').rglob('*.egg-info')]"
	python -c "import pathlib, shutil; [shutil.rmtree(p, ignore_errors=True) for p in ['build', 'dist', 'htmlcov', '.pytest_cache', '.ruff_cache']]"
	python -c "import pathlib; [p.unlink(missing_ok=True) for p in [pathlib.Path('.coverage'), pathlib.Path('coverage.xml')]]"
