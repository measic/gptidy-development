# TODO: Scale the data using the natural logarithm
log_data = np.log(data.copy())
log_data2 = np.log(data2.copy())

# TODO: Scale the sample data using the natural logarithm
log_samples = np.log(samples.copy())

# Produce a scatter matrix for each pair of newly-transformed features
pd.scatter_matrix(log_data2, alpha = 0.3, figsize = (14,8), diagonal = 'kde');