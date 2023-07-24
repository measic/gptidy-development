# Let's see what the correlation matrix looks like now: 
c = coef_ridge[coef_ridge != 0]
corr = features[c.index].corr()
plt.matshow(corr)