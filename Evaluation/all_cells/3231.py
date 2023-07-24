for i in range(250):
    w = update_nueron(w, X[i%X.shape[0], :], y[i%X.shape[0]])