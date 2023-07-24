import cvxopt

def compute_multipliers(X, t):
    N = X.shape[0]
    K = computeK(t.reshape(-1,1) * X)
    
    P = cvxopt.matrix(K)
    q = cvxopt.matrix(-np.ones(N))
    A = cvxopt.matrix(t).T
    b = cvxopt.matrix(0.0)

    sol = cvxopt.solvers.qp(P, q, A=A, b=b)
    a = np.array(sol['x'])

    return a