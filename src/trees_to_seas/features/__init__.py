"""features — Feature engineering for habitat stress covariates.

Every feature function must state in its docstring:
  - Whether the input observation is surface or bottom
  - Which publication risks (AGENTS.md Core Publication Risks) it is relevant to
  - Whether it is a water-quality, hydrological, or land-cover feature

Land-cover features belong to Model D only and must improve held-out
performance after water quality and hydrology are already included.
"""
