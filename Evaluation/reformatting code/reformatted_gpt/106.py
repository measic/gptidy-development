# Can't do PCA on sparse matrix, use TruncatedSVD instead
from sklearn.decomposition import TruncatedSVD

pca_transformer = TruncatedSVD(2).fit(X_train)
X_train_2d = pca_transformer.transform(X_train)
X_test_2d = pca_transformer.transform(X_test)