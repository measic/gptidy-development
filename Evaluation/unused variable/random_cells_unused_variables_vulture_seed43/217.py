# Get the predictions on the entire dataset
logits = model.predict(X)
preds = tf.argmax(logits, axis=1)