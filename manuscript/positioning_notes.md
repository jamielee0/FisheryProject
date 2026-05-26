# manuscript/positioning_notes.md
## Manuscript Positioning Notes — Trees to Seas

**Source:** Prompt 3 Outputs 1, 6, 7, 8, 9, 10 (2026-05-25)
**Purpose:** Working notes for manuscript framing, journal targeting, novelty claims,
introduction structure, and discussion claim boundaries. Not a draft manuscript section.

---

## Output 1: Executive Summary and Novelty Verdict

**Novelty verdict:** Publishable and plausibly novel if framed as a retrospective, externally
validated habitat-stress exposure model — not as a causal land-use, pollution, or management-
impact paper. The defensible unit: Program 195 tow-level fishery-independent data through 2024,
joined to ModMon, FerryMon, USGS, NOAA, drought, rainfall, and land-cover covariates, with
land-to-sea variables treated as incremental, noncausal predictors.

**Best first-paper species:** Blue crab, Atlantic croaker, and spot. Southern flounder
conditional (occurrence/CPUE/biomass only unless Program 195 juvenile endpoint confirmed).
Atlantic menhaden excluded. Eastern oyster: separate module only.

**Best first-paper dataset combination:** Program 195 tow-level catch, CPUE, length, tow
metadata, strata, month, grid, depth, and onboard environmental data; ModMon and FerryMon
water quality; USGS streamflow and WQ data; NOAA CO-OPS water level/station data; NOAA
climate/rainfall data; U.S. Drought Monitor; MRLC/NLCD; USDA CDL.

**Strongest journal target:** **Ecological Informatics** — scope explicitly includes ecological
data acquisition/management/analysis, machine learning, Bayesian inference and uncertainty
analysis, species distribution modelling, and forecasting ecosystem functioning.

**Best backup journal:** **Ecological Indicators** — stated aim is integrating monitoring and
assessment of ecological/environmental indicators with management practices, including modelling
and index development.

**Biggest literature risk:** Thresholds and endpoints. Blue crab has a strong Program 195
recruit cutoff; croaker has a verified June cutoff conflict; spot has a unit inconsistency;
southern flounder lacks a confirmed Program 195 juvenile cutoff. Most turbidity, pH,
chlorophyll, sediment, and degree-day thresholds are weak for first-paper hard-threshold use.

**Biggest modeling risk:** Leakage and over-optimistic prediction from random splits,
environmental interpolation, spatial autocorrelation, and sparse bottom-water observations.
Temporal, spatial, and event holdouts are non-negotiable.

**Publishable if results are positive:** Yes, if Model B or C beats static survey-stratum
baseline under temporal and spatial holdouts, remains calibrated, and produces interpretable
species-specific stress-response curves.

**Publishable if results are negative:** Yes, if framed as a rigorous validation study showing
that commonly available dynamic environmental data, borrowed thresholds, or land-cover covariates
are insufficient for reliable habitat-stress indicators without better bottom-water monitoring
or species-specific calibration.

---

## Output 6: Novelty Matrix

**Direct novelty-test answers (from Prompt 3 literature search):**

A. No verified source was found integrating Program 195 tow-level biological data with
   ModMon/FerryMon/USGS/NOAA/drought/rainfall/land-cover covariates into a multispecies
   dynamic habitat-stress model.

B. No verified source was found comparing a static Program 195 survey-stratum baseline
   against dynamic water-quality models for NC estuarine species.

C. No verified source was found building species-specific habitat stress exposure indicators
   for blue crab, Atlantic croaker, spot, and southern flounder using Program 195 endpoints.

D. No verified NC application was found using blocked temporal, spatial, and event holdout
   validation for this exact estuarine habitat-stress prediction problem. Methods are well
   established generally (Roberts et al. 2017; Valavi et al. 2019).

E. No verified source was found converting these Program 195-based models into calibrated
   suitable/marginal/dangerous habitat maps with uncertainty.

F. **The genuine novelty is not any one model class.** It is the defensible combination of:
   Program 195 tow-level endpoints + dynamic WQ/hydrology/weather/watershed lags + species-
   specific soft stress exposure metrics + static-vs-dynamic model comparison + blocked
   temporal/spatial/event validation + calibration + uncertainty-masked habitat maps +
   explicit causal claim boundaries.

G. **What is NOT novel:** hypoxia in the Neuse, WQ monitoring by ModMon/FerryMon, Program 195
   juvenile indices, HSI/species distribution models, CPUE standardization, blocked validation
   as a method, watershed-to-estuary WQ pathways.

**Novelty table:**

| Claim | Already done? | Closest papers | What they did NOT do | Trees to Seas contribution | Risk of incremental |
|-------|---------------|---------------|---------------------|--------------------------|---------------------|
| Program 195 + dynamic WQ integration | Not found | SEAMAP docs; ModMon/FerryMon | Integrate tow-level biology with dynamic WQ surfaces/lags | Tow-level integration with dynamic WQ | Low-medium if integration is rigorous |
| Static baseline vs dynamic habitat model | Not found for NC Program 195 | CPUE/FIS index literature; habitat models | Benchmark against P195 static strata | Locked A/B/C/D ladder testing dynamic value | Low if validation is strict |
| Species-specific stress exposure | Partly done in physiology/field | Selberg; Craig; croaker Gulf model | No unified P195 multispecies stress indicator | Converts thresholds into soft exposure metrics | Medium if thresholds look arbitrary |
| Blocked temporal validation | Established, not NC-specific | Roberts et al. 2017 | Not applied to this NC system | Required headline temporal holdout | Low |
| Blocked spatial validation | Established | Roberts; Valavi blockCV | Not NC Program 195 specific | Leave-stratum/zone/block holdouts | Low |
| Event holdout | Less common in fisheries habitat | Hypoxia/event literature | Rarely used as pre-registered validation | Tests generalization to high-flow/drought/storm/hypoxia windows | Medium-high; needs clean event definitions |
| Land-to-sea incremental predictor model | Watershed-WQ links exist | Stow; Reckhow; Paerl; Corbett | Did not test land cover as incremental predictor of P195 biology | Noncausal watershed covariate layer | Medium; causal overclaim risk |
| Calibrated habitat stress maps | Habitat maps exist elsewhere | Chesapeake HSI; Rubec EFH; dynamic HSI | Often lack P195 endpoints, calibration, uncertainty masks | Suitable/marginal/dangerous maps with uncertainty | Medium; maps must be calibrated |
| Multi-species NC estuarine indicator | Not found | NC FMP indices; WQ monitoring | No validated multispecies habitat-stress exposure score | Species-specific but comparable indicator framework | Medium; must avoid arbitrary index |

---

## Output 7: Manuscript Positioning by Journal

### Ecological Informatics

| Item | Recommendation |
|------|---------------|
| Title | Blocked validation of dynamic habitat-stress exposure models for North Carolina estuarine fisheries |
| Abstract thesis | Long-term fishery-independent surveys can be transformed into externally validated habitat-stress exposure models when tow-level observations are joined to dynamic WQ, hydrologic, meteorological, and watershed covariates with strict temporal/spatial/event holdouts |
| Main contribution | A leakage-resistant ecological informatics workflow for integrating Program 195, ModMon/FerryMon, USGS, NOAA, drought, rainfall, and land-cover products |
| Most important figure | Model ladder validation: static baseline vs dynamic WQ vs stress exposure vs land-to-sea model under temporal, spatial, and event holdouts |
| Must-have analysis | Calibration, blocked validation, ablation by data source, threshold sensitivity, uncertainty masks |
| Likely reviewer objection | "Model class is routine and the study is too local" |
| Claim to avoid | "Machine learning discovered the cause of decline" |
| Likelihood if results strong | Good, especially if code/workflow is transparent and paper emphasizes validation and ecological data integration |

### Ecological Indicators

| Item | Recommendation |
|------|---------------|
| Title | A validated habitat-stress exposure indicator for fishery-independent estuarine surveys in Pamlico Sound |
| Abstract thesis | Species-specific exposure to hypoxia, heat, salinity shock, freshwater pulses, and bloom/turbidity anomalies can be summarized as interpretable indicators and tested against held-out biological endpoints |
| Main contribution | A validated, uncertainty-labeled suitable/marginal/dangerous habitat exposure indicator |
| Most important figure | Habitat stress exposure score calibration against held-out occurrence, CPUE, biomass, and juvenile index outcomes |
| Must-have analysis | Indicator sensitivity to thresholds, reliability curves, class calibration, uncertainty bands, species-by-species performance |
| Likely reviewer objection | "Indicator is arbitrary or threshold borrowing is too weak" |
| Claim to avoid | "This index measures ecosystem health" |
| Likelihood if results strong | Good if the indicator is validated, not merely described |

### Ocean & Coastal Management

| Item | Recommendation |
|------|---------------|
| Title | Dynamic habitat stress maps for interpreting fixed-window estuarine fishery-independent surveys |
| Abstract thesis | Dynamic WQ and hydrologic conditions can affect how fixed survey-window observations are interpreted, and calibrated habitat-stress maps can support monitoring design and event-response interpretation |
| Main contribution | Decision-support for survey interpretation, not a stock-management prescription |
| Most important figure | Paired maps showing Program 195 survey strata overlaid with predicted suitable/marginal/dangerous habitat during normal/wet/drought/heat/hypoxia windows |
| Must-have analysis | Management use cases, uncertainty mask, "what this does/does not support" table, event holdout |
| Likely reviewer objection | "Outputs could be misread as regulatory or management blame" |
| Claim to avoid | "Management failure caused collapse" |
| Likelihood if results strong | Moderate-good if narrative is management-facing and co-reviewed by agency collaborators |

### Marine Pollution Bulletin

| Item | Recommendation |
|------|---------------|
| Focus | Emphasize directly measured water-quality variables: DO, turbidity, chlorophyll, nutrients where available, pH, salinity, temperature |
| Likely objection | "Pollution link is indirect; model-only paper" |
| Required | Strong WQ pathway analysis; measured nutrient/turbidity/hypoxia evidence; cautious land-use language |
| Claim to avoid | "Caused by pollution" |

### Environmental Modelling & Software

| Item | Recommendation |
|------|---------------|
| Requires | Public pipeline, package/API, documentation, reproducibility checklist, model evaluation |
| Likely objection | "No software contribution" |

---

## Output 8: Introduction Outline

### Paragraph 1: Broad estuarine fisheries and habitat-stress problem
**Topic sentence:** Estuarine fisheries are shaped by highly variable habitat conditions that can
alter the availability, quality, and detectability of suitable nursery and foraging habitats.

**Key points:**
- Estuaries are dynamic transition zones where salinity, temperature, oxygen, turbidity, and freshwater flow vary over short time scales
- Fishery-independent surveys are essential, but their observations are conditioned by contemporaneous habitat and catchability
- Stress exposure can influence occurrence, CPUE, growth, and redistribution without implying population-level causality
- Avoid "collapse" framing in the introduction

**Best citations:** Gillson on freshwater flow and estuarine fisheries; Hoyle et al. on CPUE/environmental covariates; Roberts et al. on structured validation
**Claims to avoid:** "Environmental stress caused fishery decline"; "Survey indices are wrong"; "Land use directly caused CPUE change"

---

### Paragraph 2: Dynamic water-quality conditions and fixed survey windows
**Topic sentence:** Fixed-window surveys provide long-term consistency, but their interpretation
can be complicated when dynamic habitat conditions shift during or immediately before sampling.

**Key points:**
- DO, temperature, salinity, turbidity, chlorophyll, and pH can vary at daily to seasonal scales
- Hypoxia, storms, freshwater pulses, drought, and heat events may change where suitable habitat occurs during survey windows
- Static strata may not capture dynamic habitat states
- This motivates a static-baseline vs dynamic-covariate model comparison

**Best citations:** Program 195 June/September design; local hypoxia literature; dynamic habitat analogs
**Claims to avoid:** "Fixed survey design is flawed"; "Dynamic models should replace surveys"

---

### Paragraph 3: NC/Pamlico Sound/Neuse system and data richness
**Topic sentence:** The Albemarle-Pamlico system provides an unusually strong test bed because
long-term fishery-independent survey data overlap with intensive water-quality, hydrologic,
meteorological, and land-cover monitoring.

**Key points:**
- Program 195 provides stratified random Pamlico Sound trawl survey in June and September
- ModMon provides long-term Neuse River Estuary WQ from 1994 onward (surface AND bottom at some stations)
- FerryMon adds repeated surface WQ across ferry routes
- USGS, NOAA, USDM, NLCD, and CDL provide hydrology, climate, drought, water-level, and land-cover covariates

**Best citations:** SEAMAP Program 195; ModMon/Data.gov; FerryMon/Buzzelli 2003; USGS/NOAA/NLCD/CDL
**Claims to avoid:** "All datasets are equally reliable"; "Surface water quality equals bottom habitat"

---

### Paragraph 4: Species and stressors
**Topic sentence:** Blue crab, Atlantic croaker, and spot are well suited for a first Program 195
analysis because survey-relevant endpoints exist, while southern flounder should be included only
if endpoint and sample-size constraints are satisfied.

**Key points:**
- Blue crab: strong <127 mm CW recruit cutoff
- Croaker: strong September cutoff but June cutoff conflict — do not finalize until resolved
- Spot: strong JAI support but June unit must be verified
- DO, temperature, salinity, salinity shock, and seasonal exposure are stronger first-paper stressors
- Turbidity, pH, chlorophyll, and sediment thresholds are mostly weak or generic for these species

**Best citations:** NCDMF blue crab/croaker/spot reviews; threshold audit; Selberg 2001; Craig 2023
**Claims to avoid:** "All species share one stress threshold"; "Generic hypoxia thresholds are species-specific"

---

### Paragraph 5: Modeling gap
**Topic sentence:** Despite extensive survey and WQ monitoring, the literature does not appear
to have produced a Program 195-centered, multispecies, externally validated dynamic habitat-stress
exposure model.

**Key points:**
- Program 195 indices are reported in FMP/ASMFC contexts
- ModMon/FerryMon studies describe WQ dynamics
- Dynamic HSI and SDM literature exists elsewhere
- The gap is the integrated, validated, species-specific exposure framework with calibration and uncertainty

**Claims to avoid:** "No one has modeled estuarine habitat"; "This is the first dynamic habitat model ever"

---

### Paragraph 6: Study objectives and hypotheses
**Topic sentence:** This study tests whether dynamic environmental and watershed-to-estuary
covariates improve held-out prediction of estuarine species occurrence, CPUE, biomass, and
juvenile indices relative to static survey baselines and whether those covariates can be
transformed into interpretable habitat-stress exposure indicators.

**Five objectives (map to H1–H5):**
1. Build Model A static baseline
2. Add dynamic WQ and lagged hydrologic/weather covariates (H1, H3)
3. Convert WQ variables to species-specific soft exposure metrics (H2)
4. Test land-to-sea variables as incremental, noncausal predictors (H4)
5. Validate with temporal, spatial, and event holdouts (H5)

**Claims to avoid:** "We estimate causal effects of land use"; "We identify management failures";
"We prove pollution caused abundance changes"

---

## Output 9: Discussion Claim Boundary Section

See CLAIM_BOUNDARIES.md §8 for the full discussion claim-boundary section.

**Quick reference:**

| Category | Examples |
|----------|---------|
| Supported (if validated) | Dynamic covariates improved held-out prediction; stress metrics predictive; habitat states shifted within uncertainty; dynamic conditions help interpret surveys; land cover added incremental value |
| Suggestive only | Consistent with stress-related redistribution; watershed conditions may help predict WQ stress; catchability may be affected by environment |
| Forbidden | Land/forestry/ag/management/pollution caused anything; predictive model proves mechanism; maps without calibration/uncertainty are decision-ready; Great Lakes analogy proves NC causality |

**Required direct statement in manuscript:**
> This study estimates predictive associations between dynamic environmental conditions and
> fishery-independent survey outcomes. It does not estimate causal effects of land use,
> management policy, or individual pollution sources.

---

## Output 10: Final Recommendations

1. **Should this project proceed as a journal paper?**
   Yes. Publishable if narrowed to a defensible, validated first paper: Program 195 + dynamic
   WQ/hydrology/weather + species-specific exposure metrics + blocked validation.

2. **Best journal target:** Ecological Informatics (data-integration and validation framework)

3. **Best backup journal:** Ecological Indicators (stress exposure score as central validated product)

4. **Best conference targets:**
   - American Fisheries Society Annual Meeting 2026 (applied fisheries; habitat-as-foundation theme)
   - CERF 2027 (best estuarine/coastal fit)
   - ICES ASC 2026 (if pitched broadly beyond NC)

5. **Final species list:**
   Primary: blue crab, Atlantic croaker, spot
   Conditional: southern flounder as occurrence/CPUE/biomass only unless P195 juvenile endpoint confirmed
   Excluded (first paper): Atlantic menhaden
   Separate module: eastern oyster (only if outcome data confirmed)

6. **Final dataset list:**
   Program 195 tow-level; ModMon; FerryMon; USGS streamflow/WQ; NOAA CO-OPS; NOAA climate/rainfall;
   U.S. Drought Monitor; MRLC/NLCD; USDA CDL. Optional: Program 915, Program 120, nutrient/sediment,
   storm tracks, forestry/CAFO/land-use proxies only if defensible.

7. **Three analyses required for publication:**
   - Locked temporal/spatial/event blocked validation with no leakage
   - Endpoint and threshold sensitivity (especially croaker June cutoff and spot June unit)
   - Calibration, uncertainty mapping, and ablation by data source

8. **Three analyses to save for Paper 2:**
   - Causal land-use or pollutant attribution design
   - Oyster mortality/growth/spat/reef module
   - Menhaden-specific endpoint using appropriate survey or life-stage dataset

9. **Exact novelty paragraph (for Introduction):**
   See CLAIM_BOUNDARIES.md §9.

---

## Conference Positioning

| Conference | Best submission type | Abstract angle | Best fit |
|------------|---------------------|---------------|----------|
| AFS Annual Meeting 2026 | Oral or contributed symposium | Fishery-independent survey interpretation under dynamic habitat stress | High — habitat as foundation of productive fisheries theme |
| CERF 2027 | Oral/poster | Watershed-to-estuary dynamic WQ exposure and estuarine fish/crab indicators | Highest estuarine/coastal fit |
| ICES ASC 2026 | Oral/poster | Spatiotemporal validation and habitat-stress prediction for survey data | Good if pitched broadly beyond NC |
| ESA Annual Meeting 2026 | Contributed talk/poster | Ecological prediction, dynamic habitat exposure, blocked validation | Good; some methodological novelty helpful |
| iEMSs 2026 | Oral/session paper | Reproducible environmental modelling pipeline | Needs workflow/software emphasis |
| ISEM Global Conference | Oral/poster | From data to decision: ecosystem modelling for estuarine habitat stress | Good modelling story |
| Climate Change AI / NeurIPS workshop | Workshop paper/poster | Interpretable, calibrated ML for coastal habitat stress under climate extremes | Needs stronger ML novelty or benchmark contribution |

---

*Last updated: 2026-05-25 — Prompt 3 Outputs 1, 6, 7, 8, 9, 10*
