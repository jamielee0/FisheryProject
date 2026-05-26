"""joins — Spatial and temporal joins between survey tows and environmental covariates.

Leakage risk is highest here. Every join function must note:
  - The temporal lag or window used
  - Whether the covariate is interpolated (risk: environmental interpolation leakage)
  - Whether the join introduces spatial autocorrelation
  - Whether it assigns surface observations to bottom habitat (forbidden)

Document join strategy decisions in the leakage_audit.md before use.
"""
