def sigmoid(x, derivative=False):
    # Definimos o sigmoid e dua derivada na mesma função para facilitar
    # seu uso.
    if derivative:
        s = sigmoid(x)
        return s * (1-s)
    return 1/(1 + np.exp(-x))