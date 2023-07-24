def loss_function(real, pred):
    # This time, the mask considers positions in the sequence that are not equal to 0 as 1, and the rest as 0
    mask = tf.math.logical_not(tf.math.equal(real, 0))
    # Calculate cross entropy for all positions but do not sum them
    loss_ = loss_object(real, pred)
    mask = tf.cast(mask, dtype=loss_.dtype)
    loss_ *= mask  # Calculate loss only for non-<pad> positions

    return tf.reduce_mean(loss_)