corr_returns = returns.corr(method="pearson")

plt.figure(figsize=(9, 5))
sns.heatmap(
    corr_returns,
    cbar=True,
    annot=True,
    annot_kws={"size": 15},
    xticklabels=tickers,
    yticklabels=tickers,
    cmap="bone_r")
plt.title("Correlation Matrix")
plt.show()