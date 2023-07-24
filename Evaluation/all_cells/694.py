# Para não deixar o gráfico visualmente poluido, faremos o plot apenas
# dos dados de 4 usuários.
plot_points_31D = {"s005":[], "s010":[], "s011":[], "s016":[]}
plot_points_2D = {"s005":[], "s010":[], "s011":[], "s016":[]}
for i, point in enumerate(norm_keystrokes):
    if recordings[i][0] in vis_users:
        plot_points_31D[recordings[i][0]].append(point)

# Novamente, para acessar os valores das variáveis do tensorflow,
# precisamos iniciar uma Session.
with tf.Session() as sess:
    # Restaura os pesos relativos ao menor custo encontrado durante o treinamento.
    # Isso garante que estamos usando o melhor conjunto de pesos encontrados e não
    # o último.
    saver.restore(sess, "./weights_autoencoder_no_final_relu/model_e99b118_1516716900.9840117.ckpt")
    print("Model restored.")
    
    # Para cada usuário, armazena as coordenadas em 2D de cada ponto seu.
    for user in plot_points_31D:
        points_31D = np.array(plot_points_31D[user])
        points_2D = sess.run(embedding_2D, feed_dict={x:points_31D})
        plot_points_2D[user] = points_2D

# Configura parâmetros do gráfico e o desenha na tela.
plt.figure(figsize=(10,10))
for user in plot_points_2D:
    plt.scatter(plot_points_2D[user][:,0], plot_points_2D[user][:,1], c=colors[user])
plt.title("Dados de digitação dos usuários {} (Autoencoder)".format(", ".join(vis_users)))
plt.show()