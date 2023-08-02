variable_def = X.loc[:, X.dtypes == np.float64]
Z2 = X.loc[:, X.dtypes == np.int64]
X_numeric = pd.concat([variable_def, Z2], axis=1)