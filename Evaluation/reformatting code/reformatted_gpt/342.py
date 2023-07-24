def next_batch(size, user):
    # Retorna um batch retirado do conjunto de treino.
    # A cada vez que a função é chamada, um novo batch
    # é retornado até todo o dataset ser coberto.
    for i in range(train_data.shape[0] // size):
        l = (train_labels[i * size:(i + 1) * size] == user).astype(np.float64)
        k = train_data[i * size:(i + 1) * size]
        yield k, l