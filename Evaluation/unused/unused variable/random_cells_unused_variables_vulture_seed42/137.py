y_kmeans = []
centers_kmeans = []
for i, x in enumerate(X):
    kmeans = KMeans(n_clusters=5)#, init=np.array([(i*200/6.0, 25) for i in range(1,6)]))
    kmeans.fit(x)
    centers_kmeans.append(kmeans.cluster_centers_)
    y_kmeans.append(kmeans.predict(x))