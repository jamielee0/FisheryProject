# Trees to Seas: Dynamic Habitat Stress Exposure for North Carolina Estuarine Fisheries

Retrospective, externally-validated habitat-stress exposure study built around
NCDMF/SEAMAP Program 195 tow-level fishery-independent survey data, joined to
ModMon, FerryMon, USGS, NOAA, drought, rainfall, and land-cover covariates.

**This is not a causal paper.** See `CLAIM_BOUNDARIES.md`.

---

## Status

Pre-analysis — repository initialization. No data ingested. No models run.

---

## Species

**Primary:** Blue crab, Atlantic croaker, Spot
**Conditional:** Southern flounder (occurrence/CPUE/biomass only pending endpoint confirmation)
**Excluded (first paper):** Atlantic menhaden
**Separate module:** Eastern oyster (only if outcome data confirmed)

---

## Model Ladder

| Model | Description |
|-------|-------------|
| A | Static survey baseline |
| B | Dynamic water-quality model |
| C | Species-specific stress exposure model |
| D | Land-to-sea incremental predictor model |
| Benchmark | Interpretable boosted tree / random forest |

---

## Repository Structure

```
FisheryProject/
├── CLAUDE.md                  # Binding rules for Claude Code sessions
├── PROJECT_CHARTER.md         # Study design and milestones
├── CLAIM_BOUNDARIES.md        # Allowed and forbidden claims
├── species_traits.yaml        # Species biological traits (placeholder)
├── threshold_table.csv        # Water-quality thresholds (placeholder)
├── endpoint_verification.md   # Survey endpoint verification log
├── RELATED_WORK_MATRIX.md     # Prior literature and methods
├── SOURCE_QUALITY_AUDIT.md    # Data source documentation
│
├── configs/                   # YAML configs (paths, parameters)
├── data/
│   ├── raw/                   # Original data — never committed
│   ├── interim/               # Intermediate — never committed
│   ├── processed/             # Final features — never committed
│   └── external/              # External reference data
├── metadata/                  # Data dictionaries, station lists, codebooks
│
├── src/trees_to_seas/
│   ├── ingest/                # Data ingestion scripts
│   ├── qa/                    # Quality assurance and flagging
│   ├── endpoints/             # Survey endpoint construction
│   ├── features/              # Feature engineering
│   ├── joins/                 # Spatial/temporal joins
│   ├── models/                # Model training
│   ├── evaluation/            # Validation and metrics
│   ├── visualization/         # Figures and maps
│   ├── reports/               # Report generation
│   └── utils/                 # Shared utilities
│
├── notebooks/                 # Exploration only — no production logic
├── scripts/                   # CLI entry points
├── tests/                     # pytest tests
├── results/                   # Model outputs — not committed
├── figures/                   # Figures — not committed
└── manuscript/                # Manuscript drafts
```

---

## Setup

```bash
# Create environment
conda env create -f environment.yml
conda activate trees_to_seas

# Install package (editable)
pip install -e .

# Run smoke test
pytest tests/test_smoke.py -v
```

---

## Key Rules

- Read `CLAUDE.md` before starting any session
- Read `CLAIM_BOUNDARIES.md` before writing any results or manuscript text
- Read `endpoint_verification.md` before writing endpoint-specific code
- No results from this repository should be interpreted causally
- All headline results require temporal, spatial, and event holdout validation
