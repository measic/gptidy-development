def calc_loss(y, y_):
    # Calcula cross-entropy usando y como resposta real e y_ como previsão
    return np.mean(-y * np.log(y_ + 1e-8) - (1-y) * np.log(1-y_ + 1e-8))