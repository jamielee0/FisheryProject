# endpoint_verification.md
## Survey Endpoint Verification Log — Trees to Seas

**Purpose:** Track verification status of every species-survey endpoint before it is used in
model code. Codex must read this file before writing endpoint-specific code.

**Last updated:** 2026-05-25 (populated from Prompts 2 + 3)

**Status key:**
- `VERIFIED` — confirmed against primary source with no known conflicts
- `CONFLICT` — documented discrepancy between sources; must be resolved before use
- `UNCONFIRMED` — not yet confirmed against data documentation or NCDMF/SEAMAP metadata
- `EXCLUDED` — out of scope for this paper
- `SEPARATE_MODULE` — only for a dedicated module with confirmed outcome data

**Endpoint policy:** For a new retrospective ecological model, use fixed, biologically/agency-confirmed
cutoffs for comparability across years. To reproduce official annual JAI time series, use year-specific
agency definitions if NCDMF confirms they changed. For croaker and spot, both approaches must be
reported as sensitivity analyses.

---

## Program 195 Survey Design

| Field | Value |
|-------|-------|
| Survey name | NCDMF/SEAMAP Program 195 Pamlico Sound Trawl Survey |
| Survey type | Stratified random bottom trawl |
| Sampling months | June and September |
| Annual grid target | 54 grids/month; 108 grids/year |
| Strata count | Seven strata |
| Coverage | Pamlico Sound and adjacent lower Neuse, Pamlico, Pungo estuarine waters |
| Temporal record | Active since 1987; data used here: preferred 1995–2024 |
| 2020–2021 status | COVID-disrupted; treat as sensitivity years |
| 2025 status | SUSPENDED — do not assume 2025+ continuity |
| Source | SEAMAP South Atlantic Program 195 documentation |
| Verified | TRUE |

---

## Blue Crab (*Callinectes sapidus*)

| Field | Value |
|-------|-------|
| Survey | Program 195 |
| Outcome variables | CPUE, biomass |
| Recruit cutoff | **<127 mm carapace width** |
| Adult/fully recruited | ≥127 mm carapace width |
| Source | NCDMF Blue Crab FMP Amendment 3 (2025); NCDMF Blue Crab FMP Review (2023) |
| Consistent across sources | YES — no major conflict found |
| Verified | **TRUE** |
| Notes | Strongest Program 195 endpoint in the species set. Programs 195, 120, and 100 all use <127 mm CW. Recruit/adult contrast useful for spatial redistribution analysis. |
| Sensitivity analyses needed | Yes: sex-specific contrasts, June vs September patterns, 2020–2021 sampling flags |

---

## Atlantic Croaker (*Micropogonias undulatus*)

### September Juvenile Endpoint

| Field | Value |
|-------|-------|
| Survey | Program 195 |
| Outcome variables | CPUE, biomass, juvenile index |
| Cutoff | **<210 mm total length** |
| Month | September |
| Sources | NCDMF Croaker FMP Review 2023; NCDMF Croaker FMP Review 2024 |
| Consistent across sources | YES |
| Verified | **TRUE** |
| Notes | Strong September endpoint. Verify unit continuity by year. |

### June Juvenile Endpoint — ACTIVE CONFLICT (Core Publication Risk #7)

| Field | Value |
|-------|-------|
| Status | **CONFLICT — DO NOT FINALIZE UNTIL RESOLVED** |
| Candidate 1 (latest) | <140 mm total length — NCDMF Croaker FMP Review 2024 |
| Candidate 2 (prior) | <160 mm total length — NCDMF Croaker FMP Review 2023; prior years |
| Conflict explanation | 2024 review appears to change or refine the June cutoff. The 2022–2023 official documents used <160 mm TL. Whether this change represents a revision, a reporting error, or a deliberate biological update is unknown. |
| Verified | **FALSE** |
| Recommended action | Confirm with NCDMF which cutoff applies historically. If NCDMF confirms a year-specific change, document the year it changed and apply the appropriate cutoff per year. Run both as sensitivity analyses regardless. |
| Manuscript requirement | Must explain whether fixed or year-specific cutoffs are used. Report both as sensitivity. |

**Resolution status: UNRESOLVED**

---

## Spot (*Leiostomus xanthurus*)

### September Juvenile Endpoint

| Field | Value |
|-------|-------|
| Survey | Program 195 |
| Outcome variables | CPUE, biomass, juvenile index |
| Cutoff | **<190 mm total length** |
| Month | September |
| Sources | NCDMF Spot FMP Review 2023; NCDMF Spot FMP Review 2024 |
| Consistent across sources | YES for September TL |
| Verified | **TRUE** |
| Notes | Strong September endpoint. Unit appears stable as total length. |

### June Juvenile Endpoint — ACTIVE UNIT CONFLICT (Core Publication Risk #8)

| Field | Value |
|-------|-------|
| Status | **UNIT CONFLICT — DO NOT FINALIZE UNTIL RESOLVED** |
| Candidate value | <140 mm (unit disputed) |
| 2022 update | NCDMF 2022 Spot Update used <140 mm TL after age-0/age-1 analysis |
| 2023 source | NCDMF 2023 Spot FMP Review and figure captions reference FL |
| 2024 source | NCDMF 2024 Spot FMP Review text references TL in some contexts |
| Conflict explanation | Different measurement types (fork length vs total length) appear in different report years or sections. Biologically, TL and FL differ by a predictable ratio, but applying the wrong unit creates a systematic error in juvenile classification. The 2022 update specifically changed the cutoff using age composition — the unit used in that update needs confirmation. |
| Verified | **FALSE** |
| Recommended action | Inspect raw Program 195 measurement fields to determine which length type is recorded for spot in each survey year. Confirm with NCDMF which cutoff and unit applies. Apply FL-to-TL conversion or separate covariate if units changed. Run both as sensitivity. |
| Manuscript requirement | Report the unit conflict and resolution in the endpoint table (Table 2) and supplement. |

**Resolution status: UNRESOLVED**

---

## Southern Flounder (*Paralichthys lethostigma*)

| Field | Value |
|-------|-------|
| Survey | Program 195 |
| Outcome variables | **Occurrence, CPUE, biomass only** (pending endpoint confirmation) |
| Juvenile endpoint | **NO CONFIRMED Program 195 cutoff** |
| NCDMF Program 120 | Used for juvenile index in 2019 assessment context |
| Program 195 status | Listed as additional data in 2019 assessment but not used as JAI |
| Southern Flounder Stock Assessment SA 2022 | Official assessment exists; confirm citation before use |
| Verified | **FALSE** |
| Recommended action | Ask NCDMF whether Program 195 can support a southern flounder juvenile endpoint. If no cutoff is confirmed, include as occurrence/CPUE/biomass only. |
| Manuscript requirement | State explicitly that southern flounder is included as occurrence/CPUE/biomass only, and explain why no juvenile endpoint is applied. |

**Resolution status: UNRESOLVED — include as conditional species**

---

## Atlantic Menhaden (*Brevoortia tyrannus*)

| Field | Value |
|-------|-------|
| Status | **EXCLUDED from first paper** |
| Reason | Demersal bottom trawl (Program 195) has poor catchability/endpoint for menhaden. Menhaden occupy broad physicochemical conditions, are pelagic as adults, and require a menhaden-specific survey endpoint (Program 915, Program 120, seine, plankton) for a defensible analysis. |
| Condition for inclusion | Add and document a menhaden-specific survey endpoint in this file before any menhaden code is written. |

---

## Eastern Oyster (*Crassostrea virginica*)

| Field | Value |
|-------|-------|
| Status | **SEPARATE MODULE ONLY** |
| Outcome data confirmed | **NO** — must confirm before any work begins |
| Acceptable outcome types | Spat settlement, mortality, growth, reef condition, restoration-site survival, disease records, salinity exposure history, harvest-area closure data |
| Restriction | Do not mix oyster analysis with Program 195 trawl-species analysis |
| Condition for inclusion | Confirm outcome data availability. Document outcome type, temporal coverage, spatial coverage, and data provider in this file and in SOURCE_QUALITY_AUDIT.md. |

---

## Values Too Uncertain to Use Directly (from Prompt 2 §5)

1. **Atlantic croaker June juvenile cutoff** — the single most important endpoint uncertainty. See above.
2. **Blue crab DO thresholds** — must be modeled as soft exposure curves. Evidence conflicts: avoidance ~<4 mg/L, severe hypoxia ~<2 mg/L, local field capture association ~<6.5 mg/L (likely not physiological). Use exposure curve approach.
3. **Spot DO thresholds** — use soft modeling: ≤2 mg/L is strong local evidence (Craig et al. 2023), 1.5 mg/L is a lab growth threshold, 4.5 mg/L is a field exclusion candidate not a controlled threshold.
4. **Croaker 5 psu salinity value** — a lab growth-favorable treatment, not a field optimum. Use for freshwater-pulse sensitivity only.
5. **Southern flounder juvenile salinity values** — useful early-life sensitivity evidence but should not be generalized to adult or Program 195 habitat without stage separation.
6. **Atlantic menhaden endpoint** — not ready for first paper without appropriate survey endpoint.
7. **Eastern oyster thresholds** — only for a separate module with confirmed oyster outcomes.
8. **Turbidity, TSS, sedimentation, pH, and chlorophyll thresholds** — mostly generic screens or qualitative relationships. Use as anomalies, percentiles, or continuous covariates unless a species-stage-specific NC threshold is confirmed.

---

## Missing Information — Requires Domain Expert Input (Dr. R)

1. **Croaker June cutoff resolution** — confirm <140 mm TL (2024) or <160 mm TL (2023) per year, and document year of change.
2. **Spot June unit confirmation** — FL or TL? Inspect raw Program 195 data fields.
3. **Southern flounder P195 cutoff** — does Program 195 support a juvenile endpoint for flounder?
4. **Atlantic menhaden endpoint pathway** — Program 120, 915, seine, plankton, or other?
5. **Eastern oyster outcome data** — confirm availability and type.
6. **ModMon depth profile availability** — which years have bottom DO, and what is the spatial coverage of bottom observations?
7. **FerryMon surface-only confirmation** — what specific parameters are available and on which ferry routes?
8. **Turbidity unit harmonization** — NTU, TSS mg/L, Secchi depth, or light attenuation across sources?
9. **Salinity-shock definition** — confirm preferred operational definition: absolute salinity change over 1d/3d/7d/14d; signed freshening; drought-to-rain transition; flow-normalized salinity anomaly.
10. **Threshold representation choice** — suitable/marginal/dangerous classes or continuous soft-exposure functions?
11. **Program 195 metadata fields** — confirm: length unit by species, carapace width for blue crab, sex, maturity/spawner flags, tow duration, swept area, gear changes, vessel changes, station/grid/stratum codes, 2020–2021 sampling flags.

---

## Endpoint Summary Table (from Prompt 3 Output 4)

| Species | Endpoint | Candidate cutoff | Unit | Month/season | Sources | Conflict | Recommended use | Sensitivity needed |
|---------|----------|-----------------|------|--------------|---------|---------|-----------------|-------------------|
| Blue crab | Recruit | <127 | mm CW | June/September | NCDMF Amendment 3; FMP reviews | None | Primary fixed cutoff | Sex-specific; 2020–2021 flags |
| Blue crab | Adult/fully recruited | ≥127 | mm CW | June/September | NCDMF Amendment 3 | None | Secondary/size-class contrast | Optional |
| Atlantic croaker | Juvenile | <140 mm TL | total length | June | NCDMF 2024 | YES: 2022–2023 used <160 mm TL | Provisional primary after NCDMF confirmation | Required: rerun <160 mm TL |
| Atlantic croaker | Juvenile (alternate) | <160 mm TL | total length | June | NCDMF 2022–2023 | YES | Sensitivity-only | Required |
| Atlantic croaker | Juvenile | <210 mm TL | total length | September | NCDMF 2022–2024 | None | Primary September cutoff | Optional: verify by year |
| Spot | Juvenile | <140 mm (FL or TL unresolved) | fork or total length | June | NCDMF 2022–2024 | YES: TL vs FL | Do not finalize until raw field confirmed | Required: FL vs TL sensitivity |
| Spot | Juvenile | <190 mm TL | total length | September | NCDMF reviews | None | Primary September cutoff | Unit harmonization |
| Southern flounder | Juvenile | UNRESOLVED | — | Program 195 June/Sept | NCDMF flounder reviews | Yes: index differs by program | Use occurrence/CPUE/biomass only unless NCDMF confirms cutoff | Required if included |
| Atlantic menhaden | Program 195 | None recommended | — | — | Prompt 1/2 constraint | Yes: gear/endpoint mismatch | EXCLUDED from first paper | N/A |
| Eastern oyster | Module endpoint | Outcome data needed | — | Oyster-relevant season | Prompt 2 | Yes: response mismatch | SEPARATE MODULE ONLY | Yes |

---

## Revision Log

| Date | Change | Author |
|------|--------|--------|
| 2026-05-25 | Initial placeholder | Claude Code |
| 2026-05-25 | Populated from Prompts 2 + 3 | Claude Code |
