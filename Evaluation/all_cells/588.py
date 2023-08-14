import sys
import os

import pandas as pd
import numpy as np

from datetime import datetime
from math import cos, radians

%matplotlib inline

# Path to support scripts 
sys.path.insert(0,os.path.abspath('/home/pyne-user/Dropbox/UCB/Computational_Tools/Scripts/Python/DataAnalysis'))
from DataManipulation import bin_differentiation, normAUBC
from DataIO import read_delimited_data_file
from Histograms import Histogram

sys.path.insert(0,os.path.abspath('/home/pyne-user/Dropbox/UCB/Computational_Tools/Scripts/Python/Unfolding'))
from HEPROW import readMTX, readGru, readFlu
from Root import FluxNormalization

sys.path.insert(0,os.path.abspath('/home/pyne-user/Dropbox/UCB/Computational_Tools/Scripts/Python/GeneralNuclear'))
from Detectors import nonparalyzable_beam_dead_time, nonparalyzable_dead_time
from MCNP import read_tally