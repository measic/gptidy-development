# get centers
sample_preds = d_model["Kmeans"][2].predict(pca_samples)
centers = d_model["Kmeans"][2].cluster_centers_
preds = d_model["Kmeans"][2].fit_predict(reduced_data)