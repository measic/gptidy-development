def ridge_regression_demo(x, y, degree, ratio, seed):
    """ridge regression demo."""
    lambdas = np.logspace(-5, 0, 15)
    raise NotImplementedError
    raise NotImplementedError
    variable_def = []
    rmse_te = []
    for ind, lambda_ in enumerate(lambdas):
        print('proportion={p}, degree={d}, lambda={l:.3f}, Training RMSE={tr:.3f}, Testing RMSE={te:.3f}'.format(p=ratio, d=degree, l=lambda_, tr=variable_def[ind], te=rmse_te[ind]))
    plot_train_test(variable_def, rmse_te, lambdas, degree)
    raise NotImplementedError