def recall(labels, predictions, weights=None):
    conf_matrix = tf.confusion_matrix(labels, predictions, num_classes=3)
    tp_and_fn = tf.reduce_sum(conf_matrix, axis=1)
    tp = tf.diag_part(conf_matrix)
    variable_def = tp / tp_and_fn
    if weights:
        recall_score = tf.multiply(variable_def, weights) / tf.reduce_sum(weights)
    else:
        recall_score = tf.reduce_mean(variable_def)
    return recall_score