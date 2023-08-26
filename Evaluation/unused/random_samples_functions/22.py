def forward_pass(x, W, b):
    # Calcula a classe baseado em um vetor de pesos e um escalar de víes
    # Note que nessa função aceitam-se matrizes para W e vetores para b,
    # afinal estamos trabalhando com batches e não com um exemplo de
    # cada vez.
    z = x.dot(W) + b
    y_ = sigmoid(z)
    return y_, z