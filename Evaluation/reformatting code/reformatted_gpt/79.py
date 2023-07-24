def gauss_seidel(A, b, x0):
    """ 
    Implements the Gauss-Seidel method with a over-relaxation parameter
    """
    # tolerance level for stopping rule
    tol = 1e-8
    eps = 1
    # iteration counter and max number of iterations
    it = 0
    maxit = 100
    
    # initialize x
    x = x0
    Q = np.triu(A)
    Q_inv = np.linalg.inv(Q)
    
    while eps > tol and it < maxit:
        it += 1 
        x_new = Q_inv @ b + (np.eye(len(b)) - Q_inv @ A) @ x
    
        eps = np.linalg.norm(x_new - x)
        
        x = x_new
        
    return x