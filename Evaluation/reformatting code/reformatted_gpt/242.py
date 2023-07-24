# X_numeric has duplicate columns. The code below removes the duplicate columns
_, i = np.unique(X_numeric.columns, return_index=True)
X_Num_Cov = X_numeric.iloc[:, i]
X_Num_Cov.to_csv('Numerical_FS.csv')
X_Num_Cov.shape