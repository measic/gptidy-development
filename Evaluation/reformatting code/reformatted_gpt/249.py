def make_input_fn(df, num_epochs):
    return tf.estimator.inputs.pandas_input_fn(
        x=df,
        y=df[LABEL],
        batch_size=128,
        num_epochs=num_epochs,
        shuffle=True,
        queue_capacity=1000,
        num_threads=1
    )