# Lista que armazenará as acurácias de teste durante o treinamento.
test_acc = []

# Variável utilizada para manter o controle de qual a maior acurácia
# encontrada até então.
max_acc = 0

# Inicializamos a Session do Tensorflow
with tf.Session() as sess:
    
    # Chamamos a função que efetivamente inicializa as variáveis criadas.
    sess.run(tf.global_variables_initializer())
    
    # Vamos treinar a rede por 100 épocas
    for epoch in range(100):
        # Cada época é composta de 200 batches de tamanho 100.
        for i in range(200):
            
            # Armazena o batch a ser processado no momento.
            batch = next_batch(100, i)
            
            # Atualiza os pesos da rede.
            train_step.run(feed_dict={x: batch[0], y: batch[1]})
            
            # Mede a acurácia da rede atual e a armazena na lista do
            # histórico.
            test_acc.append(test_accuracy())
            print("Ep {}: Batch #{} - Acc: {}%".format(epoch, i, 100*test_acc[-1]))
            
            # Caso a acurácia atual seja maior que a previamente maior,
            # salvamos os pesos atuais e atualizamos o valor de max_acc.
            if test_acc[-1] > max_acc:
                max_acc = test_acc[-1]
                save_path = saver.save(sess, "./weights/model_e{}b{}_{}.ckpt".format(epoch, i, time.time()))
                print("Model saved in file: %s" % save_path)