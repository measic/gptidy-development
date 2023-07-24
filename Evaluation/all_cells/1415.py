A = np.array([1,5,3,4,8,3])
B = A>2
print("B shows which elements of A are greater than 2\n",B)
print("An element of B is type:", type(B[0]))  #numpy boolean
print("An ordinary Boolean in Python (not numpy) is a separate type but usually can be interchanged with a numpy bool by implicit conversion.")
test_bool = True  #Python boolean
print(type(test_bool))
test = [False, True,True,True,True,True]  #list from Python booleans
print("Are the 2 boolean arrays equal?\n", B == test)  #check the equality of the numpy array and list