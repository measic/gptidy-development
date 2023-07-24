# invert differenced value
def inverse_difference(history, yhat, interval=1):
    return yhat + history[-interval]