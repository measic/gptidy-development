from datetime import datetime

import time
import os
import sys
from pathlib import Path

import numpy as np
from scipy.stats import lognorm
import pandas as pd

from astropy import stats
from astropy.io import fits
from astropy.time import Time
import astropy.units as u

import matplotlib
#matplotlib.use('nbagg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import seaborn as sns
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

config = tf.ConfigProto(
    intra_op_parallelism_threads=5,
    inter_op_parallelism_threads=5,
    allow_soft_placement=True,
    log_device_placement=True,
    device_count = {'CPU': 5}
)
sess = tf.Session(config=config)

np.random.seed(42)

print(tf.__version__)