import pickle, os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
%matplotlib inline

from cv_paper_plots import accuracy, slope, analysis

from cv_paper_plots.style import letter_fontstyle, subject_labels

from importlib import reload

import scipy.stats as stats
from statsmodels.formula.api import ols
from statsmodels.graphics.gofplots import qqplot