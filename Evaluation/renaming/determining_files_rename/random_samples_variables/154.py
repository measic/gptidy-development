variable_def = np.log(data.copy())
log_data2 = np.log(data2.copy())
log_samples = np.log(samples.copy())
pd.scatter_matrix(log_data2, alpha=0.3, figsize=(14, 8), diagonal='kde')