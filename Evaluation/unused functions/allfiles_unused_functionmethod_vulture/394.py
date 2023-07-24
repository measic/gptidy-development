def elu(z, alpha=1):
    return np.where(z < 0, alpha * (np.exp(z) - 1), z)