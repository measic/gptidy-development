def find_f(K, y, iterations=100):
    """
    Finds f using a iterative aproach also finds p(y|f)
    :param K: np.array(np.array) covariance matrix of data points we have observed
    :param y: numpy array of the y value of the data points we have observed
    :iterations: int optional default = 100 number of iterations we will preform to optimize f
    :return: (numpy array <float> f, numpy array <float> p(y|f)) f is the latent function value for each of the 
    sampled data points, p(y|f) is the probability of y given the latent function we calculated
    make sure to calculate p(y|f) after having approximated f_hat.
    """
    n = len(y)                   #-
    f = np.zeros(n)              #-
    grad = np.zeros(n)           #-
    for i in range(iterations):  #-
        for j in range(n):       #-
            sigmoid_v = sigmoid(f[j]*y[j]) #-
            grad[j] = (1-sigmoid_v)*y[j]   #-
        f = np.array(np.matmul(K, grad)).flatten()  #-
        
    y_giv_f = np.zeros(n)                #-
    for j in range(n):                   #-
        y_giv_f[j] = sigmoid(f[j]*y[j])  #-
        
    return f, y_giv_f                    #-