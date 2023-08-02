from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score
x = 3
clusterer = GaussianMixture(n_components=x)
clusterer.fit(reduced_data)
preds = clusterer.predict(reduced_data)
centers = clusterer.means_
sample_preds = clusterer.predict(pca_samples)
variable_def = silhouette_score(reduced_data, preds)
print(x, variable_def)