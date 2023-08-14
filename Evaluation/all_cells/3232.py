from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from datetime import datetime
import os.path
import shutil
import sys

from PIL import Image
from resizeimage import resizeimage
import tensorflow as tf
from tensorflow.python.framework import graph_util
from tensorflow.python.platform import gfile