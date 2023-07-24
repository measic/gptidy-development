beta1, l = least_squares(Strain1_y, Strain1_z)  # beta from y = X^T*beta --> missing the column of ones'
# print(beta1)
res1 = definitive_res(Stest1_z.dot(beta1))
# print(res1)
len(Stest1_y[Stest1_y == res1]) / len(Stest1_y)