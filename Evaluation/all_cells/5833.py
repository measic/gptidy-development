# mean of each group
m1 = np.mean(X1,axis=0)
m2 = np.mean(X2,axis=0)

m1
m2

# between spread matrix
dm1 = (np.add(m1,-m))
dm1 = dm1[np.newaxis].transpose()

dm2 = (np.add(m2,-m))
dm2 = dm2[np.newaxis].transpose()

Sb = np.add(N1*np.dot(dm1, dm1.transpose()),N2*np.dot(dm2, dm2.transpose()))


du = m2 - m1

np.dot(du, du.transpose())

Sb