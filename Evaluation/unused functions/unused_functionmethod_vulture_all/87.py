def optimize_theta(x, y, kernel, params_0=[0.1, 0.1], sigma_n=0.1):
    def log_pY(theta):                              #-
        K = np.matrix(kernel(x, x, theta, sigma_n)) #-
        f, y_giv_f = find_f(K, y)                   #-
        W = util.calculate_W(f, y)                  #-
        inv_k = np.linalg.inv(K)                    #-
        log_k = np.log(np.linalg.det(K) * np.linalg.det(inv_k+W)) #-
        Y_giv_f = np.prod(y_giv_f)                                #-
        output = 0.5 * np.matmul(np.matmul(f.T, inv_k),f)         #-
        output += 0.5 * log_k                                     #-
        output -= np.log(Y_giv_f)                                 #-
        return output                                             #-

    res = minimize(log_pY, params_0, method='nelder-mead', options={'xtol': 1e-8, 'disp': False}) #-
    return list(res.x) + [sigma_n]    #-