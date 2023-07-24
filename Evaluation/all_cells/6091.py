from scipy.linalg import pinv

H = np.array([[1, 0.]]) 
z0 = 3.2
x = np.dot(pinv(H), z0)
print(x)