lambdas = np.logspace(-5, 0, 15)

# bluid poly
tx_tr = build_poly(Strain1_z, 1)
tx_te = build_poly(Stest1_z, 1)

# ridge regression with different lambda
rmse_tr = []
rmse_te = []
for ind, lambda_ in enumerate(lambdas):
    # ridge regression
    weight = ridge_regression(Strain1_y, tx_tr, lambda_)
    rmse_tr.append(np.sqrt(2 * compute_mse(Strain1_y, tx_tr, weight)))
    rmse_te.append(np.sqrt(2 * compute_mse(Stest1_y, tx_te, weight)))
print(rmse_tr, rmse_te)
#print("last weight:",weight)