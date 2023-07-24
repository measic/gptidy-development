def backward_pass(x, y, W, b):
    # Responsável por calcular as derivadas parciais para W e b.
    # Funciona com batches também, nesse caso retornando a média
    # dos gradientes.
    y_, z = forward_pass(x, W, b)
    dLdb = (-y/(y_ + 1e-8) + (1-y)/(1-y_ + 1e-8)) * sigmoid(z, True)
    dLdW = np.zeros((dLdb.shape[0], 31))
    for i, el in enumerate(dLdb):
        dLdW[i] = x[i] * el
    dLdW = np.mean(dLdW, axis=0)
    dLdb = np.mean(dLdb, axis=0)
    return dLdW, dLdb