"""Feature engineering namespace for habitat stress covariates.

Every feature function must state whether the input observation is surface or
bottom, which publication risks it touches, and whether it is a water-quality,
hydrological, or land-cover feature.

Land-cover features belong to Model D only and must improve held-out
performance after water quality and hydrology are already included.
"""
