# Plot the weights of the first layer for the best model 
for e in [1,5,10]:
    V = Vs[0][e]
    plt.figure(figsize=(10,6))
    plt.suptitle(f'First layer weights after {e-1} epoch', y = 1.05)
    plot_digits(V.T, num_cols=5)