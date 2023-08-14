import quandl
import numpy as np
import pandas as pd
import seaborn as sns

from IPython import display
from matplotlib import style
from matplotlib import colors
from matplotlib import pyplot as plt
from scipy import optimize as opt

pd.options.display.max_rows = 10
pd.options.display.float_format = "{:.2f}".format
style.use('fivethirtyeight')
np.random.seed(4200)

%matplotlib inline
%config InlineBackend.figure_format = 'retina'