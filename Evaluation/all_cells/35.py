# Create datapoints between X_min and X_max to visualize the line of best fit
X_best_fit = np.arange(X.numpy().min(), X.numpy().max(), 0.001)[:,None]