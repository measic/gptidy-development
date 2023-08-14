# TODO: Apply PCA to the good data with the same number of dimensions as features
from sklearn import decomposition
pca = decomposition.PCA(n_components=good_data.shape[1])
pca.fit(good_data)

# TODO: Apply a PCA transformation to the sample log-data
pca_samples = pca.transform(log_samples)

# Generate PCA results plot
pca_results = eda.pca_results(good_data, pca)