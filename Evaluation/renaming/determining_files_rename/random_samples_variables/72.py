df_diffs = (np.abs(samples - true_centers.iloc[0]) < np.abs(samples - true_centers.iloc[1])).applymap(lambda x: 0 if x else 1)
variable_def = pd.concat([df_diffs, pd.Series(sample_preds, name='PREDICTION')], axis=1)
sns.heatmap(variable_def, annot=True, cbar=False, yticklabels=['sample 0', 'sample 1', 'sample 2'], linewidth=0.1, square=True)
plt.title('Samples closer to\ncluster 0 or 1?')
plt.xticks(rotation=45, ha='center')
plt.yticks(rotation=0)