import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import rc
plt.style.use('classic')
rc('font', **{'family': 'DejaVu Sans', 'serif': ['Computer Modern'], 'size':15})
rc('figure', facecolor='w')
import astropy.io.fits as fits
from astropy.nddata import Cutout2D
import math, os
from scipy.stats import poisson
from legacy import plotImg

#optional dependencies
from distutils.spawn import find_executable

if find_executable('latex'): rc('text', usetex=True)
else: rc('text', usetex=False)
    
try: from natsort import natsorted
except: pass