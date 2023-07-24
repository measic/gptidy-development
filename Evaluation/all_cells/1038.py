batch_size = 1

beta3 = least_squares_SGD(Strain1_y, Strain1_z, initial_w, batch_size, max_iters, gamma)      #beta from y = X*beta --> missing the column of ones'
res3 = definitive_res(Stest1_z.dot(beta3))
len(Stest1_y[Stest1_y==res3])/len(Stest1_y)