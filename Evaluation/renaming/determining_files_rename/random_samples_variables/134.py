def r2(labels, predictions):
    mean_labels = tf.reduce_mean(labels)
    total_sum_squares = tf.reduce_sum((labels - mean_labels) ** 2)
    variable_def = tf.reduce_sum((labels - predictions) ** 2)
    r2_score = 1 - variable_def / total_sum_squares
    return r2_score
preds = model.predict(X)
r2_score = r2(y, preds)
print('R2 score: ', r2_score.numpy())