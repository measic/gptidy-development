# Produce a scatter matrix without outliers... distribution appears more normal
pd.scatter_matrix(good_data, alpha = 0.3, figsize = (14,8), diagonal = 'kde');