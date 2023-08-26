def IRLS(data):
    length        = len(data)
    not_converged = True
    w             = np.array([0, 0, 0])
    p             = np.empty(length)
    s             = np.empty(length)
    z             = np.empty(length)

    ones          = np.ones(200)
    ones[100:]    = ones[100:]*-1
    
    temp_var      = np.hstack((ones[None].T,data))
    np.random.shuffle(temp_var)
    
    y             = temp_var[:,0]
    data          = temp_var[:,1:]
    print(data.shape)
    
    while not_converged:
        w_prev = w
        for i in range(length):
            p[i] = np.exp(w_prev.dot(data[i])) / (1 + np.exp(w_prev.dot(data[i])))
            s[i] = p[i]*(1-p[i])
            
            if math.isnan(s[i]): s[i]=1
            
            z[i] = w_prev.dot(data[i]) + (y[i]-p[i])/(max(s[i],0.00001))
            
        diag_s = np.diag(s)
#         print('diag:', diag_s.shape)
        t1     = np.linalg.inv(np.dot(np.dot(data.T, diag_s), data))
        t2     = np.dot(np.dot(data.T, diag_s), z)
        w      = np.dot(t1, t2)
#         print("t1, t2",t1.shape, t2.shape)
        w      = w/np.linalg.norm(w)
        
        print('Iterations',w)
        
        if abs(sum(w-w_prev)) < 0.000001:
            
            print("Converged!!")
            not_converged = False
            return w
            
        elif sum(abs(w)) > 900 or math.isnan(w[0]):
            
            print("Not converging!!!")
            return w
            
    return w