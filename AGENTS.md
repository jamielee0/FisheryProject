# AGENTS.md - Codex Instructions for Trees to Seas

This file is the active Codex instruction set for this repository and should be
read before editing code, configuration, documentation, or tests.

Preserve this readable Markdown structure when editing; do not collapse or
weaken any scientific rule, species scope, validation rule, or claim boundary.

## Project Identity

Full title: Trees to Seas: Dynamic Habitat Stress Exposure for North Carolina
Estuarine Fisheries.

Study type: retrospective, externally validated habitat-stress exposure study.

This project is not a causal land-use, pollution, forestry, hog-agriculture, or
management-failure paper.

Core study unit: NCDMF/SEAMAP Program 195 Pamlico Sound tow-level
fishery-independent data through 2024, joined in later tasks to dynamic
water-quality, hydrologic, meteorological, drought, storm, and land-cover
covariates.

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

| Label | Description |
| --- | --- |
| Model A | Static survey baseline |
| Model B | Dynamic water-quality model |
| Model C | Species-specific stress exposure model |
| Model D | Land-to-sea incremental predictor model |
| Benchmark | Interpretable boosted tree or random forest |

The benchmark model must never be the only model.

## Validation Requirements

All headline claims require:

- Temporal holdout
- Spatial holdout
- Event holdout
- Ablation study
- Calibration
- Uncertainty quantification
- Leakage audit

No random-split headline claims are allowed. Random-split results may only be
reported as exploratory and not externally validated.

Temporal holdout:

- Train: 1995-2016
- Validation: 2017-2019
- Test: 2022-2024
- Sensitivity: 2020-2021 included, excluded, and flagged separately

Rolling-origin folds:

- Fold 1: train 1995-2005, test 2006-2009
- Fold 2: train 1995-2009, test 2010-2013
- Fold 3: train 1995-2013, test 2014-2017
- Fold 4: train 1995-2017, test 2018-2024

## Data Rules

- Do not fabricate data, results, citations, model performance, maps, or
  scientific conclusions.
- Do not create fake data files or fake model outputs.
- Raw data, interim data, processed data, results, and figures must not be
  committed except for `.gitkeep` placeholders.
- Placeholder config and metadata files must be clearly empty templates.
- Thresholds in `threshold_table.csv` are candidate literature or agency values,
  not verified ground truth unless explicitly marked verified.
- Surface water-quality observations must never be treated as bottom habitat for
  demersal species without depth-specific documentation.

## Core Publication Risks

Track these risks in future data-touching functions, joins, features, and model
documentation:

1. Environmental interpolation leakage
2. Spatial autocorrelation
3. Station memorization
4. Sparse bottom-water observations
5. Surface water quality being treated as bottom habitat
6. Weak thresholds used as hard biological truth
7. Croaker June juvenile cutoff conflict
8. Spot June FL/TL unit conflict
9. Southern flounder juvenile endpoint uncertainty

## Forbidden Claims

Never write or imply:

- Land use caused fishery decline
- Forestry caused collapse
- Hog agriculture caused collapse
- Management killed the fishery
- Pollution caused abundance change
- A predictive model proves causation
- Generic DO, pH, chlorophyll, or turbidity thresholds are species-specific
  lethal thresholds
- Maps are decision-ready without calibration and uncertainty

## Allowed Claims

Allowed only if supported by blocked validation:

- Dynamic environmental covariates improved held-out prediction.
- Species-specific stress exposure metrics were predictive under blocked
  validation.
- Suitable, marginal, or dangerous habitat states shifted within stated
  uncertainty.
- Dynamic habitat conditions can help interpret fixed-window
  fishery-independent survey observations.
- Land-cover or watershed variables added incremental predictive value after
  measured water quality and hydrology are included.

## Required Reading Before Relevant Tasks

Read these files before work that touches the listed area:

- Always: `CLAIM_BOUNDARIES.md`
- Endpoint-specific logic: `endpoint_verification.md`
- Species-specific logic: `species_traits.yaml`
- Threshold-dependent logic: `threshold_table.csv`
- Data-source or ingest work: `SOURCE_QUALITY_AUDIT.md`
- Model or validation design: `RELATED_WORK_MATRIX.md`
- Manuscript, result narrative, captions, or claims: `CLAIM_BOUNDARIES.md` and
  `manuscript/positioning_notes.md`

## Coding Behavior Rules

- Keep changes scoped to the requested task.
- Prefer existing project structure and naming.
- Do not implement ingestion, joins, feature engineering, modeling, evaluation,
  visualization, or reporting unless explicitly asked.
- Do not add scientific values, thresholds, results, citations, or conclusions
  unless they are traceable to the project source files or verified sources.
- Do not silently resolve endpoint conflicts. Preserve unresolved status and
  document required expert review.
- Use configuration files for paths and parameters; do not hard-code local data
  paths in package code.
- Every future data-touching function must document inputs, outputs, and
  publication risks it touches.
- Run tests and linting after code changes when dependencies are available.
