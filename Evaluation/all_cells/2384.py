with model:
    trace = pm.sample(2000, n_init=50000, random_seed=SEED)