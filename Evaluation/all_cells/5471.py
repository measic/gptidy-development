def k_n_m(xn, xm, thetas):
    k = thetas[0] * np.exp(-thetas[1]/2 * np.linalg.norm(xn-xm)**2) + thetas[2] + thetas[3]*xn * xm
    
    return k