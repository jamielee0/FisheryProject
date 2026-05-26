.PHONY: install test lint clean help

help:
	@echo "Usage:"
	@echo "  make install   Install package in editable mode with dev dependencies"
	@echo "  make test      Run pytest smoke test and full test suite"
	@echo "  make lint      Run ruff linter"
	@echo "  make clean     Remove build artifacts and caches"

install:
	pip install -e ".[dev]"

test:
	pytest tests/ -v --tb=short

smoke:
	pytest tests/test_smoke.py -v

lint:
	ruff check src/ tests/

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".ruff_cache" -exec rm -rf {} +
	rm -rf dist/ build/ htmlcov/ .coverage coverage.xml
