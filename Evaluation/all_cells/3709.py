print("predictions:", predictions)
print("-" * 20)
print(tf.reduce_sum(predictions, axis=-1))