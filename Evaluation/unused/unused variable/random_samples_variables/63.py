np.random.seed(1234)
W = {user:np.random.rand(31) - 0.5 for user in users}
b = {user:np.random.rand(1) - 0.5 for user in users}