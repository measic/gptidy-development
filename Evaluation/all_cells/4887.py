# Display sample log-data after applying PCA transformation in two dimensions
df_display = pd.DataFrame(np.round(pca_samples, 4), columns = ['Dimension 1', 'Dimension 2'])
df_display.index = log_samples.index
display(df_display)