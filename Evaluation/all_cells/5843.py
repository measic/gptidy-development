from scipy import stats
print('Original number of features:', X_iris.shape[1])
print('LDA:')
print(' Explaned variance ratio: {}'.format(lda.explained_variance_ratio_))
print(' Reduced number of features:', X_lda.shape[1])
stats.describe(X_lda)


print('PCA:')
print(' Explaned variance ratio: {}'.format(pca.explained_variance_ratio_))
print(' Reduced number of features:', X_pca.shape[1])
stats.describe(X_pca)