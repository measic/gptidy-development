n = 5
x, A = vm(n)
print("For n = {}, x = {}".format(n, x) )
print("For n = {}, the condition number is {}".format(n, np.linalg.cond(A)))