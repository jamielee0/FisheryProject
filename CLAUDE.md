# CLAUDE.md - Legacy Agent Instructions

This file is retained for historical continuity. `AGENTS.md` is the active
Codex instruction set for this repository. Preserve the scientific constraints
below unless they are intentionally migrated into `AGENTS.md` or another
Codex-facing project file.

---

## 1. Project Identity

**Full title:** Trees to Seas: Dynamic Habitat Stress Exposure for North Carolina Estuarine Fisheries
**Type:** Retrospective, externally-validated habitat-stress exposure study
**What this is not:** a causal land-use, pollution, forestry, hog-agriculture, or management-failure paper

---

## 2. Scientific Direction (binding)

The strongest first paper is built around **NCDMF/SEAMAP Program 195 tow-level fishery-independent
survey data through 2024**, joined to ModMon, FerryMon, USGS, NOAA, drought, rainfall, and
land-cover covariates.

Land-to-sea variables are **incremental, noncausal predictors** — not headline causal claims.
Every variable added after measured water quality and hydrology must earn its place by improving
held-out performance.

---

## 3. Species Scope

### Primary (all endpoints)
- Blue crab (*Callinectes sapidus*)
- Atlantic croaker (*Micropogonias undulatus*)
- Spot (*Leiostomus xanthurus*)

### Conditional (occurrence/CPUE/biomass only)
- Southern flounder (*Paralichthys lethostigma*) — include as occurrence/CPUE/biomass only.
  Do **not** use a juvenile endpoint unless Program 195 juvenile data are explicitly confirmed
  and documented in `endpoint_verification.md`.

### Excluded from first paper
- Atlantic menhaden — excluded unless a menhaden-specific survey endpoint is added and
  documented in `endpoint_verification.md`.

### Separate module only
- Eastern oyster — only if oyster outcome data exist. Must not appear in the primary
  Program 195 analysis without its own documented endpoint.

---

## 4. Model Ladder

| Label       | Description                                      |
|-------------|--------------------------------------------------|
| Model A     | Static survey baseline                           |
| Model B     | Dynamic water-quality model                      |
| Model C     | Species-specific stress exposure model           |
| Model D     | Land-to-sea incremental predictor model          |
| Benchmark   | Interpretable boosted tree or random forest      |

The benchmark model **must never be presented as the only model**.

---

## 5. Validation Requirements (all required, no exceptions)

- **Temporal holdout** — a contiguous time window held out, not random years
- **Spatial holdout** — stations or clusters withheld geographically
- **Event holdout** — specific named storm / drought / hypoxia events withheld
- **Ablations** — covariates added in order; each step must show held-out change
- **Calibration** — reliability diagrams and/or ECE reported for probabilistic outputs
- **Uncertainty** — prediction intervals or posterior distributions reported
- **Leakage audit** — documented in `leakage_audit.md` before any results are finalized

**No random-split headline claims.** Any result reported only under random splits must be
clearly labeled as "exploratory, not externally validated."

---

## 6. Core Publication Risks (track in code and comments)

1. Environmental interpolation leakage
2. Spatial autocorrelation
3. Station memorization
4. Sparse bottom-water observations
5. Surface water quality being treated as bottom habitat
6. Weak thresholds used as hard biological truth
7. Croaker June juvenile cutoff conflict
8. Spot June FL/TL unit conflict
9. Southern flounder juvenile endpoint uncertainty

Every feature-engineering or join step must note which of these risks it touches.

---

## 7. Forbidden Claims

Never write, imply, or allow any analysis to suggest:

- Land use caused fishery decline
- Forestry caused collapse
- Hog agriculture caused collapse
- Management killed the fishery
- Pollution caused abundance change
- A predictive model proves causation
- Generic DO, pH, chlorophyll, or turbidity thresholds are species-specific lethal thresholds
- Maps are decision-ready without calibration and uncertainty quantification

Violation of this list is a hard stop. Do not proceed with any code path or narrative that
leads toward these claims.

---

## 8. Allowed Claims (if, and only if, supported by held-out validation)

- Dynamic environmental covariates improved held-out prediction
- Species-specific stress exposure metrics were predictive under blocked validation
- Suitable / marginal / dangerous habitat states shifted across windows, years, or event
  conditions — within stated uncertainty
- Dynamic habitat conditions can help interpret fixed-window fishery-independent survey
  observations
- Land-cover or watershed variables added incremental predictive value — only if they improve
  held-out performance after measured water quality and hydrology are already included

---

## 9. Data Rules

- **Do not fabricate data.** Placeholder files must be clearly marked `# PLACEHOLDER`.
- **Do not create fake model results.** Any result file must come from actual code runs.
- Thresholds in `threshold_table.csv` are literature-sourced candidates, not verified ground
  truth. Mark `verified = FALSE` until cross-checked against primary sources.
- Raw data files must never be committed. See `.gitignore`.

---

## 10. Code Standards

- Python ≥ 3.11; follow `pyproject.toml` dependency pins
- All functions that touch data must have a docstring stating: inputs, outputs, and which
  publication risks (#1–9 above) the function is relevant to
- Feature engineering functions must note whether they operate on surface or bottom observations
- No hard-coded file paths; use `configs/` YAML for all path and parameter configuration
- Every model training script must log the random seed, data hash, and split strategy
- Tests live in `tests/`; run with `pytest` from the project root
- Notebooks in `notebooks/` are for exploration only; no production logic in notebooks

---

## 11. Behavior Rules for Claude Code

- Read `CLAIM_BOUNDARIES.md` before writing any results narrative or manuscript text
- Read `endpoint_verification.md` before writing any endpoint-specific code
- Read `threshold_table.csv` before hardcoding any biological threshold
- Read `species_traits.yaml` before writing species-specific logic
- When adding a new data source, add it to `SOURCE_QUALITY_AUDIT.md` first
- When adding a new model or validation method, check `RELATED_WORK_MATRIX.md` for prior art
- Do not add features, refactor, or "improve" code beyond the explicit task
- Do not add comments, docstrings, or type annotations to code you did not change
- Do not create documentation files unless explicitly requested
- Prefer editing existing files over creating new ones
- Keep responses concise; lead with action, not reasoning

---

## 12. Temporal Holdout Specification (binding)

```
Training:    1995–2016
Validation:  2017–2019
Test:        2022–2024   ← manuscript headline performance
Sensitivity: 2020–2021 included, excluded, and flagged separately
```

Program 195 was suspended in 2025. Do not assume 2025+ continuity.
2020–2021 COVID sampling disruptions must be handled in sensitivity analyses.

**Rolling-origin folds (for model selection only — NOT headline claims):**
```
Fold 1: train 1995–2005, test 2006–2009
Fold 2: train 1995–2009, test 2010–2013
Fold 3: train 1995–2013, test 2014–2017
Fold 4: train 1995–2017, test 2018–2024
```

Every training script must log: random seed, data hash, split strategy, and fold ID.
Every result reported outside these folds must be labeled "exploratory" or "sensitivity."

---

## 13. Success Thresholds (pre-specified, binding)

A result is a headline success if **all** of the following hold:

- Model B or C improves held-out performance over Model A by **≥10%** in primary loss metric
  (log loss or Brier score for occurrence; RMSE on log(CPUE+1) for abundance)
- The improvement holds for **at least two core species** (blue crab, croaker, spot)
- Calibration slope is near 1; no severe overprediction
- Stress-response curves are biologically interpretable with uncertainty

**Important:** 10% is a reporting threshold, not a reject threshold. A result below 10% that is
well-calibrated and interpretable can still be published as a negative/partial result.

---

## 14. Negative Publishable Outcome (binding)

The project remains publishable as a rigorous negative result if:
- Dynamic water-quality covariates do not improve held-out prediction beyond static survey strata
- Land-cover variables add no value beyond measured water quality
- Species thresholds borrowed from literature are not transferable to NC conditions
- Static survey design explains most variation in catch
- Water-quality monitoring is too sparse for reliable bottom-habitat prediction for demersal species

Frame as: "A rigorous blocked-validation test showed that widely available dynamic environmental
datasets were insufficient to improve held-out prediction of fishery-independent estuarine survey
outcomes, highlighting the need for better bottom-water monitoring, species-specific thresholds,
and validation before habitat stress indicators are used operationally."

This framing is a credible contribution to Ecological Informatics or Ecological Indicators.

---

## 15. Context Files — Reading Order on Session Start

Before any analysis or coding session, read in this order:
1. `CLAUDE.md` (this file)
2. `CLAIM_BOUNDARIES.md`
3. `endpoint_verification.md`
4. `species_traits.yaml`
5. `threshold_table.csv` (if writing threshold-dependent code)
6. `SOURCE_QUALITY_AUDIT.md` (if writing ingest code)
7. `RELATED_WORK_MATRIX.md` (if designing a new model or validation method)
8. `manuscript/positioning_notes.md` (if writing manuscript text)
