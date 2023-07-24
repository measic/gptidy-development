import numpy as np
import matplotlib.pyplot as plt

# Integrand function
H = 0
def f(x, H):
    return (x - 5) * np.exp(-(x / 2 - 3)) + H

x = np.arange(2, 10, 0.1)
plt.plot(x, f(x, H), 'b')
plt.show()