def r2(labels, predictions):
    mean_labels = tf.reduce_mean(labels)
    variable_def = tf.reduce_sum((labels - mean_labels) ** 2)
    residual_sum_squares = tf.reduce_sum((labels - predictions) ** 2)
    r2_score = 1 - residual_sum_squares / variable_def
    return r2_score
preds = model.predict(X)
r2_score = r2(y, preds)
print('R2 score: ', r2_score.numpy())