import numpy as np
import matplotlib.pyplot as plt

x = np.arange(len(dico))
heights = [elem[1] for elem in sorted_list]
plt.loglog(x, heights)

plt.title("log-log words frequency")
plt.ylabel("Frequency")
plt.xlabel("Index")
plt.show()