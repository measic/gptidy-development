for op in (X, y, accuracy, training_op):
    tf.add_to_collection("my_important_ops", op)