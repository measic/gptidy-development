import numpy as np

C = np.array([C])
print(C)
print('transpose\n',C.transpose())
print('A more compact way to transpose where T is an alias to the transpose function')
print(C.T)
C = np.array([6,8])
print(np.matmul(C,C.T))