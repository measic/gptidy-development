# Lista que armazenará o custo ao longo do treino para cada usuário.
test_loss = {user:[] for user in users}

# Lista que armazenará as acurácias ao longodo treino para cada usuário.
test_accuracies = {user:[] for user in users}

# Definimos uma taxa de aprendizado para o Gradient Descent.
learning_rate = 1e-3

# Treinamos uma regressão linear de cada vez.
for user in users:
    # Treinaremos por 100 épocas.
    for epoch in range(100):
        # Cada época é composta por 200 batches de tamanho 100.
        for vs, ls in next_batch(100, user):
            # Testamos o desempenho do modelo atual para guardar no histórico.
            acc, predictions = test_accuracy(user, W[user], b[user])
            
            # Armazenamos a acurácia atual.
            test_accuracies[user].append(100* acc)
            
            # Armazenamos o custo atual.
            test_loss[user].append(calc_loss(predictions, (test_labels == user).astype(np.float64)))
            print("User: {} - Ep: {} - Acc: {}% - Loss: {}".format(user, epoch, test_accuracies[user][-1], test_loss[user][-1]))
            
            # Calculamos os gradientes para realizar o Gradient Descent.
            dW, db = backward_pass(vs, ls, W[user], b[user])
            
            # Atualizamos os pesos e baises do modelo.
            W[user] -= dW * learning_rate
            b[user] -= db * learning_rate