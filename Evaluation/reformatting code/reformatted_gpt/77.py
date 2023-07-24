# Pymc model
cluster_means = []
np.random.seed(45)
with pm.Model() as model:
    pi = pm.Dirichlet('pi', np.ones(K))
    comp_dist = []
    mu = []
    sigma_sq = []
    cov = []
    for i in range(K):
        temp_mean = np.random.randint(low=20, high=230, size=D)
        mu.append(pm.Normal('mu%i' % i, temp_mean, 20, shape=D))
        sigma_sq.append(pm.InverseGamma('sigma_sq%i' % i, 1, 1, shape=D))
        cov.append(tt.nlinalg.alloc_diag(sigma_sq[i]))
        comp_dist.append(pm.MvNormal.dist(mu=mu[i], cov=cov[i]))
        cluster_means.append(temp_mean)
    xobs = pm.Mixture('x_obs', pi, comp_dist, observed=X_shared)