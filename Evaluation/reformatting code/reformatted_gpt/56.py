# Utilizaremos a variável losses para armazenar os custos ao longo do treinamento.
losses = []

# min_loss guardará o custo do melhor conjunto de pesos até agora.
# Utilizaremos isso para decidir quando salvarmos os pesos.
min_loss = float("inf")

# Inicializamos uma sessao do tensorflow para podermos utilizar as variáveis criadas
# anteriormente.
with tf.Session() as sess:
    
    # Essa função efetivamente chama a inicialização das variáveis criadas.
    # As inicializa de acordo com as especificações na declaração.
    sess.run(tf.global_variables_initializer())
    
    # Vamos treinar a rede por 100 épocas.
    # Cada época é uma passagem completa pelo conjunto de treino.
    for epoch in range(100):
        # Como o conjunto de treino é composto de 20000 exemplos, faremos o
        # treinamento em 200 batches de tamanho 100 cada um.
        for i in range(200):
            
            # Utilizamos nossa função para pegar o próximo batch
            batch = next_batch(100, i)
            
            # Atualizamos os pesos da rede ao executar train_step.
            # Em seguida pegamos o valor de custo atual para
            # armazenamento e comparação futura.
            _, current_loss = sess.run([train_step, loss], feed_dict={x: batch})
            
            # Armazenamos a loss desse batch
            losses.append(current_loss)

            print("Ep {}: Batch #{} - Loss: {}".format(epoch, i, losses[-1]))
            
            # Caso o custo atual seja menor que a menor até então, encontramos 
            # pesos melhores para a rede, e portanto devemos salvá-los
            if losses[-1] < min_loss:
                # Atualizamos o valor do melhor custo 
                min_loss = losses[-1]
                
                # Salvamos os pesos da rede em um arquivo
                save_path = saver.save(sess, "./weights_autoencoder_no_final_relu/model_e{}b{}_{}.ckpt".format(epoch, i, time.time()))
                print("Model saved in file: %s" % save_path)