"""Spatial and temporal join namespace for survey tows and covariates.

Leakage risk is highest here. Every join function must note the temporal lag or
window used, interpolation status, spatial autocorrelation risk, and whether the
join assigns surface observations to bottom habitat.
"""
