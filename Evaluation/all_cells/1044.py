def kernel(x0, x1, params, sigma_n):
    """
    Runs the exponential kernal function and returns output
    :param x0: numpy array with values of x
    :param x1: numpy array with values of x'
    :param params: [float simga_f, float l]
    :param sigma_n: float sigma_n
    :return: np.array(np.array) nested np.arrays where output[i,j] == k(x0[i],x1[j])
    """
    diff = np.subtract.outer(x0, x1)  #-
    value = params[0]**2 * np.exp( -0.5 * (1.0/params[1]**2) *diff**2)  #-
    value[np.where(diff == 0.0)] += sigma_n**2   #-
    return value  #-