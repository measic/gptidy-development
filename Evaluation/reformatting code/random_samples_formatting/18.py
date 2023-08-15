# Pymc model
X_shared = theano.shared(X)
minibatch_size = 500
X_minibatch = pm.Minibatch(X, minibatch_size)
np.random.seed(45)
with pm.Model() as model:
    pi = pm.Dirichlet('pi', np.ones(K))
    comp_dist = []
    mu = []
    sigma_sq = []
    cov = []
    for i in range(K):
        mu.append(pm.Normal('mu%i' % i, 127, 80, shape=D))
        sigma_sq.append(pm.InverseGamma('sigma_sq%i' % i, 1, 1, shape=D))
        cov.append(tt.nlinalg.alloc_diag(sigma_sq[i]))
        comp_dist.append(pm.MvNormal.dist(mu=mu[i], cov=cov[i]))
    xobs = pm.Mixture('x_obs', pi, comp_dist,
            observed=X_shared)