corr = data2.corr()
mask = np.zeros_like(corr)
mask[np.triu_indices_from(mask)] = True
ax = sns.heatmap(corr, mask=mask, annot=True, cmap='RdBu')
ax.figure.set_size_inches([8.,4.])