for op in tf.get_default_graph().get_operations():
    print(op.name)