#Only run once!
X = np.hstack((X, np.ones((X.shape[0], 1))))

#Initialize Weights to zero:
w = np.zeros(X.shape[1])