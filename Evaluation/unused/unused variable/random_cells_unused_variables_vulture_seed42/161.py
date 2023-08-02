X = 35

with model:
    observations = pm.Binomial("obs", N, observed_proportion, observed=X)