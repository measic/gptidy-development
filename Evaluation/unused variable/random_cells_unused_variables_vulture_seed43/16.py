# LDA
lda = LinearDiscriminantAnalysis(n_components=2)
X_lda = lda.fit(X_iris, y).transform(X_iris)

## PCA See no need to use labels
pca = sklearnPCA(n_components=2)
X_pca = pca.fit_transform(X_iris)