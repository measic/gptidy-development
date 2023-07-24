def forecast(model, batch_size, row):
    X = row[0:-1]
    X = X.reshape(1, 1, len(x))
    yhat = model.predict(X, batch_size=batch_size)
    return yhat[0, 0]