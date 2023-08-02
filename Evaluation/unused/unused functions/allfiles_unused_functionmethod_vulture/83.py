def regression_optimize_theta(x, y, sigma_n, kernel, params_0=[0.1, 0.1]):
    
    """
    Optimizes parameters for the data given by maximizing logp(data|parameters)
    :param x: numpy array of data where we have sampled
    :param y: numpy array of y values for data where we have sampled
    :sigma_n: float sigma_n
    :param kernal: the kernel function which we will be using
    :param params_0: list params_0 this is a list that has the initial params (must be length
    of params which your kernel is expecting) from this point the optimizer will run.
    :return: list (optimal_params + [sigma_n]), this is a list that has the optimal parameterss (must be length
    of params which your kernel is expecting), but also has sigma_n in the last index.
    """
    
    def log_pY(theta):
        """
        Calculates the - log(p(y|parameters))
        :param theta: list params this is a list that has the params (must be length
        of params which your kernel is expecting)
        :return: float - log(p(y|parameters)) (using negative because our optimizer is a minimizer)
        """
        K = kernel(x, x, theta, sigma_n) #+
        log_k = np.linalg.slogdet(K)[1] #+
        output = 0.5 * np.matmul(np.matmul(y.T, np.linalg.inv(K)),y) #-
        output += 0.5 * log_k #-
        return output #-

    res = minimize(log_pY, params_0, method='nelder-mead', options={'xtol': 1e-8, 'disp': False}) #+
    return list(res.x) + [sigma_n] # +