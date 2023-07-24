# Scaling Functions

def NRM1(X):
    """Scale by dividing by the 1-norm"""
    norm = np.linalg.norm(X, ord=1)
    return X / norm

def SCL1(X):
    """Scale between (-1, 1)"""
    mean = X.mean()
    maximum = X.max()
    minimum = X.min()
    return (X - mean) / (maximum - minimum)

def TRSH(X, threshold_value=20):
    X = [0 if val < threshold_value else 1 for val in X]
    return X