import numpy as np
import os
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)
import plotly.graph_objs as go
from visiprog.data import read_viewing_conditions, polar_to_euclidean, read_img_list
from IPython.display import display, HTML