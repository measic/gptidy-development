### Preprocess the data here. It is required to normalize the data. Other preprocessing steps could include 
### converting to grayscale, etc.
### Feel free to use as many code cells as needed.
import tensorflow as tf
import numpy as np
from sklearn.utils import shuffle
# import cv2

# for img in X_train:
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
X_train_normal = np.array(X_train/255 - 0.5)
X_valid_normal = np.array(X_valid/255 - 0.5)
X_test_normal = np.array(X_test/255 - 0.5)

EPOCHS = 15
BATCH_SIZE = 128