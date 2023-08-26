Z1 = X.loc[:, X.dtypes == np.float64]
Z2 = X.loc[:, X.dtypes == np.int64]
variable_def = pd.concat([Z1, Z2], axis=1)