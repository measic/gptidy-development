#A pythonic way to do this is to use a list comprehension to create the sequence that initializes the array.
A = np.array([i*2 for i in range(1,5)])
print(A)