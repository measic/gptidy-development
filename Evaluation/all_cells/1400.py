E = np.array([[2,2],[1, 1]])
print(E)
F = np.array([3,4,5,6,7,8])
#create a 3x2 matrix from the vector.
F=F.reshape(3,2)
#this line will fail as 'shapes not aligned' because E is 2x2 and F is 3x2
#print(np.matmul(E,F))
# this line succeeds because E (2x2) can be multiplied with F.T (2x3)
print(np.matmul(E,F.T))