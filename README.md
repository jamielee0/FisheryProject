# Trees to Seas: Dynamic Habitat Stress Exposure for North Carolina Estuarine Fisheries

Retrospective, externally validated habitat-stress exposure study built around
NCDMF/SEAMAP Program 195 Pamlico Sound tow-level fishery-independent survey data
through 2024, joined later to dynamic water-quality, hydrologic, meteorological,
drought, storm, and land-cover covariates.

This is not a causal land-use, pollution, forestry, hog-agriculture, or
management-failure paper. See `CLAIM_BOUNDARIES.md` before writing results,
figures, captions, abstracts, or manuscript text.

## Status

Pre-analysis repository setup.

- No data have been ingested.
- No models have been run.
- No maps, model outputs, results, or scientific conclusions are present.
- No causal claims are supported by this repository.

## Species Scope

Primary species:

- Blue crab
- Atlantic croaker
- Spot

Conditional species:

- Southern flounder as occurrence, CPUE, or biomass only unless a Program 195
  juvenile endpoint is confirmed in `endpoint_verification.md`.

Excluded from the first Program 195-centered paper:

- Atlantic menhaden unless a menhaden-specific survey endpoint is added.

Separate module only:

- Eastern oyster, only if oyster mortality, spatfall, growth, reef condition,
  restoration survival, harvest closure, or another oyster outcome is confirmed.

## Model Ladder

| Model | Description |
| --- | --- |
| Model A | Static survey baseline |
| Model B | Dynamic water-quality model |
| Model C | Species-specific stress exposure model |
| Model D | Land-to-sea incremental predictor model |
| Benchmark | Interpretable boosted tree or random forest, never as the only model |

## Validation Requirements

Headline claims require blocked validation:

- Temporal holdout
- Spatial holdout
- Event holdout
- Ablation study
- Calibration
- Uncertainty quantification
- Leakage audit

Random-split results may only be labeled exploratory and are not valid headline
evidence.

## Setup

```bash
python -m pip install -e ".[dev]"
pytest
ruff check src tests
```

Conda users can create the environment with:

```bash
conda env create -f environment.yml
conda activate trees_to_seas
python -m pip install -e ".[dev]"
```

## Repository Structure

```text
FisheryProject/
|-- AGENTS.md                   # Codex-facing project rules
|-- CLAUDE.md                   # Legacy Claude instructions; AGENTS.md is authoritative
|-- CLAIM_BOUNDARIES.md         # Allowed and forbidden claims
|-- PROJECT_CHARTER.md          # Study design and milestones
|-- endpoint_verification.md    # Survey endpoint verification log
|-- RELATED_WORK_MATRIX.md      # Prior literature and methods matrix
|-- SOURCE_QUALITY_AUDIT.md     # Data source quality notes
|-- species_traits.yaml         # Structured species traits and endpoint caveats
|-- threshold_table.csv         # Candidate thresholds and warnings
|-- configs/                    # YAML configuration placeholders
|-- data/
|   |-- raw/                    # Original data, never committed
|   |-- interim/                # Intermediate data, never committed
|   |-- processed/              # Processed outputs, never committed
|   `-- external/               # External reference data
|-- metadata/                   # Inventory, provenance, dictionary, and decision templates
|-- src/trees_to_seas/          # Python package
|-- tests/                      # Pytest tests
|-- results/                    # Reproducible outputs, not committed
|-- figures/                    # Reproducible figures, not committed
`-- manuscript/                 # Manuscript notes and drafts
```

## Key Rules

- Read `AGENTS.md` before starting a Codex coding session.
- Read `CLAIM_BOUNDARIES.md` before writing results or manuscript text.
- Read `endpoint_verification.md` before writing endpoint-specific code.
- Read `species_traits.yaml` before writing species-specific logic.
- Read `threshold_table.csv` before using any threshold.
- Do not fabricate data, results, citations, model performance, maps, or
  scientific conclusions.
- Do not treat generic DO, pH, chlorophyll, or turbidity screens as verified
  species-specific lethal thresholds.
- Do not present land-cover or watershed covariates as causal drivers.
