def recall(labels, predictions, weights=None):
    variable_def = tf.confusion_matrix(labels, predictions, num_classes=3)
    tp_and_fn = tf.reduce_sum(variable_def, axis=1)
    tp = tf.diag_part(variable_def)
    recall_scores = tp / tp_and_fn
    if weights:
        recall_score = tf.multiply(recall_scores, weights) / tf.reduce_sum(weights)
    else:
        recall_score = tf.reduce_mean(recall_scores)
    return recall_score