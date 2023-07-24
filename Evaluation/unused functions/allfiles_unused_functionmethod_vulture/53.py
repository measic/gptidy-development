def test_accuracy(user, W, b):
    # Função que mede a acurácia do modelo em um conjunto de teste.
    predictions = forward_pass(test_data, W, b)[0]
    accuracy = np.mean((predictions > 0.5) == (test_labels == user))
    return accuracy, predictions