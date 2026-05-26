# CLAIM_BOUNDARIES.md
## Allowed and Forbidden Claims — Trees to Seas

This file is **binding**. Every result narrative, manuscript section, figure caption, abstract,
presentation slide, and code comment that generates outputs must be checked against it.

Codex must read this file before writing any results text, manuscript text, or figure captions.

---

## 1. Forbidden Claims — Hard Stop (8 Rules)

These claims must never appear in any output from this repository — in any form, including
implication, hedged language, "preliminary evidence," or cautious wording that still moves in
this direction.

| # | Forbidden claim |
|---|-----------------|
| 1 | Land use caused fishery decline |
| 2 | Forestry caused collapse |
| 3 | Hog agriculture caused collapse |
| 4 | Management killed the fishery |
| 5 | Pollution caused abundance change |
| 6 | A predictive model proves causation |
| 7 | Generic DO, pH, chlorophyll, or turbidity thresholds are species-specific lethal thresholds |
| 8 | Maps are decision-ready without calibration and uncertainty quantification |

If any draft text edges toward these claims, stop and rewrite using the allowed-claim language below.

---

## 2. Allowed Claims — With Conditions

Each claim is allowed **if and only if** the stated condition is met. Do not report a claim without
satisfying its condition first.

| # | Allowed claim | Condition |
|---|---------------|-----------|
| 1 | Dynamic environmental covariates improved held-out prediction | Must show metric improvement under temporal/spatial/event holdout — not random split only |
| 2 | Species-specific stress exposure metrics were predictive under blocked validation | Must use blocked CV or holdout, not random split |
| 3 | Suitable / marginal / dangerous habitat states shifted across windows, years, or event conditions — within stated uncertainty | Uncertainty intervals must be shown; maps must include uncertainty mask |
| 4 | Dynamic habitat conditions can help interpret fixed-window fishery-independent survey observations | Framed as interpretive aid, not causal explanation |
| 5 | Land-cover or watershed variables added incremental predictive value | Held-out improvement must be shown after measured water quality and hydrology are already included |

---

## 3. Language Guide

| Avoid | Use instead |
|-------|-------------|
| "caused" | "was associated with" / "co-occurred with" |
| "drove" | "was predictive of" (under held-out validation) |
| "explains the decline" | "partially accounts for variance in survey catch" |
| "proves" | "is consistent with" / "supports the hypothesis" |
| "shows that X kills/harms" | "threshold X is associated with reduced predicted catch" |
| "management failure led to" | [delete — not in scope] |
| "habitat is degraded" | "habitat stress exposure metrics indicate marginal or dangerous states" |
| "the model predicts real outcomes" | "the model reproduced held-out observations within stated uncertainty" |
| "land use caused fish declines" | "watershed and land-cover covariates were associated with dynamic habitat stress exposure and improved held-out prediction" |
| "collapse" | "abundance change" / "survey index decline" |
| "dynamic models should replace surveys" | "dynamic models can help interpret fixed-window survey observations" |
| "fixed survey design is flawed" | [delete or reframe as: surveys are consistent but conditioned by habitat] |

---

## 4. Threshold Claims — Special Rules

Thresholds from `threshold_table.csv` are **literature-sourced candidates**, not verified lethal
or sublethal ground truth for this system.

- Never present a generic literature threshold as a confirmed species-specific endpoint for North
  Carolina estuarine conditions without a primary source that is verified.
- Always report the source and `verified` status when citing a threshold.
- Calibration and uncertainty must accompany any threshold-based habitat state map.
- Use **soft threshold functions** (exposure curves, percentile ranks, anomalies) rather than
  single hard cutoffs whenever possible.
- For every threshold used in a model, report a sensitivity analysis with alternate threshold values.

**Threshold uncertainty class definitions:**

| Class | Meaning |
|-------|---------|
| High | Local or regional, species-specific, life-stage-relevant threshold from NC or nearby estuarine literature |
| Medium | Species-specific threshold from another estuary, lab study, or management document — not perfectly matched to NC life stage or season |
| Low | Generic estuarine, related-species, or expert-informed threshold — use only for sensitivity analysis |
| Unknown | Do not parameterize without expert review |

---

## 5. Random-Split Results

Results from random train/test splits may be reported **for exploration only**, clearly labeled:
*"exploratory, not externally validated."*

No headline abstract claim or conclusion may rest on random-split performance alone.

---

## 6. Reviewer Objections and Defenses by Journal

### Ecological Informatics
**Likely objections:**
- The ML contribution may look too routine.
- The model may look like a dashboard rather than a methodological paper.
- Random forest/XGBoost results may be criticized as black-box curve fitting.
- Reviewers will look hard for leakage between training and test periods.
- Spatial autocorrelation may inflate performance.

**Defense:**
- Use blocked temporal, spatial, and event validation.
- Make the model ladder the methodological contribution.
- Use interpretable GAMM/GLMM/spatial-temporal models as primary; boosted trees only as benchmark.
- Report calibration, uncertainty, ablations, and reproducible code.
- The journal's scope explicitly includes ecological data acquisition/management/analysis, ML,
  Bayesian inference, species distribution modelling, and forecasting ecosystem functioning.

### Ecological Indicators
**Likely objections:**
- The habitat stress score may look arbitrary.
- Thresholds may be borrowed from other systems.
- A single case study may not meet the journal's indicator-development standard.
- Reviewers may ask whether the indicator is validated against biological endpoints.

**Defense:**
- Call the metric "habitat stress exposure," not "ecosystem health."
- Use threshold uncertainty classes.
- Validate the indicator against held-out occurrence, CPUE, biomass, and juvenile indices.
- Report sensitivity to threshold choice.
- Show that the indicator adds predictive value beyond static survey design.

### Ocean & Coastal Management
**Likely objections:**
- The paper may be too technical and not management-facing enough.
- Maps could be misread as regulatory prescriptions.
- Reviewers may ask how the model changes decisions.
- Agency reviewers may object to unsupported claims about management failure.

**Defense:**
- Frame outputs as decision-support layers, not management mandates.
- Include a section on how dynamic habitat stress maps complement stock assessment and survey design.
- Include NCDMF or coastal-management coauthor review.
- Show use cases: survey interpretation, event-response monitoring, habitat-risk communication.

### Marine Pollution Bulletin
**Likely objections:**
- The pollution link may be too indirect.
- Land-use/CAFO/forestry/sediment proxies may not be measured pollutant loads.
- A model-only paper may not satisfy pollution-measurement expectations.

**Defense:**
- Center directly measured water-quality variables: DO, turbidity, chlorophyll, nutrients where
  available, pH, salinity, temperature.
- Treat land-use variables as proxies, not pollution measurements.
- Use "associated with habitat stress exposure," not "caused by pollution."
- For this journal, strengthen nutrient/turbidity/hypoxia/eutrophication analyses.

### Environmental Modelling & Software
**Likely objections:**
- No formal software contribution.

**Defense:**
- If targeting this journal, provide an open package, dashboard, or reusable API.
- Emphasize reproducibility checklist, model evaluation, and documentation.

---

## 7. Journal-Specific Title and Abstract Framing

### Ecological Informatics framing
- **Title:** Blocked validation of dynamic habitat-stress exposure models for North Carolina estuarine fisheries
- **Abstract thesis:** Long-term fishery-independent surveys can be transformed into externally validated habitat-stress exposure models when tow-level observations are joined to dynamic WQ, hydrologic, meteorological, and watershed covariates with strict temporal/spatial/event holdouts.
- **Main contribution:** A leakage-resistant ecological informatics workflow for integrating Program 195, ModMon/FerryMon, USGS, NOAA, drought, rainfall, and land-cover products.
- **Must-have:** Calibration, blocked validation, ablation by data source, threshold sensitivity, uncertainty masks.
- **Claim to avoid:** "Machine learning discovered the cause of decline."

### Ecological Indicators framing
- **Title:** A validated habitat-stress exposure indicator for fishery-independent estuarine surveys in Pamlico Sound
- **Abstract thesis:** Species-specific exposure to hypoxia, heat, salinity shock, freshwater pulses, and bloom/turbidity anomalies can be summarized as interpretable indicators and tested against held-out biological endpoints.
- **Main contribution:** A validated, uncertainty-labeled suitable/marginal/dangerous habitat exposure indicator.
- **Must-have:** Indicator sensitivity to thresholds, reliability curves, class calibration, uncertainty bands, species-by-species performance.
- **Claim to avoid:** "This index measures ecosystem health."

### Ocean & Coastal Management framing
- **Title:** Dynamic habitat stress maps for interpreting fixed-window estuarine fishery-independent surveys
- **Abstract thesis:** Dynamic WQ and hydrologic conditions can affect how fixed survey-window observations are interpreted, and calibrated habitat-stress maps can support monitoring design and event-response interpretation.
- **Must-have:** Management use cases, uncertainty mask, "what this does/does not support" table, event holdout.
- **Claim to avoid:** "Management failure caused collapse."

---

## 8. Discussion Claim Boundary Section

### Supported if models perform well

**Allowed in Discussion:**
- Dynamic WQ, hydrologic, meteorological, and watershed covariates improved held-out prediction relative to static survey strata for specified species and endpoints.
- Species-specific stress exposure metrics were predictive of occurrence, CPUE, biomass, or juvenile-index outcomes under blocked validation.
- Suitable, marginal, and dangerous habitat states shifted across survey windows, years, or event conditions — within mapped uncertainty.
- Dynamic habitat conditions can help interpret fixed-window fishery-independent survey observations.
- Land-cover or watershed variables added incremental predictive value, if and only if they improve held-out performance after measured WQ/hydrology covariates are included.

### Only suggestive (cautious language required)

**Cautious claims allowed in Discussion:**
- Patterns are consistent with stress-related redistribution.
- Freshwater pulses, drought, or storm windows may alter the spatial distribution of suitable habitat.
- Watershed conditions may help predict estuarine WQ stress exposure.
- Survey catchability may be affected by environmental conditions.
- Borrowed thresholds may or may not transfer to NC; model validation provides an empirical test.

### Not supported (forbidden in any section)

- Land use caused fishery decline.
- Forestry, agriculture, hog operations, or nutrient pollution caused species collapse.
- Management caused collapse or failed to prevent collapse.
- Habitat stress maps prove mortality.
- Generic DO, pH, chlorophyll, or turbidity screens are species-specific lethal thresholds.
- Great Lakes habitat degradation proves North Carolina causality.
- A high-performing predictive model proves mechanism or causation.
- A map without calibration and uncertainty is decision-ready.

### Required direct statement in Methods or Discussion

> This study estimates predictive associations between dynamic environmental conditions and
> fishery-independent survey outcomes. It does not estimate causal effects of land use,
> management policy, or individual pollution sources.

---

## 9. Novelty Paragraph (for Introduction)

The novelty of *Trees to Seas* is the integration of long-term Program 195 fishery-independent
tow-level data with dynamic water-quality, hydrologic, meteorological, drought, storm, and
watershed covariates to produce externally validated, species-specific habitat stress exposure
indicators for North Carolina estuarine fishes and blue crab. Prior literature documents Program
195 indices, Neuse/Pamlico water-quality dynamics, hypoxia, species-specific stress responses,
habitat suitability modelling, and blocked validation methods separately. The new contribution
is to combine those elements into a calibrated static-versus-dynamic model ladder, test it under
temporal, spatial, and event holdouts, report uncertainty and ablations, and use land-to-sea
variables only as incremental, noncausal predictors of stress exposure and biological survey outcomes.

---

## 10. Revision Log

| Date | Change | Author |
|------|--------|--------|
| 2026-05-25 | Initial placeholder | Claude Code |
| 2026-05-25 | Populated from Prompts 1 + 3 | Claude Code |
