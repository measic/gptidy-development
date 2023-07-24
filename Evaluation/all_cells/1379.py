#Element
#convert an array of size 1 (scalar array) into an ordinary scalar element 
print(A)
print(type(A)) #before conversion it is a numpy array
a = np.asscalar(A)
print(a)
print(type(a)) #after conversion it is an int (integer)