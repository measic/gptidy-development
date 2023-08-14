#This is a "non-pythonic" way to achieve the desired result. The loop is relatively slow.
# Setting the data type to integer is not usually necessary but with numpy the default is float.
#initialize an empty array of 0 elements
A = np.empty(0,dtype=int)  
for i in range(1,5):
    A = np.append(A, [i*2])
    print(A)    