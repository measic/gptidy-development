def function_def(w, x, label):
    """
    Update McCulloch + Pitts Nueron using Rosenblatt's Perceptron Algorithms
    w = neuron weights
    x = (n dimensional numpy array example)
    label = binary label
    """
    if neuron(x, w) == 0 and label == 1:
        w = w + x
        print('incorrect!, New weights = ' + str(w))
    elif neuron(x, w) == 1 and label == 0:
        w = w - x
        print('incorrect!, New weights = ' + str(w))
    else:
        print('correct!')
    return w