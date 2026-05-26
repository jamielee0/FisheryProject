# SOURCE_QUALITY_AUDIT.md
## Data Source Quality Audit — Trees to Seas

**Source:** Populated from Prompts 3 Outputs 3 and 5 (2026-05-25).
**Purpose:** Every data source used in this project must be documented here before being ingested.
Claude Code must add a new source to this file before writing ingest code.

**Critical flag for all sources:** Confirm whether each observation is surface or bottom.
This is the single most important QA step for demersal species (blue crab, croaker, spot, flounder).
See CLAUDE.md §6 Publication Risk #5: surface water quality must never be treated as bottom habitat.

---

## Part 1: NC-Specific Primary Sources

| Source | System | Dataset | Species | Variables | Years | Why it matters | Strength | Weakness | Ingest status | Use in paper |
|--------|--------|---------|---------|-----------|-------|---------------|----------|----------|--------------|-------------|
| SEAMAP-SA Program 195 | Pamlico Sound, Neuse, Pamlico, Pungo | Program 195 | multispecies | tow, strata, grids, June/Sept sampling | Survey active since 1987; 1995–2024 preferred | Defines biological backbone and fixed survey design | Official survey design documentation | Not a habitat model | NOT INGESTED | Study system/methods |
| NCDMF 2024 Atlantic croaker review | Pamlico Sound | Program 195 | croaker | JAI, length cutoffs, COVID caveats | 1987–2024 index | Latest official endpoint source | Current official source | Conflicts with 2023 cutoff | N/A — document only | Endpoints |
| NCDMF 2023 Atlantic croaker review | Pamlico Sound | Program 195 | croaker | JAI, length cutoffs | 1987–2023 | Documents June <160 mm conflict | Official source | Not current if 2024 supersedes | N/A — document only | Sensitivity/endpoints |
| NCDMF 2024 spot review | Pamlico Sound | Program 195 | spot | JAI, length cutoff text/captions | 1987–2024 | Latest official spot endpoint source | Current official source | Unit inconsistency TL/FL | N/A — document only | Endpoints/sensitivity |
| NCDMF 2022 spot update | Pamlico Sound | Program 195/P930 | spot | JAI cutoff update | 1987–2022 | Explains 2022 update using age-0/age-1 distributions | Strong agency basis | TL/FL implementation still needs confirmation | N/A — document only | Endpoints |
| NCDMF 2025 Blue Crab Amendment 3 | NC estuaries | Program 195/120/100 | blue crab | recruit/adult cutoffs | 1995–2024 | Latest blue crab endpoint evidence | Strong official endpoint | FMP context not habitat stress | N/A — document only | Endpoints |
| NCDMF southern flounder reviews 2021–2022 | NC estuaries | Program 120/195/915 | southern flounder | indices, assessment context | varies | Shows flounder relevance but endpoint uncertainty | Official context | No confirmed P195 juvenile cutoff | N/A — document only | Optional species |
| ModMon / Data.gov Neuse WQ dataset | Neuse River Estuary | ModMon | none | biological, chemical, physical WQ | 1994–present | Long-term WQ backbone | Official data documentation | **Surface AND bottom — confirm depth availability** | NOT INGESTED | Methods |
| FerryMon (UNC-IMS) | APES ferry routes | FerryMon | none | surface WQ sensors | long-running | High-frequency dynamic WQ observations | Strong spatial/temporal monitoring | **SURFACE ONLY — cannot proxy bottom habitat** | NOT INGESTED | Methods |
| Borsuk et al. 2001 | Neuse River Estuary | ModMon/WQ | none | DO, hypoxia drivers | historical | Prior predictive hypoxia model in NRE | Local peer-reviewed | No fish endpoint | N/A — literature | Methods |
| Reckhow et al. 2005 | Neuse River Estuary | WQ/nutrient | none | eutrophication, hypoxia, fish kills | historical | Establishes nutrient-criteria context | Strong local WQ evidence | Not species-specific | N/A — literature | Introduction |
| Stow et al. 2001 | Neuse River Basin | nutrient inputs/exports | none | N/P inputs, river loads | historical | Watershed-to-estuary context | Peer-reviewed | Causal links to fish not tested | N/A — literature | Discussion |
| Selberg et al. 2001 | Neuse River Estuary | field DO/crab | blue crab | DO, crab presence | field study | Local blue crab hypoxia evidence | Species-specific/local | Field association only | N/A — literature | Thresholds |
| Craig et al. 2023 | Neuse River Estuary | telemetry/WQ | spot | movement, DO ≤2 mg/L | contemporary | Local juvenile spot hypoxia response | Species/life-stage/local | Not Program 195 | N/A — literature | Thresholds |
| Campbell & Rice 2014 | Neuse River Estuary | WQ/growth | juvenile fish | hypoxia, growth | field/lab synthesis | Local hypoxia-habitat compression evidence | Strong local ecological support | Not direct tow CPUE model | N/A — literature | Thresholds/discussion |
| Guindon & Miller 1995 | Pamlico Sound | juvenile habitat/growth | southern flounder | salinity/growth | historical | Local flounder nursery salinity evidence | Species/local | Older; not Program 195 cutoff | N/A — literature | Thresholds/supplement |
| Corbett et al. 2010 | Neuse River Estuary | sediment/nutrients | none | resuspension, nutrient cycling | field/process | Sediment/nutrient pathway support | Local peer-reviewed | Not fish threshold | N/A — literature | Discussion |
| USGS OFR 92-110 | Pamlico/Neuse | continuous WQ | none | temp, conductance, DO | historical | Documents continuous bottom/surface WQ precedent | Local technical source | Older; limited locations | N/A — document | Study system |

---

## Part 2: Covariate Data Source Audit

### Program 195 — NCDMF/SEAMAP Tow-Level Survey

| Field | Status / Value |
|-------|---------------|
| Data provider | NC Division of Marine Fisheries (NCDMF) / SEAMAP South Atlantic |
| Program | SEAMAP Program 195 Pamlico Sound Trawl Survey |
| Temporal coverage | 1987–2024 survey; preferred analysis window 1995–2024 |
| 2020–2021 | COVID disruption — treat as sensitivity years; document in supplement |
| 2025+ | SUSPENDED — do not assume continuity |
| Spatial coverage | Pamlico Sound and adjacent lower Neuse, Pamlico, Pungo strata; seven strata; 54 grids/month |
| Station network changes | **UNVERIFIED — confirm gear changes, vessel changes, stratum redesigns by year** |
| Key fields | **UNVERIFIED — confirm: tow ID, station/grid/stratum, date, gear type, vessel, tow duration, swept area, depth, latitude/longitude, species-level catch and weight, length measurements (FL vs TL vs CW by species), sex, maturity flags** |
| QA/QC flags | UNVERIFIED |
| Observation type | Bottom trawl — **bottom habitat relevant; confirm gear selectivity by species and life stage** |
| Publication risk flags | station_memorization, spatial_autocorrelation, gear_selectivity_changes |
| Peer-reviewed citation | SEAMAP-SA Program 195 documentation |
| Ingest status | NOT STARTED |
| Notes | Primary outcome data. Must confirm all fields before endpoint construction. Do not assume length unit consistency across years without checking raw data. |

---

### ModMon — NC Estuarine Water Quality

| Field | Status / Value |
|-------|---------------|
| Data provider | UNC Institute of Marine Sciences / NCDENR |
| Temporal coverage | 1994–present (NCEI Accession 0294041 through 2022-01-22; check for updates) |
| Temporal gaps | UNVERIFIED |
| Spatial coverage | Fixed stations along Neuse River Estuary and Pamlico Sound |
| Station network changes | UNVERIFIED — confirm station additions/removals |
| Key fields | DO, temperature, salinity, chlorophyll-a, turbidity, pH, Secchi depth (confirm which parameters are at which depths) |
| QA/QC flags | UNVERIFIED |
| **Observation type** | **CRITICAL: ModMon collects BOTH surface and bottom profiles at some stations. Confirm which stations have bottom DO data and in which years. Demersal species require bottom-water values, not surface.** |
| Publication risk flags | surface_vs_bottom_habitat, sparse_bottom_water_observations, environmental_interpolation_leakage |
| Peer-reviewed citation | Borsuk et al. 2001; Paerl et al. 1998; Reckhow et al. 2005 |
| Ingest status | NOT STARTED |
| Notes | Core WQ backbone. Spatial join to Program 195 tow locations will require interpolation — document method and report interpolation uncertainty. |

---

### FerryMon — Ferry-Based Surface Water Quality

| Field | Status / Value |
|-------|---------------|
| Data provider | UNC Institute of Marine Sciences |
| Temporal coverage | Long-running (confirm exact start year) |
| Temporal gaps | UNVERIFIED |
| Spatial coverage | Ferry track across Neuse River and Pamlico Sound ferry routes (not fixed stations) |
| Key fields | Surface water quality — confirm specific parameters and sensor calibration history |
| QA/QC flags | UNVERIFIED |
| **Observation type** | **SURFACE ONLY — must never be treated as bottom habitat for demersal species.** Flag every FerryMon-derived feature as surface-only in all feature-engineering functions. |
| Publication risk flags | surface_vs_bottom_habitat, environmental_interpolation_leakage, spatial_autocorrelation |
| Peer-reviewed citation | Buzzelli et al. 2003 (Environmental Monitoring and Assessment) |
| Ingest status | NOT STARTED |
| Notes | Valuable for dynamic surface WQ coverage. All features derived from FerryMon must be labeled `obs_type=surface` in the feature store. |

---

### USGS NWIS — Streamflow and Gauge Height

| Field | Status / Value |
|-------|---------------|
| Data provider | USGS National Water Information System |
| API | https://api.waterdata.usgs.gov/ |
| Temporal coverage | Gauge-dependent (confirm for each relevant station) |
| Temporal gaps | UNVERIFIED |
| Spatial coverage | UNVERIFIED — must identify relevant gauges for NC estuarine watershed |
| Key fields | Daily streamflow, gauge height; sub-daily where available; water quality at some sites |
| QA/QC flags | USGS standard QA codes (Approved/Estimated/Working) — use only Approved |
| Observation type | In-stream freshwater; not estuarine |
| Publication risk flags | environmental_interpolation_leakage (lag and routing time to estuary must be documented) |
| Peer-reviewed citation | USGS standard citation |
| Ingest status | NOT STARTED |
| Notes | Define relevant watershed gauges. Document lag-window derivation. Routing time from gauge to estuary must be estimated or sensitivity-tested. |

---

### NOAA CO-OPS — Tide / Salinity / Temperature Stations

| Field | Status / Value |
|-------|---------------|
| Data provider | NOAA Center for Operational Oceanographic Products and Services |
| API | https://api.tidesandcurrents.noaa.gov/api/prod/ |
| Temporal coverage | Station-dependent |
| Temporal gaps | UNVERIFIED |
| Spatial coverage | Fixed NOAA tide/water-quality stations — identify NC Pamlico Sound relevant stations |
| Key fields | Water level, salinity, temperature; meteorological at some stations; 6-minute resolution |
| QA/QC flags | NOAA standard QA flags |
| Observation type | Typically surface or near-surface — confirm for each station used |
| Publication risk flags | surface_vs_bottom_habitat, environmental_interpolation_leakage |
| Peer-reviewed citation | NOAA CO-OPS standard citation |
| Ingest status | NOT STARTED |
| Notes | Useful for water-level and station-observation components. Confirm observation depth before use. |

---

### NOAA NCEI — Precipitation, Temperature, and Climate Products

| Field | Status / Value |
|-------|---------------|
| Data provider | NOAA National Centers for Environmental Information |
| Portal | Climate Data Online (CDO) |
| Temporal coverage | Historical; confirm for needed variables |
| Spatial coverage | Gridded and station; PRISM/gridMET may also be useful |
| Key fields | Daily/monthly precipitation, temperature, wind, degree-days |
| QA/QC flags | UNVERIFIED |
| Observation type | Atmospheric — not aquatic |
| Publication risk flags | environmental_interpolation_leakage, spatial_autocorrelation |
| Ingest status | NOT STARTED |
| Notes | Watershed aggregation method must be documented. Degree-day accumulation must specify base temperature and accumulation window. |

---

### U.S. Drought Monitor

| Field | Status / Value |
|-------|---------------|
| Data provider | National Drought Mitigation Center / NOAA / USDA |
| Temporal coverage | Weekly from 2000-01-04 onward |
| Spatial coverage | Mapped; county and polygon available |
| Key fields | Categorical drought classes D0–D4 (using convergence of evidence) |
| QA/QC flags | N/A — derived index |
| Observation type | Derived atmospheric/hydrologic index |
| Publication risk flags | environmental_interpolation_leakage (categorical to continuous conversion); record starts 2000 (limits pre-2000 use) |
| Ingest status | NOT STARTED |
| Notes | Use as event indicator (D2+ weeks) or continuous drought category. Record starts 2000 — earlier drought covariates require alternative (e.g., PDSI, SPI from PRISM/NOAA). |

---

### MRLC/NLCD — Land Cover

| Field | Status / Value |
|-------|---------------|
| Data provider | USGS MRLC Consortium |
| Product | Annual NLCD Collection 1.0 (1985–2023 annual products) |
| Temporal coverage | Annual from 1985 to 2023 |
| Temporal gaps | Earlier epoch-based products had multi-year gaps; annual product resolves this from 1985 |
| Spatial coverage | 30m raster; conterminous US |
| Key fields | Land cover class, impervious surface fraction, change metrics |
| QA/QC flags | UNVERIFIED |
| Observation type | Remote sensing — lagged effect on water quality must be modeled |
| Publication risk flags | environmental_interpolation_leakage, spatial_autocorrelation, weak thresholds (land-to-WQ pathway must not be assumed) |
| Ingest status | NOT STARTED |
| Notes | Model D only. Must show held-out improvement after water quality and hydrology are already included. Watershed aggregation method must be documented. |

---

### USDA CDL — Cropland Data Layer

| Field | Status / Value |
|-------|---------------|
| Data provider | USDA National Agricultural Statistics Service |
| Portal | CropScape |
| Temporal coverage | Annual (with resolution change beginning in 2024 — handle carefully for historical consistency) |
| Spatial coverage | 30m raster US |
| Key fields | Crop-specific land cover by year |
| QA/QC flags | UNVERIFIED |
| Observation type | Remote sensing / annual classification |
| Publication risk flags | environmental_interpolation_leakage, spatial_autocorrelation |
| Ingest status | NOT STARTED |
| Notes | 2024 resolution change must be harmonized or flagged. Use for crop composition by watershed zone. Model D only — as incremental predictor after water quality is included. |

---

## Part 3: Threshold Source Quality Audit (from Prompt 3 Output 5)

| Source/claim category | Decision | Reason | Replacement or handling |
|-----------------------|----------|--------|------------------------|
| NCDMF annual reviews and FMP amendments | Keep as primary evidence | Official survey and endpoint sources | Use for Program 195 endpoints, COVID/sampling caveats, and JAI definitions |
| SEAMAP Program 195 survey documentation | Keep as primary evidence | Official survey design documentation | Use for sampling frame, strata, months, grid targets |
| ModMon/FerryMon official documentation and Buzzelli 2003 | Keep as primary evidence | Direct WQ data provenance | Use in methods and study-system sections |
| NC water-quality standards | Keep but downgrade for biology | Regulatory screen not species threshold | Use as WQ screen only |
| NOAA/EPA generic hypoxia definitions | Keep but downgrade | Generic hypoxia screen | Use as common exposure metric not species-specific biology |
| ResearchGate-only sources | Replace or supplement only | Access route is not primary; may be incomplete/preprint | Find journal/agency copy before using as threshold evidence |
| SciSpace-only sources | Replace or supplement only | Secondary aggregator | Use only to locate primary article |
| P2InfoHouse reports | Keep as supplement only | Useful historical/local reports but not peer-reviewed threshold evidence | Do not use as hard species thresholds |
| Broad HSI models from other regions | Keep as sensitivity/supporting evidence | Often model-derived and nonlocal | Use soft functions or sensitivity ranges |
| Aquaculture sources applied to wild systems | Keep as supplement only | Controlled/culture conditions differ from estuarine field habitat | Use only for stage-specific sensitivity |
| Generic pH/chlorophyll/turbidity thresholds | Downgrade | Weak species-specific evidence | Use continuous, anomaly, or percentile covariates |
| Great Lakes analogies | Keep only as historical motivation | Not direct NC evidence | Use in introduction/discussion caution not causality |
| Neuse River estuary field reports (P2InfoHouse) | Keep as supplement only | Local but not peer-reviewed or controlled threshold | Cite as historical field observation; not hard threshold |
| Selberg et al. 2001; Craig et al. 2023; Campbell & Rice 2014 | Keep as primary threshold evidence | Peer-reviewed, local, species-specific | Use as primary evidence for blue crab and spot DO thresholds in NRE |

---

## Part 4: Known Surface-vs-Bottom Observation Flags

| Source | Observation depth | Flag required |
|--------|-------------------|--------------|
| FerryMon | Surface only | YES — all features must be labeled `obs_type=surface` |
| ModMon | Surface AND bottom (station-dependent) | YES — confirm depth per station per year; never assume surface = bottom |
| NOAA CO-OPS | Typically surface/near-surface | YES — confirm per station |
| USGS streamflow | In-stream freshwater | YES — not estuarine bottom habitat |
| Program 195 tow data | Bottom trawl | Appropriate for demersal species; note gear selectivity limits |

---

## Revision Log

| Date | Change | Author |
|------|--------|--------|
| 2026-05-25 | Initial placeholder | Claude Code |
| 2026-05-25 | Populated from Prompts 3 Outputs 3 and 5 | Claude Code |
