def regression_GP(x_new, x, y, kernel, theta):
    """
    runs regression and returns y_new_bar and variance
    :param x_new: numpy array of new data
    :param x: numpy array of data where we have sampled
    :param y: numpy array of y values for data where we have sampled
    :param kernal:  the kernel function which we will be using
    :param theta: list (params + [sigma_n]), this is a list that has the params (must be length
    of params which your kernel is expecting), but also has sigma_n in the last index.
    :return: (np.array Y_new_bar, np.array var), the mean and variance (only diagonal of variance)
    of the gaussian that describes p(b|a)
    """
    K, KS, KSS = get_Ks(x_new, x, kernel, theta) # +

    y = np.matmul(np.matmul(KS, np.linalg.inv(K)),y) # -
    var = KSS - KS.dot(np.linalg.inv(K).dot(KS.T)) # -
    var = np.diagonal(var) # -
    return(y.squeeze(), var.squeeze()) # -