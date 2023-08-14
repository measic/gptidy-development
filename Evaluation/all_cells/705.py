# Devemos especificar o dispositivo que vai rodar as operações da rede.
with tf.device("/device:GPU:0"):
    # As variáveis x e y são placeholders para os vetores de entrada e
    # labels (classes) respectivamente.
    x = tf.placeholder(tf.float32, shape=[None, 31])
    y = tf.placeholder(tf.float32, shape=[None, 51])

    # W1 é a matriz que vai levar o input para um estado intermedirário
    # de processamento da rede.
    # b1 é o vetor responsável pela translação nesse novo espaço.
    W1 = tf.get_variable("W1", shape=[31, 64], initializer=tf.contrib.layers.xavier_initializer())
    b1 = tf.Variable(tf.zeros([64]), name="b1")
    
    # A variável layer1 armazena o valor da primeira camada da rede. Isso
    # significa que layer1 utiliza W1 e b1, bem como uma função de ativação
    # (não-linearidade) para computar o valor da primeira camada da rede.
    layer1 = tf.nn.relu(tf.matmul(x,W1) + b1)
    
    # Analogamente, W2 e b2 serão utilizados para gerar a segunda camada da
    # rede (camada final).
    W2 = tf.get_variable("W2", shape=[64, 51], initializer=tf.contrib.layers.xavier_initializer())
    b2 = tf.Variable(tf.zeros([51]), name="b2")

    
    # A variável y_ armazena a última camada da rede utilizando W2 e b2 para
    # calculá-la.
    y_ = tf.matmul(layer1,W2) + b2

    # Aplicamos o softmax em y_ e definimos como função de custo a cross-entropy.
    # O tensorflow tem uma versão otimizada para realizar essas operações em uma
    # única função (o que ajuda a reduzir o tempo de treino).
    cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=y_))

    # Por fim, definimos o otimizador como o Adam.
    train_step = tf.train.AdamOptimizer().minimize(cross_entropy)