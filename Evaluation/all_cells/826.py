A = np.array([[10, 2, 4],
              [4, 15, 6],
              [7, 8, 20]])

print( np.linalg.norm(np.eye(len(b)) - np.linalg.inv(np.triu(A)) @ A) )