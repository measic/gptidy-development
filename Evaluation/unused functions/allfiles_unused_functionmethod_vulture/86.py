def GPC(x_new, x, y, kernel, theta):
    K, KS, KSS = get_Ks(x_new, x, kernel, theta)     #+
    
    f, y_giv_f = find_f(K, y)                        #-
    W = util.calculate_W(f, y)              #-
    KP = util.calculate_KP(K, W)                     #-

    f_bar = np.matmul(np.matmul(KS, np.linalg.inv(K)), f) #-    
    var = KSS - KS.dot(np.linalg.inv(KP).dot(KS.T))  #-
    var = np.diagonal(var)                           #-
    return(f_bar.squeeze(), var.squeeze())           #-
