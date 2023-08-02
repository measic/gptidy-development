def function_def(data, k, seed=None):
    """Use k-means++ to initialize a good set of centroids"""
    if seed is not None:
        np.random.seed(seed)
    centroids = np.zeros((k, data.shape[1]))
    idx = np.random.randint(data.shape[0])
    centroids[0] = data[idx, :].toarray()
    squared_distances = pairwise_distances(data, centroids[0:1], metric='euclidean').flatten() ** 2
    for i in xrange(1, k):
        idx = np.random.choice(data.shape[0], 1, p=squared_distances / sum(squared_distances))
        centroids[i] = data[idx, :].toarray()
        squared_distances = np.min(pairwise_distances(data, centroids[0:i + 1], metric='euclidean') ** 2, axis=1)
    return centroids