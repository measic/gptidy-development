np.random.seed(1)

# number of data points
n = 200

# x locations
x = np.linspace(0, 1.5, n)

# true covariance
ℓ_true = 0.1
η_true = 1.0
cov_func = η_true**2 * pm.gp.cov.ExpQuad(1, ℓ_true)
K = cov_func(x[:,None]).eval()

# zero mean function
mean = np.zeros(n)

# sample from the gp prior
f_true = np.random.multivariate_normal(mean, K + 1e-6 * np.eye(n), 1).flatten()

# link function
def invlogit(x, eps=sys.float_info.epsilon):
    return (1.0 + 2.0 * eps) / (1.0 + np.exp(-x)) + eps

y = pm.Bernoulli.dist(p=invlogit(f_true)).random()