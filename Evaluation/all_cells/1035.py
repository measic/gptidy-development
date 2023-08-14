beta2 ,l= least_squares_GD(Strain1_y, Strain1_z, initial_w, max_iters, gamma)      #beta from y = X*beta --> missing the column of ones'
res2 = definitive_res(Stest1_z.dot(beta2))
len(Stest1_y[Stest1_y==res2])/len(Stest1_y)