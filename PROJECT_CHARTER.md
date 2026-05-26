# PROJECT_CHARTER.md
## Trees to Seas: Dynamic Habitat Stress Exposure for North Carolina Estuarine Fisheries

**Status:** Pre-analysis — context files populated from Prompts 1–3
**Last updated:** 2026-05-25

---

## 1. One-Sentence Journal-Ready Thesis

Dynamic water-quality, hydrologic, meteorological, and watershed covariates can be integrated
with long-term fishery-independent estuarine survey data to estimate species-specific habitat
stress exposure and test whether shifting suitable, marginal, and dangerous habitat states predict
North Carolina estuarine fish and blue crab occurrence, CPUE, and juvenile indices better than
static survey strata alone.

---

## 2. Study Design

**Type:** Retrospective, externally validated habitat-stress exposure study.
**What this is not:** A causal land-use, pollution, forestry, hog-agriculture, or management-failure paper.
**Frame:** Predictive and associational. No causal claims unless a separate causal design is implemented.

**Temporal scope:** Preferred retrospective window **1995–2024**. ModMon begins ~1994; Program 195
provides long-term survey structure. Program 195 suspended 2025 — do not assume 2025+ continuity.
2020–2021 COVID-disrupted sampling must be treated as sensitivity years (include, exclude, and flag).

**Spatial scope:** Pamlico Sound plus lower Neuse, Pamlico, and Pungo river estuarine survey strata.
A Neuse-centered version is acceptable if water-quality coverage is strongest there.

---

## 3. Main Research Question

Do dynamic water-quality, hydrologic, meteorological, and watershed covariates improve temporally
and spatially held-out prediction of estuarine species occurrence, CPUE, biomass, and juvenile
indices relative to a static survey-stratum baseline, and can those covariates be transformed into
interpretable species-specific habitat stress exposure indicators?

---

## 4. Five Falsifiable Hypotheses

**H1. Dynamic habitat hypothesis.**
Models that include dynamic water-quality variables — temperature, salinity, dissolved oxygen,
turbidity, chlorophyll a, pH, Secchi depth, and lagged anomalies — will outperform a static
survey baseline in temporally and spatially held-out prediction of occurrence and CPUE for at
least one core species.

**H2. Species-specific stress exposure hypothesis.**
Cumulative exposure to low dissolved oxygen, heat stress, salinity shock, and high turbidity
or chlorophyll will be associated with lower occurrence, lower CPUE, or spatial redistribution,
but the strength and direction of association will differ among blue crab, Atlantic croaker, spot,
and southern flounder.

**H3. Event-lag hypothesis.**
Rainfall, river discharge, drought, and storm-window covariates at biologically plausible lags
will improve prediction of estuarine habitat stress exposure during fixed survey windows, especially
near the river-estuary transition and in shallow or stratified zones.

**H4. Watershed-to-estuary hypothesis.**
Land-cover, cropland, developed land, wetland, forest, and optional nutrient/sediment/CAFO/forestry
proxies will add predictive value mainly when summarized by hydrologically meaningful catchments and
interpreted through water-quality stress pathways — not as direct causal predictors of catch.

**H5. Indicator robustness hypothesis.**
A habitat stress exposure score will remain calibrated and interpretable under blocked temporal,
spatial, and event holdouts; if it only performs under random cross-validation, it should be
rejected as overfit.

---

## 5. Minimum Publishable Unit

| Component           | Specification                                                                                                              |
|---------------------|----------------------------------------------------------------------------------------------------------------------------|
| Region              | Pamlico Sound and adjacent lower Neuse, Pamlico, and Pungo estuarine survey strata. Neuse-centered version acceptable.   |
| Years               | Preferred: 1995–2024. Flag/exclude 2020–2021 in primary model; include in sensitivity. No 2025+ assumed.                 |
| Core species        | Atlantic croaker, spot, blue crab — strongest Program 195 fishery-independent endpoints.                                  |
| Secondary species   | Southern flounder if sample size supports; must be occurrence/CPUE/biomass only unless P195 juvenile endpoint confirmed.  |
| Excluded            | Atlantic menhaden — only if Program 915, 120, or menhaden-specific endpoint is added.                                    |
| Separate module     | Eastern oyster — only if mortality/growth/spatfall/reef-condition outcomes are available.                                 |
| Core datasets       | Program 195 tow-level; ModMon; FerryMon; NOAA station; USGS streamflow and WQ; NOAA climate/rainfall; U.S. Drought Monitor; NLCD/MRLC; USDA CDL. |
| Optional datasets   | Program 915 gill-net (supplemental validation); forestry harvest; hog CAFO; nutrient loading; sediment/ditching/drainage/point-source proxies only where geocoding, timing, and interpretation are defensible. |
| Response variables  | presence/absence; log(CPUE+1); positive-catch abundance or biomass; length-based juvenile indicators; habitat stress exposure class. |
| Predictors          | Static survey covariates; instantaneous tow environmental data; dynamic water-quality lags; cumulative stress exposure; rainfall/discharge/drought/storm lags; degree-days; salinity shock; turbidity stress; chlorophyll anomaly; land-cover composition; cropland/forest/developed/wetland proportions; distance to river mouth; estuary zone. |

---

## 6. Species Endpoints

| Species             | Endpoint type                 | Survey program  | Endpoint details (see endpoint_verification.md)                       | Verified |
|---------------------|-------------------------------|-----------------|-----------------------------------------------------------------------|----------|
| Blue crab           | Recruit CPUE / biomass        | Program 195     | Recruit: <127 mm CW; Adult: ≥127 mm CW                               | TRUE     |
| Atlantic croaker    | Juvenile CPUE / biomass       | Program 195     | June: <140 mm TL (2024) vs <160 mm TL (2023) CONFLICT; Sept: <210 mm TL | FALSE (CONFLICT) |
| Spot                | Juvenile CPUE / biomass       | Program 195     | June: <140 mm — unit TL vs FL CONFLICT; Sept: <190 mm TL             | FALSE (CONFLICT) |
| Southern flounder   | Occurrence / CPUE / biomass   | Program 195     | No confirmed juvenile cutoff — do not invent one                      | FALSE    |
| Atlantic menhaden   | EXCLUDED from first paper     | —               | —                                                                     | —        |
| Eastern oyster      | Separate module only          | TBD             | Confirm outcome data before any work begins                            | FALSE    |

---

## 7. Model Ladder

### Model A: Static Survey Baseline
**Purpose:** Establish minimum defensible benchmark. Tests how well fixed survey design, geography,
season, and tow metadata explain species observations without dynamic environmental data.

**Recommended formulation:** Hurdle / two-part model (presence/absence then positive CPUE/biomass).
Species-specific GAMM, GLMM, negative-binomial, Tweedie, or lognormal positive-catch model.
Interpretable boosted-tree benchmark acceptable. Deep learning is unnecessary and makes peer review harder.

**Predictors:** year, month/survey wave, stratum, grid/spatial block, latitude/longitude smooth,
depth, tow duration/swept area, gear/vessel metadata, wind/weather/time-of-day where available.

**Main test:** All later models must beat Model A under blocked temporal, spatial, and event validation.

### Model B: Dynamic Water-Quality Model
**Purpose:** Test whether dynamic habitat conditions improve prediction beyond static survey strata.

**Covariates to add:**
- temperature, salinity, dissolved oxygen, turbidity, chlorophyll a, pH, Secchi depth
- surface-bottom stratification, water level or tidal/stage proxy
- seasonal anomaly for each variable
- Lags: same-day, 1d, 3d, 7d, 14d, 30d, 60d, 90d

**Recommended methods:** Primary: species-specific GAMM / hierarchical GLMM / spatial-temporal GAM.
Benchmark: gradient boosted trees or random forest with strict blocked validation.
Do NOT select variables using random CV. Do NOT interpolate future observations into past training folds.
Do NOT tune on test years.

### Model C: Species-Specific Stress and Degree-Day Model
**Purpose:** Convert raw environmental variables into biologically interpretable exposure metrics.
This is the paper's strongest ecological contribution.

**Exposure metrics:**
- hypoxia exposure days/hours (DO below threshold range)
- near-hypoxia exposure
- heat stress degree-days: sum(max(0, temperature − species_threshold))
- cold shock where relevant
- salinity shock: |salinity_t − salinity_{t-k}| over 1–14d windows
- salinity outside preferred range
- turbidity stress: high-percentile turbidity or Secchi anomaly
- chlorophyll bloom anomaly
- stratification exposure
- freshwater pulse exposure
- drought exposure
- storm-window exposure

**Threshold policy:** Use **soft thresholds** and sensitivity ranges. No single brittle cutoff.
All thresholds must have species, life stage, source, and uncertainty class (High/Medium/Low).
See threshold_table.csv.

### Model D: Land-to-Sea Incremental Predictor Model
**Purpose:** Test whether watershed and land-cover information improves prediction of dynamic
habitat stress exposure or biological response, after water quality and hydrology are already included.

**Implementation order:**
- D1. Predict water-quality stress exposure from hydrology + weather + land cover.
- D2. Predict biological response from dynamic stress exposure.
- D3. Add land-cover variables to biological model only after D1 and D2.
- D4. Report whether land-cover variables improve held-out prediction beyond water-quality stress.

**Candidate predictors:** NLCD land-cover class proportions; annual NLCD change metrics; USDA CDL
crop composition; developed land/impervious surface; wetland and forest cover; row crop/pasture/hay;
distance-weighted land cover; upstream HUC or subcatchment summaries; distance to river mouth;
flow-path or residence-time proxy; optional hog CAFO density; optional forestry harvest timing;
optional nutrient loading; optional sediment/turbidity proxy.

**Framing required:** "Watershed and land-cover covariates were associated with dynamic habitat
stress exposure and, in some cases, improved held-out prediction of biological survey outcomes
after accounting for survey design and water-quality dynamics." Never "land use caused fish declines."

### Benchmark
An interpretable boosted tree or random forest must be included for comparison.
**Must never be presented as the only model.**

---

## 8. Validation Design

### Temporal Holdout (Required)
```
Training:    1995–2016
Validation:  2017–2019
Test:        2022–2024
Sensitivity: 2020–2021 included, excluded, and flagged separately
```
Program 195 documented sampling disruptions in 2020–2021; 2025 Program 195 suspended.

**Rolling-origin folds (for model selection):**
```
Fold 1: train 1995–2005, test 2006–2009
Fold 2: train 1995–2009, test 2010–2013
Fold 3: train 1995–2013, test 2014–2017
Fold 4: train 1995–2017, test 2018–2024
```
Use rolling-origin validation for model selection. Use final 2022–2024 test set for manuscript
headline performance.

### Spatial Holdout (Required)
```
Leave-one-stratum-out
Leave-one-river-zone-out
Leave-one-estuary-zone-out
Spatial grid blocks (10–20 km or Program 195 grid groups)
```
Report whether the model can predict in a held-out part of the estuary, not merely interpolate
among nearby tows.

### Event Holdout (Required)
Define events objectively before modeling:
```
High-flow events:   top 5% USGS discharge windows
Heavy-rain events:  top 5% precipitation windows
Drought events:     U.S. Drought Monitor D2+ or bottom-decile flow windows
Storm windows:      named storms or high-wind/high-rain windows, pre-registered before modeling
Hypoxia events:     bottom-decile DO windows or DO below threshold range
Heat events:        top-decile temperature or degree-day windows
```
Hold out entire event windows or event years. Tests generalization to rare but ecologically
important conditions.

### Ablation Study (Required)
```
A vs B vs C vs D (locked sequence)
no ModMon
no FerryMon
no USGS discharge
no NOAA climate
no drought index
no land-cover predictors
no lagged predictors
no species thresholds
no 2020–2021
surface-only water quality
bottom-only water quality
no storm years
```
Report not just "best model" but what information actually mattered.

### Calibration (Required)
**For occurrence:**
- Brier score, log loss, AUC, AUPRC (especially for rare species/rare stress classes)
- Calibration intercept, calibration slope, reliability curves

**For CPUE/biomass:**
- RMSE on log(CPUE+1), MAE, negative log predictive density
- Coverage of 80%, 90%, 95% prediction intervals
- PIT histograms or posterior predictive checks

**For habitat stress classes:**
- Confusion matrix, class-specific sensitivity/specificity
- Calibration by stress class
- Area mapped as suitable/marginal/dangerous with uncertainty

### Uncertainty (Required, 6 Sources)
1. Year-block bootstrap
2. Spatial-block bootstrap
3. Threshold sensitivity
4. Environmental interpolation uncertainty
5. Missing-data imputation
6. Model-class uncertainty

Maps must include an **uncertainty mask**. Areas far from water-quality observations, outside
training range, or interpolated across unsupported space-time gaps must not be shown as
confident predictions.

---

## 9. Success Criteria

**What counts as success:**
Model B or Model C improves temporally and spatially held-out prediction over Model A by a
pre-specified, ecologically meaningful margin, remains calibrated, and produces biologically
interpretable stress-response patterns for at least two core species.

**Practical success thresholds:**
- Occurrence: ≥10% reduction in log loss or Brier score relative to Model A, or meaningful improvement in AUPRC for rare outcomes.
- CPUE/biomass: ≥10% reduction in held-out RMSE or negative log predictive density.
- Calibration: calibration slope near 1; no severe overprediction of high-suitability or high-stress classes.
- Ecological interpretability: stress-response curves consistent with known species biology; uncertainty reported for threshold-dependent results.
- Mapping value: suitable/marginal/dangerous habitat maps identify dynamic changes during wet, dry, warm, hypoxic, or storm-influenced windows.

**Strongest positive result:** Dynamic stress exposure explains spatial redistribution or abundance
changes during survey windows that static strata miss.

---

## 10. Negative but Publishable Outcome

A negative result is still publishable if rigorously validated:

```
Dynamic water-quality data do not improve prediction beyond survey stratum, depth, month, and year.
Species responses are too variable for a stable multispecies stress index.
Land-cover predictors do not improve held-out prediction after measured water quality is included.
Borrowed thresholds fail under North Carolina validation.
Surface water-quality products poorly represent bottom habitat for demersal species.
```

**Framing:** "A rigorous blocked-validation test showed that widely available dynamic environmental
datasets were insufficient to improve held-out prediction of fishery-independent estuarine survey
outcomes, highlighting the need for better bottom-water monitoring, species-specific thresholds,
and validation before habitat stress indicators are used operationally."

This is a credible contribution to Ecological Informatics or Ecological Indicators — it prevents
overconfident indicator deployment.

---

## 11. Required Manuscript Figures

| Figure | Description |
|--------|-------------|
| 1 | Study system and data map: Program 195 strata, tow locations, ModMon stations, FerryMon routes, NOAA/USGS stations, major rivers, watershed zones, land-cover summary units |
| 2 | Data-integration workflow: tow-level biology joined to dynamic WQ surfaces, hydrologic lags, climate events, and land-cover summaries |
| 3 | Environmental dynamics: time series and anomalies for DO, temperature, salinity, turbidity, chlorophyll, rainfall, discharge, drought, storm windows |
| 4 | Model ladder validation: performance comparison A/B/C/D under temporal, spatial, and event holdouts |
| 5 | Species-specific response curves: partial dependence or GAM smooths for DO exposure, temperature stress, salinity shock, turbidity, discharge lags, with uncertainty bands |
| 6 | Dynamic habitat stress maps: suitable/marginal/dangerous for representative normal/wet/drought/heat/hypoxia windows |
| 7 | Calibration and uncertainty: reliability curves, prediction interval coverage, uncertainty masks for mapped habitat stress classes |
| 8 | Ablation results: which data sources and lag windows actually contributed to held-out performance |

---

## 12. Required Manuscript Tables

| Table | Description |
|-------|-------------|
| 1 | Data sources: dataset, provider, years, spatial resolution, temporal resolution, variables, QA/QC notes, access status |
| 2 | Species endpoints: species, life stage, response variables, gear relevance, length cutoffs, biological caveats |
| 3 | Stress thresholds: species, life stage, stressor, threshold range, units, source, uncertainty label, sensitivity range |
| 4 | Model ladder: Model A–D formulas, covariates, assumptions, intended inference |
| 5 | Validation design: temporal folds, spatial folds, event holdouts, metrics, primary test set |
| 6 | Predictive performance: held-out performance by species, response, model, and validation type |
| 7 | Key ecological associations: direction, effect size, uncertainty, and interpretation for major stress metrics |
| 8 | Limitations and claim boundaries: what the model supports, what it does not, what data would be needed for causal inference |

---

## 13. Required Supplement Items

```
Full data dictionary
Tow-level processing rules
Coordinate cleaning and projection
Gear, vessel, tow duration, and effort standardization
Missing-data tables by dataset and year
QA/QC criteria for water-quality sensors
Treatment of 2020–2021 sampling
Treatment of 2025+ Program 195 discontinuity
Environmental interpolation method
Lag-window construction
Threshold source table (from threshold_table.csv)
Threshold uncertainty classes
Sensitivity analyses for every threshold
All fold assignments for temporal, spatial, and event validation
Hyperparameters
Model formulas
Ablation tables
Calibration diagnostics
Residual spatial autocorrelation checks
Species-by-species sample sizes
Rare species exclusion criteria
External validation using Program 915 if used
Oyster side-analysis details if included
Land-cover aggregation rules
Hydrologic catchment definitions
No-data and extrapolation masks
Code environment and package versions
Data access and permission notes
Reproducibility checklist
```

---

## 14. Journal Targeting

| Journal | Best framing | Primary target if |
|---------|-------------|-------------------|
| Ecological Informatics | Data-integration and validated interpretable ecological ML | ML validation is the main contribution |
| Ecological Indicators | Validated habitat stress exposure indicator | Stress-exposure indicator is central product |
| Marine Pollution Bulletin | Measured WQ stress and eutrophication/hypoxia monitoring | Paper becomes WQ/hypoxia/nutrient-stress focused |
| Ocean & Coastal Management | Decision-support for survey interpretation | Agency decision support and coastal management are central |
| Environmental Modelling & Software | Reproducible environmental modelling pipeline | Open package/API/workflow is a formal software contribution |

**Best backup conference targets:**
- American Fisheries Society Annual Meeting 2026 (applied fisheries audience, habitat-as-foundation theme)
- CERF 2027 (best estuarine/coastal fit)
- ICES ASC 2026 (if pitched broadly beyond NC)

---

## 15. Covariate Data Sources

| Source | Variables | Temporal res. | Spatial res. | Observation type | Status |
|--------|-----------|---------------|--------------|-----------------|--------|
| Program 195 (NCDMF/SEAMAP) | tow catch/CPUE/length/weight/metadata | June/Sept annual | tow-level | bottom trawl | NOT INGESTED |
| ModMon (UNC-IMS/NCDENR) | DO, temp, salinity, chl-a, turbidity, pH | ~biweekly | station | **surface AND bottom — confirm depth availability** | NOT INGESTED |
| FerryMon (UNC-IMS) | surface WQ sensors | continuous | ferry track | **SURFACE ONLY** | NOT INGESTED |
| USGS NWIS | streamflow, gauge height, WQ | daily/sub-daily | gauge | in-stream | NOT INGESTED |
| NOAA CO-OPS | water level, salinity, temperature | ~6-min | station | typically surface/near-surface | NOT INGESTED |
| PRISM/NOAA NCEI | precipitation, temperature, degree-days | daily/monthly | gridded | atmospheric | NOT INGESTED |
| U.S. Drought Monitor | drought categories D0–D4 | weekly | mapped | derived index (record starts 2000) | NOT INGESTED |
| MRLC/NLCD | land cover, impervious surface, change | annual (1985–2023) | 30m raster | remote sensing | NOT INGESTED |
| USDA CDL | crop-specific land cover | annual | 30m raster (resolution change 2024+) | remote sensing | NOT INGESTED |

---

## 16. Open Questions Requiring Domain Expert Input (Dr. R)

1. Confirm correct year-specific Program 195 juvenile length cutoffs for croaker — the June <140 vs <160 mm TL discrepancy.
2. Confirm Program 195 metadata fields: length unit (FL vs TL), carapace width for blue crab, sex, maturity/spawner flags, tow duration, swept area, gear changes, vessel changes, station/grid/stratum codes, 2020–2021 sampling flags.
3. Ask whether southern flounder has an accepted NC juvenile length cutoff for Program 195.
4. Ask whether Atlantic menhaden should be excluded or handled with Program 120, Program 915, seine, plankton, or another endpoint.
5. For oysters: confirm whether the project has usable outcome data (spat settlement, mortality, growth, reef condition, restoration-site survival, disease, salinity exposure, harvest-area closure).
6. Confirm ModMon/FerryMon/USGS/NOAA join strategy: surface, bottom, or depth-matched values. Critical for demersal species DO.
7. Confirm turbidity units and harmonization strategy: NTU, TSS mg/L, Secchi depth, light attenuation, or categorical. Do not mix without conversion.
8. Confirm preferred salinity-shock and freshwater-pulse definitions.
9. Confirm whether thresholds define suitable/marginal/dangerous classes or enter as continuous soft-exposure functions.

---

## 17. Milestone Tracking

| Milestone | Target date | Status |
|-----------|-------------|--------|
| Repository initialization | 2026-05-25 | COMPLETE |
| Context files populated (Prompts 1–3) | 2026-05-25 | IN PROGRESS |
| Data access confirmed | TBD | NOT STARTED |
| Endpoint verification complete | TBD | NOT STARTED |
| Data ingest and QA complete | TBD | NOT STARTED |
| Feature engineering documented | TBD | NOT STARTED |
| Validation folds locked | TBD | NOT STARTED |
| Analysis plan pre-registered | TBD | NOT STARTED |
| Model A results | TBD | NOT STARTED |
| Full model ladder results | TBD | NOT STARTED |
| Manuscript draft | TBD | NOT STARTED |
| External/agency review | TBD | NOT STARTED |
| Submission | TBD | NOT STARTED |

---

## 18. Team

| Role | Name / Institution |
|------|--------------------|
| [PLACEHOLDER] | [PLACEHOLDER] |

---

## 19. Revision Log

| Date | Change | Author |
|------|--------|--------|
| 2026-05-25 | Initial placeholder | Claude Code |
| 2026-05-25 | Populated from Prompts 1–3 | Claude Code |
