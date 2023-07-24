u = np.add(X,-m).transpose()
S_hat = np.matmul(u,u.transpose())

Sigma_hat = S_hat/(N-1)

print(' Spread matrix Sw:')
Sw

print(' Spread matrix Sb:')
Sb

print(' Total spread matrix S_hat:')
S_hat

print(' Global covariance matrix Sigma_hat:')
Sigma_hat

print(' Covariance matrix expected Sigma:')
S