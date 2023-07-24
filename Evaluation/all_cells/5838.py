print('A and A transpose')
A
A.T

print('check eigenvectors')
# Checking the norms
np.linalg.norm(v1)
np.linalg.norm(v2)

# If I was reducing form 3s to 2d than at leats 2 eigenvetors are orthogornal
print('Since A is NOt symetric their eigenvectors are not orthogonal')

v1.dot(v2.T)

print('check eigenvalues')

# checking eigenvalues
print('cheking trace(A) and sum of all eigenvalues')
np.sum(eigen_values)
np.trace(A)

assert np.abs(np.sum(eigen_values) - np.trace(A)) < 0.1