# RELATED_WORK_MATRIX.md
## Related Work Evidence Matrix — Trees to Seas

**Source:** Populated from Prompt 3 Output 2 (2026-05-25).
**Purpose:** Track prior literature relevant to methods, claims, and validation approaches.
Codex should consult this before suggesting a new model or validation method to avoid
reinventing approaches or missing relevant prior art.

**Evidence quality key:**
- `high` — peer-reviewed primary source, local or directly applicable
- `medium` — peer-reviewed but regional/indirect, or agency report with methodological limits
- `weak` — secondary access only (ResearchGate, SciSpace aggregator) — replace with journal copy before citing

---

## Primary Survey and Endpoint Sources

| Author/Year | Title | Source type | Journal/Report | System | Species | Data used | Method | Main finding | Relevance | Gap left open | Evidence quality | Use in manuscript |
|-------------|-------|-------------|----------------|--------|---------|-----------|--------|-------------|-----------|---------------|-----------------|-------------------|
| SEAMAP-SA, n.d. | North Carolina Pamlico Sound Trawl Survey | data documentation | SEAMAP South Atlantic | Pamlico Sound, Neuse, Pamlico, Pungo | multispecies | Program 195 trawl survey | stratified random survey | June/September sampling; 54 grids/month; 108/year; seven strata | Core biological backbone | Not a dynamic habitat model | high | study system |
| NCDMF 2024 | Atlantic Croaker FMP Review | agency report | NC DEQ/NCDMF | Pamlico Sound | Atlantic croaker | Program 195 | JAI reporting | Juvenile croaker <140 mm TL in June, <210 mm TL in Sept.; COVID sampling caveats | Endpoint verification | Conflicts with 2022–2023 June cutoff | high | species endpoints |
| NCDMF 2023 | Atlantic Croaker FMP Review | agency report | NC DEQ/NCDMF | Pamlico Sound | Atlantic croaker | Program 195 | JAI reporting | Juvenile croaker <160 mm TL in June, <210 mm TL in Sept. | Confirms cutoff conflict | Does not explain change | high | species endpoints |
| NCDMF 2024 | Spot FMP Review | agency report | NC DEQ/NCDMF | Pamlico Sound | spot | Program 195 | JAI reporting | Text gives juvenile spot <140 mm TL June, <190 mm TL Sept.; figure text also references FL | Endpoint evidence; unit conflict | TL vs FL must be resolved | high | species endpoints |
| NCDMF 2023 | Spot FMP Review | agency report | NC DEQ/NCDMF | Pamlico Sound | spot | Program 195 | JAI reporting | Length cutoffs shown as <140 mm FL June, <190 mm TL Sept. | Supports Prompt 2's FL claim | Conflicts with 2022/2024 text definitions | high | species endpoints |
| NCDMF 2022 | Spot FMP Update | agency report | NC DEQ/NCDMF | Pamlico Sound | spot | Program 195, P930 | JAI update | Juvenile spot cutoffs updated in 2022 after age-0/age-1 analysis; <140 mm TL June, <190 mm TL Sept. | Explains time-varying endpoint issue | TL/FL implementation still needs confirmation | high | species endpoints |
| NCDMF 2025 | Blue Crab FMP Amendment 3 | agency report | NC DEQ/NCDMF | NC estuaries | blue crab | Program 195/120/100 | FMP amendment | Recruit crabs <127 mm CW; fully recruited ≥127 mm CW; Program 195 through 2024 | Strong endpoint source | Management document not stress-threshold study | high | species endpoints |
| NCDMF 2023 | Blue Crab FMP Review | agency report | NC DEQ/NCDMF | NC estuaries | blue crab | Program 120, 195, 100 | FMP review | Program 195 recruit/adult indices use <127 and ≥127 mm CW | Confirms historical endpoint | No dynamic habitat covariates | high | species endpoints |
| NCDMF 2022 | Southern Flounder FMP Review | agency report | NC DEQ/NCDMF | NC estuaries | southern flounder | Program 120 and others | FMP review | Program 120 used for juvenile index in assessment context | Supports flounder endpoint caution | Does not provide Program 195 length cutoff | medium | species endpoints |
| NCDMF 2021 | Southern Flounder Update | agency report | NC DEQ/NCDMF | Pamlico Sound | southern flounder | Program 195 | FMP update | P195 was not used as JAI in 2019 assessment but is additional data | Supports optional flounder treatment | No confirmed cutoff | medium | species endpoints |
| Schlick et al. 2024 | Southern Flounder Stock Assessment, South Atlantic, 1989–2022 | weak/secondary source | ResearchGate-accessed stock assessment listing | South Atlantic | southern flounder | assessment datasets | stock assessment | Official assessment appears to exist but official link not verified | Possible Paper 2/reference | Do not use as primary until official copy obtained | weak | supplement only |

---

## Water-Quality Monitoring and Estuarine Dynamics

| Author/Year | Title | Source type | Journal/Report | System | Species | Data used | Method | Main finding | Relevance | Gap left open | Evidence quality | Use in manuscript |
|-------------|-------|-------------|----------------|--------|---------|-----------|--------|-------------|-----------|---------------|-----------------|-------------------|
| Buzzelli et al. 2003 | Ferry-based monitoring of surface water quality in North Carolina estuaries | peer-reviewed | Environmental Monitoring and Assessment | APES | none | FerryMon sensor data | monitoring design | FerryMon provides cost-effective spatial/temporal WQ monitoring | Supports dynamic WQ backbone | Surface observations not bottom habitat | high | study system |
| Paerl Lab / Data.gov, current | Neuse River Estuary water quality data (ModMon) | data documentation | Data.gov / ModMon | Neuse River Estuary | none | WQ from 1994–present | monitoring dataset | Long-term biological, chemical, physical WQ observations | Core WQ source | Needs QA/QC and interpolation | high | methods |
| Borsuk et al. 2001 | Probabilistic prediction of hypoxia in the Neuse River Estuary | peer-reviewed | ModMon publication listing | Neuse River Estuary | none | WQ/hypoxia | empirical oxygen model | Predictive hypoxia modelling in NRE | Close WQ-model precedent | Not Program 195 biological integration | high | methods |
| Stow et al. 2001 | Long-term changes in watershed nutrient inputs and riverine exports in the Neuse River | peer-reviewed | Water Research | Neuse River Basin | none | nutrient inputs/loads | trend analysis | Basin nutrient sources increased; river export patterns complex | Land-to-sea pathway context | Not fish-specific; causal attribution limited | high | introduction |
| Reckhow et al. 2005 | A predictive approach to nutrient criteria | peer-reviewed | Environmental Science & Technology | Neuse River Estuary | none | eutrophication/WQ | predictive criteria | NRE had algal blooms, hypoxia, fish kills motivating nutrient criteria | Strong WQ-context citation | Not species endpoint modelling | high | study system |
| Paerl et al. 1998 | Consequences for hypoxia in the eutrophying Neuse River Estuary | peer-reviewed | Marine Ecology Progress Series | Neuse River Estuary | none | nutrient/eutrophication observations | process study | Nutrient-enhanced production and stratification linked to hypoxia | Stress pathway context | Not Program 195 | high | introduction |
| Corbett et al. 2010 | Resuspension and estuarine nutrient cycling in the Neuse River Estuary | peer-reviewed | Biogeosciences | Neuse River Estuary | none | sediment/nutrients | process study | Resuspension can affect nutrient cycling in a eutrophic estuary | Turbidity/sediment pathway context | Not a species threshold | medium | discussion |
| Brentjens et al. 2023 | Beneath the surface: trends in water quality and algal community composition in Albemarle Sound | peer-reviewed | open-access | Albemarle Sound | none | WQ/algal data | trend analysis | WQ/algal dynamics in AP system | Regional WQ context | Not Pamlico/Program 195-specific | medium | study system |
| USGS OFR 92-110 | Continuous water-quality data near Pamlico and Neuse estuaries | technical report | USGS | Pamlico/Neuse | none | 15-min WQ | station monitoring | Continuous near-surface and bottom conductance/temp/DO data | Historical WQ precedent | Older; limited spatial coverage | medium | study system |
| USGS 2013–2014 | Albemarle-Pamlico WQ and bed-sediment quality | technical report | USGS | APES | none | WQ/sediment | monitoring report | Chlorophyll state threshold exceeded in some AP samples | WQ context | Limited period | medium | discussion |
| Sokoletsky et al. 2011 | Bio-optical retrieval of chlorophyll-a using MERIS and FerryMon | peer-reviewed | Remote Sensing | Neuse/Pamlico | none | FerryMon + satellite | remote sensing | FerryMon can support chlorophyll mapping | Supports WQ-surface mapping | Surface chl not fish threshold | medium | methods |

---

## Species-Specific Stress Responses (NC and Regional)

| Author/Year | Title | Source type | Journal/Report | System | Species | Data used | Method | Main finding | Relevance | Gap left open | Evidence quality | Use in manuscript |
|-------------|-------|-------------|----------------|--------|---------|-----------|--------|-------------|-----------|---------------|-----------------|-------------------|
| Selberg et al. 2001 | Hypoxia in the Neuse River Estuary: responses of blue crabs and crabbers | peer-reviewed | North American Journal of Fisheries Management | Neuse River Estuary | blue crab | field DO/crab observations | field association | Blue crabs associated with oxygenated habitat; generally absent at low DO | Best local blue crab DO evidence | Field association not lethal threshold | high | stress thresholds |
| Craig et al. 2023 | Dynamic movement responses of juvenile spot to hypoxia | peer-reviewed | Journal article / NOAA repository | Neuse River Estuary | spot | acoustic telemetry, DO | movement analysis | Juvenile spot movement response to DO ≤2 mg/L hypoxia | Strong local spot DO evidence | Not Program 195 catch model | high | stress thresholds |
| Campbell & Rice 2014 | Effects of hypoxia-induced habitat compression on growth of juvenile fish in NRE | peer-reviewed | Marine Ecology Progress Series | Neuse River Estuary | juvenile fishes incl. spot | field/growth/WQ | field growth model | Hypoxia and habitat compression influence juvenile fish growth | Local hypoxia-response support | Not tow-level Program 195 | high | stress thresholds |
| Stierhoff et al., unverified | Hypoxia-induced growth-rate reduction in juvenile estuary-dependent fishes | weak/secondary source | ResearchGate/SciSpace-style access | estuarine lab | spot, menhaden | lab DO/growth | experiment | Growth reductions at very low DO reported | Useful only if journal copy obtained | Do not use RG-only as primary | weak | supplement only |
| Rose et al. 2018 | Modelling population effects of hypoxia on Atlantic croaker | peer-reviewed | Gulf of Mexico model paper | Gulf of Mexico | Atlantic croaker | model/DO | population model | Hypoxia can affect croaker population dynamics | Regional croaker hypoxia analog | Not NC not Program 195 | medium | discussion |
| Guindon & Miller 1995 | Growth potential of juvenile southern flounder in low-salinity nursery areas | peer-reviewed | Estuaries / ScienceDirect | Pamlico Sound | southern flounder | juvenile growth/salinity | field/lab growth | Low-salinity nursery conditions relevant to flounder growth | Strong local flounder support | Not Program 195 endpoint | medium | stress thresholds |
| Gillson 2011 | Freshwater flow and fisheries production | peer-reviewed | Reviews in Fish Biology and Fisheries | estuaries | fish | review | conceptual review | Flow affects salinity, turbidity, sediment, thermal conditions, habitat | Supports freshwater-pulse lags | Not NC-specific | medium | introduction |

---

## Hypoxia and WQ Definitions

| Author/Year | Title | Source type | Journal/Report | System | Species | Data used | Method | Main finding | Relevance | Evidence quality | Use in manuscript |
|-------------|-------|-------------|----------------|--------|---------|-----------|--------|-------------|-----------|-----------------|-------------------|
| NOAA NCCOS, n.d. | Hypoxia definition | agency report | NOAA NCCOS | generic coastal | multispecies | WQ definition | agency screen | Hypoxia often defined as DO below ~2 mg/L | Generic screen | medium | stress thresholds |
| EPA, n.d. | Hypoxia 101 | agency report | U.S. EPA | generic coastal | multispecies | WQ synthesis | agency explainer | Hypoxia commonly <2–3 mg/L; nutrient enrichment and stratification are drivers | Generic pathway support | medium | introduction |
| NC OAH/NCDEQ | NC tidal saltwater standards | agency report | NC water-quality standards | NC tidal waters | multispecies | regulatory criteria | regulatory standard | DO ≥5 mg/L; pH 6.8–8.5 screens | Regulatory WQ screen | high for regulation; low for biology | stress thresholds |

---

## Dynamic Habitat and SDM Modeling Methods

| Author/Year | Title | Source type | Journal/Report | System | Species | Method | Main finding | Relevance | Evidence quality | Use in manuscript |
|-------------|-------|-------------|----------------|--------|---------|--------|-------------|-----------|-----------------|-------------------|
| Schonfeld et al. 2024 | Hypoxia influences extent and dynamics of suitable fish habitat | peer-reviewed | Marine Ecology Progress Series | estuarine/coastal | fish | habitat modelling | Dynamic hypoxia alters suitable habitat | Close dynamic-habitat analog; not NC/Program 195 | medium | introduction |
| Dixon et al. 2024 | Spatiotemporal variation in habitat suitability in a major estuary | peer-reviewed | estuarine habitat model | Chesapeake Bay | fish | spatiotemporal HSI | DO and temperature drive habitat relationships | Dynamic HSI analog | medium | methods |
| Chesapeake Bay Program 2009 | Habitat suitability modelling workshop | technical report | Chesapeake Bay report | Chesapeake Bay | living resources | workshop synthesis | Converts WQ to living-resource distribution maps | Indicator precedent; not NC or externally validated | medium | methods |
| Rubec et al. 2022 | Essential fish habitat modelling and mapping | technical report | NOAA-related PDF | Florida/coastal | fish | suitability mapping | Uses temperature/salinity/DO/depth suitability functions | Mapping precedent; thresholds may be borrowed | medium | methods |
| Polansky et al. 2018 | Spatiotemporal models of an estuarine fish species | peer-reviewed | NOAA/PDF source | estuary | fish | spatiotemporal model | Demonstrates estuarine spatiotemporal fish modelling | Methods precedent; not stress-indicator framework | medium | methods |
| Berger et al. 2012 | Improving fishery-independent indices with environmental covariates | peer-reviewed | fisheries assessment | lake fish | walleye | index standardization | Environmental variation can influence survey indices | Survey-interpretation analog; freshwater not estuarine | medium | validation |
| Schrandt et al. 2024 | Fishery-independent monitoring design changes | peer-reviewed | Frontiers | Florida | multispecies | survey-design review | Survey consistency matters but designs adapt | Static survey context | medium | discussion |
| Hoyle et al. 2024 | CPUE modelling review | peer-reviewed | NOAA Institutional Repository | general fisheries | multispecies | review | Environmental covariates can reflect catchability, habitat, density; attribution matters | Survey catchability caution | high | methods |

---

## Blocked Validation and Leakage Methods

| Author/Year | Title | Source type | Journal/Report | System | Method | Main finding | Relevance | Evidence quality | Use in manuscript |
|-------------|-------|-------------|----------------|--------|--------|-------------|-----------|-----------------|-------------------|
| Roberts et al. 2017 | Cross-validation strategies for structured ecological data | peer-reviewed | Ecography | general ecology | methods review | Ignoring spatial/temporal structure underestimates prediction error | Justifies blocked validation; not NC-specific | high | validation |
| Valavi et al. 2019 | blockCV R package | peer-reviewed | Methods in Ecology and Evolution | SDM | software/method | Provides spatial/environmental blocking for SDM validation | Supports spatial folds | high | validation |

---

## Data Sources (APIs and Products)

| Source | Type | Variables | Use in paper |
|--------|------|-----------|-------------|
| USGS Water Data APIs | data documentation | streamflow, gauge height, daily values, WQ | methods |
| NOAA CO-OPS API | data documentation | water levels, salinity, temperature, meteorological | methods |
| NOAA NCEI Climate Data Online | data documentation | temperature, precipitation, wind, degree days | methods |
| U.S. Drought Monitor | data documentation | drought categories D0–D4; record starts 2000; weekly | methods |
| MRLC Annual NLCD Collection 1.0 | data documentation | land cover, impervious surface, change; annual 1985–2023 | methods |
| USDA NASS Cropland Data Layer / CropScape | data documentation | crop-specific land cover; annual; resolution change 2024 | methods |

---

## Historical Analogies (Motivation Only — Not Direct NC Evidence)

| Author/Year | Title | Source type | System | Relevance | Evidence quality | Use in manuscript |
|-------------|-------|-------------|--------|-----------|-----------------|-------------------|
| GLFC, n.d. | Great Lakes fisheries history | agency report | Great Lakes | Historical analogy only | medium | introduction cautionary |
| USGS, n.d. | Historical changes in major fish resources of the Great Lakes | technical report | Great Lakes | Cautionary analogy; WQ/habitat links to fish can be hard to quantify | high | discussion caution |
| Auer 2003 | Lake sturgeon rehabilitation plan | technical report | Great Lakes | Habitat degradation analogy only | medium | supplement only |
| Baril et al. 2018 | Lake sturgeon spawning habitat | peer-reviewed | Great Lakes | Historical motivation | medium | supplement only |

---

## Methods Decisions Log

| Date | Decision | Prior art | Author |
|------|----------|-----------|--------|
| PLACEHOLDER | — | — | — |

---

## Revision Log

| Date | Change | Author |
|------|--------|--------|
| 2026-05-25 | Initial placeholder | Claude Code |
| 2026-05-25 | Populated from Prompt 3 Output 2 | Claude Code |
