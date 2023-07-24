x = np.linspace(-5, 5, 50)
params = [1, 2, 1, 1]
K = periodic_kernel(x, x, params)
util.visiualize_kernel(K)