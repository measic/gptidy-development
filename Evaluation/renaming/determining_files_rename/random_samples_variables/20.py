variable_def = pairwise_distances(tf_idf, tf_idf[0:3], metric='euclidean')
cluster_assignment = np.argmin(variable_def, axis=1)