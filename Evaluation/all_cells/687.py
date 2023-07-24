retained_info = (Sigma[0] + Sigma[1]) / np.sum(Sigma)
print("Estimativa de informação retida: {}%".format(100*retained_info))