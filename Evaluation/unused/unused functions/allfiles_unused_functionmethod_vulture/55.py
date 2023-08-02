def test_accuracy():
    
    # Diz para o Tensorflow utilizar a GPU para realizar os cálculos
    # seguintes.
    with tf.device("/device:GPU:0"): 
        # Cada tf.argmax tem a função de escolher a posição do vetor
        # com maior probabilidade de ser a classe certa. O parâmetro
        # 1 passado na segunda posição indica o eixo no qual realizar
        # a operação. Dessa forma temos uma classe por exemplo do
        # batch.
        # Chamamos tf.equal para avaliar, a cada posição do vetor, se
        # os valores são iguais. Ou seja, se a previsão da rede é a
        # mesma da classe real.
        hits_and_misses = tf.equal(tf.argmax(y_,1), tf.argmax(y,1))
        
        # Convertemos o array de valores booleanos para valores
        # numéricos. False mapeia para 0 e True para 1. Dessa forma,
        # ao tirarmos a média do vetor, usando tf.reduce_mean, teremos
        # a acurácia de acertos do batch em questão.
        accuracy = tf.reduce_mean(tf.cast(hits_and_misses, tf.float32))
        
        # No código acima apenas criamos o grafo computacional que irá
        # calcular tudo que queremos. Chamando a função eval,
        # efetivamente obtemos o valor numérico desejado.
        # Retornamos esse valor.
        return accuracy.eval(feed_dict={x: test_data, y: test_labels_one_hot})