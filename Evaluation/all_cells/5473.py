def computeK(x1, x2, thetas):
    
    # not optimal implementation.
    K = []
    for i in range(len(x1)):
        innerList = []
        for j in range(len(x2)):
            innerList.append(k_n_m(x1[i], x2[j], thetas))
        K.append(innerList)
    return np.array(K)