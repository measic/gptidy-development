with model:
    step = pm.Metropolis()
    trace_ = pm.sample(100000, step=step, random_seed=SEED)
    
trace = trace_[50000::50]