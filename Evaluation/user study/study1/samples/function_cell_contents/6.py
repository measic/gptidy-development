def function_def(data, k, seed=None):
    """Randomly choose k data points as initial centroids"""
    if seed is not None:
        np.random.seed(seed)
    n = data.shape[0]
    rand_indices = np.random.randint(0, n, k)
    centroids = data[rand_indices, :].toarray()
    return centroids