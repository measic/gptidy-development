def get_Ks(x_new, x, kernel, theta):
    """
    Generates K, KS, and KSS by using the given kernel and theta
    :param x_new: numpy array of new data
    :param x: numpy array of data where we have sampled
    :param theta: list (params + [sigma_n]), this is a list that has the params (must be length
    of params which your kernel is expecting), but also has sigma_n in the last index.
    :return: np.array(np.array) K, np.array(np.array) KS, np.array(np.array) KSS  all as described above.
    """
    K = kernel(x, x, theta[:-1], theta[-1]) # K #-
    KS = kernel(x_new, x, theta[:-1], theta[-1]) # K* #-
    KSS = kernel(x_new, x_new, theta[:-1], theta[-1]) # K** #-
    return K, KS, KSS #-