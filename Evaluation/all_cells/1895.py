import os, time
import numpy as np
import scipy.sparse
import h5py
import matplotlib.pyplot as plt
%matplotlib inline

# Import auto-encoder definition.
%run -n auto_encoder.ipynb
#import auto_encoder

# Profiling.
%reload_ext memory_profiler
%reload_ext line_profiler
import objgraph

#%load_ext autoreload
#%autoreload 2

toverall = time.time()