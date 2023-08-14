with pm.Model() as model:
    # covariance function
    ℓ = pm.Gamma("ℓ", alpha=2, beta=2)
    # informative, positive normal prior on the period 
    η = pm.HalfNormal("η", sd=5)
    cov = η**2 * pm.gp.cov.ExpQuad(1, ℓ)
    
    gp = pm.gp.Latent(cov_func=cov)
    
    # make gp prior
    f = gp.prior("f", X=x[:,None])
    
    # logit link and Bernoulli likelihood
    p = pm.Deterministic("p", pm.math.invlogit(f))
    y_ = pm.Bernoulli("y", p=p, observed=y)
    
    trace = pm.sample(1000)