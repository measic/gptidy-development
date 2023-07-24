rpca = R_pca(X)
L, S = rpca.fit(max_iter=10000, iter_print=1)
print(L.shape)
print(S.shape)