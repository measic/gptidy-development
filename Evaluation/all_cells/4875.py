# change the columns labels just for visual aesthetic
data2 = data.copy()
data2.columns = [x.replace("_", "\n") for x in data.columns]
# Produce a scatter matrix for each pair of features in the data
pd.scatter_matrix(data2, alpha = 0.3, figsize = (14,8), diagonal = 'kde');