from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score
x = 3
clusterer = GaussianMixture(n_components=x)
clusterer.fit(reduced_data)
preds = clusterer.predict(reduced_data)
variable_def = clusterer.means_
sample_preds = clusterer.predict(pca_samples)
score = silhouette_score(reduced_data, preds)
print(x, score)