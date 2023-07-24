# EJERCICIO 1. 
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np

X_dev, X_eval, y_dev, y_eval = train_test_split(X, y, stratify=y, test_size=0.10)

display("#### Data Split ####")
display(y_dev['output'].value_counts())
display(y_eval['output'].value_counts())

display("#### 0/1 frequency ratio ####")

display("## dev ##")
display(y_dev['output'].value_counts()[0] / y_dev['output'].value_counts()[1])

display("## eval ##")
display(y_eval['output'].value_counts()[0] / y_eval['output'].value_counts()[1])

# Distribucion de los X de evaluacion
plt.figure(figsize=(5, 3))
plt.hist(np.array(X_eval))
plt.show()

# Distribucion de los X de entrenamiento
plt.figure(figsize=(5, 3))
plt.hist(np.array(X_dev))
plt.show()