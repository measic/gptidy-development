print('checking')
A.dot(v2)
eigen_values[1]*v2

np.testing.assert_array_almost_equal(A.dot(v2),
                                         eigen_values[1] *v2,
                                         decimal=6, err_msg='', verbose=True)

print('comparing with scilit learn')
lda = LinearDiscriminantAnalysis(n_components=1)
X_lda = lda.fit(X, labels).transform(X)

v3 = lda.scalings_

print('eigenvectors')

v3.T
v2

print('dot product between scikit learn and our eigenvector')
# 1 means they are aligned
v2.dot(v3)/np.linalg.norm(v3)