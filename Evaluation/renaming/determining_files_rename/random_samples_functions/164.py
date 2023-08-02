def function_def(X, y, w, i):
    x1s = np.arange(7)
    x2s = (-w[2] - w[0] * x1s) / w[1]
    fig = figure(0, (8, 6))
    scatter(X[:, 0], X[:, 1], c=y, s=75)
    scatter(X[i, 0], X[i, 1], c='r', s=75)
    plot(x1s, x2s)
    xlabel('$x_1$', fontsize=20)
    ylabel('$x_2$', fontsize=20)
    grid(1)