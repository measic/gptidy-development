import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import tensorflow as tf
import cv2


%matplotlib notebook
# Increase size of plots
plt.rcParams['figure.figsize'] = (9.0, 5.0)


# Helpers
from ocr.helpers import implt
from ocr.mlhelpers import TrainingPlot, DataSet
from ocr.imgtransform import coordinates_remap
from ocr.datahelpers import loadGapData, correspondingShuffle
from ocr.tfhelpers import Graph, create_cell

tf.reset_default_graph()
sess = tf.InteractiveSession()

print("OpenCV: " + cv2.__version__)
print("Numpy: " + np.__version__)
print("TensorFlow: " + tf.__version__)