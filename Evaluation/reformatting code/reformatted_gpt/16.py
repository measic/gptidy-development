import numpy as np
import matplotlib.pyplot as plt

B = np.ones((3, 3))
plt.imshow(B, interpolation='nearest', cmap=plt.cm.gray)
plt.plot(1, 1, 'or')
plt.gca().set_xlim(-1, 3)
plt.gca().set_ylim(-1, 3)