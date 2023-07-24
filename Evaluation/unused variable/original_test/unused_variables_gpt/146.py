# Display sample log-data after having a PCA transformation applied
df_display = pd.DataFrame(np.round(pca_samples, 4), columns = pca_results.index.values)
df_display.index = log_samples.index
display(df_display)