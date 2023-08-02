def gp_log_likelihood(x_train, t_train, theta, beta, C=None, invC=None):
    
    if C is None:
        K = computeK(x_train, x_train, theta)
        C = K + (1/beta)*np.eye(len(K))
    
    if invC is None:
        invC = np.linalg.inv(C)
    
    lp = np.log(1/np.sqrt((np.linalg.det(2 * np.pi * C))) * np.exp((-1/2) * t_train.T.dot(invC).dot(t_train)))
    
    return lp, C, invC