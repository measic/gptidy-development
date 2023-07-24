# Import TensorFlow and TensorFlow Eager
import tensorflow as tf
import tensorflow.contrib.eager as tfe

# Import functions to generate toy classication problems
from sklearn.datasets import load_wine
from sklearn.datasets import make_classification
from sklearn.datasets import make_regression

# Import numpy for data preprocessing
import numpy as np

# Import library for plots
import matplotlib.pyplot as plt
%matplotlib inline

# Import PCA for dimensionality reduction
from sklearn.decomposition import PCA