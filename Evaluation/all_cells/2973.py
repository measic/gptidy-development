import os
import sys
import time
import json
import h5py
import random
import itertools
import numpy as np
import pandas as pd
from pandas.plotting import table

import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.colors import Normalize
from mpl_toolkits.axes_grid1 import make_axes_locatable

%matplotlib inline

from IPython.display import SVG
# from keras import backend as K
from keras.models import Sequential
from keras.models import Model
from keras.layers import Activation
from keras.layers import Input
from keras.layers import Dense
from keras.layers import Conv1D
from keras.layers import Add
from keras.layers import LSTM
from keras.layers import Reshape
from keras.layers import Masking
from keras.layers import BatchNormalization
from keras.layers import TimeDistributed
from keras.callbacks import ModelCheckpoint
from keras.callbacks import CSVLogger
from keras.preprocessing.sequence import pad_sequences
from keras.utils.vis_utils import model_to_dot
from keras.utils.vis_utils import plot_model
from keras.utils.np_utils import to_categorical

from mixsig.mixed import MixedSignal
from mixsig.mixed import SignalGenerator
from mixsig.utils import reversed_recombined_holt_winters
from mixsig.plot_utils import plot_confusion_matrix