def computeK(X):
    K = X.dot(X.T).astype(double)
    return K