# Students should write code here
distances = pairwise_distances(tf_idf, tf_idf[0:3], metric='euclidean')
cluster_assignment = np.argmin(distances, axis=1)