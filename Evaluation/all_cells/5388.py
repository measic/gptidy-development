# TODO: Scale the data using the natural logarithm
log_data = None

# TODO: Scale the sample data using the natural logarithm
log_samples = None

# Produce a scatter matrix for each pair of newly-transformed features
pd.scatter_matrix(log_data, alpha = 0.3, figsize = (14,8), diagonal = 'kde');