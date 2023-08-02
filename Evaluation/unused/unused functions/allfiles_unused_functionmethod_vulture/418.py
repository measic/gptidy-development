def create_X_and_t(X1, X2):
    X = np.concatenate((X1, X2))
    t = np.concatenate((-np.ones(len(X1)), np.ones(len(X2))))
    
    return X, t 