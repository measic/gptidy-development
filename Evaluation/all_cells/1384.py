#demonstrates the difference between axis=0 and axis=1
AX = np.array([[1,2,3],[4,5,6]])
print(AX)
print('sum down', np.sum(AX, axis=0))
print('sum across', np.sum(AX, axis=1))