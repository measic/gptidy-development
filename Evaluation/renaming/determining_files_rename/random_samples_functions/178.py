def function_def():
    feature_placeholders = {'is_male': tf.placeholder(tf.string, [None]), 'mother_age': tf.placeholder(tf.float32, [None]), 'plurality': tf.placeholder(tf.string, [None]), 'gestation_weeks': tf.placeholder(tf.float32, [None])}
    features = {key: tf.expand_dims(tensor, -1) for key, tensor in feature_placeholders.items()}
    return tf.estimator.export.ServingInputReceiver(features, feature_placeholders)