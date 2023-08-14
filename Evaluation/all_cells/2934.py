def eval_grads(new_weights):
    sess = tf.Session()
    sess.run(tf.global_variables_initializer())
    variables = TensorFlowVariables(loss, sess)
    variables.set_weights(new_weights)
    grads = {}
    for g, v in grads_and_vars:
        grads[v.name] = sess.run(g, feed_dict={input_layer : x0.T})
        # print(str(sess.run(g, feed_dict={input_layer : x0.T})) + " - " + v.name)
    sess.close()
    return grads

def process_weights(w):
    nw = dict()
    nw['fc1/kernel'] = w['fc1/weights']
    nw['fc1/bias'] = w['fc1/biases']
    nw['fc_out/kernel'] = w['fc_out/weights']
    nw['fc_out/bias'] = w['fc_out/biases']
    return nw        

def flatten_grads(g):
    arr = np.array([])
    arr = np.append(arr, g['fc1/kernel:0'])  # weights
    arr = np.append(arr, g['fc1/bias:0'])
    arr = np.append(arr, g['fc_out/kernel:0'])  # weights
    arr = np.append(arr, g['fc_out/bias:0'])
    return arr

def full(iteration):
    true_grad = flatten_grads(eval_grads(process_weights(iteration['weights'])))
    return np.corrcoef(true_grad, iteration['grad'])