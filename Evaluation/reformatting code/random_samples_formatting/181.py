from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

n_clusters = 2

# TODO: Apply your clustering algorithm of choice to the reduced data 
clusterer = KMeans(n_clusters=n_clusters, random_state=10)
clusterer = clusterer.fit(reduced_data)

# TODO: Predict the cluster for each data point
preds = clusterer.predict(reduced_data)

# TODO: Find the cluster centers
centers = clusterer.cluster_centers_

# TODO: Predict the cluster for each transformed sample data point
sample_preds = clusterer.predict(pca_samples)

# TODO: Calculate the mean silhouette coefficient for the number of clusters chosen
score = silhouette_score(reduced_data, preds)
print("{} => {}".format(n_clusters, score))