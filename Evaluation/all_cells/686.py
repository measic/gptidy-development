#Especifica que dispositivo rodará a computação
with tf.device("/device:CPU:0"):
    
    # Cria uma variável (placeholder) cujos valores serão posteriormentes preenchidos
    # com os dados do dataset. Essa variável armazena os dados na dimensão original.
    x = tf.placeholder(tf.float32, shape=[None, 31])

    
    # Definimos a primeira camada da rede aqui
    # A variável encoder_W1 é a matriz de pesos que leva o dado original em 31D para a
    # representação intermediária em 20D.
    # A variável encoder_b1 é somada à representação em 20D para permitir a translação
    # nesse novo espaço.
    encoder_W1 = tf.get_variable("e_W1", shape=[31, 20], initializer=tf.contrib.layers.xavier_initializer())
    encoder_b1 = tf.Variable(tf.zeros([20]), name="e_b1")

    # A variável embedding_20D efetivamente utiliza encoder_W1 e encoder_b1 para calcular
    # a representação do vetor em espaço 20D.
    embedding_20D = tf.nn.relu(tf.matmul(x, encoder_W1) + encoder_b1)

    
    # De forma semelhante à camada anterior, as variáveis encoder_W2 e encoder_b2 levam
    # o vetor 20D para o espaço 2D desejado.
    encoder_W2 = tf.get_variable("e_W2", shape=[20, 2], initializer=tf.contrib.layers.xavier_initializer())
    encoder_b2 = tf.Variable(tf.zeros([2]), name="e_b2")

    # A variável embedding_2D armazena a representação em 2D do nosso dado original
    # convertendo a representação intermediária em 20D para a final em 2D.
    embedding_2D = tf.matmul(embedding_20D, encoder_W2) + encoder_b2
    
    # A variável embedding_2D_activated passa a representação em 2D do vetor por uma função
    # de ativação para dar prosseguimento ao resto da rede (reconstrução do dado original).
    embedding_2D_activated = tf.nn.sigmoid(embedding_2D)

    
    # Queremos agora voltar com as dimensões do dado representado em 2D. Para isso, de forma
    # parecida com a parte de compressão da rede, utilizaremos decoder_W1 e decoder_b1 para
    # levar o vetor 2D a um espaço intermediário em 20D.
    decoder_W1 = tf.get_variable("d_W1", shape=[2, 20], initializer=tf.contrib.layers.xavier_initializer())
    decoder_b1 = tf.Variable(tf.zeros([20]), name="d_b1")

    # A variável reconstruction_20D armazena a reconstrução no espaço intermediário 20D.
    reconstruction_20D = tf.nn.relu(tf.matmul(embedding_2D_activated, decoder_W1) + decoder_b1)

    # Por fim, as variáveis decoder_W2 e decoder_b2 fazem a reconstrução final dos dados.
    decoder_W2 = tf.get_variable("d_W2", shape=[20, 31], initializer=tf.contrib.layers.xavier_initializer())
    decoder_b2 = tf.Variable(tf.zeros([31]), name="d_b2")

    # A variável reconstruction_31D guarda a reconstrução feita pelo decoder e idealmente
    # representa o dado original do dataset.
    reconstruction_31D = tf.matmul(reconstruction_20D, decoder_W2) + decoder_b2

    # Utilizamos o erro quadrado médio como métrica de custo da rede.
    loss = tf.reduce_mean(tf.pow(x - reconstruction_31D, 2))

    # A variável train_step é responsável por fazer uma atualização de pesos através de
    # backpropagation.
    train_step = tf.train.AdamOptimizer(learning_rate=0.00001).minimize(loss)