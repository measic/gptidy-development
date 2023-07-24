def leaky_relu(z, alpha=0.01):
    return np.maximum(alpha * z, z)