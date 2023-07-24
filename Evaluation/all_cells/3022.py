score = model.evaluate(x_val, y_val, batch_size=batch_size)
model.reset_states()
y_hat = model.predict(x_val, batch_size=batch_size)
model.reset_states()