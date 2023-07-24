X, y = make_classification(n_samples=1000, n_features=2, n_informative=2, 
                           n_redundant=0, n_classes=2, n_clusters_per_class=1,
                           flip_y=0.1, class_sep=4, hypercube=False, 
                           shift=0.0, scale=1.0, random_state=2018)

# Reduce the number of samples with target 1
X = np.vstack([X[y==0], X[y==1][:50]])
y = np.hstack([y[y==0], y[y==1][:50]])