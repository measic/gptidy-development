def gp_predictive_distribution(x_train, t_train, x_test, theta, beta, C=None):
    
    if C is None:
        K = computeK(x_train, x_train, theta)
        C = K + (1/beta)*np.eye(len(K))
    
    C_inv = np.linalg.inv(C)
    
    mean_test = np.zeros(len(x_test))
    covar_test = np.zeros((len(x_test), len(x_test)))
    
    for i, x_t in enumerate(x_test):
        # kernel evaluated between all training points and the new x_test 
        k = np.array([k_n_m(x_n, x_t, theta) for x_n in x_train])   
        # kernel evaluated in the x_test with itself added of variance
        c = k_n_m(x_t, x_t, theta) + 1/beta        
        k_dot_C = np.matmul(k.T, C_inv) 
        
        mean_test[i] = np.matmul(k_dot_C,t_train)
        covar_test[i][i] = c - np.matmul(k_dot_C, k)

    return mean_test, covar_test, C