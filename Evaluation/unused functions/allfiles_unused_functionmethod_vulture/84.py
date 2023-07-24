def sigmoid(x):
    """
    Calculates the Sigmoid(x)
    :param x: numpy array <dtype=float> points we want to find sigmoid of
    :return: numpy array <dtype=float> the sigmoid of those points
    """
    return 1./(1+np.exp(-x)) #-