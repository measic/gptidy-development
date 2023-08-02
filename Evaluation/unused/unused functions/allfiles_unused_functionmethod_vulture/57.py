def vm(n):
    ## define matrix
    A = np.array([i**j for i in range(1,n+1) for j in range(0, n)] )
    A.shape = (n, n)
    ## determine the solution vector
    x_target = np.ones(n)
    b = A @ x_target
    ## solve SLE
    x = np.linalg.solve(A, b)
    
    return x, A