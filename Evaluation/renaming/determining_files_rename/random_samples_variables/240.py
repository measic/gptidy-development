from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score
x = 3
variable_def = GaussianMixture(n_components=x)
variable_def.fit(reduced_data)
preds = variable_def.predict(reduced_data)
centers = variable_def.means_
sample_preds = variable_def.predict(pca_samples)
score = silhouette_score(reduced_data, preds)
print(x, score)