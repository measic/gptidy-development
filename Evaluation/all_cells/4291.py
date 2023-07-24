import seaborn
data_corr = data.corr()
print(data_corr)
seaborn.heatmap(data_corr)