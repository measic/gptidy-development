import tensorflow as tf
import numpy as np
from sklearn.utils import shuffle
X_train_normal = np.array(X_train / 255 - 0.5)
X_valid_normal = np.array(X_valid / 255 - 0.5)
X_test_normal = np.array(X_test / 255 - 0.5)
variable_def = 15
BATCH_SIZE = 128