# kernel PCA
gamma = 100
sq_x  = -2 * X @ X.T + np.sum(X**2,1) + np.sum(X**2,1,keepdims=True)
K     = np.exp(-gamma * sq_x)
N     = K.shape[0]
one_n = np.ones((N,N)) / N
K2    = K - one_n.dot(K) - K.dot(one_n) + one_n.dot(K).dot(one_n)
eigvals, eigvecs = np.linalg.eigh(K2)