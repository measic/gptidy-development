# mean of each group
m1 = np.mean(X1,axis=0)
m2 = np.mean(X2,axis=0)

# spread matrix for each group
u1 = np.add(X1,-m1).transpose()
S1 = np.matmul(u1,u1.transpose())

u2 = np.add(X2,-m2).transpose()
S2 = np.matmul(u2,u2.transpose())

# within spread matrix
Sw = np.add(S1,S2)

# between spread matrix
dm1 = (np.add(m1,-m))
dm1 = dm1[np.newaxis].transpose()

dm2 = (np.add(m2,-m))
dm2 = dm2[np.newaxis].transpose()

Sb = np.add(N1*np.dot(dm1, dm1.transpose()),N2*np.dot(dm2, dm2.transpose()))

print('Within spread matrix:')
Sw

print('Between spread matrix:')
Sb