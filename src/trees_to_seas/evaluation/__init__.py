"""evaluation — Validation metrics, calibration, uncertainty, and ablation reporting.

All required validation components (CLAUDE.md §5):
  - Temporal holdout
  - Spatial holdout
  - Event holdout
  - Ablations
  - Calibration
  - Uncertainty
  - Leakage audit

No headline result may be reported under random-split only.
Random-split results must be labeled "exploratory, not externally validated."
"""
