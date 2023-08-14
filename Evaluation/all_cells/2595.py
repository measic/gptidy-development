import tensorflow as tf
import numpy as np
import edward as ed
import os
import matplotlib.pyplot as plt
import time
import seaborn as sns
from edward.models import Categorical, Dirichlet, InverseGamma, Normal, MultivariateNormalDiag, Mixture, Empirical, ParamMixture
%env THEANO_FLAGS=device=cpu,floatX=float32
import theano
import pymc3 as pm
import theano.tensor as tt
%matplotlib inline
plt.style.use('ggplot')
plt.rcParams["axes.grid"] = False
import warnings
warnings.filterwarnings('ignore')