"""models — Model training for the model ladder (A, B, C, D, benchmark).

All training scripts must log:
  - Random seed
  - Data hash (hash of the training dataframe)
  - Split strategy (temporal / spatial / event holdout — never random split only)

The benchmark model must not be the only model reported.
No result from this module may support a causal claim.
See CLAIM_BOUNDARIES.md before writing any result narrative.
"""
