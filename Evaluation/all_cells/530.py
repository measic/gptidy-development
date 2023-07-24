# Find responsible neuron
resp_neuron = np.argmax(np.abs(diag_classifier.coef_))
print(resp_neuron)