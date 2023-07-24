%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import IPython
from scipy.stats import norm
from abc import ABCMeta, abstractmethod
from sys import version 
import multiprocessing
from numpy import ceil, mean
import time
import os

print ' Reproducibility conditions for this notebook '.center(90,'-')
print 'Python version:     ' + version
print 'Numpy version:      ' + np.__version__
print 'IPython version:    ' + IPython.__version__
print 'Multiprocessing:    ' + multiprocessing.__version__
print '-'*90