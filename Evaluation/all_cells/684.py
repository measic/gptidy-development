reduced_sigma = np.zeros((U.shape[1], Sigma.shape[0]))
reduced_sigma[0,0] = Sigma[0]
reduced_sigma[1,1] = Sigma[1]
print("Matriz Sigma Reduzida:\n",reduced_sigma, end="\n\n")
print("Dimensões de Sigma Reduzida:",reduced_sigma.shape)