def next_batch(size, i):
    # Recorta o bloco i de tamanho size de labels do
    # conjunto de treinamento.
    l = train_labels[i*size:(i+1)*size]
    
    # Prepara os vetores que viram a ser one-hot.
    # Um para cada exemplo do batch.
    onehot = np.zeros((len(l),51))
    
    # Itera sobre as labels, marcando 1 na posição
    # correta de cada vetor one-hot.
    for j, idx in enumerate(l):
        onehot[j][idx] = 1
        
    # Recorta os vetore de entrada do conjunto de
    # treinamento.
    k = train_data[i*size:(i+1)*size]
    
    # Retorna os vetores e labels correspondentes do
    # batch.
    return k, onehot.astype(float)