A = np.matmul(Sw_inv, Sb)

eigen_values, V = np.linalg.eig(A)

print('A:')
A

print('eigen_values:')
eigen_values
print('eigen_vectors matrix:')
V

print('eigen_vectors :')
v1 = V[:,0]
v2 = V[:,1]

v1
v2