# Students should write code here
distances = pairwise_distances(tf_idf, queries, metric='euclidean')
closest_cluster = np.argmin(distances, axis=1)