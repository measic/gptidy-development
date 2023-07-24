import numpy as np
import matplotlib.pyplot as plt

N1 = 20
m1 = [1, 1]
cov1 = np.diag([0.2, 0.3])

N2 = 30
m2 = [3, 3]
cov2 = np.diag([0.1, 0.3])

X1 = np.random.multivariate_normal(m1, cov1, N1)
X2 = np.random.multivariate_normal(m2, cov2, N2)

plt.scatter(X1[:, 0], X1[:, 1], color='blue')
plt.scatter(X2[:, 0], X2[:, 1], color='green')
plt.title("Synthetic separable data")
plt.show()