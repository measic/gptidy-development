# plot the function and the derivative for the activations sigmoid, tanh and ReLU.
import numpy as np
from scipy.special import expit
import matplotlib.pyplot as plt

n = 100
xs = np.linspace(-3, 3, n)
ReLu = np.maximum(xs,0)
d_ReLu = np.concatenate((np.zeros(int(n/2)), np.ones(int(n/2))))

tanh = np.tanh(xs)
d_tanh = 1- tanh**2

sig = expit(xs)
d_sig = sig*(1- sig)

plt.figure(figsize=(20,5))
# plot ReLu:
plt.subplot(1,3, 1)
plt.plot(xs, ReLu, label = 'ReLu')
plt.plot(xs, d_ReLu, label = 'd_Relu')
plt.xlabel('x')
plt.ylabel('y')
plt.title("ReLu(x) Plot")
plt.ylim(-1.1, 1.1)
plt.legend()

# plot tanh:
plt.subplot(1,3,2)
plt.plot(xs, tanh, label = 'tanh')
plt.plot(xs, d_tanh, label = 'd_tanh')
plt.xlabel('x')
plt.ylabel('y')
plt.title("tanh(x) Plot")
plt.ylim(-1.1, 1.1)
plt.legend()

# plot sigmoid:
plt.subplot(1,3,3)
plt.plot(xs, sig, label = 'sigmoid')
plt.plot(xs, d_sig, label = 'd_sigmoid')
plt.xlabel('x')
plt.ylabel('y')
plt.title("Sigmoid(x) Plot")
plt.ylim(-1.1, 1.1)
plt.legend()
    
plt.suptitle('Activation functions')
plt.show()