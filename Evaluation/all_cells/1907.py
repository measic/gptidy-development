%matplotlib inline
import numpy
import matplotlib.pyplot as plt
import time
import numpy as np
from sys import getsizeof
from math import exp, log
import os
import random
import string
from tqdm import tqdm

from cuckoofilter import CuckooFilter
from cuckoofilter import CountingBloomFilter
from collections import defaultdict

try:
    import seaborn as sns
    sns.set(context='notebook', style='darkgrid',  font='sans-serif', font_scale=1)
except ImportError: #proceed anyway even if user does not have seaborn. 
    pass