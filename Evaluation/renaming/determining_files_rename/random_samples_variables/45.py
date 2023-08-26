variable_def = len(flower_classes)
with tf.name_scope('new_output_layer'):
    flower_logits = tf.layers.dense(prelogits, variable_def, name='flower_logits')
    Y_proba = tf.nn.softmax(flower_logits, name='Y_proba')