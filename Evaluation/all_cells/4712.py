%matplotlib inline
# python libraries
from multiprocessing import cpu_count
from sklearn.manifold import TSNE
import sys
import pandas as pd

from sklearn import decomposition, svm, preprocessing, metrics
from sklearn.utils import class_weight
from sklearn.mixture import GaussianMixture
from keras.utils import to_categorical
from keras.models import load_model

from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())

# custom libraries
base_dir = '/raid/home/cwendl'  # for guanabana
sys.path.append(base_dir + '/SIE-Master/Code')  # Path to density Tree package
from helpers.helpers import *
from helpers.data_augment import *
from helpers.data_loader import *
from helpers.parameter_search import *
from helpers.plots import *
from baselines.helpers import *
from density_forest.density_forest import *
from density_forest.helpers import *
from keras_helpers.unet import *
from keras_helpers.callbacks import *