beta4,losss=logistic_regression(Strain1_y, Strain1_z, initial_w, max_iters, gamma)
res4 = definitive_res(Stest1_z.dot(beta4))
len(Stest1_y[Stest1_y==res4])/len(Stest1_y)